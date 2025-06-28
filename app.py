"""
Activate virtual environment using: venv\Scripts\activate

packages for hosting:
pip install gunicorn
pip freeze > requirements.txt

check for versions of Flask and packages versions compatible for render platform:
(venv) C:\UAT_MS\MS587 - Databases and Web Development\SQLite-Lib-of-the-unseen>pip freeze
blinker==1.9.0
click==8.2.1
colorama==0.4.6
Flask==3.1.1
gunicorn==23.0.0
itsdangerous==2.2.0
Jinja2==3.1.6
MarkupSafe==3.0.2
packaging==25.0
pyodbc==5.2.0
Werkzeug==3.1.3

especially: 
Flask==2.3.3
gunicorn==20.1.0


"""

from flask import Flask, redirect, render_template, request, url_for
import sqlite3

app = Flask(__name__)

# SQLite database path
database_path = 'database.db'

# Home page route


@app.route('/')
def home():
    return render_template('index.html')

# Books page route - fetch content from SQLite database


@app.route('/books')
def books():
    try:
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        # ✅ FIX: Removed dbo. prefix (SQLite does not use it)
        cursor.execute("""
            SELECT b.Title, a.AuthorName, b.image, b.preview, b.story
            FROM Books b
            JOIN Authors a ON b.AuthorID = a.AuthorID
        """)
        rows = cursor.fetchall()

        books = []
        for row in rows:
            book_id = row[0]
            cursor.execute(
                "SELECT CommentText FROM Comments WHERE BookID = ?", (book_id,))
            comments = [comment[0] for comment in cursor.fetchall()]

            books.append({
                "id": book_id,
                "title": row[0],   # SQLite returns tuples
                "author": row[1],
                "image": row[2],
                "preview": row[3] if row[3] else "",
                "story": row[4] if row[4] else "",
                "book_id": row[0].replace(" ", "-").lower(),
                "comments": comments
            })

        conn.close()
        return render_template('books.html', books=books)

    except Exception as e:
        return f"Database connection error: {e}"

# Comment submission route


@app.route('/add_comment', methods=['POST'])
def add_comment():
    book_id = request.form['book_id']
    comment_text = request.form['comment_text']

    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Comments (BookID, CommentText) VALUES (?, ?)", (book_id, comment_text))
    conn.commit()
    conn.close()

    return redirect(url_for('books'))


if __name__ == '__main__':
    app.run(debug=True)

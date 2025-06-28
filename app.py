

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

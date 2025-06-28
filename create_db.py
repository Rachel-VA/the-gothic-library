import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Create Authors table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Authors (
    AuthorID INTEGER PRIMARY KEY AUTOINCREMENT,
    AuthorName TEXT NOT NULL
)
''')

# Create Books table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Books (
    BookID INTEGER PRIMARY KEY AUTOINCREMENT,
    Title TEXT NOT NULL,
    AuthorID INTEGER,
    image TEXT,
    preview TEXT,
    story TEXT,
    FOREIGN KEY (AuthorID) REFERENCES Authors (AuthorID)
)
''')

# Create Comments table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Comments (
    CommentID INTEGER PRIMARY KEY AUTOINCREMENT,
    BookID INTEGER,
    CommentText TEXT NOT NULL,
    FOREIGN KEY (BookID) REFERENCES Books (BookID)
)
''')
cursor.execute('DELETE FROM Comments')
cursor.execute('DELETE FROM sqlite_sequence WHERE name="Comments"')

# Optional: Clear old data and reset primary keys
cursor.execute('DELETE FROM Books')
cursor.execute('DELETE FROM sqlite_sequence WHERE name="Books"')
cursor.execute('DELETE FROM Authors')
cursor.execute('DELETE FROM sqlite_sequence WHERE name="Authors"')

# Insert sample authors
authors = [
    ("Eleanor Blackwood",),
    ("Gideon Frost",),
    ("Seraphina Dusk",),
    ("Thorne Ashcroft",)
]

cursor.executemany("INSERT INTO Authors (AuthorName) VALUES (?)", authors)

# Book data list
books = [
    (
        "The Silent Watcher",
        1,
        "1.jpeg",
        "Everyone in town whispered about the house on the hill. The window on the third floor always held a shadow that never moved. Clara couldn’t resist the urge to find out who—or what—was watching from within.",
        """The house had stood empty for decades, its shutters clinging by rusted hinges and ivy swallowing the stone walls. The stories of a silent watcher in the attic window had passed from generation to generation. No one dared step inside after dark, but Clara’s curiosity outweighed her fear.

One rainy evening, with only a lantern to guide her, she crossed the crumbling porch and climbed the grand staircase. Each step creaked beneath her weight, echoing through the hollow halls as though the house exhaled with every movement. The closer she drew to the attic door, the louder the silence became.

When she reached the dusty attic, her lantern flickered. Across the room, the shadow slowly turned to face her—a figure not of flesh, but memory. Clara realized the watcher had not been guarding the house—it had been waiting for her return. The house had always been hers, and now, so was the shadow."""
    ),
    (
        "Whispers in the Walls",
        2,
        "2.jpeg",
        "Eliza moved into her grandmother’s home, where the walls seemed to whisper at night. The voices called her name, pulling her deeper into memories she didn’t know she had. The house felt strangely alive, like it had been waiting for her.",
        """At first, Eliza thought the whispers were nothing more than creaking floorboards and settling walls. But the words became clear—soft voices murmuring stories she never remembered hearing. As the days passed, the house began to feel familiar, as if it recognized her more than she recognized herself.

Driven by the whispers, Eliza began peeling back layers of old wallpaper. Beneath them, she discovered scribbled drawings, faded handwriting, and diary entries—some written in her own handwriting though she had never been there before. It was as if the walls themselves had been waiting to reveal a story only she could finish.

Late one night, she followed the whispers into a forgotten room sealed behind an old bookcase. There, she found a letter addressed to her, signed with her grandmother’s name. The house had been speaking to its own blood, guiding Eliza to uncover the life she had unknowingly left behind."""
    ),
    (
        "The Lantern's Curse",
        3,
        "3.jpeg",
        "In the fog-covered marsh, a mysterious lantern glowed each night, luring travelers to follow. The old villagers warned that no one who chased its light ever returned. Jacob ignored their warnings and set out to find his missing brother.",
        """In the quiet hours before dawn, Jacob stepped into the marsh, guided by the soft glow of the distant lantern. His brother’s disappearance had left a silence in his home that only answers could fill. The fog thickened with every step, but the lantern’s glow remained steady.

Villagers claimed the light belonged to a soul trapped long ago, forever wandering the swamp. As Jacob drew closer, the skeletal hands holding the lantern came into view, and the silence around him collapsed into a deafening heartbeat.

He reached for the lantern, but the ground beneath him gave way, swallowing him into the marsh’s cold grip. The light flickered for a moment and then steadied. Another lost soul now carries the lantern through the mist, waiting for the next seeker."""
    ),
    (
        "The Forgotten Library",
        4,
        "4.jpeg",
        "Hidden behind thick ivy, Lily discovered a forgotten library that appeared only under the full moon. The dusty books seemed to whisper her name and open themselves to stories she had never written. Yet, each story knew her intimately.",
        """Lily had always believed stories were written by their authors, but the books in this ancient library knew otherwise. Their cracked spines and yellowed pages held tales about her life—events she had never spoken aloud. She soon realized that the library had been watching her, recording her every moment.

Compelled by the pull of unfinished stories, she spent nights leafing through the volumes, uncovering memories and future pages already written. Every story ended with a door—one that she could not recall ever opening.

On the final night, the library door closed behind her as she turned the last page. Her story ended with her disappearance, but new books began to whisper again, already writing about the next curious soul who might find their way in."""
    ),
    (
        "The Crimson Mirror",
        1,
        "5.jpeg",
        "Sophia found an antique mirror that promised her a life of perfection. Each day, her reflection seemed more alive, more independent. One morning, it smiled at her when she was no longer smiling back.",
        """Sophia purchased the mirror at a dusty market, drawn to its intricate frame and its glass that shimmered unnaturally. At first, it reflected her as she wished to be—graceful, confident, untouchable. But the longer she gazed, the more her reflection seemed to move when she did not.

The mirror began to show her a world where she was admired and adored, but the cost was never mentioned. Her reflection’s smiles lingered longer than her own, and its gestures became independent of her movements.

One morning, the reflection stepped forward and passed through the glass, taking Sophia’s place in the world. On the other side, Sophia’s hands pressed against the cold barrier, her voice silenced forever as the mirror watched her from the other side."""
    ),
    (
        "Beneath the Staircase",
        2,
        "6.jpeg",
        "Evelyn heard soft scratching beneath the staircase every night. No one else believed her, but the whispers calling her name became impossible to ignore. She finally opened the wooden steps to find the truth.",
        """Each night, the sound of scratching beneath the stairs grew louder, but her family dismissed it as the house settling. Evelyn knew better. The voice whispering her name was no hallucination.

Driven by curiosity and fear, she pried open the wooden steps, uncovering a narrow crawl space she never knew existed. A tiny wooden door sat at the end of the passage, waiting, unlocked.

When she crawled inside, the door closed behind her, sealing her fate. Evelyn was gone, but the scratching remained. A new voice whispered from beneath the stairs, waiting for the next listener to hear."""
    ),
    (
        "The Frostbound Grimoire",
        3,
        "7.jpeg",
        "Gideon found a magical book sealed in solid ice, buried deep in a forgotten vault. No flame could thaw it, yet it called to him in his dreams. The grimoire waited for a soul foolish enough to break its seal.",
        """The grimoire’s pages were frozen shut, but Gideon’s hands melted the frost as though it had been waiting for him. Each spell he uncovered promised more power, more answers. But the last spell was incomplete.

The book whispered to him, begging him to finish the incantation. As he read aloud the final line, his surroundings vanished, and a searing cold swallowed him whole.

His soul was bound to the pages, his story forever trapped in the grimoire’s icy grip. Now the book waits again, its frost thin and ready to crack for the next reader who dares to touch it."""
    ),
    (
        "The Ashen Doll",
        4,
        "8.jpeg",
        "No matter how many times Mara burned the doll, it always reappeared on her windowsill, untouched by flame. Its glassy eyes seemed to grow wider each morning. The doll was no longer waiting to be accepted—it was claiming her.",
        """Mara threw the doll into the fire again and again, watching it char and crumble, but each morning it returned—its glass eyes unblinking, its stitched mouth stretching wider.

Each night, the doll appeared closer to her bed, and each morning, Mara found it resting beside her pillow. It whispered to her now, soft words of comfort she never heard from anyone else.

On the final night, Mara hugged the doll tightly and whispered, 'You win.' When her parents entered the room the next morning, only the doll remained—its new glass eyes hauntingly familiar."""
    ),
    (
        "Shadows in the Garden",
        1,
        "9.jpeg",
        "The garden’s fog at night revealed shifting shadows that no one dared follow. Theo, tempted by their silent invitation, stepped into the mist. He vanished beyond the hedges, leaving only whispers behind.",
        """The garden bloomed with impossible beauty, but the shadows lurking in the fog moved with intent. Theo often watched them from his window, curiosity tugging at his heart.

One evening, unable to resist, he followed the soft rustling beyond the hedges. The fog thickened, and the shadows gathered around him, their forms dark and incomplete.

Theo was never seen again. But each night, a new shadow appears in the garden—one that watches from the same place Theo once stood, waiting for someone else to join the dance."""
    ),
    (
        "The Hollow Portrait",
        2,
        "10.jpeg",
        "The portrait’s hollow-eyed figure seemed to breathe as visitors passed by. The longer Victor stared, the more the painted man seemed to watch him. He felt an unshakable pull to touch the canvas.",
        """Victor found the portrait in a locked attic, its colors faded but its hollow eyes sharp. Something about the painting’s subject felt alive—too alive.

Each time Victor returned, the figure’s expression changed, its eyes following him closer. He could no longer tell if the portrait was a painting or a window.

When he finally touched the canvas, Victor’s body crumpled to the floor. His soul had crossed into the painting, where he now blinks from the other side, forever watching those who dare to stare too long."""
    ),
    (
        "The Phantom’s Lullaby",
        3,
        "11.jpeg",
        "A lullaby echoed softly through the abandoned orphanage, its melody sweet but unsettling. Anna followed the ghostly song, drawn to the haunting tune that no one else could hear. The lullaby led her somewhere she could not return from.",
        """Anna heard the lullaby each night from the upper floors of the orphanage, though the rooms above had been empty for years. The melody was soft, sweet, and strangely familiar.

One night, she followed the song up the winding staircase, the air growing colder with each step. The door creaked open to a room where no one stood, but the lullaby continued.

Anna’s voice soon joined the melody, blending perfectly into the ghostly tune. Though the orphanage now stands silent, those who pass by at night still hear the lullaby—sung by a voice that no longer belongs to this world."""
    ),
    (
        "The Bloodbound Bell",
        4,
        "12.jpeg",
        "The village bell had not rung for centuries. The elders warned that its toll would awaken something buried deep beneath the square. When the bell rang on its own, the ground trembled and the sky darkened.",
        """The ancient bell was bound by chains, its tongue silenced by the fears of generations. No one knew who first sealed it, but everyone knew why—it was never meant to ring again.

One morning, without wind or hand, the bell tolled. Its sound echoed through the streets, and the ground beneath the village square began to crack.

Something ancient stirred below as the bell’s tolls grew louder, summoning what had long been buried. When the villagers fled, the bell kept ringing, calling out to no one, to everyone, to whatever had finally awakened."""
    )

]

# Insert books
cursor.executemany("""
INSERT INTO Books (Title, AuthorID, image, preview, story)
VALUES (?, ?, ?, ?, ?)
""", books)

conn.commit()
conn.close()

print('✅ Database and all 12 books created successfully!')

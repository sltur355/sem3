import sqlite3


def init_db():
    conn = sqlite3.connect('bot_db.sqlite')
    cursor = conn.cursor()

    # Создание таблицы для хранения общего числа
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS state (
            id INTEGER PRIMARY KEY,
            value INTEGER NOT NULL
        )
    ''')

    # Создание таблицы для хранения истории команд
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            command TEXT NOT NULL
        )
    ''')

    # Инициализация общего числа, если оно отсутствует
    cursor.execute('SELECT * FROM state')
    if cursor.fetchone() is None:
        cursor.execute('INSERT INTO state (value) VALUES (0)')

    conn.commit()
    conn.close()


def get_value():
    conn = sqlite3.connect('bot_db.sqlite')
    cursor = conn.cursor()

    cursor.execute('SELECT value FROM state WHERE id = 1')
    value = cursor.fetchone()[0]

    conn.close()
    return value


def update_value(new_value):
    conn = sqlite3.connect('bot_db.sqlite')
    cursor = conn.cursor()

    cursor.execute('UPDATE state SET value = ? WHERE id = 1', (new_value,))

    conn.commit()
    conn.close()


def add_to_history(user_id, command):
    conn = sqlite3.connect('bot_db.sqlite')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO history (user_id, command) VALUES (?, ?)', (user_id, command))

    conn.commit()
    conn.close()


def get_history():
    conn = sqlite3.connect('bot_db.sqlite')
    cursor = conn.cursor()

    cursor.execute('SELECT user_id, command FROM history')
    history = cursor.fetchall()

    conn.close()
    return history

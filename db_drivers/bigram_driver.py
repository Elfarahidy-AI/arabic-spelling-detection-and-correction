import sqlite3

class BigramDB:
    def __init__(self, db_name):
        self.db_name = db_name
        self.create_table()

    def create_table(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS bigram
                     (key TEXT PRIMARY KEY, value TEXT)''')
        conn.commit()
        conn.close()

    def store_bigram(self, bigram):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        for key, value in bigram.items():
            c.execute("SELECT value FROM bigram WHERE key = ?", (key,))
            row = c.fetchone()
            if row:
                # Key exists, update the frequencies
                value_dict = eval(row[0])
                for word, freq in value.items():
                    if word in value_dict:
                        value_dict[word] += freq
                    else:
                        value_dict[word] = freq
                value_str = str(value_dict)
                c.execute("UPDATE bigram SET value = ? WHERE key = ?", (value_str, key))
            else:
                # Key doesn't exist, insert a new row
                value_str = str(value)
                c.execute("INSERT INTO bigram (key, value) VALUES (?, ?)", (key, value_str))
        conn.commit()
        conn.close()

    def load_bigram(self):
        bigram = {}
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("SELECT key, value FROM bigram")
        rows = c.fetchall()
        for row in rows:
            key = row[0]
            value_str = row[1]
            value = eval(value_str)
            bigram[key] = value
        conn.close()
        return bigram

    def get_frequency(self, prev_word, current_word):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("SELECT value FROM bigram WHERE key = ?", (prev_word,))
        row = c.fetchone()
        conn.close()
        if row is None:
            return 0
        if row:
            value_str = row[0]
            value = eval(value_str)
            if current_word in value:
                return value[current_word]
        return 0

    def print_first_three_entries(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("SELECT key, value FROM bigram LIMIT 3")
        rows = c.fetchall()
        conn.close()
        print("First three entries in the database:")
        for row in rows:
            key = row[0]
            value_str = row[1]
            value = eval(value_str)
            print(f"Key: {key}")
            print(f"Value: {value}")
            print("---")
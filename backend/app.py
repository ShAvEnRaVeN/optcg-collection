from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

DB = 'data/cards.db'

def get_db_connection():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/api/sets")
def api_get_sets():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT set_name FROM sets')
    rows = cursor.fetchall()
    conn.close()
    sets = [row['set_name'] for row in rows]
    return jsonify(sets)
    

@app.route("/paulspage")
def paulspage():
    return f"paul is wanting to play borderlands 3. he is mad"

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

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
    

@app.route("/api/OP01")
def api_get_OP01():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT name, num FROM OP01')
    rows = cursor.fetchall()
    conn.close()
    cards = [{'name': row['name'], 'num': row['num']} for row in rows]
    return jsonify(cards)

if __name__ == "__main__":
    app.run(debug=True)
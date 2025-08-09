from flask import Flask, jsonify, send_from_directory, abort
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
    

@app.route("/api/<set_name>")
def api_get_set(set_name):
    allowed_sets = {"OP01", "OP02", "OP03"}  # whitelist your allowed tables here

    if set_name not in allowed_sets:
        abort(404, description="Set not found")

    conn = get_db_connection()
    cursor = conn.cursor()
    query = f"SELECT * FROM {set_name}"  # safe because of whitelist check
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()

    cards = [dict(row) for row in rows]
    return jsonify(cards)

@app.route("/data/images/<path:filename>")
def serve_images(filename):
    return send_from_directory('data/images', filename)

if __name__ == "__main__":
    app.run(debug=True)
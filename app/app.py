from flask import Flask, jsonify
from db import app, db
from sqlalchemy import text

@app.route("/")
def home():
    try:
        # Ejecuta una consulta simple para testear la conexión
        with db.engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            return jsonify({"status": "ok", "db": [row[0] for row in result]})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


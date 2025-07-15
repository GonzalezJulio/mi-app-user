import os
import psycopg2
from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host=os.environ["DB_HOST"],
        port=os.environ["DB_PORT"],
        dbname=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASS"]
    )

@app.route("/")
def home():
    return jsonify({"message": "Hola, esta es mi app Flask desplegada con Docker y PostgreSQL"})

@app.route("/health")
def health():
    try:
        conn = get_db_connection()
        conn.close()
        db_status = "OK"
    except Exception as e:
        db_status = f"ERROR: {str(e)}"

    return jsonify({
        "status": "OK",
        "timestamp": datetime.utcnow().isoformat(),
        "database": db_status,
        "message": "¡Mi aplicación Flask está funcionando! 🎉"
    })

@app.route('/health')
def health_check():
    return jsonify({
        "status": "OK",
        "timestamp": datetime.utcnow().isoformat(),
        "message": "¡Mi aplicación está funcionando! 🎉"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

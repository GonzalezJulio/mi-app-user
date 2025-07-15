import logging
from flask import request

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger()

@app.before_request
def log_request():
    logger.info(f"{request.method} {request.path}")

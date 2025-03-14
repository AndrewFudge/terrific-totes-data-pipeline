import os

from pg8000.native import Connection
from dotenv import load_dotenv


load_dotenv()


def connect_to_db():
    """Deprecated - only use locally
    Connects to the 'totesys' database using PG8000,
    and environment variables using Python Dotenv."""
    return Connection(
        user=os.getenv("PG_USER"),
        password=str(os.getenv("PG_PASSWORD")),
        database=os.getenv("PG_DATABASE"),
        host=os.getenv("PG_HOST"),
        port=int(os.getenv("PG_PORT"))
    )


def close_connection(db):
    db.close()

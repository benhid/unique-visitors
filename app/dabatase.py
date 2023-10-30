import os

from databases import Database

DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite://")

database = Database(DATABASE_URL)


def get_db() -> Database:
    """
    Get the database connection.

    :return: The database connection.
    """
    return database

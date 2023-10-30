import os

from databases import Database

DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite://")

database = Database(DATABASE_URL)

hits_table_stmt = """
CREATE TABLE IF NOT EXISTS unique_hits (
    id      INTEGER PRIMARY KEY,
    set     hll
);
INSERT INTO unique_hits(id, set) VALUES (1, hll_empty()) ON CONFLICT DO NOTHING;
"""

hits_agg_stmt = "SELECT hll_cardinality(set) FROM unique_hits WHERE id = 1;"

hits_add_stmt = (
    "UPDATE unique_hits SET set = hll_add(set, hll_hash_text(:client_id)) WHERE id = 1;"
)


def get_db() -> Database:
    """
    Get the database connection.

    :return: The database connection.
    """
    return database

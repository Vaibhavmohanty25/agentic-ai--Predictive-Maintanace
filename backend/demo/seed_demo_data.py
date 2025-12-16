import os
from app.core.db import get_db, DB_PATH


def reset_database():
    """
    Clears all demo tables and resets state.
    """

    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

    # Recreate schema by reinitializing DB
    from app.core.db import init_db
    init_db()

    print("✅ Demo database reset.")


if __name__ == "__main__":
    reset_database()

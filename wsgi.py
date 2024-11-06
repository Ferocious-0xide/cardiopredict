# wsgi.py
from app import create_app
from app.database.db_operations import init_db

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        # Initialize database
        init_db()
    app.run()
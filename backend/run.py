import sys
from pathlib import Path

# Add the parent directory to sys.path
sys.path.append(str(Path(__file__).parent))

from app import create_app,db

app = create_app()
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

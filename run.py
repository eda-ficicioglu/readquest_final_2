# run.py

from app import create_app, db
from app.models import User, TestResult, SavedBook

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'TestResult': TestResult, 'SavedBook': SavedBook}

if __name__ == '__main__':
    app.run(debug=True)
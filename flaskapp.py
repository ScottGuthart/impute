from app import create_app, db
from app.models import User

app = create_app()

if __name__ == '__main__':
    app.run(use_debugger=False, use_reloader=False, passthrough_errors=True)

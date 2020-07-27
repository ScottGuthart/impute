from app import create_app, db
from app.models import User, Task

app = create_app()

if __name__ == '__main__':
    app.run(use_debugger=False, use_reloader=False, passthrough_errors=True)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Task': Task}

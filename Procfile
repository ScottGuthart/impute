web: flask db upgrade; gunicorn flaskapp:app
worker: rq worker -u $REDIS_URL flaskapp-tasks
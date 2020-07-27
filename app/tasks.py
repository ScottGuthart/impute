import sys
from missingpy import MissForest
import numpy as np
from rq import get_current_job
from app import create_app, db
from app.models import User, Task

app = create_app()
app.app_context().push()


def _set_task_progress(progress):
    job = get_current_job()
    if job:
        job.meta['progress'] = progress
        job.save_meta()
        task = Task.query.get(job.get_id())
        # task.user.add_notification('task_progress', {'task_id': job.get_id(),
        #                                              'progress': progress})
        if progress >= 100:
            task.complete = True
            db.session.commit()


def _set_task_result(result):
    job = get_current_job()
    if job:
        job.meta['result'] = result.tolist()


def floatify(x):
    try:
        return float(x)
    except ValueError:
        return np.nan


def run_impute(user_id, data):
    try:
        _set_task_progress(0)
        data = [[floatify(x) for x in row]
                for row in data]
        imputer = MissForest()
        imputed = imputer.fit_transform(data)
        _set_task_result(imputed)
        _set_task_progress(100)

    except:
        _set_task_progress(100)
        app.logger.error('Unhandled exception', exc_info=sys.exc_info())

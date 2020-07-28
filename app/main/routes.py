import os
import json
from flask import render_template, request, jsonify
from flask_login import login_required, current_user
from app import db
from app.main import bp
from app.main.save_user_file import utc_to_human_readable
from app.auth.confirm import check_confirmed
from app.models import Task


@bp.route('/')
@bp.route('/index')
@login_required
@check_confirmed
def index():
    return render_template('index.html')


@bp.route('/request_impute', methods=['GET', 'POST'])
@login_required
@check_confirmed
def request_impute():
    if current_user.get_task_in_progress('run_impute'):
        return 'An impute request is currently running'
    else:
        raw_data = json.loads(request.data)
        task = current_user.launch_task('run_impute', 'Impute', raw_data)
        db.session.commit()
        return task.id
    # imputed = run_impute(raw_data)
    # return jsonify(imputed)


@bp.route('/check_task_result/<task_id>', methods=['GET'])
@login_required
@check_confirmed
def check_task_result(task_id):
    task = Task.query.filter_by(user=current_user, id=task_id).first()
    job = task.get_rq_job()
    if task and task.complete and job:
        result = job.meta['result']
        return jsonify(result)
    elif task and not task.complete:
        return jsonify([task.get_progress()])
    else:
        return "Error finding task"


@bp.app_template_filter("autoversion")
def autoversion_filter(filename):
    # determining fullpath might be project specific
    fullpath = os.path.join("app/", filename[1:])
    try:
        timestamp = utc_to_human_readable(os.path.getmtime(fullpath), True)
    except OSError:
        print(f"couldn't find {filename}")
        return filename
    newfilename = "{0}?v={1}".format(filename, timestamp)
    # print(f"returning {newfilename}")
    return newfilename

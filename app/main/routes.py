import os
import json
import numpy as np
from missingpy import MissForest
from flask import render_template, request, jsonify
from flask_login import login_required
from app.main import bp
from app.main.save_user_file import utc_to_human_readable
from app.auth.confirm import check_confirmed


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
    raw_data = json.loads(request.data)
    data = [[float(x) if x.isnumeric() else np.nan for x in row]
            for row in raw_data]
    imputer = MissForest()
    X_imputed = imputer.fit_transform(data)

    return jsonify(X_imputed.tolist())


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
    print(f"returning {newfilename}")
    return newfilename

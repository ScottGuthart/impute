from app.main import bp
from flask import render_template
from flask_login import login_required
from app.auth.confirm import check_confirmed

@bp.route('/')
@bp.route('/index')
@login_required
@check_confirmed
def index():
    return render_template('index.html')

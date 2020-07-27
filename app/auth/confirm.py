from functools import wraps
from itsdangerous import URLSafeTimedSerializer
from flask_login import current_user
from flask import flash, redirect, url_for, current_app

def check_confirmed(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if not current_user.confirmed:
            flash('Please confirm your account!')
            return redirect(url_for('auth.unconfirmed'))
        return func(*args, **kwargs)
    return decorated_function

def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    return serializer.dumps(email, salt=current_app.config['SECURITY_PASSWORD_SALT'])

def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    try:
        email = serializer.loads(
            token,
            salt=current_app.config['SECURITY_PASSWORD_SALT'],
            max_age=expiration
        )
    except:
        return False
    return email
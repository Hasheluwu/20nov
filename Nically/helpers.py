import requests
from email_validator import validate_email, EmailNotValidError
from flask import redirect, render_template, session
from functools import wraps
import re

def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/latest/patterns/viewdecorators/
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function


def is_valid_email(email):
    try:
        # Validar el correo
        validate_email(email)
        return True
    except EmailNotValidError as e:
        # Retorna False si no es válido
        return False


def is_secure_password(password):
    # Al menos 8 caracteres, un número, una letra mayúscula y un carácter especial
    password_regex = r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    return re.match(password_regex, password) is not None

from flask import abort
from flask_login import current_user, login_required

def permission_required(permission_id):
    def decorator(f):
        @login_required
        def decorated_function(*args, **kwargs):
            if current_user.role.permission_id != permission_id:
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator


def admin_required(f): 
    return permission_required(0)(f)

from flask import abort
from flask_login import current_user, login_required

def post_required(post_name):
    def decorator(f):
        @login_required
        def decorated_function(*args, **kwargs):
            if current_user.post.name != post_name:
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator


def admin_required(f):
    return post_required("admin")(f)

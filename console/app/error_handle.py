from flask import render_template


def error_hand_500(e):
    return render_template('500.html')


def error_hand_404(e):
    return render_template('404.html')


class Ehandle:
    def init_app(self, app):
        app.register_error_handler(500, error_hand_500)
        app.register_error_handler(404, error_hand_404)

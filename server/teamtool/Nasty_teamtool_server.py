from flask_app.app import app


class NastyTeamtoolServer(object):
    def __init__(self):
        self.flask_app = app

    def run(self):
        self.flask_app.run()

if __name__ == '__main__':
    Nasty_teamtool_server = NastyTeamtoolServer()
    Nasty_teamtool_server.run()
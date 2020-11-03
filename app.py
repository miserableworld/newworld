from flask import Flask

from api.create_task import task

app = Flask(__name__)

app.config.from_object('settings.ProjectConfig')


app.register_blueprint(task,url_prefix='/req')


if __name__ == '__main__':
    app.run()

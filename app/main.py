from Flask import flask
import os

app = Flask(__name__)


@app.route("/")
def index():
    return "Welcome!"

@app.route("/env_var")
def env_var():
    """ Dockerfile will read .env file.

    :return: Environment variable named "Key"
    """
    return os.getenv("KEY")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080")
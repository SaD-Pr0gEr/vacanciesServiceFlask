from application import create_app

app = create_app()
from application.views import *


if __name__ == '__main__':
    app.run(debug=True, port=8888)

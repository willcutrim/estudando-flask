from flask import Flask
from routers.routers_user import router_user

app = Flask(__name__)

router_user(app)

if __name__ == '__main__':
    app.run(debug=True)
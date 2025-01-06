import os
from flask import Flask
from flask_migrate import Migrate
from config.database import init_app, db
from routers.routers_user import router_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
migrate = Migrate(app, db)

router_user(app)
init_app(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
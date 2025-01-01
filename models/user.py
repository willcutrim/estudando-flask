from config.database import db
from mixins.serializer_mixin import SerializeMixin

class User(db.Model, SerializeMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.Date, nullable=False)
    is_active = db.Column(db.Boolean, default=True, nullable=False)

    def __init__(self, username, email, created_at):
        self.username = username
        self.email = email
        self.created_at = created_at
    
    def register_user_if_not_exist(self):
        db_user = User.query.filter(User.username == self.username).all()
        if not db_user:
            db.session.add(self)
            db.session.commit()
        
        return True

    def __repr__(self):
        return f"<User {self.username}>"

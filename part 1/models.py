"""Models for Blogly."""

from flask_sqlachemy import SQLAlchemy

db = SQLAlchemy()

class User(db.model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.Text, nullable = False)
    last_name = db.Column(db.Text, nullable = False)
    image = db.Column(db.Text, nullable = False, default=DEFAULT_IMAGE_URL)
    
    @property
    def flnm(own):
        return f"{own.first_name} {own.last_name}"

def connect_db(app)
    db.app = app
    db.init_app(app)
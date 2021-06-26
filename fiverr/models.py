from datetime import datetime
from fiverr import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = 'freelancer'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    user_image_file = db.Column(db.String(20), nullable=False,
                                default='default.jpg')
    is_admin = db.Column(db.Boolean, default=False)
    is_valid = db.Column(db.Boolean, default=True)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}',\
                      '{self.email}',\
                      '{self.user_image_file}')"


class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    post_image_file = db.Column(db.String(20), nullable=False,
                                default='postimg.jpg')
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    category = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('freelancer.id'),
                        nullable=False)

    def __repr__(self):
        return f"Post('{self.title}',\
                      '{self.post_image_file}',\
                      '{self.date_posted},\
                      '{self.content}',\
                      '{self.category}',\
                      '{self.price}')"

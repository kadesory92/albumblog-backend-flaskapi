from app.extensions import db


class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    photos = db.relationship('Photo', backref='album', lazy=True)

    def __repr__(self):
        return f'<Album {self.title}>'

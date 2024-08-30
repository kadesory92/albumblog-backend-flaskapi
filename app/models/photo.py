from app.extensions import db


class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    thumbnailUrl = db.Column(db.String(255), nullable=True)
    album_id = db.Column(db.Integer, db.ForeignKey('album.id'), nullable=False)

    def __repr__(self):
        return f'<Photo {self.title}>'

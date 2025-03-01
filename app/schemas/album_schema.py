from app.extensions import ma
from app.models import Album


class AlbumSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Album
        load_instance = True


album_schema = AlbumSchema()
albums_schema = AlbumSchema(many=True)
from app.extensions import ma
from app.models import Photo


class PhotoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Photo
        load_instance = True


photo_schema = PhotoSchema()
photos_schema = PhotoSchema(many=True)
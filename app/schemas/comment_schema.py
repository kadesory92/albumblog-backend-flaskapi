from app.extensions import ma
from app.models import Comment


class CommentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Comment
        load_instance = True


comment_schema = CommentSchema()
comments_schema = CommentSchema(many=True)
from app.extensions import db
from app.models import User


class UserService:

    @staticmethod
    def createUser(username, email, password):
        new_user = User(username, email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    def get_all_users(self):
        return User.query.all()

    def get_user_by_id(user_id):
        return User.query.get(user_id)

    def get_user_by_username(username):
        return User.query.filter_by(username)


    def delete_user(user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False

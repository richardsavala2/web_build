import uuid
from src.common.database import Database
from flask.sessions import session


class User(object):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    @classmethod
    def get_by_email(cls, email):
        data = Database.find_one('users', {'email': email})
        if data is not None:
            return cls(**data)

    @classmethod
    def get_by_id(cls, _id):
        data = Database.find_one('users', {'email': id})
        if data is not None:
            return cls(**data)


    @staticmethod
    def login_valid(email, password):
        # user.login_valid('user_email@gmail.com', 'password1234')
        # check if email matches password
        user = User.get_by_email(email)
        if user is not None:
            # check password
            return user.password == password
        return False

    @classmethod
    def register(cls, email, password):
        user = User.get_by_email(email)
        if user is None:
            # user doesn't exist, create it
            new_user = User(email, password)
            new_user.save_to_mongo()
            session['email'] = email
            return True
        else:
            # user exists :0
            return False

    @staticmethod
    def login(user_email):
        # login_valid has already been called
        session['email'] = user_email

    @staticmethod
    def logout():
        session['email'] = None

    def get_blogs(self):
        pass

    def json(self):
        return {
            'email': self.email,
            '_id': self._id,
            'password': self.password
        }

    def save_to_mongo(self):
        Database.Insert('user', self.json())





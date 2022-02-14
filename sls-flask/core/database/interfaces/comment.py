from core.database import db


class Comment(db.Document):
    content = db.StringField(required=True, unique=True)
    publish_date = db.DateTimeField(required=True)
    _id = False

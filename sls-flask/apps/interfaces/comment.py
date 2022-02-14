from apps.interfaces import *


class CommentWrite(FlaskForm):
    content = StringField("content", validators=[DataRequired()])

from typing import Union, Tuple
from core.database.interfaces.comment import Comment
from datetime import datetime, timedelta


def write_new_comment(content: str) -> bool:
    """
    Write new comment
    """
    new_comment = Comment(content=content, publish_date=datetime.utcnow())
    success = new_comment.save()
    return success


def read_all_comments():
    """
    Read all comments limit 10 order by publish_date desc
    """
    comments = Comment.objects.order_by("-publish_date").limit(10).only("content")
    return comments

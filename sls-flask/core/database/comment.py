from typing import Union, Tuple
from core.database.interfaces.comment import Comment
from datetime import datetime, timedelta
from settings import MAX_COMMENT_LENGTH


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
    # if comments_count > MAX_COMMENT_LENGTH - 1: remove all comment
    """
    comments = (
        Comment.objects.order_by("-publish_date")
        .limit(MAX_COMMENT_LENGTH)
        .only("content")
    )
    if comments.count() > MAX_COMMENT_LENGTH - 1:
        Comment.objects.delete()
        return {}
    return comments

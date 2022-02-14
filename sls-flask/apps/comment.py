from flask import Blueprint, make_response, jsonify, request
from apps.interfaces.comment import CommentWrite
from core.database.comment import write_new_comment, read_all_comments

comment = Blueprint("comment", __name__, url_prefix="/comments")


@comment.route("", methods=["POST"])
def post_comment():
    """
    Comment
    """
    request_data = request.get_json()
    try:
        body = CommentWrite(meta={"csrf": False})
        if not body.validate():
            return make_response(jsonify(result="Bad Request"), 403)
        content = body.data.get("content", "")
        success = write_new_comment(content)
        if not success:
            return make_response(jsonify(result="DB Error"), 500)
    except Exception as e:
        print(e)
    return make_response(jsonify(result="Success"), 200)


@comment.route("", methods=["GET"])
def get_comment():
    """
    Comment
    """
    comments = read_all_comments()
    return make_response(jsonify(comments=comments), 200)

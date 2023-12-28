from app import app, USERS, models
from flask import Response, request
from http import HTTPStatus


@app.post("/users/create")
def create_user():
    data = request.get_json()
    try:
        user_id = len(USERS)
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
    except KeyError:
        return Response('Data is incorrect', HTTPStatus.BAD_REQUEST)

    if models.User.validate_email_syntax(email):
        response = Response(status=HTTPStatus.BAD_REQUEST)
        return response

    user = models.User(id=user_id, first_name=first_name, last_name=last_name, email=email)
    USERS.append(user)
    response = Response(
        user.model_dump_json(),
        HTTPStatus.OK,
        mimetype="application/json"
    )
    return response


@app.get("/users/<int:user_id>")
def get_user_by_user_id(user_id: int):
    try:
        user = USERS[user_id]
    except IndexError:
        return Response(status=HTTPStatus.NOT_FOUND)

    response = Response(
        user.model_dump_json(),
        HTTPStatus.OK,
        mimetype="application/json"
    )
    return response

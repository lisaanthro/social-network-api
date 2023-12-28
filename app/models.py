from pydantic import BaseModel
import re


class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    total_reactions: int = 0
    posts: list = []

    @staticmethod
    def validate_email_syntax(email):
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, email) is not None



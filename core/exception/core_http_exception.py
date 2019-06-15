from werkzeug.exceptions import HTTPException


class CoreHttpException(HTTPException):
    def __init__(self, code, description):
        self.code = code
        self.description = description

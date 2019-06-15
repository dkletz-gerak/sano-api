from core.exception.core_http_exception import CoreHttpException
from .exception_type import *


class SanoException(CoreHttpException):
    def __init__(
        self, code=500, error_name=GENERAL_EXCEPTION, message="Internal Server Error"
    ):
        super().__init__(code, message)
        self.error_name = error_name

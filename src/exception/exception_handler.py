from .sano_exception import SanoException
from .exception_type import GENERAL_EXCEPTION, NOT_FOUND
from flask import jsonify
import os
import traceback


def handle_general_exception(e: "SanoException"):
    err_message = e.description
    if os.getenv("ENV") == "prod" and e.code >= 500:
        err_message = "Internal server error"
    return (
        jsonify({"message": err_message, "error": e.error_name, "code": e.code}),
        e.code,
    )


def handle_other_exception(e: "Exception"):
    traceback.print_tb(e.__traceback__)
    err_message = str(e)
    if os.getenv("ENV") == "prod":
        err_message = "Internal server error"
    return (
        jsonify({"message": err_message, "error": GENERAL_EXCEPTION, "code": 500}),
        500,
    )


def handle_page_not_found(e):
    return (
        jsonify({"message": str(e), "error": NOT_FOUND, "code": 404}),
        404
    )


def handle_method_not_allowed(e):
    return (
        jsonify({"message": str(e), "error": NOT_FOUND, "code": 405}),
        405
    )

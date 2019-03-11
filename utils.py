from flask import request


def _(v):
    return int(request.form[v])

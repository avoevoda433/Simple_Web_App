from enum import Enum
from functools import wraps
from flask import request, abort
from converter.converter import check_value


class Directions(Enum):
    C2F = 'c2f'
    F2C = 'f2c'


class Elements(Enum):
    DIRECTION = 'direction'
    VALUE = 'input_value'
    WARNING_D = 'Choose a convert direction'
    WARNING_V = 'Input some value for conversion'


class ValidationError(RuntimeError):
    """
    Exception raised for errors in the direction or input value.
    """
    def __init__(self, error_msg):
        self.error_msg = error_msg
        super().__init__(self.error_msg)


def params(func):
    """
    Decorator validate request parameters and if something wrong - throw warning message or error 400.
    Else - it passes the required parameters to func
    """
    @wraps(func)
    def wrapped():
        direction = request.args.get(Elements.DIRECTION.value)
        input_value = request.args.get(Elements.VALUE.value)

        if direction not in tuple(d.value for d in Directions):
            raise ValidationError(error_msg=Elements.WARNING_D.value)
        elif not input_value:
            raise ValidationError(error_msg=Elements.WARNING_V.value)
        elif not check_value(input_value):
            abort(400)
        else:
            return func(direction, input_value)
    return wrapped

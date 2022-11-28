
def c2f_convert(value: float) -> float:
    """
    Convert a celsius temperature value to a fahrenheit
    :param value: temperature value in celsius
    :return: temperature value in fahrenheit
    """
    return round(value * 9 / 5 + 32, 2)


def f2c_convert(value: float) -> float:
    """
    Converts a fahrenheit temperature value to a celsius
    :param value: temperature value in fahrenheit
    :return: temperature value in celsius
    """
    return round((value - 32) * 5 / 9, 2)


def check_value(value: str) -> bool:
    """
    This function checks a convert string value to float opportunity
    :param value: string type value
    :return: True - if a string type value possible convert to float
             False - if a string type value impossible convert to float
    """
    try:
        return isinstance(float(value), float)
    except (TypeError, ValueError):
        return False


converter = {'c2f': c2f_convert,
             'f2c': f2c_convert}

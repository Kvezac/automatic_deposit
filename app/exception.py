class InputDateError(Exception):
    detail = "Format date input is not valid. Expected format: dd.mm.yyyy"
    code = 400

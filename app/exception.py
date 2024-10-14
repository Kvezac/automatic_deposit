class InputDateError(Exception):
    detail = "Date is not correct, valide date dd.mm.yyyy"
    status_code = 400

from datetime import datetime


def div(a, b):
    return float(a) / float(b)


def analyze_pesel(pesel):
    pesel = str(pesel)
    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    weight_index = 0
    digits_sum = 0

    for digit in pesel[:-1]:
        digits_sum += int(digit) * weights[weight_index]
        weight_index += 1

    pesel_modulo = digits_sum % 10
    validate = 10 - pesel_modulo

    if validate == 10:
        validate = 0

    gender = "male" if int(pesel[-2]) % 2 == 0 else "female"
    birth_date = datetime(("19" + pesel[0: 2]) +
                          (pesel[2:4]) + (pesel[4:6]))

    result = {
        "pesel": pesel,
        "valid": validate == (pesel[-1]),
        "gender": gender,
        "birth_date": birth_date
    }

    return result

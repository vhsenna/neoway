# Implement CPF validation logic here
# This is a simplified example
def validate_cpf(cpf):
    cpf = "".join(filter(str.isdigit, cpf))
    if len(cpf) != 11:
        return False
    if cpf == cpf[0] * 11:
        return False

    def calc_digit(cpf, t):
        d = sum(int(cpf[i]) * (t - i) for i in range(t - 1)) % 11
        return 0 if d < 2 else 11 - d

    first_digit = calc_digit(cpf, 10)
    second_digit = calc_digit(cpf, 11)

    return first_digit == int(cpf[9]) and second_digit == int(cpf[10])


# Implement CNPJ validation logic here
# This is a simplified example
def validate_cnpj(cnpj):
    cnpj = "".join(filter(str.isdigit, cnpj))
    if len(cnpj) != 14:
        return False
    if cnpj == cnpj[0] * 14:
        return False

    def calc_digit(cnpj, t):
        if t == 13:
            multipliers = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        else:
            multipliers = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

        s = sum(int(cnpj[i]) * multipliers[i] for i in range(t - 1))
        d = s % 11
        return 0 if d < 2 else 11 - d

    first_digit = calc_digit(cnpj, 13)
    second_digit = calc_digit(cnpj, 14)

    return first_digit == int(cnpj[12]) and second_digit == int(cnpj[13])

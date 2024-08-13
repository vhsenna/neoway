# Implement CPF validation logic here
# This is a simplified example
def validate_cpf(cpf):
    cpf = "".join(filter(str.isdigit, cpf))
    if len(cpf) != 11:
        return False
    if cpf == cpf[0] * 11:
        return False

    def calc_digit(t):
        d = sum((int(cpf[i]) * (t - i) for i in range(t - 1))) % 11
        return 0 if d < 2 else 11 - d

    return calc_digit(10) == int(cpf[9]) and calc_digit(11) == int(cpf[10])


# Implement CNPJ validation logic here
# This is a simplified example
def validate_cnpj(cnpj):
    cnpj = "".join(filter(str.isdigit, cnpj))
    if len(cnpj) != 14:
        return False
    if cnpj == cnpj[0] * 14:
        return False

    def calc_digit(t):
        d = sum((int(cnpj[i]) * ((t - i) % 8 + 2) for i in range(t - 2))) % 11
        return 0 if d < 2 else 11 - d

    return calc_digit(13) == int(cnpj[12]) and calc_digit(14) == int(cnpj[13])

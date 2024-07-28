#VERIFICADOR DE CPF 

cpf = input("Digite os numeros de seu cpf:")

cpf_padrao = cpf[0:9]


def verify_cpfX(cpf_padrao):
    soma_total = 0
    for digito in cpf_padrao:
        multiplicador = 2
        soma = int(digito)  * multiplicador
        multiplicador += 1
        soma_total += soma
    resto = soma_total % 11
    x = 11 - resto
    print(f"Estamos verificando os digitos X sendo ele é {x}")
    return x

cpf_padrao = cpf_padrao + str(verify_cpfX(cpf_padrao))


def verify_cpfY(cpf_padrao):
    soma_total = 0
    cpf_padrao = cpf_padrao[1:10]
    for digito in cpf_padrao:
        multiplicador = 2
        soma = int(digito) * multiplicador
        multiplicador += 1
        soma_total += soma
    resto = soma_total % 11
    y = 11 - resto
    print(f"Estamos verificando os digitos Y sendo ele {y}")
    return y


cpf_padrao = cpf_padrao + str(verify_cpfY(cpf_padrao))
print(f"O teste do cpf será iniciado agora, o cpf calculado é {cpf_padrao}")


def verify_final(cpf_padrao):
    if cpf_padrao == cpf:
        print("Este cpf é válido!")
    elif cpf_padrao != cpf:
        print("CPF invalido seu trouxa!")

print(verify_final(cpf_padrao))

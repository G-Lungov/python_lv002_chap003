# Cálculo de alíquota de IR
def main():
    
    # Investment types
    investment = {
        1: "CDB",
        2: "LCI",
        3: "LCA"
    }
    # Get user input
    select_investment = input("Digite o código do investimento: 1 (CDB), 2 (LCI), 3 (LCA) ")
    # Try to convert user input to integer
    try:
        selected_investment = int(select_investment)
        print("Você selecionou a opção", investment[selected_investment], ".")
    except ValueError:
        print("Por favor insira um número inteiro de 1 a 3. ")

    # Days invested
    days_invested_by_user = input("Quantos dias permaneceu investido o teu dinheiro? ")
    # Try to convert user input to integer
    try:
        days_invested = int(days_invested_by_user)
        print("Número de dias investidos: ", days_invested)
    except ValueError:
        print("Por favor insira um número inteiro válido. ")
    
    # Alíquota percentage base
    tax_base = {
        1: 0.225, # 180 -
        2: 0.20, # 181 a 360
        3: 0.175, # 361 a 720
        4: 0.15 # 721 +
    }
    # Alíquota storage
    aliquota = ()
    aliquota_percentage = (aliquota * 100)
    # Alíquota to be applied
    if days_invested <= 180:
        aliquota += (tax_base[1])
    elif days_invested >= 181 and days_invested <= 360:
        aliquota +=(tax_base[2])
    elif days_invested >= 361 and days_invested <= 720:
        aliquota += (tax_base[3])
    elif days_invested >= 721:
        aliquota += (tax_base[4])
    else:
        print("Algo deu errado, vamos iniciar novamente.")
    
    # Get withdrawal amount
    withdraw_amount = input("Quantia do saque: R$ ")
    # Try to convert user input to integer
    try:
        withdraw = int(withdraw_amount)
        print("A quantia determinada para saque é de: R$ ", withdraw)
    except ValueError:
        print("Não é possível fazer o saque da quantia desejada, por favor tente novamente. ")

    # Check if IR is applicable
    if selected_investment == 1:
        print(f"Será aplicado uma alíquota sobre seu saque de {aliquota_percentage}% . ")
        total_amount = (withdraw - (withdraw * aliquota))
        print(f"A quantia total a ser sacada é de R$ {total_amount} . ")
    else:
        print("Não será aplicado nenhuma alíquota sobre seu saque. ")
        print(f"A quantia total a ser sacada pe de R$ {withdraw} . ")
    
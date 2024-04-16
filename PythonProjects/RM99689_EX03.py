def calculate_loan(debt, interest_rate, num_installments):
    
    # Calculate the total debt with interest
    total_debt = debt * (1 + interest_rate / 100)
    
    # Calculate the value of each installment
    installment_value = total_debt / num_installments

    return total_debt, installment_value

def main():
    
    # Get the value of the debt from the user
    debt = float(input("Digite o valor da dívida: R$ "))

    # Define the options for the number of installments and their corresponding interest rates
    options = {
        1: 0,
        3: 10,
        6: 15,
        9: 20,
        12: 25
    }

    print("Valor da dívida | Valor do juros | Quantidade de parcelas | Valor da parcela")
    
    # Iterate over each option and calculate the loan details
    for num_installments, interest_rate in options.items():
        total_debt, installment_value = calculate_loan(debt, interest_rate, num_installments)
        print(f"Total: R$ {debt:.2f} Juros: R$ {interest_rate}% Número de parcelas: {num_installments} Valor da parcela R$ {installment_value:.2f}")
main()

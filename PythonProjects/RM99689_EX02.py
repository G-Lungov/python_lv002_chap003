def calculate_price_with_discount(car_price):
    # Calculate the final price with a 20% discount for cash payment
    return car_price * 0.8

def calculate_installment_price(final_price, num_installments, interest_rate):
    # Calculate the installment price with the given interest rate
    total_price_with_interest = final_price * (1 + interest_rate)
    return total_price_with_interest / num_installments

def main():
    # Get the price of the car from the user
    car_price = float(input("Digite o preço do carro: R$ "))

    # Calculate the final price with a 20% discount for cash payment
    final_price = calculate_price_with_discount(car_price)
    print(f"O preço final à vista com desconto de 20% é: R$ {final_price:.2f}")

    # Define the installment options and their corresponding interest rates
    installments = {
        6: 0.03,
        12: 0.06,
        18: 0.09,
        24: 0.12,
        30: 0.15,
        36: 0.18,
        42: 0.21,
        48: 0.24,
        54: 0.27,
        60: 0.3
    }

    # Print the table of installment options
    print("\nTabela de parcelamento:")
    print("{:<10} {:<25} {:<20}".format("Parcelas", "Preço da Parcela", "Preço Final"))
    for num_installments, interest_rate in installments.items():
        installment_price = calculate_installment_price(final_price, num_installments, interest_rate)
    
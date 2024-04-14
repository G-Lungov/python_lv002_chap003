def main():
    
    # Days of the week conuter
    votes = {
        "segunda-feira": 0,
        "terça-feira": 0,
        "quarta-feira": 0,
        "quinta-feira": 0,
        "sexta-feira": 0
    }

    # Get number of participants to vote
    participants = int(input("Digite a quantidade em números de participantes para a votação: "))

    # Validating last input
    if participants <=0:
        print("Número inválido de colaboradores.")
        return
    
    # Looping through participants
    for i in range(participants):
        print(f"Participante {i+1}:")
        day = input("Digite o dia da semana da sua preferência (segunda-feira, terça-feira, quarta-feira, quinta-feira, sexta-feira): ").lower()

        # Validanting last input
        if day in votes:
            votes[day] +=1
        else:
            print("Dia da semana inválido, tente novamente.")

    # Find day with more votes
    max_votes = max(votes.values())
    chosen_day = [day for day, vote_count in votes.items() if vote_count == max_votes]

    # Print the day with more votes
    if len(chosen_day) == 1:
        print(f"O dia escolhido para a realização das lives é: {chosen_day[0]}")
    else:
        print("Houve um empate entre os seguintes dias:")
        for day in chosen_day:
            print(day)

from art import logo
import random
print(logo)

should_continue = True
while should_continue:

    user_cards = []
    computer_cards = []

    # function to distrubute the card

    def deal_card():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        '''append the card in the user and computer list.'''
        # for n in range(0-1)
        for n in range(2):
            # for user
            user_index = random.randint(0, 12)
            user_cards.append(cards[user_index])
            # for computer
            computer_index = random.randint(0, 12)
            computer_cards.append(cards[computer_index])

    deal_card()
    print(user_cards, computer_cards)

    def add_card(who):
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

        if (who == "user"):
            index = random.randint(0, 12)
            user_cards.append(cards[index])
        elif (who == "comp"):
            index = random.randint(0, 12)
            computer_cards.append(cards[index])

            # function to calculate the card

    def calculate_score(card_lists):
        total = 0
        # calculating the total
        for list in card_lists:
            total += list
        # checking for the blackjack
        if (total == 21 and len(card_lists) == 2):
            return 0
        #
        if 11 in card_lists and total > 21:
            card_lists.remove(11)
            card_lists.append(1)

        return total

    def compare(user_total, computer_total):
        if user_total == computer_total:
            return "Draw 🤗"
        elif computer_total == 0:
            return "You lose, opponent has a blackjack🥺"
        elif user_total == 0:
            return "You win 🥺"
        elif user_total > 21:
            return "You lose🥺, you went over"
        elif computer_total > 21:
            return "You win 🥺, opponent went over"
        elif user_total > computer_total:
            return "You win 🥺"
        else:
            return "You lose🥺"

    is_game_over = False
    while not is_game_over:
        user_total = calculate_score(user_cards)
        computer_total = calculate_score(computer_cards)
        print(f"Your cards:{user_cards}, current score: {user_total}")
        print(f"Computer's first card:{computer_cards[0]}")
        # first condition to see the winnner
        if (user_total == 0 or computer_total == 0 or user_total > 21):
            is_game_over = True
        else:
            draw_another_card = input(
                "Do you want to draw another card, yes or no ")
            if (draw_another_card == "yes"):
                add_card("user")

            else:
                is_game_over = True

    while computer_total != 0 and computer_total < 17:
        add_card("comp")
        computer_total = calculate_score(computer_cards)
    print(f"your final hand: {user_cards}, final score:{user_total}")
    print(
        f"computer final hand: {computer_cards}, final score:{computer_total}")
    print(compare(user_total, computer_total))
    if (input("Do you want to continue playing. type yes to continue. ") != "yes"):
        should_continue = False

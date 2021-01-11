import random,art, game_data


# Prints logo
def print_logo():
    print(art.logo)


# Displaying the two options to the user
def show_choices(choice1,choice2):
    print(f"Compare A: {choice1['name']}, a {choice1['description']}, from {choice1['country']}.")
    print(art.vs)
    print(f"Against B: {choice2['name']}, a {choice2['description']}, from {choice2['country']}.")


# Calculating which follower has the most
def more_followers(choice1, choice2):
    if choice1['follower_count'] > choice2['follower_count']:
        return 'a'
    else:
        return 'b'


# Allows the user to make a guess again
def guess():
    return input("Who has more followers? Type 'A' or 'B': ").lower()


# Gets a new random person
def random_person():
    return random.choice(game_data.data)


# Initial startup
person_1 = random_person()
person_2 = random_person()
show_choices(person_1, person_2)
user_guess = guess()

# Keeps track of score
user_score = 0

# If correct_guess is true you can keep playing
correct_guess = True

while correct_guess:

    if user_guess == more_followers(person_1, person_2):
        print_logo()
        user_score += 1
        print(f"You're right! Current score: {user_score}")
        person_1 = person_2
        person_2 = random.choice(game_data.data)

        while person_1 == person_2:
            person_2 = random.choice(game_data.data)

        show_choices(person_1, person_2)
        guess()
    else:
        correct_guess = False
        print_logo()
        print(f"Sorry that's wrong. Final Score: {user_score}")






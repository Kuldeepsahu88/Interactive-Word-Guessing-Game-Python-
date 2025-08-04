import random
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Word lists
easy_words = ["apple", "train", "tiger", "money", "india"]
medium_words = ["python", "bottle", "monkey", "planet", "laptop"]
hard_words = ["elephant", "diamond", "umbrella", "computer", "mountain"]

# Log file
log_file = open("game_log.txt", "a")

# Welcome message
print(Fore.CYAN + "Welcome to the password guessing game!")
print(Fore.CYAN + "Choose a difficulty level: easy, medium or hard")
print(Fore.MAGENTA + "easy: 5-letter words | medium: 6-letter words | hard: 8+ letter words")

level = input(Fore.YELLOW + 'Enter difficulty: ').lower()
log_file.write(f"Selected difficulty: {level}\n")

# Select word
if level == "easy":
    secret = random.choice(easy_words)
elif level == "medium":
    secret = random.choice(medium_words)
elif level == "hard":
    secret = random.choice(hard_words)
else:
    print(Fore.RED + "Invalid choice. Defaulting to easy level.")
    secret = random.choice(easy_words)

print(Fore.BLUE + f"\nThe secret password has {len(secret)} letters.")
print(Fore.BLUE + "You have 10 attempts to guess it.\n")

# Game variables
attempts = 0
max_attempts = 10

while attempts < max_attempts:
    guess = input(Fore.YELLOW + "Enter your guess: ").lower()
    attempts += 1
    log_file.write(f"Attempt {attempts}: {guess}\n")

    if guess == secret:
        print(Fore.GREEN + f'\n🎉 Congratulations! You guessed it in {attempts} attempts.')
        log_file.write(f"Result: Guessed correctly in {attempts} attempts\n")
        break

    # Build hint
    hint = ""
    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i] + " "
        else:
            hint += "_ "

    print(Fore.YELLOW + "Hint: " + hint.strip())
    print(Fore.YELLOW + f"Attempts left: {max_attempts - attempts}\n")
    log_file.write(f"Hint: {hint.strip()}\n")

else:
    print(Fore.RED + f"\n❌ Sorry! You've used all your attempts. The password was '{secret}'.")
    log_file.write(f"Result: Failed. Secret word was '{secret}'\n")

print(Fore.CYAN + "Game over.")
log_file.write("Game over.\n" + "-"*30 + "\n")
log_file.close()

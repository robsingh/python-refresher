#number guessing game
'''
A human player has to guess a number between a range of 1 to n. The player inputs his guess. 
The program informs the player, if this number is larger, smaller or equal to the secret number, 
i.e. the number which the program has randomly created. 
If the player wants to gives up, he or she can input a 0 or a negative number.
'''
'''import random
upper_bound = 20
lower_bound = 1
to_be_guessed = random.randint(lower_bound, upper_bound)
guess = 0
while guess != to_be_guessed:
    guess = int(input("New number: "))
    if guess == 0:
        print("Sorry that you are giving up!")
        break
    if guess < lower_bound or guess > to_be_guessed:
            print("Guess not within the boundaries!")
    elif guess > to_be_guessed:
        upper_bound = guess - 1
        print("Number too large!")
    elif guess < to_be_guessed:
         lower_bound = guess + 1
         print("Number too small!")
else:
    print("Congratulations! You did it.")
'''

#dog to human age convertor -> 0 or a negative value means that they want to finish.
'''dog_age = 1
while dog_age > 0:
    dog_age = int(input("Age of the dog: (0 or negative number to finish)"))
    print()
    if dog_age <= 0:
        human_age = -1
    elif dog_age == 1:
        human_age = 14
    elif dog_age >= 2:
        human_age = 22 + (dog_age - 2) * 5

    print("Corresponds to " + str(human_age) + " human years!")

print("Program finished!")'''


'''
Write a Python program that calculates the factorial of a number entered by the user using a while loop. 
The factorial of a non-negative integer n, denoted in mathematics as n!, is the product of all positive integers from 1 to n. 
For example, 5! (read as "5 factorial") is equal to 5 * 4 * 3 * 2 * 1, which is 120.
'''
# could be done in a single line using recursion too, but we are focusing on 'while' loops here.
'''
n = int(input("Enter a positive integer: "))

factorial = 1
counter = 1

while counter <= n:
    factorial *= counter
    counter += 1

print(f"{n}! = {factorial}")
'''

'''
Write a Python program that simulates a simple password checker. 
The program should ask the user to enter a password and continue to prompt them until they enter the correct password. 
If the user exceeds the maximum number of attempts, the program should lock them out.
Once the correct password is entered, the program should print a success message.
'''
'''saved_password = 'OneLove'
max_attempts = 5
count_attempts = 0

while count_attempts < max_attempts:
    password = input("Enter the password: ")
    if password == saved_password:
            print("Correct Password Entered!")
            break
    else:
        count_attempts += 1
        remaining_attempts = max_attempts - count_attempts
        if remaining_attempts > 0:
             print(f"Incorrect Password. You have {remaining_attempts} attempt(s) left!")
        else:
             print("Maximum attempts exceeded! You are now locked out!")'''

'''
Write a Python program that checks whether a given positive integer is a prime number. 
(a number that can only be divided by itself and 1 without remainders) -> 2,3,5,7,11,13 and so on. 
The program should ask the user to input a number and then use a while loop to determine if the number is prime.
'''

check_prime = int(input("Enter the number to check if it is prime or not: "))
divisor = 1
is_prime = True

while divisor <= check_prime // 2:
    divisor += 1
    if check_prime % divisor == 0 and is_prime:
        is_prime = False
        break

if is_prime:
    print(check_prime, "is a prime number!")
else:
    print(check_prime, "is not a prime number.")

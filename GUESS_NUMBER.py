import random

def secret_num():
    return random.randint(1,100)

def user_case(guess, number):
    if guess == number:
        
        return "Right"
    elif abs(guess - number) <= 10:
        return "Hot"
    else:
        return "Cold"
def case():
    secret = secret_num()
    while True:
        user = int(input("enter the number from range 0 to 100:  "))
        if user < 1 or user > 100 :
            print("enter the correct Number")
            continue
        hint = user_case(secret, user)
        if hint == "Right":
            print(f"You Guessed correct {secret}")
            break
        else:
            print(hint)

if __name__ == '__main__':
    case()            
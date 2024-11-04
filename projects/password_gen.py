
# Password Generator 
import string
import secrets


letters = string.ascii_letters  # all lowercase and uppercase letters
digits = string.digits  # numbers 0-9
symbols = string.punctuation  # special characters


def pass_gen():
    try :
    
        print("Welcome to the password generator!!")
        char = int(input(f"How many letters you want in your password \n > "))

        num = int(input(f"How many numbers you want in your password  \n > "))

        spl_char = int(input(f"How many special chracters you want in your password \n > "))



        print("Your password is in the making ")
          
         # Generates random letters, numbers, and symbols
         # and put them in list to use later without list the random letters will be lost 
         # and it won't be able to generate the password 


        char  = [secrets.choice(letters) for _ in range(char)] 
        num = [secrets.choice(digits) for _ in range(num)]           
        spl_char = [secrets.choice(symbols) for _ in range(spl_char)]     

        password = char + num + spl_char

        secrets.SystemRandom().shuffle(password)    # shuffels the password
         
         # this convert the lis into a string 
        password = "".join(password)
        print(f"Your generated password is \n> {password}")

    except Exception:
        print("Please enter a valid number.")

pass_gen()


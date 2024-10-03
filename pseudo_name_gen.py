import sys, random

print("welcome to the name generator!")


first = ('baby oil', 'bad news', 'big burps') 
last = ('appleyard',  'bigmeat', 'bloomshine')

while True:
    firstname = random.choice(first)
    lastname = random.choice(last)
    print(" Your new silly name is now: {} {} \n\n".format(firstname, lastname), file=sys.stderr)
    try_again = input("Try again? (press enter else n to quit) \n")
    if try_again.lower() == 'n':
        break
input("\n press enter to exit")
    
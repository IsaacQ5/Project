import random
def givename():
    with open("Names.txt", 'w') as f:
        name = ' '
        for i in range(1000):
            names = random.randint(1,2)
            if names == 1:
                name = "Isaac \n"
            else:
                name = "Carmen \n"
            f.write(name)
givename()


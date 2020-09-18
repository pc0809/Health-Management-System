# f1 = open('Rohan-Food.txt')
# f2 = open('Rohan-Exercise.txt')
#
# g1 = open('Harry-Food.txt')
# g2 = open('Harry-Exercise.txt')
#
# h1 = open('Karan-Food.txt')
# h2 = open('Karan-Exercise.txt')

def getdate():
    import datetime
    return str(datetime.datetime.now())


def RetrieveFood():

    if a == 1:
        f1 = open('Rohan-Food.txt', 'r')
        print(f1.read())
        f1.close()

    elif a == 2:
        g1 = open('Harry-Food.txt', 'r')
        print(g1.read())
        g1.close()

    elif a == 3:
        h1 = open('Karan-Food.txt', 'r')
        print(h1.read())
        h1.close()

    else:
        print('Invalid Input!')


def RetrieveExercise():
    if a == 1:
        f2 = open('Rohan-Exercise.txt', 'rt')
        print(f2.read())
        f2.close()

    elif a == 2:
        g2 = open('Harry-Exercise.txt', 'rt')
        print(g2.read())
        g2.close()

    elif a == 3:
        h2 = open('Karan-Exercise.txt', 'rt')
        print(h2.read())
        h2.close()

    else:
        print('Invalid Input!')

def LockFood():
    if a == 1:
        f1 = open('Rohan-Food.txt', 'w')
        f1.write(getdate())
        f1.write('\n')
        f1.write(input('Write Your Food: '))
        f1.close()

    elif a == 2:
        g1 = open('Harry-Food.txt', 'w')
        g1.write(getdate())
        g1.write('\n')
        g1.write(input('Write Your Food: '))
        g1.close()

    elif a == 3:
        h1 = open('Karan-Food.txt', 'w')
        h1.write(getdate())
        h1.write('\n')
        h1.write(input('Write Your Food: '))
        h1.close()

    else:
        print('Invalid Input!')


def LockExercise():
    if a == 1:
        f2 = open('Rohan-Exercise.txt', 'w')
        f2.write(getdate())
        f2.write('\n')
        f2.write(input('Write Your Exercise: '))
        f2.close()

    elif a == 2:
        g2 = open('Harry-Exercise.txt', 'w')
        g2.write(getdate())
        g2.write('\n')
        g2.write(input('Write Your Exercise: '))
        g2.close()

    elif a == 3:
        h2 = open('Karan-Exercise.txt', 'w')
        h2.write(getdate())
        h2.write('\n')
        h2.write(input('Write Your Exercise: '))
        h2.close()

    else:
        print('Invalid Input!')

print("What's your name?")
a = int(input('1. Rohan\n2. Harry\n3. Karan\n'))

def Health():

    print('What you want to do?')
    b = int(input('1. Retrieve\n2. Lock\n'))

    print('Choose:')
    c = int(input('1. Food\n2. Exercise\n'))

    if b == 1 and c == 1:
        RetrieveFood()

    elif b == 2 and c == 1:
        LockFood()

    elif b == 1 and c == 2:
        RetrieveExercise()

    elif b == 2 and c == 2:
        LockExercise()

    else:
        print('Invalid Input!')

Health()

for i in range(5):

    x = input('Do you want to continue? YES=y or NO=n\n')

    if x == 'y':
        Health()

    elif x == 'n':
        print('Thank You!')
        break

    else:
        print('Invalid Input!')



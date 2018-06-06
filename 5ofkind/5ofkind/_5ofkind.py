
# Probability of rolling 5 of a kind

from random import randrange

def main():
    print("This program Approximates the probability of rolling")
    print("five-of-a-kind on a single roll of 5 dice.\n")

    n = int(input("How many rolls of the dice(5) should I simulate? "))
    bones = 0
    for i in range(n):
        if equalRolls(5):
            bones = bones + 1
    print("Estimated prob =", float(bones)/n)


def equalRolls(count):

    first = randrange(1,7)
    for i in range(count-1):
        roll = randrange(1,7)
        if roll != first:
            return False
    
    return True

if __name__ == '__main__':
    main()




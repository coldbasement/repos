#   Rabbits



def main():

    # table headings
    print("Wind Chill Table\n\n")
    print("Temperature".center(70))
    print("mph|", end=' ')
    temperature = list(range(-20,61,10))
    for i in  temperature:
        print("{0:5}".format(i), end=' ')
    print("\n---+" + 55 * '-')

    # lines in table
    for speed in range(0,51,5):
        print("{0:3}|".format(speed), end=' ')
        for temp in temperature:
            print("{0:5.0f}".format(windChill(temp, speed)), end=' ')
        print()
    print()

main()


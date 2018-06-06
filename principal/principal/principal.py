
def main ():
    print("This program calculates the future value")
    print("of an investment.")

    principal = eval(input("Enter the intial principal:  "))
    apr = eval(input("Enter the annual interest rate:  "))
    years = eval(input("Enter the Number of years:  "))

    for i in range(years):
        principal = principal * (1 + apr)

        print("The value in year", i , "is:", principal)

main()

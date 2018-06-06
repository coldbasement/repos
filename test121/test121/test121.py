
def main ():
    print("This program calculates the future value")
    print("of an investment.")

    principal = eval(input("Enter the intial principal:  "))
    apr = eval(input("Enter the annual interest rate:  "))
    year = eval(input("Enter the Number of years:  "))

    for i in range(1,year+1):
        principal = principal * (1 + apr)

        print("The value in year", i , "is:", principal)
main()
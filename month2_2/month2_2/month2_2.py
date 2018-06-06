

#A program to print the abbreviation of a month, given its number


def main():
 #Months lookup table
 months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug",
           "Sep", "Oct", "Nov", "Dec"]

 n =  int(input("Enter a month number (1-12): "))


 #Print results
 print("The month abbreviation is:", months[n-1] + ".")

main()

 
'''
Input

'''


def main():
    # Input the date in mm/dd/yyyy format (dateStr)
    
    dateStr = input("Enter a date(mm/dd/year): ")
    # Split the dateStr into month, day and year strings
    monthStr, dayStr, yearStr = dateStr.split("/") # "unpacked" using simultaneous assignment

    
    # convert the month string into a month number
   
    months = ["January", "February", "March", "April", 
               "May", "June", "July", "August",
              "September", "October", "November", "December"]

    monthStr = months[int(monthStr)-1]
   
    # Output the new date string
    print("The converted date is: ", monthStr, dayStr+",", yearStr)

main()


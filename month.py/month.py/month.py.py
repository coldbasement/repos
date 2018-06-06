

#A program to print the abbreviation of a month, given its number


def main():
 #Months lookup table
 months = "JanFebMarAprMayJunAugSepOctNovDec"

 n =  int(input("Enter a month number (1-12): "))

 # compute starting position of month n in months

 pos = (n-1) *3 # Jan (1-1)*3 = position 0, Dec (12-1)*3= position 33
 
 #Grab the appropriote slice(Slicing)  from months need to add 3 to pos becuase abrievation is 3 charictars 
 monthAbbrev = months[pos:pos+3]

 #Print results
 print("The month abbreviation is", monthAbbrev + ".")

main()

 




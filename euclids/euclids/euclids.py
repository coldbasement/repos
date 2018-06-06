
#    Euclid's algorithm for GCD

def gcd(m,n):
    while m != 0:
        n, m = m, n % m
    return n

def main():
    print("Euclid's Greatest Common Divisor(GCD) algorithm\n")
    n1, n2 = input("Enter two natural numbers (n1, n2): ").split(",")
    
    print("The GCD of", n1, "and", n2, "is", gcd(int(n1),int(n2)))

if __name__ == '__main__':
    main()


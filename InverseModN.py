import math

def findInverse(unit, mod):
    for i in range(1,mod):
        if unit * i % mod == 1:
            return i

def main():
    modulus = int(input("What modulus do you want to work with? "))
    print("Units mod ",modulus," and their inverses: ")
    inverses = {}
    for i in range(modulus):
        if math.gcd(i, modulus) == 1:
            inverse = findInverse(i, modulus)
            inverses[i] = inverse
            print(i, ":", inverse)

if __name__ == '__main__':
    main()
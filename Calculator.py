import math

a = (int(input("Enter 1st number on which u want to do ops.: ")))
b = (int(input("Enter 2nd number on which u want to do ops.: ")))

Ops = ("Enter 1 for Plus : +","Enter 2 for Minus: -", "Enter 3 for Multiply: *", "Enter 4 for div: /", "Enter 5 for power or exponential: ^", "Enter 6 for Square root",
"Enter 7 for cube root", "Enter 8 to find percentage: %", "Enter 9 for Pi: π", "Enter 10 for sin(a)", "Enter 11 for cos(a)", "Enter 12 for tan(a)", "Enter 13 for cosec(a)", 
"Enter 14 for ten to the power of a", "Enter 15 for finding modulo of a", "Enter 16 if want to find the number is even or odd", "Enter 17 to find out factorial of a",
"Enter 18 to find the value of e","Enter 19 to find out log of a")

a_in_radians = math.radians(a)

def ln(a):
    e = 2.7182818284590452353602874713527
    ln = e**(ln(a)) = a

def sin(a):
    return math.sin(a)

def cos(a):
    return math.cos(a)

def tan(a):
    return math.tan(a)

def csc(a):
    return 1 / math.sin(a)

print(Ops)
op = (int(input("Choose ur Operation and enter the number accordingly : ")))


match op:
    case 1:
        sum = a + b
        print("The result after adding is: ", sum)
    case 2: 
        sub = a - b
        print("The result after substracting is: ", sub)
    case 3: 
        mul = a*b
        print("The result after multipling is: ", mul)
    case 4:
        div = a/b
        print("The result after dividing is: ", div)
    case 5: 
        expo = a**b
        print("The result after power is: ", expo)
    case 6: 
        sqrt = a**(1/2)
        print("The result after square root is: ", sqrt)
    case 7:
        cubrt = a**(1/3)
        print("The result after cube root is: ", cubrt)
    case 8: 
        per = (a/b) * 100
        print("The result after percentage is: ", per, "%")
    case 9: 
        pi = 3.1415926535897932384626433832795
        PI = pi * a
        Area =  2*pi*a
        print("The value of pi is: ", pi)
        print("The result after multipling a with pi is: ", PI)
        print("The result after finding the area is: ", Area)
    case 10:
        sin = math.sin(a_in_radians)
        print("The result after sin(a) is: ", round(sin, 2))
    case 11:
        cos = math.cos(a_in_radians)
        print("The result after cos(a) is: ", round(cos, 2))
    case 12: 
        tan = math.tan(a_in_radians)
        print("The result after tan(a) is: ", round(tan,2))
    case 13:
        cosec = csc(a_in_radians)
        print("The sine of degrees is:", round(cosec, 2))
    case 14:
        ten_power = 10**a
        print("The result ten power of a is: ", ten_power)
    case 15: 
        num = int(input("Enter the number for modulo: "))
        mod = num % a
        print("The modulo is: ", mod)
    case 16:
        if a % 2 == 0:
            print("The Number is EVEN")
        else:
            print("The Number is ODD")
    case 17:
        fact = math.factorial(a)
        print(fact)
    case 18:
        e = 2.7182818284590452353602874713527
        print("The value of e: ", e)
    case 19:
        log = math.log(a)
        print(log)
    case _:
        print("Please Enter a number!! Alphabets not allowed")

#Chapter 5

# wrire factorial as a recursion
def factorial(n:list):
    if n<=1:
        print('lowest n reached')
        return n
    else:
        print(n,n-1)
        return n*factorial(n-1)

factorial(4)

def toStr(n,base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]

print(toStr(769,10))
toStr(769,10)
(1453//16)//16

convertString = "0123456789ABCDEF"
convertString[5]

#Reverse the string
def strReverse(str):
    if len(str) <= 1:
        return str
    else:
        #print("currently", str)
        return strReverse(str[1:]) + str[0] 

test_str = 'abcdef'
strReverse(test_str)
#take the string make a range
test_str = 'live not on evil'

def removeWhite(s):
    """
    remove whitespace recursively
    """
    if len(s) <=1:
        return s
    # if you need to add more exceptions, do it here
    elif (s[0] == " ") or (s[0] == "'"):
        return s[1] + removeWhite(s[2:])
    else:
        return s[0] + removeWhite(s[1:])

def isPal(s):
    s = removeWhite(s)
    if s == strReverse(s):
        return True
    else:
        return False

isPal(test_str)
islower()
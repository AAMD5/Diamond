# Return a string that looks like a * diamond shape
# return None if input is negative or even

#  *
# ***
#  *

""" *
   ***
  *****
   ***
    *"""

def diamond(n):
    
    if n % 2 == 0:
        return None
    
    String = ""
    for i in range(n-1):
        String += ' '*((n-1)-i) + ((2*i)+1)*'*'
        String += "\n"
    for i in range((n-1)):
        String += ' '*(i+2) + '*'*((2*(((n-1)-1)-i))-1)
        String += "\n"
        
    return String

print(diamond(3))
    

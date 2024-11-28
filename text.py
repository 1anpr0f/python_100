#if 5 > 2:
   # print("hello,world")
    #this is a comment
    #note:indatation spaces before writting a block of codex
#x= 50.60
#x = ["apple", "banana", "cherry"]
#print(type(x))
#if 5 > 2 :
 #   print(bool())
#import random
#print(random.randrange(1,100))



#sum of multiple of 5 and 3
#def sum_of_multiples(number):
    # Return 0 if the number is negative
    #if number < 0:
     #  return 0
    
    # Initialize sum to 0
    #total = 0
    
    # Loop through all numbers below the input number
   # for i  in range(number) :
        # Check if the number is a multiple of 3 or 5
  #   if i % 3 == 0 or i % 5 == 0:
 #           total += i
  
#    return total
#print(sum_of_multiples(1000))





#Sum the digits of the number repeatedly until you have a single-digit result.is known as digital root
#def digital_root(n):
 #   while n >= 10:
  #      n=sum(int(digit) for digit in str(n))
   #     return n
    #print(digital_root(967))
    
    
    
    
    
  #  def square_digits(n):
    # Convert the integer to a string to access each digit
   # digits = str(n)
    
    # Square each digit and concatenate the results
    #result = ''.join(str(int(digit) ** 2) for digit in digits)
    
    # Convert the concatenated result back to an integer
    #return int(result)
    
    

#def find_k(n, p):
    # Convert n to a string to process each digit
 #   digits = [int(d) for d in str(n)]
    
    # Calculate the sum of digits raised to consecutive powers starting from p
  #  powered_sum = sum(digit ** (p + i) for i, digit in enumerate(digits))
    
    # Check if powered_sum is a multiple of n
   # if powered_sum % n == 0:
 #       return powered_sum // n
    #else:
     #   return -1
#print(find_k(89,1))

test_one = "1234567890"
itter = ''
for i in test_one:
  itter += i
  print(itter)
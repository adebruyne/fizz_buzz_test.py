#Write a program that prints the numbers 
# from 1 to 100. But for multiples of three 
# print “Fizz” instead of the number and 
# for the multiples of five print “Buzz”. 
# For numbers which are multiples of both three 
# and five print “FizzBuzz”.


from fizz_buzz import *

#is it a number
#is it a number in the range of 1 to 100
#multiples of three = print("Fizz")
#multiples of five = print("Buzz")
#multiples of three and five = print("FizzBuzz")


fb1 = integer
assert is_valid_fb(fb1), "%d should be valid" %fb1

fb2 = "1-100"
assert is_valid_fb(fb2), "number should be in range of 1 to 100"

fb3 = input % 3 == 0
assert is_valid_fb(fb3), "number divisible by 3 print 'fizz'"

fb4 = input % 5 == 0
assert is_valid_fb(fb4), "number divisible by 5 print 'buzz'"

fb5 = input % 3 == 0 and input % 5 == 0
assert is_valid_fb(fb5), "number divisible by 3 and 5 print 'fizzbuzz'"


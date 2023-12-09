
#Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.


def hello_name(user_name):
 print(user_name)

hello_name("hello_USERNAME")

# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds(i):
  return

for i in range(1,100):
     if i%2!=0:
        print(i)

first_odds(i)

# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

def max_num_in_list(a_list):
   
   max = a_list[0]
   for num in a_list:
     if (num > max):
      max = num

   return max
   
a_list = [1,2,3,4,54,78]

max=max_num_in_list(a_list)

print("Maximum num : " , max)

 
               
# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year): 
    if (a_year%4==0):
        print("it is a leap year")
        return True
    elif (a_year%100!=0) or (a_year%400==0):
        print("it is not a leap year")
        return False
    
print(is_leap_year(2024))
    
# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

#a_list=[1,2,3,4,5]
def is_consecutive(a_list):
    for i in range(0,len(a_list)-1):
        if (a_list[i]+1) != a_list[i+1]:
          return False
    else:
          return True

print(is_consecutive([1,2,9,4,5]))
        
   







''' Exercise #2. Computational Thinking and Programming.'''

#########################################
# Question 1 - do not delete this comment
#########################################
number = input('please choose a number: ')
# Replace ??? with an appropriate command to get a number from the user.
# Write the rest of the code for question 1 below here.
number=int(number)
if number%2==0:
    print(f'I am {number} and I am even')
else:
    print(f'I am {number} and I am odd')

#########################################
# Question 2 - do not delete this comment
#########################################
number = input('please choose another number: ')
# Replace ??? with an appropriate command to get a number from the user.
# Write the rest of the code for question 2 below here.
number=int(number)
if number%6==0:
    print('divisible by 6')
if number%3==0 and number%2!=0: 
    print('divisible by 3')
if len(str(number))%2==0:
    print('even number of digits')

#########################################
# Question 3 - do not delete this comment
#########################################
grade =58
# Replace ??? with an integer of your choice.
# Write the rest of the code for question 3 below here.
if grade<0 or grade>100:
    print('illegal grade')
if 0<=grade and grade<=59:
    print('F')
if 60<=grade and grade<=69:
    print('D')
if 70<=grade and grade<=79:
    print('C')
if 80<=grade and grade<=89:
    print('B')
if 90<=grade and grade<=100:
    print('A')


#########################################
# Question 4 - do not delete this comment
#########################################
my_str ='aBBa'
# Replace ??? with a string of your choice.
# Write the rest of the code for question 4 below here.
rev_string=my_str[::-1]
if my_str==rev_string:
    print('True')
if my_str!=rev_string:
    print('False')




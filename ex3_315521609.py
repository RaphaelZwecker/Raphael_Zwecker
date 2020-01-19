''' Exercise #3. Computational Thinking and Programming.'''

#########################################
# Question 1 - do not delete this comment
#########################################
lst =[1,2,3,4,5,6,7,8,9] # Replace ??? with a list of your choice.
# Write the rest of the code for question 1 below here.
print(lst[::-2])


#########################################
# Question 2 - do not delete this comment
#########################################
lst =['hello',4,'yes',8,'no',12] # Replace ??? with a list of your choice.
# Write the rest of the code for question 2 below here.
x=len(lst)
print(list(range(x)))


#########################################
# Question 3 - do not delete this comment
#########################################
lst =[9,8,7,6,5,4,3,2,1] # Replace ??? with a list of integer numbers of your choice.
# Write the rest of the code for question 3 below here.
a=0
for numbers in lst:
      if numbers%2!=0:
          a=a+numbers
print(f'lists odd number is:{a}')


#########################################
# Question 4 - do not delete this comment
#########################################
x ='raphael' # Replace ??? with a value of your choice.
lst =['shlomo',2,'motti',4,'avner',8,9,'raphael'] # Replace ??? with a list of your choice.
# Write the rest of the code for question 4 below here.
if x in lst:
        print('true')
else:
        print('false')


#########################################
# Question 5 - do not delete this comment
#########################################
lst =[1,1,2] # Replace ??? with a list of your choice.
# Write the rest of the code for question 5 below here.
b=len(lst)
if b>5:
    lst=lst[:5]
    print(lst)
elif b<5:
    while b<5:
        lst.append(0)
        b=b+1
    print(lst)
elif b==5:
    print(lst)

    
    





print(8**2)
#this is exponetioal

print(81**(1/2))
#this is square root 


print(10//4)
#print qoutient(how many time it goes into no) if number


print(20%6)
# to get remimenr

print("""hello
when i use
3\nuotes.
new lines are allowed""")


print("spam" * 3)
#string can be multiplied
print(4 * '2')

#12 = 65
#in pyhton string cannot start with numers
#Variables can be reassigned as many times as you want.
#However, it is not good practice.
x = '2'
y = '4'
z = int(x) + int(y)
print(z)

#in place operators
#In-place operation is an operation that changes directly the content without making a copy. 
x=2
x += 3
#x += 3
#x *= 3
#x /= 3
#x -= 3
#x %= 3
# can use in place operatoes with strings aswell
print(x)
# can use in place operatoes with strings aswell
x = 'spam'
x+='eggs'
print(x)
# instaed of having to write 'x = x + 3' this . more concise




#walrus operator
#Walrus operator := allows you to assign values to variables within an expression, including variables that do not exist yet.
num = int(input('inputnow'))
print(num)
print(num:=int(input("input now")))
#instead of getting varible then printing we can do at some time
# by adding := to the begginig variblename THEN :=
spam = "7"
spam = spam + "0"
eggs = int(spam) + 3
print(float(eggs))
# i thought result is 10.0
# reason it is not is becuse we are adding sting not intergers . intergers it would have been 7+0
# but becuse stirng it is 7+0 = 70
# the 70 still string that is why it was converted in line 3
#float turn it form 73 to 73.0
#float == real




x = 5
y = x + 3
y = int(str(y) + "2")
print(y)
82

#i got 10 answer 82 
#it stores 8 as string which makes it not add as 8+2= 10 but as 8 and 2= 82
#tricky part is 8 is stored as string and not int
# the way i could have know 8 stored as str is becuse open AND close paranthess next to y/ the "str"
#while int open and close paranthess at begin and end
print (6==7)#boolean can be created by comparing two values
print (6!=7)#not equal to operator .true if item compared are diffrent
#Comparison operators are also called Relational operators.
#<> comparion operatoes also produce boolean values (this is how if statemnt works )
print(5>9)
#Greater than and smaller than operators can also be used to compare strings lexicographically (by leters)
print("Annie">"Andy")


num = 7
if num > 3:
   print("3")
   if num < 5:
      print("5")
      if num ==7:
         print("7")

# i thougth it would return 7
# it return 3 because the statement after that if not ture so it stops there 


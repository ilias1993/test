from math import *

print('   /|')
print('  / |')
print(' /  |')
print('/___|')

character_name = 'Jonh'
character_age = '35'
#---------------------------------------------------------------------
#---------------------------------------------------------------------
#----------------------------Strings----------------------------------
print('There was once a man named ' +character_name+',')
print('he was '+character_age+' years old.')
print('He really liked the name '+character_name+ ',')
print('but didnt like being '+character_age+'.')

phrase = 'Giraffe Academy'
print('\n' +phrase.upper())
print(len(phrase))
print(phrase[1:5])
print(phrase.index('A'))
print(phrase.index('ffe'))
print(phrase.replace('Giraffe', 'Elephant').lower())
print('\n')
#---------------------------------------------------------------------
#---------------------------------------------------------------------
#----------------------------Numbers----------------------------------
my_num = 5
my_num2 = -4
print(my_num)
print('This is the way to print numbers and strings at the same print command: ' +str(my_num))
print(abs(my_num2))
print(pow(my_num, 2))
print(max(3,4,5,19))
print(min(3,4,5,19))
print(round(2.2))
print(round(2.5))
print(round(2.6))
print(floor(5.9))
print(ceil(5.1))
print(sqrt(49))
#---------------------------------------------------------------------
#---------------------------------------------------------------------
#-----------------------Inputs From Users-----------------------------
name = input('Enter your name: ')
age = input('Enter your age: ')
print('Hello '+ name + '! ' + 'You are ' + age + '.')
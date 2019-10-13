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
print('\n')
#---------------------------------------------------------------------
#---------------------------------------------------------------------
#-----------------------Inputs From Users-----------------------------
# name = input('Enter your name: ')
# age = input('Enter your age: ')
# print('Hello '+ name + '! ' + 'You are ' + age + '.')
# print('\n')
#---------------------------------------------------------------------
#---------------------------------------------------------------------
#-----------------------------Lists-----------------------------------
lucky_numbers = [4, 8, 15, 16, 23, 43]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
print(friends)
friends.extend(lucky_numbers)
print(friends)
friends.append("Pythas")
print(friends)
friends.insert(1, "Agis")
print(friends)
friends.remove("Pythas")
print(friends)
friends.pop()
print(friends)
print(friends.index("Agis"))
friends.insert(4, "Agis")
print(friends)
print(friends.count("Agis"))
friends[7:] = []
print(friends)
friends.sort()
print(friends)
lucky_numbers.reverse()
print(lucky_numbers)
friends2 = friends.copy()
print(friends2)
print('\n')
#---------------------------------------------------------------------
#---------------------------------------------------------------------
#--------------------------Dictionaries-------------------------------
month_conversions = {
    "Jan": "Januray",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}
print(month_conversions["Sep"])
print(month_conversions.get("Apr"))
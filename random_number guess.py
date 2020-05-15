import random as rd
print(30*'#')
print('Number Guess Game')

number_range = input('Enter Number for Start Range : ')
number_range2 = input('Enter Number for range End : ')
replay = 3
while(True):
    guess_number = input('Enter Your luky Guess Number : ')
    if number_range.isnumeric() and number_range2.isnumeric() and guess_number.isnumeric():
        if number_range <number_range2:
                x = rd.randrange(int(number_range),int(number_range2))
                if x == int(guess_number):
                    print('WoW................ You win iT')
                    if (input('Dou Want to Re play : ')== 'yes'):
                        continue
                    else:
                        break
                else:
                    print('Sorry Try Again')
                    if (input('Do u want to replay : ')== 'yes'):
                        continue
                    else:
                        break
        else:
            print('invalid Input')
    else:
        print('invalid input')





print(rd.randrange(1,20))
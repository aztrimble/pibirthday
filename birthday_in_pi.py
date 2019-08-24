#!/usr/bin/env python3
'''
birthday_in_pi.py

Script to find all the ways your birthday appears in the first one million 
decimal places of pi. Pi is read in from a text file.

Must be run using python3. Otherwise it will throuw an input error.

Inputs:
    birthday [] = user is asked for their birthday in yyyymmdd format
                  NOTE: birthday is not error checked after input
Outputs:
    print to screen = Table of all the formats your birthday appears in
                      and some comments
'''

import sys

#--- Create string variable that contains pi to one million decimal places ---
filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

while True:
    #--- Obtain the users birthday and parse into year, month, and day
    birthday = input("\nEnter your birthday (yyyymmdd): ")
    birthday_year = birthday[0:4]
    birthday_month = birthday[4:6]
    birthday_day = birthday[6:]

    #--- Generate all possible combinations of the users birthday
    #--- and check if they are in pi
    n = 0

    bday = {'yyyymmdd' : birthday[:],
            'mmddyyyy' : birthday_month+birthday_day+birthday_year,
            'ddmmyyyy' : birthday_day+birthday_month+birthday_year,
            'yymmdd'   : birthday[2:],
            'mmddyy'   : birthday_month+birthday_day+birthday_year[2:],
            'ddmmyy'   : birthday_day+birthday_month+birthday_year[2:]}

    print('\n----- HAPPY PI DAY! -----')
    print('Are you predisposed to be an engineer?')
    print('Lets check the numerological arithmancy...')
    print('\nThe following table shows in what formats your birthday\n'+
            'appears in the first one million decimal places of pi.\n'+
            'A clear numerological indicator of your engineering destiny.\n')
    print('Format\t\tAppears?')
    print('----------------------')

    result = [[str(birthday)]]
    for key, value in sorted(bday.items()):
        if value in pi_string:
            result[0].append('1')
            n += 1
            if len(key)==8:
                print(key+'\tX')
            else:
                print(key+'\t\tX')
        else:
            result[0].append('0')
            if len(key)==8:
                print(key+'\t-')
            else:
                print(key+'\t\t-')

    print()
    if n==0:
        print('0 for 6, You are a rare case. Maybe you should study history and not engineering?')
    elif n==1:
        print('1 for 6, Your numerological proclivity to engineering is fairly weak')
    elif n==2:
        print('2 for 6, Not quit half? What is arithmancy trying to say?')
    elif n==3:
        print('3 for 6, Half of all possibilities. Arithmancy indicates you might have choosen the right major after all')
    elif n==4:
        print('4 for 6, And at least one long form version! Your in the right place')
    elif n==5:
        print('5 for 6, Numerological influences must have governed your engineering destiny')
    else:
        print('All 6! You really have no choice. You must be an engineer!')

    print('\nMajor bonus points for anyone that can calculate the probabilities and expected values of these results...\n')

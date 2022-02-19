#!/usr/bin/env python3
import random

with open('/usr/share/dict/words') as f:
    s = f.read().split()
s = list(set(map(lambda x: x.lower(), filter(lambda x: len(x) == 5,s))))

commands = [
    "rm",   # letter not used at all
    "at",   # fix a letter to index
    "not",  # letter is used but not at index
]

helpstr='''
USAGE:
    rm  <letters>        - remove all words that include given letters
                           e.g. [rm abcd]
    at  <index>,<letter> - remove all words that don't have <letter> at <index>
                           e.g. [at 0,a]
    not <index>,<letter> - remove all words that have <letter> at <index>,
                           as well as all words that don't have <letter>
                           e.g. [not 0,a]
'''

print(helpstr)

while True:
    # sort by unique letters, tie break by number of vowels
    s.sort(key=lambda x: (len(set(x)), len(set('aeiou').intersection(x))), reverse=True)
    n = len(s)
    if n == 0:
        print("wtf no words left")
        exit(-1)
    print(f'{n} words left', end='')
    if n > 20:
        print('... here\'s 20 of them:')
        print('   ', ', '.join(s[:20]))
    else:
        print(':')
        print('   ', ', '.join(s))

    inpt = input('refine: ')
    inpt = inpt.split()
    if len(inpt) != 2 or inpt[0] not in commands:
        print(helpstr)
        continue
    command, arg = inpt
    if command == 'rm':
        s = list(filter(lambda x: len(set(arg).intersection(x)) == 0, s))
    elif command == 'at':
        arg = arg.split(',')
        if len(arg) != 2 or not arg[0].isdigit() or len(arg[0]) != 1 or len(arg[1]) != 1:
            print(helpstr)
            continue
        i = int(arg[0])
        if i >= 5:
            print(helpstr)
            continue
        c = arg[1]
        s = list(filter(lambda x: x[i] == c, s))
    elif command == 'not':
        arg = arg.split(',')
        if len(arg) != 2 or not arg[0].isdigit() or len(arg[0]) != 1 or len(arg[1]) != 1:
            print(helpstr)
            continue
        i = int(arg[0])
        if i >= 5:
            print(helpstr)
            continue
        c = arg[1]
        s = list(filter(lambda x: x[i] != c and c in x, s))
    else:
        assert False


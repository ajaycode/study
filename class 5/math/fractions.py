__author__ = 'agummadi'

import random

answers = []

def _is_prime (number):
    if (number < 3):
        return False
    for i in range (3, number):
        if (number % i == 0):
            return False
    return True

def nearest_primes ():
    number = random.randint (10, 200)
    lower_prime = higher_prime = 0
    for i in range (number - 1, 3, -1):
        if (_is_prime (i) == True):
            lower_prime = i
            break
    i = number + 1
    while (_is_prime (i) == False):
        i = i+1
    higher_prime = i
    answer = "Lower prime: {}, Higher prime: {}".format (lower_prime, higher_prime)
    answers.append (answer)
    print ("The prime numbers that are just before and after {} are _____ and _____.".format (number))

def list_primes ():
    number = random.randint (10, 200)
    range_size = random.randint (4, 10)
    answer = []
    for i in range (number, number + range_size + 1):
        if (_is_prime(i) == True):
            answer.append (i)
    answers.append (answer)
    print ("The prime numbers between {} and {} are ________".format (number, number + range_size))



def twin_primes ():
    first_prime = random.randint (2, 25)
    while (_is_prime (first_prime) == False):
        first_prime = first_prime + 1
    if (_is_prime(first_prime + 2) == True):
        answer = "The numbers are twin primes."
    else:
        answer = "The numbers are not twin primes."
    answers.append (answer)
    print ("{} and {} are twin primes.  Yes or No?".format (first_prime, first_prime + 2))

functions = [nearest_primes, list_primes, twin_primes]


for i in range (0, len(functions) ):
    #print (functions [num])
    f = functions[i]
    f ()
for i in range (0, len (answers)):
    print (i, answers[i])

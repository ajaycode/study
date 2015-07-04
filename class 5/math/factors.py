__author__ = 'ajay'
'''factors.py: Generates fractions related mathematical problems'''

import random
import logging

answers = []

def _is_prime (number):
    if (number < 3):
        return False
    for i in range (2, number):
        if number % i == 0:
            return False
    return True

def is_prime (number):
    '''Written for conducting unit tests only'''
    return (_is_prime(number))

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

def factors (number=0):
    if number <= 0:
        number = random.randint (50, 500)
    factors = []
    n = 1
    while (n <= number):
        if (_is_prime(n) == True or n == 2):
         if (number % n == 0):
             factors.append (n)
             #factors.append (number / n)
        n = n + 1
    answers.append (factors)
    print ("The factors of {number} are _________________.".format (number=number))
    return (factors) # for unit testing

def multiples (number=0, number_of_multiples=0):
    if (number <= 0) or (number_of_multiples <= 0):
        number = random.randint (16, 200)
        number_of_multiples = random.randint (4, 8)
    multiple_list = []
    for n in range (1, number_of_multiples + 1):
        multiple_list.append (number * n)
    answers.append(multiple_list)
    print ("The first {number_of_multiples} multiples of {number} are ____________".format (number_of_multiples=number_of_multiples, number=number))
    return (multiple_list)

functions = [nearest_primes, list_primes, twin_primes, factors, multiples]

def squat ():
    print ("hello world")
    for i in range (5):
        yield (i**2)

def main ():
    logging.basicConfig (format = '%(asctime)s - %(levelname)s - %(message)s', datefmt= '%Y%m%d %I:%M:%S %p',filename='class.log', level=logging.INFO)
    for i in range (0, len(functions)):
        logging.info('Function : %s'%functions [i])
        f = functions [i]
        f ()
    for i in range (0, len (answers)):
        print (i+1, answers[i])
    primes = [ _is_prime(x) for x in range (100)]
    print (primes)
    for i in squat ():
        print (i)

if __name__ == "__main__":
    main ()
__author__ = 'Ajay'
'''factors.py: Generates fractions related mathematical problems'''
'''python <filename.py> will print all the questions, followed by a list of answers'''

import random
import logging
import os

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
    print ("The unique factors of {number} are _________________.".format (number=number))
    return (factors) # for unit testing

def all_factors (number=0):
    """Retrieves all the  prime factors of a number, even the duplicate prime factors"""
    if (number <= 0):
        number = random.randint (50, 999)
    input = number
    factor_list = []
    if _is_prime(number):
        factor_list.append (number)
    else:
        n = 1
        while (n <= number):
            if (_is_prime(n) == True or n == 2):
                if number % n == 0:
                    factor_list.append (n)
                    number = number // n
                    n = 1
            n = n + 1
    question = "___"
    for i in range (0, len (factor_list) -1):
        question = "{} X ___ ".format (question)
    question = "{} = {}, where each ____ is a prime number".format (question, input)
    print (question)
    answers.append (factor_list)
    return (factor_list)

def consecutive_primes (number=0, num_primes=0):
    if number <= 0 or num_primes <= 0:
        number = random.randint (5, 15)
        num_primes = random.randint (2,3)
    orig_number = number
    prime_list = []
    while len(prime_list) < num_primes:
        if _is_prime(number):
            prime_list.append(number)
        number = number + 1
    print ("The prime factors of a number are {} consecutive primes.  The smallest of these primes is {}.  What are the factors?  What is the number?".format (num_primes, prime_list[0]))
    product = 1
    for i in range (0, len(prime_list)):
        product = product * prime_list[i]
    answer = "Factors = {}. Product = {}".format (prime_list, product)
    answers.append(answer)
    return (answer)



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

def _highest_common_factor (number_list=[]):
    list_length  = len (number_list)
    if (len(number_list) == 0):
        list_length = random.randint(2,3)
        logging.info ("list_length = {}.".format(list_length))
        hcf = random.randint (5, 12)
        for i in range (0, list_length):
            logging.info ("index i : {}".format (i))
            number_list.append(hcf * random.randint (2, 25))
        logging.info ("Number_list = {}".format (number_list))
    ordered_list = list(number_list)
    ordered_list.sort()
    logging.info ("ordered_list = {}".format (ordered_list))
    numerator, denominator = ordered_list.pop (list_length -1), ordered_list.pop (list_length -2)
    num_iterations = len (number_list) -1

    while (num_iterations > 0):
        while (numerator % denominator != 0):
            numerator, denominator = denominator, numerator % denominator
            logging.info ("numerator = {}, denominator = {}, remainder = {}".format (numerator, denominator, numerator%denominator))
        if (len(ordered_list) > 0):
            numerator = ordered_list.pop ()
        num_iterations = num_iterations - 1
    print ("The HCF of {} is _____.".format (number_list))
    answers.append (denominator)
    return (denominator)

def lcf_and_hcf (number_list=[]):
    if (len(number_list) <= 3):
        hcf = random.randint (7, 20)
        for i in range (3):
            number_list [i] = random.randint (30, 200)
    lcm = _lowest_common_multiple (number_list)
    hcf = _highest_common_factor (number_list)
    print ("The LCM and HCF of {} are _____ and _______ respectively.".format (number_list))
    answers.append ([lcm, hcf])
    return (lcm, hcf)


functions = [nearest_primes, list_primes, twin_primes, factors,  multiples, all_factors, consecutive_primes, \
             highest_common_factor]

def squat ():
    print ("hello world")
    for i in range (5):
        yield (i**2)


def main ():
    logging.basicConfig (format = '%(asctime)s - %(levelname)s - %(message)s', datefmt= '%Y%m%d %I:%M:%S %p',filename='class.log', level=logging.INFO)
    #random.seed (os.urandom(5))
    for i in range (0, len(functions)):
        logging.info('Function : %s'%functions [i])
        f = functions [i]
        f ()

    for i in range (0, len (answers)):
        print (i+1, answers[i])
    #primes = [ _is_prime(x) for x in range (100)]
    #print (primes)
    #for i in squat ():
    #    print (i)

    #for i in range (100, 500):
     #   print (i, all_factors(i))

if __name__ == "__main__":
    main ()

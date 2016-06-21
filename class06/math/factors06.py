__author__ = 'Ajay'
'''factors.py: Generates fractions related mathematical problems'''
'''python <filename.py> will print all the questions, followed by a list of answers'''

import random
import logging
import os
import uuid
from fractions import gcd
import sys

sys.path.append ('..\\..\\')
from class05.math.factors import _is_prime, _highest_common_factor, _least_common_multiple, _generate_unique_random_numbers, answers  #all private functions
from class05.math.factors import *  #public functions


names = ['Rahul', 'Ganpat', 'Gaurav', 'Gautam','Girish']


def containers_hcf (capacity=[]):
    container_list = ["tubs", "tankers", "water tanks", "oil-ships"]
    if (len (capacity) != 2):
        capacity = []
        hcf = random.randint (12,29)
        capacity.append (hcf * random.randint (20, 40))
        capacity.append (hcf * random.randint (20, 40))
        #_,hcf = _highest_common_factor([capacity[0], capacity[1]])
        while (capacity[0] == capacity[1] or hcf == 1):
            capacity[0] = random.randint(20, 40)
            _,hcf = _highest_common_factor([capacity[0], capacity[1]])
    container = container_list[random.randint(0, len(container_list)-1)]
    print ("Two {} contain {} liters and {} liters of liquid respectively.  Find the maximum capacity of a container which can measure the liquid of both tanks when used".format(container, capacity[0], capacity[1]),\
    " an exact number of times.")
    _,answer = _highest_common_factor([capacity[0], capacity[1]])
    answers.append (answer)
    return (answer)



functions = [nearest_primes, list_primes, twin_primes, factors, multiples, all_factors, consecutive_primes, \
             highest_common_factor, least_common_multiple, lcm_and_hcf, pole_spacing, stamp_distribution,\
             march_past, building_age, chocolate_distribution, students_in_class, students_running_circles, journey_time_minimum_hours, containers_hcf]


def squat():
    print("hello world")
    for i in range(5):
        yield (i ** 2)


def main():
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(funcName)s:%(message)s', datefmt='%Y%m%d %I:%M:%S %p',
                        filename='class.log', level=logging.INFO)
    unique_id = uuid.uuid1(1)
    html_text = "<h1>Fractions</h1>\n"
    html_text += "<h2>Question Paper # {}</h2>\n".format(str(unique_id))
    html_text += r'<ol>'
    print("Question Paper # {}".format(str(unique_id)))
    # random.seed (os.urandom(5))
    for i in range(0, len(functions)):
        logging.info('Function : %s' % functions[i])

        print ("{i}) ".format(i=i+1), end="")
        f = functions[i]
        html_text += " <li>"
        f()
        html_text += " </li>\n"
        logging.info ('Answer  : %s' % answers[i])
    html_text += r'</ol>'
    print ()
    print("Answer Key # {}".format(str(unique_id)))
    for i in range(0, len (functions)): #len(answers)):
        print(i + 1, answers[i])
        #primes = [ _is_prime(x) for x in range (100)]
        #print (primes)
        #for i in squat ():
        #    print (i)

        #for i in range (100, 500):
        #   print (i, all_factors(i))


if __name__ == "__main__":
    main()

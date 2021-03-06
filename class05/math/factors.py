__author__ = 'Ajay'
'''factors.py: Generates fractions related mathematical problems'''
'''python <filename.py> will print all the questions, followed by a list of answers'''

import random
import logging
import os
import uuid
from fractions import gcd

answers = []
names = ['Rahul', 'Ganpat', 'Gaurav', 'Gautam','Girish']

def _is_prime(number):
    if number < 3 or number % 2 == 0:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def is_prime(number):
    '''Written for conducting unit tests only'''
    return _is_prime(number)


def nearest_primes():
    number = random.randint(10, 200)
    lower_prime = higher_prime = 0
    for i in range(number - 1, 3, -1):
        if (_is_prime(i) == True):
            lower_prime = i
            break
    i = number + 1
    while _is_prime(i) == False:
        i += 1
    higher_prime = i
    answer = "Lower prime: {}, Higher prime: {}".format(lower_prime, higher_prime)
    answers.append(answer)
    question = "The prime numbers that are just before and after {} are _____ and _____.".format(number)
    print (question)
    return (question, answer)


def list_primes():
    number = random.randint(10, 200)
    range_size = random.randint(4, 10)
    answer = []
    for i in range(number, number + range_size + 1):
        if _is_prime(i) == True:
            answer.append(i)
    answers.append(answer)
    question = "The prime numbers between {} and {} are ________".format(number, number + range_size)
    print (question)
    return (question, answer)


def twin_primes():
    first_prime = random.randint(2, 25)
    while (_is_prime(first_prime) is False):
        first_prime += 1
    if (_is_prime(first_prime + 2) is True):
        answer = "The numbers are twin primes."
    else:
        answer = "The numbers are not twin primes."
    answers.append(answer)
    question = "{} and {} are twin primes.  Yes or No?".format(first_prime, first_prime + 2)
    print (question)
    return (question, answer)


def factors(number=0):
    if number <= 0:
        number = random.randint(50, 500)
    factors = []
    n = 1
    while (n <= number):
        if (_is_prime(n) == True or n == 2):
            if (number % n == 0):
                factors.append(n)
                # factors.append (number / n)
        n += 1
    answers.append(factors)
    print("The unique factors of {number} are _________________.".format(number=number))
    return (factors)  # for unit testing


def _all_factors(number=0):
    """Retrieves all the  prime factors of a number, even the duplicate prime factors"""
    factor_list = []
    if _is_prime(number):
        factor_list.append(number)
    else:
        n = 1
        while (n <= number):
            if (_is_prime(n) == True or n == 2):
                if number % n == 0:
                    factor_list.append(n)
                    number //= n
                    n = 1
            n = n + 1
    return (factor_list)

def all_factors (number = 0):
    if (number <= 0):
        number = random.randint(50, 999)
    factor_list = _all_factors (number)
    question = "___"
    for i in range(0, len(factor_list) - 1):
        question = "{} X ___ ".format(question)
    question = "{} = {}, where each number is a prime number".format(question, number)
    print(question)
    answers.append(factor_list)
    return (factor_list)


def consecutive_primes(number=0, num_primes=0):
    if number <= 0 or num_primes <= 0:
        number = random.randint(5, 15)
        num_primes = random.randint(2, 3)
    orig_number = number
    prime_list = []
    while len(prime_list) < num_primes:
        if _is_prime(number):
            prime_list.append(number)
        number = number + 1
    print(
        "The prime factors of a number are {} consecutive primes.  The smallest of these primes is {}.  What are the factors?  What is the number?".format(
            num_primes, prime_list[0]))
    product = 1
    for i in range(0, len(prime_list)):
        product = product * prime_list[i]
    answer = "Factors = {}. Product = {}".format(prime_list, product)
    answers.append(answer)
    return (answer)


def multiples(number=0, number_of_multiples=0):
    if (number <= 0) or (number_of_multiples <= 0):
        number = random.randint(16, 200)
        number_of_multiples = random.randint(4, 8)
    multiple_list = []
    for n in range(1, number_of_multiples + 1):
        multiple_list.append(number * n)
    answers.append(multiple_list)
    print("The first {number_of_multiples} multiples of {number} are ____________".format(
        number_of_multiples=number_of_multiples, number=number))
    return (multiple_list)


def _highest_common_factor(number_list=[]):
    list_length = len(number_list)
    if (len(number_list) <= 1):
        list_length = random.randint(2, 3)
        logging.info("list_length = {}.".format(list_length))
        hcf = random.randint(5, 12)
        for i in range(0, list_length):
            logging.info("index i : {}".format(i))
            number_list.append(hcf * random.randint(2, 25))
        logging.info("Number_list = {}".format(number_list))
    ordered_list = list(number_list)
    ordered_list.sort()
    logging.info("ordered_list = {}".format(ordered_list))
    numerator, denominator = ordered_list.pop(list_length - 1), ordered_list.pop(list_length - 2)
    num_iterations = len(number_list) - 1

    while (num_iterations > 0):
        while (numerator % denominator != 0):
            numerator, denominator = denominator, numerator % denominator
            logging.info("numerator = {}, denominator = {}, remainder = {}".format(numerator, denominator,
                                                                                   numerator % denominator))
        if (len(ordered_list) > 0):
            numerator = ordered_list.pop()
        num_iterations = num_iterations - 1
    # print ("The HCF of {} is _____.".format (number_list))
    #answers.append (denominator)
    return (number_list, denominator)


def highest_common_factor(number_list=[]):
    number_list, hcf = _highest_common_factor(number_list)
    print("The HCF of {} is ______.".format(number_list))
    answers.append(hcf)
    return (hcf)


def _least_common_multiple(number_list=[]):
    '''

    :param number_list - finds the LCM of three numbers:
    :return: the list of numbers and the LCM
    '''
    list_length = len(number_list)
    if list_length <= 2:
        list_length = 3
        for i in range(3):
            number_list.append(random.randint(11, 50))
    greatest = max(number_list)
    while (True):
        divisible = True
        for i in range (0, list_length):
            if greatest % number_list[i] == 0:
                divisible = divisible and True
            else:
                greatest += 1
                divisible = False
                break #out of for loop
        if divisible == True:
            lcm = greatest
            break

    return (number_list, lcm)


def least_common_multiple(number_list=[]):
    number_list, lcm = _least_common_multiple(number_list)
    print("The LCM of {} is ____.".format(number_list))
    answers.append(lcm)
    return lcm


def lcm_and_hcf(number_list=[]):
    if (len(number_list) < 3):
        hcf = random.randint(7, 20)
        i = 0
        while (i < 3):
            number = random.randint(9, 25) * hcf
            if (number not in number_list):
                number_list.append(number)
                i += 1

    number_list, lcm = _least_common_multiple(number_list)
    number_list, hcf = _highest_common_factor(number_list)
    print("The LCM and HCF of {} are _____ and _______ respectively.".format(number_list))
    answers.append([lcm, hcf])
    return (lcm, hcf)

def pole_spacing (triangle_lengths=[]):
    if (len (triangle_lengths) < 3):
        i = 0;
        distance_between_poles = random.randint (5,12)
        while i < 3:
            triangle_lengths.append(random.randint(3,7) * distance_between_poles)
            i += 1
    triangle_lengths, distance_between_poles = _highest_common_factor(triangle_lengths)
    print ("A triangular plot of land is being fenced.  The sides of the plot are {}m, {}m and {}m long."\
           .format (triangle_lengths[0], triangle_lengths[1], triangle_lengths[2]),\
            "What is the greatest whole number of meters apart the fence (poles) posts can be placed and equally spaced.")
    answers.append ("{}m apart".format (distance_between_poles))
    return (distance_between_poles)

def stamp_distribution (stamp_count=[]):
    if len(stamp_count) != 2:
        number_of_members = random.randint (4, 9)
        for i in range (0, 2):
            stamp_count.append(number_of_members * random.randint(3, 8))
    stamp_count, number_of_members = _highest_common_factor(stamp_count)
    stamps_per_member_from_first_set = stamp_count[0]//number_of_members
    stamps_per_member_from_second_set = stamp_count[1]//number_of_members
    print ("Suppose a stamp club president equally distributes two different sets of stamps among club members.",\
           "One set contains {} stamps and the other set contains {} stamps.".format (stamp_count[0], stamp_count[1]), \
           "There are no stamps left undistributed.", "1. What is the greatest possible number of club members?", \
           "2. How many stamps from each set will each person receive?")
    answers.append ("1) {} members, 2) {} stamps from 1st set and {} stamps from 2nd set".format (number_of_members, stamps_per_member_from_first_set, stamps_per_member_from_second_set))
    return (number_of_members, stamps_per_member_from_first_set, stamps_per_member_from_second_set)

def march_past (team_size=[]):
    if len (team_size) != 2 or 0 in team_size:
        people_per_row = random.randint(5,9)
        for i in range (0,2):
            people = people_per_row * random.randint(4,8)
            if i == 1: #ensure that both teams do not have the same number of people
                while (people == team_size[0]):
                    people = people_per_row * random.randint(4,8)
            team_size.append(people)
    print ("Two gymnastic teams are marching at an event. There are {} members on one team and {} on the other"\
        .format (team_size[0], team_size[1]), "They are marching in rows of equal size that are as wide as possible.",\
           "How many people are in each row?")
    team_size, people_per_row = _highest_common_factor(team_size)
    answers.append (people_per_row)
    return people_per_row

def building_age (age_this_year=0):
    age_last_year = age_this_year - 1
    if age_this_year == 0:
        non_primes = [x for x in range (50, 70) if not _is_prime(x) ]
        logging.info (non_primes)
        age_this_year = non_primes[random.randint (0, len(non_primes) -1)]
        age_last_year = age_this_year - 1

        while _is_prime(age_last_year):
            age_this_year = non_primes[random.randint (0, len(non_primes) -1)]
            age_last_year = age_this_year - 1

    logging.info ("Age this year = {}".format(age_this_year))
    factors_age_this_year = _all_factors(age_this_year)
    factors_age_last_year = _all_factors (age_last_year)
    logging.info ("Factors: {} {}".format (factors_age_this_year, factors_age_last_year))
    number_list, lcm = _least_common_multiple([age_this_year, age_last_year])
    age_range = random.randint (5, 10)
    #TODO: Complete this
    print ("A building\'s age this year is a multiple of {}. Last year it was a multiple of {}.".format(factors_age_this_year[1], factors_age_last_year[1]),\
           "It is less than {} years but more than {} years old.  What is the age of the building?".format (age_this_year + age_range, age_this_year - age_range))
    answers.append (age_this_year)
    return (age_this_year)


def _generate_unique_random_numbers (start=0, end=100, count=5):
    if (start >= end) or (count <= 1) or (count > (end - start)):
        return ()
    random_number_set = set()
    while count > 0:
        element = random.randint (start, end)
        if element not in random_number_set:
            random_number_set.add (element)
            count -= 1
    logging.info ("Set of random numbers: {}".format (random_number_set))
    return sorted (random_number_set)

def chocolate_distribution (chocolates_per_friend = [], extra_chocolates=-1):
    person = names[random.randint(0,  len(names) -1)]
    if len (chocolates_per_friend) <3:
        chocolates_per_friend = list(_generate_unique_random_numbers(5, 10, 3))

    logging.info ("Chocolates per friend {}".format (chocolates_per_friend))
    if extra_chocolates < 0:
        extra_chocolates = random.randint (4, 9)
    print ("{person} has some chocolates and he gives each of his friends {choc1} or {choc2} or {choc3} chocolates.  He finds that each time"\
        " {extra} chocolates are left over.  Find the minimum number of chocolates {person} had.   How many friends did he have?"\
        .format (person=person,choc1=chocolates_per_friend[0], choc2=chocolates_per_friend[1], choc3=chocolates_per_friend[2],\
                 extra=extra_chocolates))
    chocs, lcm = _least_common_multiple(chocolates_per_friend)
    num_friends = []
    for i in range (len(chocolates_per_friend)):
        num_friends.append(lcm // chocolates_per_friend[i])
    answers.append ("Total chocolates : {}, number of friends: {}".format (lcm + extra_chocolates, num_friends))
    return (lcm + extra_chocolates, chocolates_per_friend)


def students_in_class (students_per_row=[]):
    if len(students_per_row) < 4:
        students_per_row = _generate_unique_random_numbers(5,18,4)
    print ("Students in a class are made to stand in complete rows of {}, {}, {} or {} each.  What is the minimum number"\
            " of students in that class?".format (students_per_row[0], students_per_row[1], students_per_row[2], students_per_row[3]))
    students, lcm = _least_common_multiple(students_per_row)
    answers.append(lcm)
    return (lcm)

def students_running_circles (circling_time=[]):
    if len (circling_time) < 2:
        circling_time = _generate_unique_random_numbers(7, 15, 2)
    print ("Two boys run around a circular field. They can complete one circle in {} and {} seconds respectively.".format (circling_time[0], circling_time[1]),\
            "If they start from a point together, find after what time will they be together again at the same point."\
            "Also find how many rounds each of them will have completed by that time?")
    lcm = (circling_time[0] * circling_time[1])//gcd(circling_time[0], circling_time[1])
    rounds = []
    for i in range (len(circling_time)):
        rounds.append (lcm//circling_time[i])
    answers.append("They meet at {} seconds.  They complete {} and {} rounds respectively.".format(lcm, rounds[0], rounds[1]))
    return (lcm, rounds)


def journey_time_minimum_hours (hours_per_person=[]):
    if len(hours_per_person) < 3:
        factor = random.randint (2,7)
        for i in range (3, 8, 2):
            hours_per_person.append (factor * i)
    print ("To travel to Delhi, Meena requires a total of {} hours, Rajesh requires a total of {} hours and Priya requires {} hours.".format (hours_per_person[0], hours_per_person[1], hours_per_person[2]),\
           "All the three, travel for an equal number of hours each day.  Find out 1) How many hours all the three spend ",\
            "each day to travel and 2) How many days will it take each of them to travel to Delhi?")
    hours, hcf = _highest_common_factor(hours_per_person)
    days_per_person = []
    for i in range (len (hours_per_person)):
        days_per_person.append (hours_per_person[i]//hcf)
    answers.append ("Hours per day: {}, Days per person : {}".format (hcf, days_per_person))
    return (hcf, days_per_person)


functions = [nearest_primes, list_primes, twin_primes, factors, multiples, all_factors, consecutive_primes, \
             highest_common_factor, least_common_multiple, lcm_and_hcf, pole_spacing, stamp_distribution,\
             march_past, building_age, chocolate_distribution, students_in_class, students_running_circles, journey_time_minimum_hours]


def squat():
    print("hello world")
    for i in range(5):
        yield (i ** 2)


def main():
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(funcName)s:%(message)s', datefmt='%Y%m%d %I:%M:%S %p',
                        filename='class.log', level=logging.INFO)
    unique_id = uuid.uuid1(1)
    print("Question Paper # {}".format(str(unique_id)))
    # random.seed (os.urandom(5))
    for i in range(0, len(functions)):
        logging.info('Function : %s' % functions[i])

        print ("{i}) ".format(i=i+1), end="")
        f = functions[i]
        f()
        logging.info ('Answer  : %s' % answers[i])

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

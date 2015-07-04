__author__ = 'ajay'

'''revision_class_4.py: generates problems corresponding to class 4 (CBSE) curriculum'''

import random
from fractions import Fraction
import uuid
import logging

answers = []


def multiplication ():

    number_lower_limit = 100
    number_higher_limit = 999
    #random.seed()   #TODO: Can be removed?
    multiplicand = random.randint (number_lower_limit, number_higher_limit)
    multiplier = random.randint (number_lower_limit, number_higher_limit)
    if (multiplicand  < multiplier):
        multiplicand, multiplier = multiplier, multiplicand
    answer = multiplicand * multiplier
    answers.append (answer)
    print (multiplicand, "x", multiplier, "=")

def decimal_multiplication ():
    number_lower_limit = 11
    number_higher_limit = 99
    multiplicand = random.randint (number_lower_limit, number_higher_limit)
    multiplier = random.randint (1,1500)
    multiplier = multiplier / 100
    answers.append (round (multiplicand * multiplier, 2))
    print (multiplicand, "X", multiplier, "=")


def addition ():
    number_lower_limit = 10000
    number_higher_limit = 99999
    addend_first = random.randint (number_lower_limit, number_higher_limit)
    addend_second = random.randint (number_lower_limit, number_higher_limit)
    addend_third = random.randint (number_lower_limit, number_higher_limit)
    answer = addend_first + addend_second + addend_third
    answers.append (answer)
    print (addend_first, "+", addend_second,"+", addend_third, "=")

def division ():
    dividend = random.randint (10000, 999999)
    divisor  = random.randint (2, 99)
    quotient = dividend // divisor
    remainder = dividend % divisor
    answer = "Quotient =  {}, Remainder =  {}"  .format (quotient, remainder)
    answers.append (answer)
    print ("Divide {} by {}" .format (dividend, divisor))

def division2 ():
    daily_travel = random.randint (3,9)
    total_travel = random.randint (25, 99)
    if (total_travel % daily_travel == 0):
        answers.append (total_travel//daily_travel)
    else:
        answers.append (1 + total_travel//daily_travel)
    print ("A boy walked {} km each day.  How many days will it take for him to reach the {} km marker stone?".format (daily_travel, total_travel ))

def bodmas1 ():
    number1 = random.randint (9,999)
    number3 = random.randint (2, 9)
    number2 = random.randint (2,9) * number3
    answer = number1 * number2 / number3
    answers.append (answer)
    print ("{} x {} / {} = " .format(number1, number2, number3))

def bodmas2 ():
    number1 = random.randint (9, 999)
    number2 = random.randint (99, 999)
    number3 = random.randint (9,19)
    answer = number1 + number2 * number3
    answers.append (answer)
    print ("{} + {} x {} = ".format (number1, number2, number3))

def bodmas3 ():
    number2 = random.randint (2,19)
    number3 = random.randint (2,19)
    number4 = random.randint (2,19)
    number1 = random.randint (2, 19) + number2*number3 + number4
    answers.append (number1 - number2 * number3 + number4)
    print ("{} - {} * {} + {}".format (number1, number2, number3, number4))

def bodmas4 ():
    number1 = random.randint (2, 19)
    number2 = random.randint (2,19)
    number3 = random.randint (2,19)
    number4 = number1 * number2 + number3
    answers.append (number1)
    print ("_____ * {} + {} = {}".format (number2, number3, number4))



def divisibility ():
    dividends = [2,3,4,9]
    divisor = random.randint (9999, 99999)
    index = random.randint (0, len (dividends)-1)
    if divisor % dividends[index] == 0:
        answer = "{} is divisible by {}".format (divisor, dividends[index])
    else:
        answer = "{} is not divisible by {}".format (divisor, dividends[index])
    answers.append (answer)
    print ("Is {} divisible by {}. Give reasons." .format (divisor, dividends[index]))

def lowest_common_multiple_two_numbers ():
    number1 = random.randint (9, 49)
    number2 = random.randint (2, 19)
    number1_multiples = range (number1, number1 * number2+1, number1)
    number2_multiples = range (number2, number1 * number2+1, number2)
    common_multiples = set (number1_multiples).intersection(number2_multiples)
    common_multiples = list (common_multiples)
    common_multiples.sort()
    print ("LCM of {} and {} is _________.".format (number1, number2))
    answers.append (common_multiples.pop (0))

def lowest_common_multiple_three_numbers ():
    number1 = random.randint (2, 99)
    number2 = random.randint (2, 50)
    number3 = random.randint (2, 50)
    number1_multiples = range (number1, number1 * number2 * number3 +1, number1)
    number2_multiples = range (number2, number1 * number2 * number3 +1, number2)
    number3_multiples = range (number3, number1 * number2 * number3 +1, number3)
    common_multiples = set (number1_multiples).intersection(number2_multiples).intersection(number3_multiples)
    common_multiples = list (common_multiples)
    common_multiples.sort()
    print ("LCM of {}, {} and {} is _________.".format (number1, number2, number3))
    answers.append (common_multiples.pop (0))



def fractions_ascending ():
    fraction1_numerator = random.randint (1, 9)
    fraction1_denominator = random.randint (1,9) + fraction1_numerator
    fraction2_numerator = random.randint (1, 9)
    fraction2_denominator = random.randint (1,9) + fraction2_numerator
    if (Fraction (fraction1_numerator, fraction1_denominator) > Fraction (fraction2_numerator, fraction2_denominator)):
        answer = "{}/{} is the bigger fraction.".format (fraction1_numerator, fraction1_denominator)
    else:
        answer =  "{}/{} is the bigger fraction.".format (fraction2_numerator, fraction2_denominator)
    answers.append (answer)
    print ("Which fraction is greater: {}/{} or {}/{}" .format (fraction1_numerator, fraction1_denominator,fraction2_numerator, fraction2_denominator))

def fractions_sum ():
    fraction1_numerator = random.randint (1, 9)
    fraction1_denominator = random.randint (1,9) + fraction1_numerator
    fraction2_numerator = random.randint (1, 9)
    fraction2_denominator = random.randint (1,9) + fraction2_numerator
    answer = Fraction (fraction1_numerator, fraction1_denominator) + Fraction (fraction2_numerator, fraction2_denominator)
    answers.append (answer)
    print ("The sum of {}/{} and {}/{} is __________" .format (fraction1_numerator, fraction1_denominator,fraction2_numerator, fraction2_denominator))

def fractions_difference ():
    fraction1_numerator = random.randint (1, 9)
    fraction1_denominator = random.randint (1,9) + fraction1_numerator
    fraction2_numerator = random.randint (1, 9)
    fraction2_denominator = random.randint (1,9) + fraction2_numerator
    if (Fraction (fraction1_numerator, fraction1_denominator) > Fraction (fraction2_numerator, fraction2_denominator)):
        answer = Fraction (fraction1_numerator, fraction1_denominator) - Fraction (fraction2_numerator, fraction2_denominator)
        print ("The difference of {}/{} and {}/{} is __________" .format (fraction1_numerator, fraction1_denominator,fraction2_numerator, fraction2_denominator))
    else:
        answer = Fraction (fraction2_numerator, fraction2_denominator) - Fraction (fraction1_numerator, fraction1_denominator)
        print ("The difference of {}/{} and {}/{} is __________" .format (fraction2_numerator, fraction2_denominator,fraction1_numerator, fraction1_denominator))
    answers.append (answer)


def fractions_mixed_to_improper ():
    fraction1_numerator = random.randint (1, 9)
    fraction1_denominator = random.randint (1,9) + fraction1_numerator
    number = random.randint (1, 9)
    answer = Fraction (number) + Fraction (fraction1_numerator, fraction1_denominator)
    answers.append (answer)
    print ("{} {}/{} can be written as _________________.".format (number,fraction1_numerator, fraction1_denominator ))


def fractions_improper_to_mixed ():
    fraction1_denominator = random.randint (2, 19)
    fraction1_numerator = random.randint (1,99) + fraction1_denominator
    number = fraction1_numerator//fraction1_denominator
    numerator = fraction1_numerator % fraction1_denominator
    answer_fraction = Fraction (numerator, fraction1_denominator)
    answer =  "{} {}".format (number, answer_fraction)
    answers.append (answer)
    print ("{}/{}, when converted into a mixed fraction can be written as _____________.".format(fraction1_numerator, fraction1_denominator ))

def length_addition_cm ():
    length1 = random.randint (1, 99)
    length2 = random.randint (1, 99)
    length3 = random.randint (1, 99)
    answer = length1+length2+length3
    if (answer >= 100):
        answer = "{} m, {} cm".format (answer//100, answer % 100)
    else:
        answer = "{} cm".format (answer)
    answers.append (answer)
    print ("Add {} cm, {} cm and {} cm.".format (length1, length2, length3))

def length_addition_metre ():
    length1 = random.randint (1, 999)
    length2 = random.randint (1, 999)
    length3 = random.randint (1, 999)
    answer = length1+length2+length3
    if (answer >= 1000):
        answer = "{} km, {} m".format (answer//1000, answer % 1000)
    else:
        answer = "{} m".format (answer)
    answers.append (answer)
    print ("Add {} m, {} m and {} m.".format (length1, length2, length3))

def length_addition_m_cm_mm ():
    m1 = random.randint (1,999)
    cm1 = random.randint (0, 99)
    mm1 = random.randint (0, 9)
    m2 = random.randint (1,999)
    cm2 = random.randint (0, 99)
    mm2 = random.randint (0, 9)
    print ("{} m {} cm {} mm + {} m {} cm {} mm = ".format (m1,cm1,mm1, m2,cm2, mm2))
    answer = (m1+m2)*1000+(cm1+cm2)*10+(mm1+mm2)   #mm
    m = answer//1000
    cm = (answer - m*1000)//10
    mm = answer % 10
    answer = "{} m {} cm {} mm".format (m, cm, mm)
    answers.append (answer)

def length_addition_km_m ():
    km1 = random.randint (1,999)
    m1 = random.randint (1, 999)
    km2 = random.randint (1,999)
    m2 = random.randint (1, 999)
    answer = (km1+km2)*1000 + (m1+m2)
    km = answer // 1000
    m  = answer % 1000
    answer = "{} km {} m".format (km, m)
    answers.append (answer)
    print ("{} km {} m + {} km {} m =  _____ km ______m".format (km1, m1, km2, m2))

def length_subtraction_m_cm ():
    m1 = random.randint (1,999)
    cm1 = random.randint (0, 99)
    m2 = random.randint (1,999)
    cm2 = random.randint (0, 99)
    while (m1 <= m2):
        m1 = random.randint (1,999)
    answer = (m1 * 100 + cm1) - (m2 * 100 + cm2) #mm
    m = answer//100
    cm = answer % 100
    answer = "{} m {} cm ".format (m, cm)
    answers.append (answer)
    print ("{} m {} cm  - {} m {} cm  = ".format (m1,cm1, m2,cm2,))

def length_subtraction_cm_mm ():
    cm1 = random.randint (1,99)
    mm1 = random.randint (0,9)
    cm2 = random.randint (1,99)
    mm2 = random.randint (0,9)
    while (cm1 <= cm2):
        cm1 = random.randint (1,99)
    answer = (cm1 * 10 + mm1) - (cm2 * 10 + mm2) #mm
    cm = answer//10
    mm = answer % 10
    answer = "{} cm {} mm ".format (cm, mm)
    answers.append (answer)
    print ("{} cm {} mm  - {} cm {} mm  = ".format (cm1,mm1, cm2,mm2))

def length_addition_l_ml ():
    l1 = random.randint (1,999)
    ml1 = random.randint (1, 999)
    l2 = random.randint (1,999)
    ml2 = random.randint (1, 999)
    answer = (l1+l2)*1000 + (ml1+ml2)
    l = answer // 1000
    ml  = answer % 1000
    answer = "{} l {} ml".format (l, ml)
    answers.append (answer)
    print ("{} liters {} ml + {} liters {} ml =  _____ l ______ml".format (l1,ml1, l2, ml2))

def length_subtraction_l_ml ():
    l1 = random.randint (1,999)
    ml1 = random.randint (0, 999)
    l2 = random.randint (1,999)
    ml2 = random.randint (0, 999)
    while (l1 <= l2):
        l1 = random.randint (1,999)
    answer = (l1 * 1000 + ml1) - (l2 * 1000 + ml2)
    l = answer//1000
    ml = answer % 1000
    answer = "{} l {} ml ".format (l, ml)
    answers.append (answer)
    print ("{} liter(s) {} ml  - {} liter(s) {} ml  = ".format (l1,ml1, l2,ml2,))

def meters_into_kms():
    distance = random.randint (1,150)
    answer = distance/1000
    answers.append (answer)
    print ("{} m can also be written as _______ km".format (distance))

def meters_into_kms2():
    distance = random.randint (999, 8000)
    answer = distance/1000
    answers.append (answer)
    print ("{} m can also be expressed as _________ km".format (distance))

def cm_into_meters ():
    cm = random.randint (2, 1500)
    answer = cm / 100
    answers.append (answer)
    print ("{} cm can also be expressed as _________ m".format (cm))

def cm_into_km ():
    distance = random.randint (2,1500)
    answer = distance / (1000*100)
    answers.append (answer)
    print ("{} cm can also be expressed as _________ km".format (distance))

def time_addition ():
    time1_hours = random.randint (1, 11)
    time1_minutes = random.randint (0,59)
    time2_hours = random.randint (1, 11)
    time2_minutes = random.randint (0,59)
    sum = (time1_hours * 60 + time1_minutes) + (time2_hours * 60 + time2_minutes)
    answer = "{} hours {} minutes".format (sum//60, sum % 60)
    answers.append (answer)
    print ("The sum of {} hours {} minutes and {} hours {} minutes is _______".format (time1_hours, time1_minutes, time2_hours, time2_minutes))


def time_subtraction ():
    time1_hours = random.randint (1, 11)
    time1_minutes = random.randint (0,59)
    time2_hours = random.randint (1, 11)
    time2_minutes = random.randint (0,59)
    while (time1_hours <= time2_hours):
        time1_hours = random.randint (1,11)
    difference = (time1_hours * 60 + time1_minutes) - (time2_hours * 60 + time2_minutes)
    answer = "{} hours {} minutes".format (difference//60, difference % 60)
    answers.append (answer)
    print ("The difference between {} hours {} minutes and {} hours {} minutes is _______".format (time1_hours, time1_minutes, time2_hours, time2_minutes))

def time_multiplication1 ():
    days = random.randint (2,16)
    units = ["hours", "minutes", "seconds"]
    unit = random.randint (0, len(units) -1 )

    if units[unit] == "hours":
        answer = days * 24
    elif units[unit] == "minutes":
        answer = days * 24 * 60
    elif units[unit] == "seconds":
        answer = days * 24 * 60 * 60
    answers.append (answer)
    print ("How many {} are there in {} days?".format (units[unit], days))

def time_multiplication2 ():
    #TODO: This results in 2/6, 2/6, which can be converted into like fractions.
    numerator = random.randint (1, 5)
    hour = random.randint (0, 4)
    answers.append (((6 * hour)+numerator) * 60/6)
    print ("{} {}/6 hour(s) is ___________ minutes.".format (hour, numerator))

def word_problem_division_1 ():
    toys = random.randint (12,99)
    cost_per_toy = random.randint (3,39)
    answers.append (cost_per_toy)
    print ("A boy paid Rs {} for {} toys. What is the cost of a toy?".format (toys * cost_per_toy, toys))

def word_problem_division_2 ():
    toys = random.randint (8,19)
    cost_per_toy = random.randint (3,39)
    toys_to_purchase =random.randint (8, 19)
    while (toys_to_purchase == toys):
        toys_to_purchase = random.randint (8, 19)
    answers.append (cost_per_toy * toys_to_purchase)
    print ("A boy paid Rs {} for {} toys.  What is the cost of {} toy(s)?".format (toys * cost_per_toy, toys, toys_to_purchase))

def addition_missing_numbers ():
    addend1 = random.randint (1, 99)
    addend2 = random.randint (1, 99)
    answers.append (addend1)
    print ("_____  + {} = {}.  What is the missing number?".format (addend2, addend1 + addend2))

def addition_missing_decimals2 ():
    addend1 = random.randint (1111, 9999)/100
    addend2 = random.randint (1111, 9999)/100
    answers.append (addend1)
    print ("_____  + %.2f = %.2f.  What is the missing number?" % (addend2, addend1 + addend2))


def subtraction_missing_numbers ():
    minuend = random.randint(101, 999)
    subtrahend = random.randint (9, 99)
    answers.append (subtrahend)
    print ("{} - ______  = {}.  What is the subtrahend?".format (minuend, minuend - subtrahend))

def subtraction_missing_minuend ():
    subtrahend = random.randint (9, 99999)
    difference = random.randint (9, 99999)
    answers.append (subtrahend + difference)
    print ("_____ - {} = {}. What is the minuend?".format (subtrahend, difference))

def series ():
    starting_score = random.randint (9, 20)
    num_matches = random.randint (3,7)
    score = 0
    count = num_matches
    while (count > 0):
        score = score + starting_score + (num_matches - count)
        count = count - 1
    answers.append (score)
    print ("If a batsman scored {0} runs in his first match, {0}+1 in the 2nd match, {0}+2 in the 3rd match... How many runs did he score in {1} matches?".format (starting_score, num_matches))

def leap_year ():
    start_year = random.randrange (1900, 2100, 2)
    answer = "Leap Years : "
    for year in range (start_year, start_year + 6 + 1, 2):
        if (year % 100 == 0) and (year % 400 ==0):
            answer = answer + ' {} '.format (year)
        elif (year % 100 != 0) and (year % 4 == 0):
            answer = answer + ' {} '.format (year)
    answers.append (answer)
    print ("Which of the years between {} and {} are leap years?".format (start_year, start_year + 6))

def currency_addition_subtraction ():
    num_items = random.randint (3,12)
    item_cost = random.randint (99, 1499)
    item_cost = item_cost /100
    total_cost = num_items * item_cost
    amount_to_shopkeeper = (total_cost * 100)//100 + random.randint (3, 23)
    amount_to_shopkeeper = round (amount_to_shopkeeper, 2)
    answers.append (round (amount_to_shopkeeper - total_cost, 2))
    print ("You bought {} items for $ {} each.   You gave the shop keeper $ {}. How much does he owe you?".format (num_items, item_cost, amount_to_shopkeeper))

def batting_average ():
    overs = random.randint (6, 30)
    average = random.randint (4, 19)
    answers.append (average)
    print ("A batsman scored {} runs in {} overs.  What is his batting average?".format (overs * average, overs))

def runs_remaining ():
    sixes = random.randint (3,30)
    fours = random.randint (3,30)
    singles = random.randint (3,30)
    lead = random.randint (1,99)
    answers.append (lead+1)

    print ("Team A scored {} runs.   Team B is playing now and has scored {} 6s, {} 4s and {} singles.   Team B requires ______ additional runs to win.".format (sixes *6 + fours * 4 + singles + lead, sixes, fours, singles))

def run_rate_comparison ():
    overs1 = 20
    run_rate1 = random.randint (4,19)
    overs2 = random.randint (6,18)
    run_rate2 = random.randint (4, 19)
    while (run_rate1 == run_rate2):
        run_rate2 = random.randint (6,18)
    if (run_rate1 > run_rate2):
        answers.append ("Run rate of A is higher.")
    else:
        answers.append ("Run rate of B is higher.")
    print ("Team A scored {} runs in {} overs. Team B scored {} runs in {} balls. Which team has a higher run rate?".format (run_rate1*overs1, overs1, run_rate2*overs2, overs2 * 6))

def multiplication_trip_cost ():
    mileage = random.randint (12, 24)
    distance = random.randint (100, 999)
    cost_per_liter = random.randint (6500, 8400)
    cost_per_liter = cost_per_liter / 100
    answers.append (round (distance * cost_per_liter / mileage, 2))
    print ("A car runs {} km per liter of petrol.  What is the fuel cost incurred to cover a distance of {} km, if a liter of petrol costs Rs {}?".format (mileage, distance, cost_per_liter))

def multiplication_unkwown_multiplicand ():
    multiplicand = random.randint (9, 99)
    multiplier   = random.randint (9, 99)
    answers.append (multiplicand)
    print ("_____  X {} = {}".format (multiplier, multiplicand * multiplier))

def discount():
    coupon1 = random.randint (9, 100)
    coupon2 = random.randint (9, 100)
    marked_price = random.randint (100, 1000) + coupon1 + coupon2
    tax = round (.14 * marked_price, 0)
    amount_paid = marked_price - coupon1 - coupon2 - tax
    amount_in_wallet = amount_paid + random.randrange (20, 200, 10)
    answer = "Amount Paid = {}. Amount remaining = {}".format (amount_paid, amount_in_wallet - amount_paid )
    answers.append (answer)
    print ("Raju bought a shirt marked for Rs {}.  He redeemed two coupons worth Rs {} and Rs {} and paid a tax of Rs {}".format (marked_price, coupon1, coupon2, tax))
    print ("  How much did he pay?  If he had Rs {} in his wallet, what is the balance after purchase? ".format ( amount_in_wallet))


if __name__ == '__main__':
    unique_id = uuid.uuid1(1)
    print ("Question Paper # {}".format (str(unique_id)))
    number_of_questions = random.randint (18, 25)
    i = 1

    logging.basicConfig (format = '%(asctime)s - %(levelname)s - %(message)s', datefmt= '%Y%m%d %I:%M:%S %p',filename='class.log', level=logging.INFO)


    question_low_range  = 400
    question_high_range = 443

    while (number_of_questions > 0):
        question = random.randint (question_low_range, question_high_range + 1)
        logging.info ('Question # %d' %question)
        #print ('{}) '.format (i))
        if (question == 400):
            multiplication ()
        elif (question == 401):
            addition ()
        elif (question == 402):
            division ()
        elif (question == 403):
            bodmas1()
        elif (question == 404):
            bodmas2()
        elif (question == 405):
            divisibility()
        elif (question == 406):
            lowest_common_multiple_two_numbers()
        elif (question == 407):
            lowest_common_multiple_three_numbers()
        elif (question == 408):
            fractions_ascending()
        elif (question == 409):
            fractions_sum()
        elif (question == 410):
            fractions_difference()
        elif (question == 411):
            fractions_mixed_to_improper()
        elif (question == 412):
            fractions_improper_to_mixed()
        elif (question == 413):
            length_addition_cm()
        elif (question == 414):
            length_addition_metre()
        elif (question == 415):
            length_addition_m_cm_mm()
        elif (question == 416):
            length_addition_km_m()
        elif (question == 417):
            length_subtraction_m_cm()
        elif (question == 418):
            length_subtraction_cm_mm()
        elif (question == 419):
            length_addition_l_ml()
        elif (question == 420):
            length_subtraction_l_ml()
        elif (question == 421):
            meters_into_kms()
        elif (question == 422):
            meters_into_kms2()
        elif (question == 423):
            cm_into_meters()
        elif (question == 424):
            cm_into_km()
        elif (question == 425):
            time_subtraction()
        elif (question == 426):
            word_problem_division_1()
        elif (question == 427):
            word_problem_division_2()
        elif (question == 428):
            addition_missing_numbers()
        elif (question == 429):
            subtraction_missing_numbers()
        elif (question == 430):
            subtraction_missing_minuend()
        elif (question == 431):
            time_multiplication1()
        elif (question == 432):
            series()
        elif (question == 433):
            time_addition()
        elif (question == 434):
            leap_year()
        elif (question == 435):
            bodmas3()
        elif (question == 436):
            decimal_multiplication()
        elif (question == 437):
            currency_addition_subtraction()
        elif (question == 438):
            time_multiplication2()
        elif (question == 439):
            division2 ()
        elif (question == 440):
            addition_missing_decimals2()
        elif (question == 441):
            batting_average()
        elif (question == 442):
            runs_remaining()
        elif (question == 443):
            run_rate_comparison()
        elif (question == 444):
            multiplication_trip_cost()
        elif (question == 445):
            multiplication_unkwown_multiplicand()
        elif (question == 446):
            bodmas4()
        elif (question == 447):
            discount ()
        else:
            fractions_sum()

        number_of_questions = number_of_questions - 1
        i = i + 1



    #print (answers)
    #print (len(answers))
    #addition_missing_decimals2()
    multiplication_trip_cost()
    multiplication_unkwown_multiplicand()
    bodmas4()
    discount ()





    print ("Answer Key # {}".format (str(unique_id)))
    i = 1;
    for answer in answers:
        print ("{}: {}".format (i, answer))
        i = i+1


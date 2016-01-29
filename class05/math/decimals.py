__author__ = 'Ajay'

'''Generates questions on fractions'''
'''Usage: python <this_file.py> > test.html''' #test.html can be opened in  a browser to view the fraction problems
''' Output: Generates a html file, with the questions and answers'''
# references : https://docs.python.org/2/library/decimal.html
#              https://docs.python.org/2/library/fractions.html
#              http://meta.math.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference

import random
import logging
import uuid
# from fractions import Fraction
from fractions import Fraction
import decimal
from fraction import printable_fraction, printable_fraction_from_fraction

questions = []
answers = []

style = r'<style>body{font-size:16;font-family:Verdana;}</style>'
html_pre_context = r'<html> <head> <title> Home Work Problems - Decimals </title>' + r'<script type="text/x-mathjax-config">MathJax.Hub.Config({' + \
  r'tex2jax: {' + r"inlineMath: [ ['$','$'], ['\\(','\\)'] ]" + \
  r'}' + r'})'+ r'</script><script type="text/javascript" src = "https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" ></script> ' +\
  style + r'</head > <body> '
html_post_content = r'</body></html>'

'''Generates a fraction ranging from 1...9/2..9'''

def generate_decimal (integer=999, mantissa=9999):
    return decimal.Decimal ('%d.%d' %(random.randint(0, integer), random.randint(0, mantissa)))

def decimal_to_fraction (number = decimal.Decimal()):
    if number == decimal.Decimal():
        number = generate_decimal(0, 999)
    number_in_fraction = Fraction(number)
    answer = printable_fraction_from_fraction(number_in_fraction)
    question = "Convert {} to a fraction. Simplify the fraction, if required.".format(number)
    return (question, answer)

def multiple_decimals_to_fractions (decimal_list = []):
    dec_list = []
    if not decimal_list:
        i = 0
        if len(decimal_list) <= 4:
            dec_list.append (decimal.Decimal(random.randint(1,9)/1000).quantize(decimal.Decimal('0.001'), rounding=decimal.ROUND_DOWN))
            dec_list.append (decimal.Decimal(random.randint(111,999)/1000).quantize(decimal.Decimal('0.001'), rounding=decimal.ROUND_DOWN))
            dec_list.append (decimal.Decimal(random.randint(1,9)/100).quantize(decimal.Decimal('0.01'), rounding=decimal.ROUND_DOWN))
            dec_list.append (generate_decimal(0, 9999).quantize(decimal.Decimal('0.001'), rounding=decimal.ROUND_DOWN))

        decimal_list = dec_list
    fraction_list = []
    answer = ""
    question = ""
    for i in range (0, len (decimal_list)):
        fraction_list.append( Fraction(decimal_list[i]))
        answer += printable_fraction_from_fraction(fraction_list[i])
        question += " {}".format (decimal_list[i])
        if i != len (decimal_list) -1:
            answer += ","
            question += ","
    question = "Convert the decimals into their equivalent fractions : {}".format (question)
    return (question, answer)

def decimals_sum():
    decimal1 = generate_decimal(0, 99)
    decimal2 = generate_decimal(99, 9999)
    answer = decimal1 + decimal2
    question = "The sum of {} and {} is __________".format(decimal1, decimal2)
    return (question, answer)

def decimals_mantissa_sum ():
    decimal1 = generate_decimal(0, 99)
    decimal2 = generate_decimal(0, 9999)
    answer = decimal1 + decimal2
    question = "The sum of {} and {} is __________".format(decimal1, decimal2)
    return (question, answer)

def decimals_difference ():
    minuend = generate_decimal(99, 99)
    subtrahend= generate_decimal(49, 99999)
    while (minuend <= subtrahend):
        minuend += generate_decimal(10, 9)
    question = "The difference between {} and {} is __________".format(minuend, subtrahend)
    answer = minuend - subtrahend
    return (question, answer)

def sort_decimals (decimals_list = [], ascending=True):
    list = []
    if  not decimals_list:
        i = 0
        while len (list) < 4:
            dec = generate_decimal(1, 9999)
            if dec not in list:
                list.append(dec)
                i+=1
    else:
        list = decimals_list
    logging.info ("Decimals to be sorted: {}".format(list))
    sorted_decimals_list = sorted(list)
    if ascending is not True:
        sorted_decimals_list.reverse()
    question_sub_text = ""
    for i in range (0, len(list)):
        question_sub_text += str(list[i])
        if i != len (list)-1:
            question_sub_text += ','
    if ascending is True:
        order = "ascending"
    else:
        order = "descending"
    question = 'Arrange the decimals {} in {} order'.format (question_sub_text, order )
    logging.info (question)
    answer = ""
    for i in range (0, len(list)):
        answer += str(sorted_decimals_list[i])
        if i != len (list)-1:
            answer += ','
    logging.info (answer)
    logging.info (sorted_decimals_list)
    return (question, answer)

def sort_decimals_descending (fractions_list = [], ascending=False):
    return sort_decimals(fractions_list, ascending)


def decimals_multiplication (number1=decimal.Decimal(), number2=decimal.Decimal()):
    if number1 == decimal.Decimal() or number2 == decimal.Decimal():
        number1 = generate_decimal(9,99)
        number2 = generate_decimal(999,9999)
    answer = number1 * number2
    question = "The product of {} and {} is _____. ".format (number1,number2)
    return (question, answer)

def decimals_integers_multiplication (number1=decimal.Decimal(), number2=0):
    if number1 == decimal.Decimal() or number2 == 0:
        number1 = generate_decimal(0,99)
        number2 = random.randint (5,50)
    answer = number1 * number2
    question = "{} x {} = ______".format (number1, number2)
    return (question, answer)


def decimals_division (number1=decimal.Decimal(), number2=decimal.Decimal()):
    if number1 == decimal.Decimal() or number2 == decimal.Decimal():
        number1 = generate_decimal(99,9999)
        number2 = generate_decimal(9,99)
    current_precision = decimal.getcontext().prec
    decimal.getcontext().prec = 6
    answer = number1 / number2
    decimal.getcontext().prec = current_precision
    question = "Divide {} by {}. Stop the division at 4 places after decimal point.".format (number1, number2)
    return (question, answer)

def decimals_integers_division (number1=decimal.Decimal(), number2=0):
    if number1 == decimal.Decimal() or number2 == 0:
        number1 = generate_decimal(4,99)
        number2 = random.randint (4,9)
    original_precision = decimal.getcontext().prec
    decimal.getcontext().prec=5
    answer = number1 / number2
    decimal.getcontext().prec = original_precision
    question = "{} divided by {} = ______".format (number1, number2)
    return (question, answer)

def integers_decimals_division (number1=0, number2= decimal.Decimal()):
    if number1 == 0 or number2 == decimal.Decimal():
        number1 = random.randint (19, 300)
        number2 = generate_decimal(9,9)
    original_precision = decimal.getcontext().prec
    decimal.getcontext().prec=4
    answer = number1 / number2
    decimal.getcontext().prec = original_precision
    question = "{} divided by {} = ______".format (number1, number2)
    return (question, answer)


def percentage_of_whole_numbers (percentage=0, whole_number=0):
    if percentage == 0 or whole_number == 0:
        percentage = random.randint (2,15)*5
        whole_number = random.randint (2,19) * 5
    answer = whole_number * percentage / 100
    question = "{}% of {} is _______.".format (percentage, whole_number)
    return  (question, answer)

def decimal_as_percentage (number1=decimal.Decimal()):
    if number1 == decimal.Decimal():
        number1 = generate_decimal(0, 999)
    answer = number1 * 100
    answer = float(answer)
    question = "{} can be expressed as ____%.".format (number1)
    return (question, answer)

def fraction_as_percentage (number = Fraction ()):
    if number == Fraction():
        possible_denominators = [2, 5, 10, 20, 25, 50]
        selection = random.randint (0, len (possible_denominators)-1)
        denominator = possible_denominators[selection]
        numerator = random.randint(2, 15)
        while (numerator == denominator and numerator % denominator != 0):
            numerator = random.randint (2, 15)
        number = Fraction(numerator, denominator)
        logging.info ("{} {} {}".format (selection, denominator, printable_fraction_from_fraction(number)))
    question = "Express fraction {} as a percentage.".format (printable_fraction_from_fraction(number))
    original_precision = decimal.getcontext().prec
    decimal.getcontext().prec = 2
    answer = number.numerator * 100/number.denominator
    answer = "{} %".format (answer)
    decimal.getcontext().prec = original_precision
    return (question, answer)


functions = [decimals_sum, decimals_mantissa_sum, decimals_difference, sort_decimals, sort_decimals_descending, decimals_multiplication, \
             decimals_division, decimal_to_fraction, multiple_decimals_to_fractions, decimals_integers_multiplication, decimals_integers_division,\
              integers_decimals_division,percentage_of_whole_numbers, decimal_as_percentage, fraction_as_percentage]


def main():
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y%m%d %I:%M:%S %p',
                        filename='class.log', level=logging.INFO)
    unique_id = uuid.uuid1(1)

    for i in range(0, len(functions)):
        logging.info('Function : %s' % functions[i])
        f = functions[i]
        question, answer = f()
        questions.append(question)
        answers.append(answer)
    html_text = "<h1>Decimals & Percentages</h1>\n"
    html_text += "<h2>Questions: {}</h2>\n".format(str(unique_id)[:8])
    html_text += r'<ol>'
    for i in range(0, len(questions)):
        html = "    <li> {} </li>\n".format (questions[i])
        html_text += html
    html_text += r'</ol>'
    html_text += r'<br/><hr>'
    html_text += "<h2>Answer Key: {}</h2>\n".format(str(unique_id)[:8])
    html_text += r'<ol>'
    for i in range(0, len(questions)):
        html = "    <li> {} </li>\n".format (answers[i])
        html_text += html
    html_text += r'</ol>'
    print ("{} {} {}".format(html_pre_context, html_text, html_post_content))


if __name__ == "__main__":
    main()

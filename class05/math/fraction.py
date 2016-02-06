__author__ = 'Ajay'

'''Generates questions on fractions'''
'''Usage: python <this_file.py> > test.html''' #test.html can be opened in  a browser to view the fraction problems
''' Output: Generates a html file, with the questions and answers'''
# references : https://docs.python.org/2/library/fractions.html
#              http://meta.math.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference

import random
import logging
import uuid
# from fractions import Fraction
from fractions import Fraction


questions = []
answers = []

style = r'<style>body{font-size:16;font-family:Verdana;}</style>'
html_pre_context = r'<html> <head> <title> Quiz on fractions </title>' + r'<script type="text/x-mathjax-config">MathJax.Hub.Config({' + \
  r'tex2jax: {' + r"inlineMath: [ ['$','$'], ['\\(','\\)'] ]" + \
  r'}' + r'})'+ r'</script><script type="text/javascript" src = "https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" ></script> ' +\
  style + r'</head > <body> '
html_post_content = r'</body></html>'

'''Generates a fraction ranging from 1...9/1..9'''
def __generate_fraction ():
    f = Fraction(random.randint(1,9),random.randint(2,9) )
    while f.denominator == 1: #eliminates fractions with a denominator of 1fr
        f = Fraction(random.randint(1,9),random.randint(2,9) )
    return f

def __generate_mixed_fraction ():
    frac = __generate_fraction()
    while frac.denominator == 1:
        frac = __generate_fraction()
    return frac + random.randint (1,9)

'''input: numerator and denominator
   output: a string, that appears as a fraction in LaTeX format
   '''
def printable_fraction (numerator: int, denominator: int):
    printable = "$\\frac {" + str(numerator) +"}{" +  str(denominator) + "}$"
    return printable

'''Takes a Fraction data structure'''
def printable_fraction_from_fraction (fraction: Fraction):
    return printable_fraction(fraction.numerator, fraction.denominator)

def printable_mixed_fraction (fraction: Fraction):
    if fraction.numerator <= fraction.denominator:
        return printable_fraction_from_fraction(fraction)
    else:
        whole_number = fraction.numerator // fraction.denominator
        fraction = fraction - whole_number
        printable = "${}".format(whole_number) +"\\frac {" + str(fraction.numerator) +"}{" +  str(fraction.denominator) + "}$"
        return printable


def fractions_sum():
    fraction1_numerator = random.randint(1, 9)
    fraction1_denominator = random.randint(2, 9) + fraction1_numerator
    fraction2_numerator = random.randint(1, 9)
    fraction2_denominator = random.randint(2, 9) + fraction2_numerator
    answer = Fraction(fraction1_numerator, fraction1_denominator) + Fraction(fraction2_numerator, fraction2_denominator)
    question = "The sum of {} and {} is __________".format(printable_fraction(fraction1_numerator, fraction1_denominator),
                                                                 printable_fraction(fraction2_numerator, fraction2_denominator))
    answer = printable_fraction (answer.numerator, answer.denominator)
    return (question, answer)

def fractions_difference ():
    subtrahend= Fraction (random.randint(1, 9), random.randint(2,9))
    difference = Fraction (random.randint(1, 9),random.randint(2, 5))
    minuend = subtrahend + difference
    question = "The difference between {} and {} is __________".format(printable_fraction_from_fraction(minuend),
                                                                 printable_fraction_from_fraction(subtrahend))
    answer = minuend - subtrahend
    answer = printable_fraction (answer.numerator, answer.denominator)
    return (question, answer)



def sort_unlike_fractions (fractions_list = [], ascending=True):
    list = []
    if  not fractions_list:
        i = 0
        while len (list) < 4:
            frac = __generate_fraction()
            if frac not in list:
                list.append(frac)
                i+=1
    else:
        list = fractions_list
    logging.info ("Fractions to be sorted: {}".format(list))
    sorted_fraction_list = sorted(list)
    if ascending is not True:
        sorted_fraction_list.reverse()
    question_sub_text = ""
    for i in range (0, len(list)):
        question_sub_text += printable_fraction_from_fraction(list[i])
        if i != len (list)-1:
            question_sub_text += ','
    if ascending is True:
        order = "ascending"
    else:
        order = "descending"
    question = 'Arrange the fractions {} in {} order'.format (question_sub_text, order )
    logging.info (question)
    answer = ""
    for i in range (0, len(list)):
        answer += printable_fraction_from_fraction(sorted_fraction_list[i])
        if i != len (list)-1:
            answer += ','
    logging.info (answer)
    logging.info (sorted_fraction_list)

    return (question, answer)

def sort_unlike_fractions_descending (fractions_list = [], ascending=False):
    return sort_unlike_fractions(fractions_list, ascending)

def mixed_fractions_sum (number1=Fraction(), number2=Fraction()):
    if number1 == Fraction() or number2 == Fraction():
        number1 = __generate_mixed_fraction()
        number2 = __generate_mixed_fraction()
    answer = number1 + number2
    #logging.info (number1, number2, answer)
    question = "The sum of {} and {} is _____. Convert any improper fraction into a mixed fraction.".format (printable_mixed_fraction(number1), printable_mixed_fraction(number2))
    return (question, printable_mixed_fraction(answer))

def mixed_fractions_difference (number1=Fraction(), number2=Fraction()):
    if number1 == Fraction() or number2 == Fraction():
        number1 = __generate_mixed_fraction()
        number2 = __generate_mixed_fraction()
        while number2 >= number1:
            number2 = __generate_mixed_fraction()
    answer = number1 - number2
    #logging.info (number1, number2, answer)
    question = "The difference of {} and {} is _____. Convert any improper fraction into a mixed fraction.".format (printable_mixed_fraction(number1), printable_mixed_fraction(number2))
    return (question, printable_mixed_fraction(answer))

def mixed_fractions_multiplication (number1=Fraction(), number2=Fraction()):
    if number1 == Fraction() or number2 == Fraction():
        number1 = __generate_mixed_fraction()
        number2 = __generate_fraction()
    answer = number1 * number2
    question = "The product of {} and {} is _____. Convert any improper fraction into a mixed fraction.".format (printable_mixed_fraction(number1), printable_fraction_from_fraction(number2))
    return (question, printable_mixed_fraction(answer))

def fractions_division (number1=Fraction(), number2=Fraction()):
    if number1 == Fraction() or number2 == Fraction():
        number1 = __generate_fraction()
        number2 = __generate_fraction()

    answer = number1 / number2
    question = "Divide {} by {}. Convert any improper fraction into a mixed fraction.".format (printable_fraction_from_fraction(number1), printable_fraction_from_fraction(number2))
    return (question, printable_mixed_fraction(answer))

def fractions_division_by_whole_number (number1=Fraction(), number2=0):
    if number1 == Fraction() or number2 == 0:
        number1 = __generate_fraction()
        number2 = random.randint (3,9)
    answer = number1 / number2
    question = "Divide {} by {}.".format (printable_fraction_from_fraction(number1), number2)
    return (question, printable_fraction_from_fraction(answer))

def whole_number_by_fractions_division (number1=0, number2=Fraction()):
    if number2 == Fraction() or number1 == 0:
        number2 = __generate_fraction()
        number1 = random.randint (3,9)
    answer = number1 / number2
    question = "Divide {} by {}.".format (number1, printable_fraction_from_fraction(number2))
    return (question, printable_fraction_from_fraction(answer))

def mixed_fractions_division (number1=Fraction(), number2=Fraction()):
    if number1 == Fraction() or number2 == Fraction():
        number1 = __generate_mixed_fraction()
        number2 = __generate_mixed_fraction()
    answer = number1 / number2
    question = "Divide {} by {}. Convert any improper fraction into a mixed fraction.".format (printable_mixed_fraction(number1), printable_mixed_fraction(number2))
    return (question, printable_mixed_fraction(answer))


functions = [fractions_sum, fractions_difference, sort_unlike_fractions, sort_unlike_fractions_descending, mixed_fractions_sum, \
             mixed_fractions_difference, mixed_fractions_multiplication,fractions_division, fractions_division_by_whole_number, \
             whole_number_by_fractions_division, mixed_fractions_division]


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
    html_text = "<h1>Decimals</h1>\n"
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

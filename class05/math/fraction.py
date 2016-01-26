__author__ = 'Ajay'

'''Generates questions on fractions'''
'''Usage: python <this_file.py> '''
''' Output: Generates a html file, with the questions and answers'''

import random
import logging
# from fractions import Fraction
from fractions import Fraction

questions = []
answers = []

html_pre_context = r'<html> <head> <title> Quiz on fractions </title>' + r'<script type="text/x-mathjax-config">MathJax.Hub.Config({' + \
  r'tex2jax: {' + r"inlineMath: [ ['$','$'], ['\\(','\\)'] ]" + \
  r'}' + r'})'+ r'</script><script type="text/javascript" src = "https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" ></script> </head > <body> '
html_post_content = r'</body></html>'


def fractions_sum():
    fraction1_numerator = random.randint(1, 9)
    fraction1_denominator = random.randint(1, 9) + fraction1_numerator
    fraction2_numerator = random.randint(1, 9)
    fraction2_denominator = random.randint(1, 9) + fraction2_numerator
    answer = Fraction(fraction1_numerator, fraction1_denominator) + Fraction(fraction2_numerator, fraction2_denominator)

    #print ('{}/{}'.format (fraction2_numerator, fraction2_denominator))
    question = "The sum of {} and {} is __________".format(printable_fraction(fraction1_numerator, fraction1_denominator),
                                                                 printable_fraction(fraction2_numerator, fraction2_denominator))
    answer = printable_fraction (answer.numerator, answer.denominator)
    answers.append (answer)
    return (question, answer)

def fractions_difference ():
    subtrahend_numerator = random.randint(1, 9)
    subtrahend_denominator = random.randint(1, 11) + subtrahend_numerator
    difference_numerator = random.randint(1, 5)
    difference_denominator = random.randint(1, 9) + difference_numerator
    minuend = Fraction (subtrahend_numerator, subtrahend_denominator) + Fraction (difference_numerator, difference_denominator)
    question = "The difference between {} and {} is __________".format(printable_fraction(minuend.numerator, minuend.denominator),
                                                                 printable_fraction(subtrahend_numerator, subtrahend_denominator))
    answer = minuend - Fraction(subtrahend_numerator, subtrahend_denominator)
    answer = printable_fraction (answer.numerator, answer.denominator)
    answers.append (answer)
    return (question, answer)


'''input: numerator and denominator
   output: a string, that appears as a fraction in LaTeX format
   '''
def printable_fraction (numerator: int, denominator: int):
    printable = "$\\frac {" + str(numerator) +"}{" +  str(denominator) + "}$"
    return printable

functions = [fractions_sum, fractions_difference]


def main():
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y%m%d %I:%M:%S %p',
                        filename='class.log', level=logging.INFO)
    #random.seed (os.urandom(5))
    for i in range(0, len(functions)):
        logging.info('Function : %s' % functions[i])
        f = functions[i]
        question, answer = f()
        questions.append(question)
        answers.append(answer)


    html_text = r'<ul>'
    for i in range(0, len(questions)):
        html = "<li> {} </li>".format (questions[i])
        html_text += html

        #print(answer)
    #html_text += r'$\frac {2}{9}$'
    html_text += r'</ul>'
    print ("{} {} {}".format(html_pre_context, html_text, html_post_content))
        #primes = [ _is_prime(x) for x in range (100)]
        #print (primes)
        #for i in squat ():
        #    print (i)

        #for i in range (100, 500):
        #   print (i, all_factors(i))


if __name__ == "__main__":
    main()

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

html_pre_context = r'<html> <head> <title> Quiz on fractions </title><script type="text/javascript" src = "https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" ></script> </head > <body> '
html_post_content = r'</body></html>'


def fractions_sum():
    fraction1_numerator = random.randint(1, 9)
    fraction1_denominator = random.randint(1, 9) + fraction1_numerator
    fraction2_numerator = random.randint(1, 9)
    fraction2_denominator = random.randint(1, 9) + fraction2_numerator
    answer = Fraction(fraction1_numerator, fraction1_denominator) + Fraction(fraction2_numerator, fraction2_denominator)
    #answers.append (answer)
    question = "The sum of {}/{} and {}/{} is __________".format(fraction1_numerator, fraction1_denominator,
                                                                 fraction2_numerator, fraction2_denominator)
    return (question, answer)


functions = [fractions_sum]


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
        html = "<li> {} </li>".format (question)
        html_text += html

        #print(answer)
    html_text += r'$$\frac {2}{9}$$'
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
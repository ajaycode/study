__author__ = 'Ajay'

'''Generates questions on money'''
'''Usage: python <this_file.py> > test.html''' #test.html can be opened in  a browser to view the fraction problems
''' Output: Generates a html file, with the questions and answers'''
# references : https://docs.python.org/2/library/decimal.html
#              https://docs.python.org/2/library/fractions.html
#              http://meta.math.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference

import random
import logging
import uuid
import datetime
import re
from factors import is_prime
from decimals import *
from fraction import __generate_fraction,__generate_mixed_fraction, printable_fraction_from_fraction, printable_mixed_fraction
from fractions import Fraction

chapter = r'Simplification of Numerical Expressions'

questions = []
answers = []

style = r'<style>body{font-size:16;font-family:Verdana;}</style>'
html_pre_context = r'<html> <head> <title> Home Work Problems - {} </title>' + r'<script type="text/x-mathjax-config">MathJax.Hub.Config({' + \
  r'tex2jax: {' + r"inlineMath: [ ['$','$'], ['\\(','\\)'] ]" + \
  r'}' + r'})'+ r'</script><script type="text/javascript" src = "https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" ></script> ' +\
  style + r'</head > <body> '.format (chapter)
today = datetime.date.today()
today = today.strftime("%B %d, %Y")

html_post_content = r'</body></html>'

division_sign = '&#247;'#u'\N{DIVISION SIGN}'
multiplication_sign = '&times;'#u'\N{MULTIPLICATION SIGN}'

def __generate_random_number (min=2, max=25):
    number =  random.randint (min, max)
    while is_prime(number):
        number = random.randint (min, max)
    return number

def __generate_operations (num_operations = 4): #num_operations = number of arithmetic operators present in the equation
    operations = ["+", "-", "*", "/"]
    ops_list = [] #the list of operations to be performed and the order in which they are to be performed
    for i in range (0, num_operations):
        if i > 0:
            if ops_list[i-1] == "/":   #eliminates consecutive divisions
                ops_list.append (operations[random.randint(0, len(operations)-2)])
            else:
                ops_list.append (operations[random.randint(0, len(operations)-1)])
        else:
            ops_list.append (operations[random.randint(0, len(operations)-1)])
    return ops_list

def __generate_expression (numbers_list, ops_list):
    if numbers_list == None or len (numbers_list) == 0 or ops_list == None or len (ops_list) == 0:
        logging.info ("Invalid parameters passed to function.")
        return False
    expression = ""
    for i in range (0, len (numbers_list)):
        expression += "{}".format (numbers_list[i])
        if i <= len (numbers_list) -2:
            expression += " {} ".format (ops_list[i])
    return expression

def __printable_expression (expression:str): #replaces "/" and "*" by the appropriate mathematical signs, using unicode
    expression = re.sub ("/", division_sign, expression)
    expression = re.sub ("\*", multiplication_sign, expression)
    return expression

def __printable_expression_fractions (fraction_list, ops_list):
    if fraction_list == None or len (fraction_list) == 0 or ops_list == None or len (ops_list) == 0:
        logging.info ("Invalid parameters passed to function.")
        return False
    expression = ""
    for i in range (0, len (fraction_list)):
        if fraction_list[i].numerator > fraction_list[i].denominator:
            expression += "{}".format (printable_mixed_fraction(fraction_list[i]))
        else:
            expression += "{}".format (printable_fraction_from_fraction(fraction_list[i]))
        if i <= len (fraction_list) -2:
            expression += " {} ".format (ops_list[i])
    return expression


def __factors(number=0):
    if number <= 0:
        number = random.randint(50, 500)
    factors = []
    n = 1
    while (n <= number):
      if (number % n == 0):
        factors.append(n)
        # factors.append (number / n)
      n += 1
    return (factors[1:-1])  # for unit testing



def bodmas_integers (expression = None, num_operations = 5):
    numbers_list = []
    if expression == None:
        ops_list = __generate_operations(num_operations)
        for i in range (0, num_operations + 1):
            if i == 0:
                numbers_list.append(__generate_random_number(50, 100))
            elif   i < len (ops_list) and  ops_list[i] == "/" and ops_list[i]:#ensures that there are no prime numbers before a / sign. Else the divisors are either the number or 1.
                numbers_list.append( __generate_random_number(50, 200))

            else:
                if ops_list[i-1] == "/":

                    factor_list = __factors (numbers_list[i-1])
                    logging.info ("i : {}, numbers_list : {}, factor_list: {}".format (i, numbers_list,factor_list))
                    divisor = factor_list[random.randint(0, len(factor_list)-1)]
                    numbers_list.append(divisor)
                else:
                    numbers_list.append(__generate_random_number())
        #Both numbers and operators are available.  Construct the mathematical expression
        expression = __generate_expression (numbers_list, ops_list)
    answer = eval (expression)
    question = __printable_expression(expression)
    return (question, answer)

def bodmas_decimals (expression = None, num_operations = 4):
    numbers_list = []
    multiplier = 1
    if expression == None:
        ops_list = __generate_operations(num_operations)
        for i in range (0, num_operations + 1):
            if i == 0:
                numbers_list.append(generate_decimal (2, 99))
            elif   i < len (ops_list) and  ops_list[i] == "/" and ops_list[i]:#ensures that there are no prime numbers before a / sign. Else the divisors are either the number or 1.
                multiplier = random.randint (5,9)
                numbers_list.append(generate_decimal (2, 99) * multiplier)
            else:
                if ops_list[i-1] == "/":
                    orig = decimal.getcontext().prec
                    decimal.getcontext().prec = 3
                    divisor = numbers_list[i-1]/multiplier
                    decimal.getcontext().prec = orig
                    numbers_list.append(divisor)
                else:
                    numbers_list.append(generate_decimal (0, 9))
        #Both numbers and operators are available.  Construct the mathematical expression
        expression = __generate_expression (numbers_list, ops_list)
    orig = decimal.getcontext().prec
    decimal.getcontext().prec = 3
    answer = round (eval (expression), 3)
    decimal.getcontext().prec = orig
    question = __printable_expression(expression)
    return (question, answer)


def bodmas_fractions (expression = None, num_operations = 4):#TODO: expression passed as input is ignored.  Add support for inputs, passed as strings
    numbers_list = []
    if expression == None:
        ops_list = __generate_operations(num_operations)
        for i in range (0, num_operations + 1):
            numbers_list.append(__generate_fraction ())
        #Both numbers and operators are available.  Construct the mathematical expression
        expression = __printable_expression(__printable_expression_fractions (numbers_list, ops_list))
    answer = bodmas_fractions_solver(numbers_list, ops_list)
    question = expression
    return (question, answer)

'''This function is similar to the built-in eval, but this provides the answer for fractions
This function is called by the bodmas_fractions function.
'''
def bodmas_fractions_solver (fraction_list, operations_list):
    if not operations_list or not fraction_list or len (operations_list) == 0 or len (fraction_list) == 0 or \
        len (operations_list) + 1 != len(fraction_list):
        return False
    ans = Fraction ()
    #pass 1, solve division problems
    while "/" in operations_list:
        pos = operations_list.index ("/")
        ans = fraction_list[pos] / fraction_list[pos+1]
        fraction_list[pos] = ans
        operations_list.remove("/")
        fraction_list.remove(fraction_list[pos+1])
    while "*" in operations_list: #pass 2, all multiplication operations are done
        pos = operations_list.index ("*")
        ans = fraction_list[pos] * fraction_list[pos+1]
        fraction_list[pos] = ans
        operations_list.remove("*")
        fraction_list.remove(fraction_list[pos+1])
    while "+" in operations_list: #pass 3 for addition operations
        pos = operations_list.index ("+")
        ans = fraction_list[pos] + fraction_list[pos+1]
        fraction_list[pos] = ans
        operations_list.remove("+")
        fraction_list.remove(fraction_list[pos+1])
    while "-" in operations_list: #pass 4 for subtraction
        pos = operations_list.index ("-")
        ans = fraction_list[pos] - fraction_list[pos+1]
        fraction_list[pos] = ans
        operations_list.remove("-")
        fraction_list.remove(fraction_list[pos+1])
    return ans



def bodmas_mixed_fractions (num_operations = 3):
    numbers_list = []
    expression = None
    if expression == None:
        ops_list = __generate_operations(num_operations)
        for i in range (0, num_operations + 1):
            numbers_list.append(__generate_mixed_fraction ())
        #Both numbers and operators are available.  Construct the mathematical expression
        expression = __printable_expression(__printable_expression_fractions (numbers_list, ops_list))
    answer = bodmas_fractions_solver(numbers_list, ops_list)
    question = expression
    return (question, answer)



functions = [bodmas_integers, bodmas_decimals, bodmas_fractions, bodmas_mixed_fractions]


def main():
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y%m%d %I:%M:%S %p',
                        filename='class.log', level=logging.INFO)
    unique_id = uuid.uuid1(1)

    f_list = [Fraction (200, 2),Fraction (1,4),Fraction (2,3),Fraction (1,3),Fraction (2,3)]
    ops_list = ["/", "*", "+", "-"]
    bodmas_fractions_solver(f_list, ops_list)

    num_problems = 0
    while num_problems < 30:
        for i in range(0, len(functions)):
            logging.info('Function : %s' % functions[i])
            f = functions[i]
            question, answer = f()
            if answer > 0 and answer < 5000:
                questions.append(question)
                answers.append(answer)
                num_problems += 1

    html_text = "<h1>{}</h1>\n".format(chapter)
    html_text += today
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

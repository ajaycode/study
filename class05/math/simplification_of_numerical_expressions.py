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
import factors
import re
#from factors import _is_prime

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

division_sign = u'\N{DIVISION SIGN}'
multiplication_sign = u'\N{MULTIPLICATION SIGN}'

def __generate_random_numbers (min=2, max=25):
    return random.randint (min, max)

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

def __printable_expression (expression:str): #replaces "/" and "*" by the appropriate mathematical signs, using unicode
    expression = re.sub ("/", division_sign, expression)
    expression = re.sub ("\*", multiplication_sign, expression)
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
    return (factors[1:])  # for unit testing

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

def bodmas_integers (expression = None, num_operations = 5):
    numbers_list = []
    if expression == None:
        ops_list = __generate_operations(num_operations)
        for i in range (0, num_operations + 1):
            if i == 0:
                numbers_list.append(__generate_random_numbers(50, 100))
            else:
                if ops_list[i-1] == "/":

                    factor_list = __factors (numbers_list[i-1])
                    logging.info ("i : {}, numbers_list : {}, factor_list: {}".format (i, numbers_list,factor_list))
                    divisor = factor_list[random.randint(0, len(factor_list)-1)]
                    numbers_list.append(divisor)
                else:
                    numbers_list.append(__generate_random_numbers())
        #Both numbers and operators are available.  Construct the mathematical expression
        expression = __generate_expression (numbers_list, ops_list)

    answer = eval (expression)
    question = __printable_expression(expression)
    return (question, answer)



def bodmas_fractions (expression = None):
    pass

def bodmas_mixed_fractions (expression = None):
    pass

def bodmas_decimals (expression = None):
    pass



functions = [bodmas_integers]


def main():
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y%m%d %I:%M:%S %p',
                        filename='class.log', level=logging.INFO)
    unique_id = uuid.uuid1(1)

    for i in range (0, 10):
        for i in range(0, len(functions)):
            logging.info('Function : %s' % functions[i])
            f = functions[i]
            question, answer = f()
            questions.append(question)
            answers.append(answer)
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

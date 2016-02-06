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
import decimal
from decimal import ROUND_UP
from fraction import printable_fraction, printable_fraction_from_fraction
import datetime

chapter = r'Temperature'

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


def __get_random_temperature_in_fahrenheit ():
    return random.randint (32, 212)

def __get_random_temperature_in_celsius ():
    return random.randint (1, 100)

celsius = lambda fahrenheit : (fahrenheit - 32) * 5/9

fahrenheit = lambda celsius: (9/5)* celsius + 32

def celsius_from_fahrenheit (temperature = None ):
    if temperature == None:
        temperature = __get_random_temperature_in_fahrenheit()
    answer = "{}{}C".format (round (celsius (temperature), 1), u'\N{DEGREE SIGN}')
    question = "Convert {}{}F into Celsius.".format(temperature, u'\N{DEGREE SIGN}')
    return (question, answer)

def fahrenheit_from_celsius (temperature = None):
    if temperature == None:
        temperature = __get_random_temperature_in_celsius()
    answer = "{}{}F".format (round (fahrenheit (temperature), 1), u'\N{DEGREE SIGN}')
    question = "Convert {}{}C into Fahrenheit.".format(temperature, u'\N{DEGREE SIGN}')
    return (question, answer)





functions = [celsius_from_fahrenheit, fahrenheit_from_celsius]


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

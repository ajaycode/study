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
# from fractions import Fraction
from fractions import Fraction
import decimal
from fraction import printable_fraction, printable_fraction_from_fraction

questions = []
answers = []

style = r'<style>body{font-size:16;font-family:Verdana;}</style>'
html_pre_context = r'<html> <head> <title> Home Work Problems - Money </title>' + r'<script type="text/x-mathjax-config">MathJax.Hub.Config({' + \
  r'tex2jax: {' + r"inlineMath: [ ['$','$'], ['\\(','\\)'] ]" + \
  r'}' + r'})'+ r'</script><script type="text/javascript" src = "https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" ></script> ' +\
  style + r'</head > <body> '
html_post_content = r'</body></html>'

names = ['Rahul', 'Gaurav', 'Rama', 'Utkarsh', 'Govind', 'Akash', 'Anand']
items = ['soap', 'chocolate', 'ice-cream', 'pant', 'eraser', 'orange']

def __get_name ():
    i = random.randint(0, len(names)-1)
    return names[i]

def __get_item ():
    return items[random.randint(0, len(items)-1)]

'''returns soaps, if soap is provided to it, ie, returns the plural form'''
def __get_plural (item:str):
    if item:
        return "{}s".format (item)

def purchase_costs_input_costs_selling_price (cost_price=0, input_costs=0, selling_price=0):
    if not cost_price or not input_costs or not selling_price:
        cost_price = random.randint (4000, 5000)
        input_costs = random.randint (500, 900)
        selling_price = cost_price + input_costs + random.randint (-500, 1500)
    answer = selling_price - (cost_price + input_costs)
    item = __get_plural(__get_item())
    question = "Some quantity of {} was bought for Rs {}. Rs {} was spent on transportation. The items were sold for Rs {}.  What was the profit or loss?  Indicate if it was a profit or loss."\
                 .format (item, cost_price, input_costs, selling_price)
    return (question, answer)

def cost_input_loss (cost_price=0, input_costs=0, loss=0):
    if cost_price == 0 or input_costs ==0 or loss ==0:
        cost_price = random.randint (800,850)
        input_costs = random.randint (100, 150)
        loss = random.randint (200, 300)
    answer = cost_price + input_costs - loss
    question = "{} were bought for Rs {}. Packing charges were Rs {}. Loss incurred was Rs {}. What was the selling price?".format (__get_plural(__get_item()), \
                                        cost_price, input_costs, loss)
    return (question, answer)

def selling_price_profit (selling_price=0, profit = 0):
    if selling_price == 0 or profit ==0:
        selling_price = random.randint (8000, 11000)
        profit = random.randint (800, 1100)
    answer = selling_price - profit
    question = "A set of {items} was sold for Rs {sp} at a profit of Rs {profit}.  What was its cost price?".format (items=__get_plural(__get_item()), sp=selling_price, profit=profit)
    return  (question, answer)

def bulk_purchase_with_unit_loss (bulk_purchase_price = 0, units = 0, unit_loss = 0):
    if bulk_purchase_price == 0 or units == 0 or unit_loss == 0:
        units = random.randint (31, 55)
        bulk_purchase_price = units * random.randint (31, 55)
        unit_loss = random.randint (5, 11)
    answer = bulk_purchase_price - unit_loss * units
    question = "A wholesaler purchases {} kg of sugar for Rs {} and sells each kilogram of sugar at a loss of Rs {}. Calculate the amount, he would get at the end of the sale."\
               .format (units, bulk_purchase_price, unit_loss)
    return (question, answer)

def bulk_purchase_with_unit_profit (bulk_purchase_price = 0, units = 0, unit_profit = 0):
    if bulk_purchase_price == 0 or units == 0 or unit_profit == 0:
        units = random.randint (31, 55)
        bulk_purchase_price = units * random.randint (31, 55)
        unit_profit = random.randint (5, 11)
    answer = bulk_purchase_price + unit_profit * units
    question = "A wholesaler purchases {} kg of sugar for Rs {} and sells each kilogram of sugar at a profit of Rs {}. Calculate the amount, he would get at the end of the sale."\
               .format (units, bulk_purchase_price, unit_profit)
    return (question, answer)

def unit_profit_on_bulk_sale (bulk_purchase_price=0, bulk_sale_price = 0, units = 0):
    if (bulk_purchase_price == 0 or bulk_sale_price == 0 or units == 0):
        units = random.randint (12, 19)
        unit_cost_price = random.randint (6, 14)
        unit_sale_price = unit_cost_price + random.randint (2,6)
        bulk_purchase_price = unit_cost_price * units
        bulk_sale_price = unit_sale_price * units
    answer = (bulk_sale_price - bulk_purchase_price)/units
    question = "{} units of {} were bought for Rs {} and sold for Rs {}.   Find the profit or loss per unit?".format (units, __get_plural(__get_item()), bulk_purchase_price, bulk_sale_price)
    return (question, answer)


functions = [purchase_costs_input_costs_selling_price, cost_input_loss, selling_price_profit, bulk_purchase_with_unit_loss, bulk_purchase_with_unit_profit, \
             unit_profit_on_bulk_sale]


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

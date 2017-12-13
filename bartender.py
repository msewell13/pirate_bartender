import random


questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

name = input('Hi! what is your name?')
responses = ['y', 'yes', 'si', 'ye', 'yeah', 'ok', 'sure']

def get_preferences():
    answers = {}
    for question in questions:
        answer = input('{} y/n: '.format(questions.get(question)))
        if answer in responses:
            answer = True
        else:
            answer = False
        answers[question] = answer
    return answers
  
    
def make_drink(preferences):
    drink = []
    for item in preferences:
        if preferences[item] == True:
            drink.append(random.choice(ingredients[item]))
    return drink
            
        
        
if __name__ == '__main__':

    while True:
        resp1 = get_preferences()
        resp2 = make_drink(resp1)
        print(resp2)
        order_more = input('Would you like another?: ')
        if not order_more in responses:
            break
    
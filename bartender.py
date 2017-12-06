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


def ask():
    answers = {}
    for question in questions:
        answer = input('{} y/n: '.format(questions.get(question)))
        if answer == 'y' or answer == 'yes':
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
            # print(item)
            # print(preferences.get(item))
            # drink.append(random.choice(item))
        else:
            pass
    return drink
            
        
        
if __name__ == '__main__':
    resp1 = ask()
    print(resp1)
    resp2 = make_drink(resp1)
    print(resp2)
    
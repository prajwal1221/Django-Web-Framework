from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def drinks(request, drink_name):
    drinks_dict = {
        'mocha': 'type of coffee',
        'tea': 'type of beverage',
        'lemonade': 'type of refreshment',
    }

    choice_of_drink = drinks_dict.get(drink_name, "Sorry, we don't have that drink.")

    return HttpResponse(f"<h2>{drink_name}</h2>{choice_of_drink}")
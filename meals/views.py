from django.shortcuts import render
from .models import Meals

# Create your views here.

def meal_list(request):
    meal_list = Meals.objects.all()

    contex = { 'meal_list' : meal_list }

    return render(request, 'Meals/list.html', contex)

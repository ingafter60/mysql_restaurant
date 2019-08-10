from django.shortcuts import render
from .models import Meals, Category

# Create your views here.

def meal_list(request):
    meal_list = Meals.objects.all()
    categories = Category.objects.all()

    context = { 
    	'meal_list' : meal_list, 
    	'categories' : categories,
    }

    return render(request, 'Meals/list.html', context)

def meal_detail(request, slug):
    meal_detail = Meals.objects.get(slug=slug)

    context = { 'meal_detail' : meal_detail }

    return render(request, 'Meals/detail.html', context)

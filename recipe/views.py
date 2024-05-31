from django.shortcuts import render
from .models import Category, Recipe


def main(request):
    recipes = Recipe.objects.order_by('?')[:10]
    return render(request, 'main.html', {
        'recipes': recipes
    })


def category_detail(request, category_id):
    category = Category.objects.get(id=category_id)
    recipes = Recipe.objects.filter(category=category)
    return render(request, 'category_detail.html', {
        'category': recipes
    })
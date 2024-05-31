from django.shortcuts import render
from .models import Category, Recipe


def main(request):
    """
    Renders the main page with 10 randon recipes
    """
    recipes = Recipe.objects.order_by('?')[:10]

    return render(request, 'main.html', {
        'recipes': recipes
    })


def category_detail(request, category_id):
    """
    Renders the category detail page with all recipes associated with that category by some category id
    """
    category = Category.objects.get(id=category_id)
    recipes_in_category = category.categories.all()

    return render(request, 'category_detail.html', {
        'category': recipes_in_category
    })
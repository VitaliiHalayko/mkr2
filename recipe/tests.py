from django.test import TestCase
from recipe.models import Recipe, Category
from django.urls import reverse
from django.utils import timezone


class CategoryModelTest(TestCase):
    def setUp(self):
        """
        Set up a recipe
        """
        self.category = Category.objects.create(name="Desserts")

    def test_category_creation(self):
        """
        Test a new category creating
        """
        self.assertEqual(self.category.name, "Desserts")
        self.assertEqual(str(self.category), "Desserts")


class RecipeModelTest(TestCase):
    def setUp(self):
        """
        Set up a recipe
        """
        self.category = Category.objects.create(name="Desserts")
        self.recipe = Recipe.objects.create(
            title="Chocolate Cake",
            description="Delicious chocolate cake recipe.",
            instructions="Mix ingredients and bake.",
            ingredients="Flour, sugar, cocoa, eggs, milk, butter.",
            category=self.category
        )

    def test_recipe_creation(self):
        """
        Test a new recipe creating
        """
        self.assertEqual(self.recipe.title, "Chocolate Cake")
        self.assertEqual(self.recipe.description, "Delicious chocolate cake recipe.")
        self.assertEqual(self.recipe.instructions, "Mix ingredients and bake.")
        self.assertEqual(self.recipe.ingredients, "Flour, sugar, cocoa, eggs, milk, butter.")
        self.assertEqual(self.recipe.category, self.category)
        self.assertEqual(str(self.recipe), "Chocolate Cake")


class MainViewTestCase(TestCase):
    def test_main_view(self):
        """
        Test the main page loading
        """
        self.category = Category.objects.create(name="Test Category")

        for i in range(5):
            Recipe.objects.create(
                title=f"Recipe {i}",
                description=f"Description {i}",
                instructions=f"Instructions {i}",
                ingredients=f"Ingredients {i}",
                category=self.category
            )

        response = self.client.get(reverse('main'))

        self.assertEqual(response.status_code, 200)

        self.assertQuerysetEqual(
            response.context['recipes'],
            Recipe.objects.all(),
            ordered=False
        )


class CategoryDetailViewTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Test Category")

        for i in range(5):
            Recipe.objects.create(
                title=f"Recipe {i}",
                description=f"Description {i}",
                instructions=f"Instructions {i}",
                ingredients=f"Ingredients {i}",
                category=self.category
            )

    def test_category_detail_view(self):
        """
        Test the category detail page loading
        """
        response = self.client.get(reverse('category_detail', args=(self.category.id, )))

        recipes_in_category = self.category.categories.all()

        self.assertEqual(response.status_code, 200)

        self.assertQuerysetEqual(
            response.context['category'],
            recipes_in_category,
            ordered=False
        )

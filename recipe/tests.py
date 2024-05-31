from django.test import TestCase
from recipe.models import Recipe, Category


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
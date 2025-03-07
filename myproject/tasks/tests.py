from django.test import TestCase
from .models import Task

class TaskModelTest(TestCase):
    def test_create_task(self):
        task = Task.objects.create(title="Test Task", description="Test Desc", completed=False)
        self.assertEqual(task.title, "Test Task")
        self.assertFalse(task.completed)

# Create your tests here

from django.test import TestCase
from .models import Task

class TaskModelTest(TestCase):

    def setUp(self):
        
        self.task1 = Task.objects.create(
            title='Test Task 1',
            description='This is the first test task',
            completed=False
        )
        self.task2 = Task.objects.create(
            title='Test Task 2',
            description='This is the second test task',
            completed=True
        )

    def test_task_creation(self):
        self.assertEqual(self.task1.title, 'Test Task 1')
        self.assertEqual(self.task2.description, 'This is the second test task')
        self.assertFalse(self.task1.completed)
        self.assertTrue(self.task2.completed)

    def test_task_str(self):
        self.assertEqual(str(self.task1), 'Test Task 1')
        self.assertEqual(str(self.task2), 'Test Task 2')

    def test_list_tasks(self):
        # Retrieve all tasks
        tasks = Task.objects.all()
        self.assertEqual(tasks.count(), 2)  # Ensure there are 2 tasks
        self.assertIn(self.task1, tasks)   # Check if task1 is in the list
        self.assertIn(self.task2, tasks)   # Check if task2 is in the list
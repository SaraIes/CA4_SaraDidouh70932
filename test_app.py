import unittest
from app import filter_tasks_by_degree, Task

class TestFilterTasksByDegree(unittest.TestCase):
    
    def setUp(self):
        self.tasks = [
            Task("Task 1", "important"),
            Task("Task 2", "unimportant"),
            Task("Task 3", "important"),
            Task("Task 4", "unimportant"),
            Task("Task 5", "important"),
            Task("Task 6", "unimportant")
        ]
    
    def test_filter_tasks_important(self):
        expected = [
            Task("Task 1", "important"),
            Task("Task 3", "important"),
            Task("Task 5", "important")
        ]
        filtered_tasks = filter_tasks_by_degree(self.tasks, "important")
        self.assertEqual(filtered_tasks, expected)
    
    def test_filter_tasks_unimportant(self):
        expected = [
            Task("Task 2", "unimportant"),
            Task("Task 4", "unimportant"),
            Task("Task 6", "unimportant")
        ]
        filtered_tasks = filter_tasks_by_degree(self.tasks, "unimportant")
        self.assertEqual(filtered_tasks, expected)

if __name__ == '__main__':
    unittest.main()

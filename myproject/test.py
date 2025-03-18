import requests
import unittest

BASE_URL = "http://127.0.0.1:8000/api/tasks/"


class APITestCase(unittest.TestCase):
    def setUp(self):
        self.task_data = {"title": "Test Task", "description": "Test Description", "completed": False}
        self.response = requests.post(BASE_URL, json=self.task_data)
        self.task_id = self.response.json().get('id')

    def test_create_task(self):
        self.assertEqual(self.response.status_code, 201)
        self.assertEqual(self.response.json()['title'], self.task_data['title'])

    def test_get_all_tasks(self):
        response = requests.get(BASE_URL)
        self.assertEqual(response.status_code, 200)

    def test_update_task(self):
        updated_data = {"title": "Updated Task", "description": "Updated Description", "completed": True}
        response = requests.put(f"{BASE_URL}{self.task_id}/", json=updated_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['title'], "Updated Task")

    def test_delete_task(self):
        response = requests.delete(f"{BASE_URL}{self.task_id}/")
        self.assertEqual(response.status_code, 204)


if __name__ == "__main__":
    unittest.main(verbosity=2)

import unittest
from data import save_notes_json, load_notes_from_file

class MyTestCase(unittest.TestCase):
    def test_save_notes_json(self):
        notes = [{'username': 'Test', 'title': 'Test Note'}]
        save_notes_json(notes, 'test')
        load_notes = load_notes_from_file('test')
        self.assertEqual(notes, load_notes)  # add assertion here


if __name__ == '__main__':
    unittest.main()

import unittest
import task1

class TestTask1(unittest.TestCase):
    def test_no_emotions(self):
        data = 'Я починил кодировку и теперь могу использовать кириллицу'
        result = 0
        self.assertEqual(result, task1.solve(data))

    def test_breaked_emotions(self):
        data = 'Hello X< ) :<0 ; <) X-) ;<there)'
        result = 0
        self.assertEqual(result, task1.solve(data))

    def test_one_emotion(self):
        data = 'X-{/'
        result = 1
        self.assertEqual(result, task1.solve(data))
    
    def test_many_emotions(self):
        data = 'X-{/X-{/X-{/X-{/X-{/X-{/ X-{/ X-{/'
        result = 8
        self.assertEqual(result, task1.solve(data))

    def test_emotions_with_splits(self):
        data = '[]X-{/ PIIKT love Balakshin XXX-{////         X-{/X-{/X-{/X-{'
        result = 6
        self.assertEqual(result, task1.solve(data))

if __name__ == '__main__':
    unittest.main()
import unittest

class Test_fileTestFail(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.context = app.app_context()
        self.globals = app
        self.app.testing = True

    def test_ttev1_isNotfound(self):
        result = self.app.get('/ttev1')
        self.assertEqual(result.status_code,200)

        
    def test_ttev1json_isNotfound(self):
        result = self.app.get('/answersttev1.json')
        self.assertEqual(result.status_code,404)

        
    def test_w1_isNotfound(self):
        result = self.app.get('/w1')
        self.assertEqual(result.status_code,404)

               
    def test_w1json_isNotfound(self):
        result = self.app.get('/answersw1.json')
        self.assertEqual(result.status_code,404)

        
    def test_ttev2_isNotfound(self):
        result = self.app.get('/ttev2')
        self.assertEqual(result.status_code,404)

                
    def test_ttev2json_isNotfound(self):
        result = self.app.get('/answersttev2.json')
        self.assertEqual(result.status_code,404)

        
    def test_w2_isNotfound(self):
        result = self.app.get('/w2')
        self.assertEqual(result.status_code,404)

                
    def test_w2json_isNotfound(self):
        result = self.app.get('/answersw2.json')
        self.assertEqual(result.status_code,404)

if __name__ == '__main__':
    unittest.main()

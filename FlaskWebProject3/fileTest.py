import unittest, logging
from flask import Flask
from app import app
import json

class Test_fileTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.context = app.app_context()
        self.globals = app
        self.app.testing = True

    def test_home_isfound(self):
        result = self.app.get('/home')
        self.assertEqual(result.status_code,200)


    def test_ttev1_isfound(self):
        result = self.app.get('/ttev1')
        self.assertEqual(result.status_code,200)

        
    def test_ttev1json_isfound(self):
        result = self.app.get('/answersttev1.json')
        self.assertEqual(result.status_code,200)

        
    def test_w1_isfound(self):
        result = self.app.get('/w1')
        self.assertEqual(result.status_code,200)

               
    def test_w1json_isfound(self):
        result = self.app.get('/answersw1.json')
        self.assertEqual(result.status_code,200)

        
    def test_ttev2_isfound(self):
        result = self.app.get('/ttev2')
        self.assertEqual(result.status_code,200)

                
    def test_ttev2json_isfound(self):
        result = self.app.get('/answersttev2.json')
        self.assertEqual(result.status_code,200)

        
    def test_w2_isfound(self):
        result = self.app.get('/w2')
        self.assertEqual(result.status_code,200)

                
    def test_w2json_isfound(self):
        result = self.app.get('/answersw2.json')
        self.assertEqual(result.status_code,200)




if __name__ == '__main__':
    unittest.main()

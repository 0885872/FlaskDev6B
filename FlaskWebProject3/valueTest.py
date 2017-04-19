import unittest, logging
from flask import Flask
from app import app
import json



class Test_test1(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.context = app.app_context()
        self.globals = app
        self.app.testing = True

    def test_ttev1JSONcheck(self):
        result = self.app.get("/answersttev1.json")
        self.assertGreaterEqual(len(json.loads(result.data[10:])),1)

    def test_ttev2JSONcheck(self):
        result = self.app.get("/answersttev2.json")
        self.assertGreaterEqual(len(json.loads(result.data[10:])),1)

    def test_w1JSONcheck(self):
        result = self.app.get("/answersw1.json")
        self.assertGreaterEqual(len(json.loads(result.data[10:])),1)

    def test_w2JSONcheck(self):
        result = self.app.get("/answersw2.json")
        self.assertGreaterEqual(len(json.loads(result.data[10:])),1)





if __name__ == '__main__':
    unittest.main()

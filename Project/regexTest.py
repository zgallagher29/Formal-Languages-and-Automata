import sys
from regex import checkValid
import unittest
import time

class MyTest(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()
        import regex
    def tearDown(self):
        t = time.time() - self.startTime-1
        print ("%s: %.3f" % (self.id(), t))
    def testEmail(self):
        time.sleep(1)
        self.assertTrue(checkValid('^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$','zgallagher@gmail.com'))
    
    def testNotEmail(self):
        time.sleep(1)
        self.assertFalse(checkValid('^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$','zgallaghergmail.com'))
    def testEmail10(self):
        time.sleep(1)
        self.assertTrue(checkValid('^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$','zgallagherzgallagherzgallagherzgallagherzgallagherzgallagherzgallagherzgallagherzgallagherzgallagher@gmail.comgmail.comgmail.comgmail.comgmail.comgmail.comgmail.comgmail.comgmail.com'))
    





if __name__ == '__main__':
    unittest.main() 
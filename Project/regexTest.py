import sys
from regex import checkValid
import unittest
import time

class MyTest(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()
       
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
    

    def testMention(self):
        time.sleep(1)
        self.assertTrue(checkValid('(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z]+[A-Za-z0-9_]+)', '@banana'))
    def testMention10(self):
        time.sleep(1)
        self.assertTrue(checkValid('(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z]+[A-Za-z0-9_]+)', '@bananabananabananabananabananabananabananabananabananabananabananabananabananabananabananabanana'))
    
    def testNotMention(self):
        time.sleep(1)
        self.assertFalse(checkValid('(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z]+[A-Za-z0-9_]+)', '#banana'))
    def testTopic(self):
        time.sleep(1)
        self.assertTrue(checkValid('(?<=^|(?<=[^a-zA-Z0-9-_\.]))#([A-Za-z]+[A-Za-z0-9_]+)', '#banana'))
    def testNotTopic(self):
        time.sleep(1)
        self.assertFalse(checkValid('(?<=^|(?<=[^a-zA-Z0-9-_\.]))#([A-Za-z]+[A-Za-z0-9_]+)', '@banana'))
    def testTopic10(self):
        time.sleep(1)
        self.assertTrue(checkValid('(?<=^|(?<=[^a-zA-Z0-9-_\.]))#([A-Za-z]+[A-Za-z0-9_]+)', '#bananabananabananabananabananabananabananabananabananabananabananabananabananabananabananabanana'))
    
    def testNotBackTrack(self):
        time.sleep(1)
        self.assertTrue(checkValid('(x+x+)+y','xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxy'))
    def testBackTrack15(self):
        time.sleep(1)
        self.assertFalse(checkValid('(x+x+)+y','xxxxxxxxxxxxxxx'))
    def testBackTrackBig25(self):
        time.sleep(1)
        self.assertFalse(checkValid('(x+x+)+y','xxxxxxxxxxxxxxxxxxxxxxxxxxx'))

    def testTweet(self):
        time.sleep(1)
        self.assertTrue(checkValid('^\s*(?:\S\s*){10,250}$', 'a good tweet from me'))
    def testNotTweet(self):
        time.sleep(1)
        self.assertFalse(checkValid('^\s*(?:\S\s*){10,250}$', 'a good tweet from mea good tweet from mea good tweet from mea good tweet from mea good tweet from mea good tweet from mea good tweet from mea good tweet from mea good tweet from mea good tweet from mea good tweet from mea good tweet from mea good tweet from mea good tweet from mea good tweet from mea good tweet from me'))
    
    



if __name__ == '__main__':
    unittest.main()
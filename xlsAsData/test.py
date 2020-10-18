from unittest import TestCase
from unittest import main
from random import randint
from .base import XlsAsData

class Tests(TestCase):

    def test_one(self):
        obj = XlsAsData('test.xlsx', 'title,content')
        testVal = obj.create({
            'title': 'Lorem ipsum',
            'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
        })

        self.assertIsInstance(
            testVal,
            list
        )

        for uuid in testVal:
            self.assertIsInstance(
                uuid,
                str
            )

    def test_two(self):
        obj = XlsAsData('test.xlsx', 'title,content')
        data = obj.read()

        self.assertIsInstance(
            data,
            list
        )

        for row in data:
            self.assertIsInstance(
                row,
                dict
            )

    def test_three(self):
        obj = XlsAsData('test.xlsx', 'title,content')
        testVal = str(randint(1000, 9999))
        uuids = obj.create({
            'title': 'test row',
            'content': testVal
        })

        #update
        x = obj.update(
            uuids[0],
            {
                'title': 'new Test Row',
                'content': str(randint(1000, 9999))
            }
        )
        self.assertIsInstance(
            x,
            bool
        )

        self.assertEqual(
            x,
            True
        )


        

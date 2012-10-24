#!/usr/bin/env python
"""
 * Copyright (c) 2012. Julien Lengrand-Lambert <jlengrand[at]gmail[dot]com>.
 * Released to public domain under terms of the BSD Simplified license.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *   * Redistributions of source code must retain the above copyright
 *     notice, this list of conditions and the following disclaimer.
 *   * Redistributions in binary form must reproduce the above copyright
 *     notice, this list of conditions and the following disclaimer in the
 *     documentation and/or other materials provided with the distribution.
 *   * Neither the name of the organization nor the names of its contributors
 *     may be used to endorse or promote products derived from this software
 *     without specific prior written permission.
 *
 *   See <http://www.opensource.org/licenses/bsd-license>

Unit tests for the Observer module.
See README for more information about this Observer implementation

May coverage be with me
 """

import unittest
import Observer as obs


class TestObserver(unittest.TestCase):
    """
    Testing all classes from Observer module
    """
    def setUp(self):
        """
        Method called before each test
        """
        self.myObservable = obs.Observable()

        self.default_mess = "message"

        self.name1 = "myObserver1"
        self.myObserver1 = obs.Observer(self.name1)
        self.name2 = "myObserver2"
        self.myObserver2 = obs.Observer(self.name2)
        pass

    def tearDown(self):
        """
        Method called after each test
        """
        pass

    def testObserver(self):
        """
        Checks for Exception if strange input
        """
        # Normal behavior
        self.assertEquals(self.myObserver1.name, self.name1)
        self.assertEquals(str(self.myObserver1), self.name1)
        self.assertRaises(TypeError, lambda: obs.Observer(42))

        # tests message
        self.assertEquals(self.myObserver1.message, self.default_mess)
        new_message = "new_message"
        self.myObserver1.update(new_message)
        self.assertEquals(self.myObserver1.message, new_message)
        self.assertRaises(TypeError, lambda: self.myObserver1.update([4, 2]))
        self.assertRaises(TypeError, lambda: self.myObserver1.update(None))


    def testSubscribe(self):


        pass



    def testUnsubscribe(self):
        pass

    def testNotify(self):
        pass

    def testNameUnicity(self):
        pass















if __name__ == '__main__':
    unittest.main()
    # a = Observer("riri")
    # b = Observer("fifi")
    # c = Observer("loulou")

    # d = Observable()

    # d.subscribe(a)
    # d.subscribe(b)
    # d.subscribe(b)
    # d.subscribe(c)

    # d.unsubscribe(b)

    # d.set_val(3)
    # d.set_val()
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
        self.ut = obs.ObsUtility()

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

        # tests message and update
        self.assertEquals(self.myObserver1.message, None)
        new_message = '{"name": "Bob","group": "","type": "","data": 42}'
        self.myObserver1.update(new_message)
        self.assertEquals(self.myObserver1.message, new_message)
        self.assertRaises(TypeError, lambda: self.myObserver1.update([4, 2]))
        self.assertRaises(TypeError, lambda: self.myObserver1.update(None))


    ## Observable
    def testIsJsonValid(self):
        self.assertEquals(True, self.ut.is_json_valid('{"name": "Bob","group": "","type": "","data": 42}'))
        self.assertEquals(False, self.ut.is_json_valid('{"namee": "Bob","group": "","type": "","data": 42}'))
        self.assertEquals(False, self.ut.is_json_valid('{"name": "Bob","group": "","type": ""}'))

        self.assertEquals(False, self.ut.is_json_valid('{"name": "Bob","group": "","type": "","data": 42, "last":"weekend"}'))

    def testObservable(self):
        self.assertRaises(TypeError, lambda: self.myObservable.set_val('{"group": "","type": "","data": 42}'))
        self.assertRaises(TypeError, lambda: self.myObservable.set_val('{"c": 0, "b": 0, "a": 0}'))

        self.assertRaises(TypeError, lambda: self.myObservable.set_val(42))
        self.assertRaises(TypeError, lambda: self.myObservable.set_val(None))

        val = '{"name": "Bob","group": "","type": "","data": 42}'
        self.myObservable.set_val(val)
        self.assertEquals(val, self.myObservable.message)

    def testSubscribe(self):
        self.assertEquals(len(self.myObservable.obs_collection), 0)
        self.assertRaises(TypeError, lambda: self.myObservable.subscribe(42))

        self.myObservable.subscribe(self.myObserver1)
        self.assertRaises(ValueError, lambda: self.myObservable.subscribe(self.myObserver1))  # already there
        self.myObservable.subscribe(self.myObserver2)

        self.assertEquals(len(self.myObservable.obs_collection), 2)

    def testUnsubscribe(self):
        self.myObservable.subscribe(self.myObserver1)
        self.myObservable.subscribe(self.myObserver2)
        self.assertEquals(len(self.myObservable.obs_collection), 2)
        self.myObservable.unsubscribe(self.myObserver1)
        self.assertEquals(len(self.myObservable.obs_collection), 1)

        self.assertRaises(ValueError, lambda: self.myObservable.unsubscribe(self.myObserver1))  # already removed
        self.assertRaises(TypeError, lambda: self.myObservable.unsubscribe("Georges"))

    def testNotify(self):
        self.myObservable.subscribe(self.myObserver1)
        self.myObservable.subscribe(self.myObserver2)

        test = '{"name": "R2D2","group": "","type": "","data": 42}'
        self.myObservable.set_val(test)
        self.assertEquals(self.myObserver1.message, test)
        self.assertEquals(self.myObserver2.message, test)


        self.myObservable.unsubscribe(self.myObserver1)
        test2 = '{"name": "C3PO","group": "","type": "","data": 42}'
        self.myObservable.set_val(test2 )
        self.assertEquals(self.myObserver1.message, test)
        self.assertEquals(self.myObserver2.message, test2)


if __name__ == '__main__':
    unittest.main()
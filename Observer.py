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

The following module is an implementation of the Observer pattern
See.

It is designed to use nothing but built-in python modules.
Simply copy/paste this file and import Observer to start using it.
 """

import json


class Observer():
    """
    Implements Observer entity from Observer pattern.
    An Observer can subscribe to an Observable to receive all future notifications.
    """

    def __init__(self, name="observer"):
        """
        Creates Observer.
        An Observer is uniquely defined by its name.vDefault name is 'observer'.
        """
        if not isinstance(name, str):
            raise TypeError("Expected string for name")

        self.name = name
        self.group = None
        self.message = None

    def update(self, message):
        """
        Automatically called each time Observer receives a notification.
        A notification updates message value
        """
        ut = ObsUtility()

        if ut.is_json_valid(message):
            self.message = message
        else:
            raise TypeError("Expected string for message")

    def __str__(self):
        """
        Simply returns Observer name
        """
        return self.name


class Observable():
    """
    Implements Observable entity from Observer pattern.
    The Observable owns information of interest for one or more other entities.
    Observers subscribe to Observable to receive further notifications.

    Each time message is set, all Observer are notified.
    """

    def __init__(self):
        """
        Creates Observable.
        No subscriber is registered yet.
        Message is set to 'message by default'
        """
        self.message = None
        self.obs_collection = []

    def subscribe(self, observer):
        """
        Adds observer to notification list.
        """
        if not isinstance(observer, Observer):
            raise TypeError("Subscriber must be Observer")

        if (observer in self.obs_collection):
            raise ValueError("Observer already subscribed")
        self.obs_collection.append(observer)

    def unsubscribe(self, observer):
        """
        Removes observer from notification list.
        """
        if not isinstance(observer, Observer):
            raise TypeError("Unsubscriber must be Observer")

        if not(observer in self.obs_collection):
            raise ValueError("Observer not subscribed")
        self.obs_collection.remove(observer)

    def __notify(self, mess):
        """
        Sends notification message to all subscribed observer
        """
        # sends message only to those needed
        dest = json.loads(mess)["name"]

        for observer in self.obs_collection:
            if (len(dest) == 0 ) or (observer.name == dest):
                observer.update(mess)

    def set_val(self, val):
        """
        Shall be used for automatic polling.
        Sets current Observable value and notifies update to subscribers.
        """
        ut = ObsUtility()
        if ut.is_json_valid(val):
            self.message = val
            self.__notify(self.message)
        else:
            raise TypeError("Expecting a valid JSon Object")

        self.message = val  # saves last message sent
        self.__notify(self.message)


class ObsUtility():
    def __init__(self):
        pass

    def is_json_valid(self, val):
        """
        Returns True if val is a valid JSon Object.
        Valid means :
        - correctly formatted
        - contains ONLY all needed 4 sections.
        """
        # json is valid
        mess = json.loads(val)
        # Cheks for the presence of tags
        try:
            #simply access all
            expected = sorted(["name", "group", "type", "data"])  # should be placed somewhere else
            got = sorted(mess.keys())
            return (expected == got)
        except KeyError:
            return False

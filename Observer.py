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
        self.name = name
        self.message = 'message'

    def update(self, message):
        """
        Automatically called each time Observer receives a notification.
        A notification updates message value
        """
        if message is not None:
            self.message = message
            #print "%s received %s" % (self.name, message)

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
        self.message = 'message'
        self.obs_collection = []

    def subscribe(self, observer):
        """
        Adds observer to notification list.
        """
        # FIXME: Check name unique
        try:
            if not(observer in self.obs_collection):
                self.obs_collection.append(observer)
                #print "%s added to collection" % (str(observer))
            else:
                pass
                #print "%s already in collection" % (str(observer))

        except TypeError:
            print "Failed to add %s" % (str(observer))

    def unsubscribe(self, observer):
        """
        Removes observer from notification list.
        """
        try:
            if observer in self.obs_collection:
                self.obs_collection.remove(observer)
                #print "%s removed from collection" % (str(observer))
            else:
                pass
                #print "%s not in collection" % (str(observer))

        except TypeError:
            print "Failed to remove %s" % (str(observer))

    def notify(self, mess):
        """
        Sends notification message to all subscribed observer
        """
        for observer in self.obs_collection:
            #print "sent %s to %s" % (mess, str(observer))
            observer.update(mess)

    def set_val(self, val=None):
        """
        Shall be used for automatic polling.
        Sets current Observable value and notifies update to subscribers.
        """
        self.message = val
        if val != None:
            self.notify(self.message)
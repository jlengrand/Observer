#!/usr/bin/env python

from Observer import Observer
from Observable import Observable

a = Observer("riri")
b = Observer("fifi")
c = Observer("loulou")

d = Observable()

d.subscribe(a)
d.subscribe(b)
d.subscribe(b)
d.subscribe(c)

d.unsubscribe(b)

d.set_val(3)
d.set_val()
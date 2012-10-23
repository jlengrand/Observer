# Python Observer pattern using Json

This module contains a Python implementation of the Observer pattern, using json as a format to share information.

See [Wikipedia for more information]().

## Short description of the implementation

### Observer :

An observer is uniquey defined by its name. This allows Observable to only notify a given Observer if needed.
Observers can subscribe to an Observable and will then receive all future notifications from it.
The notifications are sent in json format.


### Observable :

An Observable is an entity holding information of interest for other entities.
Observers subscribe or unsubscribe to an Observable to get notified any time message is updated.

## Description of the package

The Observer pattern does not need any external module to work. Any simple Python installation (>= 2.6) should be enough.
To use it, simply copy/paste the module file into your code base and load it in yuor code (import Observer)
You are then ready to go !

This package contains several other ressources :
- this README, only used to describe the package and give general information
- testObserver.py, the unit tests of the Observer/Obervable classes.
- exObserver.py, a simple example to show how the Observer pattern can be used.
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

### JSon Structure:

As already explained, the messages sent from the observable to the observers are formatted as a JSon Object.
This allows a simple yet efficient control of the data sent and received while staying in line with the standards.

Each transmitted object should be divided into 4 sections:

- name : The name of the Observer to send the data to. As each Observer is uniquely defined by its name, filling this section means  the data will be sent to **at most** one Observer.
- group : The group of Observers to send the data to. Each Observer may belong to a group. All Observers in the group will then be notified.
- type : the type of message contained in data. This section is not processed by the Observable and is sent as is. It may be blank, or contain anything.
- data : The actual data to be transmitted to the Observers

Here is are several examples of valid JSon message :

#### Data will be sent to Bob only. No particular message type
{
    "name": 'Bob',
    "group": '',
    "type": '',
    "data": 42
}

#### Data will be sent to all Observers in the GUI group. We may assess that this is an update :).
{
    "name": '',
    "group": 'GUI',
    "type": 'Update',
    "data": 'coffee'
}

#### No group, neither name specified. All subscribers will be notified. the message is an array of value object.
{
    "name": '',
    "group": '',
    "type": '',
    "data": ["baz", null, 1.0, 2]
}

According to the [JSon specifications](http://json.org/),
_A value can be a string in double quotes, or a number, or true or false or null, or an object or an array._

**NOTE:** group handling is currently not implemented.
In future improvements, It may also be possible to provide several names or group if needed.

## Description of the package

The Observer pattern does not need any external module to work. Any simple Python installation (>= 2.6) should be enough.
To use it, simply copy/paste the module file into your code base and load it in yuor code (import Observer)
You are then ready to go !

This package contains several other ressources :
- this README, only used to describe the package and give general information
- testObserver.py, the unit tests of the Observer/Obervable classes.
- exObserver.py, a simple example to show how the Observer pattern can be used.
from collections import defaultdict

handlers = defaultdict(list)

def register(event_type, func):
    '''
    Register a handler (func) for an event type (event_type)
    the handler is called with the event as the only argument
    '''
    handlers[event_type].append(func)

def event(event):
    '''
    Generate a new event to be handled, invokes the handlers
    for this event type
    '''
    for handler in handlers[event.type]:
        handler(event)

class Event:
    def __init__(self, event_type, value):
        self.type = event_type
        self.value = value


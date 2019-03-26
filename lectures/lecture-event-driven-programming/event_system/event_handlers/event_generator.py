import random
import event_handler
from event_handler import Event

def generate_event(event):
    event_types = ["done", "start", "status"]
    event_values = ["verygood", "bad", "verybad", "normal"]
    event_handler.event(Event(random.choice(event_types), random.choice(event_values)))

event_handler.register("timer", generate_event)

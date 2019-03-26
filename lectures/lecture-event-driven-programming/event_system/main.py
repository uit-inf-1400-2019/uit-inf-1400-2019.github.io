import os
import importlib.util
import time

import event_handler
from event_handler import Event

def import_handlers():
    '''
    Import every python file in the event_handlers subdirectory
    '''
    files = os.listdir("event_handlers/")
    for f in files:
        if not f.endswith(".py"):
            continue
        module = f.split('.')[0]
        filename = "event_handlers/" + f
        spec = importlib.util.spec_from_file_location(module, filename)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)

if __name__ == "__main__":
    import_handlers()
    print("Handlers loaded:")
    for event, func_list in event_handler.handlers.items():
        for func in func_list:
            print("Event: {}, function {}".format(event, func.__name__))

    # Create a "timer" event every 0.2 seconds
    interval = 0.2
    last_time = time.perf_counter()
    while True:
        cur_time = time.perf_counter()
        if cur_time - last_time > interval:
            last_time = cur_time
            event_handler.event(Event("timer", cur_time - last_time))

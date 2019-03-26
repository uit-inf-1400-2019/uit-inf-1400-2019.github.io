import event_handler

log_message = 0

def log_event(event):
    global log_message
    log_message += 1
    print("{} Log value: {}".format(log_message, event.value))

event_handler.register("log", log_event)

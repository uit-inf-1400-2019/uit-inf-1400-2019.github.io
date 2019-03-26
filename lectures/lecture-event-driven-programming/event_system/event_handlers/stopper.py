import event_handler

def stop_system(event):
    exit()

event_handler.register("stop", stop_system)

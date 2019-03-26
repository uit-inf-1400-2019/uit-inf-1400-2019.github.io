import event_handler
from event_handler import Event


class SystemState:
    def __init__(self):
        self.aborts = 0
        self.verybad_weight = 5

    def state_event(self, event):
        if event.value == "verybad":
            self.aborts += self.verybad_weight
        if self.aborts > 20:
            event_handler.event(Event("stop", "verybad"))
            self.aborts = 0

state = SystemState()
event_handler.register("status", state.state_event)

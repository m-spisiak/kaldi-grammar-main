from dragonfly.actions import Key
from playsound import playsound

class BeepKey(Key):
    def _execute_events(self, events):
        res = super()._execute_events(events)
        playsound('sounds/beep.mp3')
        return res
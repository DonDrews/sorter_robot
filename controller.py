from enum import Enum
from threading import Event
import time

class State(Enum):
    IDLE = 0
    TESTING = 1

#Simple FSM for controlling the robot, uses thread safe interface
#between this and the http server
class Controller:

    def __init__(self, c):
        self.cardlist = c
        self.state = State.TESTING
        self.do_reset = Event()
        self.state_funcs = {State.IDLE : self.do_idle, State.TESTING : self.do_testing}
        self.test_iter = 0
    
    def run(self):
        print("Starting run!")
        while True:
            #only check for resets between states (ensures all motors are in good state)
            #TODO: maybe have an "emergency stop" that exits the application?
            if self.do_reset.is_set():
                self.states = State.IDLE
                self.do_reset.clear()
            #all state functions block until they complete
            self.state_funcs[self.state]()

    def do_idle(self):
        pass

    def do_testing(self):
        time.sleep(5)
        self.cardlist.add_card(f"Storm Crow {self.test_iter}", "ALL")
        self.test_iter += 1

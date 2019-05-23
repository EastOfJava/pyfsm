
# Event decorator which will call the appropriate event handler based on what
# state the fsm is in.  Only use this on events of an FSM class.  
def state_event(func):

    # Throws exception if <current_state>_<func> or any_<func> is undefined
    def dispatcher(sm, *args):
        try:
            method=getattr(sm, sm.current_state+'_'+func.__name__)
        except:
            method=func
        method(*args)

    return dispatcher

# Bare bones Finite State Machine class.
class PyFSM(object):

    def __init__(self):
        self.current_state = 'idle'

    def set_state(self, state):
        self.current_state = state



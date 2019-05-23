#pyfsm
##A Simple Python Finite State Machine Framework
This is an extremely simple state machine framework that is implemented in only a few lines of code.
It consists of a single decorator and a base class. To create a Finite State Machine, siimply derive a class from the PyFSM base class and decorate any instance method that you want to be "statey" with the @state_event decorator.  Your PyFSM will be in the "idle" state to start.
Next define state_event handlers by prepending a state name and underscore to the state_event name.  You can invoke the set_state method inside the event handlers if you want to invoke a different event next time the state_event is invoked.  Below is an example.  

Here is a worker PyFSM with two events, work() and stop() and two states, "idle" and "working".  Note how there is no state-event table to be initialized beforehand.  Also note that if no specific <state>_<event> handler is defined the decorated function is called.
```python
From pyfsm import PyFSM, state_event

class WorkerFSM(PyFSM):
  def __init__(self):
    super(WorkerFSM, self).__init__()
   
  @state_event
  def work(self):
    print "Default work() handler for state {}.".format(self.current_state)
    self.set_state("idle")
   
  # This gets called when work() is invoked in the "idle" state 
  def idle_work(self):
    print "Working."
    self.set_state("working")
   
  # This gets called when work() is invoked in the "working" state 
  def working_work(self):
    print "Stop bothering me, I'm busy!"
     
  @state_event
  def stop(self):
    print "Default stop() handler for state '{}'.".format(self.current_state)
    self.set_state("idle")
     
  # This gets called when stop() is invoked in the "idle" state 
  def idle_stop(self):
    print "I'm not working."
    self.set_state("No Handler")
    
  # This gets called when stop() is invoked in the "working" state 
  def working_stop(self)"
    print "Stopping."
    self.set_state("idle")
```
The following code, then, will produce this output.  Add as many states and events as you want.
```
fsm = WorkerFSM()
fsm.work()
Working.
fsm.work()
Stop bothering me, I'm busy.
fsm.stop()
Stopping.
fsm.stop()
I'm not working.
fsm.stop()
Default stop() handler for state 'No Handler'
```

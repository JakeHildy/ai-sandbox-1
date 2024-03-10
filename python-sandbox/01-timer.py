# === Python Challenge: Implement a Timer Class ===
# Objective: Create a Python class named Timer that can be used as a 
# context manager for timing the execution of a block of code. The class 
# should also support being used directly through method calls for start 
# and stop timing. This dual functionality will allow users to choose the
# most convenient way to measure execution time in different scenarios.

import time
from helpers import pause_execution

class Timer():
    # def __init__(self):
    #     self.start_time = time.time()

    def __enter__(self):
        self.start()

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.stop()

    def start(self):
        self.start_time = time.time()
    
    def stop(self):
        self.stop_time = time.time()
        self.elapsed = self.stop_time - self.start_time
        print(f'Elapsed time: {self.elapsed:.2f} seconds')

        

    # def wrapper(*args, **kwargs):

# timer = Timer()

# timer.stop_timer()


with Timer() as t:
    # Some time-consuming operations
    pause_execution(2000)
    pass

timer = Timer()
timer.start()
pause_execution(1000)
timer.stop()

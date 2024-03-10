import time

def pause_execution(milliseconds):
    """
    Pauses execution for a specified number of milliseconds.
    
    Parameters:
    milliseconds (int): The number of milliseconds to pause.
    """
    seconds = milliseconds / 1000  # Convert milliseconds to seconds
    time.sleep(seconds)
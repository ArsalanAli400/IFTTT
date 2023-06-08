from IFTTT import *

if __name__ == "__main__":
    event = "FALL%20DETECTION"
    ifttt = IFTTT() # Pass your private key
    ifttt.IFTTT_trigger(event) # Pass Event
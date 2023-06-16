"""

    Example for using IFTTT Webhook service
"""
from IFTTT import *

if __name__ == "__main__":
    event = "event_name"
    data_ifttt = {'value1': 'enter_value'}
    ifttt = IFTTT("yourPrivateKey")    				# Pass your private key
    ifttt.IFTTT_webhook_send(event,data_ifttt)                  # Pass Event
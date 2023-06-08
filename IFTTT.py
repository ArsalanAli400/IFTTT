"""

    IFTTT: A free messaging service
    This API is related to IFTTT service
    and provides the suppport for trigger
    event message services
"""
# Modules
import http.client
import json
import time
from datetime import datetime

"""

    IFTTT class support for IFTTT services. 
    Event Trigger-based messaging service
    usage: ifttt_object = IFTTT(private key)
    :argument(privateKey)
    privateKey: provided by IFTTT subscription
"""
class IFTTT():
    def __init__(self,privateKey="5ksBJ10GNHBtkzj294br"):
        ## Host Server credentials
        self.host = "maker.ifttt.com"
        self.privateKey =  privateKey
        self.headers = {'Content-Type': 'application/json'}
        self.foo = {'text': ''}
        self.success = [200 ,204 ,302]

    """
    
        Use to test the connection for IFTTT service
    """
    def test_Connection(self):
        # Waiting Loop
        print("Connecting to {}".format(self.host), sep=' ', end='', flush=True);
        last = datetime.now()
        now = datetime.now()
        while now.second - last.second < 3:
            print(".", sep=' ', end='', flush=True)
            # Get current date and time
            now = datetime.now()
            time.sleep(0.5)
        print("\n")

        # http request code
        ## Connection 1: to check network
        connection = http.client.HTTPSConnection(self.host)
        connection.request("GET", "/")
        response = connection.getresponse()
        connection.close()
        # print("Status: {} and reason: {}".format(response.status, response.reason))
        if response.status in self.success:
            print("Connection Successful")
        else:
            return

    """
    
        IFTTT Event trigger email function
        :arg(event)
        event: name of the event subscribed
    """
    def IFTTT_trigger(self, event):
        json_data = json.dumps(self.foo)

        # Com Check Waiting Loop
        print("Connecting to {}".format(self.host), sep=' ', end='', flush=True);
        last = datetime.now()
        now = datetime.now()
        while now.second - last.second < 3:
            print(".", sep=' ', end='', flush=True)
            # Get current date and time
            now = datetime.now()
            time.sleep(0.5)
        print("\n")

        # http request code
        # Connection 1: to check network
        connection = http.client.HTTPSConnection(self.host)
        connection.request("GET", "/")
        response = connection.getresponse()
        connection.close()
        print("Status: {} and reason: {}".format(response.status, response.reason))

        # Connection 2: to trigger Connection
        url = "https:" + "//" + self.host + "/trigger/" + event + "/with/key/" + self.privateKey
        print("Requesting URL: ")
        print(url)
        connection.request('POST', url, json_data, self.headers)
        response = connection.getresponse()
        print(response.read().decode())
        time.sleep(1)
        connection.close()

if __name__ == "__main__":
    event = "FALL%20DETECTION"
    ifttt = IFTTT() # Pass your private key
    ifttt.IFTTT_trigger(event) # Pass Event
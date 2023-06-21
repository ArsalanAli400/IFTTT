"""
    Author: Arsalan Ali
    IFTTT: A free messaging service
    This API is related to IFTTT service
    and provides the suppport for trigger
    event message services
    Version: 0.2-dev
"""
# Modules
import http.client
import json
import time
from datetime import datetime
import threading

"""

    IFTTT class support for IFTTT services. 
    Event Trigger-based messaging service
    usage: ifttt_object = IFTTT(private key)
    :argument(privateKey)
    privateKey: provided by IFTTT subscription
"""


class IFTTT:
    def __init__(self, privatekey="5ksBJ10GNHBtkzj294br"):
        # Host Server credentials
        self.host = "maker.ifttt.com"
        self.privateKey = privatekey
        self.headers = {'Content-Type': 'application/json'}
        self.foo = {'text': ''}
        self.success = [20, 204, 302]

    """
    
        Use to test the connection for IFTTT service
    """
    def test_Connection(self):
        # Waiting Loop
        print("Connecting to {}".format(self.host), sep=' ', end='', flush=True)
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
        # print("Status: {} and reason: {}".format(response.status, response.reason))
        if response.status in self.success:
            print("Connection Successful")
        else:
            return

    """
    
        IFTTT Event trigger email function
    """
    def IFTTT_webhook(self, event):
        """

        :type event: name of the event subscribed
        """
        json_data = json.dumps(self.foo)

        # Com Check Waiting Loop
        print("Connecting to {}".format(self.host), sep=' ', end='', flush=True)
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

    """

            IFTTT Event trigger email function
    """
    def IFTTT_webhook_send(self, event, __arg__):
        """

        :type event: name of the event subscribed
        """
        json_data = json.dumps(__arg__)
        # Com Check Waiting Loop
        print("Connecting to {}".format(self.host), sep=' ', end='', flush=True)
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


"""
    
    ifttt_schedular: Email service with time schedule
"""
class ifttt_schedular(IFTTT):
    def __init__(self, time_sch, PrivateKey, event, value_dict):
        super().__init__(privatekey="5ksBJ10GNHBtkzj294br")
        self.__time_schedule__ = time_sch
        self.__event__ = event
        self.__value_dict__ = value_dict
        self.ifttt_obj = IFTTT(PrivateKey)
        self.thread = threading.Thread(target=self.ifttt_Tschedular, args=())

    """
    
        ifttt_Tschedular: ifttt time schedular
    """
    def ifttt_Tschedular(self):
        print("Emailing Thread Started")
        while True:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            if current_time in self.__time_schedule__:
                self.ifttt_obj.IFTTT_webhook_send(self.__event__, self.__value_dict__)
            time.sleep(1)

    def start(self):
        self.thread.start()

    def join(self):
        self.thread.join()
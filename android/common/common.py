from time import sleep

from ppadb.client import Client as AdbClient
import logging

'''
Common Devices
--------------------

python script to manage Android devices
'''


class SSMAndroidDevices:

    """
        AndroidDevices class
            this is collection of devices found by adb executable
    """

    def __init__(self, host: object, port: int) -> object:
        self.client = AdbClient(host, port)
        self.devices = self.client.devices()
        if self.devices.__len__() <= 0:
            logging.critical("There are no devices connected")
            self.num_of_device = 0
            exit()
        else:
            logging.info("There are " + self.devices.__len__().__str__() + " devices connected")
            self.num_of_device = self.devices.__len__()
        return

    def print_devices(self):
        for device in self.devices:
            print("Serial: " + device.serial)
            # print("State: " + device.serial.get_state)
            print(device.get_serial_no())
            print(device.get_device_path())
            print(device.get_state())
            # below require package name
            # print(device.get_meminfo())
            print(device.get_top_activities())
            print(" ")
            for activity in device.get_top_activities():
                print(activity.activity)
                print(activity.package)
                print(activity.pid)
                print(" ")
        return


# instantiate object with default values
androidDevices = SSMAndroidDevices("127.0.0.1", 5037)

# call print function to print devices found by adb executable
androidDevices.print_devices()

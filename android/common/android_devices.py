from enum import Enum
from time import sleep

from stp_lib.devices import *
import logging

'''
Common Devices
--------------------

python script to manage Android devices
'''


class AndroidCapability:
    """
    Get or Set(?) some of Android capability
    """


class AndroidType(Enum):
    """
    enum value to indicate type of device
    """
    NONE = 0
    PHONE = 1
    SNIFFER = 2
    HOTSPOT = 3


class AndroidDevice:
    """
    Parent android device class

    This carries DeviceController object which were instantiated from STP initialization.

    Main functionality of this class is to provide basic and common set of APIs which can
    be used by different type(role) of Android device.
    """
    dev_id = -1  # order_index from devices.py
    dev_name = ""
    dev_sn = ""
    dev_trans_id = -1  # transport id (adb devices -l)

    # TODO: add firmware information
    # TODO: add type of device info
    # TODO: add android version

    def __init__(self, dev_type: AndroidType, device: DeviceController):
        # initialize it
        self.device = device  # DeviceController instance
        self.dev_type = dev_type  # AndroidType enum
        return

    def print(self):
        print_output = "Serial No:   " + self.device.getDeviceId() + "\n"
        print_output += "Android ver: " + self.device.getAndroidFullVersion() + "\n"
        print_output += "IMEI:        " + self.device.getIMEI() + "\n"
        print_output += "API ver:     " + self.device.getApiLevel() + "\n"
        print(print_output)
        return print_output

    def print_device(self):
        if self.dev_type == AndroidType.SNIFFER:
            return
        device = get_selected_device()
        device.startActivity('com.android.settings/.Settings')
        print(device.getAndroidFullVersion())
        print(device.dev_id)
        print(device.getDeviceId())
        # dump package information
        print(device.dump())
        print(device.getApiLevel())
        print(device.getIMEI())
        # dump entire system info
        print(device.sysDump())
        print(get_devices_list())
        return

    def configure_log(self):
        return

    def copy_log(self):
        return

    def take_screenshot(self):
        return

    def copy_screenshot(self):
        return


class AndroidDeviceParser:
    """
        AndroidDevices class
            this is collection of devices found by adb executable
    """

    def __init__(self, host: object, port: int) -> object:
        return


class Sniffer:
    """ Device acts as wireless sniffer """

    def __init__(self):
        return


# instantiate object with default values
androidDevice = AndroidDevice(AndroidType.PHONE, get_selected_device())

# call print function to print devices found by adb executable
androidDevice.print_device()

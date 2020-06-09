'''
Configuration Parser

With a given configuration file name, parser is used to gather
information needed to run device

Below information is required
- configuration file name (absolute path)

Configuration file content
- host : IP address of adb server. default: 127.0.0.1
- port : port number of adb server. default: 5037
- serial number: serial number of device being tested. must be provided
'''
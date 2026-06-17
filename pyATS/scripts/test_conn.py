# Import pyATS topology loader
from pyats.topology import loader

# Define the testbed for pyATS to use
testbed = loader.load("../testbed.yaml")

# Define the device that will be connected to in this script
device = testbed.devices["R1"]

# Try to connect, if successful print "connected" and execute "show version"
try:
    device.connect(log_stdout=False)
    print("Connected")

# Print exception message if connection fails
except Exception as e:
    print(f"Failed: {e}")

# If connection was successful, disconnect after.
finally:
    if device.connected:
        print("Disconnecting")
        device.disconnect()

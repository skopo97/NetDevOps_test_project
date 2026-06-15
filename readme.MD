## This is my test project for my upcoming bachelor's thesis

The project is to setup a virtual GNS3 network connected to my local network.

This approach allows me to use Ansbile to push new configurations on the network devices.

# The topology
![Toploogy](Topology.png)

# Basic workflow
A Raspberry Pi will run Ansible and monitor a GitHub repository for new commits. When configuration changes are detected, an automated CI/CD pipeline will be triggered. The pipeline will use pyATS to test and validate the proposed configuration changes.

If the tests pass, Ansible will apply the new configurations to the network devices. If the tests fail, the changes will be rejected.


# Device configurations
We only need the following initial configurations on the network devices
- IP address
- SSH

# IP Table

|Device | Management IP |
|------------|-----------|
| R1 | 192.168.99.1 |
| S1 | 192.168.99.2 |
| Raspberry Pi | 192.168.99.10 |

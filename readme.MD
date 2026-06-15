## This is my test project for my upcoming bachelor's thesis

The project is to setup a virtual GNS3 network connected to my local management network.

This approach allows me to use Ansible to push new configurations on the network devices.

# The topology
![Topology](Topology.png)

# Basic workflow
A Raspberry Pi will run Ansible and monitor a GitHub repository for new commits. When configuration changes are detected, an automated CI/CD pipeline will be triggered. The pipeline will use pyATS to test and validate the proposed configuration changes.

If the tests pass, Ansible will apply the new configurations to the network devices. If the tests fail, the changes will be rejected.


# Device configurations
We only need the following initial configurations on the network devices
- IP address
- SSH access

# IP Table

|Device | Management IP |
|------------|-----------|
| R1 | 192.168.99.1 |
| S1 | 192.168.99.2 |
| Raspberry Pi | 192.168.99.10 |

The GNS3 management network is reachble from the local machine. SSH access has been configured and tested.

# Ansible configurations


Ansible has been configured succesfully. The current Ansible configurations allows access to R1 and S1 and run Cisco IOS commands with the 'cisco.ios.ios_command' module.

## Ansible structure

```text
ansible/
├── ansible.cfg
├── inventory/
│   ├── hosts.yml
│   └── group_vars/
│       └── all.yml
└── playbooks/
    └── test_connectivity.yml
```

## Inventory
```
 all:
  children:
    routers:
      hosts:
        R1:
          ansible_host: 192.168.99.1
    switches:
      hosts:
        S1:
          ansible_host: 192.168.99.2

```

## Group variables

All the shared Ansible connection settings are stores in a own file located at `inventory/group_vars/all.yml` 
SSH credentials are read from environment variables instead of being directly shown as plaintext on the repository.

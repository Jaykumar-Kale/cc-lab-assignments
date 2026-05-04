# Assignment 4  
## Title: Procedure to Transfer Files from One Virtual Machine to Another Virtual Machine

---

## 🎯 Objective

To configure two Ubuntu Server virtual machines in VirtualBox and securely transfer files between them using SSH and SCP protocol.

---

## 🖥️ Environment Details

**Host System:**
- Windows 11
- VirtualBox 7.x

**Virtual Machines:**
- VM1: ubuntu-server-lab
- VM2: ubuntu-server-vm2
- OS: Ubuntu Server 24.04 LTS

**Network Configuration:**
- Adapter 1: NAT (for internet access)
- Adapter 2: Internal Network (cloudnet)

---

## 🌐 Network Configuration

Both VMs were connected to an Internal Network named:

```
cloudnet
```

Static IP addresses were assigned using Netplan.

---

## 🔧 VM1 Netplan Configuration

File:
```
/etc/netplan/00-installer-config.yaml
```

Configuration:
```yaml
network:
  version: 2
  renderer: networkd
  ethernets:
    enp0s3:
      dhcp4: true
    enp0s8:
      dhcp4: false
      addresses:
        - 192.168.100.10/24
```

Apply configuration:
```
sudo chmod 600 /etc/netplan/00-installer-config.yaml
sudo netplan apply
```

---

## 🔧 VM2 Netplan Configuration

File:
```
/etc/netplan/00-installer-config.yaml
```

Configuration:
```yaml
network:
  version: 2
  renderer: networkd
  ethernets:
    enp0s3:
      dhcp4: true
    enp0s8:
      dhcp4: false
      addresses:
        - 192.168.100.11/24
```

Apply configuration:
```
sudo chmod 600 /etc/netplan/00-installer-config.yaml
sudo netplan apply
```

---

## ✅ Connectivity Verification

From VM1:

```
ping 192.168.100.11
```

Result:
- Successful communication
- 0% packet loss

This confirms both VMs are connected within the same internal private network.

---

## 🔐 SSH Server Installation

On both VMs:

```
sudo apt update
sudo apt install openssh-server -y
```

Verify SSH service:

```
sudo systemctl status ssh
```

Status should show:

```
active (running)
```

---

## 📂 File Transfer Procedure Using SCP

### Step 1: Create File on VM1

```
mkdir assignment4
cd assignment4
echo "This file was transferred from VM1 to VM2 using SCP" > transfer.txt
ls
```

---

### Step 2: Transfer File from VM1 to VM2

```
scp transfer.txt jk@192.168.100.11:/home/jk/
```

Enter VM2 password when prompted.

Expected Output:
```
100% transfer successful
```

---

### Step 3: Verify File on VM2

On VM2:

```
ls
cat transfer.txt
```

Output:

```
This file was transferred from VM1 to VM2 using SCP
```

---

## 🧠 Concepts Used

- VirtualBox Internal Networking
- Static IP configuration using Netplan
- SSH (Secure Shell)
- SCP (Secure Copy Protocol)
- VM-to-VM communication in private LAN

---

## ❓ Why SCP?

SCP (Secure Copy Protocol) transfers files securely over SSH.  
It ensures:

- Encryption
- Authentication
- Data integrity

---

## 🏁 Conclusion

The file transfer between two Ubuntu Server virtual machines was successfully completed using SCP over SSH. The Internal Network configuration allowed secure communication between VMs in a private environment without exposing them to external networks.

Assignment 4 completed successfully.

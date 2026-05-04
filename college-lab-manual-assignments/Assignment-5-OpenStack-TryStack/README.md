# Assignment 5  
## Title: Procedure to Launch Virtual Machine Using TryStack (Online OpenStack Demo)

---

## 🎯 Objective

To learn and perform the procedure to launch a virtual machine using TryStack (Online OpenStack Demo Version).

---

## ☁️ Introduction to OpenStack

OpenStack is an open-source cloud computing platform that provides Infrastructure as a Service (IaaS). It allows users to create and manage virtual machines, storage, and networking resources in a cloud environment.

TryStack is an online demo platform that allows users to experience OpenStack without installing it locally.

---

## 🧠 Key OpenStack Components Used

- Nova – Compute service (used to create virtual machines)
- Neutron – Networking service
- Glance – Image service
- Horizon – Web-based dashboard
- Keystone – Identity service

---

## 🌐 Procedure to Launch Virtual Machine in TryStack

### Step 1: Access TryStack Portal

1. Open web browser.
2. Visit the TryStack OpenStack dashboard URL.
3. Enter provided credentials (username and password).
4. Login to Horizon dashboard.

---

### Step 2: Navigate to Instances

1. From the left panel, click:
   Project → Compute → Instances
2. Click on:
   Launch Instance

---

### Step 3: Configure Instance Details

Fill the following details:

Instance Name:
```
assignment5-vm
```

Availability Zone:
```
nova
```

Instance Count:
```
1
```

Click Next.

---

### Step 4: Select Image

1. Go to the "Source" tab.
2. Select a base image such as:
   - Ubuntu
   - CirrOS
3. Click Next.

---

### Step 5: Select Flavor

Choose a flavor (defines CPU, RAM, disk):

Example:
```
m1.tiny
```

Click Next.

---

### Step 6: Configure Network

1. Select available network.
2. Ensure the instance is attached to a network.
3. Click Next.

---

### Step 7: Configure Security Group

1. Select default security group.
2. Ensure SSH (port 22) is allowed if remote access is needed.
3. Click Launch Instance.

---

## 🚀 Instance Launch

After clicking Launch:

- OpenStack Nova creates VM
- Neutron assigns network
- Glance provides image
- Instance status changes from:
  BUILD → ACTIVE

---

## ✅ Verification

When Status shows:

```
ACTIVE
```

Virtual Machine has been successfully launched.

To verify:

1. Check instance state.
2. View console from dashboard.
3. Confirm successful boot.

---

## 🏗️ Architecture Behind the Scene

User Request → Horizon Dashboard  
Horizon → Nova (Compute Service)  
Nova → Allocates resources  
Glance → Provides OS Image  
Neutron → Assigns IP & Network  
VM Instance Created  

---

## 📚 Concepts Learned

- Infrastructure as a Service (IaaS)
- Virtual Machine provisioning
- OpenStack architecture
- Cloud resource orchestration
- Instance flavors and images

---

## 🏁 Conclusion

The virtual machine was successfully launched using TryStack (OpenStack demo platform). This experiment demonstrates how cloud providers provision infrastructure dynamically using OpenStack services.

Assignment 5 completed successfully.

# Assignment 3 – CloudSim Installation and Simulation

## 📌 Objective

To install the CloudSim toolkit and simulate a cloud computing environment with multiple Virtual Machines (VMs) and Cloudlets.  
To analyze the impact of different scheduling policies (TimeShared and SpaceShared) on execution performance.

---

## 🧠 Introduction

CloudSim is a Java-based simulation toolkit used for modeling and simulating cloud computing infrastructures and services.

It enables simulation of:

- Datacenters  
- Hosts  
- Virtual Machines (VMs)  
- Cloudlets (Tasks)  
- Resource allocation strategies  
- Scheduling algorithms  

CloudSim helps test and analyze cloud resource behavior without using real cloud infrastructure.

---

## 🏗 CloudSim Architecture

User  
↓  
DatacenterBroker  
↓  
Datacenter  
↓  
Host  
↓  
Virtual Machines  
↓  
Cloudlets  

---

## 🔑 Core Components Explained

### 1️⃣ Datacenter
Represents a cloud service provider such as AWS or Azure.

### 2️⃣ Host
A physical server inside the datacenter that provides computing resources.

### 3️⃣ Virtual Machine (VM)
A virtualized compute instance that runs on a host.

### 4️⃣ Cloudlet
A task or workload submitted to a VM for execution.

### 5️⃣ Broker
Acts as an intermediary between user and datacenter.  
It manages VM creation and cloudlet allocation.

---

## ⚙ Simulation Configuration Used

- 1 Datacenter  
- 1 Host  
- 2 Processing Elements (PEs)  
- 1000 MIPS per PE  
- 2 Virtual Machines  
- 4 Cloudlets  
- Cloudlet Length = 40000  
- Scheduling Policies Tested: TimeShared and SpaceShared  

---

## 🚀 Steps to Run the Simulation

1. Navigate to project directory:

   cd Assignment-3-CloudSim

2. Compile the program:

   javac -cp "lib/*" src/org/cloudbus/cloudsim/examples/MyCloudSimExample.java

3. Run the simulation:

   java -cp "src;lib/*" org.cloudbus.cloudsim.examples.MyCloudSimExample

---

## 🔄 Scheduling Policies Comparison

### 🔹 TimeShared Scheduling

- Multiple cloudlets share CPU simultaneously  
- CPU time divided among tasks  
- Parallel execution  
- Cloudlets often finish at similar times  

### 🔹 SpaceShared Scheduling

- Only one cloudlet runs at a time per CPU core  
- Other cloudlets wait in queue  
- Sequential execution  
- Finish times are staggered  

---

## 📊 Output Analysis

### Case 1 – Single VM

All 4 cloudlets executed on one VM.  
Total execution time ≈ 160 units.

### Case 2 – Two VMs (TimeShared)

Cloudlets distributed across two VMs.  
Execution time reduced to ≈ 80 units.  
Demonstrates parallel processing.

### Case 3 – Two VMs (SpaceShared)

Each VM executes cloudlets sequentially.  
First set finishes at 40 units.  
Second set finishes at 80 units.  
Demonstrates queue-based execution.

---

## 📈 Key Observations

1. VM allocation depends on host capacity (MIPS and number of PEs).  
2. If host resources are insufficient, VM creation fails.  
3. Increasing number of PEs enables multiple VMs to run simultaneously.  
4. Scheduling policy directly affects execution order and finish time.  
5. Parallelism reduces total execution time.

---

## 🎓 Viva Questions & Answers

### Q1. Why use CloudSim?
CloudSim allows simulation of cloud environments to test scheduling and allocation policies without using real cloud infrastructure.

### Q2. What is a Cloudlet?
A Cloudlet represents a computational task executed on a Virtual Machine.

### Q3. Why did VM allocation initially fail?
Because the host had insufficient MIPS and PEs to allocate multiple VMs.

### Q4. Difference between TimeShared and SpaceShared?
TimeShared divides CPU among multiple tasks simultaneously.  
SpaceShared allows one task per CPU core at a time.

### Q5. Why did execution time reduce when two VMs were used?
Because cloudlets were executed in parallel across multiple VMs.

---

## 🧩 Technical Concepts Learned

- Cloud resource modeling  
- VM allocation constraints  
- CPU scheduling strategies  
- Parallel vs sequential execution  
- Java classpath handling  

---

## 🏁 Conclusion

Successfully installed and configured CloudSim 3.0.3.  
Simulated a cloud computing environment with multiple Virtual Machines and Cloudlets.  
Analyzed the effect of different scheduling policies on execution performance.  
Demonstrated how resource allocation impacts cloud workload execution.

---

## 📌 Resume Highlight

Simulated cloud computing infrastructure using CloudSim toolkit, implemented multi-VM allocation, and compared TimeShared and SpaceShared scheduling policies to evaluate execution performance.

Here’s an AWS EC2 certification cheat sheet based on the provided transcript:

---

### **AWS EC2 Certification Cheat Sheet**

#### **Overview of EC2**
- **EC2 (Elastic Compute Cloud)**: Core service for running virtual servers (instances) on AWS.
- EC2 provides **Infrastructure as a Service (IaaS)**, allowing you to rent virtual machines (VMs) on demand.
- Key components of EC2 include:
  - **EC2 Instances**: Virtual machines.
  - **EBS (Elastic Block Store)**: Network-attached storage.
  - **Elastic Load Balancer (ELB)**: Distributes traffic across multiple instances.
  - **Auto-Scaling Group (ASG)**: Automatically adjusts the number of EC2 instances.

#### **Instance Configuration**
- **Operating Systems (OS)**: Choose between Linux, Windows, or macOS.
- **Compute Power**: Customize the number of CPUs (vCPUs) and RAM.
- **Storage**: Attach network storage (EBS) or instance storage (temporary local storage).
- **Networking**: Configure public IPs, private IPs, and network performance options.
- **Security Group**: Acts as a firewall to control inbound/outbound traffic.
- **User Data**: Bootstrap scripts that run when the instance is first launched.

#### **EC2 Instance Types**
- EC2 instances are grouped into different types based on use cases:
  - **General Purpose**: Balanced compute, memory, and networking (e.g., `t2.micro`).
  - **Compute Optimized**: For compute-intensive tasks (e.g., `c5.large`).
  - **Memory Optimized**: For memory-intensive applications (e.g., `r5.large`).
  - **Storage Optimized**: For workloads requiring high-speed storage (e.g., `i3.large`).
- **t2.micro** is free tier-eligible (750 hours/month).

#### **Instance Lifecycle**
- **Launch**: Create and configure an instance.
- **Stop/Start**: Instances can be stopped and restarted without data loss (though public IP may change).
- **Terminate**: Permanently delete the instance and its attached storage.
- **SSH Access**: Securely access EC2 instances using SSH on port 22.
  - Use a key pair (PEM/PPK) to authenticate.
  - Ensure the correct security group allows SSH access.

#### **Purchasing Options**
1. **On-Demand Instances**:
   - Pay per second/hour.
   - No long-term commitment.
   - Best for short-term, unpredictable workloads.
   
2. **Reserved Instances (RI)**:
   - Up to 72% discount for 1- or 3-year commitments.
   - Ideal for steady-state workloads.
   - **Convertible RIs** offer flexibility in changing instance types, but with slightly lower discounts.

3. **Spot Instances**:
   - Up to 90% discount.
   - AWS can terminate instances at any time if the price exceeds your bid.
   - Best for fault-tolerant, flexible workloads like batch jobs.

4. **Dedicated Hosts**:
   - Physical server dedicated to your use.
   - Suitable for regulatory or software licensing requirements.

5. **Savings Plan**:
   - Commit to a specific amount of compute usage (e.g., $10/hour).
   - Flexible across instance sizes, OS, and tenancy.

6. **Capacity Reservations**:
   - Reserve capacity in a specific Availability Zone (AZ).
   - Charged at on-demand rates.

#### **Security**
- **Security Groups**: Firewall rules that control traffic.
  - **Inbound Rules**: Control incoming traffic (e.g., SSH on port 22, HTTP on port 80).
  - **Outbound Rules**: Control outgoing traffic.
  - Ensure proper configuration to avoid timeouts.
  
- **IAM Roles**: Assign roles to EC2 instances to grant them permissions to access AWS services without needing to store credentials.

#### **EC2 User Data**
- Used to execute scripts (e.g., installing software, updating packages) when an instance starts.
- **Bootstrapping**: Automates initial setup tasks at instance launch.

#### **Cost Management**
- **Billing and Budgets**: Monitor and set budgets to control costs.
- **Free Tier**: 750 hours/month of `t2.micro` instance usage in the first year.

---

This cheat sheet covers the essential topics to help you prepare for EC2-related questions in your AWS certification exam.
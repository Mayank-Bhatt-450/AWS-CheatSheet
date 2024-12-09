Here’s a detailed **AWS Certification Cheat Sheet** in Markdown format based on the provided transcript content:

---

# AWS Certification Cheat Sheet

## **Elastic Compute Cloud (EC2)**

### Key Features:
- **Compute Power**: Virtual machines in the cloud.
- **Instance Types**:
  - **General Purpose**: Balanced resources (e.g., `t2.micro`).
  - **Compute Optimized**: High CPU workloads (e.g., `c5.large`).
  - **Memory Optimized**: High memory needs (e.g., `r5.large`).
  - **Storage Optimized**: High I/O workloads (e.g., `i3.large`).

### Instance Lifecycle:
- **Launch**: Start an instance.
- **Stop/Start**: Retain data; public IP may change.
- **Terminate**: Deletes instance, root volume (default).

### Purchasing Options:
- **On-Demand**: Pay as you go.
- **Reserved**: Up to 72% savings for 1-3 year commitments.
- **Spot**: 90% savings for flexible workloads.
- **Dedicated Hosts**: Physical servers for regulatory needs.

---

## **EC2 Storage Options**

### **Elastic Block Store (EBS)**
- **Features**:
  - Persistent block storage.
  - Tied to a specific AZ.
  - Snapshots for backup and cross-AZ transfer.
  - Volume Types: `gp2`, `gp3` (SSD), `io1`, `io2` (High IOPS), `st1`, `sc1` (HDD).
- **Delete on Termination**:
  - Root volumes: Deleted by default.
  - Additional volumes: Not deleted by default.

### **Elastic File System (EFS)**
- **Features**:
  - Shared file system across multiple instances.
  - Works with Linux.
  - Multi-AZ support.
  - **Storage Classes**:
    - `Standard`: Default.
    - `Infrequent Access (IA)`: Cost-effective for rarely accessed files.

### **Instance Store**
- Temporary storage for high-performance tasks.
- Data is lost on instance stop/termination.

### **Amazon FSx**
- **FSx for Windows File Server**: Windows-based applications.
- **FSx for Lustre**: High-performance computing (HPC).

---

## **Docker and ECS**

### **Docker Overview**
- **Containerization**: Package apps to run consistently across environments.
- **Lightweight**: Shares the host OS kernel, minimizing resource use.

### **Elastic Container Service (ECS)**
- Run Docker containers on AWS.
- Requires EC2 instances to host containers.
- Smart container placement on available instances.

### **AWS Fargate**
- **Serverless containers**: No EC2 provisioning required.
- Simplifies scaling and infrastructure management.

### **Elastic Container Registry (ECR)**
- Private Docker registry for storing images.
- Works seamlessly with ECS and Fargate.

---

## **Serverless Computing**

### **What is Serverless?**
- No server management.
- Pay per use.
- Examples: **Lambda**, **S3**, **DynamoDB**, **Fargate**.

### **AWS Lambda**
- **Features**:
  - Executes code in response to events.
  - Supports multiple languages: Node.js, Python, Java, etc.
  - Integrates with AWS services (e.g., S3, DynamoDB).
  - Free Tier: 1M requests/month and 400,000 GB-seconds of compute time.
- **Use Cases**:
  - Event-driven tasks (e.g., S3 triggers for image processing).
  - Serverless CRON jobs (e.g., CloudWatch events).

---

## **Key AWS Services**

### **Networking**
- **VPC (Virtual Private Cloud)**: Isolated cloud network.
- **Route 53**: DNS and domain management.
- **CloudFront**: Content delivery network (CDN).
- **Elastic Load Balancer (ELB)**: Distributes traffic across EC2 instances.

### **Storage**
- **S3 (Simple Storage Service)**:
  - Object storage.
  - Scalable, durable, and secure.
  - Storage Classes: `Standard`, `IA`, `Glacier`.
- **DynamoDB**:
  - NoSQL database.
  - Fully managed and serverless.
  - Supports auto-scaling.

### **Monitoring and Management**
- **CloudWatch**:
  - Logs, metrics, and alerts.
  - Monitor resource usage and performance.
- **IAM (Identity and Access Management)**:
  - Manage user access and permissions.

---

## **Tips and Tricks**

1. **EC2**:
   - Always enable detailed monitoring for better insights.
   - Use Auto Scaling for optimal resource utilization.
2. **EBS**:
   - Use snapshots for regular backups.
   - Opt for `gp3` for cost-effective storage with good performance.
3. **EFS**:
   - Leverage lifecycle policies to reduce costs with `EFS-IA`.
4. **ECS & Fargate**:
   - Use Fargate for simplicity; ECS for granular control.
5. **Lambda**:
   - Monitor function performance with CloudWatch logs.
   - Optimize memory settings for cost and performance.

---

This cheat sheet consolidates essential AWS topics, tools, and best practices, making it ideal for certification preparation and practical use.
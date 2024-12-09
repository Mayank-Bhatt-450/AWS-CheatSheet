Here’s a comprehensive **AWS Certification Cheat Sheet** in Markdown format based on the transcript:

---

# AWS Certification Cheat Sheet

## **Elastic Compute Cloud (EC2)**

### Features

* **Instance Types** : General Purpose (`t2.micro`), Compute Optimized (`c5.large`), Memory Optimized (`r5.large`), Storage Optimized (`i3.large`).
* **Lifecycle** : Start, Stop, Terminate, Reboot, Hibernate.
* **Storage** : Elastic Block Store (EBS), Instance Store.
* **Purchasing Models** :
* **On-Demand** : Pay per second.
* **Reserved** : 1-3 year commitments, up to 72% savings.
* **Spot** : Up to 90% discount, but instances can be interrupted.
* **Dedicated Hosts** : Physical servers for regulatory compliance.

---

## **Storage Options**

### Elastic Block Store (EBS)

* **Persistent, Block Storage** : Ideal for boot volumes and databases.
* **Types** :
* `gp3` (general purpose), `io2` (high IOPS), `st1` (throughput-optimized HDD).
* **Snapshots** : Incremental backups, can be restored across AZs.

### Elastic File System (EFS)

* **Shared File Storage** : Scales automatically, multi-AZ access.
* **Storage Classes** : Standard, Infrequent Access.

### Instance Store

* **Ephemeral Storage** : Temporary, high-speed local storage.

---

## **Elastic Load Balancing (ELB)**

### Types

1. **Application Load Balancer (ALB)** : For HTTP/HTTPS traffic.
2. **Network Load Balancer (NLB)** : For high-performance, low-latency traffic.
3. **Classic Load Balancer (CLB)** : For legacy applications.

---

## **Elastic Beanstalk**

### Overview

* **Platform as a Service (PaaS)** : Simplifies application deployment.
* **Use Cases** : Web apps, backend APIs.
* **Architecture Options** :

1. Single-instance (development).
2. Load Balancer + ASG (production).
3. Worker tiers (background tasks).

---

## **Infrastructure as Code (IaC)**

### AWS CloudFormation

* **Declarative Templates** : Define infrastructure in YAML/JSON.
* **Benefits** :
* Automated creation, updating, and deletion of resources.
* Infrastructure consistency across environments.

### AWS CDK (Cloud Development Kit)

* **Programmatic IaC** : Use programming languages like Python, JavaScript.
* **Features** :
* Converts code to CloudFormation templates.
* Type safety and reusable constructs.

---

## **Networking**

### Virtual Private Cloud (VPC)

* **Isolated Networks** : Define private subnets, public subnets, route tables.
* **Key Features** :
* **NAT Gateway** : Enables private subnets to access the internet.
* **VPC Peering** : Connect VPCs within or across regions.

### Route 53

* **DNS and Domain Management** : Provides global routing policies.

---

## **Monitoring and Management**

### CloudWatch

* **Logs and Metrics** : Track resource utilization.
* **Alarms** : Set thresholds for notifications/actions.

### IAM (Identity and Access Management)

* **Users, Groups, Roles** : Fine-grained access control.
* **Best Practices** :
* Enable MFA.
* Use roles for temporary access.

---

## **Containers**

### Docker and ECS

* **Elastic Container Service (ECS)** : Orchestrate Docker containers.
* **Fargate** : Serverless container management.

---

## **Serverless**

### AWS Lambda

* **Event-Driven Compute** : Pay per execution.
* **Supported Languages** : Python, Node.js, Java.

---

## **Databases**

### DynamoDB

* **NoSQL Database** : Serverless, auto-scaling.
* **Features** :
* TTL for automatic deletion.
* Global tables for multi-region replication.

---

## **Tips for Exam Success**

* **EC2** : Use Spot Instances for cost savings.
* **EBS Snapshots** : Automate backups with lifecycle policies.
* **Networking** : Know differences between VPC components (NAT, IGW, etc.).
* **Beanstalk** : Focus on deployment strategies and architecture models.
* **CloudFormation** : Understand stacks, updates, and deletions.

---

This cheat sheet captures key AWS concepts and tools to streamline your certification preparation.

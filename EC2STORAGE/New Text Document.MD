Here's an AWS EC2 storage certification cheat sheet based on the transcript:

---

### **AWS EC2 Storage Cheat Sheet**

#### **1. EBS (Elastic Block Store)**
- **EBS** is a network-attached block storage service for EC2 instances.
- **Features**:
  - **Durability**: Data persists even after an instance is stopped or terminated.
  - **Availability Zone (AZ) Specific**: EBS volumes are tied to a specific AZ.
  - **Snapshots**: You can create snapshots (backups) of your EBS volumes.
  - **Delete on Termination**: The root volume is deleted by default when the instance is terminated, but this can be disabled.
- **Volume Types**:
  - **gp2/gp3** (General Purpose SSD): Balanced price and performance.
  - **io1/io2** (Provisioned IOPS SSD): High performance for I/O-intensive workloads.
  - **st1** (Throughput Optimized HDD): Low-cost storage for frequently accessed, throughput-intensive workloads.
  - **sc1** (Cold HDD): Lowest-cost option for infrequently accessed data.

#### **2. EBS Snapshots**
- **EBS Snapshots** are incremental backups of EBS volumes.
  - **Cross-AZ/Region Copies**: Snapshots can be copied across AZs and regions for redundancy.
  - **EBS Snapshot Archive**: Store snapshots in a lower-cost archive tier (75% cheaper) but with a 24-72 hour retrieval time.
  - **Recycle Bin**: Deleted snapshots can be recovered from the Recycle Bin within a specified retention period.

#### **3. Instance Store**
- **Instance Store** provides temporary, high-performance storage that is physically attached to the EC2 instance.
  - **Ephemeral**: Data is lost when the instance is stopped or terminated.
  - **High Performance**: Useful for temporary storage such as buffers, caches, or scratch data.
  
#### **4. EFS (Elastic File System)**
- **EFS** is a scalable network file system that can be mounted to multiple EC2 instances.
  - **Multi-AZ Access**: EFS can be accessed by instances across multiple AZs within a region.
  - **Linux-Only**: EFS works with Linux-based EC2 instances.
  - **Elastic**: Automatically scales as files are added or removed.
  - **Storage Classes**:
    - **EFS Standard**: Default storage class.
    - **EFS Infrequent Access (EFS-IA)**: Optimized for files that are not accessed frequently, providing up to 92% lower cost.
  - **Lifecycle Policies**: Automatically move files between EFS Standard and EFS-IA based on access patterns.

#### **5. Amazon FSx**
- **Amazon FSx** provides fully managed third-party file systems.
  - **FSx for Windows File Server**: Designed for Windows-based applications. Supports SMB protocol, Windows NTFS, and integrates with Microsoft Active Directory.
  - **FSx for Lustre**: High-performance file system for high-performance computing (HPC) workloads. Integrates with S3 for data storage.
  - **Use Cases**: Machine learning, financial modeling, video processing, and analytics.

#### **6. AMIs (Amazon Machine Images)**
- **AMI** is a pre-configured template that contains the OS and application software to launch EC2 instances.
  - **Custom AMIs**: You can create custom AMIs to pre-install software and configurations.
  - **EC2 Image Builder**: Automates the creation, testing, and distribution of AMIs.

#### **7. EC2 Image Builder**
- **EC2 Image Builder** automates the process of creating, testing, and distributing AMIs.
  - **Builds and Tests**: Automatically runs tests on new AMIs to ensure they are functioning correctly.
  - **Global Distribution**: AMIs can be distributed across multiple AWS regions.
  - **Scheduled Builds**: Set schedules for AMI creation (e.g., weekly).

---

This cheat sheet covers the core storage services and features related to EC2, helping you prepare for EC2-related questions on the AWS certification exam.
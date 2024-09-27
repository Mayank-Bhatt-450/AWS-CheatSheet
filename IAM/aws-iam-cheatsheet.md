# AWS IAM Certification Cheat Sheet

## IAM Overview
- IAM = Identity and Access Management
- Global service (not region-specific)
- Root account should not be used for daily tasks
- Users represent individual people/applications
- Groups are collections of users
- Policies define permissions for users/groups

## IAM Users
- One IAM user per physical person
- One IAM user per application
- Users can belong to multiple groups

## IAM Groups 
- Contain users only (not other groups)
- Used to organize users and apply permissions

## IAM Policies
- JSON documents defining permissions
- Can be attached to users, groups, or roles
- Follow least privilege principle

## IAM Roles
- For EC2 instances or AWS services
- Temporary credentials
- Avoid hardcoding credentials

## Security Tools
- IAM Credentials Report: lists all users and status of credentials
- IAM Access Advisor: shows service permissions granted and when last accessed

## Best Practices
- Enable MFA (Multi-Factor Authentication)
- Create strong password policy
- Use roles for services, not individual users
- Never share IAM users & access keys
- Rotate credentials regularly

## Access AWS
1. AWS Management Console (protected by password + MFA)
2. AWS CLI (protected by access keys)
3. AWS SDK (protected by access keys)

## AWS CLI
- Tool to interact with AWS services using commands
- Direct access to public APIs of AWS services
- Alternative to using AWS Management Console

## AWS SDK
- Language-specific APIs (set of libraries)
- Embedded within your application
- Supports many programming languages

## AWS CloudShell
- Browser-based shell
- AWS CLI pre-installed
- Persists files between sessions
- Available in specific regions only

Remember: Treat access keys like passwords - keep them secret!


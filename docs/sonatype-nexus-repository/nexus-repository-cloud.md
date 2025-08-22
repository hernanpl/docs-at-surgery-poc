---
layout: default
title: "Nexus Repository Cloud"
parent: Sonatype Nexus Repository
nav_order: 2
---

# Nexus Repository Cloud

A managed Software-as-a-Service (SaaS) offering for Nexus Repository Pro, leveraging the full capabilities of the platform without the complexities of managing the underlying infrastructure. The service delivers the same high performance and extensive features that users have come to expect from Nexus Repository with the added benefits of cloud-based flexibility and operational freedom.

- Sonatype handles all aspects of managing your mission critical service. Providing highly available deployments with rolling updates, replicated backups, and automatic failover in case of any issues. Your deployment seamlessly scales with your repository usage as your development needs grow.
- Eliminates costs and time associated with server provisioning, security hardening, maintenance upgrades, and performance tuning.
- Frees your IT and development teams from managing tools, allowing them to focus on strategic initiatives and building software. Nexus Repository Cloud is always up-to-date, often before the on-prem release. Leverage the latest features before everyone else.
- Sonatype's customer success team is available to assist in migrating your on-prem deployment to the cloud for a smooth transition with minimal downtime. Our experts review your deployment to provide guidance through the whole process.

## Differences Between Repository Deployments

The functionality of Nexus Repository Cloud is identical to using the self-hosted deployment with these improvements to the experience:

- The administration user interface and REST APIs are simplified as server operations are offloaded from your administration team and managed by Sonatype. These include the configuration of the following components: blob storage, local users, security realms, system information, outbound and ssl connections, maintenance tasks and capabilities.
- Sonatype uses a flexible authentication and identity management platform providing; secure login, single sign-on (SSO), 2FA, and team management. Connect your own identity provider to provide immediate access for your organization or use our full featured IdP to connect to the entire Sonatype platform. User tokens provide the security and flexibility to integrate with any client tooling. Allowing anonymous access to your tenant would introduces a critical security risk to your software supply chain. To protect your Nexus Repository Cloud deployment, anonymous access is not available.
- Your IdP and notification tooling need to be accessible on the public internet. Nexus Repository Cloud is hosted in SOC 2-compliant environments with encryption at rest and in transit, SSO integration, auditing, and role-based access control. 2FA is enabled by default to add an extra layer of security beyond just passwords, making it significantly harder for unauthorized individuals to access your accounts.
- Access to Sonatype's world class support has never been easier. Managing the database, importing and exporting content, upgrading and backing up the service, or seamlessly failing to another region are handled by Sonatype. Access to the underlying server files such as logging, file storage, and service configuration are protected and require a support ticket when needed.
- Full REST API support is provided for complete automation and scripting when interacting with your external systems. The legacy OSGI bundling and scripting APIs are completely removed from Nexus Repository Cloud for additional security hardening; as they are no longer needed or supported.
- Coming Soon to Self-Hosted; Available Now in Cloud The Docker client has strict requirements for the path where images are hosted in a registry. The Docker path-based routing support replaces the previous requirement for access using Docker ports and subdomains. The use of docker subdomains and connector ports are not supported in Nexus Repository Cloud.

## Connect to the Cloud Tenant

After purchasing a Sonatype Cloud solution, you receive your license and instructions for setting up the tenant.

## Set the Default Role

As a public cloud deployment, Nexus Repository Cloud does not include anonymous access, so all users must be authenticated through your identity provider configured for your tenant. Once users are authenticated, they are provided a base level of access using the `Default Role` capability. Manually create a role with with minimum access available to all authenticated users of your tenant.

## Getting Started

## Invite Users to the Cloud Tenant

Administrators may directly invite users to the tenant through the `Settings -> Security -> Users` view. An email is sent to the user to verify their email address while setting up 2FA access. Once complete, the user is able to login with permissions provided by the Default User role.

![nx-cloud-users-invite.png](/assets/images/uuid-1c18e0e8-c61b-eff3-5eff-dfd5b5c96f47.png)

## Using Client Tools

Development tools such as maven, npm and docker fetch dependencies directly from public servers on the internet. While this works for small projects, it introduces inefficiencies and risks to project stability and build reliability. Configuring your client tools to use your Nexus Repository Cloud Tenant is a fundamental step in modern software development that provides significant advantages in speed, reliability, and security.

## Administrator Roles

In the identity management platform, the `Sonatype Platform - Administrator` is assigned to the primary user associated with the purchased license. This role is automatically mapped to the in-built read-only `nx-admin` role in Nexus Repository Cloud and cannot be modified.

The `nx-admin` role may be granted to other users directly, or via another role mapping when desired.

## Usage Limits

Nexus Repository Cloud operates on a usage-based licensing model designed to offer predictable and fair pricing.

- Defined as the sum of `Egress` and `Storage` . Nexus Repository Cloud reports historical usage reporting to help price Cloud opportunities. **Egress** : This refers to the total size, in gigabytes, of all components downloaded from the Nexus Repository Cloud environment per month. **Storage** : This refers to the total size, in gigabytes, of all components stored in the repository's blob stores managed by Nexus Repository Cloud. See the Usage Metrics documentation
- **Egress** : This refers to the total size, in gigabytes, of all components downloaded from the Nexus Repository Cloud environment per month.
- **Storage** : This refers to the total size, in gigabytes, of all components stored in the repository's blob stores managed by Nexus Repository Cloud.

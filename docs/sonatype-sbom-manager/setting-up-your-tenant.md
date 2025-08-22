---
layout: default
title: "Setting up your Tenant"
parent: Sonatype SBOM Manager
nav_order: 5
---

# Setting up your Tenant

After purchasing a Lifecycle SBOM Manager license, Sonatype will initialize a SBOM Manager instance for you, based on the specifications discussed during the sales process. This initialization period depends on the time to allocate resources in your region.

When the server is ready, you will receive an email with a URL to the browser UI. This URL is unique to your organization and should be treated as sensitive information.

## Sonatype Cloud

Sonatype Cloud is a deployment solution where Sonatype manages the instance and assumes responsibility for configuration and maintenance. Reduce your time-to-value by skipping the work of provisioning hardware and the costs of managing the self-hosted service.

The functionality of Sonatype Cloud is identical to using the self-hosted deployment with a few exceptions.

- Connections to Sonatype Cloud are across the public internet. Your IdP and notification tools such as webhooks need to be accessible on the public internet.
- Access to logging, file storage, and service configuration requires a support ticket. Managing the database, upgrading the service, and backing up the system are handled by Sonatype.
- Maintenance windows and upgrades are determined by Sonatype. Default configuration such as the default credentials will not be the same as the self-hosted deployments.
- Custom integrations are not supported by Sonatype or our support team

See

### Accessing Your Cloud Solution

After purchasing a Sonatype Cloud solution, you will receive your license and instructions for setting up the tenant. The initialization depends on the timing to allocate resources for your region.

- You will receive an email with a URL to the service when ready. This URL is unique to your organization and should be treated as sensitive information.
- After receiving the getting started email, sign in to your tenant with Will are required to install your license and set up MFA when you first log in.
- Set the IP address allowed to access your tenant with Allowlist for Sonatype Cloud
- Configure user access to your tenant with

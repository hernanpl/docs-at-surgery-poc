---
layout: default
title: "Sonatype Cloud"
parent: Sonatype IQ Server
nav_order: 4
---

# Sonatype Cloud

Sonatype Cloud is a deployment solution where Sonatype manages the instance and assumes responsibility for configuration and maintenance. Reduce your time-to-value by skipping the work of provisioning hardware and the costs of managing the self-hosted service.

The functionality of Sonatype Cloud is identical to using the self-hosted deployment with a few exceptions.

- Connections to Sonatype Cloud are across the public internet. Your IdP and notification tools such as webhooks need to be accessible on the public internet.
- Access to logging, file storage, and service configuration requires a support ticket. Managing the database, upgrading the service, and backing up the system are handled by Sonatype.
- Maintenance windows and upgrades are determined by Sonatype. Default configuration such as the default credentials will not be the same as the self-hosted deployments.
- Custom integrations are not supported by Sonatype or our support team

See

## Accessing Your Cloud Solution

After purchasing a Sonatype Cloud solution, you will receive your license and instructions for setting up the tenant. The initialization depends on the timing to allocate resources for your region.

- You will receive an email with a URL to the service when ready. This URL is unique to your organization and should be treated as sensitive information.
- After receiving the getting started email, sign in to your tenant with Will are required to install your license and set up MFA when you first log in.
- Set the IP address allowed to access your tenant with Allowlist for Sonatype Cloud
- Configure user access to your tenant with

## Create the Sonatype Cloud Tenant

### Designate your support contacts

Once your organization is created, add as many members as your license provides.

Up to four (4) members of your organization may be designated as authorized support contacts and will have full access to the support team. Other members should direct questions through these contacts.

For issues setting up your organization or adding support contacts, visit [support.sonatype.com](https://support.sonatype.com/) and select “Submit A Request”.

## Authentication with Sonatype Cloud

Sonatype's Cloud solutions support many Auth0-compatible protocols. Multi-factor authentication (MFA) may be configured with an authenticator of your choice.

- **Supported Auth0 protocols** : SAML, OpenID Connect, JSON Web Token, OAuth 2.0, OAuth 1.0a, WS-Federation, and OpenID.
- **Supported MFA authenticators** : Auth, Google Authenticator, Auth0 Guardian, and Microsoft Authenticator

The following is needed to set up secure authentication.

- New users receive a "Getting Started" email from the Sonatype Team
- Follow the link to set your password and select the Reset button
- Log in with your email address and the new password.
- Scan the QR code using your authenticator app. Use the one-time code and select Continue
- Invite more users to [add to your team](#UUID-3b844ae8-5826-2e2e-996d-26ef419f44b1) to complete your setup.

## User Management with Sonatype Cloud

Adding or removing users to the Sonatype cloud instance.

### Cloud user management view

Authenticated users are visible in the User Management view. Navigate to Users from the System Preferences menu

![cloud-manage-users](/docs-at-surgery-poc/assets/images/uuid-44e8932a-fa11-7392-b407-4e58fcd43717.png)

### Adding new users

- Select Users from the System Preferences menu and select the `Invite User` button
- Enter the user details and select `Send` to confirm
- A Getting Started" email with instructions to set up authentication will be sent to the users

![cloud-invite-user]({{ "/assets/images/uuid-8cfe8833-ac98-5f13-dda8-0f7d539c28f2.png)

### Deleting users

- Navigate to the User Management view
- Select the `Delete` icon to delete the user

### Adding a service account

We recommend using service accounts to connect your tenant to integrations such as your repository manager. This account needs to be granted access to the tenant configuration and will be managed by your security administrator.

## Feature parity with Sonatype Cloud

Sonatype Cloud has full feature parity with self-hosted deployments.

## Management Responsibilities for Sonatype Cloud

Though Sonatype Cloud is a managed solution, some features, processes, and customization options are still the responsibility of the customer. Review the table below for more information, and click the links in the left heading column to learn more.

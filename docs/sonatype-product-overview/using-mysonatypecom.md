---
layout: default
title: "Using my.sonatype.com"
parent: Sonatype Product Overview
nav_order: 7
---

# Using my.sonatype.com

My.sonatype.com is a self-service hub for managing Sonatype product licenses and designating individuals as authorized contacts to open Sonatype support tickets.

![Screenshot_2024-05-13_at_12_36_11_PM.png](/docs-at-surgery-poc/assets/images/uuid-da2bd971-21fd-79fc-2923-91bb187e453a.png)

## Creating an Account

1. Navigate to [my.sonatype.com](https://my.sonatype.com) in your web browser
2. Click **Sign Up** to create a new account
3. Enter your email address and create a secure password
4. Click **Create Account** to complete the registration
5. Check your email for a verification message and click the confirmation link
6. Your account is now ready to use

## Signing In

When an account already exists for you and your organization is using a Google or GitHub as an SSO solution, select the Google or GitHub buttons to sign in.

![126653828.png](/docs-at-surgery-poc/assets/images/uuid-bfda1544-3a55-b622-7755-4c2d55e86e4e.png)

## Creating an Organization

Your company is identified as an Organization within my.sonatype.com. As the account owner, you need to create an Organization to manage your Sonatype product licenses.

To create an organization:

1. After signing in, you'll be prompted to create an organization if you don't belong to one
2. Click **Create Organization**
3. Enter your organization name (typically your company name)
4. Provide your organization's address and contact information
5. Select your organization type (e.g., Commercial, Open Source, Educational)
6. Click **Create** to establish your organization
7. You'll be designated as the organization owner with full administrative privileges

## Verifying an Organization

You are required to verify your Organization before you can designate your Support Contacts.

You'll be prompted to verify your organization when you first create it. If you did not verify your organization at that time, you can follow the steps below.

1. Navigate to your organization dashboard
2. Look for the **Verification Required** banner or notification
3. Click **Verify Organization** 
4. Upload required documentation (business license, tax ID, or other official documents)
5. Wait for Sonatype to review your verification request (typically 1-2 business days)
6. You'll receive an email notification once verification is complete
7. Verified organizations will see a **Verified** badge on their organization profile

## Adding Members to an Organization

Once you have an organization, you can add members to it. When you verify your organization, we will try to integrate any existing members from our support case management system into the organization you just created. However, you can also manually invite members into your organization.

This will email instructions for signing up for my.sonatype.com. Once that person creates an account with the specified email address, they'll automatically be added to your Organization.

## Downloading a License

After a license is verified, you can view the list of products it covers in the *Licenses* section.

First, navigate to the *Organizations* view, which is available via the Profile drop-down menu.

![Screenshot_2025-03-04_at_2_50_10_PM.png](/docs-at-surgery-poc/assets/images/uuid-733a8727-a16b-5904-6a58-9c5cd115e0a7.png)

From there, select the *Licenses* tab.

Admin-level users or organization owners can download an existing license by clicking the **Download License** button.

![License.png](/docs-at-surgery-poc/assets/images/uuid-212146d8-d278-4141-31a4-f48fc39b489f.png)

## Assigning Support Contacts

Authorized support contacts are the people in your organization whom you assign to serve as the liaisons between your company and the Sonatype support team. They are chosen from the pool of existing members in your organization.

- The number of members allowed to be support contacts is determined by the customer contract.
- Being a member of an Organization does not automatically make them a support contact.
- Only verified Organizations can have support contacts.
- Individuals who have been invited to an Organization but haven't accepted the invite email cannot be designated a support contact.

![Support_contact.png](/docs-at-surgery-poc/assets/images/uuid-6e366c96-d2b8-2bb8-9ab2-ec690a221159.png)

To assign support contacts:

1. Navigate to your organization dashboard
2. Select the **Support Contacts** tab
3. Click **Add Support Contact**
4. Choose from existing organization members or invite new members
5. Select the member you want to designate as a support contact
6. Click **Assign** to confirm the designation
7. The selected member will receive an email notification about their new role
8. Support contacts can now open and manage support tickets on behalf of the organization

**Note:** The number of support contacts allowed depends on your license agreement. Contact your Sonatype account team if you need to increase this limit.

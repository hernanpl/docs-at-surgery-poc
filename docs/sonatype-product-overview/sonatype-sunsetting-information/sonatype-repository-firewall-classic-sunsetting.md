---
layout: default
title: "Sonatype Repository Firewall Classic Sunsetting"
parent: Sonatype Sunsetting Information
nav_order: 6
---

# Sonatype Repository Firewall Classic Sunsetting

**Note:** The Sonatype Product Development Lifecycle (PDLC), including definitions of each stage, is fully defined in [Sonatype Sunsetting Information](#UUID-217b96ec-8a06-93ff-b373-ab40751a5647) For more information about Sonatype Support services, please see [Sonatype's Software Support Policy](https://www.sonatype.com/usage/software-support-policy) .

The Sonatype PDLC is designed to keep us continually improving our products and to ensure that our customers have access to our best features and functionality. This helps us provide quality support services for our features and products. Sonatype will sunset and remove the product Sonatype Repository Firewall Classic.

Existing licenses for the classic version of the Repository Firewall must switch to the Repository Firewall product.

## Classic Firewall

Classic Firewall has been sunsetted. Users need to switch to the Repository Firewall. This walk-through is the steps needed to make the switch.

### Install the Repository Firewall license

### Enable Repository Firewall features

These policies will need to be added to benefit from Repository Firewall features

- Add the Integrity-Rating policy
- Add the Component Unknown Policy

### Configure policy-compliant component selection

### Add the Integrity-Rating policy

Go to 'Orgs and Policies' and add the policy ‘Integrity-Rating’ if it is not already present.

Use the following table for configuration values:

### Component Unknown Policy

Sonatype's data service continuously learns the identity of components as they are uploaded to public repositories by the community. There is a brief window when new components have just been added and Sonatype data services has not yet learned about them.

To protect your infrastructure from using them before they are analyzed for risk, Repository Firewall may temporarily quarantine the unknown components and auto-release them once they have been reviewed.

We do this by setting the Component Unknown Policy to quarantine components with an unknown `Match State` and auto-release them once they're identified. This is recommended for the npm and PyPi ecosystems.

You will need to add this policy to each proxy repository or use the default policy for Unknown Components to enable this behavior to target the specific ecosystems.

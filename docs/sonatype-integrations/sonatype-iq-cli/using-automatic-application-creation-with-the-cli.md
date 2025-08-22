---
layout: default
title: "Using Automatic application creation with the CLI"
parent: Sonatype IQ CLI
nav_order: 6
---

# Using Automatic application creation with the CLI

When automatic application creation is enabled, Lifecycle creates new applications when the passed applicationId is not found. This is recommended for first-time evaluation of new applications.

The automatic application creation feature creates a new application under the organization that is configured. To create an application under a different organization, you can specify the `organization-id` as an input parameter.

**Note:** The CLI evaluation will error when providing an organization ID that does not match the organization the application belongs to in the Lifecycle server. This prevents accidental misconfigurations where scans are made to the wrong application; corrupting the evaluation history.

## Locating the organization ID

To locate the `organization-id`

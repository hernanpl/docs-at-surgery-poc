---
layout: default
title: "License and Features"
parent: Sonatype IQ Server
nav_order: 6
---

# License and Features

The Sonatype account team provides the license as a `.lic` file in an email sent to the primary stakeholders. A Sonatype license may contain access to multiple Sonatype solutions. Each solution enables various features depending on the solutions you purchase.

```
Lifecycle, Repository Firewall, SBOM Manager, and Developer Team. 
```

See [Sonatype Product Overview](#UUID-4d43e931-7c64-7fcc-18ee-e88460d11233) for details.

**Note:** Disconnected Sonatype Solutions Sonatype offers a solution for environments without internet access. The Sonatype Air-Gapped Environment (SAGE) product allows usage of the IQ Server in a disconnected (no internet) environment. This is a separate license purchase. If you're interested in this, you can contact Sonatype directly at sales@sonatype.com

## Sonatype Feature Matrix

Use the matrix below to understand the features your Sonatype license unlocks.

= Supported = Not Available

## Lifecycle Foundation

Lifecycle Foundation provides a subset of the Lifecycle functionality designed to support a focus on identifying and reporting security risks. Upgrade to a full Lifecycle license when ready for policy enforcement in the DevOps pipeline.

- Create customized policies for security, license, and quality standards.
- Integrate with existing CI/CD tools.
- Automatically create an application composition report, or a software bill of materials, to visualize risk and policy violations.
- Leverage the Sonatype Intelligence engine to provide remediation guidance including the use of waivers and license overrides.

Lifecycle Foundation does not let you:

- Integrate policy information and remediation guidance in a developer’s IDE.
- Include support for any automatic enforcement of policy like failing a build, or sending alerts, or automatically creating Jira tickets.
- Provide continuous monitoring of applications that are in production, to identify new risks in existing preapproved components.
- Establish legacy violations to baseline any existing violations when onboarding new applications.
- Run in High Availability deployments
- Connect to Nexus Repository or Sonatype Repository Firewall

### Use Lifecycle Foundation to be More Secure

The goal of Lifecycle Foundation is to provide open-source risk analysis by leveraging superior Sonatype intelligence. Knowing what’s in your applications empowers you to make them more secure.

Lifecycle Foundation provides access to the Lifecycle policy engine. Policy is used to identify risks associated with open-source existing in your applications.

With Lifecycle Foundation, you can use the provided reference policies, and/or create your own organizational policies. You will not have access to policy actions, use of legacy violations, or automatic notifications through email or JIRA.

Lifecycle Foundation can produce a bill of materials (BOM) via the Application Composition Report. This report serves as a point-in-time output of risk associated with components in a specific application.

The Lifecycle Dashboard searches for violations found within a specific stage or policy type. Using filters to focus on specific risks to prioritize your remediation.

Remediating risk starts with improving your process of open-source selection. This data is found in the Component Information Panel and displays remediation suggestions with Sonatype’s enriched data and guidance.

### Licensing and Features

The following table outlines the features, and limitations, of a Sonatype Lifecycle Foundation license:

## CPE Matching Experience in SBOM Manager vs. Lifecycle

Sonatype SBOM Manager and Sonatype Lifecycle both support Common Platform Enumeration- (CPE) based vulnerability matching; however, the behavior and configuration differs depending on your setup and licening.

The following table outlines how CPE matching behaves across different installation types, including new installations and deployments that existed before the introduction of CPE matching:

### Data Merging and Display Logic

The sections below explain the data merging and display logic behavior for Sonatype SBOM Manager and Sonatype Lifecycle.

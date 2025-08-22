---
layout: default
title: "Sonatype Sunsetting Information"
parent: Sonatype Product Overview
nav_order: 2
has_children: true
---

# Sonatype Sunsetting Information

## Sonatype Product Development Overview

The Sonatype Product Development Lifecycle (PDLC) is designed to keep us continually improving our products and to ensure that our customers have access to our best features and functionality. This also helps us provide quality support services for our features and products.

Our product lifecycle includes four stages:

![Sonatype Sunsetting Lifecycle]({{ "/assets/images/uuid-d83a1379-5df1-2156-8465-82819d5b057b.png)

**Note:** For more information about Sonatype Support services, please see [Sonatype's Software Support Policy](https://www.sonatype.com/usage/software-support-policy) .

The table below provides details about each stage of the Sonatype PDLC:

| Stage | Description | Duration |
|-------|-------------|----------|
| **Generally Available** | Full support with all features, updates, and bug fixes | 2 years from release date |
| **Extended Maintenance** | Limited support with critical bug fixes and security patches only | 6 months after General Availability |
| **Sunset** | No further updates, patches, or support provided | After Extended Maintenance period |
| **End of Life** | Product completely discontinued and removed | Final stage after sunset period |

## Version and Feature Status by Product

### Sonatype Nexus Repository

[Sonatype Nexus Repository 3 Versions Status](#UUID-caa22a03-094e-6423-7c93-6d9f9450d1ab)

[Sonatype Nexus Repository 2 Sunsetting Information](#UUID-7ddc7e7d-2983-c10d-206d-96135b8c54f7)

[Sonatype Nexus Repository 3 Feature Status](#UUID-910de0dd-dc88-616d-2d71-ef2843018cc9)

### Sonatype IQ Server

[Sonatype IQ Server Versions Status](#UUID-d47113e2-9a13-24c5-b05a-f7e487b88039)

[Sonatype Integration Versions Status](#UUID-1747cc1a-0843-6568-7246-e3a46d00fe40)

## FAQ

### Why is Sonatype sunsetting products?

Sonatype's mission is to help you develop software fearlessly. An essential part of that mission is regularly examining our solutions to ensure our customers' deployments have dependable, secure, and well-supported capabilities.

Eventually, some of our products will reach the end of their useful life. The Sonatype product development lifecycle (PDLC) is designed to keep us continually improving our products, ensuring that our customers have access to our best features and functionality, and helping us provide quality support services for our features and products.

### I am running a sunset version of a product, can I still receive support?

Yes, Support will provide best-effort guidance to help customers adopt suggested alternatives or an upgrade path.

We encourage all our customers to be on supported versions of our products so that you can fully leverage bug fixes and product investment towards enhanced features and capabilities.

### Who can receive support in the Extended Maintenance phase?

Support for releases in Extended Maintenance is available to all customers.

### Where can I find the timeline or more details on the versions/features being sunsetted?

See the version and feature status by product section.

## Sonatype Nexus Repository 3 Versions Status

The Sonatype Product Development Lifecycle (PDLC), including definitions of each stage, is fully defined in [Sonatype Sunsetting Information](#UUID-217b96ec-8a06-93ff-b373-ab40751a5647) .

- Sonatype Nexus Repository releases are considered generally available and fully supported for a term of **1 year after the version's release date** .
- Sonatype provides extended maintenance for each Sonatype Nexus Repository version for an additional **6 months** before that version is considered sunset.
- The **date of the initial major release** (e.g., 3.53.0 or 3.47.0) is used to determine when the patch release versions move through the PDLC process.

### Sonatype Nexus Repository 3 Release Statuses by Version

The table below lists Sonatype Nexus Repository releases with their end-of-extended maintenance and sunset dates.

**Note:** For current version status information, refer to the [Sonatype Software Support Policy](https://www.sonatype.com/usage/software-support-policy) as this information is regularly updated.

### Nexus Repository 3 FAQ

#### Why is Sonatype sunsetting Nexus Repository 3 versions?

Sonatype's mission is to help you develop software fearlessly. An essential part of that mission is regularly examining our solutions to ensure our customers' deployments have dependable, secure, and well-supported capabilities. Eventually, some product versions will reach the end of their useful life. The Sonatype PDLC is designed to keep us continually improving our products, ensuring that our customers have access to our best features and functionality, and helping us provide quality support services for our features and products.

#### Can I still receive support for sunset versions?

Yes, Support will provide best-effort guidance to help customers adopt suggested alternatives or an upgrade path. We encourage all our customers to be on supported versions so that bug fixes and product investment toward enhanced features and capabilities are fully leveraged.

#### Can I upgrade from an older version to a newer supported version?

Yes, you can upgrade your Sonatype Nexus Repository instance from an older version to a newer, supported version. We recommend that you **plan an upgrade to the latest supported version.** For upgrade guidance, see the upgrade documentation in the Nexus Repository section.

#### What about community plugins?

Unfortunately, community plugins are not supported. Many do not work with recent versions of Nexus Repository and/or PostgreSQL mode. We recommend that customers discontinue the use of incompatible plugins. For each community plugin, please check the plugin documentation for version compatibility information.

## Nexus Repository 3 Feature Status

**Note:** The Sonatype Product Development Lifecycle (PDLC), including definitions of each stage, is fully defined in [Sonatype Sunsetting Information](#UUID-217b96ec-8a06-93ff-b373-ab40751a5647) . For more information about Sonatype Support services, please see [Sonatype's Software Support Policy](https://www.sonatype.com/usage/software-support-policy).

The Sonatype PDLC is designed to keep us continually improving our products and to ensure that our customers have access to our best features and functionality. This also helps us provide quality support services for our features and products. To this end, Sonatype will sunset and remove some Sonatype Nexus Repository features as they become obsolete.

### Log4J Visualizer

- **Status** : Sunsetted (March 3, 2025), **Released** : November 24, 2021(3.37.0) In Nexus 3.78.0 the Log4J Visualizer has been removed. Log4j Visualizer was an early experiment in adding SCA features to the Nexus Repository. This has been superseded by other motions such as malware warnings.

### Bower Format

- **Status** : Sunsetted (March 3, 2025), **Released** : March 10, 2016 (3.0.0) In Nexus 3.71.0 the Bower format has been removed. Bower has no longer been a supported ecosystem by the community since 2017. This format was only supported in OrientDB instances and was not ported to support PostgreSQL or H2 database.

### OSGi Bundle Capability

- **Status** : Sunsetted (March 3, 2025), **Released** : March 10, 2016 (3.0.0) In Nexus 3.78.0 the OSGi bundle capability has been removed. Any customers using bundles when upgrading to this version will find that those bundles are not loaded.

### OrientDB

- **Extended Maintenance** : (August 6, 2024), **Sunsetting** : January 9 2026, **Released** : March 10, 2016 (3.0.0) Sonatype is invested in continually improving our solutions to take advantage of newer, more advanced technologies. As such, we are strategically moving away from legacy technologies like OrientDB and investing in supporting newer database options like PostgreSQL. Moreover, Sonatype has observed data integrity problems in some deployments using OrientDB. Migrate to a supported database. See [Migrating to a New Database](#UUID-a3ea5445-b958-e8a6-d3e7-b2d3086c58a3) .

### Java 8

- **Status** : Extended Maintenance (August 6, 2024), **Released** : February 11, 2015 Java 8 has reached the end of its life and is no longer receiving public updates. Upgrade to release 3.70.0+ using Java 17. See [Upgrade Nexus Repository Java Version](#UUID-1c91200a-32b7-90c6-0e8b-3dde385edaf5) .

### Java 11

- **Status** : Extended Maintenance (August 6, 2024), **Released** : April 2, 2024 OpenJDK 11 reaches the end of life in October 2024. While Java 11 is a long-term support version, Sonatype is investing its efforts in supporting newer Java versions. Upgrade to release 3.70.0+ using Java 17. See [Upgrading Nexus Repository Java Version](#UUID-1c91200a-32b7-90c6-0e8b-3dde385edaf5) .

### High Availability Clustering (HA-C)

- **Status** : Sunsetted (April 17, 2024), **Released** : February 2017 (3.3.0), **Maintenance** : October 17, 2023 We released the updated version of [High Availability](#UUID-906849d2-3b89-01cd-0a5b-9afd13e9ceac) in Q1 2023 with release 3.50.0. This new offering offers far superior functionality, quality, and scale. Customers currently using HA-C should upgrade to the updated HA deployment model. See [Migrating to an HA Deployment from HA-C](/document/preview/116674#UUID-602e0a4a-d0c8-4751-2f92-8e60514dd4b6) . Migrating to an HA Deployment from a Legacy HA-C or a Resilient Deployment

### Replication v1

- **Status** : Sunsetted (December 15, 2023), **Released** : September 1, 2021 (3.34.0), **Maintenance** : August 3, 2023 In 3.34.0, we introduced our first replication feature (Replication v1), which used a manually run replicator tool to copy binaries from one blob store to another. In 3.48.0, we introduced [Content Replication](#UUID-cbf916ff-6f29-b5b5-770e-0eb3fc21647e) as a much more user-friendly, lightweight feature to replace Replication v1. We also announced at that time that we would eventually remove Replication v1. The newer Content Replication feature is far simpler and includes more automation; it also has fewer system requirements and supports more formats. Customers needing a way to make artifacts readily available across distributed teams should use the newer Content Replication feature. As Content Replication is an entirely different and separate feature from Replication v1, there is no direct migration path. See [Content Replication](#UUID-cbf916ff-6f29-b5b5-770e-0eb3fc21647e)

### Red Hat OpenShift Operator and Container

- **Status** : Sunsetted (December 15, 2023), **Released** : June 2020 (3.24.0), **Maintenance** : August 3, 2023 Sonatype does not recommend using this operator because there are risks of data corruption when running the embedded databases inside a container. In October 2023, Sonatype published a new OpenShift Operator. The new operator uses an external PostgreSQL database and supports high-availability deployment options. See [Installing Sonatype Nexus Repository Using the OpenShift Operator](#UUID-a73c1c08-94b7-2eba-203f-ec9c5e764cc8) .

## Sonatype Nexus Repository 2 Sunsetting Information

The Sonatype product development lifecycle is defined in [Sonatype Sunsetting Information](#UUID-217b96ec-8a06-93ff-b373-ab40751a5647) . For more information about Sonatype Support services, see [Sonatype's Software Support Policy](https://www.sonatype.com/usage/software-support-policy) .

### Sonatype Nexus Repository 2 Sunsetting Timeline

Sonatype is sunsetting Nexus Repository 2 on **June 30, 2025** . There are no more planned improvements to Nexus Repository 2. Migrate to Sonatype Nexus Repository 3 to take advantage of the improvements, bug fixes, and new features.

See [Upgrade from Nexus Repository 2](#UUID-cc0df024-9153-58a0-73c4-234d05fa3efa)

## Sonatype Nexus Repository 2 Version Status

**Note:** The Sonatype Product Development Lifecycle (PDLC), including definitions of each stage, is fully defined in [Sonatype Sunsetting Information](#UUID-217b96ec-8a06-93ff-b373-ab40751a5647) . For more information about Sonatype Support services, please see [Sonatype's Software Support Policy](https://www.sonatype.com/usage/software-support-policy) .

Sonatype officially sunset its Nexus Repository 2 product on **June 30, 2025** . From this sunset date, Sonatype will no longer release any additional features or bug fixes for Nexus Repository 2.

If you are using Nexus Repository 2, you should [migrate to Sonatype Nexus Repository 3](https://help.sonatype.com/en/upgrading-from-nexus-repository-manager-2.html) as soon as possible.

For full details, see [Upgrading from Nexus Repository Manager 2](https://help.sonatype.com/en/upgrading-from-nexus-repository-manager-2.html).

### Sonatype Nexus Repository 2 Status by Version

The table below lists the last two major Sonatype Nexus Repository 2 releases and provides their end-of-extended maintenance and sunset dates. All prior versions released are considered sunsetted.

**Note:** For current version status information, refer to the [Sonatype Software Support Policy](https://www.sonatype.com/usage/software-support-policy).

### Nexus Repository 2 FAQ

## Sonatype Auditor Sunsetting

**Note:** The Sonatype Product Development Lifecycle (PDLC), including definitions of each stage, is fully defined in the [Sonatype Product Development Overview](#sonatype-product-development-overview) section above. For more information about Sonatype Support services, please see [Sonatype's Software Support Policy](https://www.sonatype.com/usage/software-support-policy).

The Sonatype PDLC is designed to keep us continually improving our products and to ensure that our customers have access to our best features and functionality. This helps us provide quality support services for our features and products. Sonatype will sunset and remove the product, Sonatype Auditor.

Existing licenses for the classic version of the Auditor should switch to the Sonatype SBOM Manager product.

## Sonatype Repository Firewall Classic Sunsetting

**Note:** The Sonatype Product Development Lifecycle (PDLC), including definitions of each stage, is fully defined in the [Sonatype Product Development Overview](#sonatype-product-development-overview) section above. For more information about Sonatype Support services, please see [Sonatype's Software Support Policy](https://www.sonatype.com/usage/software-support-policy).

The Sonatype PDLC is designed to keep us continually improving our products and to ensure that our customers have access to our best features and functionality. This helps us provide quality support services for our features and products. Sonatype will sunset and remove the product Sonatype Repository Firewall Classic.

Existing licenses for the classic version of the Repository Firewall must switch to the Repository Firewall product.

### Classic Firewall

Classic Firewall has been sunsetted. Users need to switch to the Repository Firewall. This walk-through is the steps needed to make the switch.

## Sonatype IQ Server Versions Status

**Note:** The Sonatype Product Development Lifecycle (PDLC), including definitions of each stage, is fully defined in . For more information about Sonatype Support services, see [Sonatype's Software Support Policy](https://www.sonatype.com/usage/software-support-policy) .

The following Sonatype licenses are powered by Sonatype IQ Server and are covered under their corresponding release lifecycle:

- Sonatype Lifecycle
- Sonatype Repository Firewall
- Sonatype SBOM Manager
- Sonatype Developer
- Sonatype Advanced Legal Pack

Sonatype IQ Server releases are considered generally available and fully supported for a term of 1 year after the version's release date.

Sonatype provides extended maintenance for each IQ Server version for an additional 6 months before that version is sunsetted.

For versions requiring patch releases, the full version line will use the dates of the initial major release to determine when the versions will move through the PDLC process.

### Sonatype IQ Server Status by Version

The table below lists IQ Server releases, the beginning of extended maintenance, and sunset dates. Versions before 2022 are considered sunsetted.

**Note:** For current version status information, refer to the [Sonatype Software Support Policy](https://www.sonatype.com/usage/software-support-policy).

### Why are you sunsetting versions of the Sonatype IQ Server?

Sonatype's mission is to help you develop software fearlessly. An essential part of that mission is regularly examining our solutions to ensure our customers' deployments have dependable, secure, and well-supported capabilities.

Eventually, some of our products will reach the end of their useful life. The Sonatype PDLC is designed to keep us continually improving our products, ensuring that our customers have access to our best features and functionality, and helping us provide quality support services for our features and products.

In line with that, we will be sunsetting the product versions that are out of support per [Sonatype’s support policy](https://www.sonatype.com/usage/software-support-policy) .

### I am running a sunset version of Sonatype IQ Server; can I still receive support?

Yes -- Support will provide best-effort guidance to help customers adopt suggested alternatives or an upgrade path.

We encourage all our customers to be on supported versions so that bug fixes and product investment toward enhanced features and capabilities are fully leveraged.

## Sonatype IQ Server Feature Status

**Note:** The Sonatype Product Development Lifecycle (PDLC), including definitions of each stage, is fully defined in the [Sonatype Product Development Overview](#sonatype-product-development-overview) section above. For more information about Sonatype Support services, please see [Sonatype's Software Support Policy](https://www.sonatype.com/usage/software-support-policy).

The Sonatype PDLC is designed to keep us continually improving our products and ensure our customers have access to our best features and functionality. This also helps us provide quality support services for our features and products. To this end, Sonatype will sunset and remove some Sonatype IQ Server features as they become obsolete.

## Sonatype Integrations Version Status

**Note:** The Sonatype Product Development Lifecycle (PDLC), including definitions of each stage, is fully defined in [Sonatype Sunsetting Information](#UUID-217b96ec-8a06-93ff-b373-ab40751a5647) . For support-related information, refer to [Sonatype Software Support Policy](https://www.sonatype.com/usage/software-support-policy) .

Sonatype integration releases are considered generally available and fully supported for a term of **1 year after the version's release date** .

At that point, Sonatype provides extended maintenance for each Sonatype integration version for an additional **6 months** before that version is marked for sunsetting.

For versions requiring patch releases, the full version line will use the dates of the initial major release to determine when the versions will move through the PDLC process.

### Sonatype CLI

[https://sonatype.github.io/iq-cli/support](https://sonatype.github.io/iq-cli/support )

**Note:** The native Mac OSX CLI has been sunset and will receive only critical bug and security fixes until June 10th, 2025. After this date, it will no longer be supported. The native Linux and Windows CLI have been sunset and will receive only critical bug and security fixes until September 14, 2025. After this date, they will no longer be supported. For the latest features and full support, [switch to our cross-platform Java CLI with bundled JDK](#UUID-4e396b62-fd65-1cfc-dd99-2fb0a20e7b36_section-idm234690697763901) .

### Sonatype CLM for Maven

[https://sonatype.github.io/clm-maven-plugin/support](https://sonatype.github.io/clm-maven-plugin/support)

### Sonatype Platform Plugin for Jenkins

[https://sonatype.github.io/jenkins-plugin/support](https://sonatype.github.io/jenkins-plugin/support)

### Sonatype for Azure DevOps

[https://sonatype.github.io/iq-azure-devops/support](https://sonatype.github.io/iq-azure-devops/support)

### Sonatype for Fortify SSC

[https://sonatype.github.io/nexus-iq-fortify/support](https://sonatype.github.io/nexus-iq-fortify/support)

### Sonatype for Bamboo Data Center

[https://sonatype.github.io/clm-bamboo-plugin/support](https://sonatype.github.io/clm-bamboo-plugin/support)

### Sonatype for Eclipse

[https://sonatype.github.io/insight-eclipse/support](https://sonatype.github.io/insight-eclipse/support)

### Sonatype for IDEA

[https://sonatype.github.io/nexus-iq-idea-plugin/support](https://sonatype.github.io/nexus-iq-idea-plugin/support)

### Sonatype for Visual Studio 2022

[https://sonatype.github.io/visual-studio-2022-extension/support](https://sonatype.github.io/visual-studio-2022-extension/support)

### Sonatype for VS Code

[https://sonatype.github.io/iq-vscode-plugin/support](https://sonatype.github.io/iq-vscode-plugin/support)

### Sonatype for Jira Data Center

[https://sonatype.github.io/iq-jira-plugin/support](https://sonatype.github.io/iq-jira-plugin/support)

### Sonatype for Jira Cloud

[https://sonatype.github.io/lifecycle-jira-cloud-integration/support](https://sonatype.github.io/lifecycle-jira-cloud-integration/support)

### Sonatype GitHub Actions

[https://sonatype.github.io/github-actions/support](https://sonatype.github.io/github-actions/support)

### Sonatype for GitLab CI

[https://sonatype.github.io/gitlab-nexus-platform-plugin/support](https://sonatype.github.io/gitlab-nexus-platform-plugin/support)

### Repository Firewall for Artifactory plugin

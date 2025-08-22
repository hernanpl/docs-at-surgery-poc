---
layout: default
title: "Product Information"
parent: Sonatype Nexus Repository
nav_order: 1
---

# Product Information

This space contains important Nexus Repository product information for your reference needs.

## Just Getting Started?

- [Download](#download) Nexus Repository
- Make sure you understand our [System Requirements](#sonatype-nexus-repository-system-requirements)
- Learn about new features from our [Release Notes](#release-notes)

## Trying to Decide Which Nexus Repository is Right for You?

- Check out our [Nexus Repository Pro features](#nexus-repository-professional-features)
- Start a [Nexus Repository Pro trial](https://www.sonatype.com/products/repository-pro/trial)
- Take a look at our [feature matrix](#nexus-repository-feature-matrix)

## Download

Download the latest version of Nexus Repository TM for use with all deployments. On this page are the latest downloads of the Unix/Linux, Microsoft Windows, and Apple macOS versions.

See License Management in the administration documentation to upgrade to Nexus Professional.

### Download Sonatype Nexus Repository 3.82.0

⚠️ **Warning:** Known Issue with *Repair - Reconcile component database from blob store* task for Azure blob stores Sonatype has identified an issue in Sonatype Nexus Repository where running the *Repair - reconcile component database from blob store* task with the *integrity check* option enabled can incorrectly remove content from repositories that use an Azure blob store. If you are using an Azure blob store, do not run this task with *integrity check* selected.

*The Unix archive bundled with a platform-specific JDK can not be used on a Mac.*

For new installations, see [Install Nexus Repository](install-nexus-repository.md) and [System Requirements](#sonatype-nexus-repository-system-requirements).

**Note:** *Nexus Repository is distributed with Sencha Ext JS pursuant to a FLOSS Exception agreed upon between Sonatype, Inc. and Sencha Inc. Sencha Ext JS is licensed under GPL v3 and cannot be redistributed as part of a closed source work.*

### Nexus Repository TM Database Migrator

Download the latest version of the database migrator using the links below:

[Database Migrator 3.82.0](https://download.sonatype.com/nexus/nxrm3-migrator/nexus-db-migrator-3.82.0-05.jar) ( [ASC](https://download.sonatype.com/nexus/nxrm3-migrator/nexus-db-migrator-3.82.0-05.jar.asc) , [SHA1](https://download.sonatype.com/nexus/nxrm3-migrator/nexus-db-migrator-3.82.0-05.jar.sha1) , [SHA256](https://download.sonatype.com/nexus/nxrm3-migrator/nexus-db-migrator-3.82.0-05.jar.sha256) , [SHA512](https://download.sonatype.com/nexus/nxrm3-migrator/nexus-db-migrator-3.82.0-05.jar.sha512) )

- See the Database Migration documentation for the migrator documentation.
- See the OrientDB Migration guide to migrate from OrientDB.

### Related Links

- [GitHub](https://github.com/sonatype/nxrm3-ha-repository/tree/main/nxrm-ha) | [ArtifactHub](https://artifacthub.io/packages/helm/sonatype/nxrm-ha)
- [DockerHub](https://hub.docker.com/r/sonatype/nexus3/)
- [Cloud Deployments](nexus-repository-cloud.md)
- Nexus Platform Plugin for Jenkins
- [5C9BD9F4EAAD7054](https://keys.openpgp.org/search?q=5C9BD9F4EAAD7054)

### Nexus Repository 3.70.x Downloads with OrientDB

As of Nexus Repository TM release 3.71, H2 is the embedded database as support for OrientDB is deprecated. Nexus Repository TM instances using Orient DB need to migrate to use either the embedded H2 or an external PostgreSQL database. Instances that cannot be migrated must remain on the 3.70.x point releases for critical bug fixes.

See the Upgrade documentation for upgrading to 3.71.0 and beyond.

### Download Archives - Repository Manager 3

Nexus Repository TM is always rapidly evolving; we discourage using older versions.

Docker images for Nexus Repository TM are available on [Docker Hub](https://hub.docker.com/r/sonatype/nexus3/) .

Information about deployment templates is found in the [Cloud Deployments](nexus-repository-cloud.md) documentation.

**Note:** *Nexus Repository*

## Release Notes

### Sonatype Nexus Repository Releases

Select a version to learn more about what was included in that Nexus Repository release. Or, select a year for a high-level overview of major changes in that year.

- The Nexus Repository 3.70.x line is the last release line to support OrientDB. If you must remain on OrientDB, you will need to remain on our 3.70.x release line until you can migrate to H2 or PostgreSQL. This marks OrientDB's transition to Extended Maintenance as defined in our [sunsetting documentation](../sonatype-product-overview/sonatype-sunsetting-information/index.md) . As of **January 9, 2026** , OrientDB will be considered officially sunset. 3.70.3 Released Oct 10, 2024!

### 2024 Release Notes
- 3.82.0 - Current release (includes Azure blob store repair task fixes)
- 3.81.0 - Performance improvements and bug fixes  
- 3.80.0 - Security updates and feature enhancements
- 3.79.0 - Database migration tools and stability improvements
- 3.78.0 - New build process and Windows service improvements
- 3.77.0 - High availability enhancements
- 3.76.0 - Additional format support improvements
- 3.75.0 - Performance optimizations
- 3.74.0 - Security and stability updates
- 3.73.0 - Feature additions and bug fixes
- 3.72.0 - Database improvements
- 3.71.0 - H2 database transition (OrientDB deprecated)
- 3.70.3 - Final OrientDB support release

### 2023 Release Notes
Notable releases included PostgreSQL performance improvements, cleanup policy enhancements, and format-specific updates for Docker, Maven, npm, and other supported formats.

### 2022 Release Notes  
Major releases focused on high availability improvements, cloud deployment optimizations, and security enhancements.

### 2021 Release Notes
Key developments included expanded cloud support, performance improvements, and enhanced repository management features.

### 2025 Release Notes

This page contains a list of 2025 Sonatype Nexus Repository releases, links to each release's release notes, and a brief list of major changes per release.

Note that while we strive to fully document new features before releasing them to our Cloud environments, there may be occasional delays. In such instances, we will update this page with links to the relevant help documentation as soon as it becomes available.

### 2024 Release Notes

This page contains a list of 2024 Sonatype Nexus Repository releases, links to each release's release notes, and a brief list of major changes per release.

### 2023 Release Notes

### 2022 Release Notes

### 2021 Release Notes

### Security Advisories

**Note:** Sonatype is currently refreshing its methodology for reporting on Security Advisories. This page contains historical data for informational purposes only.

## Sonatype Nexus Repository System Requirements

This topic covers system requirements for the Nexus Repository.

- Sonatype's product development lifecycle is explained in [Sonatype Sunsetting Information](../sonatype-product-overview/sonatype-sunsetting-information/index.md) . The supported versions are listed on the version status page.
- Sonatype Nexus Repository supports the `Linux` , `Windows` , and `MacOS` operating systems. Sonatype has not tested nor supported other operating systems.
- We recommend using a dedicated operating system user account to run each unique process on a given host. The Nexus Repository process user must be able to create a valid shell. Do not run Nexus Repository as the `root` user.
- Nexus Repository consumes more file handles than the default value allowed by Linux or MacOS operating systems. Some container platforms (e.g., Amazon ECS) override the default limits set on the container. Running out of file descriptors leads to data loss. Increase the limit on the number of open file descriptors for the user running Nexus Repository. See the topic, [Adjusting the File Handle Limits](#adjusting-the-file-handle-limits) for instructions on how to do this in your environment.
- Our policy is to support the most recent modern browser version of your supported OS at the time of the Nexus Repository version release date.
- Sonatype does not officially support nor recommend using virus scanners with Nexus Repository. We have seen 10x longer startup times on Windows servers and significant performance impact when using a virus scanner to monitor the installation directory.

### Supported Java Versions

Nexus Repository is tested on and supports **OpenJDK** and requires **Java 17** . Nexus Repository is compatible with both Intel and AMD CPU architectures.

As of release 2.78.0 the Nexus Repository bundle includes the recommended JVM.

See [Java Compatibility Matrix](../sonatype-product-overview/java-compatibility-matrix.md) .

### CPU

Performance is primarily bounded by IO (disk and network) rather than CPU. Available CPUs will impact longer-running operations and thread count. See the [thread allocation algorithms of the web container](https://support.sonatype.com/hc/en-us/articles/360000744687-Understanding-Eclipse-Jetty-9-4-8-Thread-Allocation) .

See the Memory Recommendations by Profile Size section below for CPU recommendation by deployment.

### Memory Requirements

At a high level, expect to allocate up to **two-thirds of available RAM** to Nexus Repository; leaving **one-third of RAM** available for system processes and buffers.

Memory requirements vary by profile size. There is not a single defined requirement due to the complexity of all possible use cases. The section below outlines the memory and CPU recommendations for each node in small, medium, large, and very large profiles.

Highly available deployments must meet these requirements for all nodes in the cluster.

See our [Nexus Repository Memory Overview topic](#nexus-repository-memory-overview) for details about the different types of memory that Nexus Repository uses and examples of memory-related Java requirements.

### Database Requirements

Nexus Repository supports two database options: an embedded H2 database or an external PostgreSQL database.

### Disk Space Requirements

Required disk space for Nexus Repository varies by deployment size and complexity. You must have **at least 4GB available disk space at all times** ; if available disk space drops below 4GB, the database will switch to read-only mode.

Sonatype Nexus Repository requires disk space for two primary directories:

- **Application Directory** - Size varies slightly per release; as of August 2024, it is around **390MB** . It is normal to have multiple application directories installed on the same host over time as you upgrade.
- **Data Directory** - Size varies based on complexity and formats. Plan for substantial disk space. Note that formats like Docker and Maven can use very large amounts of storage (500GB easily).

### File Systems

Nexus Repository has two primary storage requirements:

- **Embedded data** : requires very responsive, fast storage, ideally local disk
- **Blob storage** : requires moderately responsive, high-capacity storage

### Requirements for High Availability

This section covers specific requirements for high-availability (HA) deployments for Nexus Repository. Review the following details before starting:

- High-availability (HA) deployments are only available for Nexus Repository Pro customers.
- Prepare to have in-house expertise in these technologies. E.g.; Load Balancer, Kubernetes, Helm Charts, Docker, Cloud Infrastructure, etc.
- Evaluate the total investment costs of your architecture to meet your expected traffic and business requirements.
- Improper deployment to production may result in excessive downtime and data loss.

### Adjusting the File Handle Limits

This topic covers how to adjust file handle limits in Linux and MacOS. It also provides details on ensuring container platforms do not override the file handle limits configured in our Docker images.

### Adjust the PostgreSQL Max Connections

High-availability deployments require more connections than those provided by the default value. Set the value high enough to account for the connection pool sizes of all Nexus Repository nodes as well as a buffer for DBAs and automated tools that connect directly to the database.

Increasing the connections available requires more resources for the PostgreSQL server. Make sure your server has enough resources to handle the additional load. See the PostgreSQL requirements section below for recommendations on server sizing. Your specific reference architecture also includes these recommendations.

### Nexus Repository Memory Overview

The sections below explain the different configurable memory types, Java arguments for managing certain memory configurations, and examples of using those Java arguments.

### Installing the Trigram Module

This section covers installing the postgresql-contrib package available from your Linux distribution. In order to install it, the PostgreSQL user must have **CREATE** privileges on the current database. This can be granted using a command like the following:

```
grant create on database <database_name> to <database_user>;
```

After granting CREATE privileges for your database, you will then need to install the postgresql-contrib package available from your Linux distribution. For example, you might use the following for Fedora:

```
sudo dnf install postgresql-contrib
```

Once installed, execute the following command to create the extension. If your JDBC URL does not specify a schema, then use public:

```
create extension pg_trgm schema <schema>;
```

Once that is done, you should see the extension listed:

```
select * from pg_extension;
```

Once that is done, you should see the extension listed:

### Advanced Database Memory Tuning

To apply database tuning settings like those below, amend the postgresql.conf file, save, and restart the database.

If you are unsure where the conf file is located, you can use the following command:

```
psql -U postgres -c 'SHOW config_file'
```

## Performance Data

Sonatype provides performance data to help with assessing features and deployment methods that your organization could benefit from. The following testing reports are available for the performance of Nexus Repository:

### Deployment Architecture

- [High Availability using AWS](#sonatype-nexus-repository-high-availability-performance-data-using-aws)
- [High Availability using Azure](#sonatype-nexus-repository-high-availability-performance-data-using-azure)

### Repository Feature Performance

- [Cleanup](#cleanup-performance-data)
- [Change Repository Blob Store Task](#change-repository-blob-store-task-performance-testing)
- [Repository Size Calculations](#repository-size-calculation-performance-data) NEW IN 3.68.0

### Sonatype Nexus Repository High Availability Performance Data Using AWS

For full transparency and to help you evaluate whether a High Availability (HA) Sonatype Nexus Repository deployment is right for your organization, we are providing findings from our internal performance testing.

### Sonatype Nexus Repository High Availability Performance Data Using Azure

For full transparency and to help you evaluate whether a High Availability (HA) Sonatype Nexus Repository deployment is right for your organization, we are providing findings from our internal performance testing.

### Sonatype Nexus Repository High Availability Performance Data Using Google Cloud Platform

The following findings are from our internal performance testing to provide transparency in evaluating when a High Availability (HA) Sonatype Nexus Repository deployment is right for your organization.

### Cleanup Performance Data

This testing aimed to evaluate performance between Java- and SQL-based cleanup. It also sought to understand performance impacts when opting to retain specific versions while using SQL-based cleanup; this feature was added in release 3.65.0.

As of release 3.65.0, Nexus Repository deployments using PostgreSQL databases use SQL-based cleanup by default.

### Repository Size Calculation Performance Data

The repository size calculation test case evaluates performance when loading the the repository sizes displayed under *Settings* → *Repository* → *Repositories* . This feature is available for deployments using a PostgreSQL database.

### Change Repository Blob Store Task Performance Testing

### Recalculate Blob Store Storage Task Performance Testing

In Sonatype Nexus Repository 3.69.0, we introduced the *Repair - Recalculate blob store storage* task that calculates the total space occupied by blobs in a blob store. We are providing the performance testing information below to help you appropriately plan and allocate resources for using this task.

## Nexus Repository Professional Features

Sonatype Nexus Repository Community Edition provides a solid foundation for any organization getting started with fully managing its software supply chain. As usage grows and your teams require more mature capabilities, we recommend upgrading to the Nexus Repository Professional edition to unlock the features needed to fully support your critical infrastructure.

The following features as some of the benefits you unlock when you upgrade to Pro. [Click here](https://www.sonatype.com/products/repository-pro/trial) to start your free trial.

### World Class Enterprise Support

Sonatype Nexus Repository Pro users receive access to our world-class support organization. This highly skilled group works with you to resolve issues encountered while using the product.

Details are found in our [Support Policy](https://www.sonatype.com/usage/software-support-policy) .

### Customer Success

Sonatype invests in every enterprise customer through our Customer Success team. This team is unique in that they proactively and continuously collaborate with you to ensure you derive ongoing value from your investment.

Ask them about training in repository management for your teams and providing a Repository Health Check to perform a details review of your development while providing guidance to help your organization mature.

### High Availability and Resilient Deployments

Nexus Repository is mission-critical for your business. Highly available (HA) deployments protect your business in the event of disaster or outages. We include a growing list of resilient deployment architectures and recovery tools to protect your investment.

Nexus Repository Pro protects your data from risk while reducing your recovery time and meeting recovery point objectives.

### SAML Authentication and Single Sign-On

Nexus Repository Pro integrates with many identity providers for centralized identity management. Using SAML, Nexus Repository acts as a service provider that receives users' authentication and authorization information from external identity providers.

### User Token Support

Sonatype Nexus Repository Pro’s user token feature establishes a two-part token for the user. Usage of the token acts as a substitute method for authentication that would normally require passing your username and password in plain text.

User tokens reduce the risk of exposing your enterprise credentials when using external tools such as CI build services, automation tools, development environments, and scripting with the REST APIs. Administrators may reset and rotate keys from within the Nexus Repository as part of their security policies.

### Content Replication

Teams today rarely work from a single location, so why should artifacts be stuck in one? Content replication allows you to make artifacts readily available across distributed teams. With content replication, you can manage what binaries are copied from one instance and pre-emptively pulled via HTTP to other instances. Here's how it works:

### Staging and Build Promotion

Nexus Repository Pro provides Staging and Build Promotion capabilities to ensure the integrity and quality of software components before they are released. This feature allows organizations to implement controlled workflows for validating, testing, and promoting artifacts through different lifecycle stages.

With staging, users can temporarily hold newly published components in an isolated repository before making them available in a release repository. This approach helps prevent the accidental deployment of incomplete or unverified artifacts. Build promotion further enhances this process by enabling teams to transition artifacts from one repository to another based on validation criteria, ensuring that only approved versions reach production.

By integrating Staging and Build Promotion into their software development lifecycle, teams can enforce quality gates, reduce deployment risks, and maintain better governance over their repositories.

For more details, refer to the Staging documentation in the Nexus Repository administration guide.

![16355975.png](/docs-at-surgery-poc/assets/images/uuid-215b839a-15ea-ef18-01c6-32e06154c964.png)

### Tagging

Nexus Repository Pro includes a Tagging feature that allows users to assign metadata tags to repository components, simplifying asset organization, tracking, and management. By applying tags, teams can efficiently categorize and reference specific artifacts across different repositories, enabling better version control and lifecycle management.

With Tagging, users can:

- Identify and group related components for streamlined retrieval.
- Track artifacts across different development and deployment stages.
- Integrate tagging into automated workflows for enhanced DevOps processes.

This feature is particularly useful for managing artifacts in large-scale environments, where clear identification and traceability are essential for governance and compliance. The implementation is highly flexible to include any metadata you need to track with the components.

For more details, refer to the Tagging documentation in the Nexus Repository administration guide.

### Retain Select Versions for Cleanup Policies

Nexus Repository Pro includes the Retain Select Versions feature as part of its cleanup policies, providing greater control over artifact retention. This feature allows users to specify and preserve particular versions of components while automatically removing older or unnecessary versions based on defined cleanup rules.

By leveraging Retain Select Versions, organizations can ensure that critical versions remain available while optimizing storage usage and maintaining repository hygiene. This capability is especially beneficial for teams that need to keep specific releases for compliance, rollback, or long-term support purposes while still automating repository cleanup.

For more details, refer to the Cleanup Policies documentation in the Nexus Repository administration guide.

### Import and Export Repositories

Importing and exporting repositories is a common enterprise capability to move a large number of components between repositories or repository managers. Use cases to utilize import and export include:

These tasks keep track of the last run results and if run again, they will skip files that were processed previously. These tasks work with HA-C setup.

A temporary file system location is needed for these tasks to export to and import from. Please also ensure the Sonatype Nexus Repository instance running the task has sufficient disk space for export and blob storage for import before running this task to avoid disk full issues.

### Google Cloud Blob Store

The Google Cloud Storage Blob Store allows assets to be stored in a Google Cloud Storage (GCS) bucket. Nexus Repository Pro can take advantage of the storage features that Google Cloud provides, such as redundancy options, configurable storage classes, and access control when running within the Google Cloud environment.

### Azure Blob Store

The Azure Blob Store allows assets to be stored in an Azure Storage Account container. Nexus Repository Pro can take advantage of the storage features that Azure provides such as replication, configurable performance profiles, and access control when running from within the Azure cloud.

### Group Blob Stores

A group blob store combines multiple blob stores to function as a single location for your repositories. Members of the group can be added or removed. Fill Policies are selectable algorithms that determine to which group member a blob is written. These features significantly increase the flexibility customers have in using and upgrading their storage. More information can be found in the Nexus Repository Storage Guide documentation.

### Change Repository Blob Store

Change repository blob store is a task that allows changing the blob store of a given repository. It moves the blobs from the chosen repository to a different blob store.

Some common use cases to utilize the Change Repository Blob Store task:

### Docker Subdomain Connector

Nexus Repository Pro supports the Docker Subdomain Connector, allowing users to configure a dedicated subdomain for their Docker repositories. This feature simplifies repository access by enabling fully qualified domain names (FQDNs) for Docker registries, eliminating the need to specify a port number when pulling or pushing images.

By using the Docker Subdomain Connector, organizations can improve usability, align with industry best practices, and integrate seamlessly with Docker clients and automation tools. This functionality is particularly useful in environments where security policies restrict non-standard ports or where multiple Docker repositories require clear separation by domain.

For more details, refer to the Docker Subdomain Connector documentation in the Nexus Repository administration guide.

### Deployment to Group Repositories

Nexus Repository Pro supports Deployment to Group Repositories for **npm** and **Docker** registries, allowing users to publish artifacts to a group repository. When configuring the group, a hosted repository is set to store published artifacts. This feature simplifies artifact management by enabling deployment to a single endpoint while ensuring that the artifact is available to all member repositories within the group.

This capability enhances repository management efficiency and is particularly beneficial for teams that require centralized artifact deployment while maintaining access through a unified repository group.

- Using a single endpoint to pull and publish means fewer exposed docker connector ports are required.
- Docker groups reuse layers published across mutiple repositories reducing the required storage. Published images only require that the proprietary layers are pushed.
- Docker doesn't provide a way to specify different endpoints for pushing and pulling content complicating the build process. This feature lets you configure a single endpoint.

### Repository Health Check (RHC)

Nexus Repository users can automatically identify open-source security risks at the earliest stages of their DevOps pipeline. Specifically, the RHC feature empowers software development teams with important capabilities:

- **Risk Prioritization**: Prioritizes vulnerable components by severity and impact, showing download frequency over the past 30 days to help focus remediation efforts.
- **Remediation Guidance**: Provides actionable recommendations on which components should be upgraded or replaced to address security vulnerabilities.

### Atlassian Crowd Support

Atlassian Crowd is a single sign-on and identity management product that many organizations use to consolidate user accounts and control which users and groups have access to which applications. Atlassian Crowd support is a feature preinstalled and ready to configure in Nexus Repository Pro. Nexus Repository contains a security realm that allows you to configure Nexus Repository to authenticate against an Atlassian Crowd instance.

## Nexus Repository Feature Matrix

This matrix outlines the Nexus Repository features available in Community Edition versus a Professional (PRO) license. The matrix is updated as new features are released. Unsupported items are represented by a red x (error)" icon, while supported items are represented by a green "(tick)" icon.

Contact [nexus-feedback@sonatype.com](mailto:nexus-feedback@sonatype.com) with questions on specific features.

### Nexus Repository Support

Sonatype support for Nexus Repository is crucial for organizations relying on the platform for mission-critical software delivery. A professional license unlocks direct access to Sonatype's expertise, providing invaluable assistance with complex configurations, troubleshooting, performance optimization, and integration challenges.

[Enterprise-level Sonatype Support](https://support.sonatype.com/hc/en-us/requests/new)

For Nexus Repository Community Edition users, the vibrant Nexus Repository community serves as a valuable resource for support and guidance. While not offering the direct, one-on-one assistance of a professional Sonatype license, the community provides a platform for users to connect with peers, share experiences, and find solutions to common challenges.

Community Edition users are recommended to select the `Ask Sona` chatbot to provide relevant information, links, and suggestions based on your query.

[Community](https://community.sonatype.com/) and [Knowledge Base](https://support.sonatype.com)

### Custom Metadata

**Note**: The Custom Metadata feature has been deprecated and replaced with the component tagging feature in Nexus Repository Pro.

## Nexus Repository Telemetry

Sonatype Nexus Repository's in-product analytics feature helps improve Nexus Repository, guiding the areas on which we focus our efforts.

### What Gets Sent?

This feature will collect anonymous, non-sensitive information on the general use of Nexus Repository.

- We do not collect information that identifies specific users: no usernames, passwords, emails, hostnames, or URLs of any kind.
- This feature doesn’t collect identifying information on which you or your teams are working. We don’t collect repository names, component names, coordinates or paths, the names or content of content selectors or routing rules, or paths of any kind—anything that might inadvertently contain information about your organization’s projects or the components you’re using.
- We collect high-level configuration choices, feature usage rates, internal error frequency, and performance information. Are you using the S3 blob store support? Is it working well? Is it fast enough? Have you switched to NuGet v3, or is v2 still everywhere?
- We collect a limited amount of environmental information to help us understand nuts and bolts details like memory and thread pool efficiency. This also helps us see how the great cloud migration is going and when it’s time to deepen our support for new environments where you are deploying Nexus Repository.

### Feedback

While automated data is useful, we continue to rely on feedback from developers and DevOps professionals like you to truly understand how you’re using Nexus Repository and how well it meets your needs.

If you have questions or feedback about this program or any other aspect of Nexus Repository, please let us know [in the Nexus Repository Manager category.](https://community.sonatype.com/c/nexus-repository/6)

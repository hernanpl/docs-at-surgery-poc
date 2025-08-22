---
layout: default
title: "Upgrade Nexus Repository"
parent: Sonatype Nexus Repository
nav_order: 5
---

# Upgrade Nexus Repository

Upgrading the Nexus Repository is necessary for new features, bug fixes, performance improvements, and other security patches. Regularly updating to the latest release is recommended.

## Pre-Upgrade Checklist

## Perform the Upgrade

## Nexus Repository Upgrade Paths

Find the Nexus Repository version you have in the left column. Follow the upgrade procedure in the right column.

## Upgrading to Nexus Repository 3.71.0 and Beyond

Nexus Repository 3.70.x release branch are the final releases to support the embedded OrientDB database, Java 8, and Java 11. Before updating to a release after 3.70.x, you must migrate off from Orient database and upgrade your version of Java. Support for OrientDB is being sunsetted and is no longer included in Nexus Repository versions 3.71.0 and beyond.

See the Nexus Repository Sunsetting Information documentation

Expand the section below that corresponds to your current database. If you don't know your current database, see the Determining Current Database help topic .

### Upgrade Paths

The table below provides a brief overview of the upgrade process based on your current database.

### Nexus Repository Deployments Using OrientDB

If you are already using a PostgreSQL database, you can upgrade your Nexus Repository instance following your typical upgrade instructions. However, you will still need to upgrade your Java version to Java 17; Nexus Repository 3.71.0+ does not support Java 8 or 11. If you do not know how to change your Java version, see our documentation on how to change your Java version .

![Orient_369_java811.png](/docs-at-surgery-poc/assets/images/uuid-06403468-cf21-df55-3399-8b19730da6f5.png)

### Nexus Repository Deployments Using H2

Nexus Repository versions from 3.70.0 and beyond require a version 2.x H2 database; previous Nexus Repository versions used a version 1.x database. Therefore, you will need to run a task to export your H2 v1.x database before upgrading Nexus Repository. Sonatype added this task in version 3.69.0, so you must be on 3.69.0 before proceeding. The sections below will walk you through this process.

The internal H2 database used by Nexus Repository was updated in the 3.71.0 release. This upgrade workflow requires exporting the H2 database using a special task available in the 3.69.0 release before upgrading. Support for Java 17 was introduced in the 3.69.0 release and is required for all future releases.

![H2_Pre368_Java811.png]({{ /assets/images/uuid-1a81d9d4-cc4a-0d1b-a77d-6606feb7f03b.png)

### Nexus Repository Deployments Using PostgreSQL

If you are already using a PostgreSQL database, you can upgrade your Nexus Repository instance following your typical upgrade instructions. However, you will still need to upgrade your Java version to Java 17; Nexus Repository 3.71.0+ does not support Java 8 or 11. If you do not know how to change your Java version, see our documentation on how to change your Java version .

## Upgrade from Nexus Repository 2

Nexus Repository 3 is a complete redesign that does not include legacy code from Nexus Repository 2. Nexus Repository 3 uses a different storage model for managing components that is far more scalable for non-Maven ecosystems and deployment environments. While this avoids file system limitations from Nexus Repository 2, upgrading requires completely transforming the repository metadata and artifact storage model.

Nexus Repository 3 has a non-destructive built-in upgrade wizard to migrate content from Nexus Repository 2 deployments. While this method is recommended and acceptable for most deployments some caveats must be considered before beginning.

Review the [Feature Equivalency Matrix](#UUID-634482c9-b9f5-488c-536e-e8a2cb662ae5)

### Built-in Upgrade Wizard

Using the upgrade wizard is the preferred method when your deployment meets all of the requirements. In some cases, you may combine this method for the majority of the migration along with other methods for content that falls out of the requirements.

- **Community Edition (CE)** : both instances must be on corresponding versions of Nexus Repository 2 and 3. Nexus Repository 3 CE deployments need to migrate to 3.76.0 deployed with Java 17 using an H2 database before upgrading to later versions. **Professional (Pro) License** : Upgrade to the latest version with an external PostgreSQL database.
- This method is not supported when already using Nexus Repository 3.
- You cannot upgrade when only one instance has the Pro license installed.
- Nexus Repository 2 allowed different cases for repository names. This is not allowed in Nexus Repository 3.

See [Upgrade Wizard](#UUID-f9bdd27b-511a-5aa1-c462-6ad9e18fe6ee)

### Using the Repository Import Task

Organizations may consolidate by importing content into Nexus Repository 3 using the [Repository Import](#UUID-1f2f2f72-0cc4-084a-43de-ed7d1b38dc60) task.

- Best for those already using Nexus Repository 3 and needing to import Nexus Repository 2 content into the existing Nexus Repository 3 instance.
- The import task brings in the content of a folder on disk that the server has permissions and access to. The repositories from Nexus Repository 2 are already in this format and do not need to export them from the repository first. You may connect directly to the repository on disk or using a backup. Using Hard Linking is far faster and does not duplicate the data on disk. New files added after the import start are picked up by the task and imported. The import may be run multiple times to bring in any differences.
- This moves repository contents, not the configuration. Metadata such as creation and last download dates are set to when the content is imported into Nexus Repository 3. The import task is able to maintain the created date, last updated date, and the last downloaded date attributes from Nexus Repository 2. This may complicate cleaning up repositories after importing.
- Proxy repositories from Nexus Repository 2 would need to be imported as hosted repositories.
- You need to create and run individual tasks for each repository. Multiple tasks do not run at the same time.
- This method takes significant amount of time when importing a lot of data to copy into the repository. Use the Proxying Repositories method below to make the source content available while waiting for the import tasks to complete.

### Importing through Proxy Repositories

Using proxy repositories is an effective way of making Nexus Repository 2 content available in Nexus Repository 3 while both versions are used in production.

- Only the content actively requested in Nexus Repository 3 is fetched from Nexus Repository 2. This may be a method to separate unused content.
- The Nexus Repository 2 must be available for Nexus Repository 3 to fetch content so both environments would need to be maintained for a long enough amount of time for all content to be migrated. This method may be difficult to know when Nexus Repository 2 is no longer needed.
- The content from Nexus Repository 2 is stored in proxy repositories in Nexus Repository 3.
- This method requires creating a proxy repository for every repository to migrate from Nexus Repository 2. We recommend adding these proxies to group repositories so that hosted content is accessible by a single endpoint.

### Upgrade Wizard

Nexus Repository includes the Upgrade Wizard used to migrate Nexus Repository 2 to a new Nexus Repository 3 instance. Upgrading to Nexus Repository 3 using the Upgrade Wizard is the preferred method.

### Changes during the Upgrade Process

The wizard includes the following configurations in the upgrade.

- Active Security Realms, Anonymous, Access Settings, Atlassian Crowd Settings, HTTP Proxy Settings, LDAP Settings, NuGet API Keys, Privileges, Repository Health Check, Role Mappings for LDAP/Crowd, Roles, SSL Certificates, Users User Tokens
- Maven2, npm, NuGet, Site Repositories, RubyGems (This does not include Maven2 staging repositories)
- Repositories keep items in quarantine. Changes to quarantined items are updated through the synchronization upgrade step.
- uploaded_by, uploaded_by_ip, uploaded_date, lastModified

### Upgrade Wizard Instructions

The upgrade wizard is meant to be used only once. Do not attempt to run the upgrade multiple times on production environments.

See [Upgrade Wizard](#UUID-f9bdd27b-511a-5aa1-c462-6ad9e18fe6ee) for Prerequisites

### Upgrading Staging

This topic provides Nexus Repository administrators valuable information about the change in staging implementation between Nexus Repository 2 and 3 as well as guidance on migrating your data and processes. For detailed information on using the staging feature in Nexus Repository 3, see the [Staging topic](#UUID-7bc63556-9690-e797-782e-538b2ec719cc) .

### Feature Equivalency Matrix

Nexus Repository 3 represents a complete rewrite of architecture and functionality. Some features from Nexus Repository 2 are no longer available in Nexus Repository 3. The matrix below details features replaced or removed in Nexus Repository 3.

## Migrating to a New Database

This topic covers migrating the database Nexus Repository uses with the Database Migrator utility.

Download the latest database migrator utility to receive the latest performance improvements.

See [Download the Latest Database Migrator Utility](#UUID-502a5426-c7f0-d5ee-9139-4a8b19bd5bc5_id_Download-DownloadSonatypeNexusRepositoryDatabaseMigrator)

### Considerations Before Migrating

Review the following considerations before migrating:

- The original Orient database is not changed and may be used as a recovery point. The migrator does not support migrating back to OrientDB from H2 or PostgreSQL. Running the migrator again overwrites any data in the target database.
- Run the database migration in the same environment to avoid complications and to simplify recovery when something goes wrong. Use the same version you were using before the migration. Migrating directly to the cloud from on-premises is not supported.
- We recommended performing a test migration using a backup of your production instance. Be aware that a backup instance connecting to cloud blob stores may still be connected to production data. The migration may skip artifacts from the source database when they are not found in the file reference. Consult the migration log files to valid the contents that was migrated. Searching and cleanup works differently in H2 and PostgreSQL databases. Evaluate that cleanup policies identify the correct components for cleanup.
- PostgreSQL and H2 do not support Bower or the community formats (e.g., APK, Composer, CPAN, Puppet). A subset of Nuget v2 protocol does not work the same as from OrientDB. Unsupported formats are not migrated. Custom plugins that interact with the database, assets, or components may no longer work with the new databases. Groovy scripting is not supported in later versions.

### Migration Environment Prerequisite Requirements

Review the requirements below for the database migration:

- A new version of the migration is released for every version of Nexus Repository to take advantage of improvements and bug fixes to the migration process. Only the latest version of the migration is available for download to avoid support issues. Upgrade to the latest supported version of Nexus Repository for your database.
- OrientDB is not supported in version of Nexus Repository past the 3.70.x branch. Your Nexus Repository instance must be on the latest 3.70.x version to migration from OrientDB. See [OrientDB Deployments](#UUID-9865c501-4a51-ce88-35b7-edcd84fbae85) .
- The database migrator does not support Oracle JDK. Migrating from OrientDB requires using Java 8 or 11. You will have to upgrade the version of Java after the upgrade depending on the supported version. Consult the system requirements for the version you are upgrading to.
- The `$data-dir/db` directory and the temp directory must have enough space for both the backup and the extracted backup to the tmp directory.

### Post-Migration Tasks

These tasks are critical to the proper functioning of the repository after the migration process and may take a notable amount of time to complete.

**Do not restart your instance** while the post-migration tasks are running to avoid damaging your browse and search index.

### Migrating From H2 to PostgreSQL

The section covers migrating Nexus Repository instance with an embedded H2 database to an external PostgreSQL database.

### Migrating From PostgreSQL to H2

This topic covers migrating from a PostgreSQL database to an embedded H2 database.

**Note:** Migrating a Nexus Repository Docker Image to H2 If you are migrating a Nexus Repository Docker image, log into the Docker image and run the Database Migrator following the normal instructions below.

Your Nexus Repository instance will now start in H2 mode with a migrated H2 database.

### Migrating From OrientDB to H2

Migrate Nexus Repository instance from OrientDB to H2.

### Migrating From OrientDB to PostgreSQL

The section below covers migrating your Nexus Repository instance from OrientDB to an external PostgreSQL database.

**Note:** When using AWS Aurora as your database, include `gssEncMode=disable` as a query parameter of JDBC URL.

### Determining Current Database

Confirm the database Nexus Repository is using by navigating to the data store view in *Settings* → *Repository* → *Data Store* . This displays the JDBC URL for your current database.

The *Data Store* screen appears for those using either an H2 or PostgreSQL database. To verify your instance is using OrientDB use the following steps:

- Navigate to the `System Information` under `Support → System Information` .
- Locate the `nexus-properties` section.
- Check that `nexus.orient.enabled` is `true` .

See the [Data Store](#UUID-0a4b7d32-de30-e0f5-be4f-e4d75cc118ef) topic for more information.

### Controlling Database Migrator Logging

The database migrator logs processing of individual components, assets, and content repository records at a `TRACE` level, so they will not appear in logs.

Items that are filtered, skipped, or encounter an error during processing still appear in the logs.

Modify logging levels using one of the following methods:

- Create an application.properties file in the folder from which you are running the database migrator. Add a line like the following:
- Pass an argument to the database migrator using a command like the following:

### Restoring a Database Backup After Migration

If you need to restore a particular backup from before migration to PostgreSQL, you would need to set up a new PostgreSQL instance and then complete the following steps:

### Reverting Back to OrientDB

The migration process is one-way: the migrator utility extracts configuration and component metadata from the Orient database and moves it to H2 or PostgreSQL. The Orient database is unchanged and remains in place as a restoration point.

Once you start a Nexus Repository instance, database and blob storage contents diverge. After this, reverting to Orient requires restoring the blob stores from the backup.

Use the following steps to revert to OrientDB:

We recommend running the blob store reconciliation task after reverting to reconcile changes to the blob store with the database with any binaries that you may have made since the migration.

**Note:** Legacy Embedded Orient Database Nexus Repository's legacy embedded Orient database entered extended maintenance in August 2024. All deployments must migrate off of OrientDB to upgrade to newer versions. Version 3.71.0 and beyond do not support OrientDB. If you are unable to migrate, you must remain on the 3.70.x version line.

## Rolling Upgrades in High Availability

High availability (HA) environments may upgrade Nexus Repository without downtime (i.e., rolling upgrade, zero-downtime upgrade).

### Terminology

- Zero-downtime upgrades in Nexus Repository mean the system remains available during updates, especially in HA clusters, ensuring uninterrupted artifact access. This is achieved through rolling upgrades, allowing users and builds to continue without service disruption.
- Updating a Nexus Repository by sequentially upgrading nodes in a high availability cluster, minimizing downtime for artifact access. Rolling upgrades involve stopping and upgrading each node before then upgrading the database schema. While an individual node is stopped, the other active nodes continue to serve traffic, resulting in no downtime for consumers of the service.
- Having different versions of Nexus Repository installed on the nodes of a cluster. While running in mixed mode, new features are not available until all the nodes on the cluster as well as the database schema are upgraded. While upgrading nodes, administrators may see a warning indicating that the cluster is running in mixed mode. Running in mixed mode outside of an active upgrade is not supported.

### Limitations for Rolling Upgrades

The following section details some limitations:

- You may need to upgrade to an intermediate version before going to the latest version. Upgrading Nexus Repository from 3.71.0 to 3.72.0 is the first version where zero-downtime upgrades are available.
- Running in mixed mode outside of an active upgrade is not supported. Nexus Repository may become unstable and behave in unexpected ways. Complete the upgrade in as short amount of time as possible to minimize the amount of time Nexus Repository nodes are on different versions.
- All nodes must have rolling upgrades enabled or they return an error when Nexus Repository detects mixed mode.
- When adding nodes during schema migration, these nodes stop with an error code and log the errors.
- You cannot roll back once you proceed with finalizing the upgrade by updating the database schema. You will need to restore from a backup to roll back.
- Without sticky sessions, users may see UI inconsistencies during the upgrade process due to changes made between versions. Sticky sessions need to be configured on your load balancer or ingress controller.

### Prerequisites for Rolling Upgrades

To use rolling upgrades with zero downtime, you must meet the following prerequisite requirements:

- Nexus Repository Pro in an HA environment with a PostgreSQL database using the supported HA Helm chart version 71.0.0 or above. Pro Feature
- Restart each instance after enabling the feature on each node before proceeding with the upgrade.
- NGINX provides documentation on [enabling session persistence](https://docs.nginx.com/nginx/admin-guide/load-balancer/http-load-balancer/) .

### Enable Zero-Downtime Upgrades

Zero-downtime upgrades must be enabled and restarted on every node before upgrading them. The process to enable is different depending on the environment you are running your cluster. Select the appropriate method below:

- Update the `values.yaml` with the zero downtime configuration.
- Update the Nexus Repository custom resource definition (NexusRepo)
- Update the `statefulset.yaml` with the zero downtime configuration.
- Set the environment variable for every node.
- modify the `$data-dir/sonatype-work/nexus3/etc/nexus.properties` for each node.

### Rolling Back on Zero-Downtime Upgrades

Zero downtime upgrades each node to the latest Nexus Repository version before updating the database. At any point before finalizing the changes to the database, the cluster may be rolled back to the version of Nexus Repository running previously.

- If the upgrade has not been finalized, the cluster is in mixed mode. Bring down the instance(s) with the higher version to move the nodes back to the older versions.
- The finalize button appears when all instances have the upgraded version, but the database is not yet upgraded. At this stage, you can start instances with the previous version to put the cluster back into mixed mode.
- Once finalized, rolling back is possible by restoring from a backup.

### Phase 1 - Upgrade Each Node

One node at a time; take the node offline, upgrade the node, and start the node using the new Nexus Repository version. Upgrade the nodes by replacing the binaries or follow the instructions for Kubernetes environments.

- Nodes are upgrades one at a time.
- The load balancer distributes requests to active nodes.
- PostgreSQL database remains on the old schema.

![Untitled.jpg](/docs-at-surgery-poc/assets/images/uuid-1499024c-e677-3dd8-6a97-f7d54ec53ee4.jpg)

### Phase 2 - Finalize Upgrade

Finalize the upgrade by migrating your database schema if applicable; not all releases will require a database schema migration.

When the upgrade requires a database schema migration, administrators with the `nexus:*` permission see a banner at the bottom of the screen. There is a delay of up to 10 minutes before the banner appears.

![Finalize_Upgrade_Banner.png]({{ /assets/images/uuid-b0bc06ef-f31e-64fd-522c-00e41876aa84.png)

### Supported Rolling Upgrade Paths

We may occasionally have limitations on eligible version upgrade ranges. Attempting to exceed the upgrade windows will result in new nodes failing to start. Follow this section to stay up to date on any required intermediate versions.

## Upgrade Nexus Repository Java Version

This section covers upgrading the Java version that your Nexus Repository instance is using. Before proceeding, make sure you understand which Nexus Repository versions are compatible with available Java versions.

The Sonatype team provides alternate distribution binaries and configuration to align with the supported Java version. You must download the correct distribution before switch to a different java version.

The metrics exported from the JVM through the metrics API endpoint and Prometheus may differ between Java versions.

### Upgrade with Docker

Use the Java version Docker tag to upgrade your Java version.

See [Nexus Repository tags in Docker Hub](https://hub.docker.com/r/sonatype/nexus3/tags)

### Upgrade with the Helm Chart

When using the Helm chart, set the Java version by update the `nexusTag` property in the `values.xml` of the chart. Use the available Docker images to set the appropriate tag.

```
container:
  image:
    repository: sonatype/nexus3      
    nexusTag: 3.78.0-java17
```

See the [Helm Chart](https://github.com/sonatype/nxrm3-ha-repository/blob/main/nxrm-ha/values.yaml#L94)

### Upgrading Your Java Version Using the Distribution Archive

Download the archive with the appropriate Java version from [Downloads](#UUID-502a5426-c7f0-d5ee-9139-4a8b19bd5bc5) . The Java SDK is bundled with the software distribution for MacOS, Windows, and Unix systems. Note that the Unix archive is bundled with a platform-specific JDK can not be used on a Mac.

## Upgrading Nexus Repository in a Kubernetes Environment

The following are instructions for upgrading your resilient or highly available (HA) Sonatype Nexus Repository deployment in a Kubernetes environment.

For Highly Available deployments, we recommend using Rolling Upgrades.

See [Rolling Upgrades in High Availability](#UUID-1d301297-d4f6-1358-5546-4fb54f3d8517)

**Note:** Using Zero-Downtime (Rolling) Upgrades When doing a zero-downtime upgrade (available when upgrading to 3.72.0+), you can also use `kubectl set image/undo rollout` for rollouts and rollbacks. See the [Kubernetes documentation on rolling back a deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#rolling-back-a-deployment) .

### Upgrading Using YAMLs Without Helm Charts

### Upgrading Using Helm Charts

This section covers upgrading Sonatype Nexus Repository using a Helm chart.

**Note:** Updating to Helm Chart with Shared Logging From Nexus Repository release 3.68.0 forward, the Helm chart uses a shared logging location. Before updating to a Nexus Repository 3.68.0+ Helm chart from an earlier version, download a support zip for each of your Nexus Repository instances.

### Upgrading to the Combined Helm Chart

Before release 3.62.0, we offered separate Helm charts for AWS and Azure environments. As of release 3.62.0, we offer a single HA Helm chart ( [GitHub](https://github.com/sonatype/nxrm3-ha-repository/tree/main/nxrm-ha) , [ArtifactHub](https://artifacthub.io/packages/helm/sonatype/nxrm-ha) ) to used in AWS, Azure, or on-premises deployments.

If you were previously using one of the separate Helm charts and will now be using the combined one, follow these steps:

## Upgrading an H2 Database from 1.x to 2.x

Release 3.70.0 upgraded Nexus Repository's embedded H2 database from version 1.4.200 to the 2.x H2 version line. This means that Nexus Repository versions 3.70.0 and beyond are no longer compatible with H2's version 1.x line, and upgrading your H2 database to 2.x is required to upgrade Nexus Repository to version 3.70.0+.

As noted in the [H2 upgrade documentation](https://www.h2database.com/html/migration-to-v2.html) , there are many changes between the 1.x and 2.x version lines. Sonatype created an easy way to help H2 users upgrade their H2 databases when upgrading to Nexus Repository 3.70.0 and beyond.

### Prerequisites for Upgrading the H2 Database

Upgrading the H2 database involves exporting the database. Changes made after exporting are lost and not included in the exported file.

To minimize any potential for lost information during the upgrade period, complete the following prerequisite steps immediately before upgrading to Nexus Repository 3.70.0+:

You can now continue to upgrade your Nexus Repository instance to version 3.70.0+

### Upgrading Your H2 Database and Nexus Repository Instance

After meeting the prerequisite steps, use the following steps to complete both your Nexus Repository and H2 upgrades:

### Rolling Back an H2 Upgrade

Should you need to retry an H2 upgrade, you need to roll back your instance as well. Before rolling anything back, check your $data-dir/db folder to see if it contains a `nexus-<timestamp>-backup.zip` file. If not, go back to Nexus Repository 3.69.0.

## Migrating to a Resilient Deployment

Migrating Nexus Repository to a resilient architecture requires migrating to an external PostgreSQL database and migrating your blob stores before changing the server architecture. Deployments currently using PostgreSQL and object storage may skip to the reference architectures while reviewing this documentation to cover any required configuration.

We recommend migrating in phases while testing the service at each phase. Similarly, we recommend starting with a single node in the new environment before scaling to a highly available cluster. This reduces the complexity and potential points of error.

### Moving from On-Premise to Cloud Platforms

When migrating from on-premise to cloud deployments, we recommend using a lift-and-shift approach.

**Lift-and-shift** is a cloud migration strategy where an organization moves its existing Nexus Repository deployment from an on-premises environment to the cloud without making significant modifications to its architecture, code, or functionality. We recommend maintaining your current architecture as much as possible during the initial move.

One exception to this guidance is to use a load balancer from the start rather than connecting directly to the Nexus Repository server. This reduces the amount of effort required later to reconfigure builds and tooling pointing to Nexus Repository as you scale your service.

See [Migrating Blobs to the Cloud](#UUID-853e0b2d-afd6-8076-9e52-bbaef1296d67_id_ConfiguringBlobStores-MigratingfromanOn-PremisesBlobStoretoaCloudBlobStoreUsingVendor-ProvidedTools) for recommended tooling to migrate your data to the cloud environment.

### Migrating to PostgreSQL Database

Resilient and high-availability architecture requires using an external PostgreSQL database. For cloud deployments, we recommend using the following cloud services for your PostgreSQL database:

- AWS Aurora or RDS PostgreSQL
- Azure Database for PostgreSQL
- Google Cloud SQL for PostgreSQL

For all migrations, follow these instructions for [Migrating to PostgreSQL](#UUID-a3ea5445-b958-e8a6-d3e7-b2d3086c58a3) .

### On-Premise Deployments

On-premise is defined as either your infrastructure or a data center managed by your organization. While you may use similar technologies as those managed by the cloud providers, these instructions are separate to isolate cloud-specific requirements.

For any resilient deployment, the blob stores should not be located in the `sonatype-work` directory so you may be required to move the blob stores depending on your chosen deployment.

- [Resilient single-node deployment](#UUID-fc1c4086-a8a2-0fce-2726-05395ca1e035)
- [High-availability multi-node deployment](#UUID-988b4409-5bfe-5b4b-d2fd-cc19c781f491)

### Cloud Deployments

After migrating the database, move your blob stores to the cloud's object storage. Resilient and high-availability deployments leverage object storage for reliability and redundancy.

See [Migrating Blobs to the Cloud](#UUID-853e0b2d-afd6-8076-9e52-bbaef1296d67_id_ConfiguringBlobStores-MigratingfromanOn-PremisesBlobStoretoaCloudBlobStoreUsingVendor-ProvidedTools) for steps in copying your blob stores to your cloud object storage.

## Moving from a High Availability Deployment to a Single Instance

This topic provides instructions to follow should you need to move from a clustered, highly available Nexus Repository deployment to a single instance.

### Container-Based Instructions

### Non-Container-Based Instructions

## Migrate to Nexus Repository from Artifactory

Migrating from JFrog Artifactory to Sonatype Nexus Repository involves several key steps. Here's a breakdown of the process, covering planning, data migration, configuration, and testing.

- **Local -> Hosted Repositories** : For storing your internal artifacts.
- **Remote -> Proxy Repositories** : For proxying external repositories.
- **Virtual -> Group Repositories** : For aggregating multiple local(hosted) and remote(proxy) repositories.

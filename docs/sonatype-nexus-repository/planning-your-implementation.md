---
layout: default
title: "Planning Your Implementation"
parent: Sonatype Nexus Repository
nav_order: 3
---

# Planning Your Implementation

Before installing Nexus Repository, you should take some time to consider your specific needs so that you can plan a robust implementation. Some specific things to consider include the following:

- Do you need a resilient deployment?
- Will you use an external PostgreSQL database?
- What installation method will you use?
- Have you considered how to secure your implementation?

Read about the above topics and much more in this section.

## Nexus Repository Reference Architectures

Reference architectures are designed to provide guidance in deploying Nexus Repository with adequate resources, tailored to anticipated load profiles based on real-world data and customer experience. Selecting the appropriate architecture is crucial for deployment stability and performance. Insufficient resource allocation leads to performance degradation, data integrity issues, or data loss.

Organizations also use multiple deployments to serve different business requirements and for scalability across regions. We provide a deployment pattern library of common use cases aligned to business outcomes.

See the Deployment Pattern Library section below

Use the table below to identify which profile best matches your needs. Select the link to the appropriate deployment architecture from the header row.

** The recommendations for sizing listed above are not related to Community Edition limits. The use of the Postgres supported architecture is available for Community Edition, however, it not does not included an increase to the usage limits.*

### Sizing Your Deployment

Nexus Repository deployments have access to usage statistics to determine the scale of their deployment.

See [Usage Metrics](https://help.sonatype.com/en/usage-metrics.html)

New deployments need to forecast their usage to size their deployment. Consider the following practices when projecting load:

- Using Nexus Repository to proxy third-party components for builds
- The number of applications in active development and the frequency of when they are built
- The number of developers that will use Nexus Repository as a system of record
- Enabling anonymous access for publicly available downloads
- Automation tasks that make requests to the repository

### Nexus Repository Reference Architecture 1

### Nexus Repository Reference Architecture 2

### Nexus Repository Reference Architecture 3

### Nexus Repository Reference Architecture 4

## Deployment Pattern Library

Nexus Repository is mission-critical infrastructure with the need to balance the availability of the service with the cost of the hardware required to operate. Many Nexus Repository users have deployment teams across the globe, making effective and efficient distribution essential. In evaluating industry struggles and our customers' needs, we've identified three primary concerns that can be addressed with appropriate deployment patterns: resiliency, scalability, and distribution.

- Resiliency refers to the ability to recover from disruptions to critical processes and supporting technology systems. Regardless of your distribution and scalability needs, you must have some level of resiliency for a successful deployment. Resiliency starts with backup and restore procedures. Use this pattern for every Nexus Repository instance that is a system of record in your deployment. See the Resiliency documentation for a comprehensive list of failure scenarios and recommendations.
- Enterprise deployments experience large spikes in requests or require scalability to handle intense workloads. Scalability refers to a deployment's ability to adjust to these flexible, changing demands. These are some ways Nexus Repository can be scaled. Adding capacity in terms of compute, memory, and faster storage. Separating distinct workloads such as development, distribution, or ecosystems. Distributing requests across an HA cluster or independent servers proxying from a central source.
- Adding capacity in terms of compute, memory, and faster storage.
- Separating distinct workloads such as development, distribution, or ecosystems.
- Distributing requests across an HA cluster or independent servers proxying from a central source.
- A solid Nexus Repository deployment requires establishing both your current and future distribution needs. You can define these by answering a few important questions: You'll need to decide how many authoritative vs. transient instances you need; this helps determine a base deployment pattern from which to design your full deployment. A star pattern is a centralized administration with transient servers as local proxies. A federated deployment will involve distinct regional hubs sharing replicated content. When there are very high read traffic on a single system of record consider distributing this traffic to more transient proxy nodes to insolate your development environments. See the scaling with proxies documentation Bi-directional proxying allows users to pull artifacts on demand from a distant repository via a proxy repository Content replication proactively pulls content from a central host repository so content is quickly available on the remote server.
- You'll need to decide how many authoritative vs. transient instances you need; this helps determine a base deployment pattern from which to design your full deployment. A star pattern is a centralized administration with transient servers as local proxies. A federated deployment will involve distinct regional hubs sharing replicated content.
- When there are very high read traffic on a single system of record consider distributing this traffic to more transient proxy nodes to insolate your development environments. See the scaling with proxies documentation
- Bi-directional proxying allows users to pull artifacts on demand from a distant repository via a proxy repository Content replication proactively pulls content from a central host repository so content is quickly available on the remote server.

### Deployment Patterns

The patterns in this library represent proven ways of deploying Nexus Repository; you likely need to combine multiple patterns to meet your needs.

### Backup/Same-Site Restore

![189431856.png](/docs-at-surgery-poc/assets/images/uuid-831ac8df-a461-8d81-fd6b-1d4cdf13a81b.png)

The backup/same-site restore pattern is the most common and simplest pattern to address data integrity and corruption concerns. With this pattern, you simply back up your Sonatype Nexus Repository instance so that you can restore from a point in time should it become necessary.

### Disaster Recovery Site

The disaster recovery pattern provides recovery across data centers or cloud regions. Your disaster recovery site will have a cold standby node ready to go so that you can spin up a Nexus Repository instance and switch to this site in the event of failure at your primary site.

![Disaster Recovery Site deployment pattern](/docs-at-surgery-poc/assets/images/uuid-084d6e08-3155-fdb3-64e2-72c47d2ded38.png)

### On-Prem Active/Passive Resiliency

Active/Passive resiliency patterns with automatic recovery mechanisms like Kubernetes allow you to accomplish automatic failover without manual intervention in the event of node or VM failure.

![189431862.png](/docs-at-surgery-poc/assets/images/uuid-36338d95-5843-0b33-aa00-4727c923f040.png)

### Cloud Active/Passive Resiliency

Active/Passive resiliency patterns with automatic recovery mechanisms like Kubernetes allow you to accomplish automatic failover without manual intervention in the event of node or availability zone failure.

![Cloud Active Passive Resiliency Deployment Pattern](/docs-at-surgery-poc/assets/images/uuid-d14f77ed-6461-e105-b6dc-f1ab150a6a39.png)

### On-Prem Active/Active High Availability

When Sonatype Nexus Repository is mission-critical, an active/active high availability deployment pattern can help you maximize uptime and minimize data loss in the event of node failure.

![189431869.png](/docs-at-surgery-poc/assets/images/uuid-a9b600c5-3c2b-45b6-2e02-1c3324c00722.png)

### Cloud Active/Active High Availability

When Sonatype Nexus Repository is mission-critical, an active/active high availability deployment pattern can help you maximize uptime and minimize data loss in the event of node or availability zone failure.

![189431871.png](/docs-at-surgery-poc/assets/images/uuid-2106362d-2049-8451-88f1-f55bfff31ec0.png)

### Star Pattern

![Star deployment pattern](/docs-at-surgery-poc/assets/images/uuid-623266c8-7f0a-0554-f920-0dbd03cdda4d.png)

Also known as the hub and spoke model" (like a wagon wheel), the star deployment pattern uses a single central server from which additional servers pull components. Using a star deployment pattern helps conserve bandwidth while making components available across geographical regions. The example star pattern above has only two points, but you can expand this pattern to as many points as you need.

In a star pattern, you have a primary region ("Region A" in the example above) with a primary Sonatype Nexus Repository instance (node). This is where all writes happen.

Developers in another region ("Region B" in the example above) may need access to the components in region A. Whether they are pulling things into their IDEs or pulling containers, you save bandwidth between regions A and B by setting up a cache. Do this by standing up a Sonatype Nexus Repository instance that is primarily focused on proxying the node in region A.

You might also have non-human consumers such as highly secured production deployments that need to pull directly from a local cache as shown in the section called "Region C" in the example above.

The star pattern provides great content availability and access speed while saving bandwidth.

### Federated Repositories

![Federated repositories pattern](/docs-at-surgery-poc/assets/images/uuid-f960ac92-92ca-e073-6315-563b44d79814.png)

The federated repositories pattern builds off of the Bi-Directional Proxying pattern. As with bi-directional proxying, the geographically separated teams may only share portions of what they create (e.g., perhaps they don't share their Maven components but only the finished wars/Docker containers).

The example above comprises three separate teams in three separate regions. There is bi-directional proxying between regions A and B; regions A and C; and regions B and C. To zoom in and see what bi-directional proxying looks like between each of these regions, see the Bi-Directional Proxying pattern.

This pattern allows for teams in different regions to proxy content from another region on-demand.

### Scaling with Proxies

![Scaling with proxies](/docs-at-surgery-poc/assets/images/uuid-a7f39585-3e43-680c-87c0-d6f28736377b.png)

Much of the load that Sonatype Nexus Repository must bear comes from reads rather than writes. Scaling with proxy nodes allows you to take read load off of a primary Sonatype Nexus Repository instance (node) by using proxy nodes with a load balancer to split read traffic.

The proxy nodes are identical to the primary node and don't need to share any state. However, if you make a repository on your primary node, you will need to make a corresponding proxy in the proxy layer.

### Scaling with Proxy Nodes

Operating a mission-critical Nexus Repository deployment may mean serving a significant read load. In these cases, we recommend directing read-only traffic to a proxy node and offloading requests from the primary server. This topic covers a common scalability pattern that relies on proxy repositories.

### Bi-Directional Proxying

![174719255.png](/docs-at-surgery-poc/assets/images/uuid-b8c62d9a-0426-b187-fbf8-61663d37f3cc.png)

Bi-directional proxying allows teams in separate regions to share components.

In the example above, there are two teams in two different regions; each team also has their own build/CI server. They may be sharing only a portion of what they create, but they accomplish this sharing by each publishing to a hosted repository in their own region. A proxy repository in the other region then pulls the components from the hosted repository, making them accessible to the other team.

To make reads simple, they group together the hosted and proxy repositories in each of their regions. This way, they have on-demand access to both components written to the hosted repository in their own region as well as those pulled from the other region by their proxy repository.

### Content Replication Pattern

Content Replication is a Sonatype Nexus Repository Pro feature that allows you to publish artifacts in one Sonatype Nexus Repository instance and then have another instance pre-emptively fetch via HTTP to provide faster artifact availability across distributed teams. This is different from (and faster than) Federated Repositories or Bi-Directional Proxying where a proxy repository must fetch content on demand.

![174719259.png](/docs-at-surgery-poc/assets/images/uuid-4c1ab6f5-065d-19a9-ea44-eb2e803d93e4.png)

### Combination Active/Active High Availability + Disaster Recovery Site

While our active/active high availability (HA) patterns protect against node or availability zone outages, combining this pattern with a disaster recovery (DR) site can also help protect against a regional outage.

![189431879.png](/docs-at-surgery-poc/assets/images/uuid-845c679f-437a-9557-3490-31a37af9dd3a.png)

In this pattern, an active/active HA cluster handles the primary load in the primary data center or spreads across AZs in one region.

Then, at a DR site with a second data center or in a second region, you stand by ready to set up another active/active HA cluster in the event of a regional outage.

### Combination Active/Active High Availability + Disaster Recovery Site + Federated Repositories

If you have resiliency, scalability, and distribution needs, you can combine multiple patterns together such as in this combination of disaster recovery (DR), active/active high availability (HA), and federated repository pattern.

![189431881.png](/docs-at-surgery-poc/assets/images/uuid-932ef026-b05d-f146-01bf-bf09e31af0c5.png)

In this pattern, a primary site (called "Region A" in this example) has an active/active HA setup that is federated to Region B. Each region also has a passive DR site set up in case the primary site in that region goes down.

## Resiliency

Resiliency is the ability to recover from disruptions to critical processes and supporting technology systems. This includes anything from hardware or software issues to network outages or data center failures. A resilient Nexus Repository implementation is designed to minimize downtime.

This involves redundancy, failover mechanisms, and robust data management strategies to protect against data loss and service interruptions.

Choosing the appropriate resiliency options is your primary goal when designing your Nexus Repository architecture.

See the Migrating to a Resilient Deployment documentation for details.

### Resiliency Terminology

Understanding the specific terminology used is crucial for understanding the guidance recommended in this section. Here's a breakdown of the key terms:

- A node represents a single, running instance of the Nexus Repository application. It encompasses the software, resources (CPU, memory, storage), and configuration necessary for the repository to function. A standalone deployment consists of a single node, while clustered deployments involve multiple nodes. We generally recommend that each node reside on a physical server to limit the risk of hardware failure.
- A system of record is the authoritative Nexus Repository instance for a given artifact.
- A cluster is a group of interconnected nodes working together to provide high availability and scalability for Nexus Repository. Clustering allows for distributing the workload, providing redundancy, and ensuring continued operation even if some nodes fail. The nodes in the cluster connect to a shared external database and write to the same blob stores.
- HA refers to the system's ability to remain operational and accessible with minimal downtime. In Nexus Repository, HA is typically achieved through clustering, where multiple nodes can take over if one node becomes unavailable.
- Failover is the automatic process of switching to a redundant or backup node in the event of a primary node's failure. This ensures continuous service availability.
- Replication involves copying data from one node to another. In Nexus Repository, replication can be used to synchronize data across multiple nodes in a cluster, ensuring data consistency and enabling failover.
- Load balancing distributes incoming requests across multiple nodes in a cluster. This helps to prevent any single node from becoming overloaded and improves overall performance.
- Data consistency ensures that all nodes in a cluster have the same, up-to-date data. This is crucial for maintaining data integrity and preventing conflicts.
- DR refers to the process of restoring the Nexus Repository system and its data after a major outage or disaster. This typically involves backups, failover to a geographically separate location, and a recovery plan.
- Backup and restore procedures are essential for protecting Nexus Repository data. Regular backups allow you to recover from data loss or system failures. Backups should include documenting the service environment and the system configuration, as well as the application binaries, blob stores, and database. You may want different schedules or priorities depending on the frequency of deployments and audit requirements.
- The amount of data loss that is acceptable when a restore becomes necessary. Measured in the amount of time since that last backup.
- The length of time required to restore the service. This may includes a least a partial recovery, the service in at least read only state, or one that restores the service to the RPO.
- Monitoring of Nexus Repository nodes and the cluster as a whole is crucial for detecting potential issues and ensuring system health. Monitoring tools can track metrics like CPU usage, memory consumption, and network activity.

### Recommendations for Resiliency

Resiliency involves balancing three outcomes; the costs of your maintenance plan, with the time needed to recover, against the risks of disruptions to the service. The following best practices are tools for improving the resiliency of your Nexus Repository.

- Implement a robust backup strategy that includes regular, automated backups of the Nexus Repository data, configuration, and application files. Store backups securely, preferably in a separate location such as a data center in another region.
- Deploy Nexus Repository in a clustered configuration to ensure high availability and automatic failover in case of node failures.
- Implement comprehensive monitoring of Nexus Repository nodes, the cluster (if applicable), the database, and the underlying infrastructure. Monitor key metrics such as CPU usage, memory consumption, disk space, network activity, and application logs. Set up alerts for critical events.
- Develop and regularly test a disaster recovery plan that outlines the steps to restore Nexus Repository in the event of a major outage or disaster. This plan should include procedures for backup restoration, failover to a secondary location, and communication with stakeholders.
- Implement security best practices to protect Nexus Repository from security breaches. This includes strong password policies, least privilege access controls, updating to the latest versions, and vulnerability scanning.
- Regularly test failover and recovery procedures to ensure they work as expected. This includes simulating node failures, database failures, and network outages. Test the backup and restore process to verify its effectiveness.

### Failure Scenarios and Recovery

This section provides a breakdown of potential failure scenarios for Nexus Repository in both single-node and clustered environments. The scope of interruption you need to mitigate balanced with the cost of ownership for those deployments determines which architecture is needed to achieve your required level of resiliency.

### Library of Patterns

The sections below list various patterns to use depending on your resiliency requirements.

### Single-Node Cloud Resilient Deployment Using AWS

**Note:** A Helm Chart ( [GitHub](https://github.com/sonatype/nxrm3-ha-repository/tree/main/nxrm-ha) , [ArtifactHub](https://artifacthub.io/packages/helm/sonatype/nxrm-ha) ) is available for our resiliency and high-availability deployment options. Be sure to read the deployment instructions in the [associated README file](https://github.com/sonatype/nxrm3-ha-repository/blob/main/nxrm-ha/README.md) before using the chart.

This section provides instructions for setting up Nexus Repository in Amazon Web Services (AWS) aligned to the following deployment model.

![NXRM_AWS_Resiliency.png](/docs-at-surgery-poc/assets/images/uuid-d976f7c8-1179-e2af-9e69-b9a0a2b4b363.png)

### Single-Node Cloud Resilient Deployment Using Azure

**Note:** A Helm Chart ( [GitHub](https://github.com/sonatype/nxrm3-ha-repository/tree/main/nxrm-ha) , [ArtifactHub](https://artifacthub.io/packages/helm/sonatype/nxrm-ha) ) is available for our resiliency and high-availability deployment options. Be sure to read the deployment instructions in the [associated README file](https://github.com/sonatype/nxrm3-ha-repository/blob/main/nxrm-ha/README.md) before using the chart.

You never know when disaster may strike. With a resilient deployment on Azure like the one outlined below, you can ensure that you still have access to Nexus Repository in the event of a service or data center outage.

If you already have a Nexus Repository instance and want to migrate to a resilient architecture, see our migration documentation.

![NXRM_Azure_Resiliency.png](/docs-at-surgery-poc/assets/images/uuid-9aea9d36-2628-1812-5fd1-e055a34a5476.png)

### Single-Node Cloud Resilient Deployment Example Using Google Cloud

**Note:** A Helm Chart ( [GitHub](https://github.com/sonatype/nxrm3-ha-repository/tree/main/nxrm-ha) , [ArtifactHub](https://artifacthub.io/packages/helm/sonatype/nxrm-ha) ) is available for our resiliency and high-availability deployment options. Be sure to read the deployment instructions in the [associated README file](https://github.com/sonatype/nxrm3-ha-repository/blob/main/nxrm-ha/README.md) before using the chart.

Ensure continuous delivery even in the face of disruptions. The steps below detail how to create a resilient Nexus Repository deployment on Google Cloud, leveraging Google Kubernetes Engine (GKE) and persistent storage to keep your artifacts available through outages.

If you already have a Nexus Repository instance and want to migrate to a resilient architecture, see our migration documentation.

![Resilient_GCP_NXRM.png](/docs-at-surgery-poc/assets/images/uuid-1d6bdfb1-f12d-4942-d1d5-a17ea374c26a.png)

### Single Data Center On-Premises Resilient Deployment Example Using Kubernetes

This architecture illustrates how to use a Kubernetes cluster and PostgreSQL database to create a resilient Nexus Repository deployment. In this reference architecture, a maximum of one Nexus Repository instance is running at a time. Having more than one Nexus Repository instance replica does not work.

This model is designed to protect against the following scenarios:

- A node/server failure within a data center
- A Nexus Repository service failure

Use this architecture to fit the following profiles:

- Desire to minimize downtime by automatically failing over to a backup node in case of a failure.
- Experience with Kubernetes as part of other in-house applications.
- Nexus Repository is configured with an external PostgreSQL database.
- High Availability (HA) in active-active mode is not required.
- This model is compatible with the Community Edition. The included Helm chart are only available for Pro deployments, however they may be manually adjusted for CE deployments.

![Nexus_Repository_Resiliency_-_On_-premises_Resiliency_deployment.png](/docs-at-surgery-poc/assets/images/uuid-f455835c-87c0-6cc0-7dfa-7c81ee020bca.png)

## High Availability Deployment

**Note:** Only available in Sonatype Nexus Repository TM Pro. Interested in a free trial? [Start here](https://www.sonatype.com/products/repository-pro/trial) .

High availability (HA) refers to a system's ability to operate continuously with minimum downtime. It's about ensuring that critical systems and applications are accessible and reliable, even in the face of unexpected events or failures.

### Overview

Nexus Repository accomplishes HA by deploying a cluster of redundant instances, or nodes, running simultaneously within a single data center. This model improves uptime as at least one node of Nexus Repository is available to receive requests in the event of other instances are unavailable.

See the Requirements for High Availability documentation

- The Nexus Repository nodes are behind an application load balancer that monitors the availability of the nodes and distributes requests to available instances.
- The instances connect to a shared external database on separate hardware and managed independently from Nexus Repository.
- Components are stored in shared blob stores located on network storage or object-based storage. Each instance requires low-latency access to the shared storage.
- Each Nexus Repository instance should run on separate hardware to avoid losing multiple nodes due to a single point of failure. A minimum of two nodes are required for HA deployments. Additional nodes provide extra redundancy to handle more capacity to allow for scaling of the cluster. Keep in mind that the network's bandwidth and the database's hardware are the limiting factors as you scale up the number of nodes in a cluster.

![Nexus Repository HA Architecture Overview with Clients, REST, and UI leading into an application load balancer that feeds two Nexus Repository instances. These use an external database and shared blob storage.](/docs-at-surgery-poc/assets/images/uuid-a04719b1-2c21-d8aa-a4be-7de7597561ee.png)

### Related Topics

- Follow the steps outlined in Installing Sonatype Nexus Repository Using the OpenShift Operator.
- Detailed instructions for migration are captured in the Migrating to an HA Deployment from a Legacy HA-C or a Resilient Deployment documentation. Migrating to an HA Deployment from a Legacy HA-C or a Resilient Deployment
- Nexus Repository 3.71.0 supports zero downtime upgrades. For details, see our help topic on upgrading Nexus Repository using rolling upgrades.
- As of Nexus Repository 3.68.0, the Helm chart uses a shared logging location.
- Detailed instructions for downgrading are captured in the High Availability Deployment to a single instance documentation.
- See the Content Selectors documentation for the differences in how content selectors work in HA deployments.
- Enabling HA removes the default blob stores on new instances. Follow the instructions in the Migrating to Shared Blob Storage documentation to change your default blob stores to a shared location.

### Nexus Repository vs. IQ Server High Availability

Sonatype offers high availability (HA) deployment options for both its Nexus Repository and IQ Server products. The table below details the notable differences in the high availability requirements.

See the IQ Server HA help documentation

### Manual High Availability Deployment

**Note:** Only available in Sonatype Nexus Repository TM Pro. Interested in a free trial? [Start here](https://www.sonatype.com/products/repository-pro/trial) .

⚠️ **Warning:** Nexus Repository High Availability deployments should be fully deployed and tested in a development environment before being attempted in production. Improper deployment in a production environment may result in critical data loss.

### On-Premises High Availability Using Kubernetes

**Note:** Only available in Sonatype Nexus Repository TM Pro. Interested in a free trial? [Start here](https://www.sonatype.com/products/repository-pro/trial) .

⚠️ **Warning:** Sonatype Nexus Repository High Availability deployments should be fully deployed and tested in a development environment before attempting to deploy in production. Improper deployment in a production environment can result in critical data loss.

This example architecture illustrates how to use a Kubernetes cluster and PostgreSQL database to create a highly available Nexus Repository deployment.

![Nexus_Repository_Resiliency_-_On_-premises_HA_deployment.png](/docs-at-surgery-poc/assets/images/uuid-4d747f6f-20fd-9d23-e097-84c532d56f7b.png)

### High Availability in Amazon Web Services

![nx_architecture_ha_aws](/docs-at-surgery-poc/assets/images/uuid-6f5b9667-9994-f94f-ce54-6b0918e82b1c.png)

High Availability should be deployed and tested in a development environment before deploying to production. This reference architecture is designed to protect against the following scenarios:

- An AWS Availability Zone (AZ) outage within a single AWS region
- A node/server (i.e., EC2) failure
- A Nexus Repository service failure

Use this architecture for the following use cases:

- Nexus Repository Pro user looking for a deployment option to reduce downtime.
- Require automatic failover and fault tolerance in your deployment requirement.
- An Elastic Kubernetes Service (EKS) cluster is in your deployment pipeline.
- Nexus Repository is using an external PostgreSQL database.

### Option 4 - High Availability Deployment in Azure

**Note:** Only available in Sonatype Nexus Repository TM Pro. Interested in a free trial? [Start here](https://www.sonatype.com/products/repository-pro/trial) .

⚠️ **Warning:** Sonatype Nexus Repository High Availability deployments should be fully deployed and tested in a development environment before attempting to deploy in production. Improper deployment in a production environment can result in critical data loss.

The reference architecture and steps below provide detailed information on setting up a highly available Nexus Repository deployment in Azure.

![NXRM_Azure_HA.png](/docs-at-surgery-poc/assets/images/uuid-38046518-9792-38fe-d090-4127fff91d68.png)

### Option 5 - High Availability Deployment in Google Cloud

**Note:** Only available in Sonatype Nexus Repository TM Pro. Interested in a free trial? [Start here](https://www.sonatype.com/products/repository-pro/trial) .

**Note:** A Helm Chart ( [GitHub](https://github.com/sonatype/nxrm3-ha-repository/tree/main/nxrm-ha) , [ArtifactHub](https://artifacthub.io/packages/helm/sonatype/nxrm-ha) ) is available for our resiliency and high-availability deployment options. Be sure to read the deployment instructions in the [associated README file](https://github.com/sonatype/nxrm3-ha-repository/blob/main/nxrm-ha/README.md) before using the chart.

⚠️ **Warning:** Sonatype Nexus Repository High Availability deployments should be fully deployed and tested in a development environment before attempting to deploy in production. Improper deployment in a production environment can result in critical data loss.

The reference architecture and steps below provide detailed information on setting up a highly available Nexus Repository deployment in Google Cloud Platform (GCP).

![HA_GCP_NXRM.png](/docs-at-surgery-poc/assets/images/uuid-d32a54bd-4f5a-6af9-1f1f-5e14d2d1f423.png)

### Post-Deployment Steps for HA

**Note:** Only available in Sonatype Nexus Repository TM Pro. Interested in a free trial? [Start here](https://www.sonatype.com/products/repository-pro/trial) .

After you have completed your high availability (HA) deployment, there are a few steps you must take before you can fully use Sonatype Nexus Repository in its new HA environment.

### Validating Your HA Deployment

**Note:** Only available in Sonatype Nexus Repository TM Pro. Interested in a free trial? [Start here](https://www.sonatype.com/products/repository-pro/trial) .

Nexus Repository has a couple of ways for you to see detailed information about your deployed nodes and verify your deployment.

### Migrate Nexus Repository Clustered Deployments to Use External Secrets Operator

As of release 3.74.0, highly available deployments may use an external secrets operator. Follow these steps to migrate to an external secrets operator:

## Nexus Repository Database

Nexus Repository has two databases available. Use the following table to choose a database for your deployment.

- See the configure PostgreSQL documentation for new instances
- See the migrating to a PostgreSQL documentation for existing instances

### Legacy Orient Database

Nexus Repository's legacy embedded OrientDB database is in extended maintenance as of August 2024. Nexus Repository deployments must migrate off of OrientDB.

You must remain on the 3.70.x version line if you are unable to migrate at this time.

## Storage Guide

Nexus Repository uses a *binary large object (blob)* storage, or **blob store** , to store files found in a repository. This includes metadata, hashes, and repository-generated indexes. When adding to a repository, Nexus Repository renames and obfuscates the contents to avoid naming collisions and file system constraints. Avoid modifying these files outside of the Nexus Repository.

- Repositories are configured to use either a single *blob store* or a *blob store group* . Many repositories may use the same blob store. Blob store groups may use many storage locations and different storage types.
- The first time Nexus Repository launches, the initial repositories are configured to use a file system blob store named `default` in the data directory.
- Blob stores are set to: a folder in the file system, a network storage, or cloud object storage. Configure the location of blob stores with as low latency as possible for optimal performance.
- Having a large number of blob stores impacts the system performance as querying, cleanup, and indexing tasks are specific to a blob store.
- When adding to a repository, Nexus Repository renames and obfuscates the contents to avoid naming collisions and file system constraints. Component metadata is stored in a file along with the component.

Learn about blob store layouts in the Storage Planning documentation

Learn how to manage blob stores from the configuring blob stores documentation

### Storage Terminology

- An object containing data (e.g., component binaries and metadata files) within a blob store.
- An internal storage mechanism for the binary parts of components and their assets.
- When using a group blob store, the fill policy determines to which blob store a blob is written.
- A blob store that delegates operations to one of the other blob stores on its list.
- When a soft-deleted blob is permanently removed from the blob store.
- When a blob store is converted to a virtual grouping of one or more blob stores. Repositories using a group may store components across multiple store locations and types.
- The system labels a file for deletion, but it remains in the blob store. The compact blob store task eventually deletes these files.
- This feature monitors a blob store and raises an alert when the specific metric exceeds the constraint. The system reports the blob store as unhealthy when used beyond its quota limits. However, it still allows writes to the storage with a logged warning.

### Migrating to Shared Blob Storage

**Note:** Only available in Sonatype Nexus Repository TM Pro. Interested in a free trial? [Start here](https://www.sonatype.com/products/repository-pro/trial) .

Blob storage for highly available deployments must be in a shared network location accessible to all nodes in the deployment.

Before moving blob stores to a new location, update the path for the blob store in the Nexus Repository user interface. Nexus Repository requires the new location to be empty when changing an existing blob store location. Put your instance in read only mode during this operation to avoid corrupting the database during the move.

### Storage Planning

Many attributes are immutable once a blob store is created. We recommend you carefully plan your blob store configuration before your initial deployment. While there are ways to change the configuration later, these methods come with a fair amount of rework, increased storage requirements, and potential downtime.

You will need to choose which types to use, how many blob stores to create, and how you allocate repositories to these blob stores. These decisions should be based on the following:

- the size of your repositories
- the storage space available
- the rate at which you expect them to grow over time
- the options you have available for adding storage space

### Using Replicated Blob Stores

Nexus Repository provides a mechanism to override specific blob store attributes using environment variables used during the Nexus Repository startup. Use this mechanism to override the blob store bucket name attribute to point to a replica.

```
NEXUS_BLOB_STORE_OVERRIDE='{blob-store-name": {"s3": {"bucket": "bucket-name"}}}'
```

The `NEXUS_BLOB_STORE_OVERRIDE` environment variable contains a JSON object with the properties to remap your blob store location.

The environment variable only updates the blob store configuration in the Nexus Repository database and does not modify the contents of the blob store. The blob store override environment variable does not copy contents between blob stores. Replicating blob stores is outside the scope of this feature.

You may use the override to modify several blob stores:

```
NEXUS_BLOB_STORE_OVERRIDE='{"blob-store-1": {"s3": {...}}, "blob-store-2": {"s3": {...}}, "blob-store-3": {"s3": {...}}}'
```

You may modify several attributes for each blob store:

```
NEXUS_BLOB_STORE_OVERRIDE='{"nxrm-blob-store": {"s3": {"bucket": "nxrm-bucket-stage", "region": "us-east-2"}}}'
```

The attributes available for override are defined for the blob store configuration in the Nexus Repository database. The most common attributes for each environment are as follows:

## Run Behind a Reverse Proxy

Using a reverse proxy in front of Nexus Repository is a highly recommended and common practice for several compelling reasons, covering security, performance, flexibility, and operational efficiency. This section provides guidance on how to configure a reverse proxy servers to work with Nexus Repository.

Here are some of the key benefits:

- Nexus Repository may be configured with SSL, but offloading this to a reverse proxy like Nginx or Apache is often preferred. The reverse proxy handles the SSL handshake, decrypts incoming requests, and encrypts outgoing responses. Using a reverse proxy to resolve SSL (Secure Sockets Layer) is a common and highly recommended practice, especially in production environments. It's often referred to as SSL/TLS Termination or SSL Offloading. Doing this offloads the CPU-intensive SSL processing from the Nexus Repository so that it's resources are focused on handling other requests. You only need to install and manage SSL certificates on the reverse proxy server, rather than on every individual Nexus Repository instance. This simplifies certificate renewal and the upgrade workflow for your server.
- The reverse proxy acts as a buffer between the public internet and your Nexus Repository instance. It can be placed in a Demilitarized Zone (DMZ), protecting your internal Nexus Repository server from direct exposure to external threats. In the instance where Nexus Repository needs to be proxied at a different base path you must change the default path by editing a property value. See the Base URL Capability documentation
- A reverse proxy allows you to expose Nexus on standard HTTP (80) and HTTPS (443) ports, simplifying access for clients and adhering to network policies. This is useful for Docker repositories, which require specific ports or subdomains for push/pull operations if not proxied. See the Docker Reverse Proxy Strategies documentation
- In a high-availability setup (Nexus Repository Pro), a reverse proxy acts as a load balancer to distribute incoming requests across multiple instances, improving performance and ensuring continuous availability even when one node fails. See the High-Availability Deployments documentation
- When setting up SSO and using a reverse proxy instead of Nexus Repository, you need to forward to the same context path on the reverse proxy and the Nexus Repository instance for SSO host headers to be accepted. See the Configuring the Runtime Environment documentation

### Reverse Proxy on Restricted Ports

Forward requests from port `80` to the default Nexus Repository port `8081` .

### Reverse Proxy Virtual Host and Custom Context Path

Accept requests from a custom subdomain ( `repo` ) and the application context path ( `/nexus` ).

### Reverse Proxy SSL Termination at Base Path

Accept HTTPS requests on the standard port `443` and serve content using the default non-restricted HTTP port `8081` .

To test your configuration, review the steps to [generate a self-signed SSL certificate](https://support.sonatype.com/hc/en-us/articles/213465768-SSL-Certificate-Guide) for reverse proxy servers.

### Apache httpd with npm Repositories

Npm [scoped packages](https://docs.npmjs.com/misc/scope) use encoded slash characters ("/") in their URL's. By default, Apache does not allow encoded slashes to pass through. When using npm and Apache reverse proxy add the following to your configuration to allow encoded slashes through:

```
AllowEncodedSlashes NoDecode
```

The ProxyPass directive needs the nocanon option:

```
ProxyPass / http://localhost:8081/ nocanon
```

## Securing Nexus Repository

Below are suggestions for making your Nexus Repository instance more secure.

### Limit IPs that can be reached from your Nexus Repository Host

Nexus Repository can be configured by an administrator to contact internal and external IPs for various reasons such as retrieving certificates, creating proxy repositories, dispatching events to remote URLs, and so on. You may limit the IPs that can be reached from the host machine running your Nexus Repository instance but note that doing so could block the main use case for some features.

For example, webhooks give administrators a way of integrating Nexus Repository with other systems (e.g. an auditing system, another Nexus Repository instance, or a lightweight listener potentially on the same host), typically in the same data center. Hence, limiting webhook destinations to, for example, IPs external to your data center effectively blocks the main use case for them.

### Privileges and Service Account

- Only assign the least necessary privileges to Nexus Repository users.
- Create a dedicated operating system service account for running Nexus Repository - do not run as the root user. In addition, the service account must have read/write permissions to the `$install-dir` and sonatype-work directories and must be able to create a valid shell. See our System Requirements for detailed operating system service account recommendations.

### Containerization

Running Nexus Repository in a Docker container may reduce the impact of a successful attack. Without containerisation, if a malicious person successfully exploits a service and gains root access, they could do damage to other services running on the host. On the other hand, containerising means a successful attack on that service is restricted to the container running that service.

The Nexus Repository 3 docker images are found at: [https://hub.docker.com/r/sonatype/nexus3/](https://hub.docker.com/r/sonatype/nexus3/) .

## Keeping Disk Usage Low

Generally, we recommend using Cleanup Policies and the *Admin - Compact blob store* task to keep disk usage low. However, this page details several other items for when policies are not enough.

### Tasks

If Cleanup Policies are not meeting your needs, you may need to use the existing tasks. See the FAQ of Cleanup Policies for more about what Cleanup Policies cover and what needs Tasks used instead.

**Note:** These tasks only soft delete components while the *Admin - Compact blob store* task is needed to free up disk space.

### For More Complex Cleanup Scenarios

For scenarios where the policies and tasks don't cover their provided variables, use the REST API to find and delete what you need via a REST call.

For example, if you'd like to delete all components named `alpha` , you can perform the following curl to identify them:

```
curl -X GET "http://localhost:8081/service/rest/v1/search?name=alpha" -H "accept: application/json"
```

Depending on your results, you can then call individual deletes or design a script to remove them all. Example of what a delete curl might look like:

```
curl -X DELETE "http://localhost:8081/service/rest/v1/components/bWF2ZW4tcmVsZWFzZXM6ODg0OTFjZDFkMTg1ZGQxMzgwYjA3YWQzNDAwOGVmNTc" -H "accept: application/json"
```

### Examining Blobstore Space Usage

If you would like more insight into how blobstore space is being consumed to make better-informed configuration decisions, you can run Groovy scripts either from the command line or from within NXRM using the *Execute Script* task.

This [Knowledge Base article](https://support.sonatype.com/hc/en-us/articles/115009519847-Investigating-Blobstore-Space-Usage) provides samples to get you started.

### Totally Out of Space / Seeing Errors?

If you are currently out of disk space, there are a couple of other Knowledge Base articles you can look at to free up space urgently and get the system up and running:

[What to Do When the Database is Out of Disk Space](https://support.sonatype.com/hc/en-us/articles/360000052388)

[What to Do When the Blob Store is Out of Disk Space](https://support.sonatype.com/hc/en-us/articles/360000096228)

## Backup and Restore

For H2 databases, Nexus Repository provides tasks to create database snapshots and relocate them to a target disk. Other directories in your local instance (or instances) should also be copied and rebuilt on a backup disk (see the Prepare a Backup documentation ).

Along with your backup procedure, you can configure Nexus Repository to save the H2 database that stores your component metadata and system configurations.

You can configure this task to export settings and metadata from the underlying H2 database. The scheduled task does the following:

- Stores the databases to a new location when configured
- Generates a snapshot of the databases for you to back up
- Suspends access to the database until the backup is complete
- Cancel any currently running scheduled tasks

This section shows you how to configure and execute the tasks as well as how to recover the exported database of your Nexus Repository.

See the Backup and Restore in Amazon Web Services documentation for further information.

### Configure the Backup Task

Scheduled tasks are available to back up the embedded databases (H2 or OrientDB).

### Prepare a Backup

Nexus Repository stores data in blob stores and keeps some metadata and configuration information separately in databases. You must back up the blob stores and metadata databases together. Your backup strategy should involve backing up both your databases and blob stores together to a new location in order to keep the data intact.

Complete the steps below to perform a backup:

### Restore Database

This topic covers steps for restoring an OrientDB or H2 database that you previously exported using a Nexus Repository task. Note that you will also need to restore your blob stores containing components as part of this process.

### Backup and Restore in Amazon Web Services

This section covers recovery from backup in Amazon Web Services (AWS). While the details here are specific to AWS, a similarly effective deployment model is likely possible with other cloud vendors. As a best practice, you should also examine current AWS documentation before implementing your deployment to validate that AWS services have not changed in a way that will impact your needs and estimate deployment costs.

## Quick Start Guide - Proxying Maven and NPM

If you're new to Nexus Repository 3, use this guide to get familiar with configuring the application as a dedicated proxy server for Maven and npm builds.

To reach that goal, follow each section to:

- Install Nexus Repository 3
- Run the server locally for testing Production deployments should follow the Planning your Implementation documentation
- Production deployments should follow the Planning your Implementation documentation
- Proxy a basic Maven and npm build

When you complete the steps, the components will be cached locally to your server. After meeting the requirements, it will take approximately 15 minutes to proxy Maven and npm with the code snippets below.

### Requirements

Before you can set up the proxy server for Maven and npm, you'll need to install and configure the following external tools for the repository manager:

- A Java Development Kit (JDK) in a supported version as detailed in the table below - Nexus Repository 3 is a Java server application
- Supported for all currently released versions
- Required for versions up to and including 3.66.0
- 3.67.0 and above
- 3.69.0 and above
- Not supported in OrientDB environments
- [Apache Maven](https://maven.apache.org/download.cgi) - Nexus Repository 3 includes a proxy configured to [Central Repository](https://search.maven.org/) when you first start up. For the maven client to use Nexus Repository to request dependencies, you will want to define this proxy repository in both your `settings.xml` file and the Project Object Model file (POM).
- For the maven client to use Nexus Repository to request dependencies, you will want to define this proxy repository in both your `settings.xml` file and the Project Object Model file (POM).
- [npm](https://www.npmjs.com/get-npm) - A popular repository for javascript components. Nexus Repository 3 doesn’t ship configured wiith a proxy to the npm repository. You will first need to add this proxy repository to Nexus Repository. Then [configure your npm client](https://docs.npmjs.com/cli/v8/using-npm/registry) to access the newly created proxy by updating the `.npmrc` configuration file as shown below.
- Nexus Repository 3 doesn’t ship configured wiith a proxy to the npm repository. You will first need to add this proxy repository to Nexus Repository. Then [configure your npm client](https://docs.npmjs.com/cli/v8/using-npm/registry) to access the newly created proxy by updating the `.npmrc` configuration file as shown below.
- You will first need to add this proxy repository to Nexus Repository.
- Then [configure your npm client](https://docs.npmjs.com/cli/v8/using-npm/registry) to access the newly created proxy by updating the `.npmrc` configuration file as shown below.

### Part 1 - Installing and Starting Nexus Repository Manager 3

### Part 2 - Proxying Maven and npm Components

When you proxy components the repository manager acts as a local intermediary server for any download requests going to remote repositories / registries. After logging in, these next steps will show you how to configure then test your configuration with local builds for a Maven and npm project.

### Part 3 - Viewing Proxied Components

After your Maven and npm projects are successfully built, follow these steps to view the cached components:

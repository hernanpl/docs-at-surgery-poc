---
layout: default
title: "IQ Server Reference Architecture"
parent: Sonatype IQ Server
nav_order: 5
---

# IQ Server Reference Architecture

Sonatype IQ Server is designed to handle varying volumes of application workloads. The stability and performance of your IQ Server installation depends upon:

- Deployment instance (type of AWS instance)
- Primary usage patterns (no. of scans per second)
- Scale of the deployment (application/user counts)

A general recommendation for IQ Server system requirements can be found [here](#UUID-8f9362cc-c8ef-de1b-ccf2-e7a7d24885f0) .

Based on the performance tests for varying amounts of operating workloads in real time environments, we have defined a set of hardware system recommendations, for different volumes and scale of the application workloads. These recommendations are designed to extract maximum ROI from your system resources that are provisioned for your IQ Server deployment.

## Sizing your IQ Server Requirement

You can determine the size of your IQ Server deployment based on the table below:

For High Availability Reference Architecture for IQ Server , refer to [IQ Server High Availability Installation](#UUID-12c3ef20-4a59-f13b-8c71-d93cf59c54c0) .

## Small Size Deployments

**What is a Small Size Deployment?**

**Available Options**

There are 2 options available to install Sonatype IQ Server:

- Internal database
- External database

**1. Recommendations for Sonatype IQ Server with internal database**

Reference Architecture Diagram:

![SIQ_Single_Instance_H2.png](/assets/images/uuid-df47322b-0dfb-7bf3-35f3-8cb33572057e.png)

**2. Recommendations for Sonatype IQ Server with external database**

Reference Architecture Diagram:

![SIQ_Single_Instance_Postgres_port.png](/assets/images/uuid-0d10fab9-c052-b6dc-28dd-2e82c48329c1.png)

**Recommendations for Container Environments**

Sonatype IQ Server with internal database is not compatible with container lifecycles. This could lead to hard to fix database corruption issues. We do not recommend deploying IQ Server with internal database in a container environment.

## Medium Sized Deployments

**What is a Medium Size Deployment?**

**Available Options**

There are 2 options available to install Sonatype IQ Server:

- External database
- Active/Passive deployment for resiliency

**1. Recommendations for Sonatype IQ Server with external database**

**Reference Architecture Diagram:**

![SIQ_Medium_size_Postgres_port.png](/assets/images/uuid-36823f53-a667-f75e-9642-020f16830d68.png)

**2. Recommendations for Sonatype IQ Server active-passive deployment**

To ensure uptime and minimize or prevent data loss in the event of unprecedented failures, you can deploy Sonatype IQ Server in an active-passive configuration, with a load balancer.

Active-passive architecture clones a single instance (primary instance) and places one or more independent instances behind a load balancer. If the load balancer detects that the primary instance is unavailable, incoming requests are redirected to the failover or standby instances (other independent instances.)

**Reference Architecture Diagram:**

![SIQ_Active_Passive_Medium_port.png](/assets/images/uuid-0e0e8050-d95c-1092-88e0-24241ee203c0.png)

For active-passive deployment using internal database, data will have to be replicated between the active and passive instance of the IQ Server.

The following assets need to be replicated:

- config.yml
- nexus-iq-server<version>.jar
- ‘/sonatype-work’ directory

## Large Sized Deployments

**What is a Large Size Deployment?**

**Recommendations**

**Reference Architecture Diagram:**

![IQ_Large_nonHA_Deployment_port.png](/assets/images/uuid-4c4386bc-21b6-4139-4859-6f02148c4873.png)

**High Availability active-active Deployment**

High Availability (HA) configurations for Sonatype IQ Server are designed to protect against individual components failure and causing system downtime. Examples of failures include:

- AWS Availability Zone (AZ) outage (within a single AWS region)
- Node/server (EC2) failures
- IQ Service/database failures

Refer to [Recommendations and Reference Architecture for Sonatype IQ HA](#UUID-12c3ef20-4a59-f13b-8c71-d93cf59c54c0) for more information.

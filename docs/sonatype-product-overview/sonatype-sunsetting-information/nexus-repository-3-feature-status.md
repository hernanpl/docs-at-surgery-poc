---
layout: default
title: "Nexus Repository 3 Feature Status"
parent: Sonatype Sunsetting Information
nav_order: 2
---

# Nexus Repository 3 Feature Status

**Note:** The Sonatype Product Development Lifecycle (PDLC), including definitions of each stage, is fully defined in [Sonatype Sunsetting Information](#UUID-217b96ec-8a06-93ff-b373-ab40751a5647) . For more information about Sonatype Support services, please see [Sonatype's Software Support Policy](https://www.sonatype.com/usage/software-support-policy) For more information about Sonatype Support services, please see [Sonatype's Software Support Policy](https://www.sonatype.com/usage/software-support-policy) .

The Sonatype PDLC is designed to keep us continually improving our products and to ensure that our customers have access to our best features and functionality. This also helps us provide quality support services for our features and products. To this end, Sonatype will sunset and remove some Sonatype Nexus Repository features as they become obsolete.

## Log4J Visualizer

- **Status** : Sunsetted (March 3, 2025), **Released** : November 24, 2021(3.37.0) In Nexus 3.78.0 the Log4J Visualizer has been removed. Log4j Visualizer was an early experiment in adding SCA features to the Nexus Repository. This has been superseded by other motions such as malware warnings.

## Bower Format

- **Status** : Sunsetted (March 3, 2025), **Released** : March 10, 2016 (3.0.0) In Nexus 3.71.0 the Bower format has been removed. Bower has no longer been a supported ecosystem by the community since 2017. This format was only supported in OrientDB instances and was not ported to support PostgreSQL or H2 database.

## OSGi Bundle Capability

- **Status** : Sunsetted (March 3, 2025), **Released** : March 10, 2016 (3.0.0) In Nexus 3.78.0 the OSGi bundle capability has been removed. Any customers using bundles when upgrading to this version will find that those bundles are not loaded.

## OrientDB

- **Extended Maintenance** : (August 6, 2024), **Sunsetting** : January 9 2026, **Released** : March 10, 2016 (3.0.0) Sonatype is invested in continually improving our solutions to take advantage of newer, more advanced technologies. As such, we are strategically moving away from legacy technologies like OrientDB and investing in supporting newer database options like PostgreSQL. Moreover, Sonatype has observed data integrity problems in some deployments using OrientDB. Migrate to a supported database. See [Migrating to a New Database](#UUID-a3ea5445-b958-e8a6-d3e7-b2d3086c58a3) .

## Java 8

- **Status** : Extended Maintenance (August 6, 2024), **Released** : February 11, 2015 Java 8 has reached the end of its life and is no longer receiving public updates. Upgrade to release 3.70.0+ using Java 17. See [Upgrade Nexus Repository Java Version](#UUID-1c91200a-32b7-90c6-0e8b-3dde385edaf5) .

## Java 11

- **Status** : Extended Maintenance (August 6, 2024), **Released** : April 2, 2024 OpenJDK 11 reaches the end of life in October 2024. While Java 11 is a long-term support version, Sonatype is investing its efforts in supporting newer Java versions. Upgrade to release 3.70.0+ using Java 17. See [Upgrading Nexus Repository Java Version](#UUID-1c91200a-32b7-90c6-0e8b-3dde385edaf5) .

## High Availability Clustering (HA-C)

- **Status** : Sunsetted (April 17, 2024), **Released** : February 2017 (3.3.0), **Maintenance** : October 17, 2023 We released the updated version of [High Availability](#UUID-906849d2-3b89-01cd-0a5b-9afd13e9ceac) in Q1 2023 with release 3.50.0. This new offering offers far superior functionality, quality, and scale. Customers currently using HA-C should upgrade to the updated HA deployment model. See [Migrating to an HA Deployment from HA-C](/document/preview/116674#UUID-602e0a4a-d0c8-4751-2f92-8e60514dd4b6) . Migrating to an HA Deployment from a Legacy HA-C or a Resilient Deployment

## Replication v1

- **Status** : Sunsetted (December 15, 2023), **Released** : September 1, 2021 (3.34.0), **Maintenance** : August 3, 2023 In 3.34.0, we introduced our first replication feature (Replication v1), which used a manually run replicator tool to copy binaries from one blob store to another. In 3.48.0, we introduced [Content Replication](#UUID-cbf916ff-6f29-b5b5-770e-0eb3fc21647e) as a much more user-friendly, lightweight feature to replace Replication v1. We also announced at that time that we would eventually remove Replication v1. The newer Content Replication feature is far simpler and includes more automation; it also has fewer system requirements and supports more formats. Customers needing a way to make artifacts readily available across distributed teams should use the newer Content Replication feature. As Content Replication is an entirely different and separate feature from Replication v1, there is no direct migration path. See [Content Replication](#UUID-cbf916ff-6f29-b5b5-770e-0eb3fc21647e)

## Red Hat OpenShift Operator and Container

- **Status** : Sunsetted (December 15, 2023), **Released** : June 2020 (3.24.0), **Maintenance** : August 3, 2023 Sonatype does not recommend using this operator because there are risks of data corruption when running the embedded databases inside a container. In October 2023, Sonatype published a new OpenShift Operator. The new operator uses an external PostgreSQL database and supports high-availability deployment options. See [Installing Sonatype Nexus Repository Using the OpenShift Operator](#UUID-a73c1c08-94b7-2eba-203f-ec9c5e764cc8) .

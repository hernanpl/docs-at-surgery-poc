---
layout: default
title: "IQ Server System Requirements"
parent: Sonatype IQ Server
nav_order: 3
---

# IQ Server System Requirements

The IQ Server should be deployed on dedicated hardware where the specific requirements depend on the deployment architecture, the primary usage patterns, and the scale of deployment. The following guidelines may differ from your requirements.

Development, test, or evaluation deployments can be scaled smaller than these recommendations and will continue to function, though performance degradation may be observed.

Sonatype offers a managed cloud option. [Visit our sales page for details.](https://www.sonatype.com/request-nexus-lifecycle-and-firewall-cloud?hsLang=en-us)

## Installation Requirements

## Cloud Installation Requirements

### For Amazon EC2 - Secure Cloud Services

## Browser Requirements

IQ Server supports the latest version of your OS-supported browser at the time of the release date.

### For the best experience:

## REST API Requirements

The REST APIs are versioned. We recommend using the latest version of the IQ Server. This ensures your system will take advantage of the latest features and improvements.

## Estimating Heap Sizes

### General Memory Guidelines

- Minimum physical/RAM memory on the host 16GB for production use
- Minimum heap ( -Xms ) must equal set maximum heap ( -Xmx )
- Minimum heap size 8GB for production use
- Minimum unallocated host physical/RAM memory should be no less than 1/3 of total physical RAM to allow space for OS, application binaries, and SCM integration
- For heap >= 8GB recommend using G1GC garbage collector

### Guidelines for Heap Sizing

These profiles help gauge the typical physical memory requirements needed for a dedicated server host running IQ Server. *Due to the inherent complexities of use cases, one size does not fit all and this should only be interpreted as a guideline.*

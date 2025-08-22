---
layout: default
title: "Integration of IQ Webhook with Fortify SSC Sync Service"
parent: Fortify SSC
nav_order: 1
---

# Integration of IQ Webhook with Fortify SSC Sync Service

The Fortify SSC synchronization service supports data synchronization with the IQ server in two ways:

- Scheduled polling (cron jobs) using the Synchronization Scheduler Refer to details on [Synchronization Scheduler](https://help.sonatype.com/en/sonatype-fortify-ssc.html#synchronization-scheduler) .
- Using IQ webhooks The following sections describe the integration of Fortify SSC Sync service with IQ webhook event.

## Data Flow Using IQ Webhook Events

![Fortify_SSC_IQ_Webhook_drawio.png](/assets/images/uuid-07765f91-97b0-2901-280d-c221caaab088.png)

All application evaluations are sent to the Fortify SSC synchronization services. However, only those applications that are in the mapping file are processed.

Similar to the [Synchronization Scheduler](https://help.sonatype.com/en/sonatype-fortify-ssc.html#synchronization-scheduler) , continuous monitoring results are synchronized only if there is a change in the data or violation.

## Steps to Integrate IQ Webhook with Fortify SSC Sync Service

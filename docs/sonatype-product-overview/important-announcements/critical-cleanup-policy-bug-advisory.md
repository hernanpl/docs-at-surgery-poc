---
layout: default
title: "Critical Cleanup Policy Bug Advisory"
parent: Important Announcements
nav_order: 1
---

# Critical Cleanup Policy Bug Advisory

⚠️ **Warning:** This bug is fixed in release 3.41.1, which is now available. Please [download](#UUID-502a5426-c7f0-d5ee-9139-4a8b19bd5bc5) and upgrade to this or a later release.

Sonatype has discovered a critical bug that can cause [cleanup policies](#UUID-e936050e-ecbe-2f0c-14ac-12034790da0f) to unintentionally delete binaries in Nexus Repository deployments using H2 or PostgreSQL.

## Who is Impacted?

Deployments meeting **all** of the following criteria are impacted by this bug:

- Your deployment must be using Nexus Repository 3.31.0 to 3.41.0
- Your deployment must have been explicitly migrated to or originally deployed using an **H2** or **PostgreSQL** database
- Cleanup policies must be applied to one or more repositories
- Those cleanup policies must have *Component Age* or *Component Usage* criteria

## What Database am I Using?

If you are unsure what database you are using, take the following steps:

- Check your `$data-dir/etc/nexus.properties` for `nexus.datastore.enabled=true`
  - Property **does not exist** - you are using OrientDB and are not impacted by this bug
  - Property **does** exist - you are using either H2 or PostgreSQL and are potentially impacted by this bug
    - If there is also a `$nexus-dir/etc/fabric/nexus-store.properties` file that contains a Postgres JDBC URL, then you are using PostgreSQL
    - If no Postgres JDBC URL exists, but you do have `nexus.datastore.enabled=true` in your `$data-dir/etc/nexus.properties`, then you are using H2

Or

- Log into your Nexus Repository instance as an administrator
- Navigate to *Administration* → *Repository* and see if there is a *Data Store* menu item available
  - Menu item **does not exist** - you are using OrientDB and are not impacted by this bug
  - Menu item **does** exist - you are using either H2 or PostgreSQL and are potentially impacted by this bug

## What Should You Do if You are Currently Impacted?

If your deployment meets all of the above criteria, you should immediately take the following actions:

- Disable cleanup policy tasks
  - Navigate to *Admin* → *System* → *Tasks*
  - Locate the *Cleanup Service* task in the task list; select this task to open the detailed view
  - Uncheck the *Task enabled* box
- Disable the blob store compact task (if using File or Azure Blob Stores)
  - Navigate to *Admin* → *System* → *Tasks*
  - Locate the *Admin - Compact blob store* task; select this task to open the detailed view
  - Uncheck the *Task enabled* box
- Disable S3 Lifecycle Rules (if using S3 Blob Stores, see [https://aws.amazon.com/blogs/aws/amazon-s3-lifecycle-management-update/](https://aws.amazon.com/blogs/aws/amazon-s3-lifecycle-management-update/) )
- Disable Azure Blob Storage Lifecycle Rules if configured on the Azure side (if using Azure Blob Stores, see [https://docs.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-overview?tabs=azure-portal](https://docs.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-overview?tabs=azure-portal) )
- Preserve backup media that have already been made of your Nexus Repository deployment

## How Can You Prevent Impact if Not Currently Affected?

If your deployment does not meet all of the above criteria, you should take the following actions to prevent impact:

- If not currently using H2 or PostgreSQL, do not migrate at this time
- If you are already using H2 or PostgreSQL and have any cleanup policies, disable the cleanup policy tasks and blob store cleanup task:
  - Navigate to *Admin* → *System* → *Tasks*
  - Locate the *Cleanup Service* task and the *Admin - Compact blob store* task in the task list; select each task to open the detailed view
  - Uncheck the *Task enabled* box for each task
- If you are already using H2 or PostgreSQL, do not create new cleanup policies.

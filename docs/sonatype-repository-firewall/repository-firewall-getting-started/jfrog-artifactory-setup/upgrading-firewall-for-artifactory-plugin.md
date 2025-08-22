---
layout: default
title: "Upgrading Firewall for Artifactory plugin"
parent: JFrog Artifactory Setup
nav_order: 4
---

# Upgrading Firewall for Artifactory plugin

## 1.x to 2.0 Migration

Repository Firewall for JFrog Artifactory 2.0 fixes an issue in the 1.x series where the 'repository manager' column in the 'Repositories' view in IQ displayed a hash value instead of the repository name.

Do the following to complete the migration and display the repository identifier:

The migration will automatically begin on JFrog Artifactory startup.

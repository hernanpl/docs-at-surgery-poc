---
layout: default
title: "Container Security"
parent: Sonatype Integrations
nav_order: 4
---

# Sonatype Container Security Enhancement - OS-Focused Container Scans

Sonatype Container Security now offers the option to focus container scans exclusively on OS-related components and their associated vulnerabilities, excluding other component types like Java (jar) files. You can enable this feature by setting the [new environmental variable](#UUID-256fe272-31f8-babd-fac3-f39c0503cfae_section-idm4650626893318434200382712946) `NEXUS_CONTAINER_INCLUDE_ONLY_OS_COMPONENTS` to `true` . This enhancement provides greater flexibility and control over scan results, allowing users to concentrate specifically on OS-level security concerns.

---
layout: default
title: "Sonatype SBOM Manager"
nav_order: 6
has_children: true
---

# Sonatype SBOM Manager

This release includes the following changes for Sonatype SBOM Manager:

## Broader Catalog Coverage

Sonatype SBOM Manager now uses Common Platform Enumeration (CPE)–based matching to detect vulnerabilities across a broader catalog of technologies, including third-party applications, operating systems, firmware, and embedded hardware. This enhancement improves the depth and reach of vulnerability coverage in generated SBOMs, helping users identify more risks across their software supply chain.

This release also introduces a new *Data Enrichment* column in the *Disclosed Vulnerabilities* table. This column helps users differentiate vulnerability records based on metadata source: *Sonatype Enhanced* , *Vendor Data* , or *Public Data* . This enhancement improves transparency and makes it easier to understand the origin and trust level of each finding.

See the [SBOM Manager Component Details View help documentation](#UUID-61adf94a-2de2-6ae7-d24e-da33effe2ed9) for details.

---
layout: default
title: "SBOM Component Details View"
parent: Sonatype SBOM Manager
nav_order: 13
---

# SBOM Component Details View

The component detail view summarizes component metadata found from the source SBOM and Sonatype data services. Use this view to verify and report risk associated with components reported in your SBOM.

Use the VEX workflow to annotate any reported and discovered vulnerabilities from within your SBOM.

![SBOM-Component-Details-Header.png](/docs-at-surgery-poc/assets/images/uuid-40905ce6-0572-a9a9-ae5e-5d2dc16ffd2c.png)

Displayed under the component name; the parent organization, application, file name, and imported date for the SBOM this component. Use the top breadcrumb to return to the bill of materials view.

## Component Identifiers

Color-coded identifiers help you rapidly identify relational information about the component. A list of possible tags is provided in the table below:

## Component Summary

The component summary section provides risk analysis details for the component.

![Screenshot_2024-12-17_at_3_24_16_PM.png]({{ /assets/images/uuid-bde230cd-2ef0-d9e9-8a92-97eff719f40b.png)

## Disclosed Vulnerabilities and Sonatype Identified Vulnerabilities

The disclosed vulnerabilities section provides a table of vulnerabilities included in the original SBOM for components not known to Sonatype. The Sonatype identified vulnerabilities section lists vulnerabilities of the component and is updated through Continuous Monitoring.

![SBOM-disclosed-vulnerabilities.png](/docs-at-surgery-poc/assets/images/uuid-5e82032d-e008-04fd-fbfe-82f604eb1e7a.png)

### Vulnerability Details

Details about the vulnerability expand and appear in a side panel when you select an Issue ID.

![SBOM-Component-Details-Vulnerability-Details.png]({{ /assets/images/uuid-5d1a8c80-57eb-89aa-a768-c8e1a143aeeb.png)

The Vulnerability Details panel provides details of vulnerability including; description, explanation, detection, recommendations, affected versions, root causes, advisories, and CVSS details.

### Policy Violations

The policy violation tab lists the policy violations for the component. The violations may be selected to open the violation details view.

![Screenshot_2024-12-17_at_3_21_17_PM.png]({{ "/assets/images/uuid-371ebdda-d216-2533-ce3f-018f345a27f3.png)

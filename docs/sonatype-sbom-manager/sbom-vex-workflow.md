---
layout: default
title: "SBOM VEX Workflow"
parent: Sonatype SBOM Manager
nav_order: 15
---

# SBOM VEX Workflow

Vulnerability Exploitability eXchange or VEX communicates the exploitability of components with known vulnerabilities in the context of the product in which they are used. (source [CycloneDX documentation](https://cyclonedx.org/capabilities/vex/) ). The actual risk of a vulnerable component may be significantly lower when the vulnerable method is not referenced in the application's call flow or when development has isolated the risk from the rest of the application.

Using reachability analysis, developers determine when their applications are at risk of discovered vulnerabilities and use SBOM Manager to annotate their application's SBOM to communicate the exploitability status to their stakeholders.

The following steps are an overview of the VEX Workflow:

## Adding VEX Annotations to Vulnerabilities

VEX annotations are added from the or the .

## Copy VEX Annotations from Previous Versions

When the previous version of the application has been annotated with a VEX status and justification, those annotations may be copied to the current version's vulnerabilities to reduce the time your team spends on vulnerability management.

![sbom-vex-copy.png](/docs-at-surgery-poc/assets/images/uuid-4f298214-483b-ad71-4805-60da2c83fcbe.png)

## VEX Annotations

VEX Annotations are a set of normalized statuses for known vulnerabilities on open-source dependencies found in an SBOM. The status is used to simplify informing stakeholders of remediation efforts.

The following are the components of a VEX annotation for a vulnerability. Details are sourced from the [CycloneDX specifications](https://cyclonedx.org/docs/1.5/json/) . The analysis status is the only required field.

### Analysis status

Declares the current state of an occurrence of a vulnerability, after automated or manual analysis.

### Justification

The rationale of why the impact analysis state was asserted.

### Response

A response to the vulnerability by the manufacturer, supplier, or project responsible for the affected component or service. Responses are strongly encouraged for vulnerabilities where the analysis state is exploitable.

### Description

Detailed description of the impact including methods used during assessment. If a vulnerability is not exploitable, this field should include specific details on why the component or service is not impacted by this vulnerability.

## VEX Use cases

Learn more from [CISA.org VEX Use-cases](https://www.cisa.gov/sites/default/files/2023-01/VEX_Use_Cases_Aprill2022.pdf)

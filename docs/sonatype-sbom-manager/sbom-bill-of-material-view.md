---
layout: default
title: "SBOM Bill of Material View"
parent: Sonatype SBOM Manager
nav_order: 12
---

# SBOM Bill of Material View

The Bill of Material view summarizes the components and their risk found in the SBOM, focusing on annotating the vulnerabilities with VEX audit details.

![SBOM_Bill_of_Material_View.png](/assets/images/uuid-0c565fac-21ab-199a-2de7-d394817ce360.png)

## Actions

- Use the *Version Switcher* dropdown to navigate to other application versions.
- Use the **Export SBOM** : Dropdown to download the annotated SBOM. Options under the dropdown include: **Export Original SBOM** : Download the original unmodified SBOM. The original SBOM filenames are in the following format: **Additional Export Options** : Choose between CycloneDX or SPDX in either JSON or XML file formats. The annotated SBOM filenames follow the format below: The export will always use the latest version of the supported specification. **Export PDF** : Save a PDF report of the policy violations including a list of vulnerabilities, licenses, and components.
- **Export Original SBOM** : Download the original unmodified SBOM. The original SBOM filenames are in the following format:
- **Additional Export Options** : Choose between CycloneDX or SPDX in either JSON or XML file formats. The annotated SBOM filenames follow the format below: The export will always use the latest version of the supported specification.
- **Export PDF** : Save a PDF report of the policy violations including a list of vulnerabilities, licenses, and components.
- Select a component from the list to open the [component details view](#UUID-61adf94a-2de2-6ae7-d24e-da33effe2ed9) .

## Summary

Relationship of the reported dependencies. See [Software Dependencies: A beginner's guide](https://www.sonatype.com/blog/software-dependencies-a-beginners-guide) to learn more.

- **Direct** : The explicit dependencies that a software component defines and employs. **Transitive** : Dependencies indirectly used by a software component brought into your application as dependencies for other components. **Unspecified** : When the component's dependency information was not declared in the SBOM.
- **Direct** : The explicit dependencies that a software component defines and employs.
- **Transitive** : Dependencies indirectly used by a software component brought into your application as dependencies for other components.
- **Unspecified** : When the component's dependency information was not declared in the SBOM.
- Provides a total of known vulnerabilities for the components in the SBOM.
- **Release Ready** : The SBOM contains no high or critical vulnerabilities, or all high and critical vulnerabilities are VEX annotated. **Partially Annotated** : The SBOM includes some high or critical vulnerabilities, and not all of them are VEX annotated. **Needs Attention** : The SBOM contains some high or critical vulnerabilities, and none of them are VEX annotated.
- **Release Ready** : The SBOM contains no high or critical vulnerabilities, or all high and critical vulnerabilities are VEX annotated.
- **Partially Annotated** : The SBOM includes some high or critical vulnerabilities, and not all of them are VEX annotated.
- **Needs Attention** : The SBOM contains some high or critical vulnerabilities, and none of them are VEX annotated.
- Provides a total of known policy violations for the components in the SBOM.

## Components

The component list displays the components found in the SBOM with their dependency information, vulnerabilities, and licenses. The percentage annotated provides feedback at a glance on how well your teams are doing monitoring risk in your SBOMs.

- Use the `search bar` to filter by either the component name or license.
- The `Filter By` menu narrows results by vulnerability and dependency type.
- Selecting a component navigates to the component details view.

## Export PDF Report

The generated PDF includes the `Analysis Status` for VEX annotated vulnerabilities and third-party reported vulnerabilities stored in the SBOM.

See the [VEX Workflow](#UUID-802be01f-19ec-fc23-7537-34280dc06905) for details.

![SBM-Export-PDF-Analysis_Status.png](/assets/images/uuid-b086d3f3-d17f-6ef3-5030-1cc143cf0a3c.png)

## Missing Vulnerabilities in Imported SBOMs

If an uploaded SBOM includes vulnerability information but no vulnerabilities appear in the Bill of Material view after import and evaluation, it may be due to incomplete or insufficient vulnerability metadata within the SBOM file.

To ensure vulnerability data from the SBOM is properly recognized and retained after evaluation, the following fields are required or strongly recommended in the vulnerabilities section of the SBOM:

- `id` : a unique identifier for the vulnerability (e.g., `CVE-2022-42003` ).
- `ratings` : must include at least one rating object. Each rating must include a `score` (numerical CVSS score). `source` : it is highly recommended to include metadata about the source of the vulnerability (e.g., NVD or GHSA). If multiple sources are available, SBOM Manager prioritizes NVD data.
- `source` : it is highly recommended to include metadata about the source of the vulnerability (e.g., NVD or GHSA). If multiple sources are available, SBOM Manager prioritizes NVD data.
- `affects` : must link vulnerabilities to components using the `affects` field that references the components' `bom-ref` .

### Example of a properly structured vulnerability entry:

```
 {
  "vulnerabilities": [
    {
      "id": "CVE-2022-42003",
      "source": {
        "name": "NVD",
        "url": "http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42003"
      },
      "ratings": [
        {
          "source": {
            "name": "NVD"
          },
          "score": 7.5,
          "severity": "critical",
          "method": "CVSSv3",
          "vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H"
        },
        {
          "source": {
            "name": "NVD"
          },
          "score": 7.5,
          "severity": "critical"
        }
      ],
      "cwes": [
        502
      ],
      "analysis": {
        "state": "resolved_with_pedigree",
        "justification": "requires_environment",
        "response": [
          "workaround_available",
          "update"
        ],
        "detail": "Analysis Detail"
      },
      "affects": [
        {
          "ref": "pkg:maven/com.fasterxml.jackson.core/jackson-databind@2.13.4?type=jar"
        }
      ]
    }
  ]
}

```

### How SBOM Manager Processes Vulnerability Data

It's important to note that SBOM Manager is responsible for merging third-party vulnerability data from the SBOM with vulnerability insights from Sonatype’s proprietary data.

- If no valid rating (with score) is present in the SBOM, the vulnerability is considered informational only and will not be included in policy evaluation results.
- Vulnerabilities with missing or invalid `id` , no `score` , or lacking `ratings` will not be used for risk assessment and will not appear in the Bill of Material view.

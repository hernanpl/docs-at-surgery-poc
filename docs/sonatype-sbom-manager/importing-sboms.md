---
layout: default
title: "Importing SBOMs"
parent: Sonatype SBOM Manager
nav_order: 11
---

# Importing SBOMs

Import SBOMs and archives by selecting the *Import* button from the Applications View.

Supported file types include CycloneDX, SPDX, and most non-proprietary binary archive files.

SBOMs cannot use UTF-16; convert them to UTF-8 before importing.

**Note:** Compliance Stage The SBOM Manager uses the `Compliance` stage when importing SBOMs and Binary files. This stage is only available for the SBOM Manager solution as a target stage for Continuous Monitoring.

## Validation Errors on Import

Not all SBOMs are created at the same level of quality or fully meet the format's specification requirements. When validation errors occur during import the user has the option to proceed with the import at the risk of missing data in the Bill of Materials report.

Software Bill of Materials that failed validation have the warning message " `Invalid SBOM Detected` " at the top of the view and a warning icon remains to indicate the issue.

![sbm-application-validation-error.png](/assets/images/uuid-6d1f5c57-6bbd-eb43-ebe6-0f58b74e2477.png)

### Skip Validation

When importing an invalid SBOM, you have the option to import it as is by checking the option to "Skip validation and import anyway". This method only imports the components section of the SBOM.

**The option to**

![sbm-skip-validation.png](/assets/images/uuid-d11d1b21-9316-3613-bfeb-5ed775625115.png)

- Using this method only imports the components section of the SBOM and the resulting report may not be VEX annotated.
- If you import an invalid SBOM, only the original SBOM can be exported. Most other actions will be disabled.
- Use the validation error details to correct the original SBOM, making it valid for importing and managing in SBOM Manager.

**Note:** The `skipSbomImportValidation` feature flag, when enabled, will bypass the validation step during SBOM import in both Lifecycle and SBOM Manager. This means that if you import an invalid SBOM while this flag is enabled, you will not see the validation error modal in SBOM Manager, and the SBOM will be imported anyway. For more information about Lifecycle supported features go to the [Feature Configuration REST API](#UUID-c0e9fb56-7cb8-d415-9ee3-451a5bc9fd97) page.

## Similar Matching for SBOMs

When scanning binary files, Sonatype can determine when an open-source component has been modified from the versions found in open-source repositories. These components are labeled with the property `sonatype:match_state` as a `similar` match.

See the topic [Component Identification: Match States](#UUID-c8a1f963-f80b-dd2f-ca31-eac799d3267e_id_ComponentIdentification-matchstateMatchStates) to learn more.

![Screenshot_2024-12-09_at_2_39_37_PM.png](/assets/images/uuid-1872f6fd-76df-05d0-8d6b-133eb7fd5561.png)

## Binary File Names

When analyzing binary files, the name of the original binary files is stored with the component data and included in the user interface, the exported SBOM, and the PDF report. When storing the value in the SBOM the file name is included as the custom property `sonatype:original_file` .

![Screenshot_2024-12-09_at_2_45_19_PM.png](/assets/images/uuid-64e223ef-5e8a-2347-d511-7fbe03443a10.png)

## Supported Files for Importing

This table lists the supported files for importing. While individual project files are supported we recommend including the application in an archive file such as a zip or tar.gz.

**Note:** Converting between SPDX and CycloneDX formats The SPDX and CyconeDX formats are the most popular software bill of materials options. These standards are developed for different use cases and may not completely align with the information found within. Converting between SPDX and CycloneDX formats may result in the loss of data. Review our blog post to learn more about [comparing and converting between SBOM formats](https://www.sonatype.com/blog/how-to-convert-your-sbom-between-spdx-and-cyclonedx-formats) and the CycloneDX documentation on the [high-level overview of the information lost during conversion](https://github.com/CycloneDX/cyclonedx-dotnet-library#high-level-overview-of-information-lost-during-conversion) .

## Support for Container Analysis

Import SBOMs for your containers using Sonatype Container Security support in SBOM Manager. These scans use the Sonatype CLI and the container client to download images and analyze them for vulnerabilities.

This feature supports the following:

- The “ `compliance` ” stage is required to used for SBOM Manager.
- Use of the Sonatype CLI is limited to scan targets with the “ `container:` ” prefix
- Use of the Jenkins plugin is not supported.

Example Analysis

```
java -jar nexus-iq-cli.jar -a username:password -i app -s http://localhost:8070 -t compliance container:nginx:1.27.2
```

Learn more on [Sonatype Container Security](#UUID-256fe272-31f8-babd-fac3-f39c0503cfae) documentation.

## Merge Multiple SBOMs

When storing multiple SBOMs for a single application, say from various microservices, you may combine them into a single SBOM for the whole release.

This is accomplished with the following workflow:

The archive may include a mix of SBOMs as well as the application binaries to generate a single SBOM.

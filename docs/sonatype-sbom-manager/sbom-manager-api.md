---
layout: default
title: "SBOM Manager API"
parent: Sonatype SBOM Manager
nav_order: 10
---

# SBOM Manager API

We recommend using a user token and token password when using the API.

Examples use the localhost environment. Adjust the referencing service and credentials for your own environment. If you are in Sonatype Cloud, use `HTTPS` and include `/platform` in your API calls. See more details in [REST APIs](#UUID-2e8bede8-1587-8455-0658-e63ba0f39cab_section-idm4581033107560034273016704952) .

## Import an SBOM

Write permissions for the application are required to import a file. The application will have to be created before importing an SBOM.

Note also that SBOMs cannot use UTF-16; you will need to convert them to UTF-8 for them to be properly ingested.

```
POST /api/v2/sbom/import
```

- **applicationId** - use the GET to fetch the internal application ID.
- **file** - Full path to the SBOM file to import (as available on your client machine).
- **enableBinaryImport** - optional parameter to analyze a binary and generate an SBOM during the import step.
- **applicationVersion** - optional parameter to manually set the version of the imported SBOM.
- **ignoreValidationError** - optional parameter to import an SBOM if one or more skippable validation errors occur. The default value is `false` . When set to `true` , and skippable validation errors occur, only the SBOM components will be imported.

```
# Upload an SBOM (JSON or XML) – note the @ in front of the path
curl -u admin:admin123 \
  -F file=@/Users/andrewhaigh/Projects/AzureDevOps/struts2-rce/cyclonedx_1_6.sbom.json \
  -F applicationId=8e43cf2b6cd645a79faab71ff864cb45 \
  -F applicationVersion=my_app_version \
  -X POST 'http://localhost:8070/api/v2/sbom/import?ignoreValidationError=true'

```

Use the returned status URL to check the import status.

```
{"statusUrl":"api/v2/sbom/applications/c9920b0b240f405a8fc11c897864e2e5/status/a5bd3587cf7d45f3aaa2c09401a47b27"}
```

When complete, you will receive the details on your imported SBOM.

```
{
  "downloadUrl":"api/v2/sbom/c9920b0b240f405a8fc11c897864e2e5/version/20240409105223535?form=original",
  "applicationId":"c9920b0b240f405a8fc11c897864e2e5",
  "version":"20240409105223535",
  "isError":false,
  "errorMessage":null
}
```

### Analyzing a Binary for SBOM Import

Include the optional enableBinaryImport property when analyzing a binary archive on importing. This will analyze the binary and generate an SBOM to import in one step.

```
POST /api/v2/sbom/import?enableBinaryImport=true
```

Example curl

```
curl -i -u admin:admin123 -H "Content-Type: multipart/form-data" -X POST http://localhost:8070/api/v2/sbom/import?enableBinaryImport=true -F "applicationId={applicationId}" -F "file=@uber.jar" -F "applicationVersion=my_app_version"

```

**Note:** When importing binaries containing SBOMs, the SBOMs must follow the required naming conventions of including the `bom` suffix to be picked up by the scanner. See the [CycloneDX documentation](#UUID-71778dbe-a6d1-72eb-d37f-f1ae5835e7c9_section-idm23457062595783) for details.

## Export an SBOM in a specific format

Read permissions are required to export the SBOM.

```
GET api/v2/sbom/applications/{applidationId}/versions/{SBOM_version}?state=original&specification=cyclonedx1.5
```

- **applicationId** - use the GET to fetch the internal application ID
- **SBOM_version** - use the to fetch the available versions
- **state** ( *optional* ) - download either the imported or annotated versions. options include: `original` or `current` ( *default* )
- options include: `original` or `current` ( *default* )
- **specification** ( *optional* ) - Target specification of the SBOM. options include: `cyclonedx1.2` , `cyclonedx1.3` , `cyclonedx1.4` , `cyclonedx1.5` , `cyclonedx1.6` ( *default* ), `spdx2.2` , and `spdx2.3`
- options include: `cyclonedx1.2` , `cyclonedx1.3` , `cyclonedx1.4` , `cyclonedx1.5` , `cyclonedx1.6` ( *default* ), `spdx2.2` , and `spdx2.3`

Example

```
curl -i -u <UserToken>:<TokenPassword> "http://localhost:8070/api/v2/sbom/applications/c9920b0b240f405a8fc11c897864e2e5/versions/20240409105223535?state=original"
```

When successful, the SBOM is returned in the requested state and format.

## Get all SBOM Versions

Returns a list of SBOMS for an application. Read permissions for the application are required.

```
GET /api/v2/sbom/applications/{applicationId}
```

- **sortByDate** : Sort results by import date. Allowed values [asc|desc]. The default value is asc
- **pageSize** : Number of items to return by page. The default value is 10
- **page** : Current page number. The default value is 1

example

```
curl -i -u <UserToken>:<TokenPassword> -X GET "http://localhost:8070/api/v2/sbom/applications/f5dc55cbec7b47a4a21d59140b7c1934"
```

```
{
  "totalResultsCount": 1,
  "results": [
    {
      "applicationVersion": "20240412170706311",
      "spec": "CycloneDx",
      "specVersion": "1.1",
      "importDate": "2024-04-12T17:07:06.312-05:00",
      "none": 0,
      "low": 0,
      "medium": 6,
      "high": 3,
      "critical": 0
    }
  ]
}
```

## Get an SBOM Version

Downloads a specific SBOM version in its original or current state. Read permission for the applications are required.

```
GET /api/v2/sbom/applications/{applicationId}/versions/{sbom_version}
```

- **applicationId** - use the GET to fetch the internal application ID
- **SBOM_version** - use the to fetch the available versions

```
curl -i -u <UserToken>:<TokenPassword> -X GET "http://localhost:8070/api/v2/sbom/applications/f5dc55cbec7b47a4a21d59140b7c1934/versions/20240312111234920"
```

```
<?xml version="1.0" encoding="UTF-8"?>
<bom xmlns="http://cyclonedx.org/schema/bom/1.1" serialNumber="urn:uuid:3e671687-395b-41f5-a30f-a58921a69b79" version="1">
    <components>
        <component type="library">
            <publisher>Apache</publisher>
            <group>org.apache.tomcat</group>
            <name>tomcat-catalina</name>
            <version>9.0.14</version>
            <hashes>
                <hash alg="MD5">3942447fac867ae5cdb3229b658f4d48</hash>
                <hash alg="SHA-1">e6b1000b94e835ffd37f4c6dcbdad43f4b48a02a</hash>
                <hash alg="SHA-256">f498a8ff2dd007e29c2074f5e4b01a9a01775c3ff3aeaf6906ea503bc5791b7b</hash>
                <hash alg="SHA-512">e8f33e424f3f4ed6db76a482fde1a5298970e442c531729119e37991884bdffab4f9426b7ee11fccd074eeda0634d71697d6f88a460dce0ac8d627a29f7d1282</hash>
            </hashes>
            <licenses>
                <license>
                    <id>Apache-2.0</id>
                </license>
            </licenses>
            <purl>pkg:maven/org.apache.tomcat/tomcat-catalina@9.0.14?type=jar</purl>
        </component>
    </components>
</bom>
```

## Get components from SBOM

Lists the components in a specific SBOM version with data about vulnerabilities and licenses. Read permissions for the application are required.

```
GET /api/v2/sbom/applications/{applicationId}/versions/{SBOM_version}/components
```

- **applicationId** - use the GET to fetch the internal application ID
- **SBOM_version** - use the to fetch the available versions

```
curl -i -u <UserToken>:<TokenPassword> -X GET "http://localhost:8070/api/v2/sbom/applications/f5dc55cbec7b47a4a21d59140b7c1934/versions/20240412170706311/components"
```

```
[
  {
    "hash": "e6b1000b94e835ffd37f",
    "packageUrl": "pkg:maven/org.apache.tomcat/tomcat-catalina@9.0.14?type=jar",
    "componentIdentifier": {
      "format": "maven",
      "coordinates": {
        "artifactId": "tomcat-catalina",
        "extension": "jar",
        "groupId": "org.apache.tomcat",
        "version": "9.0.14"
      }
    },
    "displayName": "org.apache.tomcat : tomcat-catalina : 9.0.14",
    "licenses": [
      {
        "licenseId": "Apache-2.0",
        "licenseName": "Apache-2.0"
      },
      {
        "licenseId": "Public Domain",
        "licenseName": null
      }
    ],
    "vulnerabilitySeverityNoneCount": 0,
    "vulnerabilitySeverityLowCount": 0,
    "vulnerabilitySeverityMediumCount": 6,
    "vulnerabilitySeverityHighCount": 3,
    "vulnerabilitySeverityCriticalCount": 0
  }
]
```

## Delete an SBOM

Write permissions for the application are required to delete an SBOM.

```
DELETE /api/v2/sbom/applications/{applicationId}/versions/{sbomVersion}
```

- **applicationId** - use the GET to fetch the internal application ID
- **SBOM_version** - use the to fetch the available versions

Example

```
curl -i -u <UserToken>:<TokenPassword> -X DELETE "http://localhost:8070/api/v2/sbom/applications/f5dc55cbec7b47a4a21d59140b7c1934/versions/20240312111234920"
```

## Add/Update VEX annotations for an SBOM

Adds or updates a VEX annotation to a given component in a specific SBOM version. Write permissions for the application are required to modify VEX annotation.

```
PUT /api/v2/sbom/applications/{applicationId}/versions/{sbomVersion}/vulnerability/{vulnerabilityRef}/analysis
```

```
{
  "componentLocator": {
    "hash": "cf05e1449bccc5dae87b"
  }, 
  "vulnerabilityAnalysis": {
    "state": "exploitable", 
    "justification": "requires_dependency", 
    "response": "can_not_fix", 
    "detail": "no detail"
  }
}
```

- **componentLocator** (required): Locate the component either by hash (SHA-1) or Package-URL
- **vulnerabilityAnalysis** : information about the VEX annotation. **state** (required): vulnerability analysis state **justification** : The rationale of why the impact analysis state was asserted **response** : A response to the vulnerability by the manufacturer, supplier, or project responsible for the affected component or service. **detail** : Detailed description of the impact including methods used during the assessment
- **state** (required): vulnerability analysis state
- **justification** : The rationale of why the impact analysis state was asserted
- **response** : A response to the vulnerability by the manufacturer, supplier, or project responsible for the affected component or service.
- **detail** : Detailed description of the impact including methods used during the assessment

```
curl -i -u <UserToken>:<TokenPassword> -X PUT -d '{"componentLocator": {"hash": "cf05e1449bccc5dae87b"}, "vulnerabilityAnalysis": {"state": "exploitable", "justification": "requires_dependency", "response": "can_not_fix", "detail": "no detail"}}' "http://localhost:8070/api/v2/sbom/applications/f5dc55cbec7b47a4a21d59140b7c1934/versions/20240312111234920/vulnerability/CVE-2017-7525/analysis"
```

A summary of the update is returned on a successful response.

```
{
   "createdOn" : "2024-05-29T12:17:15.526-03:00",
   "detail" : null,
   "justification" : null,
   "lastUpdatedBy" : "jmartin",
   "lastUpdatedOn" : "2024-05-29T12:17:15.526-03:00",
   "response" : "can_not_fix",
   "state" : "exploitable"
}
```

Update

The annotation is updated when one has already been added. The `lastUpdatedOn` and `lastUpdatedBy` fields are modified when VEX annotations are added.

## Delete VEX annotations

Write permissions for the application are required to delete VEX annotations for a specific component's vulnerability.

```
DELETE /api/v2/sbom/applications/{applicationId}/versions/{sbomVersion}/vulnerability/{vulnerabilityRef}/analysis
```

```
{
  "hash": "cf05e1449bccc5dae87b",
  "packageUrl": "pkg:maven/org.apache.tomcat/tomcat-catalina@9.0.14?type=jar"
}
```

Either the component `hash` or `packageUrl` is required but not both. See to learn more.

- **hash** : The component’s truncated SHA1. Found in the URL of the component details view or using the get Components API for a specific SBOM version.
- **packageUrl** : Component’s Package-URL

```
curl -i -u <UserToken>:<TokenPassword> -X DELETE -d '{"hash": "cf05e1449bccc5dae87b"}' "http://localhost:8070/api/v2/sbom/applications/f5dc55cbec7b47a4a21d59140b7c1934/versions/20240312111234920/vulnerability/CVE-2017-7525/analysis"
```

## Interactive Swagger UI

### Interactive Swagger UI

Use the in-product Swagger interface to interact with the REST APIs to quickly execute API requests, and validate responses.

![APi_option_in_left_nav.png](/assets/images/uuid-6cd7e83d-ce4d-2b48-b011-9182b8f2e17a.png)

The *API* option in the left navigation bar displays the *API page* .

Click on the *Public* tab to access all REST APIs supported by Sonatype for your product.

REST APIs under the *Experimental* tab are evolving and are not recommended for critical workloads. We strongly recommend using them controlled environments at your own risk. Learn more about [Experimental APIs](#UUID-90b91a6a-1f18-4c8f-1a4d-8e84629b9e79) .

The REST APIs are arranged in an alphabetical order, with a brief description on usage.

![methods.png](/assets/images/uuid-ea0bde6c-1aad-3992-ea70-cf0a22004254.png)

Click on the dropdown arrow at the right end of the method names to expand the method descriptions.

Check the *Permissions required* to ensure you have the correct permissions to execute/try out the method.

The Swagger interface also enables you to import the REST APIs into any tool that supports OpenAPI (version 3), for downstream application development.

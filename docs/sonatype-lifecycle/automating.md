---
layout: default
title: "Automating"
parent: Sonatype Lifecycle
nav_order: 7
---

# Automating

The automating section of IQ Server Help is where you'll find info on things like REST APIs and how to get started using Webhooks.

## REST APIs

This section covers the REST APIs available for Sonatype IQ Server. Sonatype APIs are designed for system-to-system functionality with examples using the HTTP client curl. Following along, you may initiate the requests via a command line tool or modify the examples for other API tools. Most examples use the localhost environment with the default server credentials. You need to adjust the referencing service and credentials for your environment.

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

Many API reference component identifiers for searching and describing reporting components found in applications.

See for a comprehensive list of format coordinate examples.

Most Sonatype REST APIs are delineated between the API version and the branch. Some APIs are solution-specific and are only available depending on your licensed solution.

For self-hosted environments, we recommend keeping your software up to date to ensure compatibility with this documentation.

Take appropriate measures to prevent security issues such as Injection and Cross-Site Scripting (XSS) when using the responses of the APIs.

### IQ Server Product Version Format

IQ Server is versioned using a release identifier that is incremented sequentially for each generally available release. When referring to new functionality added to the IQ Server, typically the release number is provided. The release version is embedded as the second component of the IQ Server full product version:

**Examples** : Version 168, Release 169, IQ Server 170, etc

```
{major version}.{RELEASE VERSION}.{patch version}-{build number}
```

### Sonatype APIs for Cloud Environments

The following are considerations when making API calls to a Sonatype Cloud tenant.

Include the `/platform` path when making API calls to a Sonatype Cloud tenant.

```
curl -u {user}:{token} https://{tenant}.sonatype.app/platform/api/v2/applications
```

The REST API usage in Sonatype Cloud is subject to rate limiting.

- API requests rate limits: **1,500 requests / IP address / 5-minute period**

When rate limits are exceeded, the service returns a 429 error code with the following message.

- `Rate limit exceeded. Please wait 5 minutes. If this is a recurring issue, reach out to your administrator or contact your Sonatype support representative.`

### Accessing REST APIs via Reverse Proxy Authentication

API requests that change data are subject to cross-site request forgery (CSRF) protection. When authentication is handled by a reverse proxy server, these requests need to include matching headers and cookie tokens. The specific value of the token is irrelevant, only that it needs to be the same for both.

- required header: `X-CSRF-TOKEN`
- required cookie: `CLM-CSRF-TOKEN`

```
curl --header "X-CSRF-TOKEN: api" --cookie "CLM-CSRF-TOKEN=api" ...
```

### IQ API Reference

[https://sonatype.github.io/sonatype-documentation/api/iq/latest/iq-api.json](https://sonatype.github.io/sonatype-documentation/api/iq/latest/iq-api.json)

### Advanced Search REST API

APIs for automating the features.

### Application Categories REST API

The Application Categories API manages application categories or tags assigned to applications in an organization. An application category or tag consists of a name, a description and a color.

Possible values for the field color are:

```
light-red, light-green, light-blue, light-purple, dark-red, dark-green, dark-blue, dark-purple, orange, yellow
```

### Application REST API

The Application REST API is for managing applications in the IQ Server.

### Organizations REST API

The Organizations REST API is for creating new organizations, as well as retrieving, editing, or deleting existing organizations in IQ Server. The 'Edit IQ Elements' permissions are needed for the organizations referenced in the call.

To add a tag to an organization, refer to the [Application Categories REST API](#UUID-df27624d-90dd-86b8-f903-a127c4764f07) .

### Report REST APIs

The [Application Composition Report](#UUID-868dafe4-30f1-bdbb-96e8-6a161291dc6a) is created when an evaluation occurs.

### Atlassian Crowd REST API

You may configure an Atlassian Crowd server for authenticating users and managing users and groups. This section assumes you are familiar with Atlassian Crowd, and have a Crowd server currently in use.

### Audit Log REST API

The Audit Log REST API can retrieve data from the audit logs for your *Lifecycle* instance for the specified time period. The response will contain lines of text from the audit logs in chronologically ascending order.

**Permissions Required:** Access Audit Log

To configure a custom role that allows users to access the audit logs, click on *Create Role* button in the Roles section under *System Preferences* . Ensure that the *Access audit log* option under the *Permissions* section is enabled. For more information refer to [Roles and Permissions](https://help.sonatype.com/en/role-management.html) .

### Authorization Configuration REST API

Authorization configuration in IQ Server is done by granting/revoking [roles](#UUID-dbc7b586-b425-e5b2-82a5-76c9e16bbcee) to/from users and groups.

These APIs use internal IDs for organizations, applications, and roles.

To find the internal IDs for organizations and applications, use .

**Note:** You can use the static identifier `ROOT_ORGANIZATION_ID` for the root organization

To find the internal IDs for roles, use .

### Component Claim REST API

**Note:** Note that the IQ Server's UI currently only supports claiming components in the maven format. As such, viewing, adding, updating, and removing component claims in formats other than maven is currently only supported via this API.

### Component Details REST API

The Component Details REST API provides information on security vulnerability, license data, age, and popularity information for a specified component.

For more information on supported formats and examples, refer to .

### Component Evaluation REST API

The Component Evaluation REST API allows for a single component, or multiple components, to be evaluated against a specific application and the associated policies.

This API uses the following REST resources:

- POST - to submit a component or list of components, as well as the application containing the policies the component(s) will be evaluated against.
- GET - to check the status of the evaluation and retrieve the results when completed.

For the API we provide a step-by-step example using the HTTP client cURL, though any HTTP client tool could be used. In addition, we’ll reference other APIs such as the one required to obtain an application’s internal ID.

### Component Labels REST API

The Component Labels API allows you to manage component labels for applications, organizations, and repositories.

A component label consists of a label, a color, and an optional description.

Valid values for the field color are:

```
light-red, light-green, light-blue,  light-purple, dark-red, dark-green, dark-blue, dark-purple, orange, yellow
```

### Component Remediation REST API

The APIs listed on this page provide a way to obtain suggestions for the remediation of policy violations on a per-component basis. The remediation recommendations provided via these APIs are similar to those provided on the Component Details Page version graph. A component can be validated against policies that are either associated with an application or organization.

Remediation Output Types:

The endpoints return the following set of remediation output types:

- **next-no-violations** This type of remediation contains the version of the provided component that does not violate any policies. If no version meets this criteria, this remediation type will not be present in the response. If there is a version that meets this criteria, it will be returned as the recommendation for this remediation type.
- **next-non-failing** This type of remediation contains the version of the provided component that does not fail the build for the specified stageId. So, the recommended version in this remediation type could potentially trigger warnings based on the policies, but would not fail the build. Note that this type of remediation is only returned if the {stageId} parameter is supplied in the endpoint. Similar to next-no-violations remediation type, if no version meets this criteria, this type will not be present in the response. If there is a version that meets this criteria, it will be returned as the recommendation for this remediation type.
- **next-no-violations-with-dependencies** This type of remediation is similar to next-no-violations above but it also guarantees that all the dependencies of the recommended version do not violate any policy. If no version meets this criteria, this remediation type will not be present in the response. If there is a version that meets this criteria, it will be returned as the recommendation for this remediation type.
- **next-non-failing-with-dependencies** This type of remediation is similar to next-non-failing above but it also guarantees that all the dependencies of the recommended version do not fail the build for the specified stageId. So, the recommended version in this remediation type could potentially trigger warnings based on the policies and its dependencies could also potentially trigger warnings based on the policies, but the recommended component version and its dependencies will not fail the build. Note that this type of remediation is only returned if the {stageId} parameter is supplied in the endpoint. If no version meets this criteria, this type will not be present in the response. If there is a version that meets this criteria, it will be returned as the recommendation for this remediation type.

**Note:** The current version will be returned as recommended if it satisfies the recommendation strategy.

By including the input query parameter *includeParentRemediation* set to value *true* , the response will show whether the component is a direct dependency or transitive dependency and will contain the component details for remediation.

If the component is a transitive dependency, the response contains the remediation component details, based on the nearest parent dependency. The *type* field in the response indicates the type of remediation that is being suggested, i.e. version with **next-no-violations-with-dependencies** and **next-non-failing-with-dependencies** .

**Example curl command**

```
curl -u admin:admin123 -X POST -H "Content-Type: application/json" -d '{"componentIdentifier": {"format":"maven","coordinates": {"artifactId":"logback-core,"extension":"jar","groupId":"ch.qos.logback","version":"1.3.14"}}}' 'http://localhost:8070/api/v2/components/remediation/application/{applicationInternalId}?stageId={stageId}&scanId={scanId}&includeParentRemediation=true'
```

**Sample response if the component is a transitive dependency**

```
{
    "remediation": {
        "versionChanges": [
            {
                "type": "next-no-violations-with-dependencies",
                "data": {
                    "component": {
                        "packageUrl": "pkg:maven/ch.qos.logback/logback-core@1.3.14?type=jar",
                        "hash": null,
                        "componentIdentifier": {
                            "format": "maven",
                            "coordinates": {
                                "artifactId": "logback-core",
                                "classifier": "",
                                "extension": "jar",
                                "groupId": "ch.qos.logback",
                                "version": "1.3.14"
                            }
                        },
                        "displayName": "ch.qos.logback : logback-core : 1.3.14"
                    }
                },
                "directDependency": false,
                "directDependencyData": [
                    {
                        "component": {
                            "packageUrl": "pkg:maven/ch.qos.logback/logback-classic@1.3.14?type=jar",
                            "hash": null,
                            "componentIdentifier": {
                                "format": "maven",
                                "coordinates": {
                                    "artifactId": "logback-classic",
                                    "classifier": "",
                                    "extension": "jar",
                                    "groupId": "ch.qos.logback",
                                    "version": "1.3.14"
                                }
                            },
                            "displayName": "ch.qos.logback : logback-classic : 1.3.14"
                        }
                    }
                ]
            },
            {
                "type": "next-non-failing-with-dependencies",
                "data": {
                    "component": {
                        "packageUrl": "pkg:maven/ch.qos.logback/logback-core@1.3.14?type=jar",
                        "hash": null,
                        "componentIdentifier": {
                            "format": "maven",
                            "coordinates": {
                                "artifactId": "logback-core",
                                "classifier": "",
                                "extension": "jar",
                                "groupId": "ch.qos.logback",
                                "version": "1.3.14"
                            }
                        },
                        "displayName": "ch.qos.logback : logback-core : 1.3.14"
                    }
                },
                "directDependency": false,
                "directDependencyData": [
                    {
                        "component": {
                            "packageUrl": "pkg:maven/ch.qos.logback/logback-classic@1.3.14?type=jar",
                            "hash": null,
                            "componentIdentifier": {
                                "format": "maven",
                                "coordinates": {
                                    "artifactId": "logback-classic",
                                    "classifier": "",
                                    "extension": "jar",
                                    "groupId": "ch.qos.logback",
                                    "version": "1.3.14"
                                }
                            },
                            "displayName": "ch.qos.logback : logback-classic : 1.3.14"
                        }
                    }
                ]
            }
        ]
    }
}
```

If the component is a direct dependency, the response will contain the remediation component details and the type of remediation being suggested i.e. version with **next-no-violations-with-dependencies** and **next-non-failing-with-dependencies** .

**Example curl command**

```
curl -u admin:admin123 -X POST -H "Content-Type: application/json" -d '{"componentIdentifier": {"format":"maven","coordinates": {"artifactId":"logback-classic,"extension":"jar","groupId":"ch.qos.logback","version":"1.3.14"}}}' 'http://localhost:8070/api/v2/components/remediation/application/{applicationInternalId}?stageId={stageId}&scanId={scanId}&includeParentRemediation=true'
```

**Sample response if the component is a direct dependency**

```
{
    "remediation": {
        "versionChanges": [
            {
                "type": "next-no-violations",
                "data": {
                    "component": {
                        "packageUrl": "pkg:maven/ch.qos.logback/logback-classic@1.3.14?type=jar",
                        "hash": null,
                        "componentIdentifier": {
                            "format": "maven",
                            "coordinates": {
                                "artifactId": "logback-classic",
                                "classifier": "",
                                "extension": "jar",
                                "groupId": "ch.qos.logback",
                                "version": "1.3.14"
                            }
                        },
                        "displayName": "ch.qos.logback : logback-classic : 1.3.14"
                    }
                },
                "directDependency": true
            },
            {
                "type": "next-non-failing",
                "data": {
                    "component": {
                        "packageUrl": "pkg:maven/ch.qos.logback/logback-classic@1.3.14?type=jar",
                        "hash": null,
                        "componentIdentifier": {
                            "format": "maven",
                            "coordinates": {
                                "artifactId": "logback-classic",
                                "classifier": "",
                                "extension": "jar",
                                "groupId": "ch.qos.logback",
                                "version": "1.3.14"
                            }
                        },
                        "displayName": "ch.qos.logback : logback-classic : 1.3.14"
                    }
                },
                "directDependency": true
            },
            {
                "type": "next-no-violations-with-dependencies",
                "data": {
                    "component": {
                        "packageUrl": "pkg:maven/ch.qos.logback/logback-classic@1.3.14?type=jar",
                        "hash": null,
                        "componentIdentifier": {
                            "format": "maven",
                            "coordinates": {
                                "artifactId": "logback-classic",
                                "classifier": "",
                                "extension": "jar",
                                "groupId": "ch.qos.logback",
                                "version": "1.3.14"
                            }
                        },
                        "displayName": "ch.qos.logback : logback-classic : 1.3.14"
                    }
                },
                "directDependency": true
            },
            {
                "type": "next-non-failing-with-dependencies",
                "data": {
                    "component": {
                        "packageUrl": "pkg:maven/ch.qos.logback/logback-classic@1.3.14?type=jar",
                        "hash": null,
                        "componentIdentifier": {
                            "format": "maven",
                            "coordinates": {
                                "artifactId": "logback-classic",
                                "classifier": "",
                                "extension": "jar",
                                "groupId": "ch.qos.logback",
                                "version": "1.3.14"
                            }
                        },
                        "displayName": "ch.qos.logback : logback-classic : 1.3.14"
                    }
                },
                "directDependency": true
            }
        ]
    }
}
```

### Component Search REST API

The Component Search API returns the metadata for a component. This API searches application reports for the components specified.

Using GET requests it allows you to retrieve component information such as application ID, application name, report HTML URL, component hash, component coordinates, the highest threat level of the policy violations (for the found component), and dependency information.

Below, we’ve provided an example of the GET request. We’ve done this using the HTTP client cURL. Of course, you could use any HTTP client tool. Additionally, to help demonstrate the use of the API, we’ve broken out the various pieces for this request and provided an example of data that is retrieved.

### Component Versions REST API

The Component Versions API returns a list of versions for a component. This API method is available via a POST resource:

```
POST api/v2/components/versions
```

In order to use the API you must know the component identifier for the component you wish to find the versions for. A non-exhaustive list of examples for various formats is provided.

### Configuration REST API

The Configuration REST API allows users with the System Administrator role or the Edit System Configuration and Users permission, to configure the server.

### CPE Matching REST API

Use the CPE Matching Configuration REST API to add/set/remove CPE matching configuration to organizations and applications.

### Cross-Stage Policy Violation REST API

A Cross-Stage violation represents an aggregate of time-overlapping but equal policy violations within a given app across all stages. This data allows analysis such as how long it takes to investigate and remove a violation that was found during a stage until it is no longer reported in any stage.

You may use the steps described in to extract a particular policy violation ID you want to track.

### Data Retention Policy REST API

[Data retention policies](#UUID-2b3cfee1-89f1-01d1-3054-80b82081877c) help to limit the disk space consumption of IQ Server by defining what data is obsolete and hence can be removed from the server. The REST API described here allows you to inspect and change the retention policies that are in effect.

### Feature Configuration REST API

This API allows users with the [System Administrator role,](#UUID-dbc7b586-b425-e5b2-82a5-76c9e16bbcee) or the [Edit System Configuration and Users permission](#UUID-dbc7b586-b425-e5b2-82a5-76c9e16bbcee) to enable/disable certain Nexus IQ Server features.

### Mail REST API

For email-based notifications, configure an SMTP server. The REST API described here allows system administrators to manage that configuration. The base URL must be configured before starting.

### HTTP Proxy Server Configuration REST API

For IQ Server to be able to connect to other servers via an HTTP proxy server. The REST API described here allows system administrators to manage the HTTP proxy server configuration:

### JIRA Configuration REST API

This REST API endpoint allows anyone with the System Administrator role or the Edit System Configuration and Users permission to manage JIRA configurations for notifications.

**Note:** This REST API endpoint can be used with Jira Cloud, Jira Server, or Jira Data Center. Jira Server and Data Center users are encouraged to use the Sonatype for Jira integration for advanced features.

### License Legal REST API

This endpoint is only available with the [Advanced Legal Pack](#UUID-d81c430b-4c59-206b-62c0-b6b792f18fea) .

### License Overrides REST API

**Note:** Releases 189 - 190 used the path `api/v2/licenseOverride` for this API. However, in release 191, we have updated the API to match Sonatype's naming convention. As of release 191, this API uses `api/v2/licenseOverrides` (with " `Overrides` " now plural).

Use the endpoints on this page to manage the license overrides for a component.

**Methods Supported:**

- [POST](#UUID-8eadfe3c-ebaa-85d2-fab1-97940929f94f_section-idm33487080012528)
- [GET](#UUID-8eadfe3c-ebaa-85d2-fab1-97940929f94f_section-idm234870829974623)
- [DELETE](#UUID-8eadfe3c-ebaa-85d2-fab1-97940929f94f_section-idm234870847839827)

### Product License REST API

### Manifest Evaluation REST API

⚠️ **Warning:** This REST API was deprecated in IQ Server Release 126 and removed in IQ Server Release 169. Use instead.

### Policy Violation REST API

Use this REST API to access unfixed policy violation data gathered during the evaluation of applications.

**Note:** The Policy Violations REST API only retrieves non-fixed violations.

### Policy Waiver REST API

This API can be used to create, retrieve, update and delete policy waivers.

**NOTE: The GET Method currently does not support retrieval of expired waivers.**

### Policy Waiver Request REST API

This API can be used to create, retrieve, update and delete policy waivers requests.

**Methods Supported:**

- GET
- POST
- PUT

### Auto Policy Waiver REST API

The Auto Policy Waiver REST API allows you to manage the configuration of [Automated Waivers](#UUID-9ed00015-ccb9-9b92-4b3b-9f9967513617) for an organization or application.

Using this REST API you can create a new Automated Waiver configuration or retrieve, update or delete an existing Automated Waiver configuration.

**Permissions Required** : Waive Policy Violations

**Methods supported:**

- GET
- POST
- PUT
- DELETE

### Exclude Auto Policy Waiver REST API

Use this REST API to manage exclusion of [Automated Waivers](#UUID-9ed00015-ccb9-9b92-4b3b-9f9967513617) on security policy violations.

Automated Waivers, when configured at the organization or application level are applied to security policy violations that meet the configuration criteria. You can [exclude or remove an Automated Waiver](#UUID-9ed00015-ccb9-9b92-4b3b-9f9967513617_section-idm234694214606936) on a specific security policy violation, even if it is configured at the organization or application level.

**Permisisons Required:** Waive Policy Violations

**Methods Supported:**

- GET
- POST
- DELETE

### Applicable Waivers REST API

### Similar Waivers REST API

### Component Waivers REST API

**Note:** All repository reports must be re-evaluated in order to include the most accurate policy waiver information used by this API.

The Component Waivers API focuses on existing policy waivers by component. The waivers can be at any scope (app, org, root org, repository, or all repositories). Waivers are listed for each stage to fully detail all the waivers for an application. Stages can carry duplicate waivers, but this accurately reflects every waiver in which a component is in one stage and not another. For repository waivers the only applicable stage is the proxy stage.

### Stale Waivers REST API

The Stale Waivers REST API reports waivers that are stale. A waiver is considered to be stale when it is not used in the IQ Server. Examples are:

- A waiver applied in an evaluation and later skipped in another evaluation because the violation it waived does not exist anymore (perhaps due to component upgrade) is a stale waiver
- A waiver added but not applied because there was no evaluation is a stale waiver (it is not used until there is an evaluation)

A list of stale waivers is useful to identify potential risks in future evaluations because it helps to determine where violations can be unintentionally waived.

Stale evaluations listed under stale waivers help determine where evaluations may be needed in order to verify that the waivers are truly not used. An application or repository evaluation is considered to be stale if a new waiver has been created since the last evaluation.

**Note:** All repository reports must be re-evaluated after Nexus IQ Server version 76 in order to include the most accurate policy waiver information used by the new API.

### Transitive Waivers REST API

### Waiver Reason REST API

The Waiver Reason REST API can be used to retrieve all *Waiver Reasons* that can be applied to a waiver.

All authenticated users in *Lifecycle* can use the Waiver Reason REST API to view the *Waiver Reasons* .

### Promote Scan REST API

The Promote Scan REST API allows for an existing scan report to be promoted to a specified stage. The scan metadata generated for a specific build scan can be resubmitted for an evaluation of its components without having to rebuild the application. This new evaluation will update the most recent security and license data against your current policies.

### Reverse Proxy Authentication Configuration REST API

Use to manage a reverse proxy authentication configuration. These endpoints require the `System Administrator` role or the `Edit System Configuration and Users` permission.

### Role REST API

In the following sections, all partial URLs are relative to IQ Server's base URL, and we issue requests using the `cURL` tool. Also, all request/response bodies are JSON content (formatted here for readability).

### SAML REST API

SAML allows to integrate IQ Server with your single sign-on (SSO) infrastructure and this REST API enables [system administrators](#UUID-dbc7b586-b425-e5b2-82a5-76c9e16bbcee) to inspect and update the needed configuration for IQ Server. Consult the [SAML Integration](#UUID-20ae9fbe-ea8f-6190-9982-302d92303804) page for details on integrating IQ Server with an identity provider and/or configuring SAML using the UI instead of the REST API explained here.

### Security Vulnerability Override API

API to obtain the status (Security Vulnerability Override) of security vulnerabilities in the system, when one has been applied at a point in time.

### Source Control Configuration REST API

The REST API endpoints described here allow anyone with the System Administrator role or the Edit System Configuration and Users permission to manage a Source Control Configuration.

### Source Control Evaluation REST API

The Source Control Evaluation REST API provides a way to perform an application policy evaluation on supported manifest files discovered in a source control branch.

Source control evaluations are executed asynchronously and it is thus a 2-step process for the API user to obtain the results:

### Source Control REST API

Source Control REST API can be used to:

- Create, update, and delete source control entries for the root organization, sub-organizations, and applications. This is implemented with two separate endpoints one for all organizations (including the root), and a second one for applications. The API signatures between the two are similar and differences will be noted below.
- Automatically assign a role (e.g., *developer* ) to all contributors of the a GitHub repository. This removes the need for manual user role assignment. See [Automatic Role Assignment](#UUID-0af5b737-af38-5ec5-ea69-62d8211951d8_id_SourceControlRESTAPIv2-Step4-Deleteasourcecontrolentry) .
- [Map existing SCM user credentials](#section-idm234646010084107) (GitHub) to local or LDAP *Lifecycle* users. RELEASE 192 This has been extended to include SAML users. The Source Control REST API can be used to map existing SCM user credentials (GitHub) to local, LDAP, SAML users (for on-premises IQ Server) and OAuth (for Cloud/SaaS IQ Server).

⚠️ **Warning:** The `enablePullRequests` and `enableStatusChecks` fields in the JSON payload were deprecated in IQ Server Release 124: `- enablePullRequests` was replaced with `pullRequestCommentingEnabled` `- enableStatusChecks` was replaced with `statusChecksEnabled` If you use an IQ Server version prior to 124, you'll have to replace the deprecated field names in the examples below.

### CycloneDX REST API

This API returns a CycloneDX SBOM document (in both XML and JSON formats) containing coordinates and licenses for components in a scan report. It supports all component formats. Retrieve the internal application identifier and then pass it as an input parameter to get the SBOM report.

### SPDX REST API

The SPDX REST API returns an [SPDX](https://spdx.github.io/spdx-spec/v2.3/) SBOM document (in both XML and JSON formats) containing coordinates, licenses, and dependencies for components in an IQ Server-generated application scan report. This REST API supports all component formats.

### Success Metrics Data REST API

The Success Metrics Data REST API returns policy evaluation, violation and remediation data, aggregated monthly or weekly. This API is available via a POST resource:

```
POST api/v2/reports/metrics
```

**Note:** Larger data sets may take considerable time to load the first time you access Success Metrics Data. It is recommended to generate the aggregations first by creating and loading a [Success Metrics](#UUID-26c7f8c8-a12d-affa-b1b3-96772119846e) report for the desired applications and organizations.

### Third-Party Analysis REST API

Use the Third-Party Analysis REST API to perform an analysis of a software bill of materials (SBOM) for your application.

- The analysis is performed as an asynchronous request that can be monitored or as a fire-and-forget action.
- The analysis results include the Policy Actions as determined by the analysis stage.
- Users require the Evaluate Applications permission to call this API.
- When the same component is found more than once in the SBOM, only the data of the first component is processed.

### User REST API

The user REST API allows System Administrators to do the following.

In the following sections, all partial URLs are relative to IQ Server's base URL and we issue requests using the `cURL` tool. Also, all request/response bodies are JSON content (formatted here for readability) and any endpoints that return a user's details exclude their password for security.

**Note:** When enabled the audit log records changes to user access.

### User Token REST API

IQ Server users can create user tokens which then can be used for authentication instead of their usernames and passwords. A user token is a pair of a user code and a passcode unique to the user, which will grant the permissions that are granted with their credentials.

Further information regarding User Tokens can be found on the page.

### Vulnerability Details REST API

The Vulnerability Details REST API allows you to retrieve vulnerability details by passing a CVE ID/Sonatype vulnerability identifier or a component identifier. The response will include the **root causes** of the vulnerability when you pass the component identifier as a parameter in the GET request.

## Lifecycle Webhooks

Webhooks are HTTP callbacks that send data to a defined URL. Custom integrations may be built that respond to webhook event types from Lifecycle. When an event is triggered, the server sends an HTTP POST payload to the webhook’s defined URL.

With the received payload, your script may respond through the REST APIs.

Webhooks are defined by the following:

- **Webhook URL** - the destination the webhook payload is sent.
- **Description** - internal note for details on the use of the webhook.
- **Secret Key** - Defined by the user, use a secret key to ensure the authenticity of the source.
- **Event Type** - the event that occurs that is sent to the webhook.

### Webhook Limitations

A limitation with webhooks is that there is no validation that the webhook was received by the destination. No re-attempt requests are made on failures.

We do not recommend using webhooks for auditing purposes as notifications may be lost due to latency or the remote service not being available.

Use the [Audit Log](#UUID-8425a6ca-fe03-5803-f03b-3c6d6c8b1444) for mission-critical message queuing for reporting and monitoring.

### Webhook Access

Webhooks are created by System Administrators. Webhooks do not have a permissions model and will send HTTP requests for every configured event. The system consuming the webhooks will have access to all the data provided by the event types.

### Create a Webhook

Use the following steps to create a webhook.

Use the Webhook configuration to edit and delete webhooks.

### Working with HMAC Payloads

Hash-based message authentication code (or HMAC) is a cryptographic authentication technique that uses a hash function and a secret key. ( [source](https://www.okta.com/identity-101/hmac/) )

When enabling the secret key, the `X-Nexus-Webhook-Signature` header is sent with the webhook payloads to verify you are receiving an authentic message. When verifying the HMAC digest, the HmacDigest value should match the signature value.

### Example script when receiving the webhook

Webhooks may be consumed with many tools. The following example is a simple service using node.js.

Run the following to initialize the environment. The secret key is saved to a setting.json file.

```
npm init
npm install express
npm install body-parser
echo {\"secretKey\":\"secretKey\"} > settings.json
```

Add the code below to a file named `app.js` , and run the webhook listener via the command: `node app.js`

```
const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const settings = require('./settings.json');
const crypto = require('crypto');

app.use(bodyParser.json());

app.post('/', function(req, res) {
  const body = req.body;
  const signature = req.headers['x-nexus-webhook-signature'];
  var hmacDigest = crypto.createHmac("sha1", settings.secretKey).update(JSON.stringify(body)).digest("hex");

  console.log('Webhook received');
  console.log('Headers: ' + JSON.stringify(req.headers));
  console.log('Body: ' + JSON.stringify(req.body));
  console.log('HmacDigest: ' + hmacDigest);
  console.log('Signature: ' + signature);
  res.send();
});

app.listen(3000, function() {
  console.log('Server running on port 3000.');
});
```

Additional code may be added to further process the request by connecting with the server APIs to access details on the request.

### Example Headers and Payloads

It is important to understand the payload being received. The event contains special headers that help describe the event.

```
Content-Type: application/json; charset=UTF-8
User-Agent: Sonatype_CLM_Server/1.24.0-SNAPSHOT (Java 1.7.0_25; Mac OS X 10.11.5)
X-Nexus-Webhook-Signature: 687f3719b87232cf1c11b3ef7ea10c49218b6df1
X-Nexus-Webhook-Id: iq:policyManagement
X-Nexus-Webhook-Delivery: 7f4a6dde-5c68-4999-bcc0-a62f3fb8ae48
```

A payload is returned with each event type.

```
{
    'applicationEvaluation': {
        'policyEvaluationId': 'debceb1d-9209-485d-8d07-bd5390de7ef5',
        'stage': 'build',
        'ownerId': '6a454175-f55d-4d33-ba44-90ac3af2e8b8',
        'evaluationDate': '2015-05-05T23:40:12Z',
        'affectedComponentCount': 10,
        'criticalComponentCount': 2,
        'severeComponentCount': 5,
        'moderateComponentCount': 3,
        'outcome': 'fail'
    }
}
```

The data structure of the event payload differs by event.

### Lifecycle Webhooks Events Types

### Webhooks Concepts: IQ Server and Slack Integration

Using our Webhooks documentation in the IQ Space as a starting point, we want to show you how you can take that information and make something useful out of it. This article shows you how to build a webhook and deploy it to a Serverless framework like AWS Lambda. The Serverless function will consume an IQ policy evaluation event and push a message about it to Slack.

We chose Serverless because we found a lot of value in this integration, but we don’t want the overhead of an operations team managing it all. The Serverless framework allows AWS to handle management of the application, and only accrues charges when the requests come in and out. In other words—it spins up our application and handles the request, then turns down when it’s not needed. Serverless is perfectly suited for an example like this because we’re simply mapping an object that IQ Server provides into something that Slack expects.

## Experimental APIs

Here at Sonatype, we are always looking to innovate new technologies and make those tools available sooner to our users. The Experimental APIs allow our customers to use capabilities that are not currently supported for general usage.

As the design of these capabilities is in motion you should expect them to change over time as new functionality is added and performance improved. These features are not intended to be used for critical workloads until we ensure that they are ready for production and become Generally Available (GA.)

If you wish to use them, and we hope you do, know that they are 'use at your own risk' so take the necessary precautions by backing up your environments regularly and/or restricting their usage to testing environments. If you do run into trouble, click on the *Sonatype Labs* link at [community.sonatype.com](https://community.sonatype.com/c/sonatype-labs/32) .

Like with all our innovative features, we want to learn from you. Please direct your feedback to our [ideas.sonatype.com](http://ideas.sonatype.com/) portal or let our Customer Success team know your thoughts.

### Repository Results REST API

The Repository Results REST API allows for requesting information about the components in a repository. Depending on the owner type this endpoint may return details of multiple repositories. This REST API endpoint is accessed with the `View IQ Elements` permission.

### Vulnerability Custom Attributes REST API

The Vulnerability Custom Attributes REST API allows you to customize the attributes of a vulnerability, such as CWE ID, CVSS vector string, severity, and remediation. Customizing the vulnerability attributes to match your development environment can help with prioritizing the remediation of vulnerabilities. These values will override Sonatype-provided values. You can set up policy constraints based on these custom attributes.

### Vulnerability Group REST API

The Vulnerability Group REST API allows you to group multiple vulnerability IDs (CVEs and Sonatype vulnerability IDs) into custom vulnerability group names. These group names can be used to set up policy constraints.

### Vulnerability Analysis Details REST API

This experimental Vulnerability Analysis Details API allows you to maintain VEX information, by adding, updating or removing the analysis tag from a report’s vulnerability data. It accepts a *POST* request with a set of Cyclone DX formatted analysis details, with a reference vulnerability ID to be updated (replaced or added). It also accepts a *DELETE* post for a specific vulnerability ID to have the *analysis* elements removed.

### Call Flow Analysis REST API

The Call Flow Analysis REST API allows you to:

- GET the existing *call flow analysis* configuration for an application.
- PUT or create/update a new or existing *call flow analysis* configuration.
- DELETE an existing *call flow analysis* configuration for an application.

### ALP Dashboard REST APIs

The experimental REST APIs on this page provide a programmatic access to the same underlying datasets as used on the *Legal Obligations* page for the Advanced Legal Pack (ALP).

The *Legal Obligations* page is accessible from the *Legal* option in the left navigation bar of *Sonatype Lifecycle* .

**Methods Supported:**

- POST

### Attributions REST API

Use this REST API to manage *Additional Attributions* for a component.

**Methods Supported:**

- GET
- POST
- DELETE

### Copyrights REST API

Use this REST API to manage copyright notices for a component.

**Methods Supported:**

- GET
- POST

### Obligations REST API

Use this REST API to manage the Obligations for a component.

**Methods Supported:**

- GET
- POST
- DELETE

### Legal REST API

Use this REST API to manage Notice files and License files for a component.

**Methods Supported:**

- GET
- POST

### Source Link REST API

Use this REST API to specify the links to the original source code files for the component.

**Methods Supported:**

- POST

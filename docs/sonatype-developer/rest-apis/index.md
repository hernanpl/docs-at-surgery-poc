---
layout: default
title: "REST APIs"
parent: Sonatype Developer
nav_order: 6
has_children: true
---

# REST APIs

This section covers the REST APIs available for Sonatype IQ Server. Sonatype APIs are designed for system-to-system functionality with examples using the HTTP client curl. Following along, you may initiate the requests via a command line tool or modify the examples for other API tools. Most examples use the localhost environment with the default server credentials. You need to adjust the referencing service and credentials for your environment.

## Interactive Swagger UI

Use the in-product Swagger interface to interact with the REST APIs to quickly execute API requests, and validate responses.

![APi_option_in_left_nav.png](/docs-at-surgery-poc/assets/images/uuid-6cd7e83d-ce4d-2b48-b011-9182b8f2e17a.png)

The *API* option in the left navigation bar displays the *API page* .

Click on the *Public* tab to access all REST APIs supported by Sonatype for your product.

REST APIs under the *Experimental* tab are evolving and are not recommended for critical workloads. We strongly recommend using them controlled environments at your own risk. Learn more about [Experimental APIs](#UUID-90b91a6a-1f18-4c8f-1a4d-8e84629b9e79) .

The REST APIs are arranged in an alphabetical order, with a brief description on usage.

![methods.png]({{ /assets/images/uuid-ea0bde6c-1aad-3992-ea70-cf0a22004254.png)

Click on the dropdown arrow at the right end of the method names to expand the method descriptions.

Check the *Permissions required* to ensure you have the correct permissions to execute/try out the method.

The Swagger interface also enables you to import the REST APIs into any tool that supports OpenAPI (version 3), for downstream application development.

Many API reference component identifiers for searching and describing reporting components found in applications.

See for a comprehensive list of format coordinate examples.

Most Sonatype REST APIs are delineated between the API version and the branch. Some APIs are solution-specific and are only available depending on your licensed solution.

For self-hosted environments, we recommend keeping your software up to date to ensure compatibility with this documentation.

Take appropriate measures to prevent security issues such as Injection and Cross-Site Scripting (XSS) when using the responses of the APIs.

## IQ Server Product Version Format

IQ Server is versioned using a release identifier that is incremented sequentially for each generally available release. When referring to new functionality added to the IQ Server, typically the release number is provided. The release version is embedded as the second component of the IQ Server full product version:

**Examples** : Version 168, Release 169, IQ Server 170, etc

```
{major version}.{RELEASE VERSION}.{patch version}-{build number}
```

### Find the IQ Server Version Using the HTTP Response Server Header

HTTP responses from IQ Server include a "Server" header that contains the full product version.

The Server header value has this format:

```
{product http name}/{major version}.{release version}.{minor version}-{build number}
```

Using an HTTP client to make the following request from the command line:

```
curl -sSkI http://localhost:8070/ping

HTTP/1.1 200 OK
Date: Thu, 04 Jan 2024 15:11:09 GMT
Strict-Transport-Security: max-age=31536000; includeSubDomains

```

The following example returns just the Server from the response:

```
curl -I http://localhost:8070/ping 2>&1 | grep -i '^Server:' | awk '{print $2}'

NexusIQ/1.183.0-01
```

In this example, the `release version` is 183.

## Sonatype APIs for Cloud Environments

The following are considerations when making API calls to a Sonatype Cloud tenant.

Include the `/platform` path when making API calls to a Sonatype Cloud tenant.

```
curl -u {user}:{token} https://{tenant}.sonatype.app/platform/api/v2/applications
```

The REST API usage in Sonatype Cloud is subject to rate limiting.

- API requests rate limits: **1,500 requests / IP address / 5-minute period**

When rate limits are exceeded, the service returns a 429 error code with the following message.

- `Rate limit exceeded. Please wait 5 minutes. If this is a recurring issue, reach out to your administrator or contact your Sonatype support representative.`

## Accessing REST APIs via Reverse Proxy Authentication

API requests that change data are subject to cross-site request forgery (CSRF) protection. When authentication is handled by a reverse proxy server, these requests need to include matching headers and cookie tokens. The specific value of the token is irrelevant, only that it needs to be the same for both.

- required header: `X-CSRF-TOKEN`
- required cookie: `CLM-CSRF-TOKEN`

```
curl --header "X-CSRF-TOKEN: api" --cookie "CLM-CSRF-TOKEN=api" ...
```

## IQ API Reference

[https://sonatype.github.io/sonatype-documentation/api/iq/latest/iq-api.json](https://sonatype.github.io/sonatype-documentation/api/iq/latest/iq-api.json)

## Advanced Search REST API

APIs for automating the features.

### Create the Advanced Search Index

Creating or rebuilding the index is demanding on IQ Server's database. The index will continue to process after making the request so have patience.

- Requires user with the System Administrator role.
- Allow many minutes for the request to complete
- Avoid performing this operation during peak hours for large instances

```
POST /api/v2/search/advanced/index
```

Example:

```
curl -u admin:admin123 -X POST http://localhost:8070/api/v2/search/advanced/index
```

### GET Advanced Search Results

Searches are made using GET requests. Parameters need to be URL-encoded for special characters.

```
GET /api/v2/search/advanced?query=query&pageSize=10&page=1
```

The mandatory query parameter is the string to search for. Query parameters: pageSize and page are optional with default values of 10 and 1 respectively.

The allComponents parameter is used to retrieve search results including components with no violations. The default value is false and optional.

For example, using a local installation of IQ Server with its default configuration, a request using the cURL tool would be:

```
curl -u admin:admin123 http://localhost:8070/api/v2/search/advanced?query=itemType%3Aorganization&pageSize=10&page=1&allComponents=true
```

In this request the ':' is URL encoded to '%3A'. As with the Advanced Search feature in the UI, asterisks '*' are wildcards and are URL encoded to %2A

When the search index does not exist or is unreadable, the request returns a 409 status code. Otherwise, a JSON response body is returned.

An example of a successful response body for the above example search request is as follows:

```
{
    "searchQuery": "itemType:organization",
    "page": 1,
    "pageSize": 10,
    "totalNumberOfHits": 2,
    "isExactTotalNumberOfHits": true,
    "groupingByDTOS": [
        {
            "groupIdentifier": "ITEM_TYPE",
            "groupBy": "ORGANIZATION",
            "additionalInfo": null,
            "searchResultItemDTOS": [
                {
                    "itemType": "ORGANIZATION",
                    "organizationId": "ROOT_ORGANIZATION_ID",
                    "organizationName": "Root Organization",
                    "resultIndex": 1
                },
                {
                    "itemType": "ORGANIZATION",
                    "organizationId": "aadb7e6a9c1444378498af5e0f7decab",
                    "organizationName": "org",
                    "resultIndex": 2
                }
            ]
        }
    ]
}
```

### GET Export CSV Search Results

Use the following endpoint to export the results in CSV format. The endpoint receives 2 parameters:

- query parameter contains the search query
- allComponents parameter to get non-violating components (defaults to false)

```
GET /api/v2/search/advanced/export/csv?query=query&allComponents=true
```

Fields are filled according to the item type, and an empty field means that the item type does not contain the value itself.

Example:

```
curl -u admin:admin123 -X GET http://localhost:8070/api/v2/search/advanced/export/csv?query=componentName%3Ajquery%2A > output.csv

```

The resulting .csv will contains violating components with a componentName field that matches the search phrase jquery*. As we did not use the allComponents parameter, our data is limited to components associated with a violation.

## Application Categories REST API

The Application Categories API manages application categories or tags assigned to applications in an organization. An application category or tag consists of a name, a description and a color.

Possible values for the field color are:

```
light-red, light-green, light-blue, light-purple, dark-red, dark-green, dark-blue, dark-purple, orange, yellow
```

### Creating Application Categories

An application category or tag for an organization can be created by sending a POST request

```
POST /api/v2/applicationCategories/organization/{organizationId}
```

with a body specifying the application category's details.

As an example, in order to create an application category using the cURL tool for the organization with id `3c1f21228ec243d5abdff55e913c7ab8` the command would be as follows:

```
curl -u admin:admin123 -X POST -H 'Content-Type: application/json' 'http://localhost:8070/api/v2/applicationCategories/organization/3c1f21228ec243d5abdff55e913c7ab8' -d '{"name": "Internal Application","color": "dark-blue","description": "Applications internal to company."}'
```

The server responds with a `200 OK` upon successful creation echoing the created application category with its details including the assigned `id` :

```
{
  "id": "72ad13b69f1141bdba66ff396a905b68",
  "name": "Internal Application",
  "description": "Applications internal to company",
  "organizationId": "3c1f21228ec243d5abdff55e913c7ab8",
  "color": "dark-blue"
}
```

### Retrieving Application Categories

Application categories or tags owned by an organization can be retrieved by sending a `GET` request

```
GET /api/v2/applicationCategories/organization/{organizationId}
```

As an example, in order to list owned application categories using the cURL tool for the organization with id `3c1f21228ec243d5abdff55e913c7ab8` the command would be as follows:

```
curl -u admin:admin123 'http://localhost:8070/api/v2/applicationCategories/organization/3c1f21228ec243d5abdff55e913c7ab8'
```

The server responds with a `200 OK` upon successful query and returns application categories available to an organization:

```
[
  {
    "id": "72ad13b69f1141bdba66ff396a905b68",
    "name": "Internal Application",
    "description": "Applications internal to company",
    "organizationId": "3c1f21228ec243d5abdff55e913c7ab8",
    "color": "dark-blue"
  },
  {
    "id": "93e7890eebbf45a990927c1ac9a547e1",
    "name": "Test",
    "description": "Test",
    "organizationId": "3c1f21228ec243d5abdff55e913c7ab8",
    "color": "orange"
  }
]
```

### Updating Application Categories

An application category or tag owned by an organization can be updated by sending a `PUT` request to

```
PUT /api/v2/applicationCategories/organization/{organizationId}
```

with a body specifying the application category's details including the `id` of the application category to be updated.

As an example, in order to update an application category using the cURL tool for the organization with id `3c1f21228ec243d5abdff55e913c7ab8` the command would be as follows:

```
curl -u admin:admin123 -X PUT -H 'Content-Type: application/json' 'http://localhost:8070/api/v2/applicationCategories/organization/3c1f21228ec243d5abdff55e913c7ab8' -d '{"id": "72ad13b69f1141bdba66ff396a905b68", "name": "Internal Application - Updated","color": "light-red","description": "Description updated."}'
```

The server responds with a `200 OK` upon successful update echoing the updated application category with its details:

```
{
  "id": "72ad13b69f1141bdba66ff396a905b68",
  "name": "Internal Application - Updated",
  "description": "Description updated.",
  "organizationId": "3c1f21228ec243d5abdff55e913c7ab8",
  "color": "light-red"
}
```

### Deleting Application Categories

An application category or tag can be deleted sending a `DELETE` request to

```
DELETE /api/v2/applicationCategories/organization/{organizationId}/{applicationCategoryId}
```

The server responds with a `204 No Content` upon successful deletion.

## Application REST API

The Application REST API is for managing applications in the IQ Server.

### Getting the Application ID

The application ID is the internal system reference created when adding an application to the IQ Server. Use this identifier to reference the application in most REST API calls reference a specific application. Find the application ID from the Application REST API using the Public ID assigned by your organization to the application when it was created. The Public ID is located under the application name in the IQ Server user interface.

```
GET /api/v2/applications?publicId={PublicId}
```

The application ID is labeled as ' `id` ' in the response metadata for the application.

```
{ "applications": [
  {
    
```

### Getting All Applications

Retrieve all applications

```
GET /api/v2/applications
```

```
curl -u [token]:{password} http://localhost:8070/api/v2/applications
```

The endpoint returns all of the applications the user has read permissions to access.

Here is an example of what might be returned.

```
{ "applications": [
 {
   "id": "e1db2d3f4ccf40a38f193183bffdb7e5",
   "publicId": "app1",
   "name": "app1",
   "organizationId": "8162c39152974035b8d66df12f5abe7d",
   "contactUserName": null,
   "applicationTags": []
 },
 {
   "id": "47951e63ddd742868484dee8630767bc",
   "publicId": "app3",
   "name": "app3",
   "organizationId": "3e9d988f6727420ea445b02fbeaf73e9",
   "contactUserName": null,
   "applicationTags": [
     {
       "id": "feaf2c2e33854216bd47f62d9d5371a8",
       "tagId": "131765d40bee47fb9be5bc60d7b52cce",
       "applicationId": "47951e63ddd742868484dee8630767bc"
     }
   ]
  }
]}
```

### Adding Applications using the REST API

When adding a new application to IQ Server we recommend including the application context (the application categories and organization the application will belong to) and access control (who owns and has access to the application). Consider using [automatic applications](#UUID-970842c9-7d92-6480-0ef5-651e25d453c8) when setting the organization and access controls are not required.

### Update Application Information

The following application metadata may be modified after adding the application.

- "publicId" - When changing the public ID, remember to update your integration and build tools to use the new value.
- "name" - The name will need to be unique or the request will fail.
- "contactUserName" - The username of the owner responsible for the application used in the UI and reports.
- "applicationTags" (tagID) - Application categories assigned to the application used to scope policy.

The following identifiers may not be modified:

- "id" - This is the internally assigned application ID used to reference the application.
- "organizationId" - The parent organizational group to which the application belongs. See the "Moving an Application to a Different Organization" section to change the application's organization.

Use the same request body object from adding a new application when making the PUT update request.

Example Request

```
curl -u admin:admin123 -X PUT -H "Content-Type: application/json" -d '{"id":"4bb67dcfc86344e3a483832f8c496419","publicId":"MyApplicationID","name":"MySecondApplication","organizationId":"bb41817bd3e2403a8a52fe8bcd8fe25a","contactUserName":"NewAppContact","applicationTags":[{"tagId":"cfea8fa79df64283bd64e5b6b624ba48"}]}' 'http://localhost:8070/api/v2/applications/4bb67dcfc86344e3a483832f8c496419'
```

When successful the request will return the updated application object.

### Moving an Application to a Different Organization

An application may be moved from one organization to another using the request:

```
POST /api/v2/applications/{applicationInternalId}/move/organization/{organizationId}
```

```
curl -u admin:admin123 -X POST http://localhost:8070/api/v2/applications/4bb67dcfc86344e3a483832f8c496419/move/organization/bb41817bd3e2403a8a52fe8bcd8fe25a
```

The possible responses are as follows:

- If the application is successfully moved to the target organization, status code 200 will be returned with an empty body.
- Moving an application to a different organization can be successful albeit with warnings. In this case, status code 200 is returned with a body containing the warnings as follows:

```
{
  "warnings": [
    "Some policy waivers (1 in total) that were previously inherited no longer apply in the new parent organization.",
    "Some component labels (2 in total) that were previously inherited no longer exist in the new parent organization.",
    "Some license overrides (3 in total) that were previously inherited no longer exist in the new parent organization."
  ]
}
```

- Moving an application to an organization can fail due to conflicts between the organizations the application is moved between. In this case status code 409 is returned with errors as follows:

```
{
  "errors": [
    "The application category 'Internal' from the organization 'Source-Organization' has no counterpart in the new parent organization.",
    "The policy 'Internal-Policy' from the organization 'Source-Organization' has no counterpart in the new parent organization."
  ]
}
```

- If either an application with the provided "applicationInternalId" or an organization with the submitted "organizationId" is not found, this request yields status code 404.
- Trying to move an application to the same organization yields status code 400.

### Deleting an Application

Permanently delete an application

⚠️ **Warning:** Deleting an application will permanently remove the application and all scan data associated with it.

```
DELETE /api/v2/applications/{applicationInternalId}
```

```
curl -u admin:admin123 -X DELETE 'http://localhost:8070/api/v2/applications/4bb67dcfc86344e3a483832f8c496419'
```

Standard HTTP status codes are returned in response to the request.

## Organizations REST API

The Organizations REST API is for creating new organizations, as well as retrieving, editing, or deleting existing organizations in IQ Server. The 'Edit IQ Elements' permissions are needed for the organizations referenced in the call.

To add a tag to an organization, refer to the [Application Categories REST API](#UUID-df27624d-90dd-86b8-f903-a127c4764f07) .

### Get a list of organizations

Fetch all organizations or query for a specific one. The response will include the organization's parent org as well as any application tags configured at this level.

Get all organizations

```
GET /api/v2/organizations
```

To get a specific organization by its organization ID

```
GET /api/v2/organizations/{organizationId}
```

Query for a specific organization by name.

```
GET /api/v2/organizations?organizationName={YourOrganizationName}
```

Example using the organization ID:

```
curl -u admin:admin123 -X GET http://localhost:8070/api/v2/organizations/8e4f7ced6b9d462390f7df882b43c4fb
```

Example Response:

```
{
    "organizations": [
        {
            "id": "36d7e629462a4038b581488c347959bc",
            "name": "My Organization",
                        "parentOrganizationId": "9b0a94c9187e46cca05866208a7d79cb"
            "tags": [ ]
        },
        {
            "id": "f48b5344fa204a4c88df96b2d455d521",
            "name": "My Organization 2",
                        "parentOrganizationId": "9b0a44c9187e46cca05866208a7d79cb"
            "tags": [
                {
                    "id": "cd8fd2f4f289445b8975092e7d3045ba",
                    "name": "Distributed",
                                        "description": "Applications that are provided for consumption outside the company",
                    "color": "yellow"
                },
                {
                    "id": "004d789684834f7c889c8b186a5ff24b",
                    "name": "Hosted",
                                        "description": "Applications that are hosted such as services or software as a service.",
                    "color": "grey"
                },
                {
                    "id": "da9e09887c754157a2113831ae7e99ac",
                    "name": "Internal",
                    "description": "Applications that are used only by your employees",
                    "color": "green"
                }
            ]
        }
    ]
}
```

### Adding organizations using POST request

To add a new organization named "My Organization." The name of the organization provided should be unique. When leaving out a parent organization the new organization will be added to the root organization.

```
POST /api/v2/organizations
```

Payload example:

```
{
    "name": "My Organization"
}
```

Payload example with a parent organization. You must include the organization ID of the parent.

```
{
    "name": "test-grand4-child",
    "parentOrganizationId": "9b0a94c9187e46cca05866208a7d79cb"
}
```

Sample cURL:

```
curl -u admin:admin123 -X POST -H "Content-Type: application/json" -d '{"name": "My Organization"}' 'http://localhost:8070/api/v2/organizations'
```

Example POST response

```
{
    "id": "ab3d35233046480a9c30bb2437a48103",
    "name": "My Organization",
        "parentOrganizationId": "ROOT_ORGANIZATION_ID"
    "tags": []
}
```

### Moving an organization using PUT request

Use the PUT method to change the parent organization to a new parent organization in the hierarchy. This can be used to transition an existing single organization-level hierarchy to [multi-level organization hierarchy](#UUID-11edcff9-b9af-84a5-06ae-cd1c7f3d3924_section-idm457156767605283421427955469) .

```
PUT /api/v2/organizations/{organizationId}/move/destination/{destinationId}
```

The organization ID refers to the organization that is being moved and the destination ID is the organization ID of the new parent.

200 - HTTP response code indicates that the organization has been successfully moved under a new parent in the hierarchy. The JSON response may list warnings if any, even if the move is successful.

409 - HTTP response code indicates that the organization could not be moved due to conflicts/causes listed in the "errors" response field.

```
{
  "errors": [
    {
      "message": "New parent org Org Level 2 is already set and in use as the parent of org Org 2 Level 3",
      "type": "PARENT_HIERARCHY"
    }
  ],
  "warnings": [
    {
      "message": "Some policy waivers that were previously inherited no longer apply in the new parent organization.",
      "type": "POLICY_WAIVER"
    }
  ]
}
```

### Response fields for successful GET and POST requests

### Error response fields for POST request

## Report REST APIs

The [Application Composition Report](#UUID-868dafe4-30f1-bdbb-96e8-6a161291dc6a) is created when an evaluation occurs.

The Reports API provides a summary of an application’s most recent reports across the various stages (e.g. Build, Stage Release, and Release). The API consists of using the GET REST resource that is part of both the applications and reports APIs.

To assist in learning to use this API we will provide both the API as well as an example using the HTTP client cURL. We’ve approached this in a step-by-step manner that will start with gathering the internal application ID and then retrieving the report information.

**Note:** In our example below, we have isolated retrieving a report for a single application. However, if desired the reports for all applications can also be retrieved. In this case, skip to Step 2, where a corresponding tip has been included to assist.

### Raw Component's Data by Report REST API (v2)

When an application is evaluated, two very distinct sets of information are generated; the first set pertains to the components identified in an application and the vulnerabilities and licenses associated to them, we call this information the *Raw Data* . The second set of information is the result of evaluating the Raw Data against the policies defined in IQ.

The following steps detail how to obtain the *Raw Data* . The steps for obtaining the Policy data are detailed later on the section *Policy Data by Report REST API (v2).*

### Policy Violations by Report REST API (v2)

As mentioned before, in the process of scanning an application and after identifying the components and their raw data, the next step consists of evaluating this data against the policies defined in IQ.

The following API endpoint is a way to obtain the information resulting from this evaluation.

**Note:** It is important to note that this API endpoint is *Component oriented,* meaning that its results are centered around components and how the data relates to them (including the policy violations). This contrasts with the whose results are centered around violations.

### Retrieving Application Evaluation Policy Violation Diffs

Nexus IQ for SCM allows policy evaluations to be linked to the Git commit hash of the scanned commit. Using the hash, the diff on policy violations for two commits with associated policy evaluations is executed. This diff report enables users to track the impact of their changes on policy violations.

### Retrieving the Scan Report History

Use the GET method to retrieve a list of the latest reports (100 maximum) for a given application.

**Example:**

Obtain the internal application ID and use the GET request to retrieve the policy evaluation history.

```
GET /api/v2/reports/applications/{applicationInternalId}/history
```

Using the cURL command and the application ID from the example above, it would look like this:

```
curl -u admin:admin123 -X GET 'http://localhost:8070/api/v2/reports/applications/4537e6fe68c24dd5ac83efd97d4fc2f4/history'
```

**Response:**

```
{
    "applicationId": "4537e6fe68c24dd5ac83efd97d4fc2f4",
    "policyEvaluations": [
        {
            "stage": "develop",
            "applicationId": "4537e6fe68c24dd5ac83efd97d4fc2f4",
            "evaluationDate": "2020-06-03T13:43:10.816-03:00",
            "latestReportHtmlUrl": "ui/links/application/MyApplicationID/latestReport/develop",
            "reportHtmlUrl": "ui/links/application/MyApplicationID/report/53a99dd8b58e4d819c0791a8087df62c",
            "embeddableReportHtmlUrl": "ui/links/application/MyApplicationID/report/53a99dd8b58e4d819c0791a8087df62c/embeddable",
            "reportPdfUrl": "ui/links/application/MyApplicationID/report/53a99dd8b58e4d819c0791a8087df62c/pdf",
            "reportDataUrl": "api/v2/applications/MyApplicationID/reports/53a99dd8b58e4d819c0791a8087df62c/raw",
            "policyEvaluationId": "6ccd7900214f45d6b7fe5d99324b16c9",
            "scanId": "53a99dd8b58e4d819c0791a8087df62c",
            "isReevaluation": false,
            "isForMonitoring": false,
            "commitHash": "7951853e5d0f048ae48925820b138e0bcc4148f2",
            "scanTriggerType": "WEB_UI",
            "policyEvaluationResult": {
                "alerts": [],
                "affectedComponentCount": 14,
                "criticalComponentCount": 9,
                "severeComponentCount": 4,
                "moderateComponentCount": 1,
                "criticalPolicyViolationCount": 35,
                "severePolicyViolationCount": 17,
                "moderatePolicyViolationCount": 2,
                "grandfatheredPolicyViolationCount": 0,
                "legacyViolationCount": 0
            }
        },
        {
            "stage": "release",
            "applicationId": "4537e6fe68c24dd5ac83efd97d4fc2f4",
            "evaluationDate": "2020-06-03T13:42:41.311-03:00",
            "latestReportHtmlUrl": "ui/links/application/MyApplicationID/latestReport/release",
            "reportHtmlUrl": "ui/links/application/MyApplicationID/report/a2be87580faa40dcb6c5ca6408d30b8e",
            "embeddableReportHtmlUrl": "ui/links/application/MyApplicationID/report/a2be87580faa40dcb6c5ca6408d30b8e/embeddable",
            "reportPdfUrl": "ui/links/application/MyApplicationID/report/a2be87580faa40dcb6c5ca6408d30b8e/pdf",
            "reportDataUrl": "api/v2/applications/MyApplicationID/reports/a2be87580faa40dcb6c5ca6408d30b8e/raw",
            "policyEvaluationId": "c52c14df046f4f0fb5ee9723165f866d",
            "scanId": "a2be87580faa40dcb6c5ca6408d30b8e",
            "isReevaluation": false,
            "isForMonitoring": false,
            "commitHash": "7951853e5d0f048ae48925820b138e0bcc4148f2",
            "scanTriggerType": "WEB_UI",
            "policyEvaluationResult": {
                "alerts": [],
                "affectedComponentCount": 14,
                "criticalComponentCount": 9,
                "severeComponentCount": 4,
                "moderateComponentCount": 1,
                "criticalPolicyViolationCount": 35,
                "severePolicyViolationCount": 17,
                "moderatePolicyViolationCount": 2,
                "grandfatheredPolicyViolationCount": 0,
                "legacyViolationCount": 0
            }
        }
    ]
}
```

Using the query parameters `stage` and/or `limit` allows you to retrieve reports from a specific stage and/or limited to a given count (most recent reports.)

**Example:**

```
curl -u admin:admin123 -X GET 'http://localhost:8070/api/v2/reports/applications/4537e6fe68c24dd5ac83efd97d4fc2f4/history?stage=release&limit=1'
```

**Response:**

```
{
    "applicationId": "4537e6fe68c24dd5ac83efd97d4fc2f4",
    "policyEvaluations": [
        {
            "stage": "release",
            "applicationId": "4537e6fe68c24dd5ac83efd97d4fc2f4",
            "evaluationDate": "2020-06-03T13:42:41.311-03:00",
            "latestReportHtmlUrl": "ui/links/application/MyApplicationID/latestReport/release",
            "reportHtmlUrl": "ui/links/application/MyApplicationID/report/a2be87580faa40dcb6c5ca6408d30b8e",
            "embeddableReportHtmlUrl": "ui/links/application/MyApplicationID/report/a2be87580faa40dcb6c5ca6408d30b8e/embeddable",
            "reportPdfUrl": "ui/links/application/MyApplicationID/report/a2be87580faa40dcb6c5ca6408d30b8e/pdf",
            "reportDataUrl": "api/v2/applications/MyApplicationID/reports/a2be87580faa40dcb6c5ca6408d30b8e/raw",
            "policyEvaluationId": "c52c14df046f4f0fb5ee9723165f866d",
            "scanId": "a2be87580faa40dcb6c5ca6408d30b8e",
            "isReevaluation": false,
            "isForMonitoring": false,
            "commitHash": "7951853e5d0f048ae48925820b138e0bcc4148f2",
            "scanTriggerType": "WEB_UI",
            "policyEvaluationResult": {
                "alerts": [],
                "affectedComponentCount": 14,
                "criticalComponentCount": 9,
                "severeComponentCount": 4,
                "moderateComponentCount": 1,
                "criticalPolicyViolationCount": 35,
                "severePolicyViolationCount": 17,
                "moderatePolicyViolationCount": 2,
                "grandfatheredPolicyViolationCount": 0
            }
        }
    ]
}
```

### Application Dependency Tree REST API

**Note:** This endpoint works for Java (Maven) and NPM applications.

## Atlassian Crowd REST API

You may configure an Atlassian Crowd server for authenticating users and managing users and groups. This section assumes you are familiar with Atlassian Crowd, and have a Crowd server currently in use.

### Creating/updating a Crowd Connection

To create/update a Crowd connection, a System Administrator can issue a PUT request at the following endpoint:

```
PUT /api/v2/config/crowd
```

The PUT request must use the `application/json` content type and must provide the connection data in the request body. The request body must contain the following fields:

**serverUrl** , which holds the Crowd Server URL.

**applicationName** , which holds the Crowd Application Name.

**applicationPassword** , which holds the Crowd Application Password.

When updating you don't need to provide all fields, instead you can provide only the fields you want to update except when updating the server URL since that also requires the application password.

```
curl -X PUT -u admin:admin123 -H 'Content-Type: application/json' -d '{"serverUrl": "http://localhost:8095/crowd", "applicationName": "sonatype", "applicationPassword": "admin123"}' http://localhost:8070/api/v2/config/crowd
```

The successful HTTP response would be **204 No Content.**

### Getting Crowd Connection details

To get an existing Crowd connection, a System Administrator can issue a GET request at the following endpoint:

```
GET /api/v2/config/crowd
```

```
curl -u admin:admin123 http://localhost:8070/api/v2/config/crowd
```

The successful HTTP response would be **200 OK** . The response looks like this:

```
{
    "serverUrl": "http://localhost:8095/crowd",
    "applicationName": "sonatype"
}
```

For security reasons, the password is not included as part of the response.

### Removing a Crowd Connection

To remove an existing Crowd connection, a System Administrator can issue a DELETE request at the following endpoint:

```
DELETE /api/v2/config/crowd
```

Only a single Crowd configuration may be set or deleted.

```
curl -u admin:admin123 -X DELETE http://localhost:8070/api/v2/config/crowd
```

The successful HTTP response would be 204 No Content.

### Testing a new or existing Crowd Connection

To test a Crowd Connection, a System Administrator can issue a POST request at the following endpoint:

```
POST /api/v2/config/crowd/test
```

For testing an existing connection, a request body is not required, otherwise, the request body must contain the following fields:

- `serverUrl` : holds the Crowd Server URL
- `applicationName` : holds the Crowd Application Name
- `applicationPassword` : holds the Crowd Application Password

For example, using a local installation of IQ Server with its default configuration and assuming the Crowd server is also installed locally, a request using the curl tool would be:

```
curl -u admin:admin123 -X POST -H 'Content-Type: application/json' -d '{"serverUrl": "http://localhost:8095/crowd", "applicationName": "sonatype", "applicationPassword": "admin123"}' http://localhost:8070/api/v2/config/crowd/test
```

For testing an existing connection, a request using the cURL would be:

```
curl -u admin:admin123 -X POST http://localhost:8070/api/v2/config/crowd/test
```

The successful HTTP response would be 200 OK.

```
{"code":200,"message":null}
```

## Audit Log REST API

The Audit Log REST API can retrieve data from the audit logs for your *Lifecycle* instance for the specified time period. The response will contain lines of text from the audit logs in chronologically ascending order.

**Permissions Required:** Access Audit Log

To configure a custom role that allows users to access the audit logs, click on *Create Role* button in the Roles section under *System Preferences* . Ensure that the *Access audit log* option under the *Permissions* section is enabled. For more information refer to [Roles and Permissions](https://help.sonatype.com/en/role-management.html) .

### Methods Supported

### Related Links:

[Audit logging configuration](https://help.sonatype.com/en/logging-configuration.html#audit-log-162302) for more information on audit events.

[Lifecycle system logs](https://help.sonatype.com/en/audit-log.html) for more information on audit logs.

## Authorization Configuration REST API

Authorization configuration in IQ Server is done by granting/revoking [roles](#UUID-dbc7b586-b425-e5b2-82a5-76c9e16bbcee) to/from users and groups.

These APIs use internal IDs for organizations, applications, and roles.

To find the internal IDs for organizations and applications, use .

**Note:** You can use the static identifier `ROOT_ORGANIZATION_ID` for the root organization

To find the internal IDs for roles, use .

### Get the users and groups by role

Get the users and groups by role for an application by making an HTTP GET request to:

```
GET /api/v2/roleMemberships/application/{applicationInternalId}
```

Get the users and groups by role for an organization by making an HTTP GET request to:

```
GET /api/v2/roleMemberships/organization/{organizationId}
```

Get the users and groups by role for all repositories by making an HTTP GET request to:

```
GET /api/v2/roleMemberships/repository_container
```

Get the users and groups by role for administrator roles by making an HTTP GET request to:

```
GET /api/v2/roleMemberships/global
```

For example

```
curl -X GET -u admin:admin123 'http://localhost:8070/api/v2/roleMemberships/organization/a67da3c322d44ed68a2f5ae17db6a965'
```

returns the users and groups by role for the organization with ID a67da3c322d44ed68a2f5ae17db6a965:

```
{
  "memberMappings": [
    {
      "roleId": "1da70fae1fd54d6cb7999871ebdb9a36",
      "members": [
        {
          "ownerId": "a67da3c322d44ed68a2f5ae17db6a965",
          "ownerType": "ORGANIZATION",
          "type": "USER",
          "userOrGroupName": "admin"
        },
        {
          "ownerId": "a67da3c322d44ed68a2f5ae17db6a965",
          "ownerType": "ORGANIZATION",
          "type": "USER",
          "userOrGroupName": "mike"
        }
      ]
    },
    {
      "roleId": "1cddabf7fdaa47d6833454af10e0a3ef",
      "members": [
        {
          "ownerId": "a67da3c322d44ed68a2f5ae17db6a965",
          "ownerType": "ORGANIZATION",
          "type": "USER",
          "userOrGroupName": "ted"
        }
      ]
    }
  ]
}
```

Note that the result includes both members that were granted a role for the particular organization/application the REST request was made for as well as members that inherit a role from higher up in the organization hierarchy.

### Grant a role to a user or group

A role can be granted to a user for an application by making an HTTP PUT request to:

```
PUT /api/v2/roleMemberships/application/{applicationInternalId}/role/{roleId}/user/{userName}
```

A role can be granted to a group for an application by making an HTTP PUT request to:

```
PUT /api/v2/roleMemberships/application/{applicationInternalId}/role/{roleId}/group/{groupName}
```

A role can be granted to a user for an organization by making an HTTP PUT request to:

```
PUT /api/v2/roleMemberships/organization/{organizationId}/role/{roleId}/user/{userName}
```

A role can be granted to a group for an organization by making an HTTP PUT request to:

```
PUT /api/v2/roleMemberships/organization/{organizationId}/role/{roleId}/group/{groupName}
```

A role can be granted to a user for all repositories by making an HTTP PUT request to:

```
PUT /api/v2/roleMemberships/repository_container/role/{roleId}/user/{userName}
```

A role can be granted to a group for all repositories by making an HTTP PUT request to:

```
PUT /api/v2/roleMemberships/repository_container/role/{roleId}/group/{groupName}
```

An administrator role can be granted to a user by making an HTTP PUT request to:

```
PUT /api/v2/roleMemberships/global/role/{roleId}/user/{userName}
```

An administrator role can be granted to a group by making an HTTP PUT request to:

```
PUT /api/v2/roleMemberships/global/role/{roleId}/group/{groupName}
```

For example

```
curl -X PUT -u admin:admin123 'http://localhost:8070/api/v2/roleMemberships/organization/a67da3c322d44ed68a2f5ae17db6a965/role/1da70fae1fd54d6cb7999871ebdb9a36/user/mike'
```

grants the role with ID 1da70fae1fd54d6cb7999871ebdb9a36 (this is the ID of the Developer role) to user mike for the organization with ID a67da3c322d44ed68a2f5ae17db6a965.

### Revoke a role from a user or group

A role can be revoked from a user for an application by making an HTTP DELETE request to:

```
DELETE /api/v2/roleMemberships/application/{applicationInternalId}/role/{roleId}/user/{userName}
```

A role can be revoked from a group for an application by making an HTTP DELETE request to:

```
DELETE /api/v2/roleMemberships/application/{applicationInternalId}/role/{roleId}/group/{groupName}
```

A role can be revoked from a user for an organization by making an HTTP DELETE request to:

```
DELETE /api/v2/roleMemberships/organization/{organizationId}/role/{roleId}/user/{userName}
```

A role can be revoked from a group for an organization by making an HTTP DELETE request to:

```
DELETE /api/v2/roleMemberships/organization/{organizationId}/role/{roleId}/group/{groupName}
```

A role can be revoked from a user for all repositories by making an HTTP DELETE request to:

```
DELETE /api/v2/roleMemberships/repository_container/role/{roleId}/user/{userName}
```

A role can be revoked from a group for all repositories by making an HTTP DELETE request to:

```
DELETE /api/v2/roleMemberships/repository_container/role/{roleId}/group/{groupName}
```

An administrator role can be revoked from a user by making an HTTP DELETE request to:

```
DELETE /api/v2/roleMemberships/global/role/{roleId}/user/{userName}
```

An administrator role can be revoked from a group by making an HTTP DELETE request to:

```
DELETE /api/v2/roleMemberships/global/role/{roleId}/group/{groupName}
```

For example

```
curl -X DELETE -u admin:admin123 'http://localhost:8070/api/v2/roleMemberships/organization/a67da3c322d44ed68a2f5ae17db6a965/role/1da70fae1fd54d6cb7999871ebdb9a36/user/mike'
```

revokes the role with ID 1da70fae1fd54d6cb7999871ebdb9a36 (this is the ID of the Developer role) from user mike for the organization with ID a67da3c322d44ed68a2f5ae17db6a965.

## Component Claim REST API

**Note:** Note that the IQ Server's UI currently only supports claiming components in the maven format. As such, viewing, adding, updating, and removing component claims in formats other than maven is currently only supported via this API.

### GET a Component Claim by Component Hash

To get a component's claim, you can issue a GET request to the following path

```
GET /api/v2/claim/components/{componentHash}
```

where `componentHash` is the SHA1 hash of the component.

Below is an example request

```
curl -u admin:admin123 http://localhost:8070/api/v2/claim/components/4632184fe1d932764efe
```

If a component claim does not exist for the given component hash, then the request yields HTTP status code 404. Otherwise, a JSON response will be returned with the following properties

The following is an example successful response

```
{
    "hash": "4632184fe1d932764efe",
    "comment": "c1",
    "createTime": "2020-02-14T00:00:00.000Z",
    "claimerId": "admin",
    "claimerName": "Admin BuiltIn"
    "componentIdentifier": {
        "format": "maven",
        "coordinates": {
            "artifactId": "a",
            "classifier": "c",
            "extension": "e",
            "groupId": "g",
            "version": "v"
        }
    },
    "packageUrl": "pkg:maven/g/a@v?classifier=c&type=e"
}
```

### GET all Component Claims

To get all component claims, a Policy Administrator can issue a GET request to the following path

```
GET /api/v2/claim/components
```

Below is an example request

```
curl -u admin:admin123 http://localhost:8070/api/v2/claim/components
```

The following is an example successful response

```
{
    "componentClaims": [
        {
            "hash": "4632184fe1d932764efe",
            "comment": "c1",
            "createTime": "2020-02-14T00:00:00.000Z",
            "claimerId": "admin",
            "claimerName": "Admin BuiltIn"
            "componentIdentifier": {
                "format": "maven",
                "coordinates": {
                    "artifactId": "a",
                    "classifier": "c",
                    "extension": "e",
                    "groupId": "g",
                    "version": "v"
                }
            },
            "packageUrl": "pkg:maven/g/a@v?classifier=c&type=e"
        },
        {
            "hash": "6d0684d8acf85cd6e7f2",
            "comment": "c2",
            "createTime": "2020-01-09T15:01:10.000Z",
            "componentIdentifier": {
                "format": "a-name",
                "coordinates": {
                    "name": "n",
                    "qualifier": "q",
                    "version": "v"
                }
            },
            "packageUrl": "pkg:a-name/n@v?qualifier=q"
        }
    ]
}
```

### POST/Add/Update a Component Claim

To add or update a component claim, a Policy Administrator can issue a POST request to the following path

```
POST /api/v2/claim/components
```

The request requires a JSON body/payload, using the same properties described above, and must include at least a `hash` (of the component being claimed) and a valid `componentIdentifier` / `packageUrl` .

Below is an example request

```
curl -u admin:admin123 -X POST -H "Content-Type: application/json" -d '{"hash":"a4d45b211072d89c0e54","comment":"c3","createTime":"2020-01-09T15:01:10.000Z","componentIdentifier":{"format":"npm","coordinates":{"packageId":"p","version":"v"}}}' http://localhost:8070/api/v2/claim/components
```

The following is an example successful response

```
{
    "hash": "a4d45b211072d89c0e54",
    "comment": "c3",
    "createTime": "2020-01-09T15:01:10.000Z",
    "claimerId": "admin",
    "claimerName": "Admin BuiltIn"
    "componentIdentifier": {
        "format": "npm",
        "coordinates": {
            "packageId": "p",
            "version": "v"
        }
    },
    "packageUrl": "pkg:npm/p@v"
}
```

### DELETE a Component Claim by Component Hash

To delete a component claim, you can issue a DELETE request to the following path

```
DELETE /api/v2/claim/components/{componentHash}
```

where `componentHash` is the SHA1 hash of the component. If a component claim does not exist for the given component hash, then the request yields HTTP status code 404.

Below is an example request

```
curl -X DELETE -u admin:admin123 http://localhost:8070/api/v2/claim/components/6d0684d8acf85cd6e7f2
```

## Component Details REST API

The Component Details REST API provides information on security vulnerability, license data, age, and popularity information for a specified component.

For more information on supported formats and examples, refer to .

### Methods supported:

```
POST api/v2/components/details
```

Using the POST request, this API can be used to retrieve component data in 3 ways:

### Example 1: Passing the componentIdentifier

In our example we’ll be searching using Maven coordinates.

Include the *componentIdentfier* as JSON

```
{
  "components": [
    {
        "componentIdentifier": {
        "format": "maven",
        "coordinates": {
          "artifactId": "tomcat-util",
          "extension": "jar",
          "groupId": "tomcat",
          "version": "5.5.23"
         }
      }
    }
  ]
}
```

Putting this together with the cURL command, as well as including the IQ Server URL for the POST resource path, you should have something that looks like this:

```
curl -u admin:admin123 -X POST -H "Content-Type: application/json" -d '{"components":[{"hash": null,"componentIdentifier": {"format":"maven","coordinates": {"artifactId":"tomcat-util","extension":"jar","groupId":"tomcat","version":"5.5.23"}}}]}' 'http://localhost:8070/api/v2/components/details'
```

### Example 2: Passing the packageURL Identifier

Example for retrieving information on a Maven component:

```
{
 "components": [
   {
     "packageUrl":"pkg:maven/tomcat/tomcat-util@5.5.23?type=jar"
   }
 ]
}
```

cURL command to run this request:

```
curl -u admin:admin123 -X POST -H "Content-Type: application/json" -d '{"components":[{"packageUrl":"pkg:maven/tomcat/tomcat-util@5.5.23?type=jar"}]}' 'http://localhost:8070/api/v2/components/details'
```

### Example 3: Passing the hash for the component

Example for retrieving details based on component hash:

```
curl -u admin:admin123 -X POST -H "Content-Type: application/json" -d '{"components":[{"hash":"1249e25aebb15358beddd23d4cb09d793c75c33d"}]}' 'http://localhost:8070/api/v2/components/details'
```

### Response Fields:

IQ Server will respond with the component details as shown below. Note that the returned hash value is truncated and is meant to be used as an identifier that can be passed into subsequent REST API calls. It is not intended to be used as a checksum.

```
{
   "componentDetails":[
      {
         "component":{
            "packageUrl": "pkg:maven/tomcat/tomcat-util@5.5.23?type=jar",
            "hash":"1249e25aebb15358bedd",
            "componentIdentifier":{
               "format":"maven",
               "coordinates":{
                  "artifactId":"tomcat-util",
                  "classifier":"",
                  "extension":"jar",
                  "groupId":"tomcat",
                  "version":"5.5.23"
               }
            },
            "displayName": "tomcat : tomcat-util : 5.5.23"
         },
         "matchState":"exact",
         "catalogDate":"2008-01-29T01:45:22.000-05:00",
         "relativePopularity":100,
         "hygieneRating": "Exemplar",
         "integrityRating": "Pending",
         "licenseData":{
            "declaredLicenses":[
               {
                  "licenseId":"Apache-2.0",
                  "licenseName":"Apache-2.0"
               }
            ],
            "observedLicenses":[
               {
                  "licenseId":"No-Sources",
                  "licenseName":"No Sources"
               }
            ],
            "effectiveLicenses":[
               {
                  "licenseId":"Apache-2.0",
                  "licenseName":"Apache-2.0"
               }
            ]
         },
         "securityData":{
            "securityIssues":[
               {
                  "source":"cve",
                  "reference":"CVE-2007-3385",
                  "severity":4.3,
                  "url":"http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2007-3385",
                  "threatCategory":"severe"
               },
               {
                  "source":"cve",
                  "reference":"CVE-2007-5333",
                  "severity":5.0,
                  "url":"http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2007-5333",
                  "threatCategory":"severe"
               },
               {
                  "source":"cve",
                  "reference":"CVE-2011-2526",
                  "severity":4.4,
                  "url":"http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2011-2526",
                  "threatCategory":"severe"
               },
               {
                  "source":"cve",
                  "reference":"CVE-2012-0022",
                  "severity":5.0,
                  "url":"http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-0022",
                  "threatCategory":"severe"
               },
               {
                  "source":"osvdb",
                  "reference":"37071",
                  "severity":4.3,
                  "url":"http://osvdb.org/37071",
                  "threatCategory":"severe"
               },
               {
                  "source":"osvdb",
                  "reference":"41435",
                  "severity":5.0,
                  "url":"http://osvdb.org/41435",
                  "threatCategory":"severe"
               },
               {
                  "source":"osvdb",
                  "reference":"73797",
                  "severity":4.4,
                  "url":"http://osvdb.org/73797",
                  "threatCategory":"severe"
               },
               {
                  "source":"osvdb",
                  "reference":"73798",
                  "severity":4.4,
                  "url":"http://osvdb.org/73798",
                  "threatCategory":"severe"
               },
               {
                  "source":"osvdb",
                  "reference":"78573",
                  "severity":5.0,
                  "url":"http://osvdb.org/78573",
                  "threatCategory":"severe"
               }
            ]
         },
         "projectData" : {
            "firstReleaseDate" : "2008-01-24T03:19:17.000-07:00",
            "lastReleaseDate" : "2008-01-24T03:19:17.000-07:00",
            "projectMetadata" : {
               "description" : "The Apache Software Foundation provides support for the Apache community of open-source software projects.\n    The Apache projects are characterized by a collaborative, consensus based development process, an open and\n    pragmatic software license, and a desire to create high quality software that leads the way in its field.\n    We consider ourselves not simply a group of projects sharing a server, but rather a community of developers\n    and users.",
               "organization" : "The Apache Software Foundation"
            },
            "sourceControlManagement" : {
               "scmUrl" : "https://svn.apache.org/repos/asf/maven/pom/tags/apache-4/tomcat-parent/tomcat-util"
            }
         }
      }
   ]
}
```

### Change history for Component Details REST API

## Component Evaluation REST API

The Component Evaluation REST API allows for a single component, or multiple components, to be evaluated against a specific application and the associated policies.

This API uses the following REST resources:

- POST - to submit a component or list of components, as well as the application containing the policies the component(s) will be evaluated against.
- GET - to check the status of the evaluation and retrieve the results when completed.

For the API we provide a step-by-step example using the HTTP client cURL, though any HTTP client tool could be used. In addition, we’ll reference other APIs such as the one required to obtain an application’s internal ID.

### Step 1 - Get Component Information

First, you need to decide which components you want to evaluate. You’ll need a bit of component information in the form of the GAVE (Group, Artifact, Version, and Extension) or the hash for each component you wish to evaluate.

There are a variety of ways to get the GAVE, the most common is to get the information from the repository that houses the component. For example, [The Central Repository](http://search.maven.org/) has the GAVE for all components stored there.

If you wish to use the hash, Sonatype uses `sha1` for all components it processes.

### Step 2 - Get the Application ID

Next, you will need to pick the application you want to evaluate your component against. This begins with obtaining the application’s public ID, which is used to retrieve the internal application ID.

The public ID can be found via the IQ Server GUI by navigating to the respective application and copying the application ID, which is located just below the application name.

This is done using the following GET REST resource from our application API:

```
GET /api/v2/applications?publicId={YourPublicId}
```

Using the cURL command, it would look like this:

```
curl -u admin:admin123 -X GET 'http://localhost:8070/api/v2/applications?publicId=MyApplicationID'
```

If you like, you can also return multiple applications by appending additional &publicId={SomeOtherPublicId} to the command above. Alternatively, if desired, all applications can always be returned by omitting the reference to the public id. This will give the public ID and internal application ID for all applications.

information will be returned (unique to your application). This has been formatted for readability:

```
{
    "applications": [
        {
            "id": "529b7f71bb714eca8955e5d66687ae2c",
            "publicId": "MyApplicationID",
            "name": "MyApplication",
            "organizationId": "bb41817bd3e2403a8a52fe8bcd8fe25a",
            "contactUserName": "NewAppContact",
            "applicationTags": [
                {
                    "id": "9beee80c6fc148dfa51e8b0359ee4d4e",
                    "tagId": "cfea8fa79df64283bd64e5b6b624ba48",
                    "applicationId": "529b7f71bb714eca8955e5d66687ae2c"
                }
            ]
        }
    ]
}
```

From the information returned above, make a note of the ID. This is the internal application ID.

### Step 3 - Submit Component for Evaluation

Alright, by now you should have either the GAVE or truncated hash for your component, as well as the internal application ID. We’ll put this information together using the POST REST resource:

```
POST /api/v2/evaluation/applications/{applicationInternalId}
```

Added to this will be a JSON formatted body (see the [component search REST API's](#UUID-f30aa750-45d4-dd78-8777-d5275998e940) for coordinate format examples):

```
{
"components": 
  [
    {
      "hash": null,
      "componentIdentifier": {
        "format": "maven",
        "coordinates": {
          "artifactId": "commons-fileupload",
          "groupId": "commons-fileupload",
          "version": "1.2.2",
          "extension": "jar"      
        }
      }
    }
  ]
}



```

Together, this should look like this:

```
curl -u admin:admin123 -X POST -H "Content-Type: application/json" -d '{"components": [{"hash": null,"componentIdentifier": {"format": "maven","coordinates": {"artifactId": "commons-fileupload","groupId": "commons-fileupload","version": "1.2.2","extension":"jar"}}}]}' 'http://localhost:8070/api/v2/evaluation/applications/529b7f71bb714eca8955e5d66687ae2c'
```

A successful POST will result in JSON formatted data confirming that the evaluation was submitted.

```
{
   "resultId": "917e0c5e92a646a5b8879a40890078bc",
   "submittedDate": "2015-02-02T10:43:22.975-05:00",
   "applicationId": "529b7f71bb714eca8955e5d66687ae2c",
   "resultsUrl": "api/v2/evaluation/applications/529b7f71bb714eca8955e5d66687ae2c/results/917e0c5e92a646a5b8879a40890078bc"
}
```

Be sure to make note of the result ID and application ID. These will be used to check and retrieve results. If you are following along with cURL, you can simply copy the results URL.

### Together, this will look like:

```
curl -u admin:admin123 -X POST -H "Content-Type: application/json" -d '{"components": [{"packageUrl": "pkg:maven/commmons-fileupload/commons-fileupload@1.2.2?type=jar"}]}' 'http://localhost:8070/api/v2/evaluation/applications/529b7f71bb714eca8955e5d66687ae2c'
```

A successful POST will result in the same JSON formatted confirmation when submitted using the component identifier.

### Step 4 Get Evaluation Results

Now, depending on how many components you evaluated, the IQ Server may need some time to process them. You can check the status and obtain results using the following GET REST Resource:

```
GET /api/v2/evaluation/applications/{applicationInternalId}/results/{resultId}
```

In our example, we’re going to use the resultsURL and as before, cURL:

```
curl -u admin:admin123 -X GET 'http://localhost:8070/api/v2/evaluation/applications/529b7f71bb714eca8955e5d66687ae2c/results/917e0c5e92a646a5b8879a40890078bc'
```

You will receive a 404 status code when the report is not ready. When ready you will receive results similar to those below:

```
{
   "submittedDate": "2015-02-13T18:01:42.082-05:00",
   "evaluationDate": "2015-02-13T18:01:42.084-05:00",
   "applicationId": "529b7f71bb714eca8955e5d66687ae2c",
   "results": [
      {
         "component":{
            "hash": null,
            "packageUrl": "pkg:maven/commons-fileupload/commons-fileupload@1.2.2?type=jar",
            "componentIdentifier": {
               "format": "maven",
               "coordinates": {
                  "artifactId": "commons-fileupload",
                  "extension": "jar",
                  "groupId": "commons-fileupload",
                  "version": "1.2.2"
               }
            },
            "proprietary": false
         },
         "matchState": "exact",
         "catalogDate": "2010-07-29T16:41:12.000-04:00",
         "licenseData": {
            "declaredLicenses": [
               {
                  "licenseId": "Apache-2.0",
                  "licenseName": "Apache-2.0"
               }
            ],
            "observedLicenses": [
               {
                  "licenseId": "Apache-2.0",
                  "licenseName": "Apache-2.0"
               }
            ],
            "effectiveLicenses": [
               {
                  "licenseId": "Apache-2.0",
                  "licenseName": "Apache-2.0"
               }
            ],
            "overriddenLicenses": [

            ],
            "status": "Open"
         },
         "securityData": {
            "securityIssues": [
               {
                  "source": "cve",
                  "reference": "CVE-2013-2186",
                  "severity": 7.5,
                  "status": "Open",
                  "url": "http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2013-2186",
                  "threatCategory": "critical"
               },
               {
                  "source": "osvdb",
                  "reference": "98703",
                  "severity": 7.5,
                  "status": "Open",
                  "url": "http://osvdb.org/98703",
                  "threatCategory": "critical"
               },
               {
                  "source": "cve",
                  "reference": "CVE-2014-0050",
                  "severity": 5.0,
                  "status": "Open",
                  "url": "http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-0050",
                  "threatCategory": "severe"
               },
               {
                  "source": "osvdb",
                  "reference": "102945",
                  "severity": 5.0,
                  "status": "Open",
                  "url": "http://osvdb.org/102945",
                  "threatCategory": "severe"
               }
            ]
         },
         "policyData": {
            "policyViolations": [
               {
                  "policyId": "0ccc3321662d491c86b32554ea84e4e9",
                  "policyName": "Security-High",
                  "threatLevel": 9,
                  "constraintViolations": [
                     {
                        "constraintId": "d2dfc91f3bf4460ba0da3f7201e4adb7",
                        "constraintName": "CVSS >=7 and <10",
                        "reasons": [
                           {
                              "reason": "Found 2 Security Vulnerabilities with Severity >= 7"
                           },
                           {
                              "reason": "Found 4 Security Vulnerabilities with Severity < 10"
                           },
                           {
                              "reason": "Found 4 Security Vulnerabilities with Status OPEN"
                           }
                        ]
                     }
                  ]
               },
               {
                  "policyId": "0f1b57e6788c4e9bb0f65cde3b6e9f1c",
                  "policyName": "Security-Medium",
                  "threatLevel": 7,
                  "constraintViolations": [
                     {
                        "constraintId": "12a71811de694876b51e4c06c10bad76",
                        "constraintName": "CVSS >=4 and <7",
                        "reasons": [
                           {
                              "reason": "Found 4 Security Vulnerabilities with Severity >= 4"
                           },
                           {
                              "reason": "Found 2 Security Vulnerabilities with Severity < 7"
                           },
                           {
                              "reason": "Found 4 Security Vulnerabilities with Status OPEN"
                           }
                        ]
                     }
                  ]
               }
            ]
         }
      }
   ],
   "isError": false,
   "errorMessage": null
}
```

The last bit of information indicates if there were any errors encountered during the evaluation. In this example, there were no errors.

The returned component *hash* value is truncated and is meant to be used as an identifier that can be passed into subsequent REST API calls. It is not intended to be used as a checksum.

## Component Labels REST API

The Component Labels API allows you to manage component labels for applications, organizations, and repositories.

A component label consists of a label, a color, and an optional description.

Valid values for the field color are:

```
light-red, light-green, light-blue,  light-purple, dark-red, dark-green, dark-blue, dark-purple, orange, yellow
```

### Creating Component Labels

1. To create a component label for an application, use a POST request and specify the applicationId.

```
POST /api/v2/labels/application/{applicationId}
```

2. To create component label for an organization, use a POST request and specify the organizationId.

```
POST /api/v2/labels/organization/{organizationId}
```

3. To create a component label for a repository, use a POST request and specify the repositoryId.

```
POST /api/v2/labels/repository/{repositoryId}
```

### Querying Component Labels

1. To retrieve details for component labels for an application, use a `GET` request and specify the application ID.

```
GET /api/v2/labels/application/{applicationId}
```

2. To retrieve details for component labels for an organization, use a `GET` request and specify the organization ID.

```
GET /api/v2/labels/organization/{organizationId}
```

3. To retrieve details for component labels for a repository, use a `GET` request and specify the repository ID.

```
GET /api/v2/labels/repository/{repositoryId}
```

### Updating Component Labels

To update and existing component label for an application, use the PUT request and specify the applicationID

```
PUT /api/v2/labels/application/{applicationId}
```

To update an existing component label for an organization, use the PUT request and specify the organizationID

```
PUT /api/v2/labels/organization/{organizationId}
```

To update an existing component label for a repository, use the PUT request and specify the repositoryId

```
PUT /api/v2/labels/repository/{repositoryId}
```

### Deleting Component Labels

1. To delete an application label, use a `DELETE` request and specify the application Id and label Id.

A component label for an application can be deleted by sending a `DELETE` request to

```
DELETE api/v2/labels/application/{applicationId}/{labelId}
```

2. To delete an organization label, use a `DELETE` request and specify the organization ID and label ID.

```
DELETE /api/v2/labels/organization/{organizationId}/{labelId}
```

3. To delete a repository label, use a `DELETE` request and specify the repository ID and label ID.

```
DELETE /api/v2/labels/repository/{repositoryId}/{labelId}
```

### Assign Component Labels

1. To assign a component label to an application, use the POST request and specify the component hash, label name, and the application ID.

```
POST /api/v2/components/{componentHash}/labels/{labelName}/applications/{applicationId}
```

where componentHash is the sha 1 hash from the source repository, lablelName is an existing label name and applicationId is the internal application ID.

2. To assign a component labels to an organization, use the POST request and specify the component hash, label name, and the organization ID.

```
POST /api/v2/components/{componentHash}/labels/{labelName}/organizations/{organizationId}
```

where componentHash is the sha 1 hash from the source repository, lablelName is an existing label name and organizationId is the internal organization ID.

### Unassign Component Labels

1. To unassign or remove a component label from an application, use the DELETE request and specify the component hash, label name, and internal application ID.

```
DELETE /api/v2/components/{componentHash}/labels/{labelName}/applications/{applicationId}
```

2. To unassign or remove a component label from an organization, use the DELETE request and specify the component hash, label name, and internal organization ID.

```
DELETE /api/v2/components/{componentHash}/labels/{labelName}/organizations/{organizationId}
```

**NOTE:** This operation only deletes the component labels defined at the organization level. Component labels that have been assigned in the context of individual applications within the organization are not affected.

## Component Remediation REST API

The APIs listed on this page provide a way to obtain suggestions for the remediation of policy violations on a per-component basis. The remediation recommendations provided via these APIs are similar to those provided on the Component Details Page version graph. A component can be validated against policies that are either associated with an application or organization.

Remediation Output Types:

The endpoints return the following set of remediation output types:

- **next-no-violations** This type of remediation contains the version of the provided component that does not violate any policies. If no version meets this criteria, this remediation type will not be present in the response. If there is a version that meets this criteria, it will be returned as the recommendation for this remediation type.
- **next-non-failing** This type of remediation contains the version of the provided component that does not fail the build for the specified stageId. So, the recommended version in this remediation type could potentially trigger warnings based on the policies, but would not fail the build. Note that this type of remediation is only returned if the {stageId} parameter is supplied in the endpoint. Similar to next-no-violations remediation type, if no version meets this criteria, this type will not be present in the response. If there is a version that meets this criteria, it will be returned as the recommendation for this remediation type.
- **next-no-violations-with-dependencies** This type of remediation is similar to next-no-violations above but it also guarantees that all the dependencies of the recommended version do not violate any policy. If no version meets this criteria, this remediation type will not be present in the response. If there is a version that meets this criteria, it will be returned as the recommendation for this remediation type.
- **next-non-failing-with-dependencies** This type of remediation is similar to next-non-failing above but it also guarantees that all the dependencies of the recommended version do not fail the build for the specified stageId. So, the recommended version in this remediation type could potentially trigger warnings based on the policies and its dependencies could also potentially trigger warnings based on the policies, but the recommended component version and its dependencies will not fail the build. Note that this type of remediation is only returned if the {stageId} parameter is supplied in the endpoint. If no version meets this criteria, this type will not be present in the response. If there is a version that meets this criteria, it will be returned as the recommendation for this remediation type.

**Note:** The current version will be returned as recommended if it satisfies the recommendation strategy.

### Remediation by Application policy

The following endpoint, relative to IQ Server's base URL, may be invoked to list remediation recommendations for a component based on policies set at the **application** level. This is the most commonly used endpoint which is also leveraged by the component intelligence panel (CIP) version graph.

```
POST /api/v2/components/remediation/application/{applicationInternalId}?stageId={stageId}&identificationSource={identificationSource}&scanId={scanId}
```

**Note:** The stageId query param is optional but is required for the ** remediation types to be returned in the response.

**Note:** The identificationSource and scanId query parameters are optional but are required if you want the remediation result to be based on third-party scan information.

You can use the to obtain the `applicationInternalId` for an application.

With the POST request, you will need to provide the component details in the payload. For help finding components, see . For help with other formats, see .

Here is a sample JSON payload with component information that can be submitted in the POST request body:

```
{
  "componentIdentifier": {
    "format": "maven",
    "coordinates": {
      "artifactId": "tomcat-util",
      "extension": "jar",
      "groupId": "tomcat",
      "version": "5.5.23"
     }
  }
}
```

Assuming a local installation of IQ Server with its default configuration, the following example using the `cURL` tool finds applicable remediation steps for a component:

```
curl -u admin:admin123 -X POST -H "Content-Type: application/json" -d '{"componentIdentifier": {"format":"maven","coordinates": {"artifactId":"tomcat-util","extension":"jar","groupId":"tomcat","version":"5.5.23"}}}' 'http://localhost:8070/api/v2/components/remediation/application/{applicationInternalId}?stageId={stageId}'
```

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

### Remediation by Organization policy

The following endpoint, relative to IQ Server's base URL, may be invoked to list remediation recommendations for a component based on policies set at the **organization** level. This endpoint may prove to be useful in cases where a component needs to be evaluated against the policies set at the organization level.

```
POST /api/v2/components/remediation/organization/{organizationId}?stageId={stageId}&identificationSource={identificationSource}&scanId={scanId}
```

**Note:** The stageId query param is optional but is required for the ** remediation types to be returned in the response.

**Note:** The identificationSource and scanId (or reportId) query parameters are optional but are required if you want the remediation result to be based on third-party scan information. The identificationSource can be obtained from the [Component Details Page](#UUID-c348055a-b083-a26c-6dda-b4cfda3cf2ef) in the UI.

You can use the [Organization REST API](#UUID-2b83db02-df62-d885-19a8-e6ab5c6fe256) to obtain the `organizationId` for an organization.

With the POST request, you will need to provide the component details in the payload. For help finding components, see [Component Search REST API](#UUID-f30aa750-45d4-dd78-8777-d5275998e940) . For help with other formats, see [Formats with the REST API](#UUID-e1088e50-6e44-edf0-d5af-178b1349e7bd) .

Here is a sample JSON payload with component information that can be submitted in the POST request body:

```
{
  "componentIdentifier": {
    "format": "maven",
    "coordinates": {
      "artifactId": "tomcat-util",
      "extension": "jar",
      "groupId": "tomcat",
      "version": "5.5.23"
     }
  }
}
```

Assuming a local installation of IQ Server with its default configuration, the following example uses the `cURL` tool finds applicable remediation steps for a component:

```
curl -u admin:admin123 -X POST -H "Content-Type: application/json" -d '{"componentIdentifier": {"format":"maven","coordinates": {"artifactId":"tomcat-util","extension":"jar","groupId":"tomcat","version":"5.5.23"}}}' 'http://localhost:8070/api/v2/components/remediation/organization/{organizationId}?stageId={stageId}'
```

### Remediation by repository policy

The following endpoint, relative to IQ Server's base URL, may be invoked to list remediation recommendations for a repository component.

```
POST /api/v2/components/remediation/repository/{repositoryId}
```

With the POST request, you will need to provide the component details in the payload. For help finding components, see . For help with other formats, see .

Here is a sample JSON payload with component information that can be submitted in the POST request body:

```
{
  "componentIdentifier": {
    "format": "maven",
    "coordinates": {
      "artifactId": "tomcat-util",
      "extension": "jar",
      "groupId": "tomcat",
      "version": "5.5.23"
     }
  }
}
```

Assuming a local installation of IQ Server with its default configuration, the following example uses the `cURL` tool finds applicable remediation steps for a component:

```
curl -u admin:admin123 -X POST -H "Content-Type: application/json" -d '{"componentIdentifier": {"format":"maven","coordinates": {"artifactId":"tomcat-util","extension":"jar","groupId":"tomcat","version":"5.5.23"}}}' 'http://localhost:8070/api/v2/components/remediation/repository/{repositoryId}'
```

## Component Search REST API

The Component Search API returns the metadata for a component. This API searches application reports for the components specified.

Using GET requests it allows you to retrieve component information such as application ID, application name, report HTML URL, component hash, component coordinates, the highest threat level of the policy violations (for the found component), and dependency information.

Below, we’ve provided an example of the GET request. We’ve done this using the HTTP client cURL. Of course, you could use any HTTP client tool. Additionally, to help demonstrate the use of the API, we’ve broken out the various pieces for this request and provided an example of data that is retrieved.

### Searching for Components

First, make sure your IQ Server is started. Also, as we mentioned, you will need to have evaluated at least one application. With those two things completed, let’s take a look at the GET API.

```
GET /api/v2/search/component
```

Now, in addition to this, you will need to add two parameters - the **stage** , and then add your **search** **parameters** .

### Using Wildcards

The Component Search API supports the use of wildcards when searching using the GAVEC (coordinates). This endpoint follows the same logic as the coordinates policy condition.

## Component Versions REST API

The Component Versions API returns a list of versions for a component. This API method is available via a POST resource:

```
POST api/v2/components/versions
```

In order to use the API you must know the component identifier for the component you wish to find the versions for. A non-exhaustive list of examples for various formats is provided.

### Maven Example

When finding a version for a Maven component, an appropriate Maven component identifier must be used.

```
{
  "format": "maven",
  "coordinates": {
    "artifactId": "tomcat-util",
    "groupId": "tomcat"
  }
}
```

You can use cURL to run this request.

```
curl -u admin:admin123 -X POST -H "Content-Type: application/json" -d '{ "format": "maven", "coordinates": { "artifactId": "tomcat-util", "groupId": "tomcat" } }' 'http://localhost:8070/api/v2/components/versions'
```

### Javascript Example

For Javascript components the a-name (authoritative name) must be used.

```
{
  "format": "a-name",
  "coordinates": {
    "name": "vizion",
    "qualifier" : ""
  }
}
```

You can also use cURL for this request.

```
curl -u admin:admin123 -X POST -H "Content-Type: application/json" -d '{ "format": "a-name", "coordinates": { "name": "vizion", "qualifier": "" } }' 'http://localhost:8070/api/v2/components/versions'
```

### Python Example

For Python components a component identifier appropriate for the PyPI format must be utilized.

```
{
  "format": "pypi",
  "coordinates": {
    "name": "pyOpenSSL"
  }
}
```

This also has a corresponding cURL request.

```
 curl -u admin:admin123 -X POST -H "Content-Type: application/json" -d '{ "format": "pypi", "coordinates": { "name": "pyOpenSSL" } }' 'http://localhost:8070/api/v2/components/versions'
```

### Response

You will receive a response containing a JSON array with the known versions sorted in ascending order. For the Maven example above, you will see something like the following.

```
[
  "3.2.1",
  "3.3.2",
  "4.0.6",
  "4.1.31",
  "4.1.34",
  "4.1.36",
  "5.0.16",
  "5.0.18",
  "5.0.28",
  "5.5.4",
  "5.5.7-alpha",
  "5.5.7",
  "5.5.8-alpha",
  "5.5.9-alpha",
  "5.5.9",
  "5.5.12",
  "5.5.15",
  "5.5.23"
]
```

### Using Package-URL (PURL) Identifiers

This API supports retrieving component versions based on [PURL](https://github.com/package-url/purl-spec) identifiers. When finding a version for a Maven component an appropriate PURL identifier can be used.

```
{
  "packageUrl": "pkg:maven/tomcat/tomcat-util"
}
```

Here is an example cURL to run this request.

```
curl -u admin:admin123 -X POST -H "Content-Type: application/json" -d '{ "packageUrl": "pkg:maven/tomcat/tomcat-util" }' 'http://localhost:8070/api/v2/components/versions'
```

Similarly, for the same Javascript example above, the following cURL command can be used

```
curl -u admin:admin123 -X POST -H "Content-Type: application/json" -d '{ "packageUrl": "pkg:a-name/vizion" }' 'http://localhost:8070/api/v2/components/versions'
```

## Configuration REST API

The Configuration REST API allows users with the System Administrator role or the Edit System Configuration and Users permission, to configure the server.

### API Requests

### IQ Server Connection Properties

Use the following properties to manage connecting to the IQ Server. The IQ Server supports the following solutions: Lifecycle, Developer, SBOM Manager, and Repository Firewall.

### IQ Server Configuration Properties

Use the following properties to manage the IQ Server configuration. The IQ Server supports the following solutions: Lifecycle, Developer, SBOM Manager, and Repository Firewall.

### Lifecycle Properties

Use the following properties to manage the Lifecycle solution-specific configuration.

### Repository Firewall Properties

Use the following properties to manage the Repository Firewall solution-specific configuration.

### List of Supported Properties

## CPE Matching REST API

Use the CPE Matching Configuration REST API to add/set/remove CPE matching configuration to organizations and applications.

### Get CPE Matching Configuration

Returns the current CPE Matching settings for an application or organization.

`View IQ Elements` permissions are required.

```
GET /api/v2/{ownerType}/{internalOwnerId}/configuration/publicSource/cpe
```

- **ownerType** - Type of owner. Allowed values: `application` | `organization` .
- **internalOwnerId** - Internal ID of the application or organization.

Example:

```
curl -i -u <UserToken>:<TokenPassword> \
  -X GET "http://localhost:8070/api/v2/application/3fa85f64e7/configuration/publicSource/cpe"
```

```
{
  "inheritedFromOrganizationName": "finance-services",
  "enabledInParent": true,
  "allowOverride": false,
  "enabled": true
}
```

- **enabled** - `true` if CPE Matching is active for the specified owner.
- **allowOverride** - `true` if child applications may override the setting.
- **enabledInParent** - `true` if CPE Matching is enabled in any parent organization.
- **inheritedFromOrganizationName** - parent organization providing the effective setting, or omitted when not inherited.

### Apply CPE Matching Configuration

Enables or updates CPE Matching for an application or organization.

`Edit IQ Elements` permissions are required.

```
PUT /api/v2/{ownerType}/{internalOwnerId}/configuration/publicSource/cpe
```

- **enabled** - `true` if CPE Matching is active for the specified owner
- **allowOverride** - `true` if child applications may override the setting

Example:

```
curl -i -u <UserToken>:<TokenPassword> \
  -H "Content-Type: application/json" \
  -d '{"allowOverride":false,"enabled":true}' \
  -X PUT "http://localhost:8070/api/v2/application/3fa85f64e7/configuration/publicSource/cpe"
```

```
{
  "allowOverride": false,
  "enabled": true
}
```

## Cross-Stage Policy Violation REST API

A Cross-Stage violation represents an aggregate of time-overlapping but equal policy violations within a given app across all stages. This data allows analysis such as how long it takes to investigate and remove a violation that was found during a stage until it is no longer reported in any stage.

You may use the steps described in to extract a particular policy violation ID you want to track.

### Available Endpoints

Once you have located the desired ID you can use the following endpoints to obtain the information on the cross-stage violation:

### Response Data

Here is the example of a cross-stage violation response from the above endpoints, where the cross-stage violation represents two occurrences of the same violation: build violation and release stage violation.

```
{
    "policyId": "93be2ac23c294d7683ec81d6faaca604",
    "policyName": "Security-Critical",
    "policyViolationId": "fb4c05d6054043ddaf434a71db8384db",
    "threatLevel": 10,
    "constraintViolations": [
        {
            "constraintId": "d0818181e9d342e7b8c7625409f5935e",
            "constraintName": "Critical risk CVSS score",
            "reasons": [
                {
                    "reason": "Found security vulnerability sonatype-2019-0115 with severity >= 9 (severity = 9.8)",
                    "reference": {
                        "type": "SECURITY_VULNERABILITY_REFID",
                        "value": "sonatype-2019-0115"
                    }
                }
            ]
        }
    ],
    "applicationPublicId": "Webgoat",
    "applicationName": "Webgoat",
    "organizationName": "Ex Main",
    "openTime": "2020-06-17T11:32:16.024-05:00",
    "fixTime": null,
    "hash": "37081687a930b9a4a29c",
    "policyThreatCategory": "security",
    "displayName": {
        "parts": [
            {
                "field": "Name",
                "value": "org.webjars jquery"
            },
            {
                "value": " "
            },
            {
                "field": "Version",
                "value": "1.10.2"
            }
        ]
    },
    "componentIdentifier": {
        "format": "a-name",
        "coordinates": {
            "name": "org.webjars jquery",
            "qualifier": "",
            "version": "1.10.2"
        }
    },
    "filename": "jquery-1.10.2.min.js",
    "stageData": {
        "build": {
            "mostRecentEvaluationTime": "2020-06-17T11:32:16.024-05:00",
            "mostRecentScanId": "c6e307ca087b4682998b9298245b74d6",
            "actionTypeId": "fail"
        },
        "stage-release": {
            "mostRecentEvaluationTime": "2020-06-18T11:03:01.933-05:00",
            "mostRecentScanId": "e78e289a664b4b8fb6b969d531fc1dea",
            "actionTypeId": "fail"
        }
    },
    "policyOwner": {
        "ownerId": "ROOT_ORGANIZATION_ID",
        "ownerName": "Root Organization",
        "ownerType": "organization"
    }
}
```

**Note:** If the violated policy no longer exists, policyOwner will have null properties. This can happen after importing new policies.

The policyViolationId is the cross-stage violation Id

The stageData will report the information for stages where the violation was found, including the Ids of the specific scans where it was reported.

The rest of the information returned by the API is analog to the information returned by

## Data Retention Policy REST API

[Data retention policies](#UUID-2b3cfee1-89f1-01d1-3054-80b82081877c) help to limit the disk space consumption of IQ Server by defining what data is obsolete and hence can be removed from the server. The REST API described here allows you to inspect and change the retention policies that are in effect.

### Query Current Retention Policies

By making an HTTP GET request to the following URL relative to IQ Server's base URL the data retention policies for a given organization can be retrieved:

```
GET /api/v2/dataRetentionPolicies/organizations/{organizationId}
```

You use the to locate the organizationId for an organization.

Assuming a local installation of IQ Server with its default configuration, the following example using the `cURL` tool queries the retention policies for the root organization:

```
curl -u admin:admin123 http://localhost:8070/api/v2/dataRetentionPolicies/organizations/ROOT_ORGANIZATION_ID
```

Again, assuming the default configuration, the above request would yield this JSON response payload (formatted here for readability):

```
{
  "applicationReports": {
    "stages": {
      "develop": {
        "inheritPolicy": false,
        "enablePurging": true,
        "maxAge": "3 months"
      },
      "build": {
        "inheritPolicy": false,
        "enablePurging": true,
        "maxAge": "3 months"
      },
      "stage-release": {
        "inheritPolicy": false,
        "enablePurging": true,
        "maxAge": "3 months"
      },
      "release": {
        "inheritPolicy": false,
        "enablePurging": true,
        "maxAge": "10 years"
      },
      "operate": {
        "inheritPolicy": false,
        "enablePurging": true,
        "maxAge": "10 years"
      },
      "continuous-monitoring": {
        "inheritPolicy": false,
        "enablePurging": true,
        "maxAge": "3 months"
      }
    }
  },
  "successMetrics": {
    "inheritPolicy": false,
    "enablePurging": true,
    "maxAge": "1 year"
  }
}
```

For application reports, each stage in the application lifecycle ( `develop` , `build` , etc.) has its own retention policy. A notable exception are application reports that were created by continuous monitoring: They are not subject to the retention policy of whatever stage is being monitored but have their own retention policy under the key `continuous-monitoring` .

Note that the response lists only those stages that the installed product license enables. So you might see fewer entries with your IQ Server than shown in the above example.

A single retention policy for the application reports consists of these fields:

**Note:** There is no priority between the `maxAge` and `maxCount` criteria. If both are set, then you may see the oldest reports that are below `maxAge` being removed because `maxCount` is exceeded, or old reports being deleted because `maxAge` is exceeded even if the number of reports is below `maxCount` .

The retention policy for Success Metrics consists mostly of the same fields as those for application reports:

### Configure Retention Policies

A HTTP PUT request to the same URL when reading the current configuration is used to change the retention policies:

```
PUT /api/v2/dataRetentionPolicies/organizations/{organizationId}
```

The request needs to be accompanied by a JSON payload that has generally the same format as described above. It is however allowed to omit all but one stage from the `stages` map to selectively update only the retention policy for a few stages or to only specify `successMetrics` to update the retention policy for Success Metrics and not application reports.

The next example would update the retention policy of the root organization regarding application reports for the build stage:

```
curl -u admin:admin123 -H "Content-Type: application/json" -X PUT -d '{"applicationReports": {"stages": {"build": {"enablePurging": true, "maxAge": "2 weeks", "maxCount": 100}}}}' http://localhost:8070/api/v2/dataRetentionPolicies/organizations/ROOT_ORGANIZATION_ID
```

Note that when `enablePurging` is `true` , at least one purge criteria, `maxAge` or `maxCount` , needs to be specified.

If the request body is malformed, no changes to the retention policies are carried out and the status code 400 ("Bad Request") is sent back.

**Note:** Purging of obsolete data is done automatically by a background job that runs once day. So enabling purging or setting stricter retention policies does typically not take effect until the next day.

### Limitations of Data Retention Policy REST API

To optimize resource usage for this REST API, IQ Server has a preset limit of purging 5000 reports in one call. If your reports to be purged exceed 5000, and were not purged before, you will have to issue multiple calls to this REST API, to reduce the reports below or equal to the *maxCount* field setting.

IQ Server will automatically apply the maxCount field setting for subsequent purges.

## Feature Configuration REST API

This API allows users with the [System Administrator role,](#UUID-dbc7b586-b425-e5b2-82a5-76c9e16bbcee) or the [Edit System Configuration and Users permission](#UUID-dbc7b586-b425-e5b2-82a5-76c9e16bbcee) to enable/disable certain Nexus IQ Server features.

### Features supported:

The table below shows the features that can be enabled/disabled via this REST API. The "Supported From" column indicates the Sonatype IQ server release that supports the enabling/disabling of each feature using this REST API.

### POST to Enable a Feature

To enable a feature, you can make a POST request to the following path:

### Response:

A successful request yields HTTP status code 204.

If an invalid feature is supplied, or the feature is already enabled, then the request yields a bad request response with HTTP status code 400.

### DELETE to Disable a Feature

To disable a feature, you can make a DELETE request to the following path:

### Response:

A successful request yields HTTP status code 204.

If an invalid feature is supplied, or the feature is already disabled, then the request yields a bad request response with HTTP status code 400.

## Mail REST API

For email-based notifications, configure an SMTP server. The REST API described here allows system administrators to manage that configuration. The base URL must be configured before starting.

### Query Current Mail Configuration

To inspect the currently configured SMTP server, you can make a GET request to the following path:

```
GET /api/v2/config/mail
```

Below is an example request to a local IQ Server using the built-in administrator account and the cURL tool:

```
curl -u admin:admin123 http://localhost:8070/api/v2/config/mail
```

If no mail integration is configured, the request yields HTTP status code 404. Otherwise, a JSON document with the following properties is returned:

### Test Mail Configuration

To test a mail configuration without changing the current mail configuration, you can make a POST request to the following path:

```
POST /api/v2/config/mail/test/{recipientEmail}
```

The request requires a JSON document as a payload, using the same properties described above. The properties `hostname` , `port` and `systemEmail` are required.

The system will send a test mail to the address specified by `recipientEmail` using the mail configuration provided in the JSON document.

If the `password` is specified in the input data, then `passwordIsIncluded` must be set to *true* . If `passwordIsIncluded` is set to *true* and the `password` is not included, then the `password` is null, which means "no password".

For test operations, if the password should be loaded from the mail configuration already stored in IQ Server, then the `password` can be omitted and `passwordIsIncluded` set to false. However, this is allowed only when the `hostname` and `port` match the stored mail configuration. If the `hostname` or `port` is different, then the `password` must be included and `passwordIsIncluded` must be set to *true* . The `passwordIsIncluded` flag is only used for test/update operations and it is not part of the mail configuration itself.

The next example demonstrates such a request:

```
curl -u admin:admin123 -H "Content-Type: application/json" -X POST -d '{"hostname": "smtp.server", "port": 587, "username": "MyUsername", "password": "MySecret", "passwordIsIncluded": true, "startTlsEnabled": true, "systemEmail": "noreply@smtp.server"}' http://localhost:8070/api/v2/config/mail/test/johndoe@example.com
```

A successful test of the configuration is signaled by HTTP status code 204, indicating the email was sent. If any required JSON property is missing or otherwise invalid, HTTP status code 400 is returned.

### Configure Mail Integration

To enable or update the integration with an SMTP server, you can make a PUT request to the following path:

```
PUT /api/v2/config/mail
```

The request requires a JSON document as payload, using the same properties as already described above. The properties `hostname` , `port` and `systemEmail` are required.

If the `password` is specified in the input data, then `passwordIsIncluded` must be set to *true* . If `passwordIsIncluded` is set to *true* and the `password` is not included, then the `password` is null, which means "no password".

For update operations, if the password should remain unchanged, then the `password` can be omitted and `passwordIsIncluded` set to false. However, this is allowed only when the `hostname` and `port` are not changed. If the `hostname` or `port` is changed, then the password must be included and `passwordIsIncluded` must be set to *true* . The `passwordIsIncluded` flag is only used for test/update operations and it is not part of the mail configuration itself.

The next example demonstrates such a request:

```
curl -u admin:admin123 -H "Content-Type: application/json" -X PUT -d '{"hostname": "smtp.server", "port": 587, "username": "MyUsername", "password": "MySecret", "passwordIsIncluded": true, "startTlsEnabled": true, "systemEmail": "noreply@smtp.server"}' http://localhost:8070/api/v2/config/mail
```

A successful update of the configuration is signaled by HTTP status code 204. If any required JSON property is missing or otherwise invalid, HTTP status code 400 is returned.

### Disable Mail Integration

The email configuration can be removed using the delete request:

```
DELETE /api/v2/config/mail
```

For example:

```
curl -u admin:admin123 -X DELETE http://localhost:8070/api/v2/config/mail
```

The request responds with HTTP status code 204 when the email configuration is removed. If no mail server was configured, the HTTP status code 404 is returned instead.

## HTTP Proxy Server Configuration REST API

For IQ Server to be able to connect to other servers via an HTTP proxy server. The REST API described here allows system administrators to manage the HTTP proxy server configuration:

### Query Current HTTP Proxy Server Configuration

To inspect the currently configured HTTP proxy server, you can make a request to the following path:

```
GET /api/v2/config/httpProxyServer
```

Below is an example request to a local IQ Server using the built-in administrator account and the cURL tool:

```
curl -u admin:admin123 http://localhost:8070/api/v2/config/httpProxyServer
```

If no HTTP proxy server is configured, the request yields HTTP status code 404. Otherwise, a JSON document with the following properties is returned:

### Configure HTTP Proxy Server

To enable or update the HTTP proxy server, a PUT request to the aforementioned REST path is used:

```
PUT /api/v2/config/httpProxyServer
```

The request requires a JSON document as payload, using the same properties as already described above. The properties `hostname` and `port` are required.

If the `password` is specified in the input data, then `passwordIsIncluded` must be set to *true* . If `passwordIsIncluded` is set to *true* and the `password` is not included, then the `password` is null, which means "no password".

For update operations, if the password should remain unchanged, then the `password` can be omitted and `passwordIsIncluded` set to false. However, this is allowed only when the `hostname` and `port` are not changed. If the `hostname` or `port` is changed, then the password must be included and `passwordIsIncluded` must be set to *true* . The `passwordIsIncluded` flag is only used for update operations and it is not part of the HTTP proxy server configuration itself.

The next example demonstrates such a request:

```
curl -u admin:admin123 -H "Content-Type: application/json" -X PUT -d '{"hostname": "myproxyserver", "port": 8080, "username": "MyUsername", "password": "MySecret", "passwordIsIncluded": true, "excludeHosts": ["*.example.com", "*.example.org"]}' http://localhost:8070/api/v2/config/httpProxyServer
```

A successful update of the configuration is signaled by HTTP status code 204. If any required JSON property is missing or otherwise invalid, HTTP status code 400 is returned.

### Disable HTTP Proxy Server

If IQ Server does not need an HTTP proxy server, the proxy server configuration can be entirely removed using the request:

```
DELETE /api/v2/config/httpProxyServer
```

For example:

```
curl -u admin:admin123 -X DELETE http://localhost:8070/api/v2/config/httpProxyServer
```

If an HTTP proxy server was configured, the request responds with HTTP status code 204. If no HTTP proxy server was configured to begin with, the HTTP status code 404 is returned instead.

## JIRA Configuration REST API

This REST API endpoint allows anyone with the System Administrator role or the Edit System Configuration and Users permission to manage JIRA configurations for notifications.

**Note:** This REST API endpoint can be used with Jira Cloud, Jira Server, or Jira Data Center. Jira Server and Data Center users are encouraged to use the Sonatype for Jira integration for advanced features.

### JIRA Configuration Properties

### GET the JIRA Configuration

To get the JIRA configuration you can make a GET request to the following path:

```
GET /api/v2/config/jira
```

Below is an example request to a local IQ Server using the built-in administrator account and the cURL tool:

```
curl -u admin:admin123 http://localhost:8070/api/v2/config/jira
```

If no JIRA configuration is saved, then the request yields HTTP status code 404. Otherwise, a JSON response with all the properties described above except for password is returned.

### PUT the JIRA Configuration

To set the JIRA configuration you can make a PUT request to the following path:

```
PUT /api/v2/config/jira
```

The request requires a JSON body as payload.

If the JIRA configuration is being created for the first time, then the url is required and all other properties are optional. Although if supplying credentials, then a username and password must be supplied together.

If the JIRA configuration already exists, then any supplied properties will update their values to the given values.

**Note:** If updating the url for an existing JIRA configuration that has credentials defined, then credentials must also be supplied. These credentials do not have to match the existing credentials but will replace the existing credentials. Supplying a `null` username and `null` password will remove the credentials.

Below is an example request to a local IQ Server using the built-in administrator account and the cURL tool:

```
curl -u admin:admin123 -X PUT -H "Content-Type: application/json" -d '{"url": "http://localhost:8080", "username": "admin@test.com", "password": "admin123", "customFields": {"reporter": {"id": "123:abc-123-abc"}}}' http://localhost:8070/api/v2/config/jira
```

A successful request yields HTTP status code 204. Note that the reporter account id can be obtained from the Jira users api at /rest/api/3/users or from the url of user account profile in Jira.

### DELETE the JIRA Configuration

To delete the JIRA configuration you can make a DELETE request to the following path:

```
DELETE /api/v2/config/jira
```

Below is an example request to a local IQ Server using the built-in administrator account and the cURL tool:

```
curl -u admin:admin123 -X DELETE http://localhost:8070/api/v2/config/jira
```

A successful request yields HTTP status code 204.

## License Legal REST API

This endpoint is only available with the [Advanced Legal Pack](#UUID-d81c430b-4c59-206b-62c0-b6b792f18fea) .

### License Legal Application Report Raw Data

This section of endpoints returns the raw JSON legal data for an application.

### Legal Attribution Report Templates

The legal attribution HTML report can be generated from a template. The template allows the following fields to be configured:

- documentTitle: The title is displayed at the top of the attribution report.
- header: *Optional* header which will be displayed at the top of the attribution report above the title.
- footer: *Optional* footer displayed at the bottom of the report.
- includeTableOfContents: if true a table of contents containing links to components and their licenses will be added to the report.
- includeStandardLicenseTexts: if true, the standard license text will be displayed for components with no License files.
- includeAppendix: if true, the standard license text will be grouped in the report appendix (ignore if includeStandardLicenseTexts if false). If false, the standard license text will appear in each component section.
- RELEASE 136 includeInnerSource: if true, [InnerSource components](#UUID-ca9833c6-2581-80b8-3b57-84dd160adaf6) will be included in the attribution report.
- RELEASE 137 includeSonatypeSpecialLicenses: if true, SonatypeSpecial Licenses (e.g., Generic-Copyleft-Clause, Generic-Liberal-Clause, See-License-Clause, Identity-Clause, etc.) will be included in the attribution report.

Templates can be created, updated, and modified. When generating a report you may also pass in a template identifier to generate a report from the given template.

### Legal Attribution Attribution Report HTML

### GET a License Legal Component Report

To get a License Legal Component Report's raw data you can issue a GET request to the following path

```
GET /api/v2/licenseLegalMetadata/{organization|application}/{ownerId}/component?{componentIdentifier|packageUrl|hash}=...
```

The specified organization or application will determine the license, copyright, notice files, license files, and attribution files overrides (if any). For example, if obligations are resolved at an Organization scope then all components under this Organization will contain these overriden values. Note that the Root Organization can also be specified via the organization id `ROOT_ORGANIZATION_ID` .

For example, to get the license legal component report for an application with id "MyApp" and a component with coordinates "org.apache.httpcomponents : httpclient : 4.1" and hash "93cd011acb220de08b57" you could issue any one of these requests.

```
curl -u admin:admin123 http://localhost:8070/api/v2/licenseLegalMetadata/application/MyApp/component?componentIdentifier=%7B%22format%22:%22maven%22,%22coordinates%22:%7B%22artifactId%22:%22httpclient%22,%22classifier%22:%22%22,%22extension%22:%22jar%22,%22groupId%22:%22org.apache.httpcomponents%22,%22version%22:%224.1%22%7D%7D
```

```
curl -u admin:admin123 http://localhost:8070/api/v2/licenseLegalMetadata/application/MyApp/component?packageUrl=pkg:maven/org.apache.httpcomponents/httpclient@4.1?type=jar
```

```
curl -u admin:admin123 http://localhost:8070/api/v2/licenseLegalMetadata/application/MyApp/component?hash=93cd011acb220de08b57
```

Note that only one of `componentIdentifier` , `packageUrl` , or `hash` , must be specified.

There are also two optional parameters, `identificationSource` specifying the component identification source, and `scanId` specifying the id for the report where the component was identified. Note that the latter is only used with a third party identification source.

For example, to get the license legal component report for an application with id "MyApp" and a component with coordinates "debian-9 : glibc : 2.24-11+deb9u3" identified by a third party scan with id "1c0af74bbbb4474e8b4ac417f94d2692", you could issue this request

```
curl -u admin:admin123 http://localhost:8070/api/v2/licenseLegalMetadata/application/MyApp/component?componentIdentifier=%7B%22format%22:%22debian-9%22,%22coordinates%22:%7B%22name%22:%22glibc%22,%22version%22:%222.24-11+deb9u3%22%7D%7D&identificationSource=Clair&scanId=1c0af74bbbb4474e8b4ac417f94d2692
```

The initial cURL request will produce a JSON response of the following form (some data has been omitted and/or abbreviated for brevity)

```
{
    "component": {
        "packageUrl": "pkg:maven/org.apache.httpcomponents/httpclient@4.1?type=jar",
        "hash": "93cd011acb220de08b57",
        "componentIdentifier": {
            "format": "maven",
            "coordinates": {
                "artifactId": "httpclient",
                "classifier": "",
                "extension": "jar",
                "groupId": "org.apache.httpcomponents",
                "version": "4.1"
            }
        },
        "displayName": "httpclient",
        "licenseLegalData": {
            "declaredLicenses": [
                "See-License-Clause",
                "Apache-UNSPECIFIED"
            ],
            "observedLicenses": [
                "Apache-2.0"
            ],
            "effectiveLicenses": [
                "See-License-Clause",
                "Apache-2.0"
            ],
            "highestEffectiveLicenseThreatGroup": "Liberal",
            "copyrights": [
                {
                    "id": null,
                    "content": "Copyright 2000-2010 Some Auther",
                    "originalContentHash": "sha256Hash",
                    "status": "enabled"
                },
                {
                    "id": 123,
                    "content": "Copyright 1999-2010 The Apache Software Foundation",
                    "originalContentHash": "sha256Hash",
                    "status": "disabled"
                },
                ...
            ],
            "licenseFiles": [
                {
                    "id": null,
                    "relPath": "META-INF/LICENSE.txt",
                    "content": "license file 2 content",
                    "originalContentHash": "sha256Hash",
                    "status": "disabled"
                },
                ...
            ],
            "noticeFiles": [
                {
                    "id": 2,
                    "relPath": "NOTICE.txt",
                    "content": "notice file 1 content",
                    "originalContentHash": "sha256Hash",
                    "status": "enabled"
                },
                ...
            ],
            "obligations": [
                {
                    "name": "Existing Liability",
                    "status": "OPEN"
                },
                {
                    "name": "Inclusion of Copyright",
                    "status": "FULFILLED",
                    "comment": "obligation comment",
                    "ownerId": "ownerId",
                    "lastUpdatedAt": 1615407013073,
                    "lastUpdatedByUsername": "admin"
                },
                ...
            ],
            "sourceLinks": [
                {
                    "id": null,
                    "sourceLink": "https://repo1.maven.org/maven2/org/apache/httpcomponents/httpclient/4.1/httpclient-4.1.jar",
                    "status": "enabled"
                },
                ...
            ]
        }
    },
    "licenseLegalMetadata": [
        {
            "licenseId": "Apache-UNSPECIFIED",
            "licenseName": "Apache",
            "licenseText": null,
            "obligations": []
        },
        {
            "licenseId": "Apache-2.0",
            "licenseName": "Apache-2.0",
            "licenseText": "Apache-2.0 Standard License Text content",
            "obligations": [
                {
                    "name": "Inclusion of License",
                    "obligationTexts": [
                        "You must give any other recipients of the Work or Derivative Works a copy of this License;"
                    ]
                },
                ...
            ],
            "threatGroup": {
                "name": "Liberal",
                "threatLevel": 0
            },
            "isMulti": false
        },
        ...
    ]
}
```

## License Overrides REST API

**Note:** Releases 189 - 190 used the path `api/v2/licenseOverride` for this API. However, in release 191, we have updated the API to match Sonatype's naming convention. As of release 191, this API uses `api/v2/licenseOverrides` (with " `Overrides` " now plural).

Use the endpoints on this page to manage the license overrides for a component.

**Methods Supported:**

- [POST](#UUID-8eadfe3c-ebaa-85d2-fab1-97940929f94f_section-idm33487080012528)
- [GET](#UUID-8eadfe3c-ebaa-85d2-fab1-97940929f94f_section-idm234870829974623)
- [DELETE](#UUID-8eadfe3c-ebaa-85d2-fab1-97940929f94f_section-idm234870847839827)

### Change the License Overrides

You can update the license overrides using the POST method.

**Permissions required:** Change Licenses

```
POST /api/v2/licenseOverrides/{ownerType}/{ownerId}
```

The JSON payload consists of:

**Example:**

```
curl --location 'http://localhost:8070/api/v2/licenseOverrides/application/apptest' \
--header 'Content-Type: application/json' \
--header 'Authorization: Basic <USER_PASS_BASIC_TOKEN>' \
--data-raw '{
    "componentIdentifier": {
        "format": "a-name",
        "coordinates": {
            "name": "@microsoft/applicationinsights-teechannel-js",
            "qualifier": "",
            "version": "3.0.0-beta.2304-07"
        }
    },
    "comment": "This is a comment.",
    "licenseIds": ["123-OSO-MIT-PL-2.0", "42-Unlicense"],
    "status": "OVERRIDDEN"
}'
```

**Response:**

The response contains the updated license overrides *status* and the *licenseOverrideID* as id.

```
{
    "id": "a2449b221c394553865b93d276b0d2fc",
    "ownerId": "f575f8cec94445b29c564e2cec617e7f",
    "comment": "This is a comment.",
    "licenseIds": [
        "42-Unlicense",
        "123-OSO-MIT-PL-2.0"
    ],
    "componentIdentifier": {
        "format": "a-name",
        "coordinates": {
            "name": "@microsoft/applicationinsights-teechannel-js",
            "qualifier": "",
            "version": "3.0.0-beta.2304-07"
        }
    },
    "status": "OVERRIDDEN"
}
```

### Retrieve the Overrides for Component License

Use the GET method to retrieve the license overrides for the component license, by specifying the component identifier.

**Permissions required:** View IQ Elements

```
GET /api/v2/licenseOverrides/{ownerType}/{ownerId}
```

**Example:**

```
curl --location --globoff 'http://localhost:8070/api/v2/licenseOverrides/application/apptest?componentIdentifier=%7B%22format%22%3A%20%22a-name%22%2C%0A%20%20%20%20%20%22coordinates%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%22name%22%3A%20%22%40microsoft%2Fapplicationinsights-teechannel-js%22%2C%0A%20%20%20%20%20%20%20%20%22qualifier%22%3A%20%22%22%2C%0A%20%20%20%20%20%20%20%20%22version%22%3A%20%223.0.0-beta.2304-07%22%0A%20%20%20%20%20%20%7D%0A%20%20%20%7D' \
--header 'Authorization: Basic <BASIC_TOKEN>'
```

**Response**

The response contains details for the overrides that were applied to the component license.

```
{
    "licenseOverridesByOwner": [
        {
            "ownerId": "apptest",
            "ownerName": "apptest",
            "ownerType": "application",
            "licenseOverride": {
                "id": "a2449b221c394553865b93d276b0d2fc",
                "ownerId": "f575f8cec94445b29c564e2cec617e7f",
                "status": "OVERRIDDEN",
                "comment": "This is a comment.",
                "licenseIds": [
                    "123-OSO-MIT-PL-2.0",
                    "42-Unlicense"
                ],
                "componentIdentifier": {
                    "format": "a-name",
                    "coordinates": {
                        "name": "@microsoft/applicationinsights-teechannel-js",
                        "qualifier": "",
                        "version": "3.0.0-beta.2304-07"
                    }
                }
            }
        },
        {
            "ownerId": "86d4db175f67424b99a2a7adc83df79e",
            "ownerName": "org3",
            "ownerType": "organization",
            "licenseOverride": null
        },
        {
            "ownerId": "ROOT_ORGANIZATION_ID",
            "ownerName": "Root Organization",
            "ownerType": "organization",
            "licenseOverride": {
                "id": "f15c58e5636044ceb6ef765a7d2bb35b",
                "ownerId": "ROOT_ORGANIZATION_ID",
                "status": "OVERRIDDEN",
                "comment": "This is a comment.",
                "licenseIds": [
                    "123-OSO-MIT-PL-2.0",
                    "42-Unlicense"
                ],
                "componentIdentifier": {
                    "format": "a-name",
                    "coordinates": {
                        "name": "@microsoft/applicationinsights-teechannel-js",
                        "qualifier": "",
                        "version": "3.0.0-beta.2304-07"
                    }
                }
            }
        }
    ]
}
```

### Delete License Overrides

Use the DELETE method to remove license overrides for a component by specifying the `licenseOverrideID` . The `licenseOverrideID` can be retrieved using the [GET method](#UUID-8eadfe3c-ebaa-85d2-fab1-97940929f94f_N1743620952806) above.

**Permisisons required:** Change Licenses

```
DELETE /api/v2/licenseOverrides/{ownerType}/{ownerId}/{licenseOverrideId}
```

**Example:**

```
curl --location --request DELETE 'http://localhost:8070/api/v2/licenseOverrides/application/apptest/<LICENSE_OVERRIDE_ID>' \
--header 'Authorization: Basic <BASIC_TOKEN>'
```

**Response**

The response code 204 indicates that the license overrides were deleted successfully.

## Product License REST API

### POST to Install a Product License

A System Administrator is required to use this request:

```
POST /api/v2/product/license
```

The POST request must use the `multipart/form-data` content type and must have one name/value pair with "file" as the name and the product license as the value.

For example, using a local installation of IQ Server with its default configuration and assuming the product license is located at `/some/path/license.lic` , a request using the cURL tool would be:

```
curl -u admin:admin123 -F file="@/path/license.lic" http://localhost:8070/api/v2/product/license
```

The "@" symbol is required.

### DELETE to Uninstall a Product License

A System Administrator is required to delete the license.

**Note:** You will not be able to use the IQ Server until a valid license has been installed.

```
DELETE /api/v2/product/license
```

For example, using a local installation with its default configuration, a request using the cURL tool would be:

```
curl -u admin:admin123 -X DELETE http://localhost:8070/api/v2/product/license
```

## Manifest Evaluation REST API

⚠️ **Warning:** This REST API was deprecated in IQ Server Release 126 and removed in IQ Server Release 169. Use instead.

### Request a Manifest Evaluation

```
POST /api/v2/evaluation/applications/{applicationInternalId}/manifestEvaluation
```

```
{
        "stageId": "develop",
        "branchName": "my-test-branch-name"
}
```

```
curl -u admin:admin123 -X POST -H "Content-Type: application/json" -d '{"stageId":"develop","branchName":"my-test-branch-name"}' 'http://localhost:8070/api/v2/evaluation/applications/cb748fb6ff8f4251b40b63edf1cc465c/manifestEvaluation'
```

```
{
        "statusUrl": "api/v2/evaluation/applications/cb748fb6ff8f4251b40b63edf1cc465c/status/accc369749774924baa1d207494c29e1"
}
```

### Check the Status of a Manifest Evaluation Request

```
GET api/v2/evaluation/applications/{applicationInternalId}/status/{statusId}
```

```
curl -u admin:admin123 'http://localhost:8070/api/v2/evaluation/applications/cb748fb6ff8f4251b40b63edf1cc465c/status/accc369749774924baa1d207494c29e1'
```

The response will include one of three possible status values:

```
PENDING, FAILED, COMPLETED
```

```
{
        "status": "PENDING"
}
```

```
{
        "status": "FAILED",
        "reason": "message"
}
```

```
{
        "status": "COMPLETED",
        "reportHtmlUrl": "ui/links/application/cb748fb6ff8f4251b40b63edf1cc465c/report/affdb6b964a64f0bad2db7170c7560dc",
        "embeddableReportHtmlUrl": "ui/links/application/cb748fb6ff8f4251b40b63edf1cc465c/report/affdb6b964a64f0bad2db7170c7560dc/embeddable",
        "reportPdfUrl": "ui/links/application/cb748fb6ff8f4251b40b63edf1cc465c/report/affdb6b964a64f0bad2db7170c7560dc/pdf",
        "reportDataUrl": "api/v2/applications/cb748fb6ff8f4251b40b63edf1cc465c/reports/affdb6b964a64f0bad2db7170c7560dc"
}
```

## Policy Violation REST API

Use this REST API to access unfixed policy violation data gathered during the evaluation of applications.

**Note:** The Policy Violations REST API only retrieves non-fixed violations.

### Permissions Required:

View IQ Elements

### Methods Supported:

### Pre-requisite: Get the policy metadata

To access policy violation information you need the identifier for the policy.

```
GET /api/v2/policies/
```

Example:

```
curl -u admin:admin123 -X GET 'http://localhost:8070/api/v2/policies'
```

The list of policies is returned in JSON format. The policy IDs will be unique to your instance.

```
{
    "policies": [
        {
            "id": "6984017845c645b0ad0c95401ad4f17d",
            "name": "My Application Policy",
            "ownerId": "36d7e629462a4038b581488c347959bc",
            "ownerType": "APPLICATION",
            "threatLevel": 5,
            "policyType": "quality"
        },
    ]
}
```

### GET all active violations of a policy

Using the policy ID from above, you can query the complete list of active, non-fixed violations for that policy.

```
GET /api/v2/policyViolations?p=policyID
```

Example:

```
curl -u admin:admin123 -X GET 'http://localhost:8070/api/v2/policyViolations?p=6984017845c645b0ad0c95401ad4f17d'
```

Parameters `openTimeAfter` and `openTimeBefore` are supported to filter the results.

Both are optional, and they can be used together or independently. The accepted format is YYYY-MM-DD .

```
curl -u admin:admin123 -X GET 'http://localhost:8070/api/v2/policyViolations?p=6984017845c645b0ad0c95401ad4f17d&openTimeAfter=2020-01-01&openTimeBefore=2020-06-31'
```

Sample response:

```
{
   "applicationViolations":[
      {
         "application":{
            "id":"529b7f71bb714eca8955e5d66687ae2c",
            "publicId":"MyAppID1",
            "name":"MyApplications",
            "organizationId":"36d7e629462a4038b581488c347959bc",
            "contactUserName":null
         },
         "policyViolations":[
            {
               "policyId":"6984017845c645b0ad0c95401ad4f17d",
               "policyName":"Security-High",
               "policyViolationId":"020613b2521b4aeb9ee0d8a0adfd6f2d",
               "stageId":"build",
               "reportId":"c0ddefc4512f42d0bcbe29029e2be117"
               "reportUrl":"ui/links/application/MyAppID1/report/c0ddef
               c4512f42d0bcbe29029e2be117",
               "openTime": "2020-04-27T13:37:57.264+0000",
               "threatLevel":9,
               "constraintViolations":[
                  {
                     "constraintId":"19011de290b147a38c820ad7bd5c653d",
                     "constraintName":"CVSS >=7 and <10",
                     "reasons":[
                        {
                           "reason":"Found 2 Security Vulnerabilities with Severity >= 7"
                        },
                        {
                           "reason":"Found 4 Security Vulnerabilities with Severity < 10"
                        },
                        {
                           "reason":"Found 4 Security Vulnerabilities with Status OPEN"
                        }
                     ]
                  }
               ],
               "component":{
                  "hash":"384faa82e193d4e4b054",
                  "componentIdentifier":{
                     "format":"maven",
                     "coordinates":{
                        "artifactId":"tomcat-util",
                        "classifier":"",
                        "extension":"jar",
                        "groupId":"tomcat",
                        "version":"5.5.23"
                     }
                  },
                  "packageUrl":"pkg:maven/tomcat/tomcat-util@5.5.23?type=jar",
                  "proprietary":false
               }
            }
         ]
      }
   ]
}
```

### GET all violations of a policy by specifying *type*

Using the policy ID(s) from above, you can specify the `type` of violations ( *active* , *legacy* or *waived* ).

Example 1:

```
curl -u admin:admin123 -X GET 'http://localhost:8070/api/v2/policyViolations?p=448e1122e9b148cdb71a2935967c657b&type=legacy'
```

Example 2:

If more than one type is specified, the request is considered as an OR operation. In the example below, the response will contain policy violations that are waived OR are legacy violations.

```
curl -u admin:admin123 -X GET 'http://localhost:8070/api/v2/policyViolations?p=448e1122e9b148cdb71a2935967c657b&type=legacy&type=waived'
```

Example 3:

```
curl -u admin:admin123 -X GET 'http://localhost:8070/api/v2/policyViolations?p=448e1122e9b148cdb71a2935967c657b&type=legacy&type=waived&type=active'
```

### Sample Response

```
{
  "applicationViolations": [
      {
          "application": {
              "id": "0ed38f7107a242788b05b7a82a61d549",
              "publicId": "refactor-app",
              "name": "refactor-app",
              "organizationId": "3abf9898bfe4452ca38cc561122d776b",
              "contactUserName": null
          },
          "policyViolations": [
              {
                  "policyId": "448e1122e9b148cdb71a2935967c657b",
                  "policyName": "Security-Medium",
                  "policyViolationId": "5790f2e02d4f4dd38148047bde597824",
                  "openTime": "2025-02-12T17:25:15.179+0000",
                  "waiveTime": "2025-02-12T17:25:15.179+0000",
                  "fixTime": "2025-02-12T17:25:15.179+0000",
                  "legacyViolationTime": "2025-02-12T17:25:15.179+0000",
                  "threatLevel": 7,
                  "constraintViolations": [
                      {
                          "constraintId": "2b36001e89554960a44a2a3ddcb29ed6",
                          "constraintName": "Medium risk CVSS score",
                          "reasons": [
                              {
                                  "reason": "Found security vulnerability sonatype-2020-0103 with severity >= 4 (severity = 5.3)",
                                  "reference": {
                                      "type": "SECURITY_VULNERABILITY_REFID",
                                      "value": "sonatype-2020-0103"
                                  }
                              },
                              {
                                  "reason": "Found security vulnerability sonatype-2020-0103 with severity < 7 (severity = 5.3)",
                                  "reference": {
                                      "type": "SECURITY_VULNERABILITY_REFID",
                                      "value": "sonatype-2020-0103"
                                  }
                              }
                          ]
                      }
                  ],
                  "stageId": "build",
                  "reportId": "5d661036e325411dae640176f20e2a30",
                  "reportUrl": "ui/links/application/refactor-app/report/5d661036e325411dae640176f20e2a30",
                  "component": {
                      "packageUrl": "pkg:maven/io.netty/netty-codec-http@4.1.33.Final?type=jar",
                      "hash": "ad557dffc0777b1b2455",
                      "componentIdentifier": {
                          "format": "maven",
                          "coordinates": {
                              "artifactId": "netty-codec-http",
                              "classifier": "",
                              "extension": "jar",
                              "groupId": "io.netty",
                              "version": "4.1.33.Final"
                          }
                      },
                      "displayName": "io.netty : netty-codec-http : 4.1.33.Final",
                      "proprietary": false
                  },
                  "isWaived": true,
                  "isLegacy": false
              },
              {
                  "policyId": "448e1122e9b148cdb71a2935967c657b",
                  "policyName": "Security-Medium",
                  "policyViolationId": "93fa5486685a46218126a9c25afec2f8",
                  "openTime": "2025-02-06T17:40:57.474+0000",
                  "threatLevel": 7,
                  "constraintViolations": [
                      {
                          "constraintId": "2b36001e89554960a44a2a3ddcb29ed6",
                          "constraintName": "Medium risk CVSS score",
                          "reasons": [
                              {
                                  "reason": "Found security vulnerability CVE-2024-31033 with severity >= 4 (severity = 5.9)",
                                  "reference": {
                                      "type": "SECURITY_VULNERABILITY_REFID",
                                      "value": "CVE-2024-31033"
                                  }
                              },
                              {
                                  "reason": "Found security vulnerability CVE-2024-31033 with severity < 7 (severity = 5.9)",
                                  "reference": {
                                      "type": "SECURITY_VULNERABILITY_REFID",
                                      "value": "CVE-2024-31033"
                                  }
                              }
                          ]
                      }
                  ],
                  "stageId": "build",
                  "reportId": "5d661036e325411dae640176f20e2a30",
                  "reportUrl": "ui/links/application/refactor-app/report/5d661036e325411dae640176f20e2a30",
                  "component": {
                      "packageUrl": "pkg:maven/io.jsonwebtoken/jjwt@0.9.1?type=jar",
                      "hash": "54d2abfc3e63a28824d3",
                      "componentIdentifier": {
                          "format": "maven",
                          "coordinates": {
                              "artifactId": "jjwt",
                              "classifier": "",
                              "extension": "jar",
                              "groupId": "io.jsonwebtoken",
                              "version": "0.9.1"
                          }
                      },
                      "displayName": "io.jsonwebtoken : jjwt : 0.9.1",
                      "proprietary": false
                  },
                  "isWaived": false,
                  "isLegacy": true
              },
                {
                  "policyId": "448e1122e9b148cdb71a2935967c657b",
                  "policyName": "Security-Medium",
                  "policyViolationId": "2c5bacbb8a0146e7baa641b470939817",
                  "openTime": "2025-02-06T17:40:57.474+0000",
                  "threatLevel": 7,
                  "constraintViolations": [
                      {
                          "constraintId": "2b36001e89554960a44a2a3ddcb29ed6",
                          "constraintName": "Medium risk CVSS score",
                          "reasons": [
                              {
                                  "reason": "Found security vulnerability sonatype-2018-0601 with severity >= 4 (severity = 6.1)",
                                  "reference": {
                                      "type": "SECURITY_VULNERABILITY_REFID",
                                      "value": "sonatype-2018-0601"
                                  }
                              },
                              {
                                  "reason": "Found security vulnerability sonatype-2018-0601 with severity < 7 (severity = 6.1)",
                                  "reference": {
                                      "type": "SECURITY_VULNERABILITY_REFID",
                                      "value": "sonatype-2018-0601"
                                  }
                              }
                          ]
                      }
                  ],
                  "stageId": "build",
                  "reportId": "5d661036e325411dae640176f20e2a30",
                  "reportUrl": "ui/links/application/refactor-app/report/5d661036e325411dae640176f20e2a30",
                  "component": {
                      "packageUrl": "pkg:maven/org.asciidoctor/asciidoctorj@2.5.13?type=jar",
                      "hash": "03f9fba7ef863a251600",
                      "componentIdentifier": {
                          "format": "maven",
                          "coordinates": {
                              "artifactId": "asciidoctorj",
                              "classifier": "",
                              "extension": "jar",
                              "groupId": "org.asciidoctor",
                              "version": "2.5.13"
                          }
                      },
                      "displayName": "org.asciidoctor : asciidoctorj : 2.5.13",
                      "proprietary": false
                  },
                  "isWaived": true,
                  "isLegacy": true
              },
          ]
      }
  ]
}
```

**Response Description**

## Policy Waiver REST API

This API can be used to create, retrieve, update and delete policy waivers.

**NOTE: The GET Method currently does not support retrieval of expired waivers.**

### GET

### POST

### PUT to Update an Existing Waiver

```
PUT api/v2/policyWaivers/{ownerType: application|organization|repository|repository_manager|repository_container}/{ownerId}/{policyWaiverId}
```

The scope of the waiver is determined by the parameters *ownerType* and *ownerID* . Possible values for *ownerType* and *owner ID* are application, organization, root organization, repository or repository container.

Use the GET method above to retrieve the *policyWaiverID* .

Specify the *policyWaiverID* in the PUT request, for the policy waiver to be updated.

**NOTE:** Updating *matcherStrategy* is currently unsupported.

**Examples:**

1. Update a policy waiver with id 3458b438595740119043dd49a1a146df that applies to the root org.

```
curl -u admin:admin123 -X PUT http://localhost:8070/api/v2/policyWaivers/organization/ROOT_ORGANIZATION_ID/3458b438595740119043dd49a1a146df
```

2. JSON payload:

```
{
    "comment": "updating expiryTime",
    "expiryTime": "2025-12-26T00:00:00.000+0000",
    "matcherStrategy": "ALL_COMPONENTS",
    "waiverReasonId": "5810538dfd311b6da17557360a10dc64"
}
```

**Response:**

**HTTP status 204** : (No content) to indicate that the waiver has been successfully updated.

### DELETE

```
DELETE /api/v2/policyWaivers/{ownerType: application|organization|repository|repository_container}/{ownerId}/{policyWaiverId}
```

The scope of the waiver is determined by the parameters ownerType andownerID. Possible values for ownerType and owner ID are application, organization, root organization, repository or repository container.

**Examples:**

1. Delete a policy waiver with id 3458b438595740119043dd49a1a146df that applies to the root org

```
curl -u admin:admin123 -X DELETE http://localhost:8070/api/v2/policyWaivers/organization/ROOT_ORGANIZATION_ID/3458b438595740119043dd49a1a146df
```

2. Delete a policy waiver with id d248b438595740119043dd49a1a146da for an application having application id 787c2e3dc8e745c48743926251eef00b:

```
curl -u admin:admin123 -X DELETE http://localhost:8070/api/v2/policyWaivers/application/787c2e3dc8e745c48743926251eef00b/d248b438595740119043dd49a1a146da
```

3. Delete a policy waiver with id 2338b438595740119043dd49a1a146dc in the repository container

```
curl -u admin:admin123 -X DELETE http://localhost:8070/api/v2/policyWaivers/repository_container/REPOSITORY_CONTAINER_ID/2338b438595740119043dd49a1a146dc
```

4. Delete a policy waiver with id e678b438595740119043dd49a1a14645 in the repository having id 6891f877e254428c991d9be640a32969:

```
curl -u admin:admin123 -X DELETE http://localhost:8070/api/v2/policyWaivers/repository/6891f877e254428c991d9be640a32969/e678b438595740119043dd49a1a14645
```

**Response:**

No response/content indicates that the waiver has been successfully deleted.

### Change history for Policy Waiver REST API v2

### Other Related REST APIs

## Policy Waiver Request REST API

This API can be used to create, retrieve, update and delete policy waivers requests.

**Methods Supported:**

- GET
- POST
- PUT

### GET Existing Waiver Requests

```
GET api/v2/policyWaiverRequests/{ownerType: application|organization|repository|repository_manager|repository_container}/{ownerId}/{policyWaiverRequestId}
```

Use this method to retrieve the existing waiver requests by specifying the *policyWaiverRequestID* .

**Example:**

```
curl -u admin:admin123 -X GET http://localhost:8070/api/v2/policyWaiverRequests/application/68cc2742858f4bf7888bc34f9e95ad3d/3058258b647e45c8ad25b6b150297cca
```

**Response:**

The response contains the waiver request details for the specified *policywaiverRequestId* .

```
{
  "policyName": "Security-High",
  "scopeOwnerType": "application",
  "scopeOwnerName": "Pub Test",
  "noteToReviewer": "Optional notes giving more details to the reviewer.",
  "componentIdentifier": {
    "coordinates": {
      "version": "1.0.0",
      "name": "croupier"
    },
    "format": "pub"
  },
  "scopeOwnerId": "68cc2742858f4bf7888bc34f9e95ad3d",
  "status": "REQUESTED",
  "policyId": "42cd0281505a4271a3cd46836e267665",
  "requesterName": "Admin BuiltIn",
  "policyWaiverRequestId": "3058258b647e45c8ad25b6b150297cca",
  "policyWaiverReasonId": "9b704ef5bc064fc29d7fe08a251ee9a6",
  "vulnerabilityId": "CVE-2022-23540",
  "associatedPackageUrl": "pkg:pub/croupier@1.0.0",
  "constraintFactsJson": "[{\"constraintId\":\"7f1d44a9e880487ab6a818be8c5962a4\",\"constraintName\":\"High risk CVSS score\",\"operatorName\":\"AND\",\"conditionFacts\":[{\"conditionTypeId\":\"SecurityVulnerabilitySeverity\",\"conditionIndex\":0,\"summary\":\"Security Vulnerability Severity >= 7\",\"reason\":\"Found security vulnerability CVE-2022-23540 with severity >= 7 (severity = 7.6)\",\"reference\":{\"value\":\"CVE-2022-23540\",\"type\":\"SECURITY_VULNERABILITY_REFID\"},\"triggerJson\":\"{\\\"conditionIndex\\\":0,\\\"trigger\\\":{\\\"refId\\\":\\\"CVE-2022-23540\\\",\\\"severity\\\":7.6}}\"},{\"conditionTypeId\":\"SecurityVulnerabilitySeverity\",\"conditionIndex\":1,\"summary\":\"Security Vulnerability Severity < 9\",\"reason\":\"Found security vulnerability CVE-2022-23540 with severity < 9 (severity = 7.6)\",\"reference\":{\"value\":\"CVE-2022-23540\",\"type\":\"SECURITY_VULNERABILITY_REFID\"},\"triggerJson\":\"{\\\"conditionIndex\\\":1,\\\"trigger\\\":{\\\"refId\\\":\\\"CVE-2022-23540\\\",\\\"severity\\\":7.6}}\"}]}]",
  "constraintFacts": [
    {
      "conditionFacts": [
        {
          "triggerJson": "{\"conditionIndex\":0,\"trigger\":{\"refId\":\"CVE-2022-23540\",\"severity\":7.6}}",
          "reason": "Found security vulnerability CVE-2022-23540 with severity >= 7 (severity = 7.6)",
          "summary": "Security Vulnerability Severity >= 7",
          "conditionIndex": 0,
          "conditionTypeId": "SecurityVulnerabilitySeverity",
          "reference": {
            "value": "CVE-2022-23540",
            "type": "SECURITY_VULNERABILITY_REFID"
          }
        },{
          "triggerJson": "{\"conditionIndex\":1,\"trigger\":{\"refId\":\"CVE-2022-23540\",\"severity\":7.6}}",
          "reason": "Found security vulnerability CVE-2022-23540 with severity < 9 (severity = 7.6)",
          "summary": "Security Vulnerability Severity < 9",
          "conditionIndex": 1,
          "conditionTypeId": "SecurityVulnerabilitySeverity",
          "reference": {
            "value": "CVE-2022-23540",
            "type": "SECURITY_VULNERABILITY_REFID"
          }
        }],
      "operatorName": "AND",
      "constraintId": "7f1d44a9e880487ab6a818be8c5962a4",
      "constraintName": "High risk CVSS score"
    }],
  "comment": "Optional comments explaining why the policy violation is waived.",
  "displayName": {
    "parts": [
      {
        "value": "croupier",
        "field": "Name"
      },{
        "value": " : "
      },{
        "value": "1.0.0",
        "field": "Version"
      }],
    "name": "croupier"
  },
  "hash": "794b85b341e1fa0a149a",
  "matcherStrategy": "EXACT_COMPONENT",
  "policyViolationId": "a0d65d48322c4056b1bd3d79ba7e696b",
  "reasonText": "Acknowledged violation",
  "expiryTime": "2025-12-26T00:00:00.000+0000",
  "requesterId": "admin",
  "requestTime": "2025-05-30T15:00:51.438+0000",
  "expireWhenRemediationAvailable": false
}
```

### POST for New Policy Waiver Request

```
POST api/v2/policyWaiverRequests/{ownerType: application|organization|repository|repository_manager|repository_container}/{ownerId}/policyViolation/{policyViolationId}
```

Use this method to create a new waiver request for a policy violation at the application, organization, or repository level.

The details for the policy waiver request can be included in the JSON payload as below

**Payload Example:**

```
{
    "matcherStrategy": "ALL_COMPONENTS",
    "expiryTime": "2025-12-26T00:00:00.000+0000",
    "expireWhenRemediationAvailable": false,
    "waiverReasonId": "9b704ef5bc064fc29d7fe08a251ee9a6",
    "comment": "Optional comments explaining why the policy violation is waived.",
    "noteToReviewer": "Optional notes giving more details to the reviewer."
}
```

**Example:**

```
curl -u admin:admin123 -X POST -H "Content-Type: application/json" -d '{"matcherStrategy": "ALL_COMPONENTS", "expiryTime": "2025-12-26T00:00:00.000+0000", "expireWhenRemediationAvailable": false, "waiverReasonId": "9b704ef5bc064fc29d7fe08a251ee9a6", "comment": "Optional comments explaining why the policy violation is waived.", "noteToReviewer": "Optional notes giving more details to the reviewer."}' http://localhost:8070/api/v2/policyWaiverRequests/application/68cc2742858f4bf7888bc34f9e95ad3d/policyViolation/a0d65d48322c4056b1bd3d79ba7e696b
```

**Response:**

```
{
  "policyName": "Security-High",
  "scopeOwnerType": "application",
  "scopeOwnerName": "Test App",
  "noteToReviewer": "Optional notes giving more details to the reviewer.",
  "componentIdentifier": null,
  "scopeOwnerId": "68cc2742858f4bf7888bc34f9e95ad3d",
  "status": "REQUESTED",
  "policyId": "42cd0281505a4271a3cd46836e267665",
  "requesterName": "Admin BuiltIn",
  "policyWaiverRequestId": "3058258b647e45c8ad25b6b150297cca",
  "policyWaiverReasonId": "9b704ef5bc064fc29d7fe08a251ee9a6",
  "vulnerabilityId": "CVE-2022-23540",
  "associatedPackageUrl": null,
  "constraintFactsJson": "[{\"constraintId\":\"7f1d44a9e880487ab6a818be8c5962a4\",\"constraintName\":\"High risk CVSS score\",\"operatorName\":\"AND\",\"conditionFacts\":[{\"conditionTypeId\":\"SecurityVulnerabilitySeverity\",\"conditionIndex\":0,\"summary\":\"Security Vulnerability Severity >= 7\",\"reason\":\"Found security vulnerability CVE-2022-23540 with severity >= 7 (severity = 7.6)\",\"reference\":{\"value\":\"CVE-2022-23540\",\"type\":\"SECURITY_VULNERABILITY_REFID\"},\"triggerJson\":\"{\\\"conditionIndex\\\":0,\\\"trigger\\\":{\\\"refId\\\":\\\"CVE-2022-23540\\\",\\\"severity\\\":7.6}}\"},{\"conditionTypeId\":\"SecurityVulnerabilitySeverity\",\"conditionIndex\":1,\"summary\":\"Security Vulnerability Severity < 9\",\"reason\":\"Found security vulnerability CVE-2022-23540 with severity < 9 (severity = 7.6)\",\"reference\":{\"value\":\"CVE-2022-23540\",\"type\":\"SECURITY_VULNERABILITY_REFID\"},\"triggerJson\":\"{\\\"conditionIndex\\\":1,\\\"trigger\\\":{\\\"refId\\\":\\\"CVE-2022-23540\\\",\\\"severity\\\":7.6}}\"}]}]",
  "constraintFacts": [
    {
      "conditionFacts": [
        {
          "triggerJson": "{\"conditionIndex\":0,\"trigger\":{\"refId\":\"CVE-2022-23540\",\"severity\":7.6}}",
          "reason": "Found security vulnerability CVE-2022-23540 with severity >= 7 (severity = 7.6)",
          "summary": "Security Vulnerability Severity >= 7",
          "conditionIndex": 0,
          "conditionTypeId": "SecurityVulnerabilitySeverity",
          "reference": {
            "value": "CVE-2022-23540",
            "type": "SECURITY_VULNERABILITY_REFID"
          }
        },{
          "triggerJson": "{\"conditionIndex\":1,\"trigger\":{\"refId\":\"CVE-2022-23540\",\"severity\":7.6}}",
          "reason": "Found security vulnerability CVE-2022-23540 with severity < 9 (severity = 7.6)",
          "summary": "Security Vulnerability Severity < 9",
          "conditionIndex": 1,
          "conditionTypeId": "SecurityVulnerabilitySeverity",
          "reference": {
            "value": "CVE-2022-23540",
            "type": "SECURITY_VULNERABILITY_REFID"
          }
        }],
      "operatorName": "AND",
      "constraintId": "7f1d44a9e880487ab6a818be8c5962a4",
      "constraintName": "High risk CVSS score"
    }],
  "comment": "Optional comments explaining why the policy violation is waived.",
  "displayName": null,
  "hash": null,
  "matcherStrategy": "ALL_COMPONENTS",
  "policyViolationId": "a0d65d48322c4056b1bd3d79ba7e696b",
  "reasonText": "Acknowledged violation",
  "expiryTime": "2025-12-26T00:00:00.000+0000",
  "requesterId": "admin",
  "requestTime": "2025-05-30T15:00:51.438+0000",
  "expireWhenRemediationAvailable": false
}
```

### POST to Review (Approve or Reject) a Policy Waiver Request

```
POST api/v2/policyWaiverRequests/{ownerType: application|organization|repository|repository_manager|repository_container}/{ownerId}/review/{policyWaiverRequestId}
```

Use this method to approve or reject a request for a policy violation waiver.

The details for the policy waiver request that is being approved or rejected, can be included in the JSON payload as below:

**Payload :**

**Example:**

```
curl -u admin:admin123 -X POST -H "Content-Type: application/json" -d '{"status": "APPROVED", "matcherStrategy": "EXACT_COMPONENT", "expiryTime": "2025-12-26T00:00:00.000+0000", "expireWhenRemediationAvailable": false, "waiverReasonId": "9b704ef5bc064fc29d7fe08a251ee9a6", "comment": "Optional comments explaining why the policy violation is waived."}' http://localhost:8070/api/v2/policyWaiverRequests/application/68cc2742858f4bf7888bc34f9e95ad3d/review/3058258b647e45c8ad25b6b150297cca
```

**Response:**

Note that the status field is APPROVED for this waiver request.

```
{
  "policyName": "Security-High",
  "scopeOwnerType": "application",
  "scopeOwnerName": "Test App",
  "noteToReviewer": "Optional notes giving more details to the reviewer.",
  "componentIdentifier": {
    "coordinates": {
      "version": "1.0.0",
      "name": "croupier"
    },
    "format": "pub"
  },
  "scopeOwnerId": "68cc2742858f4bf7888bc34f9e95ad3d",
  "status": "APPROVED",
  "policyId": "42cd0281505a4271a3cd46836e267665",
  "requesterName": "Admin BuiltIn",
  "policyWaiverRequestId": "3058258b647e45c8ad25b6b150297cca",
  "policyWaiverReasonId": "9b704ef5bc064fc29d7fe08a251ee9a6",
  "vulnerabilityId": "CVE-2022-23540",
  "reviewerName": "Admin BuiltIn",
  "associatedPackageUrl": "pkg:pub/croupier@1.0.0",
  "constraintFactsJson": "[{\"constraintId\":\"7f1d44a9e880487ab6a818be8c5962a4\",\"constraintName\":\"High risk CVSS score\",\"operatorName\":\"AND\",\"conditionFacts\":[{\"conditionTypeId\":\"SecurityVulnerabilitySeverity\",\"conditionIndex\":0,\"summary\":\"Security Vulnerability Severity >= 7\",\"reason\":\"Found security vulnerability CVE-2022-23540 with severity >= 7 (severity = 7.6)\",\"reference\":{\"value\":\"CVE-2022-23540\",\"type\":\"SECURITY_VULNERABILITY_REFID\"},\"triggerJson\":\"{\\\"conditionIndex\\\":0,\\\"trigger\\\":{\\\"refId\\\":\\\"CVE-2022-23540\\\",\\\"severity\\\":7.6}}\"},{\"conditionTypeId\":\"SecurityVulnerabilitySeverity\",\"conditionIndex\":1,\"summary\":\"Security Vulnerability Severity < 9\",\"reason\":\"Found security vulnerability CVE-2022-23540 with severity < 9 (severity = 7.6)\",\"reference\":{\"value\":\"CVE-2022-23540\",\"type\":\"SECURITY_VULNERABILITY_REFID\"},\"triggerJson\":\"{\\\"conditionIndex\\\":1,\\\"trigger\\\":{\\\"refId\\\":\\\"CVE-2022-23540\\\",\\\"severity\\\":7.6}}\"}]}]",
  "reviewerId": "admin",
  "constraintFacts": [
    {
      "conditionFacts": [
        {
          "triggerJson": "{\"conditionIndex\":0,\"trigger\":{\"refId\":\"CVE-2022-23540\",\"severity\":7.6}}",
          "reason": "Found security vulnerability CVE-2022-23540 with severity >= 7 (severity = 7.6)",
          "summary": "Security Vulnerability Severity >= 7",
          "conditionIndex": 0,
          "conditionTypeId": "SecurityVulnerabilitySeverity",
          "reference": {
            "value": "CVE-2022-23540",
            "type": "SECURITY_VULNERABILITY_REFID"
          }
        },{
          "triggerJson": "{\"conditionIndex\":1,\"trigger\":{\"refId\":\"CVE-2022-23540\",\"severity\":7.6}}",
          "reason": "Found security vulnerability CVE-2022-23540 with severity < 9 (severity = 7.6)",
          "summary": "Security Vulnerability Severity < 9",
          "conditionIndex": 1,
          "conditionTypeId": "SecurityVulnerabilitySeverity",
          "reference": {
            "value": "CVE-2022-23540",
            "type": "SECURITY_VULNERABILITY_REFID"
          }
        }],
      "operatorName": "AND",
      "constraintId": "7f1d44a9e880487ab6a818be8c5962a4",
      "constraintName": "High risk CVSS score"
    }],
  "comment": "Optional comments explaining why the policy violation is waived.",
  "displayName": {
    "parts": [
      {
        "value": "croupier",
        "field": "Name"
      },{
        "value": " : "
      },{
        "value": "1.0.0",
        "field": "Version"
      }],
    "name": "croupier"
  },
  "hash": "794b85b341e1fa0a149a",
  "matcherStrategy": "EXACT_COMPONENT",
  "policyViolationId": "a0d65d48322c4056b1bd3d79ba7e696b",
  "reasonText": "Acknowledged violation",
  "expiryTime": "2025-12-26T00:00:00.000+0000",
  "requesterId": "admin",
  "requestTime": "2025-05-30T15:00:51.438+0000",
  "expireWhenRemediationAvailable": false
}
```

### PUT to Update a Waiver Request

```
PUT api/v2/policyWaiverRequests/{ownerType: application|organization|repository|repository_manager|repository_container}/{ownerId}/{policyWaiverRequestId}
```

Use this method to update an existing waiver request, by specifying the waiver request Id.

The details to be updated for the policy waiver request can be included in the JSON payload.

See [description for the JSON payload](#UUID-456e8faa-6b04-bf57-72fd-d06626a33d72_N1748884029713) .

**Payload Example:**

```
{
    "matcherStrategy": "EXACT_COMPONENT",
    "expiryTime": "2025-12-26T00:00:00.000+0000",
    "expireWhenRemediationAvailable": false,
    "waiverReasonId": "9b704ef5bc064fc29d7fe08a251ee9a6",
    "comment": "Optional comments explaining why the policy violation is waived.",
    "noteToReviewer": "Optional notes giving more details to the reviewer."
}
```

**Example:**

```
curl -u admin:admin123 -X PUT -H "Content-Type: application/json" -d '{"matcherStrategy": "EXACT_COMPONENT", "expiryTime": "2025-12-26T00:00:00.000+0000", "expireWhenRemediationAvailable": false, "waiverReasonId": "9b704ef5bc064fc29d7fe08a251ee9a6", "comment": "Optional comments explaining why the policy violation is waived.", "noteToReviewer": "Optional notes giving more details to the reviewer."}' http://localhost:8070/api/v2/policyWaiverRequests/application/68cc2742858f4bf7888bc34f9e95ad3d/3058258b647e45c8ad25b6b150297cca
```

**Response:**

```
{
  "policyName": "Security-High",
  "scopeOwnerType": "application",
  "scopeOwnerName": "Test App",
  "noteToReviewer": "Optional notes giving more details to the reviewer.",
  "componentIdentifier": {
    "coordinates": {
      "version": "1.0.0",
      "name": "croupier"
    },
    "format": "pub"
  },
  "scopeOwnerId": "68cc2742858f4bf7888bc34f9e95ad3d",
  "status": "REQUESTED",
  "policyId": "42cd0281505a4271a3cd46836e267665",
  "requesterName": "Admin BuiltIn",
  "policyWaiverRequestId": "3058258b647e45c8ad25b6b150297cca",
  "policyWaiverReasonId": "9b704ef5bc064fc29d7fe08a251ee9a6",
  "vulnerabilityId": "CVE-2022-23540",
  "associatedPackageUrl": "pkg:pub/croupier@1.0.0",
  "constraintFactsJson": "[{\"constraintId\":\"7f1d44a9e880487ab6a818be8c5962a4\",\"constraintName\":\"High risk CVSS score\",\"operatorName\":\"AND\",\"conditionFacts\":[{\"conditionTypeId\":\"SecurityVulnerabilitySeverity\",\"conditionIndex\":0,\"summary\":\"Security Vulnerability Severity >= 7\",\"reason\":\"Found security vulnerability CVE-2022-23540 with severity >= 7 (severity = 7.6)\",\"reference\":{\"value\":\"CVE-2022-23540\",\"type\":\"SECURITY_VULNERABILITY_REFID\"},\"triggerJson\":\"{\\\"conditionIndex\\\":0,\\\"trigger\\\":{\\\"refId\\\":\\\"CVE-2022-23540\\\",\\\"severity\\\":7.6}}\"},{\"conditionTypeId\":\"SecurityVulnerabilitySeverity\",\"conditionIndex\":1,\"summary\":\"Security Vulnerability Severity < 9\",\"reason\":\"Found security vulnerability CVE-2022-23540 with severity < 9 (severity = 7.6)\",\"reference\":{\"value\":\"CVE-2022-23540\",\"type\":\"SECURITY_VULNERABILITY_REFID\"},\"triggerJson\":\"{\\\"conditionIndex\\\":1,\\\"trigger\\\":{\\\"refId\\\":\\\"CVE-2022-23540\\\",\\\"severity\\\":7.6}}\"}]}]",
  "constraintFacts": [
    {
      "conditionFacts": [
        {
          "triggerJson": "{\"conditionIndex\":0,\"trigger\":{\"refId\":\"CVE-2022-23540\",\"severity\":7.6}}",
          "reason": "Found security vulnerability CVE-2022-23540 with severity >= 7 (severity = 7.6)",
          "summary": "Security Vulnerability Severity >= 7",
          "conditionIndex": 0,
          "conditionTypeId": "SecurityVulnerabilitySeverity",
          "reference": {
            "value": "CVE-2022-23540",
            "type": "SECURITY_VULNERABILITY_REFID"
          }
        },{
          "triggerJson": "{\"conditionIndex\":1,\"trigger\":{\"refId\":\"CVE-2022-23540\",\"severity\":7.6}}",
          "reason": "Found security vulnerability CVE-2022-23540 with severity < 9 (severity = 7.6)",
          "summary": "Security Vulnerability Severity < 9",
          "conditionIndex": 1,
          "conditionTypeId": "SecurityVulnerabilitySeverity",
          "reference": {
            "value": "CVE-2022-23540",
            "type": "SECURITY_VULNERABILITY_REFID"
          }
        }],
      "operatorName": "AND",
      "constraintId": "7f1d44a9e880487ab6a818be8c5962a4",
      "constraintName": "High risk CVSS score"
    }],
  "comment": "Optional comments explaining why the policy violation is waived.",
  "displayName": {
    "parts": [
      {
        "value": "croupier",
        "field": "Name"
      },{
        "value": " : "
      },{
        "value": "1.0.0",
        "field": "Version"
      }],
    "name": "croupier"
  },
  "hash": "794b85b341e1fa0a149a",
  "matcherStrategy": "EXACT_COMPONENT",
  "policyViolationId": "a0d65d48322c4056b1bd3d79ba7e696b",
  "reasonText": "Acknowledged violation",
  "expiryTime": "2025-12-26T00:00:00.000+0000",
  "requesterId": "admin",
  "requestTime": "2025-05-30T15:00:51.438+0000",
  "expireWhenRemediationAvailable": false
}
```

## Auto Policy Waiver REST API

The Auto Policy Waiver REST API allows you to manage the configuration of [Automated Waivers](#UUID-9ed00015-ccb9-9b92-4b3b-9f9967513617) for an organization or application.

Using this REST API you can create a new Automated Waiver configuration or retrieve, update or delete an existing Automated Waiver configuration.

**Permissions Required** : Waive Policy Violations

**Methods supported:**

- GET
- POST
- PUT
- DELETE

### GET Existing Automated Waivers

```
GET /api/v2/autoPolicyWaivers/{ownerType: application|organization}/{ownerId}
```

Use this method to retrieve the configuration of all Automated Waivers for the specified *ownerType* and *ownerId* .

**Example:**

To retrieve the Automated Waiver configuration details for an organization, the field ownerType is *organization* , followed by the *organizationId* .

```
curl -X GET -u admin:admin123 http://localhost:8070/api/v2/autoPolicyWaivers/organization/<organizationId>
```

To retrieve the Automated Waiver configuration details for a specific auto-waiver, you can specify the *autoPolicyWaiverId* as below:

```
GET /{ownerType: application|organization}/{ownerId}/{autoPolicyWaiverId}
```

**Response:**

The response contains a list of Automated Waivers grouped by *autoPolicyWaiverId* .

```
{
    "autoPolicyWaiverId": "8dae7860ca9d4e26a91371ab156e2080",
    "ownerId": "5b6c0dde3b0e415487dd0c92220d105c",
    "ownerType": "application",
    "ownerName": "waiver-test",
    "publicId": "waiver-test",
    "threatLevel": 7,
    "reachable": null,
    "pathForward": true,
    "creatorId": "admin",
    "creatorName": "Admin BuiltIn",
    "createTime": "2024-12-11T03:06:41.985+0000"
}
```

If a security policy violation is configured for Automated Waivers both at the organization level and application level, there response retrieves the details for the automated waiver applied at the application level.

To retrieve the status of an existing Automated Waiver for an organization or application, you can send a request as below:

```
curl -X GET -u admin:admin123 http://localhost:8070/api/v2/autoPolicyWaivers/organization/<organizationId>/status
```

**Response:**

The response contains the status for the specified Automated Waiver.

### POST New Automated Waiver

```
POST /api/v2/autoPolicyWaivers/{ownerType: application|organization}/{ownerId}
```

Use this method to create a new waiver request for a policy violation at the application, organization, or repository level.

**Example:**

```
curl -X POST -u admin:admin123 -H "Content-Type: application/json" -d '{"threatLevel": "5", "pathForward": "true", "reachable": "false"}' http://localhost:8070/api/v2/autoPolicyWaivers/organization/9cee7b6754f04d10a168fa8e32a265f0
```

**Response:**

The response contains the configuration details for the Automated Waiver created.

```
{
    "autoPolicyWaiverId": "bd68235902a448428abb9ee789899f91",
    "ownerId": "5b6c0dde3b0e415487dd0c92220d105c",
    "threatLevel": 9,
    "reachable": false,
    "pathForward": true,
    "creatorId": "admin",
    "creatorName": "Admin BuiltIn",
    "createTime": "2024-12-26T16:23:10.073+0000"
}
```

### PUT To Update An Existing Automated Waiver

```
PUT /api/v2/autoPolicyWaivers/{ownerType: application|organization}/{ownerId}/{autoPolicyWaiverId}
```

Use this method to update an existing configuration of an Automated Waiver by providing the *applicationId/organizationId* and the *autoPolicyWaiverId*

**Example:**

```
curl -X PUT -u admin:admin123 -H "Content-Type: application/json" -d '{"threatLevel": "1", "pathForward": "true", "reachable": "false", "autoPolicyWaiverId": "ead479f981d94d37958539f56642c365", "ownerId": "9cee7b6754f04d10a168fa8e32a265f0"}'
```

**Response:**

The response contains details of the updated Automated Waiver.

```
{
    "autoPolicyWaiverId": "bd68235902a448428abb9ee789899f91",
    "ownerId": "5b6c0dde3b0e415487dd0c92220d105c",
    "threatLevel": 9,
    "reachable": false,
    "pathForward": true,
    "creatorId": "admin",
    "creatorName": "Admin BuiltIn",
    "createTime": "2024-12-26T16:23:10.073+0000"
}
```

### DELETE An Existing Automated Waiver

```
DELETE /api/v2/autoPolicyWaivers/{ownerType: application|organization}/{ownerId}/{autoPolicyWaiverId}
```

Use this method to delete and an existing configuration for Automated Waiver by providing the *autoPolicyWaiverId* .

**Example:**

```
curl -X DELETE -u admin:admin123 http://localhost:8070/api/v2/autoPolicyWaivers/organization/<organizationId>/<autoPolicyWaiverId>
```

A response code 204 indicates that the Automated Waiver was deleted successfully.

## Exclude Auto Policy Waiver REST API

Use this REST API to manage exclusion of [Automated Waivers](#UUID-9ed00015-ccb9-9b92-4b3b-9f9967513617) on security policy violations.

Automated Waivers, when configured at the organization or application level are applied to security policy violations that meet the configuration criteria. You can [exclude or remove an Automated Waiver](#UUID-9ed00015-ccb9-9b92-4b3b-9f9967513617_section-idm234694214606936) on a specific security policy violation, even if it is configured at the organization or application level.

**Permisisons Required:** Waive Policy Violations

**Methods Supported:**

- GET
- POST
- DELETE

### GET Existing Exclusions on Automated Waivers

```
GET /api/v2/autoPolicyWaiverExclusions/{ownerType: application|organization}/{ownerId}/{autoPolicyWaiverId}
```

Use this method to retrieve existing exclusion or removals of Automated Waivers that were created on policy violations, by providing the *autoPolicyWaiverId* .

**Example:**

To retrieve all Exclusions of the Automated Waiver with *autoPolicyWaiverId* waiver-789 for the applicationId 8a57c492dab64068ba6aa0c4a724e0db on page number one with 10 results per page:

```
curl -X GET -u admin:admin123 http://localhost:8070/api/v2/autoPolicyWaiverExclusions/application/8a57c492dab64068ba6aa0c4a724e0db/waiver-789?page=1&pageSize=10 \
--header 'Accept: application/json'
```

**Response:**

A successful response (response code 200) contains a list of Exclusions ( *autoPolicyWaiverExclusionId* ).

### POST New Exclusion on Automated Waiver

```
POST /api/v2/autoPolicyWaiverExclusions/{ownerType: application|organization}/{ownerId}
```

Use this method to revoke/remove Automated Waiver from a policy violation. Successful execution of this request will result in creating an *Exclusion* .

An *Exclusion* will exclude this policy violation from Automated Waiver, even if the parent application or organization has been configured for Automated Waivers.

The request body consists of the following input parameters:

**Example:**

To create an exclusion on an Automated Waiver (with autoPolicyWaiverId *waiver-789* ), created on a policy violation (with policyViolationId *policy-567* , corresponding to the evaluation (with scanID *scan-001* ) of the application (with applicationPublicID *app-123* .

```
curl -X POST -u admin:admin123 http://localhost:8070/api/v2/autoPolicyWaiverExclusions/application/8a57c492dab64068ba6aa0c4a724e0db \
--header 'Content-Type: application/json' \
--data '{
	"applicationPublicId": "app-123",
	"ownerId": "8a57c492dab64068ba6aa0c4a724e0db",
	"policyViolationId": "policy-567",
	"autoPolicyWaiverId": "waiver-789",
	"scanId": "scan-001",
	"matchStrategy": "POLICY_VIOLATION"
}'
```

**Response:**

An Exclusion for the Automated Waiver is created. The response includes details on the policy violation on which the Automated Waiver was applied.

```
{
    "autoPolicyWaiverExclusionId": "a6afe407442e479091dcd317ea30d550",
    "ownerId": "5b6c0dde3b0e415487dd0c92220d105c",
    "creatorId": "admin",
    "creatorName": "Admin BuiltIn",
    "createTime": "2024-12-26T16:45:59.614+0000",
    "autoPolicyWaiverId": "36e5c493f6ee4aacb568766395372ef8",
    "hash": "47e0b80099d6109ef199",
    "scanId": "0647de7c9fa84959b8a832ee4a2524f9",
    "componentMatchStrategy": "POLICY_VIOLATION",
    "policyViolationId": "80de81ee5f064cc4aee492ad5a8c971d",
    "threatLevel": 7,
    "policyName": "Security-Medium",
    "componentDisplayName": "com.nulab-inc : zxcvbn : 1.9.0",
    "componentIdentifier": {
        "format": "maven",
        "coordinates": {
            "artifactId": "zxcvbn",
            "classifier": "",
            "extension": "jar",
            "groupId": "com.nulab-inc",
            "version": "1.9.0"
        }
    },
    "vulnerabilityIdentifiers": "sonatype-2023-2654",
    "policyId": "9f7aaee3df89410eb2ba8c07c4965b35",
    "constraintFacts": [
        {
            "constraintId": "1ec7c74b2b65414d85bf1767f9efc8fd",
            "constraintName": "Medium risk CVSS score",
            "operatorName": "AND",
            "conditionFacts": [
                {
                    "conditionTypeId": "SecurityVulnerabilitySeverity",
                    "conditionIndex": 0,
                    "summary": "Security Vulnerability Severity >= 4",
                    "reason": "Found security vulnerability sonatype-2023-2654 with severity >= 4 (severity = 5.3)",
                    "reference": {
                        "value": "sonatype-2023-2654",
                        "type": "SECURITY_VULNERABILITY_REFID"
                    },
                    "triggerJson": "{\"conditionIndex\":0,\"trigger\":{\"refId\":\"sonatype-2023-2654\",\"severity\":5.3}}"
                },
                {
                    "conditionTypeId": "SecurityVulnerabilitySeverity",
                    "conditionIndex": 1,
                    "summary": "Security Vulnerability Severity < 7",
                    "reason": "Found security vulnerability sonatype-2023-2654 with severity < 7 (severity = 5.3)",
                    "reference": {
                        "value": "sonatype-2023-2654",
                        "type": "SECURITY_VULNERABILITY_REFID"
                    },
                    "triggerJson": "{\"conditionIndex\":1,\"trigger\":{\"refId\":\"sonatype-2023-2654\",\"severity\":5.3}}"
                }
            ]
        }
    ]
}
```

### DELETE Exclusion of Automated Waiver

```
DELETE /api/v2/autoPolicyWaiverExclusions/{ownerType: application|organization}/{ownerId}/{autoPolicyWaiverId}/{autoPolicyWaiverExclusionId}
```

Use this method to delete an *Exclusion* of Automated Waiver on a policy violation.

When an *Exclusion* is deleted, the policy violation is eligible for Automated Waivers again. Automated Waiver will be applied to this policy violation after a re-evaluation.

**Example:**

```
curl -X DELETE -u admin:admin123 http://localhost:8070/api/v2/autoPolicyWaiverExclusions/application/8a57c492dab64068ba6aa0c4a724e0db/waiver-789/exclusion-001
```

**Response:**

A response code 204 indicates that the *Exclusion* is deleted. The policy violation is once again eligible for Automated Waiver. The Automated Waiver will be applied after the next evaluation.

## Applicable Waivers REST API

This API provides a way to obtain all waivers (including Automated Waivers, see [endpoint for Automated Waiver](#UUID-90c6acd1-194a-5679-b6a6-edc74fc12e75_section-idm234701337289215) ) that are applicable to a particular policy violation. A waiver is considered applicable to a given violation if the following conditions apply:

The API can be accessed via the following endpoint as a GET request, relative to IQ Server's base URL.

```
GET /api/v2/policyViolations/{policyViolationId}/applicableWaivers
```

**Note:** The Policy Violation ID can be obtained by [Policy Violation REST API](#UUID-4a859fd3-2931-252c-9ff5-84a5a62b6c51) or [Report Related REST API](#UUID-af2cb0fe-38c7-fccd-b351-eb0cfd73cb8e) .

Assuming a local installation of IQ Server with its default configuration, the following example using `cURL` lists waivers that apply to a policy violation:

```
curl -u admin:admin123 -X GET -H "Content-Type: application/json" 'http://localhost:8070/api/v2/policyViolations/{policyViolationId}/applicableWaivers'
```

The response returned by this API contains two sets of waivers, one set containing active waivers and another containing expired waivers, that apply to the provided violation. Each of the waiver items contains several details regarding the waivers as described in the table below.

## Similar Waivers REST API

You can use this REST API to retrieve all similar waivers that could potentially be applied a given policy violation.

A waiver is considered "similar" if it meets all of the following conditions:

- The user has *View* permission for the waiver, i.e. *View* permission on the organization or application that the waiver is scoped to.
- The waiver is created for the same policy.
- The waiver is applicable to the current component, either by being an exact waiver, applicable to any version of the same component or by being applicable to “All components”.
- The expiration date of the waiver is later than the current date.
- The waiver is not already applicable to the policy violation.

For **security violations** only, a waiver is considered "similar" if the vulnerabilityId (CVE or Sonatype Id) matches the vulnerabilityId of the security violation.

## Component Waivers REST API

**Note:** All repository reports must be re-evaluated in order to include the most accurate policy waiver information used by this API.

The Component Waivers API focuses on existing policy waivers by component. The waivers can be at any scope (app, org, root org, repository, or all repositories). Waivers are listed for each stage to fully detail all the waivers for an application. Stages can carry duplicate waivers, but this accurately reflects every waiver in which a component is in one stage and not another. For repository waivers the only applicable stage is the proxy stage.

### Requesting Component Waivers

To list the component waivers:

```
GET api/v2/reports/components/waivers
```

A sample request to list the component waivers is done with the following command:

```
curl -u admin:admin123 -X GET http://localhost:8070/api/v2/reports/components/waivers
```

This API currently supports filtering by component format/ecosystem. To retrieve waivers only for components in a particular ecosystem, for example maven, add a "format" query parameter to the URL as follows:

```
GET api/v2/reports/components/waivers?format=maven

```

### Response Description

The server will respond with JSON that groups waivers by application components and repository components. The waived application violations will be listed per stage and include the waiver details. Similarly, the waived repository violations will be listed in the proxy stage and include waiver details.

Here is a brief outline of the response which describes the high-level object composition. For the full response details continue to the Response Sample.

**Response Outline**

```
{
  "applicationWaivers": [
    {
      "application": {},
      "stages": [
        {
          "stageId": "build",
          "componentPolicyViolations": [
            {
              "component": {},
              "waivedPolicyViolations": [
                {
                  "policyWaiver": {
                    "policyWaiverId": "e8f43ba30718456eadad6f0616f4c68e",
                    "comment": "temporary waiver",
                    "isObsolete": false,
                    "createTime": "2019-10-16T20:52:27.659+0000",
                    "expiryTime": "2019-10-23T00:00:00.000+0000",
                    "reasonId": "Not reachable",
                    "policyWaiverReasonId": "policyWaiverReasonId",
                    "scopeOwnerType": "root_organization",
                    "scopeOwnerId": "ROOT_ORGANIZATION_ID",
                    "scopeOwnerName": "Root Organization",
                    "hash": "1249e25aebb15358bedd",
                    "policyId": "775a6e88799040c5bb2dd8f020124d07",
                    "creatorId": "authorizedUser",
                    "creatorName": "Authorized User",
                    "matcherStrategy": "EXACT_COMPONENT",
                    "associatedPackageUrl": "pkg:maven/commons-beanutils/commons-beanutils@1.8.3?type=jar",
                    "componentIdentifier": {
                      "format": "maven",
                      "coordinates": {
                        "artifactId": "commons-beanutils",
                        "extension": "jar",
                        "groupId": "commons-beanutils",
                        "version": "1.8.3"
                      }
                    },
                    "displayName": {
                      "parts": [
                        {
                          "field": "Group",
                          "value": "commons-beanutils"
                        },
                        {
                          "value": " : "
                        },
                        {
                          "field": "Artifact",
                          "value": "commons-beanutils"
                        },
                        {
                          "value": " : "
                        },
                        {
                          "field": "Version",
                          "value": "1.8.3"
                        }
                      ],
                      "name": "commons-beanutils"
                    }
                  }
                }
              ]
            }
          ]
        },
        {
          "stageId": "release",
          "componentPolicyViolations": [
            {
              "component": {},
              "waivedPolicyViolations": [
                {
                  "policyWaiver": {
                    "comment": "The waiver cannot be found.  Please re-evaluate.",
                    "isObsolete": true
                  }
                }
              ]
            }
          ]
        }
      ]
    }
  ],
  "repositoryWaivers": [
    {
      "repository": {},
      "stages": [
        {
          "stageId": "proxy",
          "componentPolicyViolations": [
            {
              "component": {},
              "waivedPolicyViolations": [
                {
                  "policyWaiver": {
                    "policyWaiverId": "e8f43ba30718456eadad6f0616f4c68e",
                    "comment": "temporary waiver",
                    "isObsolete": false,
                    "createTime": "2019-10-16T20:52:27.659+0000",
                    "scopeOwnerType": "root_organization",
                    "scopeOwnerId": "ROOT_ORGANIZATION_ID",
                    "scopeOwnerName": "Root Organization",
                    "hash": "1249e25aebb15358bedd",
                    "policyId": "775a6e88799040c5bb2dd8f020124d07",
                    "creatorId": "authorizedUser",
                    "creatorName": "Authorized User",
                    "matcherStrategy": "EXACT_COMPONENT",
                    "associatedPackageUrl": "pkg:maven/commons-beanutils/commons-beanutils@1.8.4?type=jar",
                    "componentIdentifier": {
                      "format": "maven",
                      "coordinates": {
                        "artifactId": "commons-beanutils",
                        "extension": "jar",
                        "groupId": "commons-beanutils",
                        "version": "1.8.4"
                      }
                    },
                    "displayName": {
                      "parts": [
                        {
                          "field": "Group",
                          "value": "commons-beanutils"
                        },
                        {
                          "value": " : "
                        },
                        {
                          "field": "Artifact",
                          "value": "commons-beanutils"
                        },
                        {
                          "value": " : "
                        },
                        {
                          "field": "Version",
                          "value": "1.8.4"
                        }
                      ],
                      "name": "commons-beanutils"
                    }
                  }
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}
```

### Sample Response

A sample response returned by the API:

**Sample Response**

```
{
  "applicationWaivers": [
      {
          "application": {
              "id": "0d3fa305cb8d4ff4b9442d29816cf24c",
              "publicId": "application",
              "name": "Application - TestApp",
              "organizationId": "e40aed6067cc431491d42154c1257ed6",
              "contactUserName": null
          },
          "stages": [
              {
                  "stageId": "build",
                  "componentPolicyViolations": [
                      {
                          "component": {
                              "packageUrl": "pkg:maven/commons-beanutils/commons-beanutils@1.8.3?type=jar",
                              "hash": "686ef3410bcf4ab8ce7f",
                              "componentIdentifier": {
                                  "format": "maven",
                                  "coordinates": {
                                      "artifactId": "commons-beanutils",
                                      "classifier": "",
                                      "extension": "jar",
                                      "groupId": "commons-beanutils",
                                      "version": "1.8.3"
                                  }
                              },
                              "displayName": "commons-beanutils : commons-beanutils : 1.8.3"
                          },
                          "waivedPolicyViolations": [
                              {
                                  "policyId": "d378f2c0bb2d404bbec04cd5f894188b",
                                  "policyName": "Security-High",
                                  "policyViolationId": "5e02da4a230049feb08da590eceb3258",
                                  "threatLevel": 9,
                                  "constraintViolations": [
                                      {
                                          "constraintId": "6b68cdbe13884c779e44d643062b4b1c",
                                          "constraintName": "High risk CVSS score",
                                          "reasons": [
                                              {
                                                  "reason": "Found security vulnerability CVE-2014-0114 with severity >= 7 (severity = 7.5)",
                                                  "reference": {
                                                      "type": "SECURITY_VULNERABILITY_REFID",
                                                      "value": "CVE-2014-0114"
                                                  }
                                              },
                                              {
                                                  "reason": "Found security vulnerability CVE-2014-0114 with severity < 9 (severity = 7.5)",
                                                  "reference": {
                                                      "type": "SECURITY_VULNERABILITY_REFID",
                                                      "value": "CVE-2014-0114"
                                                  }
                                              }
                                          ]
                                      }
                                  ],
                                  "policyWaiver": {
                                      "policyWaiverId": "9fc1ee3f2761458380d2135ef01135f4",
                                      "comment": "",
                                      "createTime": "2022-10-07T21:49:00.051+0000",
                                      "expiryTime": "2022-10-22T04:59:59.999+0000",
                                      "reasonText": "Not exploitable",
                                      "policyWaiverReasonId": "f6990a32cd8d4ea78853ca829d948927",
                                      "isObsolete": false,
                                      "scopeOwnerType": "organization",
                                      "scopeOwnerId": "e40aed6067cc431491d42154c1257ed6",
                                      "scopeOwnerName": "MyOrg",
                                      "hash": "686ef3410bcf4ab8ce7f",
                                      "policyId": "d378f2c0bb2d404bbec04cd5f894188b",
                                      "vulnerabilityId": "CVE-2014-0114",
                                      "creatorId": "admin",
                                      "creatorName": "Admin BuiltIn",
                                      "matcherStrategy": "EXACT_COMPONENT",
                                      "associatedPackageUrl": "pkg:maven/commons-beanutils/commons-beanutils@1.8.3?type=jar",
                                      "componentIdentifier": {
                                          "format": "maven",
                                          "coordinates": {
                                              "artifactId": "commons-beanutils",
                                              "extension": "jar",
                                              "groupId": "commons-beanutils",
                                              "version": "1.8.3"
                                          }
                                      },
                                      "displayName": {
                                          "parts": [
                                              {
                                                  "field": "Group",
                                                  "value": "commons-beanutils"
                                              },
                                              {
                                                  "value": " : "
                                              },
                                              {
                                                  "field": "Artifact",
                                                  "value": "commons-beanutils"
                                              },
                                              {
                                                  "value": " : "
                                              },
                                              {
                                                  "field": "Version",
                                                  "value": "1.8.3"
                                              }
                                          ],
                                          "name": "commons-beanutils"
                                      }
                                  }
                              }
                          ]
                      },
                      {
                          "component": {
                              "packageUrl": "pkg:maven/org.sonatype.nexus/nexus-rest-client@3.25.1-01?classifier=sources&type=jar",
                              "hash": "3ef19d8647bc8031ee94",
                              "componentIdentifier": {
                                  "format": "maven",
                                  "coordinates": {
                                      "artifactId": "nexus-rest-client",
                                      "classifier": "sources",
                                      "extension": "jar",
                                      "groupId": "org.sonatype.nexus",
                                      "version": "3.25.1-01"
                                  }
                              },
                              "displayName": "org.sonatype.nexus : nexus-rest-client : jar : sources : 3.25.1-01"
                          },
                          "waivedPolicyViolations": [
                              {
                                  "policyId": "a9f5f3450375455b8335e02a1ee222db",
                                  "policyName": "Component-Similar",
                                  "policyViolationId": "4b8e59f540424081965533a668b568ba",
                                  "threatLevel": 7,
                                  "constraintViolations": [
                                      {
                                          "constraintId": "c6b8ac4472d24f29bfa8a1d79f28653e",
                                          "constraintName": "Unknown modification to component",
                                          "reasons": [
                                              {
                                                  "reason": "Match state was 'Similar'",
                                                  "reference": null
                                              },
                                              {
                                                  "reason": "Coordinates were org.sonatype.nexus : nexus-rest-client : jar : sources : 3.25.1-01 (do not match org.eclipse.* : * : * : * : *)",
                                                  "reference": null
                                              }
                                          ]
                                      }
                                  ],
                                  "policyWaiver": {
                                      "policyWaiverId": "88a3cca014dd4122ae24b07e3d2477cb",
                                      "comment": "",
                                      "createTime": "2022-10-07T21:29:39.111+0000",
                                      "expiryTime": "2022-11-07T04:59:59.999+0000",
                                      "reasonText": "Not exploitable",
                                      "policyWaiverReasonId": "f6390a32cd8d2ea78453ca829d948927",
                                      "isObsolete": false,
                                      "scopeOwnerType": "application",
                                      "scopeOwnerId": "0d3fa305cb8d4ff4b9442d29816cf24c",
                                      "scopeOwnerName": "Application - TestApp",
                                      "hash": "3ef19d8647bc8031ee94",
                                      "policyId": "a9f5f3450375455b8335e02a1ee222db",
                                      "creatorId": "admin",
                                      "creatorName": "Admin BuiltIn",
                                      "matcherStrategy": "EXACT_COMPONENT",
                                      "associatedPackageUrl": "pkg:maven/org.sonatype.nexus/nexus-rest-client@3.25.1-01?classifier=sources&type=jar",
                                      "componentIdentifier": {
                                          "format": "maven",
                                          "coordinates": {
                                              "artifactId": "nexus-rest-client",
                                              "classifier": "sources",
                                              "extension": "jar",
                                              "groupId": "org.sonatype.nexus",
                                              "version": "3.25.1-01"
                                          }
                                      },
                                      "displayName": {
                                          "parts": [
                                              {
                                                  "field": "Group",
                                                  "value": "org.sonatype.nexus"
                                              },
                                              {
                                                  "value": " : "
                                              },
                                              {
                                                  "field": "Artifact",
                                                  "value": "nexus-rest-client"
                                              },
                                              {
                                                  "value": " : "
                                              },
                                              {
                                                  "field": "Extension",
                                                  "value": "jar"
                                              },
                                              {
                                                  "value": " : "
                                              },
                                              {
                                                  "field": "Classifier",
                                                  "value": "sources"
                                              },
                                              {
                                                  "value": " : "
                                              },
                                              {
                                                  "field": "Version",
                                                  "value": "3.25.1-01"
                                              }
                                          ],
                                          "name": "nexus-rest-client"
                                      }
                                  }
                              }
                          ]
                      }
                  ]
              }
          ]
      }
  ],
  "repositoryWaivers": []
}
```

**Note:** The returned component *hash* value is truncated and is meant to be used as an identifier that can be passed into subsequent REST API calls. It is not intended to be used as a checksum.

### Other Related REST APIs

## Stale Waivers REST API

The Stale Waivers REST API reports waivers that are stale. A waiver is considered to be stale when it is not used in the IQ Server. Examples are:

- A waiver applied in an evaluation and later skipped in another evaluation because the violation it waived does not exist anymore (perhaps due to component upgrade) is a stale waiver
- A waiver added but not applied because there was no evaluation is a stale waiver (it is not used until there is an evaluation)

A list of stale waivers is useful to identify potential risks in future evaluations because it helps to determine where violations can be unintentionally waived.

Stale evaluations listed under stale waivers help determine where evaluations may be needed in order to verify that the waivers are truly not used. An application or repository evaluation is considered to be stale if a new waiver has been created since the last evaluation.

**Note:** All repository reports must be re-evaluated after Nexus IQ Server version 76 in order to include the most accurate policy waiver information used by the new API.

### Scope of waivers and user permissions

Only the stale waivers that the specific user has permission to see will be returned, even though the computation of the staleness of a waiver can include applications and/or repositories that the user does not have permission to see.

For example, when Organization A has Application 1 and Application 2, and a user has permission to only Application 1, the user will see waivers scoped to Organization A because Application 1 is too under the scope of those waivers, but the user will not see waivers scoped to Application 2 because Application 1 is not under the scope of those waivers. Also, the computation of staleness of a waiver scoped to Organization A will include both Application 1 and Application 2, even if the user has only access to Application 1.

In the case of stale evaluations, only applications and repositories that are stale and that the user has permission to see will be returned.

Before performing any actions on stale waivers it is recommended to have complete visibility of what can be affected. This can be achieved by calling the API with sufficient user permissions (preferably an admin user).

### Requesting Stale Waivers

An HTTP GET method is used to list the Stale Waivers:

```
GET /api/v2/reports/waivers/stale
```

A sample request to list the stale waivers is done by issuing the following curl command:

```
curl -u admin:admin123 -X GET 'http://localhost:8070/api/v2/reports/waivers/stale'
```

### Response description

The response is a JSON object with the property "staleWaivers". This property has an array with stale waivers.

Here is a sample response:

```
{
  "staleWaivers": [
    {
      "waiverId": "943d67ad7b904ea092ce0487a99b358e",
      "policyId": "112b8420643b4219a7775ba5d37889b5",
      "policyName": "Security-Critical",
      "comment": "",
      "scopeOwnerType": "root_organization",
      "scopeOwnerId": "ROOT_ORGANIZATION_ID",
      "scopeOwnerName": "Root Organization",
      "createTime": "2020-01-21T20:56:35.803+0000",
                "expiryTime": "2020-02-21T20:56:35.803+0000",
      "reasonText": "Not exploitable",
      "policyWaiverReasonId": "f6990a32cd8d4ea78653ca829d348927",
                "creatorId": "authorizedUser",
                "creatorName": "Authorized User",
      "constraintFacts": [
        {
          "constraintName": "Critical risk CVSS score",
          "constraintId": "5ec402530f6849dab3066d6a598fd7d2",
          "reasons": [
            {
              "reason": "Found security vulnerability sonatype-2015-0002 with severity >= 9 (severity = 9.0)"
            }
          ]
        }
      ],
      "staleEvaluations": {
        "applications": [
          {
            "application": {
              "id": "887474a442524a8e950cb90e906b53a8",
              "publicId": "webgoat",
              "name": "WebGoat",
              "organizationId": "b301c86db103482cb276f4c9ca388d9f",
              "contactUserName": null
            },
            "stages": [
              {
                "stageId": "build",
                "lastEvaluationDate": "2020-01-21T20:55:44.362+0000"
              }
            ]
          }
        ],
        "repositories": [
          {
            "repository": {
              "repositoryId": "2c52468043374959946a679082c72434",
              "publicId": "maven-central-proxy",
              "format": "maven2"
            },
            "stages": [
              {
                "stageId": "proxy",
                "lastEvaluationDate": "2020-01-21T20:48:30.433+0000"
              }
            ]
          }
        ]
      }
    }
  ]
}
```

Here is a description of the properties of a stale waiver:

⚠️ **Warning:** A 409 HTTP status code will be returned if waivers are found for repositories that have not been re-evaluated since Nexus IQ Server version 76.

### Other Related REST APIs

## Transitive Waivers REST API

### Transitive Violations

A transitive policy violation is a violation in the report that is brought in by a transitive dependency.

Following APIs provide a way of getting and waiving transitive violations of a component in a specific stage (e.g. Build, Stage Release, and Release) or scan.

## Waiver Reason REST API

The Waiver Reason REST API can be used to retrieve all *Waiver Reasons* that can be applied to a waiver.

All authenticated users in *Lifecycle* can use the Waiver Reason REST API to view the *Waiver Reasons* .

### Methods Supported

GET

```
GET /api/v2/policyWaiverReasons
```

**Example**

```
curl -u admin:admin123 -X GET http://localhost:8070/api/v2/policyWaiverReasons
```

**Response**

```
[
  {
    "id": "9b704ef5bc064fc29d7fe08a251ee9a6",
    "type": "system",
    "reasonText": "Acknowledged violation"
  },
  {
    "id": "42069f58114f4df8b435a40a415d2835",
    "type": "system",
    "reasonText": "Mitigated externally"
  },
  {
    "id": "39984de3d6e64f508df82b4cbfd72f70",
    "type": "system",
    "reasonText": "No upgrade path"
  },
  {
    "id": "f6990a32cd8d4ea78853ca829d948927",
    "type": "system",
    "reasonText": "Not exploitable"
  },
  {
    "id": "3446e70e60e04676a90131f3dea9bdb5",
    "type": "system",
    "reasonText": "Researching"
  },
  {
    "id": "c991ef95866d4903ad0c6c217ac47c07",
    "type": "system",
    "reasonText": "Other"
  }
]
```

**Response Fields:**

## Promote Scan REST API

The Promote Scan REST API allows for an existing scan report to be promoted to a specified stage. The scan metadata generated for a specific build scan can be resubmitted for an evaluation of its components without having to rebuild the application. This new evaluation will update the most recent security and license data against your current policies.

### Purging Scan Files

In the default configuration for IQ Server, only the latest scan data is retained while older scan files are automatically purged at the time of the next scan. This means that while this configuration is set only the latest scan file could be promoted.

Cleanup of scan files can be changed to purge them along with their corresponding reports. This is required if you will need to promote any scan rather than only the latest.

Use the Configuration REST API to retain scan files for a longer period of time.

```
# Set the purgeScanFiles property to withReports.

curl -u admin:admin123 -X PUT -H "Content-Type: application/json" -d '{"purgeScanFiles": "withReports"}' http://localhost:8070/api/v2/config
```

### Rest Calls

The API uses the following REST methods

- POST - to submit a request to promote a scan to another stage.
- GET - to check the status of a promote scan request.

### Promotion Workflow

## Reverse Proxy Authentication Configuration REST API

Use to manage a reverse proxy authentication configuration. These endpoints require the `System Administrator` role or the `Edit System Configuration and Users` permission.

### GET a Reverse Proxy Authentication Configuration

To get the reverse proxy authentication configuration you can make a GET request to the following path:

```
GET /api/v2/config/reverseProxyAuthentication
```

```
curl -u admin:admin123 http://localhost:8070/api/v2/config/reverseProxyAuthentication
```

Returns ' `Reverse proxy authentication not configured` ' when not set.

### PUT a Reverse Proxy Authentication Configuration

To set the reverse proxy authentication configuration you can make a PUT request to the following path:

```
PUT /api/v2/config/reverseProxyAuthentication
```

```
{
  "enabled": true, 
  "usernameHeader": "MY_USERNAME_HEADER", 
  "csrfProtectionDisabled": true, 
  "logoutUrl": "http://localhost/logout/index.html"
}
```

Property not set use the default values from the table below.

```
curl -X PUT -u admin:admin123 -H "Content-Type: application/json" -d "{\"enabled\": true, \"usernameHeader\": \"MY_USERNAME_HEADER\", \"csrfProtectionDisabled\": true, \"logoutUrl\": \"http://localhost/logout/index.html\"}" "http://localhost:8070/api/v2/config/reverseProxyAuthentication"
```

### DELETE a Reverse Proxy Authentication Configuration

To delete the reverse proxy authentication configuration you can make a DELETE request to the following path:

```
DELETE /api/v2/config/reverseProxyAuthentication
```

Below is an example request to a local IQ Server using the built-in administrator account and the cURL tool:

```
curl -X DELETE -u admin:admin123 http://localhost:8070/api/v2/config/reverseProxyAuthentication
```

## Role REST API

In the following sections, all partial URLs are relative to IQ Server's base URL, and we issue requests using the `cURL` tool. Also, all request/response bodies are JSON content (formatted here for readability).

### Get roles

Roles can be retrieved by making an HTTP GET request to

```
GET /api/v2/roles
```

For example

```
curl -u admin:admin123 'http://localhost:8070/api/v2/roles'
```

gives

```
{
  "roles": [
    {
      "id": "1b92fae3e55a411793a091fb821c422d",
      "name": "System Administrator",
      "description": "Manages system configuration and users."
    },
    {
      "id": "b9646757e98e486da7d730025f5245f8",
      "name": "Policy Administrator",
      "description": "Manages all organizations, applications, policies, and policy violations."
    },
    {
      "id": "1cddabf7fdaa47d6833454af10e0a3ef",
      "name": "Owner",
      "description": "Manages assigned organizations, applications, policies, and policy violations."
    },
    {
      "id": "1da70fae1fd54d6cb7999871ebdb9a36",
      "name": "Developer",
      "description": "Views all information for their assigned organization or application."
    },
    {
      "id": "2cb71b3468d649789163ea2e212b541e",
      "name": "Application Evaluator",
      "description": "Evaluates applications and views policy violation summary results."
    },
    {
      "id": "90c7c98683b4471cb77a916744540bcc",
      "name": "Component Evaluator",
      "description": "Evaluates individual components and views policy violation results for a specified application."
    }
  ]
}
```

## SAML REST API

SAML allows to integrate IQ Server with your single sign-on (SSO) infrastructure and this REST API enables [system administrators](#UUID-dbc7b586-b425-e5b2-82a5-76c9e16bbcee) to inspect and update the needed configuration for IQ Server. Consult the [SAML Integration](#UUID-20ae9fbe-ea8f-6190-9982-302d92303804) page for details on integrating IQ Server with an identity provider and/or configuring SAML using the UI instead of the REST API explained here.

### Query Current SAML Configuration

The SAML configuration that is currently in effect can be determined using the request

```
GET /api/v2/config/saml
```

Using the cURL tool, the following example demonstrates a complete request to a local IQ Server using its built-in admin account

```
curl -u admin:admin123 http://localhost:8070/api/v2/config/saml
```

If SAML is not configured, the request yields HTTP status code 404. If SAML is configured, the response will be a JSON document similar to the one below.

```
{
  "identityProviderName": "My Identity Provider",
  "entityId": "http://localhost:8070/api/v2/config/saml/metadata",
  "firstNameAttributeName": "firstName",
  "lastNameAttributeName": "lastName",
  "emailAttributeName": "email",
  "usernameAttributeName": "username",
  "groupsAttributeName": "groups",
  "validateResponseSignature": null,
  "validateAssertionSignature": false,
  "identityProviderMetadataXml": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><EntityDescriptor ..."
}
```

The next section regarding changes to the configuration will detail the meaning of the individual parameters.

### Configure SAML Integration

To enable single sign-on using SAML, the API accepts PUT requests to the same path as used for reading the SAML configuration

```
PUT /api/v2/config/saml
```

This request uses the content type `multipart/form-data` to transport the needed configuration to the IQ Server. The form data consists of two parameters:

- `identityProviderXml` The SAML metadata of your identity provider (IdP), i.e. the server that will be handling the single sign-on for users accessing IQ Server. Consult the documentation of your identity provider on how exactly to obtain this metadata. As an orientation, the metadata should have the following form:
- `samlConfiguration` A JSON document with additional configuration properties needed for IQ Server to interact with the identity provider. This document supports the following properties, all of which are optional and defaulted if not specified: Property Description Default Value `identityProviderName` The name of your identity provider to be displayed on the login form when SAML is configured. Ideally this should be set to a name that users will recognise. `identity provider` `entityId` The URI that IQ Server will use to identify itself in requests to the single sign-on service. `<iqServerBaseUrl>` `/api/v2/config/saml/metadata` `firstNameAttributeName` The name of the SAML attribute that IQ Server will extract from the login response of the identity provider to determine the user's first name. `firstName` `lastNameAttributeName` The name of the SAML attribute that IQ Server will extract from the login response of the identity provider to determine the user's last name. `lastName` `emailAttributeName` The name of the SAML attribute that IQ Server will extract from the login response of the identity provider to determine the user's mail address. `email` `usernameAttributeName` The name of the SAML attribute that IQ Server will extract from the login response of the identity provider to determine the user's username/id. `username` `groupsAttributeName` The name of the SAML attribute that IQ Server will extract from the login response of the identity provider to determine the groups the user is a member of. `groups` `validateResponseSignature` A boolean flag ( `true` / `false` ) denoting whether SAML responses from the identity provider are cryptographically signed to avoid tampering. `null` in which case the setting is derived from the SAML metadata of the identity provider, performing signature validation if a signing key ( `<KeyDescriptor>` ) is included `validateAssertionSignature` A boolean flag ( `true` / `false` ) denoting whether SAML assertions from the identity provider are cryptographically signed to avoid tampering. `null` in which case the setting is derived from the SAML metadata of the identity provider, performing signature validation if a signing key ( `<KeyDescriptor>` ) is included

If SAML is not yet configured, the `identityProviderXml` parameter is mandatory for the request to succeed. If SAML is already configured, either `identityProviderXml` or `samlConfiguration` can be omitted from the request to keep its current setting and selectively update only the other parameter.

The following concrete example sets the `identityProviderXml` to the content of the file `saml-idp-metadata.xml` and uses default values for most of the remaning SAML configuration except for the `groupsAttributeName` :

```
curl -u admin:admin123 -X PUT -F identityProviderXml=@saml-idp-metadata.xml -F samlConfiguration='{"groupsAttributeName": "memberOf"}' http://localhost:8070/api/v2/config/saml
```

The response is either HTTP status code 204 if the operation was successful or status code 400 if any part of the new configuration is invalid in which case the previous SAML configuration remains in effect.

### Query IQ Server's Metadata

IQ Server's metadata currently in effect can be downloaded using the request

```
GET /api/v2/config/saml/metadata
```

Using the cURL tool, the following example demonstrates a complete request to a local IQ Server using its built-in admin account

```
curl -u admin:admin123 http://localhost:8070/api/v2/config/saml/metadata
```

If SAML is not configured, the request yields HTTP status code 404. If SAML is configured, the response will be an XML document similar to the one below.

```
<EntityDescriptor xmlns="urn:oasis:names:tc:SAML:2.0:metadata" entityID="http://localhost:8070/api/v2/config/saml/metadata">
    <SPSSODescriptor AuthnRequestsSigned="false" WantAssertionsSigned="true"
        protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol urn:oasis:names:tc:SAML:1.1:protocol
                                    http://schemas.xmlsoap.org/ws/2003/07/secext">
        <KeyDescriptor use="encryption">
          <dsig:KeyInfo xmlns:dsig="http://www.w3.org/2000/09/xmldsig#">
            <dsig:X509Data>
              <dsig:X509Certificate>MIIC4heX5KLRbvE3Xnb1y3B9lSw0JpgINSXxKiwUVyJHtacCo+LQ==</dsig:X509Certificate>
            </dsig:X509Data>
          </dsig:KeyInfo>
        </KeyDescriptor>
        <SingleLogoutService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="http://localhost:8070/saml"/>
        <NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified</NameIDFormat>
        <AssertionConsumerService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="http://localhost:8070/saml"
                index="1" isDefault="true" />
    </SPSSODescriptor>
</EntityDescriptor>
```

### Disable SAML Integration

If the SAML integration and thereby single sign-on needs to be disabled, an HTTP DELETE request is used

```
DELETE /api/v2/config/saml
```

For example

```
curl -u admin:admin123 -X DELETE http://localhost:8070/api/v2/config/saml
```

If SAML was configured, the request responds with HTTP status code 204. If SAML was not configured to begin with the HTTP status code 404 is returned instead.

## Security Vulnerability Override API

API to obtain the status (Security Vulnerability Override) of security vulnerabilities in the system, when one has been applied at a point in time.

### Available endpoints

### Response Data

Here is the example of a response for a call to the endpoint described above

```
{
   "securityOverrides":[
      {
         "securityOverrideId":"b318b2555bac47089d00bdad1eb11a4c",
         "hash":"894ebaea50d38ef8776d",
         "referenceId":"CVE-2020-11023",
         "status":"Not Applicable",
         "comment":"This security vulnerability is not currently applicable",
         "owner":{
            "ownerPublicId":"nemesis",
            "ownerId":"bef62081db3140b49274bb807bbbc60e",
            "ownerName":"Nemesis",
            "ownerType":"APPLICATION"
         },
         "currentlyAffectedComponents":[
            {
               "packageUrl":"pkg:a-name/jQuery@1.6.4",
               "hash":"894ebaea50d38ef8776d",
               "componentIdentifier":{
                  "format":"a-name",
                  "coordinates":{
                     "name":"jQuery",
                     "qualifier":"",
                     "version":"1.6.4"
                  }
               },
               "proprietary":false,
               "thirdParty":false
            }
         ]
      }
   ]
}
```

## Source Control Configuration REST API

The REST API endpoints described here allow anyone with the System Administrator role or the Edit System Configuration and Users permission to manage a Source Control Configuration.

### Source Control Configuration Properties

**Note:** If no source control configuration is saved, then internally we will use a default configuration when needed, which uses the value for each property if it is not configured. A source control configuration (default or custom) will only be needed if source control management has been configured for an organization or application.

### GET the Source Control Configuration

To get the source control configuration you can make a GET request to the following path:

```
GET /api/v2/config/sourceControl
```

Below is an example request to a local IQ Server using the built-in administrator account and the cURL tool:

```
curl -u admin:admin123 http://localhost:8070/api/v2/config/sourceControl
```

If no source control configuration is saved, then the request yields HTTP status code 404. Otherwise, a JSON response with all the properties described above is returned.

### PUT the Source Control Configuration

To set the source control configuration you can make a PUT request to the following path:

```
PUT /api/v2/config/sourceControl
```

The request requires a JSON body as payload.

All properties are optional.

If the source control configuration is being created for the first time, then any property that is not supplied will take its default value.

If the source control configuration already exists, then any supplied properties will have their values updated to the given values.

Below is an example request to a local IQ Server using the built-in administrator account and the cURL tool:

```
curl -u admin:admin123 -X PUT -H "Content-Type: application/json" -d '{"cloneDirectory": "some-clone-directory", "gitImplementation": "native", "prCommentPurgeWindow": 90, "prEventPurgeWindow": 7, "gitExecutable": "/path/to/native/git/executable", "gitTimeoutSeconds": 150, "commitUsername": "some-commit-username", "commitEmail": "some-commit-email@domain", "useUsernameInRepositoryCloneUrl": true, "defaultBranchMonitoringStartTime": "1:11", "defaultBranchMonitoringIntervalHours": 2, "pullRequestMonitoringIntervalSeconds": 3}' http://localhost:8070/api/v2/config/sourceControl
```

A successful request yields HTTP status code 204.

### DELETE the Source Control Configuration

To delete the source control configuration you can make a DELETE request to the following path:

```
DELETE /api/v2/config/sourceControl
```

Below is an example request to a local IQ Server using the built-in administrator account and the cURL tool:

```
curl -u admin:admin123 -X DELETE http://localhost:8070/api/v2/config/sourceControl
```

A successful request yields HTTP status code 204.

## Source Control Evaluation REST API

The Source Control Evaluation REST API provides a way to perform an application policy evaluation on supported manifest files discovered in a source control branch.

Source control evaluations are executed asynchronously and it is thus a 2-step process for the API user to obtain the results:

### Request a Source Control Evaluation

To request a source control evaluation, you need the ID of the application associated with the source control repository, the name of the target branch in the source control repository and the ID of the target stage. For source control evaluations on feature branches the target stage is usually "develop". For source control evaluations on the default branch the "source" stage is more appropriate. Other stage IDs that can be used in either case, but not recommended, are "build", "stage-release", "release", "operate".

By default, the evaluation is done for the whole repository. If only part(s) of the repository should be evaluated, the optional scanTargets attribute can be used to specify one or more paths inside the repository. These paths cannot contain "../" or "..\".

```
POST /api/v2/evaluation/applications/{applicationInternalId}/sourceControlEvaluation
```

with a JSON body:

```
{
        "stageId": "develop",
        "branchName": "my-test-branch-name",
        "scanTargets": ["path-inside-repository1", "path-inside-repository2"]
}
```

Example using the cURL tool:

```
curl -u admin:admin123 -X POST -H "Content-Type: application/json" -d '{"stageId":"develop","branchName":"my-test-branch-name"}' 'http://localhost:8070/api/v2/evaluation/applications/cb748fb6ff8f4251b40b63edf1cc465c/sourceControlEvaluation'
```

which will result in a JSON response like this:

```
{
        "statusUrl": "api/v2/evaluation/applications/cb748fb6ff8f4251b40b63edf1cc465c/status/accc369749774924baa1d207494c29e1"
}
```

### Check the Status of a Source Control Evaluation Request

The status URL returned above can be used to check the evaluation status:

```
GET api/v2/evaluation/applications/{applicationInternalId}/status/{statusId}
```

Example using the cURL tool:

```
curl -u admin:admin123 'http://localhost:8070/api/v2/evaluation/applications/cb748fb6ff8f4251b40b63edf1cc465c/status/accc369749774924baa1d207494c29e1'
```

The response will include one of three possible status values:

- "PENDING"
- "FAILED"
- "COMPLETED"

For example, if the evaluation is still in progress:

```
{
        "status": "PENDING"
}
```

or, in the rare case of an error that causes the evaluation to fail:

```
{
        "status": "FAILED",
        "reason": "message"
}
```

or, finally, if the evaluation is successful links to the evaluation report are provided:

```
{
        "status": "COMPLETED",
        "reportHtmlUrl": "ui/links/application/cb748fb6ff8f4251b40b63edf1cc465c/report/affdb6b964a64f0bad2db7170c7560dc",
        "embeddableReportHtmlUrl": "ui/links/application/cb748fb6ff8f4251b40b63edf1cc465c/report/affdb6b964a64f0bad2db7170c7560dc/embeddable",
        "reportPdfUrl": "ui/links/application/cb748fb6ff8f4251b40b63edf1cc465c/report/affdb6b964a64f0bad2db7170c7560dc/pdf",
        "reportDataUrl": "api/v2/applications/cb748fb6ff8f4251b40b63edf1cc465c/reports/affdb6b964a64f0bad2db7170c7560dc"
}
```

## Source Control REST API

Source Control REST API can be used to:

- Create, update, and delete source control entries for the root organization, sub-organizations, and applications. This is implemented with two separate endpoints one for all organizations (including the root), and a second one for applications. The API signatures between the two are similar and differences will be noted below.
- Automatically assign a role (e.g., *developer* ) to all contributors of the a GitHub repository. This removes the need for manual user role assignment. See [Automatic Role Assignment](#UUID-0af5b737-af38-5ec5-ea69-62d8211951d8_id_SourceControlRESTAPIv2-Step4-Deleteasourcecontrolentry) .
- [Map existing SCM user credentials](#section-idm234646010084107) (GitHub) to local or LDAP *Lifecycle* users. RELEASE 192 This has been extended to include SAML users. The Source Control REST API can be used to map existing SCM user credentials (GitHub) to local, LDAP, SAML users (for on-premises IQ Server) and OAuth (for Cloud/SaaS IQ Server).

⚠️ **Warning:** The `enablePullRequests` and `enableStatusChecks` fields in the JSON payload were deprecated in IQ Server Release 124: `- enablePullRequests` was replaced with `pullRequestCommentingEnabled` `- enableStatusChecks` was replaced with `statusChecksEnabled` If you use an IQ Server version prior to 124, you'll have to replace the deprecated field names in the examples below.

### Create a source control entry

Permissions Required: `Edit IQ Elements`

To create a source control entry use the following endpoint. To create one for an organization use `organization` in the path, and for an application use `application` in the path.

```
POST /api/v2/sourceControl/{organization|application}/{ownerId}
```

With the following JSON body

```
{
    "token": "{scm access token}",
    "provider": "github",
    "repositoryUrl": "https://example.com/my-org/my-repo", 
    "baseBranch": "master",
    "remediationPullRequestsEnabled": true,
    "pullRequestCommentingEnabled": true,
    "sourceControlEvaluationsEnabled": true
}
```

- The `ownerId` parameter is required. For the `/api/v2/sourceControl/organization/` endpoint it must be a valid organization ID (use " `ROOT_ORGANIZATION_ID"` for the root organization). For the `/api/v2/sourceControl/application/` endpoint it must be a valid application ID.
- The `repositoryUrl` can only be specified for applications. Valid HTTP(S) and SSH URLs are accepted.
- The `token` field is optional. It must be defined at one of the root organization, organization or application level. Each level inherits from the parent level and when present, will override any values set in the parents. See the [Source Control Configuration](#UUID-161243f0-61ce-a164-d457-2bff696761b4_id_SourceControlConfigurationOverview-createaccesstokenCreateAccessToken) page for information on what permissions or scopes are required on the token.
- The `username` field is optional and only allowed to be set on SCMs that require it. Currently, this is required for Bitbucket Server, Bitbucket Cloud and Azure DevOps.
- The `provider` field is required for the root organization and cannot be specified for other organizations or applications. Allowed values are `azure` , `github` , `gitlab` , and `bitbucket` .
- The `baseBranch` field is required for the root organization. Organizations and applications inherit from the root unless overridden.
- The `remediationPullRequestsEnabled` field is optional. Set to `true` to enable the Automated Pull Requests feature.
- The `pullRequestCommentingEnabled` field is optional. Set to `true` to enable the Pull Request Commenting feature.
- The `sourceControlEvaluationsEnabled` field is optional. Set to `true` to enable Nexus IQ triggered source control evaluations, which are the foundation of the Continuous Risk Profile feature.

**Note:** Two formats are supported for SSH URLs: `ssh://user@server/project-path.git` and `user@server:project-path.git` . On save all SSH URLs are converted to the HTTPS format. If an SSH URL is provided, subsequent retrievals will return the converted URL.

### Get a source control entry

Permissions Required: `View IQ Elements`

To get a source control entry use the following endpoint. To get for an organization use `organization` in the path, and for an application use `application` in the path.

```
GET /api/v2/sourceControl/{organization|application}/{ownerId}
```

- The `ownerId` parameter is required. For the `/api/v2/sourceControl/organization/` endpoint it must be a valid organization ID (use " `ROOT_ORGANIZATION_ID"` for the root organization). For the `/api/v2/sourceControl/application/` endpoint it must be a valid application ID.

The response can contain the following fields

```
{
    "id": "83af9dafc06946f9a82833eceb8425ed",
    "ownerId": "7e68069cbb228a05bbf89a2c2992a8bce45b1027",
    "repositoryUrl": null,
    "token": "#~FAKE~SECRET~KEY~#",
    "provider": null,
    "baseBranch": "master",
    "remediationPullRequestsEnabled": null,
    "pullRequestCommentingEnabled": null,
    "sourceControlEvaluationsEnabled": null,
    "statusChecksEnabled": null
}
```

- Fields that do not contain a value are `null` . For organizations and applications, this indicates inheriting the configuration from the parent. Applications will inherit values from the parent organization and organizations will inherit from the root organization.
- The `ownerId` field is required. For the `/api/v2/sourceControl/organization/` endpoint it will be an organization ID. For the `/api/v2/sourceControl/application/` endpoint it will be an application ID.
- The `repositoryUrl` will only show for applications and will always be `null` for organizations.
- The `token` field is obfuscated if populated.
- The `id` and `statusChecksEnabled` fields are internal fields.

### Replace a source control entry

Permissions Required: `Edit IQ Elements`

To replace a source control entry use the following endpoint. To replace one for an organization use `organization` in the path, and for an application use `application` in the path.

```
PUT /api/v2/sourceControl/{organization|application}/{ownerId}
```

- The `ownerId` parameter is required. For the `/api/v2/sourceControl/organization/` endpoint it will be an organization ID. For the `/api/v2/sourceControl/application/` endpoint it will be an application ID.

With the same JSON body as for `POST` .

### Delete a source control entry

Permissions Required: `Edit IQ Elements`

To delete a source control entry use the following endpoint. To delete one for an organization use `organization` in the path, and for an application use `application` in the path.

```
DELETE /api/v2/sourceControl/{organization|application}/{ownerId}
```

- The `ownerId` parameter is required. For the `/api/v2/sourceControl/organization/` endpoint it will be an organization ID. For the `/api/v2/sourceControl/application/` endpoint it will be an application ID.

The response is an empty payload with a `204` (Success - no content) status.

### Automatic Role Assignment (GitHub)

Automatic Role Assignment lets you automatically grant Lifecycle roles to GitHub contributors.

**Note:** This capability is currently offered for GitHub repositories only. This feature currently supports matching for local, LDAP, SAML (release 192 for on-premises IQ Server) and OAuth (for Cloud/SaaS IQ Server) user accounts.

### Configure User Mappings (GitHub)

User mappings define how Lifecycle attempts to match GitHub contributor information to existing local, LDAP or SAML (release 192) Lifecycle users.

Each mapping consists of the following:

- A `from` field (GitHub data)
- A `to` field (Lifecycle user attribute)

When you provide multiple user mappings, Lifecycle tries the mappings in order and stops evaluating once it finds a mapping that yields at least one match (i.e., if the first mapping does not match, it moves on to the next mapping).

If you specify duplicate user mappings, you will see an error message like the one below:

```
There was a duplicate mapping GITLOG_FULLNAME:IQ_FULLNAME . Mappings should be unique
```

## CycloneDX REST API

This API returns a CycloneDX SBOM document (in both XML and JSON formats) containing coordinates and licenses for components in a scan report. It supports all component formats. Retrieve the internal application identifier and then pass it as an input parameter to get the SBOM report.

### Step 1 - Get the internal application ID

Use the Application REST API with the application’s public ID (user-created) to retrieve the application's internal ID.

```
GET /api/v2/applications?publicId={YourPublicId}
```

### Step 2 - Retrieve the SBOM with the application ID

The returned version of the supported CycloneDX schema is required when requesting an SBOM. Possible values for the version are:

```
1.1, 1.2, 1.3, 1.4, 1.5, 1.6
```

The API can retrieve the SBOM based on the latest evaluation by instead passing the stage ID in the GET method.

```
GET /api/v2/cycloneDx/{version}/{applicationInternalId}/stages/{stageId}
```

Possible values for the stage ID are:

```
build, stage-release, release, operate
```

### Response

A file with filename format [prefix]-bom.[xml|json] will be created, if you have used the curl command with options -O -J (see example c above.)

Here is an example of XML response:

```
<bom xmlns="http://cyclonedx.org/schema/bom/1.5" serialNumber="a6cba7fe0559450fb70251a80709021b" version="1">
    <components>
        <component type="library">
            <group>org.apache.tomcat</group>
            <name>tomcat-catalina</name>
            <version>9.0.14</version>
            <scope>required</scope>
            <hashes>
                <hash alg="SHA-1">af008de6e523b6eeb5e8</hash>
            </hashes>
            <licenses>
                <license>
                    <id>Apache-2.0</id>
                </license>
            </licenses>
            <purl>pkg:maven/org.apache.tomcat/tomcat-catalina@9.0.14?type=jar</purl>
        </component>
        <component type="library">
            <name>Microsoft.AspNetCore.Http.Features</name>
            <version>3.1.3</version>
            <scope>required</scope>
            <hashes>
                <hash alg="SHA-1">1c82fd7494c626d1d009</hash>
            </hashes>
            <licenses>
                <license>
                    <id>Apache-2.0</id>
                </license>
                <license>
                    <id>Not-Supported</id>
                </license>
            </licenses>
            <purl>pkg:nuget/Microsoft.AspNetCore.Http.Features@3.1.3</purl>
        </component>
    </components>
    <externalReferences>
        <reference type="bom">
            <url>http://localhost:8070/ui/links/application/app/report/a6cba7fe0559450fb70251a80709021b</url>
            <comment>http://localhost:8070/ui/links/application/app/report/a6cba7fe0559450fb70251a80709021b</comment>
        </reference>
    </externalReferences>
</bom>
```

To ensure valid SBOM generation, we now put the Sonatype truncated SHA1 into a property instead of a hash and use license name instead of license id for any non-SPDX licenses.

```
<bom xmlns="http://cyclonedx.org/schema/bom/1.5" serialNumber="a6cba7fe0559450fb70251a80709021b" version="1">
    <components>
        <component type="library">
            <group>org.apache.tomcat</group>
            <name>tomcat-catalina</name>
            <version>9.0.14</version>
            <scope>required</scope>
            <properties>
                <property name="Sonatype truncated SHA1">af008de6e523b6eeb5e8</property>
            </properties>
            <licenses>
                <license>
                    <id>Apache-2.0</id>
                </license>
            </licenses>
            <purl>pkg:maven/org.apache.tomcat/tomcat-catalina@9.0.14?type=jar</purl>
        </component>
        <component type="library">
            <name>Microsoft.AspNetCore.Http.Features</name>
            <version>3.1.3</version>
            <scope>required</scope>
             <properties>
                <property name="Sonatype truncated SHA1">1c82fd7494c626d1d009</property>
            </properties>
            <licenses>
                <license>
                    <id>Apache-2.0</id>
                </license>
                <license>
                    <name>Not-Supported</name>
                </license>
            </licenses>
            <purl>pkg:nuget/Microsoft.AspNetCore.Http.Features@3.1.3</purl>
        </component>
    </components>
    <externalReferences>
        <reference type="bom">
            <url>http://localhost:8070/ui/links/application/app/report/a6cba7fe0559450fb70251a80709021b</url>
            <comment>http://localhost:8070/ui/links/application/app/report/a6cba7fe0559450fb70251a80709021b</comment>
        </reference>
    </externalReferences>
</bom>
```

The response now includes detailed vulnerability information in the SBOM. Note that this is only available for CycloneDX version 1.4 or higher.

```
<bom serialNumber="urn:uuid:4b31ae4b-926f-4973-bd34-aa9efa95cd8a" version="1" xmlns="http://cyclonedx.org/schema/bom/1.5">
  <metadata>
    <timestamp>2022-08-01T19:45:40Z</timestamp>
  </metadata>
  <components>
    <component type="library" bom-ref="pkg:rpm/libzstd@1.4.4-1.el8?arch=x86_64">
      <name>libzstd</name>
      <version>1.4.4-1.el8</version>
      <purl>pkg:rpm/libzstd@1.4.4-1.el8?arch=x86_64</purl>
      <modified>false</modified>
      <properties>
        <property name="Sonatype truncated SHA1">f5f4780ecfb517cca289</property>
        <property name="Match State">exact</property>
        <property name="Identification Source">Sonatype</property>
      </properties>
    </component>
  </components>
  <externalReferences>
    <reference type="bom">
      <url>http://localhost:8070/ui/links/application/app/report/4b31ae4b926f4973bd34aa9efa95cd8a</url>
      <comment>IQ Report</comment>
    </reference>
  </externalReferences>
  <vulnerabilities>
    <vulnerability>
      <id>sonatype-2022-0219</id>
      <source>
        <name>SONATYPE</name>
        <url>http://localhost:8070/ui/links/vln/sonatype-2022-0219</url>
      </source>
      <ratings>
        <rating>
          <source>
            <name>SONATYPE</name>
          </source>
          <score>7.8</score>
          <severity>critical</severity>
          <method>other</method>
          <vector>CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H</vector>
        </rating>
      </ratings>
      <cwes>
        <cwe>119</cwe>
      </cwes>
      <affects>
        <target>
          <ref>pkg:rpm/libzstd@1.4.4-1.el8?arch=x86_64</ref>
        </target>
      </affects>
    </vulnerability>
  </vulnerabilities>
</bom>
```

The response now includes dependency graph information in the SBOM. Note that this is only available for CycloneDX version 1.2 or higher.

```
<bom serialNumber="urn:uuid:33dfc2b6-6d6f-4174-8f4f-2b09cd3ba363" version="1" xmlns="http://cyclonedx.org/schema/bom/1.2">
  <metadata>
    <timestamp>2022-10-10T16:50:51Z</timestamp>
    <component type="application" bom-ref="pkg:maven/com.samplecompany.app/sample-app@2.36.19-SNAPSHOT?type=pom">
      <group>com.samplecompany.app</group>
      <name>sample-app</name>
      <version>2.36.19-SNAPSHOT</version>
      <purl>pkg:maven/com.samplecompany.app/sample-app@2.36.19-SNAPSHOT?type=pom</purl>
    </component>
  </metadata>
  <components>
    <component type="library" bom-ref="pkg:maven/org.apache.httpcomponents/httpcore@4.4.13?type=jar">
      <group>org.apache.httpcomponents</group>
      <name>httpcore</name>
      <version>4.4.13</version>
      <licenses/>
      <purl>pkg:maven/org.apache.httpcomponents/httpcore@4.4.13?type=jar</purl>
      <modified>false</modified>
    </component>
    <component type="library" bom-ref="pkg:maven/commons-codec/commons-codec@1.15?type=jar">
      <group>commons-codec</group>
      <name>commons-codec</name>
      <version>1.15</version>
      <licenses/>
      <purl>pkg:maven/commons-codec/commons-codec@1.15?type=jar</purl>
      <modified>false</modified>
    </component>
    <component type="library" bom-ref="pkg:maven/org.slf4j/jcl-over-slf4j@1.7.36?type=jar">
      <group>org.slf4j</group>
      <name>jcl-over-slf4j</name>
      <version>1.7.36</version>
      <licenses/>
      <purl>pkg:maven/org.slf4j/jcl-over-slf4j@1.7.36?type=jar</purl>
      <modified>false</modified>
    </component>
    <component type="library" bom-ref="pkg:maven/org.apache.httpcomponents/httpclient@4.5.13?type=jar">
      <group>org.apache.httpcomponents</group>
      <name>httpclient</name>
      <version>4.5.13</version>
      <licenses/>
      <purl>pkg:maven/org.apache.httpcomponents/httpclient@4.5.13?type=jar</purl>
      <modified>false</modified>
    </component>
    <component type="library" bom-ref="pkg:maven/com.samplecompany.app/app-test@2.36.19-SNAPSHOT?type=jar">
      <group>com.samplecompany.app</group>
      <name>app-test</name>
      <version>2.36.19-SNAPSHOT</version>
      <licenses/>
      <purl>pkg:maven/com.samplecompany.app/app-test@2.36.19-SNAPSHOT?type=jar</purl>
      <modified>false</modified>
    </component>
    <component type="library" bom-ref="pkg:maven/com.samplecompany.app/app-test-proxy@2.36.19-SNAPSHOT?type=jar">
      <group>com.samplecompany.app</group>
      <name>app-test-proxy</name>
      <version>2.36.19-SNAPSHOT</version>
      <licenses/>
      <purl>pkg:maven/com.samplecompany.app/app-test-proxy@2.36.19-SNAPSHOT?type=jar</purl>
      <modified>false</modified>
    </component>
  </components>
  <externalReferences>
    <reference type="bom">
      <url>http://localhost:8070/ui/links/application/maven/report/33dfc2b66d6f41748f4f2b09cd3ba363</url>
      <comment>IQ Report</comment>
    </reference>
  </externalReferences>
  <dependencies>
    <dependency ref="pkg:maven/com.samplecompany.app/sample-app@2.36.19-SNAPSHOT?type=pom">
      <dependency ref="pkg:maven/com.samplecompany.app/app-test@2.36.19-SNAPSHOT?type=jar"/>
      <dependency ref="pkg:maven/com.samplecompany.app/app-test-proxy@2.36.19-SNAPSHOT?type=jar"/>
    </dependency>
    <dependency ref="pkg:maven/com.samplecompany.app/app-test@2.36.19-SNAPSHOT?type=jar"/>
    <dependency ref="pkg:maven/com.samplecompany.app/app-test-proxy@2.36.19-SNAPSHOT?type=jar">
      <dependency ref="pkg:maven/org.slf4j/jcl-over-slf4j@1.7.36?type=jar"/>
      <dependency ref="pkg:maven/org.apache.httpcomponents/httpclient@4.5.13?type=jar"/>
    </dependency>
    <dependency ref="pkg:maven/org.slf4j/jcl-over-slf4j@1.7.36?type=jar"/>
    <dependency ref="pkg:maven/org.apache.httpcomponents/httpclient@4.5.13?type=jar">
      <dependency ref="pkg:maven/org.apache.httpcomponents/httpcore@4.4.13?type=jar"/>
      <dependency ref="pkg:maven/commons-codec/commons-codec@1.15?type=jar"/>
    </dependency>
    <dependency ref="pkg:maven/org.apache.httpcomponents/httpcore@4.4.13?type=jar"/>
  </dependencies>
</bom>
```

The response now includes in the metadata section information about the IQ version used to generate the SBOM. Note that this is only available for CycloneDX version 1.2 or higher.

```
<bom serialNumber="urn:uuid:33dfc2b6-6d6f-4174-8f4f-2b09cd3ba363" version="1" xmlns="http://cyclonedx.org/schema/bom/1.5">
  <metadata>
    <timestamp>2023-02-05T16:50:51Z</timestamp>
    <tools>
      <tool>
        <vendor>Sonatype Inc.</vendor>
        <name>Nexus IQ Server</name>
        <version>1.154.0-01</version>
      </tool>
    </tools>
    <component type="application" bom-ref="pkg:maven/com.samplecompany.app/sample-app@2.36.19-SNAPSHOT?type=pom">
      <group>com.samplecompany.app</group>
      <name>sample-app</name>
      <version>2.36.19-SNAPSHOT</version>
      <purl>pkg:maven/com.samplecompany.app/sample-app@2.36.19-SNAPSHOT?type=pom</purl>
    </component>
  </metadata>
  <components>
    <component type="library" bom-ref="pkg:maven/org.apache.httpcomponents/httpcore@4.4.13?type=jar">
      <group>org.apache.httpcomponents</group>
      <name>httpcore</name>
      <version>4.4.13</version>
      <licenses/>
      <purl>pkg:maven/org.apache.httpcomponents/httpcore@4.4.13?type=jar</purl>
      <modified>false</modified>
    </component>
    <component type="library" bom-ref="pkg:maven/commons-codec/commons-codec@1.15?type=jar">
      <group>commons-codec</group>
      <name>commons-codec</name>
      <version>1.15</version>
      <licenses/>
      <purl>pkg:maven/commons-codec/commons-codec@1.15?type=jar</purl>
      <modified>false</modified>
    </component>
    <component type="library" bom-ref="pkg:maven/org.slf4j/jcl-over-slf4j@1.7.36?type=jar">
      <group>org.slf4j</group>
      <name>jcl-over-slf4j</name>
      <version>1.7.36</version>
      <licenses/>
      <purl>pkg:maven/org.slf4j/jcl-over-slf4j@1.7.36?type=jar</purl>
      <modified>false</modified>
    </component>
    <component type="library" bom-ref="pkg:maven/org.apache.httpcomponents/httpclient@4.5.13?type=jar">
      <group>org.apache.httpcomponents</group>
      <name>httpclient</name>
      <version>4.5.13</version>
      <licenses/>
      <purl>pkg:maven/org.apache.httpcomponents/httpclient@4.5.13?type=jar</purl>
      <modified>false</modified>
    </component>
    <component type="library" bom-ref="pkg:maven/com.samplecompany.app/app-test@2.36.19-SNAPSHOT?type=jar">
      <group>com.samplecompany.app</group>
      <name>app-test</name>
      <version>2.36.19-SNAPSHOT</version>
      <licenses/>
      <purl>pkg:maven/com.samplecompany.app/app-test@2.36.19-SNAPSHOT?type=jar</purl>
      <modified>false</modified>
    </component>
    <component type="library" bom-ref="pkg:maven/com.samplecompany.app/app-test-proxy@2.36.19-SNAPSHOT?type=jar">
      <group>com.samplecompany.app</group>
      <name>app-test-proxy</name>
      <version>2.36.19-SNAPSHOT</version>
      <licenses/>
      <purl>pkg:maven/com.samplecompany.app/app-test-proxy@2.36.19-SNAPSHOT?type=jar</purl>
      <modified>false</modified>
    </component>
  </components>
  <externalReferences>
    <reference type="bom">
      <url>http://localhost:8070/ui/links/application/maven/report/33dfc2b66d6f41748f4f2b09cd3ba363</url>
      <comment>IQ Report</comment>
    </reference>
  </externalReferences>
  <dependencies>
    <dependency ref="pkg:maven/com.samplecompany.app/sample-app@2.36.19-SNAPSHOT?type=pom">
      <dependency ref="pkg:maven/com.samplecompany.app/app-test@2.36.19-SNAPSHOT?type=jar"/>
      <dependency ref="pkg:maven/com.samplecompany.app/app-test-proxy@2.36.19-SNAPSHOT?type=jar"/>
    </dependency>
    <dependency ref="pkg:maven/com.samplecompany.app/app-test@2.36.19-SNAPSHOT?type=jar"/>
    <dependency ref="pkg:maven/com.samplecompany.app/app-test-proxy@2.36.19-SNAPSHOT?type=jar">
      <dependency ref="pkg:maven/org.slf4j/jcl-over-slf4j@1.7.36?type=jar"/>
      <dependency ref="pkg:maven/org.apache.httpcomponents/httpclient@4.5.13?type=jar"/>
    </dependency>
    <dependency ref="pkg:maven/org.slf4j/jcl-over-slf4j@1.7.36?type=jar"/>
    <dependency ref="pkg:maven/org.apache.httpcomponents/httpclient@4.5.13?type=jar">
      <dependency ref="pkg:maven/org.apache.httpcomponents/httpcore@4.4.13?type=jar"/>
      <dependency ref="pkg:maven/commons-codec/commons-codec@1.15?type=jar"/>
    </dependency>
    <dependency ref="pkg:maven/org.apache.httpcomponents/httpcore@4.4.13?type=jar"/>
  </dependencies>
</bom>
```

**Note:** The dependency information reported by Sonatype

There are cases where *Sonatype Lifecycle* generates a report (and may determine a dependency graph) of a scan policy evaluation even when no information is found about the containing project. For example, if you scan an archive of binary components outside a project context. In such cases, the response includes a pre-defined parent component name as a placeholder in the metadata section if the report does not contain any project data.

This component will include " *sonatype* " as the namespace and the name of the IQ application with prefix " *iq_application_* " along with the policy evaluation's " *scanId* " being the version. For example:

```
<bom serialNumber="urn:uuid:33dfc2b6-6d6f-4174-8f4f-2b09cd3ba363" version="1" xmlns="http://cyclonedx.org/schema/bom/1.5">
  <metadata>
    <timestamp>2023-06-10T16:50:51Z</timestamp>
    <tools>
      <tool>
        <vendor>Sonatype Inc.</vendor>
        <name>Nexus IQ Server</name>
        <version>1.163.0-01</version>
      </tool>
    </tools>
    <component type="application" bom-ref="b18d79de-7878-42b4-8b0e-6254e109a7a2">
      <group>sonatype</group>
      <name>iq_application_sample-app</name>
      <version>272b82ee904a45e7a1de4299540a284a</version>
      <purl>pkg:generic/sonatype/iq_application_sample-app@272b82ee904a45e7a1de4299540a284a</purl>
    </component>
  </metadata>
...


```

The response may include vulnerability analysis information in the SBOM.

**Note:** Information under the *vulnerability analysis* section will appear if it originally existed in the SBOM that was scanned for the same stage. If it did not exist, you can add the vulnerability analysis section in the original SBOM using the .

```
...
<analysis>
  <state>resolved_with_pedigree</state>
  <justification>requires_environment</justification>
  <responses>
    <response>workaround_available</response>
    <response>update</response>
  </responses>
  <detail>Analysis Detail</detail>
</analysis>
..
```

The response may include Common Platform Enumeration (CPE) and Software Identification (SWID) details, but only if they were present in the original SBOM scanned for that stage.

```
"cpe": "cpe:/a:acme:application:9.1.1",
"swid": {
    "tagId": "swidgen-242eb18a-503e-ca37-393b-cf156ef09691_9.1.1",
    "name": "Acme Application",
    "version": "9.1.1",
    "tagVersion": 0,
    "patch": false,
    "text": {
        "encoding": "base64",
        "contentType": "text/xml",
        "content": "PD94bWwgdmVyc"
    }
}
```

The response includes the field occurrences for every component. This is available for CycloneDX version 1.5 or higher.

```
...
<components>
...
  <component type="library" bom-ref="7e161007-1f0f-467a-8dad-fc4701e90302">
    <group>org.springframework.boot</group>
    <name>spring-boot-autoconfigure</name>
    <version>2.0.3.RELEASE</version>
    <licenses>
      <license>
          <id>Apache-2.0</id>
      </license>
    </licenses>
    <purl>pkg:maven/org.springframework.boot/spring-boot-autoconfigure@2.0.3.RELEASE?type=jar</purl>
    <modified>false</modified>
    <properties>
      <property name="Sonatype truncated SHA1">011bc4cc96b08fabad2b</property>
      <property name="Match State">exact</property>
      <property name="Identification Source">Sonatype</property>
    </properties>
    <evidence>
      <occurrences>
        <occurrence>
          <location>MySampleApp-1.war/WEB-INF/lib/spring-boot-autoconfigure-2.0.3.RELEASE.jar</location>
        </occurrence>
      </occurrences>
    </evidence>
  </component>
  ...
</components>
...
```

### Change history for CycloneDX REST API

## SPDX REST API

The SPDX REST API returns an [SPDX](https://spdx.github.io/spdx-spec/v2.3/) SBOM document (in both XML and JSON formats) containing coordinates, licenses, and dependencies for components in an IQ Server-generated application scan report. This REST API supports all component formats.

### Methods supported:

To use SPDX REST API, first retrieve the internal application ID and then pass it as an input parameter.

### Step 1: Get the internal application ID

Use the with the application’s public ID to retrieve the internal application ID for the application you need to generate the SBOM.

```
GET /api/v2/applications?publicId={YourPublicId}
```

### Step 2: Generate the SBOM

Use the internal application ID from step 1 to generate the SPDX BOM document

```
GET /api/v2/spdx/{applicationInternalId}/reports/{scanId}
```

*scanId* corresponds to the application scan for which an IQ Server report was created.

This API can also retrieve the SBOM based on the latest application evaluation stage, by specifying the *stageId* in the GET method.

```
GET /api/v2/spdx/{applicationInternalId}/stages/{stageId}
```

Possible values for *stageId* are ****

## Success Metrics Data REST API

The Success Metrics Data REST API returns policy evaluation, violation and remediation data, aggregated monthly or weekly. This API is available via a POST resource:

```
POST api/v2/reports/metrics
```

**Note:** Larger data sets may take considerable time to load the first time you access Success Metrics Data. It is recommended to generate the aggregations first by creating and loading a [Success Metrics](#UUID-26c7f8c8-a12d-affa-b1b3-96772119846e) report for the desired applications and organizations.

### Request

Content-Type: application/json

Accept header: application/json (for response in JSON format) OR text/csv (for response in csv format.)

**Request format for JSON response**

```
curl -u <username>:<password> -X POST http://localhost:8070/api/v2/reports/metrics -H "Content-Type: application/json" -H "Accept: application/json" -d "{\"timePeriod\": \"MONTH\", \"firstTimePeriod\": \"<yyyy-mm>\", \"lastTimePeriod\": \"<yyyy-mm>\", \"applicationIds\": [], \"organizationIds\": [\"<orgId>\"]}" -o "<filename.json>"
```

**Request format for csv response**

```
curl -u <username>:<password> -X POST http://localhost:8070/api/v2/reports/metrics -H "Content-Type: application/json" -H "Accept: text/csv" -d "{\"timePeriod\": \"MONTH\", \"firstTimePeriod\": \"<yyyy-mm>\", \"lastTimePeriod\": \"<yyyy-mm>\", \"applicationIds\": [], \"organizationIds\": [\"<orgId>\"]}" -o "<filename.csv>"
```

**Request body**

```
{
  // "MONTH" or "WEEK"
  "timePeriod": "MONTH",
   
  // If timePeriod is MONTH - an ISO 8601 year and month without timezone.
  // If timePeriod is WEEK  - an ISO 8601 week year and week (e.g. week of 29 December 2008 is "2009-W01").
  "firstTimePeriod": "2018-08",

  // Same rules as above. Must be equal to or after firstTimePeriod. Can be omitted,
  // in which case data for all successive time periods is provided including partial data for the current one.
  "lastTimePeriod": "2018-08",

  // If both of these are null or empty, data for all applications (that the user has access to) is returned.
  // applicationIds are Internal ids.
  "applicationIds": [],
  "organizationIds": []
}
```

**Note:** Application ids are internal ids. Internal application ids can be retrieved using [Application REST APIs](#UUID-98adbe51-96e2-70d8-15c6-35e4a74130a9) (see Step 5). Organization ids can be retrieved using [Organization REST APIs](#UUID-2b83db02-df62-d885-19a8-e6ab5c6fe256) .

### Response JSON

**Response JSON**

```
[{
  "applicationId": "foo",
  "applicationPublicId": "asdf",
  "applicationName": "Foo",
  "organizationId": "bar",
  "organizationName:" "Bar",

  // Aggregations are sorted chronologically.
  "aggregations": [{

    // ISO 8601 date.
    "timePeriodStart": "2018-08-01",

    "evaluationCount": 0,
    
    // Mean Time to Resolution (MTTR) in milliseconds.
    "mttrLowThreat": 0,
    "mttrModerateThreat": 0,
    "mttrSevereThreat": 0,
    "mttrCriticalThreat": 0,

    "discoveredCounts": ViolationCountJSON,
    "fixedCounts": ViolationCountJSON,
    "waivedCounts": ViolationCountJSON,

    // Number of unresolved violations at the end of the aggregation period.
    "openCountsAtTimePeriodEnd": ViolationCountJSON
  }]
}]
```

**ViolationCountJSON**

```
{
  "SECURITY": {
    "LOW": 0,
    "MODERATE": 0,
    "SEVERE": 0,
    "CRITICAL": 0
  },
  "LICENSE": {
    "LOW": 0,
    "MODERATE": 0,
    "SEVERE": 0,
    "CRITICAL": 0
  },
  "QUALITY": {
    "LOW": 0,
    "MODERATE": 0,
    "SEVERE": 0,
    "CRITICAL": 0
  },
  "OTHER": {
    "LOW": 0,
    "MODERATE": 0,
    "SEVERE": 0,
    "CRITICAL": 0
  }
}
```

### Response CSV

A CSV document containing all of the fields in the Response JSON, with one row per aggregation. Rows from the same application are grouped together and ordered chronologically. A row of column headers is included at the beginning of the file.

**CSV fields**

```
applicationId
applicationPublicId
applicationName
organizationId
organizationName

timePeriodStart

evaluationCount

mttrLowThreat
mttrModerateThreat
mttrSevereThreat
mttrCriticalThreat

discoveredCountSecurityLow
discoveredCountSecurityModerate
discoveredCountSecuritySevere
discoveredCountSecurityCritical
discoveredCountLicenseLow
discoveredCountLicenseModerate
discoveredCountLicenseSevere
discoveredCountLicenseCritical
discoveredCountQualityLow
discoveredCountQualityModerate
discoveredCountQualitySevere
discoveredCountQualityCritical
discoveredCountOtherLow
discoveredCountOtherModerate
discoveredCountOtherSevere
discoveredCountOtherCritical

fixedCountSecurityLow
fixedCountSecurityModerate
fixedCountSecuritySevere
fixedCountSecurityCritical
fixedCountLicenseLow
fixedCountLicenseModerate
fixedCountLicenseSevere
fixedCountLicenseCritical
fixedCountQualityLow
fixedCountQualityModerate
fixedCountQualitySevere
fixedCountQualityCritical
fixedCountOtherLow
fixedCountOtherModerate
fixedCountOtherSevere
fixedCountOtherCritical

waivedCountSecurityLow
waivedCountSecurityModerate
waivedCountSecuritySevere
waivedCountSecurityCritical
waivedCountLicenseLow
waivedCountLicenseModerate
waivedCountLicenseSevere
waivedCountLicenseCritical
waivedCountQualityLow
waivedCountQualityModerate
waivedCountQualitySevere
waivedCountQualityCritical
waivedCountOtherLow
waivedCountOtherModerate
waivedCountOtherSevere
waivedCountOtherCritical

openCountAtTimePeriodEndSecurityLow
openCountAtTimePeriodEndSecurityModerate
openCountAtTimePeriodEndSecuritySevere
openCountAtTimePeriodEndSecurityCritical
openCountAtTimePeriodEndLicenseLow
openCountAtTimePeriodEndLicenseModerate
openCountAtTimePeriodEndLicenseSevere
openCountAtTimePeriodEndLicenseCritical
openCountAtTimePeriodEndQualityLow
openCountAtTimePeriodEndQualityModerate
openCountAtTimePeriodEndQualitySevere
openCountAtTimePeriodEndQualityCritical
openCountAtTimePeriodEndOtherLow
openCountAtTimePeriodEndOtherModerate
openCountAtTimePeriodEndOtherSevere
openCountAtTimePeriodEndOtherCritical
```

## Third-Party Analysis REST API

Use the Third-Party Analysis REST API to perform an analysis of a software bill of materials (SBOM) for your application.

- The analysis is performed as an asynchronous request that can be monitored or as a fire-and-forget action.
- The analysis results include the Policy Actions as determined by the analysis stage.
- Users require the Evaluate Applications permission to call this API.
- When the same component is found more than once in the SBOM, only the data of the first component is processed.

### Submit SBOM for evaluation

Use a POST request to submit the SBOM for evaluation.

```
POST /api/v2/scan/applications/{applicationId}/sources/{source}?stageId={stageId}
```

- `applicationInternalId` : The internal ID for the application. See the [Application REST API](#UUID-98adbe51-96e2-70d8-15c6-35e4a74130a9) to get the application's internal identifier.
- `stageId` : the Lifecycle or SBOM Manager stage to run the analysis.
- `source` : specify the source of the SBOM file or the tool used to create it.
- Adjust the request header's 'Content-Type' depending on when the file is in XML or JSON formats
- The contents of SBOM may be embedded directly in the call or linked as an included file

Example request with the XML file embedded:

```
curl -u admin:admin123 -X POST -H "Content-Type: application/xml" -d '<bom xmlns="http://cyclonedx.org/schema/bom/1.4" serialNumber="urn:uuid:3e671687-395b-41f5-a30f-a58921a69b79" version="1"> <components> <component type="library"> <publisher>Apache</publisher> <group>org.apache.tomcat</group> <name>tomcat-catalina</name> <version>9.0.14</version> <purl>pkg:maven/org.apache.tomcat/tomcat-catalina@9.0.14?type=jar</purl> </component> </components> </bom>' 'http://localhost:8070/api/v2/scan/applications/4537e6fe68c24dd5ac83efd97d4fc2f4/sources/cyclonedx'
```

Example request with the JSON file linked:

```
curl -u admin:admin123 -X POST -H "Content-Type: application/json" --data "@cyclonedx-bom.json" 'http://localhost:8070/api/v2/scan/applications/4537e6fe68c24dd5ac83efd97d4fc2f4/sources/cyclonedx'
```

A successful POST will result in JSON formatted data confirming that the evaluation was submitted.

```
{ "statusUrl": "api/v2/scan/applications/a20bc16e83944595a94c2e36c1cd228e/status/9cee2b6366fc4d328edc318eae46b2cb" }
```

### Checking the status URL to get the scan result

While the analysis is running, the status URL returned from the response may be used to check the status of the scan. This URL includes the application ID and the scan status ID.

```
GET /api/v2/scan/applications/{applicationInternalId}/status/{statusId}
```

Until the analysis is complete this endpoint will return a 404 status and the following message with your application ID and scan status ID.

```
Report with status id {statusId} for application with id {applicationInternalId} is not ready.
```

When the report is ready the response results in JSON response object containing an analysis summary.

```
{
  "policyAction": "Failure",
  "reportHtmlUrl": "ui/links/application/my-app/report/95c4c14e",
  "reportPdfUrl": "ui/links/application/my-app/report/95c4c14e/pdf",
  "reportDataUrl": "api/v2/applications/my-app/reports/95c4c14e/raw",
  "embeddableReportHtmlUrl": "ui/links/application/my-app/report/95c4c14e/embeddable"
  "isError": false,
  "componentsAffected": {
    "critical": 1,
    "severe": 0,
    "moderate": 0
  },
  "openPolicyViolations": {
    "critical": 2,
    "severe": 1,
    "moderate": 0
  },
  "legacyViolations":0
 }
```

### When the Package URL is Not Available

The package URL is the most effective way to specify the exact component referenced in an application. When not available, the component coordinated and hash may be used to approximate the intended component.

### Supported SBOM and Data Formats

⚠️ **Warning:** Support for CycloneDX vulnerability schema 1.0 XML extension is deprecated with BOM specification 1.4 Use the vulnerabilities type included with version 1.4

### Examples of Valid SBOM Payload

## User REST API

The user REST API allows System Administrators to do the following.

In the following sections, all partial URLs are relative to IQ Server's base URL and we issue requests using the `cURL` tool. Also, all request/response bodies are JSON content (formatted here for readability) and any endpoints that return a user's details exclude their password for security.

**Note:** When enabled the audit log records changes to user access.

### Get all user details

All user details can be retrieved by making an HTTP GET request to

```
GET /api/v2/users
```

An optional "realm" query parameter can be added to retrieve all user details for users belonging to the given security [realm](#UUID-2197ec59-d239-afa5-7ea9-d03c857286d1) . If omitted, the realm will default to be the Internal realm. Supported values include "Internal" and "SAML".

For example

```
curl -u admin:admin123 http://localhost:8070/api/v2/users?realm=Internal
```

gives

```
{
        "users": [
                {
                        "username": "admin",
                        "firstName": "Admin",
                        "lastName": "BuiltIn",
                        "email": "admin@localhost"
                },
                {
                        "username": "bob",
                        "firstName": "Bob",
                        "lastName": "Smith",
                        "email": "bobsmith@domain.com"
                }
        ]
}
```

### Get user details

A user's details can be retrieved by making an HTTP GET request to

```
GET /api/v2/users/{username}
```

An optional "realm" query parameter can be added to retrieve a user's details in the given security [realm](#UUID-2197ec59-d239-afa5-7ea9-d03c857286d1) . If omitted, the realm will default to be the Internal realm. Supported values include "Internal" and "SAML".

For example

```
curl -u admin:admin123 'http://localhost:8070/api/v2/users/bob?realm=Internal'
```

gives

```
{
  "username": "bob",
  "firstName": "Bob",
  "lastName": "Smith",
  "email": "bobsmith@domain.com"
}
```

### Create users

A user can be created by making an HTTP POST request to

```
POST /api/v2/users
```

with a body specifying the user's details.

For example, using the body

```
{
  "username": "ted",
  "password": "secret",
  "firstName": "Ted",
  "lastName": "Baker",
  "email": "tedbaker@example.com"
}
```

Note that all of these fields are required.

```
curl -u admin:admin123 -X POST -H 'Content-Type: application/json' 'http://localhost:8070/api/v2/users' -d '{"username": "ted","password": "secret","firstName": "Ted","lastName": "Baker","email": "tedbaker@example.com"}'
```

gives

```
...
HTTP/1.1 204 No Content
...
```

### Update users

A user can be updated by making an HTTP PUT request to

```
PUT /api/v2/users/{username}
```

with a body specifying the user's details.

For example, using the body

```
{
  "firstName": "Teddy",
  "lastName": "Norman",
  "email": "tnorman@example.com"
}
```

Note that only the "username" in the path is required, any unspecified fields will remain unchanged. If a "username" is also provided in the body, then it must match that in the path.

Also, note that a user's "username" and/or "password" cannot be updated this way.

```
curl -u admin:admin123 -X PUT -H 'Content-Type: application/json' 'http://localhost:8070/api/v2/users/ted' -d '{"firstName": "Teddy","lastName": "Norman","email": "tnorman@example.com"}'
```

gives

```
{
  "username": "ted",
  "firstName": "Teddy",
  "lastName": "Norman",
  "email": "tnorman@example.com"
}
```

An example of a partial update would be

```
curl -u admin:admin123 -X PUT -H 'Content-Type: application/json' 'http://localhost:8070/api/v2/users/ted' -d '{"email": "tnorman@new.com"}'
```

which gives

```
{
  "username": "ted",
  "firstName": "Teddy",
  "lastName": "Norman",
  "email": "tnorman@new.com"
}
```

### Delete users

A user can be deleted by making an HTTP DELETE request to

```
DELETE /api/v2/users/{username}
```

An optional "realm" query parameter can be added to delete a user from the given security [realm](#UUID-2197ec59-d239-afa5-7ea9-d03c857286d1) . If omitted, the realm will default to be the Internal realm. Supported values include "Internal" and "SAML".

For example

```
curl -u admin:admin123 -X DELETE 'http://localhost:8070/api/v2/users/bob?realm=Internal'
```

gives

```
...
HTTP/1.1 204 No Content
...
```

## User Token REST API

IQ Server users can create user tokens which then can be used for authentication instead of their usernames and passwords. A user token is a pair of a user code and a passcode unique to the user, which will grant the permissions that are granted with their credentials.

Further information regarding User Tokens can be found on the page.

### Creating a User Token

An IQ Server user can generate a user token for themselves by the request:

```
POST /api/v2/userTokens/currentUser
```

Using the cURL tool, the following example demonstrates a complete request to a local IQ Server to create a user token:

```
curl -u iq-user:my-secret -X POST http://localhost:8070/api/v2/userTokens/currentUser
```

Given a user exists with the username iq-user and the password my-secret is correct, a user token will be generated for the user similar to:

```
{
    "userCode":"NFWIevo8",
    "passCode":"wv5XosXBU5EBv1OfT31POJ0MgGGbHgbtIRYxq9k4GRgg"
}
```

The successful response to a user token creation as above is the only opportunity for the user to see the generated information and there is no way to retrieve the user token information afterwards. A user can only have a single user token and reset their user token by means of deleting their existing token and generating a new one.

### Checking if User has a Token

An IQ Server user can check if they have a user token issued using the following request:

```
GET /api/v2/userTokens/currentUser/hasToken
```

Using the cURL tool, the following example demonstrates a complete request to a local IQ Server to query if there is an existing token for the user:

```
curl -u iq-server-user:my-secret -X GET http://localhost:8070/api/v2/userTokens/currentUser/hasToken
```

A sample response will resemble the following:

```
{
    "userTokenExists": true
}
```

### Deleting a User Token

An IQ Server user can delete their existing user token by the request:

```
DELETE /api/v2/userTokens/currentUser
```

Using the cURL tool, the following example demonstrates a complete request to a local IQ Server to delete an existing user token:

```
curl -u iq-server-user:my-secret -X DELETE http://localhost:8070/api/v2/userTokens/currentUser
```

### User Token Maintenance for System Administrators

## Vulnerability Details REST API

The Vulnerability Details REST API allows you to retrieve vulnerability details by passing a CVE ID/Sonatype vulnerability identifier or a component identifier. The response will include the **root causes** of the vulnerability when you pass the component identifier as a parameter in the GET request.

### User Permissions Required to Invoke this API call

- View IQ Elements

### Methods supported:

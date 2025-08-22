---
layout: default
title: "Automation"
parent: Sonatype Nexus Repository
nav_order: 9
---

# Automation

This section guides using the APIs, webhooks, and integrations to automate Nexus Repository functionality.

## REST API

Use the REST API to integrate Nexus Repository with external systems. Nexus Repository leverages the OpenAPI Specification (OAS) as its official API documentation. This document is available to download from any instance at the following URL and does not require privileges to access.

```
<nexus_url>/service/rest/swagger.json
```

### Swagger UI in Nexus Repository

We ship Nexus Repository with Swagger UI - a simple, interactive user interface, where REST calls are processed directly through the UI to observe the results in the browser.

This interface is located under the API section via the System sub-menu of the Settings menu.

The *nx-settings-read* privilege is required to access this page. This privilege provides access to multiple views in the user interface. There is not a setting to view only the API view at this time.

The API view lists all APIs and their examples, however, only the APIs that the user has permission to utilize are functional.

### Beta Endpoints in the Nexus Repository API

APIs under the `beta` endpoints are fully supported by Sonatype and are safe to use in production systems. Compatible newer versions may have aliases allowing newer functionality without changing the published endpoint.

## Staging API

Staging is a simple but powerful feature in Nexus Repository that lets you move artifacts from one repository to another using API calls from your CI/CD tools. You can use this to build workflows with quality checks so artifacts are not used before they are ready.

Staging has a powerful connection with other features such as Cleanup Policies which help keep your build pipelines lean and light on storage space.

See the Staging documentation

## Tagging API

Tagging assigns descriptive metadata to components stored in Nexus Repository and makes it possible to organize and track a logical grouping of related artifacts across repositories. Tags facilitate lifecycle management by allowing teams to mark components as they move through development, testing, deployment, and clean-up stages. Tagging improves searching and retrieval of specific components based on custom metadata all through the REST API.

Add custom attributes as JSON data within tags for flexible and detailed annotation of software assets.

See the Tagging documentation

## Scripting API

Scripts may be written to perform custom tasks that can't be handled directly through the UI or the REST API. Nexus Repository scripts are written in the [Groovy](http://groovy-lang.org/) programming language.

To make Nexus Repository more secure, the Groovy scripting engine is disabled by default.

See the Script API documentation for details.

## Nexus Platform Integrations

Below are official integrations for Nexus Repository. Bring open-source policy management and Sonatype component intelligence to Nexus Repository.

### Sonatype IQ Server

The Sonatype IQ Server is an open-source governance and policy management tool that provides compliance metadata to open-source components stored in the Nexus Repository.

![nx-connect-iq-server.png](/assets/images/uuid-91620e5c-d17a-9c33-122b-651bff57a42f.png)

### Nexus Repository for Maven Plugin

Use the Nexus Repository for Maven plugin for staging packages.

See the Nexus Repository Maven Plugin documentation

### Nexus Platform Plugin for Jenkins

A Jenkins plugin that integrates via Jenkins Pipeline or Project steps with Nexus Repository and Sonatype Lifecycle.

See the Nexus Platform Plugin for Jenkins documentation.

## Pagination

Many of the REST API's make use of a pagination strategy for dealing with operations that can return a large number of items. This strategy is built around the notion of a `continuationToken` and a page size that determines the maximum number of items that can be returned in a single response.

As of release 3.74.0, pagination offers a default of 100 items for the assets and components APIs; this setting is not configurable.

When a `continuationToken` is present in a response and has a non-null value, this signifies that there are more items available:

```
GET /service/rest/v1/<api>?<query>
```

```
{
  "items" : [
    ...
  ],
  "continuationToken" : "88491cd1d185dd136f143f20c4e7d50c"
}
```

The API that produced the response will take a `continuationToken` as an additional argument to the original query to signify that the next page of results is desired:

```
GET /service/rest/v1/<api>?<query>&continuationToken=88491cd1d185dd136f143f20c4e7d50c
```

If this response also contains a non-null `continuationToken` , then its value can again be added to the original query to get the next page. This continues until the response returns a `continuationToken` with a value of `null` which signifies that there are no more pages of results.

### Example Python Script

This example uses Python scripting and the Search API to search the contents of a repository and save the results to a text file. The script continues to make requests to the repository until the `continuationToken` is null.

```
import requests
import json

repository_url = 'https://repo.company.com/'
source_repository = 'maven-hosted'
file_name = 'search_results.json'
source_url = repository_url \
   + '/service/rest/v1/search?repository=' \
   + source_repository

nx_token = None
read_again = True
items = []

while read_again == True:
  if not ( nx_token is None):
    url = source_url + "&continuationToken=" + nx_token

  response = requests.get(url)
  if response.status_code != 200:
    print('Error: ', response.status_code)
    exit(0)

  results = response.json()
  nx_token = results['continuationToken']
  items.extend(results['items'])

  if nx_token is None:
    read_again = False

pretty = json.dumps(items, indent=4)
with open(file_name, "w+") as file:
	file.write(pretty)
```

## Download artifacts using URI

Nexus Repository is designed to work with your build tools to pull artifacts from repositories using a repository-specific formatted URI.

Use this URI to download artifacts via other tools such as curl, get, or even through a browser directly.

Examples:

## Webhooks

Webhooks are defined as an HTTP callback. In simple terms, webhooks allow Nexus Repository administrators to configure HTTP-based callbacks to notify external services of important events happening within Nexus Repository.

Organizations are using webhooks in many ways to further automate their workflows, and integrate third party systems with key services. The Nexus Repository provides the ability to use webhooks for global auditing, repository based events, and for events on specific repositories.

### Using Webhooks

Setting up webhooks in Nexus Repository can be accomplished by any user with sufficient privilege to create *Capabilities* , generally an administrator.

For ease of testing Webhooks, you can use a service such as [RequestBin](https://requestb.in/) to quickly test out your desired Webhook. Alternatively any lightweight server that can allow you to see the contents of an HTTP POST will work.

### Enabling A Global Webhook Capability

To enable a global webhook, perform the following steps:

**Note:** A Global: Webhook capability for Event Type audit requires that you also enable the Audit capability, in order for events to be fed to the webhook.

This form also includes an option to use a *Secret Key* for sending your events with a HMAC payload digest.

**Note:** Webhooks will provide a `sha1` hash of the JSON body using a shared secret key. This allows you to verify the data integrity as well as its authenticity. The JSON body is hashed without whitespace and this hash is provided in the header as `X-Nexus-Webhook-Signature` .

After you enable the capability, you will now see the *Webhook: Global* capability in the list of *Capabilities* .

### Enabling A Repository Webhook Capability

To enable a Webhook for a specific repository, perform the following steps:

This form also includes an option to use a Secret Key for sending your events with a HMAC payload digest.

**Note:** Nexus Repository Manager Webhooks will provide a sha1 hash of the JSON body using a shared secret key. This allows you to verify the data integrity as well as its authenticity. The JSON body is hashed without whitespace and this hash is provided in the header as `X-Nexus-Webhook-Signature` .

After you enable the capability, you will now see the *Webhook: Repository* capability in the list of *Capabilities* .

### Working With HMAC Payloads

If you have enabled a secret key to generate an HMAC digest, a special header will be sent with all of your Webhook payloads. This header is `X-Nexus-Webhook-Signature` . It can be used to ensure that the message you receive is in fact what was originally generated.

For ease of getting you up and running with webhooks using HMAC, here is an example express based node.js script that can be used to verify that the payload you receive is what was originally sent.

**app.js**

```
const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const crypto = require('crypto');
const secretKey = 'mysecretkey';
 
 
app.use(bodyParser.json());
 
 
app.post('/', function(req, res) {
  const body = req.body;
  const signature = req.headers['x-nexus-webhook-signature'];
  var hmacDigest = crypto.createHmac("sha1",
secretKey).update(JSON.stringify(body)).digest("hex");
 
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

This script can also be used for testing as an alternative to [RequestBin](https://requestbin.com/) .

### Example Headers And Payloads

To work with a webhook, you need to know a bit about the payload you’ll be receiving. Each event you receive a payload for will contain special headers that describe what the event is.

**Example Headers**

```
X-Request-Id: d535c62b-063e-4ace-90ce-f7b579d6c37c
Content-Type: application/json; charset=UTF-8
User-Agent: Nexus/3.1.0-SNAPSHOT (PRO; Mac OS X; 10.11.1; x86_64; 1.8.0_60)
X-Nexus-Webhook-Signature: 687f3719b87232cf1c11b3ef7ea10c49218b6df1
X-Nexus-Webhook-Id: rm:repository:asset
X-Nexus-Webhook-Delivery: 7f4a6dde-5c68-4999-bcc0-a62f3fb8ae48
```

Of special importance are the following three headers:

A payload will be returned with each event type, an example of one for a repository asset webhook is shown below:

**Example Payload**

```
{
   "timestamp" : "2016-11-10T23:57:49.664+0000",
   "nodeId" : "52905B51-085CCABB-CEBBEAAD-16795588-FC927D93",
   "initiator" : "admin/127.0.0.1",
   "repositoryName" : "npm-proxy",
   "action" : "CREATED",
   "asset" : {
   "id" : "31c950c8eeeab78336308177ae9c441c",
   "assetId" : "bnBtLXByb3h5OjMxYzk1MGM4ZWVlYWI3ODMzNjMwODE3N2FlOWM0NDFj",
   "format" : "npm",
   "name" : "concrete"
  }
}
```

Events share common fields, described in detail below:

Below, you will find examples of many Payloads that are returned, to help you get up and running with webhooks in Nexus Repository Manager.

## Bundle Development

⚠️ **Warning:** The OSGi bundle capability has been removed from the Nexus Repository as of version 3.78.0. Any installations using bundles when upgrading to this version will find that the bundles are not loaded. This page is only for information purposes for prior releases.

Nexus Repository is built on top of the OSGi container [Apache Karaf](http://karaf.apache.org/) . This supporting core infrastructure provides a foundation for these editions. The functionality is encapsulated in several OSGi bundles. Each edition is composed of several bundles, that provide specific features.

Bundles can provide further functionality for the back end such as support for new repository formats, specific behavior for components, new tasks, and any other additional functionality as well as new user interface components and modifications. They can also group a number of these features in one bundle.

This section provides a high-level overview and information to begin developing your bundles for the Nexus platform, specifically the Nexus Repository.

Knowledge of Apache Maven and Java is required for your bundle development efforts. OSGi-related knowledge is highly relevant and beneficial. Please ensure to consult the documentation for the relevant projects, when necessary.

### Bundle Development Overview

Bundles for Nexus Repository are written in Java as the implementation language using Apache Maven as the build system. The [public code base](https://github.com/sonatype/nexus-public) may used as a starting point to investigate existing bundles and their source code.

The easiest way to create a new bundle project is to replicate a bundle with a similar functionality. Inspect the source code of bundles with similar functionality, and read the JavaDoc documentation for the involved classes.

To gain access to all the components needed for your bundle development, you have to proxy the Sonatype grid repository with the URL:

```
https://repository.sonatype.org/content/groups/sonatype-public-grid/
```

Set up your project to include inheriting from the parent of all the Nexus Repository bundles with the version you are targeting as follows.

### View Running Bundles

The Nexus Repository Manager application runs on the OSGi container Apache Felix. All features and plugins are managed by the container and are implemented as OSGi bundles. The *Bundles* feature view is available in the *System* section of the *Administration* main menu. It allows you to inspect a list of all the OSGi bundles that are deployed as part of the application and access detailed information about each bundle.

Find out more about OSGi and OSGi bundles on the website of the [OSGi Alliance](https://www.osgi.org/) .

Permission to access this page in your Nexus Repository Manager can be granted granularly using the nx-bundles privilege.

### Installing Bundles

To include your bundle in Nexus Repository, the bundle needs to be loaded by the OSGi container.

The default build assembles multiple bundles that form the foundation of Nexus Repository. These definitions are found in the [assemblies](https://github.com/sonatype/nexus-public/tree/master/assemblies/) module. The supported distributions are defined in the modules `nexus-oss-feature` and `nexus-pro-feature` , which are part of the internal code base.

### Contributing Bundles

Ideally, any new bundles created yield significant benefits for the overall community of users. Sonatype encourages the contribution of such bundles to the upstream repository and is offering support and help for such efforts.

The minimum steps for such contributions are:

- Create a pull request with the relevant changes to the [nexus-public repository](https://github.com/sonatype/nexus-public)
- Sign and submit a contributor license agreement to Sonatype

In further collaboration, Sontaype will decide upon the next steps on a case-by-case basis and work with you to:

- Create sufficient tests
- Provide access to upstream repositories
- Facilitate other infrastructure such as CI server builds
- Help you with verification and testing
- Work with you on user documentation and outreach
- Expose your work to the user community

### Support for a New Repository Format

This section examines the efforts required to implement support for a new repository format in the Nexus Repository Manager. By default, the repository manager includes support for various repository formats including `raw` -format, `maven2` -format and others.

When implementing support for a new repository format, it is important to get a good understanding of the format itself as well as the tools and the community working with the format. It might even be necessary to read and understand the source code of potential native, upstream implementations to support a format.

Following are a few questions that can provide some useful answers leading to a better understanding of the format

and necessary steps for implementation;

- What is this format all about?
- What tools (client/server) are involved?
- What communication is performed between client and server?
- Do any protocols or specifications exist?
- What authentication method needs to be supported by the repository manager?
- How can the repository manager authenticate against a proxied remote server?
- How does the concepts of components and assets used in Nexus Repository Manager map to the format?
- What is the best way to map the component identifier of name, version and group to the format?
- What format specific attributes should be stored as components and assets?
- Is it necessary to rewrite proxied metadata? E.g. proxied metadata contains absolute URLs to proxied server that it has to rewrite to point to repository manager.
- Are there any special features that should be considered?

To provide sufficient support for users, a new repository format needs to include a number of features:

- proxying components from remote repositories
- storing and managing components in a hosted repository
- exposing multiple repositories to users as a single repository group
- format-specific search criteria and the related search functionality

Depending on the specifics of the repository format being implemented a number of other features have to be provided or can optionally provide additional value to the user:

- any required tasks for maintenance of the repositories and their content
- client side tools to allow the standard tools to interact with the repositories on the repository manager
- custom features to display information about the repositories or their content in the user interface

The implementation of all these features for the raw -format can be found in the module `plugins/nexus-repository-raw` . The raw format is a good example code-base to expose as it presents the most simplistic repository format.

The Maven repository format as used by Apache Maven and many other tools is implemented in the `plugins/nexus-repository-maven` module. It can serve as another, slightly more complex, example. Examining the code base can be especially useful, if you know the Maven repository format.

## Nexus Repository API Reference

Below is a copy of the latest Nexus Repository API Swagger file, which is available in the Nexus Repository user interface under Settings → System → API

[https://sonatype.github.io/sonatype-documentation/api/nexus-repository/latest/nexus-repository-api.json](https://sonatype.github.io/sonatype-documentation/api/nexus-repository/latest/nexus-repository-api.json)

## Assets API

### Introduction

This set of endpoints is for interacting with assets directly.

### Endpoints

## Blob Store API

The Blob Store exposes HTTP endpoints for creating, updating, deleting, retrieving, and listing blob stores.

See the API section is found in the Settings menu under System → API of your Nexus Repository instance for detailed information about the Blob Store API including sample requests and responses.

### Endpoints

The blob stores REST API endpoints can be used to accomplish the following:

- List blob stores
- Delete blob store
- Create blob store
- Get blob store configuration
- Update blob store
- Get blob store quota

## Capabilities API

These REST API endpoints are used to manage capabilities for Nexus Repository. The user needs access to read and edit the `nexus:settings` permissions. Capabilities differ in their required properties. Review the capabilities documentation for list of capabilities, types, and properties.

See the Capabilities documentation

### Get Capabilities

The request returns a list of capabilities. The user requires the following permissions: ( `nexus:settings.read` )

```
GET /service/rest/v1/capabilities
```

Example

```
curl -u admin:admin123 -X GET http://localhost:8081/service/rest/v1/capabilities
```

Example response

```
[
  {
    "id": "018b####-49##-30##-1e##-09347#######",
    "type": "firewall.audit",
    "notes": "",
    "enabled": false,
    "properties": {
      "quarantine": "true",
      "repository": "npm-proxy"
    }
  }
]

```

### Create Capabilities

The user requires the following permissions: ( `nexus:settings.edit` ) The request to add a new capability is submitted in the body of a POST request. The endpoint will return a 201 when successful and a 409 when the name already exists.

```
POST /service/rest/v1/capabilities
```

```
{
  "type": "string",
  "notes": "string",
  "enabled": true,
  "properties": {
    "additionalProp1": "string",
    "additionalProp2": "string"
  }
}
```

The following parameters are included in the body of the request. Any that are not included as criteria in the request are set to `null` .

- `` - the type of capability to add.
- **** - set to true to enable the capability.
- `` - any details on the specific capability.
- **** - an object of additional properties to send. See the capabilities documentation for details on the required properties to include for each capability.

Example Request

```
curl -u admin:admin123
  -H 'accept:application/json'
  -H 'Content-Type: application/json'
  -d '{
    "type":"firewall.audit",
    "enabled":"true",
    "notes": "",
    "properties": {
        "repository":"npm-proxy", 
        "quarantine":"true"
    }}'
  -X POST http://localhost:8081/service/rest/v1/capabilities 
```

### Update Capability

The user requires the following permissions: ( `nexus:settings.edit` ) The request to update a capability with a PUT request. The endpoint will return a 201 when successful.

```
PUT /service/rest/v1/capabilities/{capabilityId}
```

Use the GET endpoint to locate the `id` property to use as the `capabilityId` .

### Remove Capability

The user requires the following permissions: ( `nexus:settings.delete` ) The request to remove a capability with a DELETE request. The endpoint will return a 201 when successful.

```
DELETE /service/rest/v1/capabilities/{capabilityId}
```

Use the GET endpoint to locate the `id` property to use as the `capabilityId` .

## Cleanup Policies API

These REST API endpoints are used to manage cleanup policies to Nexus Repository. The user needs access to read and edit the `nexus:settings` permissions.

Assigning cleanup policies will require the use of the Repositories API.

**Note:** Only available in Sonatype Nexus Repository TM Pro. Interested in a free trial? [Start here](https://www.sonatype.com/products/repository-pro/trial) .

### Get Cleanup Policies

Request returns a list of cleanup policies. The user requires the following permissions: ( `nexus:settings.read` )

```
GET /service/rest/v1/cleanup-policies
```

Example

```
curl -u admin:admin123 -X GET http://localhost:8081/service/rest/v1/cleanup-policies
```

Example response

```
[
  {
    "notes": "",
    "criteriaLastBlobUpdated": null,
    "criteriaLastDownloaded": null,
    "criteriaReleaseType": null,
    "crtieriaAsserRegex": ".*",
    "retain": null,
    "name": "test-cleanup",
    "format": "maven2",
  }
]
```

### Get Cleanup Policy by Policy Name

Required permissions ( `nexus:settings.read` )

```
GET /service/rest/v1/cleanup-policies/{name}
```

- **** - User created name for the cleanup policy

Example

```
curl -u admin:admin123 -X GET http://localhost:8081/service/rest/v1/cleanup-policies/test-cleanup
```

See the *GET Cleanup Policy* example for the response.

### Create Cleanup Policy

The user requires the following permissions: ( `nexus:settings.edit` ) The request to add a new cleanup policy is submitted in the body of a POST request. The endpoint will return a 201 when successful and a 409 when the name already exists.

```
POST /service/rest/v1/cleanup-policies
```

```
{
  "notes": "string",
  "criteriaLastBlobUpdated": 0,
  "criteriaLastDownloaded": 0,
  "criteriaReleaseType": "RELEASES",
  "criteriaAssetRegex": "string",
  "retain": null,
  "name": "policy-name",
  "format": "string"
}
```

The following parameters may be included in the body of the request. Any that are not included as criteria in the request are set to `null` . Some parameters are not accepted based on the supplied format.

See the Cleanup Policies documentation for details on which fields should be provided for a given format.

- `` - any details on the specific cleanup policy.
- `` - the age of the component in days.
- `` - the last time the component had been downloaded in days.
- `` - When needed, this is either *PRELEASE* or *RELEASE* .
- `` - a regex string to filter for specific asset paths.
- `` - number of versions to keep. Only available for Docker and Maven release repositories on PostgreSQL deployments.
- `` - the name of the policy needs to be unique and cannot be edited once set. Only letters, digits, underscores(_), hyphens(-), and dots(.) are allowed and may not start with underscore or dot.
- `` - the target format for the cleanup policy. Some formats have various capabilities and requirements. Note that you cannot currently specify all formats.

Example Request

```
curl -u admin:admin123 -H 'accept:application/json' -H 'Content-Type: application/json' -d '{"name":"test-cleanup","format":"maven2", "criteriaLastDownloaded":10}' -X POST http://localhost:8081/service/rest/v1/cleanup-policies
```

### Update Cleanup Policy

Modify existing cleanup policies. The user requires the following permissions: ( `nexus:settings.edit` ). Use the policy name as a path parameter and inside the body object. The request returns a 204 on a successful update or 404 when the policy name is not found.

```
PUT /service/rest/v1/cleanup-policies/{name}
```

See the Create Cleanup Policy for body parameters. The policy name may not be modified.

### Delete Cleanup Policy

Remove Cleanup Policy from Nexus Repository. The user requires the following permissions: ( `nexus:settings.edit` ). Returns a 204 response when the cleanup policy is successfully deleted, and a 404 when the policy name is not found.

```
DELETE /service/rest/v1/cleanup-policies/{name}
```

Example

```
curl -u admin:admin123 -X DELETE http://localhost:8081/service/rest/v1/cleanup-policies/test-cleanup
```

## Components API

### Introduction

This set of endpoints is for interacting with components directly.

### Endpoints

## Email API

The Email API exposes a set of endpoints for specifying and viewing SMTP server settings used by Nexus Repository for sending email.

See the API section found in the Settings menu under System → API of your Nexus Repository instance for detailed information about the email API including sample requests and responses.

### Endpoints

The email REST API endpoints can be used to accomplish the following:

- Get email configuration
- Set email configuration
- Disable email configuration
- Verify email configuration

## EULA REST API

Component downloads and uploads are blocked until a Nexus Administrator has agreed to the terms in the Sonatype Nexus Repository Community Edition end-user license agreement (EULA).

See [Sonatype Nexus Repository Community Edtion EULA](https://links.sonatype.com/products/nxrm/ce-eula) for the complete text.

To agree to the EULA, submit a POST request with the exact text from the `disclaimer` received from the GET request from the same endpoint while updating the `accepted` property to true.

### Endpoints

The following endpoints are available for the Nexus Repository EULA API. These endpoints require an administrator role with the `nexus:*` privilege to access and edit.

## HTTP Configuration API

The HTTP Configuration API allows Nexus Repository customers to manage the outbound HTTP settings.

Review the HTTP and HTTPS Request and Proxy Settings documentation for details.

### Default HTTP Settings in Nexus Repository

The default outbound HTTP settings in Nexus Repository are as follows:

### Get HTTP Settings

This request returns a list of outbound HTTP settings. The user requires the following permissions: ( `nexus:settings:read` )

```
GET /service/rest/v1/http
```

Example

```
curl -u admin:admin123 -X GET http://localhost:8081/service/rest/v1/http
```

The returned password fields are redacted for security.

### Update HTTP Settings

Send the configuration to update the outbound HTTP settings. The user requires the following permissions: ( `nexus:settings:update` )

```
PUT /service/rest/v1/http
```

The request requires the body parameter with the values to be set.

```
Example ValueModel{
  "nonProxyHosts": [
    "string"
  ],
  "userAgent": "string",
  "timeout": 3600,
  "retries": 10,
  "httpProxy": {
    "enabled": true,
    "host": "string",
    "port": "string",
    "authInfo": {
      "enabled": true,
      "username": "string",
      "password": "string",
      "ntlmHost": "string",
      "ntlmDomain": "string"
    }
  },
  "httpsProxy": {
    "enabled": true,
    "host": "string",
    "port": "string",
    "authInfo": {
      "enabled": true,
      "username": "string",
      "password": "string",
      "ntlmHost": "string",
      "ntlmDomain": "string"
    }
  }
}
```

### Delete HTTP Settings

Deletes the outbound HTTP settings. The user requires the following permissions: ( `nexus:settings:update` )

```
DELETE /service/rest/v1/http
```

Example

```
curl -u admin:admin123 -X DELETE http://localhost:8081/service/rest/v1/http
```

The response returns a 204 when successful

## Sonatype Repository Firewall API

The Repository Firewall API exposes HTTP endpoints for managing the connection details to the Repository Firewall service.

Authorization required, required permissions for endpoints should be applied (nexus:settings:**)

### Endpoints

The REST API endpoints are used for the following:

- **Manage Repository Firewall configuration** Get the configuration Update the configuration Setting the fail-open mode Disable/Enable the configuration Verify the configuration
- Get the configuration
- Update the configuration Setting the fail-open mode
- Setting the fail-open mode
- Disable/Enable the configuration
- Verify the configuration
- **Manage Firewall: Audit and Quarantine configuration for proxy repositories** Get the audit status for all proxy repositories Get the audit status by proxy repository name Set the audit status for a proxy repository Set the quarantine status for a proxy repository
- Get the audit status for all proxy repositories
- Get the audit status by proxy repository name
- Set the audit status for a proxy repository
- Set the quarantine status for a proxy repository

### Get the Repository Firewall configuration

Required user permissions ( `nexus:settings:read` )

```
GET /service/rest/v1/iq
```

Example Request

```
curl -X GET -u <nexus_username>:<nexus_password> "<nexus_base_url>/service/rest/v1/iq"
```

**Note:** Getting the configuration includes `#~NXRM~PLACEHOLDER~PASSWORD~#` instead of the password for security.

### Update the Repository Firewall configuration

Required user permissions ( `nexus:settings:edit` )

```
PUT /service/rest/v1/iq
```

This request requires a body with the server access parameters.

```
{
  "enabled": true, 
  "showLink": true,
  "url": "<iq_base_url>",
  "authenticationType": "USER", 
  "username": "<iq_username>", 
  "password": "<iq_password>",
  "useTrustStoreForUrl": true,
  "timeoutSeconds": 3600, 
  "failOpenModeEnabled": true
}
```

Example Request

```
curl -X PUT -u <nexus_username>:<nexus_password> -H 'Content-Type: application/json' -d '{"enabled": true, "showLink": true, "url": "<iq_base_url>","authenticationType": "USER","username": "admin","password": "admin123","useTrustStoreForUrl": true,"timeoutSeconds": 3600, "failOpenModeEnabled": true}' "<nexus_base_url>/service/rest/v1/iq"
```

### Managing the Audit for Proxy Repositories

Required user permissions ( `nexus:settings:read,update` ) in Nexus Repository version 3.70 or greater

## Licensing API

The Product Licensing API exposes a set of endpoints for License Management.

### Get Installed License

Get details on the current installed license.

```
curl -X 'GET' \
  'https://{nexusHost}/service/rest/v1/system/license' \
  -H 'accept: application/json' \
  -u {username}:{password}

```

### Install a License

Install the license using the Licensing REST API. The Swagger UI does not allow for installing a license file.

```
POST /service/rest/v1/system/license
```

Example Request

```
curl -v -X 'POST' \
  'https://{nexusHost}/service/rest/v1/system/license' \
  -H 'Content-Type: application/octet-stream' \
  -H 'Accept: application/json' \
  -u {username}:{password} \
  --data-binary @/absolute/path/to/license.lic 

```

### Uninstall a License

Uninstall the license using the Licensing REST API

```
DELETE /service/rest/v1/system/license
```

Example Request

```
curl -X 'DELETE' \
  'https://{nexusHost}/service/rest/v1/system/license' \
  -H 'accept: application/json' \
  -u {username}:{password}

```

## Lifecycle API

⚠️ **Warning:** These operations are intended to be used with the guidance of Sonatype support. Usage without the supervision of Sonatype is not supported or recommended.

### Introduction

The Lifecycle API allows Nexus Repository Manager administrators to change the phase in which an Nexus Repository instance is running. A lifecycle phase is a step in the start-up process used to group similar components and ensure that their dependencies are started before them. In order of execution during startup, the phases are:

### Endpoints

## Maintenance API

These high availability clustering-specific REST endpoints allow the user to inspect and manipulate the state of a node in an Orient database cluster. The expectation is that these will be used mainly for troubleshooting and recovery operations.

⚠️ **Warning:** **High Availability Clustering** is a legacy feature that only works on the Orient database. Use our high availability or resilient deployment options described in the Resiliency and High Availability documentation.

### Introduction

**Possible Database Names:** component, config, security

### Endpoints

## Nodes API

**Note:** Only available in Sonatype Nexus Repository TM Pro. Interested in a free trial? [Start here](https://www.sonatype.com/products/repository-pro/trial) .

### Introduction

These endpoints allow us to get information about the nodes in the current cluster and update the friendly names of individual nodes. The list of nodes returned is a view of the state of the system and cannot be edited through this API. From this API, nodes can be assigned friendly names, but that is currently the only editable attribute. The friendly names may provide a more convenient mechanism to identify individual nodes for administrative activities.

### Endpoints

## Read-Only API

### Introduction

This set of endpoints is used to enable and disable read-only mode on the underlying database. This is useful when conducting some maintenance activities.

⚠️ **Warning:** This is a system-level feature that prevents changes to the underlying database. Do not use this feature if you want developers to download components from Nexus Repository, as this feature may prevent that from working. This feature is only appropriate for installs that use the legacy OrientDB embedded database.

### Endpoints

## Repositories API

This set of endpoints is for interacting with repositories directly. These endpoints are used to create, update, and retrieve repository configuration. See the embedded Swagger documentation for details on how each format is used.

Accessing the documentation can be found using the following link:

```
<server-url>/#admin/system/api
```

### List Repositories Example

```
GET /service/rest/v1/repositories
```

This endpoint lists the repositories the authenticated user has the browse permission to access. The ordering of results are consistent across queries, however, they are not alphabetical nor paginated.

```
curl -u admin:admin123 -X GET http://localhost:8081/service/rest/v1/repositories
```

This produces a response listing the repositories the user has permission to browse:

```
[{
  "name": "nuget.org-proxy",
  "format": "nuget",
  "type": "proxy",
  "url": "http://localhost:8081/repository/nuget.org-proxy",
  "attributes": {
    "proxy": {
      "remoteUrl" : "https://www.nuget.org/api/v2/"
    }
  }
},{
  "name": "maven-releases",
  "format": "maven2",
  "type": "hosted",
  "url": "http://localhost:8081/repository/maven-releases"
}]
```

### Add a Repository Example

The below example is taken from the Swagger UI for adding a Maven-hosted repository and is listed for demonstration purposes only. Each format and repository type has different requirements that are documented in the Swagger interface. Building your query through the Swagger interface is recommended.

```
curl -X POST -u admin:admin123 'http://localhost:8081/service/rest/v1/repositories/maven/hosted' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'NX-ANTI-CSRF-TOKEN: 0.2000863451060393' \
  -H 'X-Nexus-UI: true' \
  -d '{
  "name": "maven-internal",
  "online": true,
  "storage": {
    "blobStoreName": "default",
    "strictContentTypeValidation": true,
    "writePolicy": "allow_once"
  },
  "cleanup": {
    "policyNames": [
      "string"
    ]
  },
  "component": {
    "proprietaryComponents": true
  },
  "maven": {
    "versionPolicy": "MIXED",
    "layoutPolicy": "STRICT",
    "contentDisposition": "ATTACHMENT"
  }
}
```

## Search API

The Search API facilitates searching for components and assets in addition to downloading a specific asset.

Details about these endpoints are described in the generated documentation in Repository Manager under the administrative view System/API.

```
<nexus_url>/#admin/system/api
```

These endpoints use a pagination strategy that is used to iterate through search results.

### Notable Search Functionality Differences Between Environments

Due to ongoing work for improving component search in Sonatype Nexus Repository, some functionality differences currently exist between deployments using OrientDB, H2, PostgreSQL, and/or High Availability (HA).

Specific differences and considerations are documented in the Searching for Components section.

### Empty Values

Starting in Sonatype Nexus Repository version 3.57.0, we made enhancements to the Search APIs to improve the behavior for query parameters on fields that accept empty values.

An empty value for most fields is treated as “specifically empty" instead of the former behavior of treating it like a wildcard.

The repository and format parameters cannot be empty as every component is stored in a repository and format. These fields are never empty.

### Search Components

```
GET /service/rest/v1/search
```

Find components based on general and format-specific attributes. The search uses the same mechanism used by the Repository Manager UI to find components.

The search takes the form of a GET request against the endpoint which returns a JSON document with information about the components that are found.

In this example, we search for components in the `maven-central` repository which has a group of `org.osgi`

```
curl -u admin:admin123 -X GET 'http://localhost:8081/service/rest/v1/search?repository=maven-central&group=org.osgi'
```

This returns a JSON document containing a list of items that correspond to the components found during the search:

```
{
  "items" : [ {
    "id" : "bWF2ZW4tY2VudHJhbDoyZTQ3ZGRhMGYxYjU1NWUwNzE1OWRjOWY5ZGQzZmVmNA",
    "repository": "maven-central",
    "format": "maven2",
    "group": "org.osgi",
    "name": "org.osgi.core",
    "version": "4.3.1",
    "assets": [ {
      "downloadUrl": "http://localhost:8081/repository/maven-central/org/osgi/org.osgi.core/4.3.1/org.osgi.core-4.3.1-sources.jar",
      "path": "org/osgi/org.osgi.core/4.3.1/org.osgi.core-4.3.1-sources.jar",
      "id" : "bWF2ZW4tY2VudHJhbDplMDE4OGVkMDcyOGZhNjhmNDExNzU2OGU1MjQ2NjZiYg",
      "repository": "maven-central",
      "format": "maven2",
      "checksum": {
        "sha1" : "80bfafcf783988442b3a58318face1d2132db33d",
        "md5" : "87ee0258b79dc852626b91818316b9c3"
      }
    }, {
      "downloadUrl": "http://localhost:8081/repository/maven-central/org/osgi/org.osgi.core/4.3.1/org.osgi.core-4.3.1.jar",
      "path": "org/osgi/org.osgi.core/4.3.1/org.osgi.core-4.3.1.jar",
      "id": "bWF2ZW4tY2VudHJhbDpkMDY0ODA0YThlZDVhZDZlNjhmZGU5MWNmM2NiZTgzMw",
      "repository": "maven-central",
      "format": "maven2",
      "checksum": {
        "sha1" : "5458ffe2ba049e76c29f2df2dc3ffccddf8b839e",
        "md5" : "8053bbc1b55d51f5abae005625209d08"
      }
    }, {
      "downloadUrl": "http://localhost:8081/repository/maven-central/org/osgi/org.osgi.core/4.3.1/org.osgi.core-4.3.1.pom",
      "path": "org/osgi/org.osgi.core/4.3.1/org.osgi.core-4.3.1.pom",
      "id": "bWF2ZW4tY2VudHJhbDo2NTRiYjdkMGE1OTIxMzg1OWZhMTVkMzNmYWU1ZmY3OA",
      "repository": "maven-central",
      "format": "maven2",
      "checksum": {
        "sha1" : "79391fc69dd72ad1fd983d01b4572f93f644882b",
        "md5" : "3d87a59bcdb4b131d9a63e87e0ed924a"
      }
    } ]
  } ],
  "continuationToken": null
}
```

### Search Assets

```
GET /service/rest/v1/search/assets
```

This endpoint is focused on searching for assets. All of the same search criteria are available as in the component search above, but only assets will be returned.

Let's again search the maven-central repository for assets that have a group of `org.osgi`

```
curl -u admin:admin123 -X GET 'http://localhost:8081/service/rest/v1/search/assets?repository=maven-central&group=org.osgi'
```

This returns a JSON document containing a list of items corresponding to the assets found during the search:

```
{
  "items" : [ {
    "downloadUrl": "http://localhost:8081/repository/maven-central/org/osgi/org.osgi.core/4.3.1/org.osgi.core-4.3.1-sources.jar",
    "path": "org/osgi/org.osgi.core/4.3.1/org.osgi.core-4.3.1-sources.jar",
    "id" : "bWF2ZW4tY2VudHJhbDplMDE4OGVkMDcyOGZhNjhmNDExNzU2OGU1MjQ2NjZiYg",
    "repository": "maven-central",
    "format": "maven2",
    "checksum": {
      "sha1" : "80bfafcf783988442b3a58318face1d2132db33d",
      "md5" : "87ee0258b79dc852626b91818316b9c3"
    }
  }, {
    "downloadUrl": "http://localhost:8081/repository/maven-central/org/osgi/org.osgi.core/4.3.1/org.osgi.core-4.3.1.jar",
    "path": "org/osgi/org.osgi.core/4.3.1/org.osgi.core-4.3.1.jar",
    "id": "bWF2ZW4tY2VudHJhbDpkMDY0ODA0YThlZDVhZDZlNjhmZGU5MWNmM2NiZTgzMw",
    "repository": "maven-central",
    "format": "maven2",
    "checksum": {
      "sha1" : "5458ffe2ba049e76c29f2df2dc3ffccddf8b839e",
      "md5" : "8053bbc1b55d51f5abae005625209d08"
    }
  }, {
    "downloadUrl": "http://localhost:8081/repository/maven-central/org/osgi/org.osgi.core/4.3.1/org.osgi.core-4.3.1.pom",
    "path" : "org/osgi/org.osgi.core/4.3.1/org.osgi.core-4.3.1.pom",
    "id" : "bWF2ZW4tY2VudHJhbDo2NTRiYjdkMGE1OTIxMzg1OWZhMTVkMzNmYWU1ZmY3OA",
    "repository": "maven-central",
    "format": "maven2",
    "checksum": {
      "sha1" : "79391fc69dd72ad1fd983d01b4572f93f644882b",
      "md5" : "3d87a59bcdb4b131d9a63e87e0ed924a"
    }
  } ],
  "continuationToken": null
}
```

This shows us that we found three assets and that there are no additional pages of results.

### Search and Download Asset

```
GET /service/rest/v1/search/assets/download
```

This endpoint is specifically designed to search for one asset and then redirect the request to the `downloadUrl` of that asset.

Let's say we want to download the asset corresponding to a jar whose group is `org.osgi` , name is `org.osgi.core` , and version is `4.3.1` .

To achieve this, the search must return a single asset. Continuing our example, we can use the asset search endpoint above to refine our search until it returns a single asset:

```
curl -u admin:admin123 -X GET 'http://localhost:8081/service/rest/v1/search/assets?group=org.osgi&name=org.osgi.core&version=4.3.1&maven.extension=jar&maven.classifier'
```

In the above example, the last parameter `maven.classifier` has no value. This indicates that the matched asset should have no classifier.

**Note:** Using the full parameter name is not always required. For example, you may use `classifier` instead of the full `maven.classifier` .

The response returned by the above looks like this:

**Example Response**

```
{
  "items" : [ {
    "downloadUrl": "http://localhost:8081/repository/maven-central/org/osgi/org.osgi.core/4.3.1/org.osgi.core-4.3.1.jar",
    "path": "org/osgi/org.osgi.core/4.3.1/org.osgi.core-4.3.1.jar",
    "id": "bWF2ZW4tY2VudHJhbDpkMDY0ODA0YThlZDVhZDZlNjhmZGU5MWNmM2NiZTgzMw",
    "repository": "maven-central",
    "format": "maven2",
    "checksum": {
      "sha1" : "5458ffe2ba049e76c29f2df2dc3ffccddf8b839e",
      "md5" : "8053bbc1b55d51f5abae005625209d08"
    }
  } ],
  "continuationToken": null
}
```

Then we can append `/download` to produce the URL we can use to download the asset:

```
curl -L -u admin:admin123 -X GET 'http://localhost:8081/service/rest/v1/search/assets/download?group=org.osgi&name=org.osgi.core&version=4.3.1&maven.extension=jar&maven.classifier'
```

If successful, this will give us a 302 response and redirect us to the repository manager download URL for the asset. To follow a redirect with curl you will need a -L parameter.

**Example Response**

```
HTTP/1.1 302 Found
Content-Length: 0
Date: Fri, 19 Jan 2018 17:34:21 GMT
Location: http://localhost:8081/repository/maven-central/org/osgi/org.osgi.core/4.3.1/org.osgi.core-4.3.1.jar
...
```

Note that the search parameters in the example contain a parameter ( `maven.classifier` ) with no value:

```
...?group=org.osgi&name=org.osgi.core&version=4.3.1&maven.extension=jar&maven.classifier
```

Specifying a parameter with no value is an indicator to the search endpoint to only return assets that correspondingly have no value for that parameter. This technique can be used to filter down search results to a single asset for some formats such as Maven where the component contains multiple assets that match all search criteria specified right up to the extension. For example, a Maven component can have the actual JAR file for a library, plus have a source JAR. In these cases, just specifying `maven.extension=jar` is not specific enough to return a single asset but we can further narrow the search results by specifying that we want only the main JAR file asset, not the sources JAR by including an empty `maven.classifier` parameter.

Alternatively, let's now assume that instead of wanting the main `org.osgi.core` JAR we desire to search for and download the sources JAR (e.g. `org.osgi.core-4.3.1-sources.jar` ). That is, we want to search for and download the asset corresponding to a jar whose group is `org.osgi` , name is `org.osgi.core` , version is 4.3.1 and maven.classifier is `sources` .

We can achieve this by using the asset search endpoint and including the `maven.classifier` with a specified value of `sources` :

```
curl -L -u admin:admin123 -X GET 'http://localhost:8081/service/rest/v1/search/assets/download?group=org.osgi&name=org.osgi.core&version=4.3.1&maven.classifier=sources'
```

If successful, this will give us a 302 response and redirect us to the repository manager download URL for the asset. To follow a redirect with curl you will need a -L parameter.

```
HTTP/1.1 302 Found
Content-Length: 0
Date: Fri, 19 Jan 2018 17:34:21 GMT
Location: http://localhost:8081/repository/maven-central/org/osgi/org.osgi.core/4.3.1/org.osgi.core-4.3.1-sources.jar
...
```

## Security Management API

See the API documentation found in the Settings menu under System of Nexus Repository.

### Content Selectors

The content selectors REST API endpoints can be used to create and manage content selectors:

- list the content selectors
- create or modify content selectors

### LDAP

The LDAP endpoints can be used to accomplish the following:

- List all LDAP servers
- Create LDAP server
- Retrieve the details of a single LDAP server
- Update LDAP server
- Delete LDAP server
- Change LDAP server ordering

### Privileges

The privileges REST API endpoints can be used to create and manage privileges:

- list the privileges
- create or modify privileges

### Roles

The roles REST API endpoints can be used to create and manage roles and their permissions within Nexus Repository:

- list the roles from any configured user source (internal or external)
- create or modify local roles and external role mappings

### Users

The users REST API endpoints can be used to create and manage users and their permissions within Nexus Repository:

- search for users available to NXRM whether they were defined locally or from a configured authentication source such as LDAP
- create or modify local users
- change the roles associated with an external user
- reset an individual user token
- reset all user tokens in the system

**Note:** The users REST API can accept the following realm names associated with user tokens: `LdapRealm` , `Crowd` , `SamlRealm` , and `NexusAuthenticatingRealm` .

### User Sources

This endpoint provides a list of the available users sources in Nexus Repository. Other REST endpoints use these to indicate the source of certain types of entities (e.g., a user from an LDAP server).

## Service Metrics Data API

This topic covers how to programmatically retrieve usage metrics from the API. This API is not currently available in the Swagger documentation that displays within the Nexus Repository user interface.

The `nexus:metrics:read` privilege is required to use this API.

Query the `/service/metrics/data` endpoint for the fields specified in the table below.

* "Metric" in this instance refers to the corresponding metric available in the user interface via the Usage Center. For maximum data parity with the user interface metrics information, you will want to retrieve this data before midnight (based on server time) each day.

## Script API

⚠️ **Warning:** As of release 3.21.2, the Groovy scripting engine is **disabled by default as a security best practice** . This affects Groovy scripts as used through the REST API and scheduled tasks.

This is a powerful scripting API that provides methods to simplify provisioning and executing other complex tasks in the repository manager. These APIs can be invoked from scripts that are published to the repository manager and executed within the application server.

### Enabling Scripting

While keeping scripting disabled is a security best practice, you can enable it when necessary.

To temporarily allow adding/editing a script source, take the following steps:

### Endpoints

### Writing Scripts

The scripting language used on the repository manager is [Groovy](http://www.groovy-lang.org/) . Any editor can be used to author the scripts.

For recommendations on configuring a stable scripting environment and tips from Sonatype, see [this knowledge base article](https://support.sonatype.com/hc/en-us/articles/115015812727-Nexus-3-Groovy-Script-development-environment-setup) .

The available APIs are contained in a number of JAR files. All these files, including JavaDoc and Sources archives, are available from the [Central Repository](http://search.maven.org/) . They can be manually downloaded and extracted. E.g. the different versions and the specific JAR files for `org.sonatype.nexus:nexus-core` are available in versioned directories at `https://repo1.maven.org/maven2/org/sonatype/nexus/nexus-core/` .

This manual process can be simplified and improved by the usage of a Maven project declaring the relevant components as dependencies. An example project with this setup called `nexus-script-example` and a few scripts are available in the [example project](https://github.com/sonatype/nexus-book-examples/tree/nexus-3.x) .

**Maven Project pom.xml Declaring the API Dependencies for Scripting**

```
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
 
  <groupId>com.example.automation</groupId>
  <artifactId>nexus-script-demo</artifactId>
  <version>1.0-SNAPSHOT</version>
 
  <properties>
    <nx-version>3.3.0-01</nx-version>
  </properties>
  <dependencies>
    <dependency>
      <groupId>org.sonatype.nexus</groupId>
      <artifactId>nexus-core</artifactId>
      <version>${nx-version}</version>
    </dependency>
    <dependency>
      <groupId>org.sonatype.nexus</groupId>
      <artifactId>nexus-script</artifactId>
      <version>${nx-version}</version>
    </dependency>
    <dependency>
      <groupId>org.sonatype.nexus</groupId>
      <artifactId>nexus-security</artifactId>
      <version>${nx-version}</version>
    </dependency>
    <dependency>
      <groupId>org.sonatype.nexus.plugins</groupId>
      <artifactId>nexus-script-plugin</artifactId>
      <version>${nx-version}</version>
    </dependency>
  </dependencies>
</project>
```

Development environments such as IntelliJ IDEA or Eclipse IDE can download the relevant JavaDoc and Sources JAR files to ease your development. Typically you would create your scripts in `src/main/groovy` or `src/main/scripts` .

The scripting API exposes specific tooling for IntelliJ IDEA that allows you to get access to code completion and similar convenience features while writing your scripts in this Maven project. Currently, the API exposes four main providers with numerous convenient methods:

- Core API: allows a script to set global configuration options
- Security API: allows a script to add users, roles, and privileges
- Blob Store API: allows a script to create new blob stores
- Repository API: provides a simple, format-specific interface for creating repositories

The API is deliberately designed to be simple to use. It encapsulates complex configurations in single-method invocations. Many of the included methods use default values that can be omitted. For example, the method to create a hosted repository using the Maven format in the simplest usage simply requires a name.

```
repository.createMavenHosted("private")
```

This method simply uses the default values for the rest of the parameters and is therefore equivalent to:

```
repository.createMavenHosted("private", BlobStoreManager.DEFAULT_BLOBSTORE_NAME, true, VersionPolicy.RELEASE, WritePolicy.ALLOW_ONCE, LayoutPolicy.STRICT)
```

You can inspect the default values in the API documentation available by inspecting the declaration of the specific methods in your IDE or by viewing the JavaDoc.

In terms of overall complexity of the scripts created, it is best to break large tasks up into multiple scripts and therefore invocations.

### Managing and Running Scripts

Once you have completed the creation of your script, you need to publish it to the repository manager for execution. This is done by REST API invocations or through the UI.

To run a script from the Nexus Repository UI, you must create a scheduled task. Navigate to *Tasks* from the *Settings* menu, and create a task of type *Admin - Execute script* . Enter the script source into the *Source* form field. Set the task frequency to *Manual* (or another setting to execute on a schedule) and save. The script can then be executed by selecting it from the list of tasks and pressing the *Run* button.

```
http://localhost:8081/service/rest/v1/script
```

This endpoint accepts JSON-formatted payloads with your script as the `content` .

Example JSON formatted file `maven.json` with a simple repository creation script:

```
{
  "name": "maven",
  "type": "groovy",
  "content": "repository.createMavenHosted('private')"
}
```

The JSON file `maven.json` located in the current directory can be published to the repository manager with an HTTP POST like:

```
curl -v -X POST -u admin:admin123 --header "Content-Type: application/json" 'http://localhost:8081/service/rest/v1/script' -d @maven.json
```

A list of scripts stored on the repository manager can be accessed with:

```
curl -v -X GET -u admin:admin123 'http://localhost:8081/service/rest/v1/script'
```

The same call with a script name appended returns the actual script content.

A script can be executed by sending a POST to the run method of the specific script.

```
curl -v -X POST -u admin:admin123 --header "Content-Type: text/plain" 'http://localhost:8081/service/rest/v1/script/maven/run'
```

A successful execution should result in a `HTTP/1.1 200 OK` .

Scripts can be removed with a HTTP DELETE operation to the specific script:

```
curl -v -X DELETE -u admin:admin123 'http://localhost:8081/service/rest/v1/script/maven'
```

### Examples

The API for scripts is capable of a number of different tasks. This section provides examples for script writing, publishing and executing them.

The **** project in the [scripting section of the example project](https://github.com/sonatype-nexus-community/nexus-scripting-examples) includes a number of JSON file with simple scripts:

****

simplest script to create a hosted Maven repository

****

simple script to create a hosted and proxy repository as well as a repository group for npm usage

****

simple script to create a hosted and proxy repository as well as a repository group for bower usage

****

parameterized script to enable or disable anonymous access

Simple shell scripts are added to contain the curl invocations to manage scripts via the REST API:

****

Upload a specified JSON file

****

Delete a script specified by its name

****

List all deployed scripts

****

Run a script specified by its name

****

Run the anonymous script on the server with the parameter true or false

****

Update an existing script by specifying the name and the JSON file to use for the update

An example sequence of creating and running a script is:

```
./create.sh maven.json
./run.sh maven
```

Subsequently you could list all scripts and delete the maven script with:

```
./list.sh
./delete.sh maven
```

Since scripts are typically longer than a single line and creating them in a separate file in the IDE is recommended, using a helper script that formats a .groovy file into a JSON file and submits it to the repository manager can be a convenient approach.

The **** project in the [scripting section of example project](https://github.com/sonatype-nexus-community/nexus-scripting-examples) includes an example implementation using Groovy invoked from a shell script. All scripts in this folder can be published and executed via the `provision.sh` file. This results in the download of all required dependencies and the upload and execution of the referenced script. Alternatively, you can provision the scripts individually:

```
groovy addUpdateScript.groovy -u "admin" -p "admin123" -n "raw" -f "rawRepositories.groovy" -h "http://localhost:8081"
curl -v -X POST -u admin:admin123 --header "Content-Type: text/plain" "http://localhost:8081/service/rest/v1/script/raw/run"
```

The following scripts are available:

****

for NPM and Bower repositories suitable for server-side and client JavaScript-based development

****

creates a new blob store and uses it for a hosted raw repository

****

disables anonymous access, creates a new administrator account, creates a new role with a simple expansion to anonymous user role and a user, creates a new role with publishing access to all repositories and a user

****

configures the base URL capability and a proxy server

Logging from your scripts into the repository manager logs is automatically available and performed with the usual calls:

```
log.info('User jane.doe created')
```

The result of the last script line is by default returned as a string. This can be a message as simple as `Success!` or more complex structured data.

For instance, you can easily return JSON using built-in Groovy classes like:

```
return groovy.json.JsonOutput.toJson([result: 'Success!'])
```

which looks like:

```
{
    "result": "Success!"
}
```

Passing parameters to the script can use JSON encoded arguments like:

```
{
  "id": "foo",
  "name": "bar",
  "description": "baz",
  "privilegeIds": ["nx-all"],
  "roleIds": ["nx-admin"]
}
```

which in turn can be parsed using the `JsonSlurper` class in the script:

```
import groovy.json.JsonSlurper
 
//expects json string with appropriate content to be passed in
def role = new JsonSlurper().parseText(args)
 
security.addRole(role.id, role.name, role.description, role.privilegeIds, role.roleIds)
```

You can read more about how to work with XML and JSON with Groovy on [http://groovy-lang.org/processing-xml.html](http://groovy-lang.org/processing-xml.html) and [http://groovy-lang.org/json.html](http://groovy-lang.org/json.html) .

## Status API

This set of endpoints is used to determine the status of an instance. This is useful when conducting some maintenance activities.

All three of the endpoints below require that the port is available and Java is running.

**Note:** These checks only relay Nexus Repository's state and are not hardware checks. They do not validate whether an external database is functional/reachable or if disk access is available; those tasks require dedicated monitoring software. Nexus Repository can only report on its own internal state.

### Status Endpoint

```
GET /service/rest/v1/status
```

This endpoint validates that the server can respond to read requests.

**Curl Example**

```
curl -X GET http://localhost:8081/service/rest/v1/status
```

The response code contains the information. A 200 indicates the instance can serve read requests, a 503 otherwise.

### Writable Endpoint

```
GET /service/rest/v1/status/writable
```

This endpoint validates that server can respond to read and write requests (i.e., that Nexus Repository is not in read-only mode).

**Curl Example**

```
curl -X GET http://localhost:8081/service/rest/v1/status/writable
```

The response code contains the information. A 200 indicates the instance can serve write and read requests, a 503 otherwise.

### Check Endpoint

```
GET /service/rest/v1/status/check
```

This endpoint returns the results of the system status checks.

**Curl Example**

```
curl -X GET http://localhost:8081/service/rest/v1/status/check
```

The response contains the system status check results, such as in the example below:

These results are also available in the user interface under *Settings* → *Support* → *Status*

Click here to expand...

```
{
  "additionalProp1": {
    "healthy": true,
    "message": "string",
    "error": {
      "cause": "string",
      "stackTrace": [
        {
          "methodName": "string",
          "fileName": "string",
          "lineNumber": 0,
          "className": "string",
          "nativeMethod": true
        }
      ],
      "message": "string",
      "localizedMessage": "string",
      "suppressed": [
        "string"
      ]
    },
    "details": {
      "additionalProp1": {},
      "additionalProp2": {},
      "additionalProp3": {}
    },
    "time": 0,
    "duration": 0,
    "timestamp": "string"
  },
  "additionalProp2": {
    "healthy": true,
    "message": "string",
    "error": {
      "cause": "string",
      "stackTrace": [
        {
          "methodName": "string",
          "fileName": "string",
          "lineNumber": 0,
          "className": "string",
          "nativeMethod": true
        }
      ],
      "message": "string",
      "localizedMessage": "string",
      "suppressed": [
        "string"
      ]
    },
    "details": {
      "additionalProp1": {},
      "additionalProp2": {},
      "additionalProp3": {}
    },
    "time": 0,
    "duration": 0,
    "timestamp": "string"
  },
  "additionalProp3": {
    "healthy": true,
    "message": "string",
    "error": {
      "cause": "string",
      "stackTrace": [
        {
          "methodName": "string",
          "fileName": "string",
          "lineNumber": 0,
          "className": "string",
          "nativeMethod": true
        }
      ],
      "message": "string",
      "localizedMessage": "string",
      "suppressed": [
        "string"
      ]
    },
    "details": {
      "additionalProp1": {},
      "additionalProp2": {},
      "additionalProp3": {}
    },
    "time": 0,
    "duration": 0,
    "timestamp": "string"
  }
}
```

## Support API

### Introduction

This endpoint allows us to download a support zip from an instance.

### Endpoints

## Tasks API

This set of endpoints allows us to interact with tasks that have been created in the Nexus Repository. You will need appropriate privileges to view, create, update, or delete tasks.

See the Tasks documentation.

### List Tasks

This endpoint iterate through a listing of all the existing tasks.

```
GET /service/rest/v1/tasks
```

```
curl 'http://localhost:8081/service/rest/v1/tasks' \
  -u admin:admin123 \
  -H 'accept: application/json'
```

Include the type of tasks filter the results.

```
curl 'http://localhost:8081/service/rest/v1/tasks?type=assetBlob.cleanup' \
  -u admin:admin123 \
  -H 'accept: application/json'

```

### Get Task by Identifier

This endpoint retrieves the details on an individual task.

```
GET /service/rest/v1/tasks/{id}
```

```
curl 'http://localhost:8081/service/rest/v1/tasks/0261aed9-9f29-447b-8794-f21693b1f9ac' \
  -u admin:admin123 \
  -H 'accept: application/json'
```

### Run Task

This endpoint runs an individual task.

```
POST /service/rest/v1/tasks/{id}/run
```

```
curl -u admin:admin123 -X POST 'http://localhost:8081/service/rest/v1/tasks/0261aed9-9f29-447b-8794-f21693b1f9ac/run'
```

```
HTTP/1.1 204 No Content
Date: Mon, 22 Jan 2018 22:19:47 GMT
...
```

### Stop Task

```
POST /service/rest/v1/tasks/{id}/stop
```

This endpoint allows us to stop an individual task. This is the equivalent of cancelling a task in the repository manager UI. Note that not all tasks will respond to a cancellation request.

For example to stop the "Hello World" task:

```
curl -u admin:admin123 -X POST 'http://localhost:8081/service/rest/v1/tasks/0261aed9-9f29-447b-8794-f21693b1f9ac/stop'
```

In this example the "Hello World" task was not running when the stop request was made. We will get a 409 response code that signifies that the requested task was not currently running:

**Example Response**

```
HTTP/1.1 409 Conflict
Content-Length: 0
Date: Mon, 22 Jan 2018 22:22:33 GMT
...
```

### Nexus Repository Pro Endpoints

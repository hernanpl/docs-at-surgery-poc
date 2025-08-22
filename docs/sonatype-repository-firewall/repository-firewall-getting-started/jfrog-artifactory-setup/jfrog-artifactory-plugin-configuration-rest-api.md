---
layout: default
title: "JFrog Artifactory Plugin Configuration REST API"
parent: JFrog Artifactory Setup
nav_order: 3
---

# JFrog Artifactory Plugin Configuration REST API

PLUGIN RELEASE 2.4.8

In the following examples, the calls are made to your JFrog Artifactory server by substituting an admin username and password as well as your JFrog Artifactory URL.

Sensitive configuration properties will have their values obfuscated in returned API requests.

## Get Configuration Properties

The getFirewallProperties endpoint returns all configuration properties.

```
curl -u username:password "https://artifactory.example.com/api/plugins/execute/getFirewallProperties"
```

Specific configuration properties may be requested using the same endpoint; both keys and values.

```
curl -u username:password "https://artifactory.example.com/api/plugins/execute/getFirewallProperties?params=keys=k1,k2"
```

## Add or Update Configuration Properties

This sets key {parameter1} to value {value1} and key {parameter2} to value {value2}.

```
curl -u username:password -X PUT "https://artifactory.example.com/api/plugins/execute/addOrUpdateFirewallProperties?params={parameter1}={value-1}%7C{parameter-2}={value-2}"
```

## Remove a Configuration Property

This API endpoint removes the {parameter1} and {parameter2} configuration properties.

```
curl -u username:password -X DELETE "https://artifactory.example.com/api/plugins/execute/removeFirewallProperties?params=keys={parameter1},{parameter2}"
```

## Set the Configuration File Content

This endpoint sets the entire configuration file content to that of the given firewall.properties file. Note the following before using this endpoint:

- This endpoint requires the submitted file encoding to be ISO 8859-1.
- All configuration file properties will be overridden using this endpoint.

```
curl -u username:password -X PUT --data-binary @firewall.properties "https://artifactory.example.com/api/plugins/execute/setFirewallProperties"
```

## Reload Artifactory Plugins

This endpoint reloads the Firewall for Artifactory plugin after changes in the plugin configuration.

Update the plugin by calling the following custom implementation of the [JFrog reload plugins endpoint](https://jfrog.com/help/r/jfrog-rest-apis/reload-plugins) . This endpoint reloads the plugin when modifications are made since the last time the call was made.

```
curl -u username:password -X POST "https://artifactory.example.com/api/plugins/execute/reload"
```

## Check IQ Server Connection

This endpoint will check the IQ Server connection.

- When the connection is successful a 200 status code is returned.
- A different status code is returned by the IQ Server connection attempt.

The returned body will contain the non-sensitive IQ Server connection properties for review.

```
curl -u username:password -X GET "https://artifactory.example.com/api/plugins/execute/checkIQConnection"
```

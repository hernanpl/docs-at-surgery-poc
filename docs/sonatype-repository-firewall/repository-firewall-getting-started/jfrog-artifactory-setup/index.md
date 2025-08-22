---
layout: default
title: "JFrog Artifactory Setup"
parent: Repository Firewall Getting Started
nav_order: 2
has_children: true
---

# JFrog Artifactory Setup

The Sonatype Repository Firewall for JFrog Artifactory solution protects your development environment from risky open-source components. The plugin uses policies configured in the Firewall server to quarantine unwanted components from being served through your remote repositories.

## Supported JFrog Artifactory Versions

The Firewall for JFrog Artifactory plugin version 2.4.11+ supports JFrog Artifactory 7.37.13 onwards.

We recommend using 7.55.6 or later due to [known issues](https://jfrog.atlassian.net/browse/RTFACT-29397) in older Artifactory versions.

JFrog Artifactory SaaS is not supported. The following versions are not supported: 7.49.3 |7.49.5 |7.49.8 |7.55.2 |reached "JFrog Artifactory end of life" date

## JFrog Artifactory’s Plugin Caching

JFrog Artifactory will restore its plugin cache over files being copied into the directory when the timestamp of the cache is newer than the files to replace the cached ones.

We recommend using the 'touch' command on the plugin files before copying them into the JFrog Artifactory's plugin directory to ensure that their timestamp is newer than the files in the cache.

```
touch <filename>;
```

Similarly, we recommend avoiding editing files while they are inside the plugins directory. Text editors commonly create temporary files while editing, which may be accessed by JFrog Artifactory; leading to corrupted files being stored in the plugin cache.

JFrog Artifactory may start to cache files before they are fully unpacked when unzipping files directly into the plugins directory. This results in a partial jar file being stored as the current version, and thus a corrupt install. Unpack the archive to a temporary folder outside of the plugins directory before copying them.

## Installation

A running JFrog Artifactory instance will immediately load plugins copied to the plugins directly. Avoid corrupting the installation by extracting the plugin to a temporary directory before moving it to the plugin's directory. This is not an issue when the server is shut down.

### Client Access

- Ensure that client requests are going through nginx reverse proxy (default port:80). When using a load balancer in front of Artifactory, the load balancer must forward requests to nginx and not artifactory directly. See [Artifactory Bypassing the Router](https://jfrog.com/help/r/how-do-i-tune-artifactory-for-heavy-loads/bypassing-the-router)
- When client requests are not using the ip address directly, force requests to use `--http1.1` as load balancers default to HTTP2 for requests which is not currently supported.

### Disabling Repositories

To disable Repository Firewall for a repository with quarantine enabled, you need to add a configuration line into the `firewall.properties` file as follows:

```
firewall.repo.maven-remove=disabled
```

- Commenting out a repository configuration does not disable it. Use the `disabled` setting instead.
- When quarantine is disabled, currently quarantined components are released to the repository. These components will not be re-quarantined without first deleting them from the remote repository and requesting them again.
- You do not need to explicitly disable Repository Firewall for repositories that have never had firewall enabled. Repositories not listed in `firewall.properties` are ignored by our plugin.
- We recommend using the REST API to configure the plugin due to the plugin caching issue mentioned above. See [JFrog Artifactory Plugin Caching](#UUID-a4009412-b400-4271-2e16-5a16aa196bbb_section-idm4581840584368034222847470973)

### Considerations

- The Firewall for JFrog Artifactory plugin processes new components as of when the plugin was enabled. Previously downloaded components are allowed to prevent existing builds from breaking.
- When the plugin is installed, removing the `firewall.properties` will cause any download requests to be denied until the `firewall.properties` file is restored and JFrog Artifactory is restarted.
- Nexus Firewall for Artifactory requires the `store artifacts locally` advanced setting.
- Repository Firewall supports the `remote` repository type. The `virtual` repository type is indirectly supported when it includes a `remote` repository. Adding `virtual` repositories to the `firewall.properties` file is not supported.
- Configure 'local' repositories as 'proprietary' to use for preventing Namespace Confusion attacks.
- Configured repositories are displayed in `Repository Managers` under ' `Organization and Policies` ' in the Firewall server.
- The username must be configured in the Firewall server with the `Component Evaluator` role. Consider using a service account with user tokens.

### High Availability

## Troubleshooting

The Repository Firewall plugin for Artifactory returns a ' `DENY` ' state for the below unexpected scenarios:

- The Repository Firewall is not fully initialized
- Unhandled exceptions
- Communication issues with the IQ server
- Misconfiguration of the `firewall.properties` file

## Logging

The Sonatype Repository Firewall for JFrog Artifactory plugin ships with logging by default. Additional logs are available for debugging when necessary. Each time a component request is blocked is not logged to prevent excessive log entries.

JFrog Artifactory uses the Logback library for logging. To understand JFrog Artifactory logging and modify logged information, see the [JFrog Artifactory documentation](https://www.jfrog.com/confluence/display/RTF/Artifactory+Log+Files#ArtifactoryLogFiles-ConfiguringLogVerbosity)

Add this section to the logback.xml file to increase logging for the plugin:

```
<logger name="com.sonatype.iq.artifactory">
    <level value="debug"/>
</logger>
```

## Getting the Firewall results page through the JFrog Artifactory API

Every repository protected by Repository Firewall has a results page detailing all of the evaluations made as components are requested through the repository. You may find this URL by making the following call to the JFrog Artifactory server.

```
curl -u {username}:{password} https://{artifactory.example.com}/api/plugins/execute/firewallEvaluationSummary?params=repo={virtual-repo-name}
```

In the example above, substitute your: `username` , `password` , `JFrog Artifactory URL` , and `virtual-repository-name` .

This is an example of the response:

```
{
  "moderateComponentCount" : 0,
  "quarantinedComponentCount" : 0,
  "reportUrl" : "https://myiqserver:8070/ui/links/repository/0396e6d401d143399d53493e57c106e8/result"
  "severeComponentCount" : 0,
  "criticalComponentCount" : 0,
  "affectedComponentCount" : 0
}
```

The `reportUrl` may be opened in a browser. This directs you to the static policy report URL.

The property `firewall.iqRepositoryUrl` links to the same Repository Results URL and is unique to each repository.

IQ Repository URL property for a repository with Firewall enabled:

![120521688.png](/docs-at-surgery-poc/assets/images/uuid-fad235f0-0d82-459c-222d-0f20b953ee25.png)

## Firewall for Artifactory Configuration

All plugin configuration is managed by the `firewall.properties` file.

```
# These properties are to configure the connection to the IQ server.
# The values below are example values and should be updated with your own.
firewall.iq.url=http://iq.example.com:8070
firewall.iq.username=exampleusername
firewall.iq.password=examplepassword

# This identifies this JFrog Artifactory instance in the IQ 'Repositories' view
firewall.repository.manager.id=artifactory-instance-1

# The URL that users will use to connect to the IQ Server.
# This URL will be prepended to the Repository Results view URI.
# For example, a complete Repository Results view URL:
#   http://iq.public.com:8070/ui/links/repository/0396e6d401d143399d53493e57c106e8/result
firewall.iq.public.url=http://iq.public.com:8070

# Define if fail open mode should be enabled (Default value is disabled).
# When IQ server is not reachable, new components can be downloaded without evaluation.
# firewall.iq.fail.open.mode.enabled=true

# Define repositories with a 'firewall.repo.' prefix.
# Possible options are 'quarantine', 'audit', 'policyCompliantComponentSelection', 'proprietary' and 'disabled'.
# 'policyCompliantComponentSelection' implies 'quarantine'.
# 'proprietary' can only be set on repositories of type 'local'.
#
# If quarantine is enabled and later disabled, all quarantined components will be made available
# in the repository; those components cannot be re-quarantined.
#
# Note that commenting out a repository configuration will not disable it,
# instead if you want to disable a repository configuration including
# 'quarantine', 'audit', or 'policyCompliantComponentSelection'
# then you must explicitly set it to be 'disabled'
# firewall.repo.<example-repository-name>=quarantine
# firewall.repo.<other-example-repository-name>=audit
# firewall.repo.<another-example-repository-name>=disabled
# firewall.repo.<example-local-repository-name>=proprietary

# Define http proxy settings if applicable
# firewall.iq.proxy.hostname=
# firewall.iq.proxy.port=
# firewall.iq.proxy.username=
# firewall.iq.proxy.password=
# firewall.iq.proxy.ntlm.domain=
# firewall.iq.proxy.ntlm.workstation=

```

### Using an HTTP Proxy for Outbound Traffic

Use the following configuration options if your JFrogArtifactory instance needs to reach the IQ Server via an HTTP proxy server.

```
# The host running the proxy server.
firewall.iq.proxy.hostname=company-proxy.example.com

# The port on which the proxy server listens.
firewall.iq.proxy.port=8080

# The username used to access the proxy server (if necessary).
firewall.iq.proxy.username=proxyusername

# The password used to access the proxy server (if necessary).
# firewall.iq.proxy.password=proxypassword
```

### NTLM

Configure the domain and workstation if your proxy server uses NT LAN Manager (NTLM) authentication.

```
# The Windows domain used for authentication
firewall.iq.proxy.ntlm.domain=companydomain
 
# The name of the local computer running JFrog Artifactory
firewall.iq.proxy.ntlm.workstation=localworkstation
```

### High Availability Caching

Firewall for JFrog Artifactory HA requires a different internal cache strategy and may be configured with the following:

For versions 2.2 and 2.4.2 only.

```
# Disable local memory cache (default: MEMORY_THEN_STORAGE )
firewall.cache.quarantine.strategy=STORAGE_ONLY
```

It is safe to switch between different cache strategies. Restart JFrog Artifactory for the changes to take effect.

## JFrog Artifactory Plugin Configuration REST API

PLUGIN RELEASE 2.4.8

In the following examples, the calls are made to your JFrog Artifactory server by substituting an admin username and password as well as your JFrog Artifactory URL.

Sensitive configuration properties will have their values obfuscated in returned API requests.

### Get Configuration Properties

The getFirewallProperties endpoint returns all configuration properties.

```
curl -u username:password https://artifactory.example.com/api/plugins/execute/getFirewallProperties"
```

Specific configuration properties may be requested using the same endpoint; both keys and values.

```
curl -u username:password "https://artifactory.example.com/api/plugins/execute/getFirewallProperties?params=keys=k1,k2"
```

### Add or Update Configuration Properties

This sets key {parameter1} to value {value1} and key {parameter2} to value {value2}.

```
curl -u username:password -X PUT "https://artifactory.example.com/api/plugins/execute/addOrUpdateFirewallProperties?params={parameter1}={value-1}%7C{parameter-2}={value-2}"
```

### Remove a Configuration Property

This API endpoint removes the {parameter1} and {parameter2} configuration properties.

```
curl -u username:password -X DELETE "https://artifactory.example.com/api/plugins/execute/removeFirewallProperties?params=keys={parameter1},{parameter2}"
```

### Set the Configuration File Content

This endpoint sets the entire configuration file content to that of the given firewall.properties file. Note the following before using this endpoint:

- This endpoint requires the submitted file encoding to be ISO 8859-1.
- All configuration file properties will be overridden using this endpoint.

```
curl -u username:password -X PUT --data-binary @firewall.properties "https://artifactory.example.com/api/plugins/execute/setFirewallProperties"
```

### Reload Artifactory Plugins

This endpoint reloads the Firewall for Artifactory plugin after changes in the plugin configuration.

Update the plugin by calling the following custom implementation of the [JFrog reload plugins endpoint](https://jfrog.com/help/r/jfrog-rest-apis/reload-plugins) . This endpoint reloads the plugin when modifications are made since the last time the call was made.

```
curl -u username:password -X POST "https://artifactory.example.com/api/plugins/execute/reload"
```

### Check IQ Server Connection

This endpoint will check the IQ Server connection.

- When the connection is successful a 200 status code is returned.
- A different status code is returned by the IQ Server connection attempt.

The returned body will contain the non-sensitive IQ Server connection properties for review.

```
curl -u username:password -X GET "https://artifactory.example.com/api/plugins/execute/checkIQConnection"
```

## Upgrading Firewall for Artifactory plugin

### 1.x to 2.0 Migration

Repository Firewall for JFrog Artifactory 2.0 fixes an issue in the 1.x series where the 'repository manager' column in the 'Repositories' view in IQ displayed a hash value instead of the repository name.

Do the following to complete the migration and display the repository identifier:

The migration will automatically begin on JFrog Artifactory startup.

## Uninstalling the Firewall for Artifactory Plugin

![56233163.png]({{ "/assets/images/uuid-3e7b2c65-e0a6-dd68-1308-db2bab9faba8.png)

## Firewall for Artifactory Release Notes

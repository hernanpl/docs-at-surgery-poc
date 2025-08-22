---
layout: default
title: "Repository Firewall Getting Started"
parent: Sonatype Repository Firewall
nav_order: 3
has_children: true
---

# Repository Firewall Getting Started

Repository Firewall is a set of features, powered by IQ Server, that integrate with Nexus Repository or through a plugin with JFrog Artifactory.

Configure the Repository Firewall with the following steps:

To configure Nexus Repository, review the [Repository Firewall Capability](#UUID-796a595c-096c-0e85-488b-8e4f46c9b628)

## Connect to an Artifact Repository

Your Repository Firewall license supports either Nexus Repository Pro or JFrog Artifactory.

- The Firewall features are enabled in Nexus Repository Pro when you install your license. See
- For JFrog Artifactory you are required to install and manage the Repository Firewall for Artifactory plugin to enable the functionality. Note that Artifactory SaaS is not supported. See

## Review the Repository Audit

Once enabled, the Repository Firewall begins to audit repositories for open-source threats and generate a report of the current risk.

Learn more about the .

## Nexus Repository 3 Pro Setup

To set up Repository Firewall for your Nexus Repository, you need to connect to the Firewall server in Nexus Repository Administration and enable the Firewall capability on your proxy repositories.

Use the following steps for Nexus Repository 3 Pro:

**Note:** We recommend using a service account when connecting Nexus Repository to the IQ Server in production environments. Consider generating user tokens as an added layer of security. At a minimum, this account requires access to the `Evaluate Individual Components` permission at the `Repository Managers` level in IQ Server `Org and Policies` .

Leave the following configuration options blank unless directed by Sonatype support:

- *Properties, Connection Timeout*

### Firewall Audit and Quarantine Capability

The Repository Firewall configuration may be managed by setting the `Firewall: Audit and Quarantine` capability for each proxy repository that will need to be protected.

### Firewall Results in Nexus Repository

The repository audit results are summarized in the `Firewall Report` column of the Repositories view in the Settings menu.

The Firewall Report column includes the following items:

- Count of components by their highest policy violation level
- Count of quarantined components
- Link to the results on the Firewall server

**Note:** When an issue occurs, a red exclamation mark and a description of the error appear in the Firewall Report column. Details of the error are available in the Nexus Repository log file.

## JFrog Artifactory Setup

The Sonatype Repository Firewall for JFrog Artifactory solution protects your development environment from risky open-source components. The plugin uses policies configured in the Firewall server to quarantine unwanted components from being served through your remote repositories.

### Supported JFrog Artifactory Versions

The Firewall for JFrog Artifactory plugin version 2.4.11+ supports JFrog Artifactory 7.37.13 onwards.

We recommend using 7.55.6 or later due to [known issues](https://jfrog.atlassian.net/browse/RTFACT-29397) in older Artifactory versions.

JFrog Artifactory SaaS is not supported. The following versions are not supported: 7.49.3 |7.49.5 |7.49.8 |7.55.2 |reached "JFrog Artifactory end of life" date

### JFrog Artifactory’s Plugin Caching

JFrog Artifactory will restore its plugin cache over files being copied into the directory when the timestamp of the cache is newer than the files to replace the cached ones.

We recommend using the 'touch' command on the plugin files before copying them into the JFrog Artifactory's plugin directory to ensure that their timestamp is newer than the files in the cache.

```
touch <filename>;
```

Similarly, we recommend avoiding editing files while they are inside the plugins directory. Text editors commonly create temporary files while editing, which may be accessed by JFrog Artifactory; leading to corrupted files being stored in the plugin cache.

JFrog Artifactory may start to cache files before they are fully unpacked when unzipping files directly into the plugins directory. This results in a partial jar file being stored as the current version, and thus a corrupt install. Unpack the archive to a temporary folder outside of the plugins directory before copying them.

### Installation

A running JFrog Artifactory instance will immediately load plugins copied to the plugins directly. Avoid corrupting the installation by extracting the plugin to a temporary directory before moving it to the plugin's directory. This is not an issue when the server is shut down.

### Troubleshooting

The Repository Firewall plugin for Artifactory returns a ' `DENY` ' state for the below unexpected scenarios:

- The Repository Firewall is not fully initialized
- Unhandled exceptions
- Communication issues with the IQ server
- Misconfiguration of the `firewall.properties` file

### Logging

The Sonatype Repository Firewall for JFrog Artifactory plugin ships with logging by default. Additional logs are available for debugging when necessary. Each time a component request is blocked is not logged to prevent excessive log entries.

JFrog Artifactory uses the Logback library for logging. To understand JFrog Artifactory logging and modify logged information, see the [JFrog Artifactory documentation](https://www.jfrog.com/confluence/display/RTF/Artifactory+Log+Files#ArtifactoryLogFiles-ConfiguringLogVerbosity)

Add this section to the logback.xml file to increase logging for the plugin:

```
<logger name="com.sonatype.iq.artifactory">
    <level value="debug"/>
</logger>
```

### Getting the Firewall results page through the JFrog Artifactory API

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

![120521688.png](/assets/images/uuid-fad235f0-0d82-459c-222d-0f20b953ee25.png)

### Firewall for Artifactory Configuration

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

### JFrog Artifactory Plugin Configuration REST API

PLUGIN RELEASE 2.4.8

In the following examples, the calls are made to your JFrog Artifactory server by substituting an admin username and password as well as your JFrog Artifactory URL.

Sensitive configuration properties will have their values obfuscated in returned API requests.

### Upgrading Firewall for Artifactory plugin

### Uninstalling the Firewall for Artifactory Plugin

![56233163.png](/assets/images/uuid-3e7b2c65-e0a6-dd68-1308-db2bab9faba8.png)

### Firewall for Artifactory Release Notes

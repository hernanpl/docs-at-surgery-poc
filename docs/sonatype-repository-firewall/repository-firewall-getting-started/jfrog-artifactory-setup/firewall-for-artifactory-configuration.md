---
layout: default
title: "Firewall for Artifactory Configuration"
parent: JFrog Artifactory Setup
nav_order: 2
---

# Firewall for Artifactory Configuration

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

## Using an HTTP Proxy for Outbound Traffic

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

## NTLM

Configure the domain and workstation if your proxy server uses NT LAN Manager (NTLM) authentication.

```
# The Windows domain used for authentication
firewall.iq.proxy.ntlm.domain=companydomain
 
# The name of the local computer running JFrog Artifactory
firewall.iq.proxy.ntlm.workstation=localworkstation
```

## High Availability Caching

Firewall for JFrog Artifactory HA requires a different internal cache strategy and may be configured with the following:

For versions 2.2 and 2.4.2 only.

```
# Disable local memory cache (default: MEMORY_THEN_STORAGE )
firewall.cache.quarantine.strategy=STORAGE_ONLY
```

It is safe to switch between different cache strategies. Restart JFrog Artifactory for the changes to take effect.

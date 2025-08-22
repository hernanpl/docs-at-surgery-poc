---
layout: default
title: "Namespace Confusion API"
parent: Firewall APIs
nav_order: 5
---

# Namespace Confusion API

Namespace Confusion is an attack where malicious packages are installed using weaknesses common in dependency management practices. These endpoints require the `EVALUATE_COMPONENT` permission in the IQ server.

See the [Namespace Confusion protection](#UUID-53279c26-0859-f790-35e9-7d43cfff316d) documentation

## Add a Namespace to Protect

Use the following endpoint to add new namespaces to the Namespace Confusion protection. This API requires the `nexus.capabilities.read` permissions.

```
POST /api/v2/malware-defense/namespace_confusion/maven
```

Example request

```
curl -X POST "http://localhost:8070/api/v2/malware-defense/namespace_confusion/maven" \
  --header 'Content-Type: application/json' \
  -u admin:admin123 \
  -d '["org.sonatype"]'
```

The passed in data element includes an array of namespaces to add. An asterisk character (*) may be used as a wild card.

### Repository Endpoints

When a repository as a source to manage the namespace does not exist then one is created automatically with the name 'nsc_{format}' . For instances the follow names are used for maven and npm components. These repositories are created under a `namespace_confusion` repository instance.

```
nsc_maven
nsc_npm
```

## Remove all Namespaces

Removes the contents of the entire namespace repository

```
DELETE /api/v2/malware-defense/namespace_confusion/maven
```

```
curl -X DELETE "http://localhost:8070/api/v2/malware-defense/namespace_confusion/maven" \
  --header 'Content-Type: application/json' \
  -u admin:admin123'
```

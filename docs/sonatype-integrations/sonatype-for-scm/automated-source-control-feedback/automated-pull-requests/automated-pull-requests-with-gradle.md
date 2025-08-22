---
layout: default
title: "Automated Pull Requests with Gradle"
parent: Automated Pull Requests
nav_order: 4
---

# Automated Pull Requests with Gradle

## Gradle

Sonatype for SCM supports updates to `build.gradle` files. During policy evaluations, Lifecycle scans your `build.gradle` files for matching components and creates a Pull Request for every match that has a remediation available.

All `build.gradle` files that exist in the repository will be examined, except `build.gradle` files in `src/test` directories, which are ignored. These are considered test files or build artifacts and not relevant project manifest files.

Only Groovy-based build files are supported. Any `gradle.properties` files found in the root directory are considered as well.

### Dependencies

Sonatype for SCM supports:

- Component defined directly inside a `dependencies` block with a literal version.
- Component defined inside a `constraints` block of a `dependencies` block with a literal version.
- Component defined inside a `dependencies` block with a property or variable version. Component versions are also looked up in the `gradle.properties` file, if one exists.
- Component defined inside a `dependencies` block with version constraints.
- Gradle version ranges are supported for all the above-mentioned cases.

### Version Pinning and Best Practices

Sonatype for SCM will always bump to a specific version by pinning it in the manifest.

In the below range syntax example, this means that a `build.gradle` containing:

```
dependencies {
  implementation "org.apache.struts:struts2-core:[2.2.1 , 2.2.10)"
}
```

This will result in a pull request to replace the contents with (assuming that version 2.2.8 passes the policy check):

```
dependencies {
  implementation "org.apache.struts:struts2-core:2.2.8"
}
```

**Important:** Pinning your dependency version is a best practice. Only a pinned version allows you to control remediation through security and quality policies. For the above example, version 2.2.8 might pass a policy check, but version 2.2.9 might not. A version range does not allow this type of control.

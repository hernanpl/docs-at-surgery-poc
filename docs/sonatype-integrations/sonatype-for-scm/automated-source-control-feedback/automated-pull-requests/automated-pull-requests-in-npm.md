---
layout: default
title: "Automated Pull Requests in npm"
parent: Automated Pull Requests
nav_order: 3
---

# Automated Pull Requests in npm

## npm

Nexus IQ for SCM supports updates to your `package.json` file. Upon policy violations for Javascript components, we will scan your `package.json` for matching components and create a Pull Request for every match that has a remediation available.

Any `package.json` that exists in the repository will be examined. Any `package.json` that contains in its path a directory named `test` , `spec` , `node_modules` , or `node` will be ignored. These are considered test files or build artifacts and not relevant project manifest files.

### Dependencies

Nexus IQ for SCM supports

- Components defined inside the `"dependencies"` section
- Components defined inside the `"devDependencies"` section Note: Nexus IQ for SCM can only bump dependencies that are part of a scan and that have a policy violation with a remediation. Most often `devDependencies` are not included as part of a final build.
- Components defined inside the `"peerDependencies"` section
- Components defined inside the `"optionalDependencies"` section

### Semantic Version Ranges

Nexus IQ for SCM supports the same semantic version range syntax from NodeJS Semver itself.

- [https://docs.npmjs.com/misc/semver](https://docs.npmjs.com/misc/semver)
- [https://github.com/npm/node-semver](https://github.com/npm/node-semver)

For example, the following is valid:

```
^6.1.0 <6.5.2
```

This will match version 6.1.0 all the way up, but not including, 6.5.2

### Version Pinning and Best Practices

It is important to note that Nexus IQ for SCM will always bump to a specific version, therefore pinning it in your manifest. In the above range syntax example, this means that a package.json containing:

```
"dependencies": {
  "package": "^6.1.0 <6.5.2"
}
```

will result in a pull request to replace the contents with:

```
"dependencies": {
  "package": "6.4.1"
}
```

**Important:** Pinning your dependency version is best practice. Only a pinned version allows you to control remediation through security and quality policies. For example, version 1.3.7 might pass policy, but version 1.3.8 might not. A version range of ~1.3.0 does not allow this type of control.

### Updating Your Lock Files

Sonatype for SCM will not update your lock files (npm `package.lock` or Yarn `yarn.lock` ).

In order to include lock file changes as part of the pull request, Sonatype recommends leveraging your CI system to perform those changes and run appropriate tests.

---
layout: default
title: "Namespace Confusion Protection"
parent: Sonatype Repository Firewall
nav_order: 7
---

# Namespace Confusion Protection

Namespace Confusion (also known as Dependency Confusion) is a Software Supply Chain Attack where malicious packages are installed using weaknesses common in dependency management practices. Repository Firewall offers protection from dependency confusion with features targeting different types of attacks.

Namespace Confusion Protections applies to [proxy repositories supported by Repository Firewall](#UUID-e3911a1d-2048-4a5d-b1e4-411c76c50d4e_section-idm4519183419561634243173713689) .

## What are Namespace Confusion attacks?

When requesting dependencies from your repository manager, we use a mix of local and public repositories as a `group` or `virtual` repository. This simplifies the build configuration instead of requesting from multiple sources.

A Namespace Confusion attack is a software supply chain attack that attempts to trick package managers into downloading malicious components found in public repositories instead of the local proprietary components. Bad actors upload components with the same name as proprietary components to public ecosystems in hopes they will mistakenly download the malicious component instead.

A common practice with Javascript and Python development teams is to request the latest version of the component that is available. When requesting internal proprietary components, the default repository manager configuration will search both internal repositories as well as remote repositories for the highest version of the component to use. This opens the supply chain to significant external risk. Bad actors publish higher versions in the public repository so that their malicious package is selected instead of the correct one. Repository Firewall's Namespace Confusion Protection is designed to protect you from threats like this.

### Types of Namespace Confusion Attacks

Here are some common dependency confusion-type attacks:

- Attackers upload packages with the same name as internal packages to a public package repository, often with a higher version than has been published to this point. The goal is to trick package managers into pulling the highest version from the public repository instead of the internal repository This attack takes advantage of the common practice of using version ranges instead of pinned versions in the project manifest.
- Attackers upload packages with the same name as internal packages to a public package repository, often with a higher version than has been published to this point.
- The goal is to trick package managers into pulling the highest version from the public repository instead of the internal repository
- This attack takes advantage of the common practice of using version ranges instead of pinned versions in the project manifest.
- Sometimes packages are imported into a software project with a different name than the public package. When a developer unknowingly or accidentally installs a package using the import name instead of the actual package name, they may download a malicious package instead. An example of a package with a different name than the import name is the PyPI package `beautifulsoup4` , which is imported as `bs4` .
- Sometimes packages are imported into a software project with a different name than the public package.
- When a developer unknowingly or accidentally installs a package using the import name instead of the actual package name, they may download a malicious package instead.
- An example of a package with a different name than the import name is the PyPI package `beautifulsoup4` , which is imported as `bs4` .
- In this attack, a malicious package is uploaded to a public repository with a similar name to a popular package. If a developer makes a typo when attempting to install the popular package, the malicious package is downloaded instead.
- In this attack, a malicious package is uploaded to a public repository with a similar name to a popular package.
- If a developer makes a typo when attempting to install the popular package, the malicious package is downloaded instead.

### Preventing Namespace Confusion

Repository Firewall prevents namespace confusion attacks by building a list of internal namespaces for your proprietary or internal components. The list of namespaces is generated from the hosted repositories you select that contain your proprietary components. The namespaces (the component name or Group ID) are added to a global list in IQ Server. This list is used to block components from being downloaded from external proxy repositories protected by Firewall.

We recommend that you move all open-source or third-party components into a separate repository from your proprietary components before enabling this feature. This includes patched and rebuilt versions of public open-source components.

Repository Firewall will include the namespace of those open-source components when mapping your proprietary namespace. When this happens, all versions of those open-source components will be blocked from download through the public proxy.

⚠️ **Warning:** If you are unsure if your hosted repository contains public open-source components, do not enable this feature. See the Removing Namespaces section for details.

## Prerequisites

- Have the policy, Security-Namespace Conflict configured in the IQ Server Have the policy action set to Fail at the proxy stage
- Have the policy action set to Fail at the proxy stage
- Repository managers connected to IQ Server: Nexus Repository 3.30 or greater JFrog Artifactory version 2.4.4 or greater Repository Firewall for JFrog Artifactory plugin and license
- Nexus Repository 3.30 or greater
- JFrog Artifactory version 2.4.4 or greater Repository Firewall for JFrog Artifactory plugin and license
- Repository Firewall for JFrog Artifactory plugin and license

## Configuring Namespace Confusion Protection

The first time you configure the Repository Firewall in your repository manager will trigger the Guide Setup process. This is the easiest way to select the hosted repositories to use with Namespace confusion protection.

Components quarantined to prevent namespace confusion can be viewed and released like any other quarantined component.

See [Managing the Quarantine](#UUID-0d9f2ae5-d7a2-4ffa-53e6-5d7a66720db9) for more information.

**Note:** To reduce overhead, the repository manager updates Firewall with proprietary names to protect are by way of a scheduled task that runs by default every 2 hours. Ensure that enough time has past before attempting to test Namespace Confusion Protection.

### Determining Namespaces depending on the repository format:

- Default behavior Uses the namespace (e.g., a Maven group, npm scope) If no namespace is available, then Firewall uses the name of the component (e.g., Maven artifact, name for npm)
- For Apt, Conda, R, Conan, RubyGems (New in 3.68.0), and PyPI (New in 3.68.0) - the namespace is determined by the component's name.

### Configure Nexus Repository 3

To protect a repository from dependency/namespace confusion in Nexus Repository 3:

### Configure jFrog Artifactory

To protect a repository from dependency/namespace confusion in jFrog Artifactory:

### Manually Configuring Namespaces

You can manually configure the namespace confusion protection for individual component namespaces in the IQ Server.

To configure, follow the instructions below.

### Removing Namespaces

Component namespaces can be removed from the namespace confusion list. Removing a component from this list will allow you to download public versions of the removed component. This is useful when you upload a 3rd party component to a protected repository.

To remove a component from the Namespace Confusion List:

---
layout: default
title: "Using Nexus Repository"
parent: Sonatype Nexus Repository
nav_order: 7
---

# Using Nexus Repository

This section covers the basic aspects of using Nexus Repository, including the following:

- User interface Overview
- Searching Components
- Browsing Repositories

## Repository Manager Concepts

In modern software development, managing your software efficiently and securely is crucial. A repository manager acts as a centralized location for storing, retrieving, and distributing software components and artifacts. They are your organization's system of record or library of software; from compiled code, to container images, to third party software.

This document explains the core concepts of repository managers, their role in DevOps pipelines, and best practices for secure artifact management.

### What is a Repository Manager?

A repository manager is a dedicated server application that stores and manages binary software artifacts and dependencies used in your development process. Think of it as a private, curated app store for your organization's software components.

- Eliminate shadow downloads with centralized artifact storage.
- Simplify dependency resolution for both private and public components.
- Cache remote artifacts to reduce build times and improve build performance.
- Control access to artifacts and open-source components that present risk to the organization.
- Integrate with DevOps pipelines for seamless artifact lifecycle management and distribution.

Instead of relying on scattered downloads or inconsistent internal practices, a repository manager provides a single source of truth for all your artifacts, including:

- **Open-source components** : Libraries, frameworks, and other dependencies from public repositories like Maven Central, npm, PyPI, and NuGet.
- **Build artifacts** : Outputs of your build process, ready for deployment.
- **Internal artifacts** : Components developed within your organization, such as libraries, modules, and applications.
- **Third-party components** : Software obtained from commercial vendors.

### Why Use a Repository Manager?

The benefits of using a repository manager are numerous and impact every stage of the software development lifecycle:

- **Simple Dependency Management** : Nexus Repository acts as a proxy for external repositories, caching frequently used components. This speeds up builds, reduces network traffic, and provides a consistent and reliable source for dependencies. By caching external dependencies, Nexus Repository insulates your builds from network outages or issues with external repositories.
- **Centralized Storage** : A single repository for all your artifacts eliminates the chaos of managing dependencies across different locations. Integrate with your CI/CD pipeline to automate the deployment of artifacts to any environment.
- **Enhanced Security** : Nexus Repository allows you to implement security policies and control access to artifacts. Prevent the use of vulnerable components and protect your software supply chain.
- **Designed for Automation** : Nexus Repository provides a rich API that allows for automation and integration with other systems.

### Components

A component is a package of resources that your software application uses (e.g., a library or a framework). Some examples of components include the following:

- Java byte code in class files
- C object files
- text files (e.g., properties files, XML files, JavaScript code, HTML, CSS
- binary files such as images, PDF files, sound files

Components can come in numerous formats, including the following:

- Java JAR, WAR, and EAR formats
- plain ZIP or .tar.gz files
- other package formats such as NuGet packages, Ruby gems, NPM packages
- executable formats, Android APK files, various installer formats

Components can be as complex as an entire application or as simple as a static resource; they can even comprise multiple nested components themselves along with assets. For example, a Java web application may be packaged as a WAR component containing multiple JAR components and JavaScript libraries. These JARs and libraries are also standalone components in other contexts while also being included as part of the WAR component.

While we use the generic term "component" in Nexus Repository, components are also called artifacts, packages, bundles, archives, and other terms.

Each component is identified by a unique set of coordinates. For example, you may have heard of GAV (group, artifact, and version) coordinates for Maven; however, coordinate names and usage strategies vary between formats.

### Assets

An asset is a single file associated with a component. Many formats have a one-to-one mapping for component to asset; however, more complex formats have numerous assets associated with a component. For example, a typical JAR component in a Maven repository is defined at least by the POM and the JAR files; each file as well as additional files (e.g., Javadoc, Sources JAR) is a separate asset belonging to the same component.

In the Docker format, assets have unique identifiers called Docker layers. You can reuse these assets for different components (i.e., Docker images).

### Components in Repositories

The open source community as well as proprietary vendors are continually creating new components. For example, there are libraries and frameworks written in various languages on different platforms that developers use for application development every day. Developers typically build applications for a specific domain by combining multiple components' features with their own custom components containing their application code.

To make consumption and usage easier, components are aggregated into collections called repositories; these are typically available on the Internet as a service. Different platforms may use terms such as "registry" and others to refer to repositories.

Examples of repositories available on the Internet as a service include the following:

- Central Repository, also known as Maven Central
- NuGet Gallery
- [RubyGems.org](http://RubyGems.org)
- [npmjs.org](http://npmjs.org)
- [Docker](https://hub.docker.com/search?q=)

Numerous tools like the following access components in these repositories:

- package managers like npm, nuget, gem
- build tools such as Maven, Gradle, rake, grunt
- IDE’s such as Eclipse, IntelliJ, Visual Studio

### Proxy Repositories

Dependency managers use components from public open-source repositories to build applications. They use a local cache to reduce the requests and bandwidth used to download components from the remote repository. This speeds up build times and keeps the final output consistent.

This introduces risk as the local cache is not centrally managed. In a modern DevOps pipeline, organizations have multiple build servers and development teams. Managing multiple component caches is not efficient or cost-effective. Routing traffic through a proxy repository is a primary use case when using a universal artifact repository like Nexus Repository.

A proxy repository is a substitute access point and managed cache for remote repositories. These are public repositories for open source components or private repositories such as another Nexus Repository for instance. They respond in the same way as the public repository does while allowing your organization to centrally manage the cache, ensuring your dependencies are always available, and greatly reducing traffic to external services.

Here is a simple example of the proxy in action.

Future requests for the same component skip the external request and immediately deliver the component.

### Routing Rules

Routing rules are useful tools to limit requests to external repositories to only the artifacts needed from the proxy. Routing rules help block dependency confusion like attacks against an organization’s internal namespace. Routing rules speed up access times for group repositories by limiting requests to only the proxies where the components should be fetched.

- Use routing rules on all proxy repositories.
- BLOCK access to your component namespaces to prevent dependency confusion attacks.
- ALLOW access to only the components needed from the public repository.

### Remote Teams

Development teams are often located across the globe. Remote teams may choose to run a local repository manager to proxy components from a centrally managed server. When building artifacts remotely they may also want to set up a bidirectional flow of artifacts using a combination of proxies and hosted repositories. Here are some considerations to keep in mind.

- The central hub and spoke model, where built artifacts are written to a central server, is far easier to manage and scale than trying to set up a bi-directional configuration. Each additional remote location will require an exponential number of connections and proxies to keep the organization connected. They are more complicated to back up and recover from any form of outage.
- Avoid using large group repositories (hundreds) where many remote proxies are configured as this will very negatively affect performance as the group will need to check each remote repository for every request. Keep group repositories to only the proxies that are needed for the build and leverage a single hosted repository for teams where possible.
- When proxying remote group repositories, it is pretty easy to create circle references. This happens when a proxy is made against a remote group repository which may also include a proxy to the source repository.

### Clean Up your Proxies

You may accumulate several proxy repositories over time and not remember why or who uses them unless you start with a clear onboarding process, strict RBAC roles, and good documentation. Every proxy in a group repository adds time to resolve dependencies and overhead to the server. Regularly review if you need proxies and take them offline when they are not actively being used.

- Use custom group repositories for teams that need additional proxies.
- Remote proxies should use HTTPS to protect against man-in-the-middle attacks.
- Periodically audit the URLs from a proxy that it is still valid and if their remote authentication is correct.
- If a proxy will be permanently offline, consider exporting and reimporting it as a 3rd-party hosted repository.
- Avoid duplicate proxies to the same URL. Proxies can be reused by multiple teams in group repositories.
- The order of repositories in group repositories matters. Keep the local hosted repositories first. Searching the hosted repositories is far quicker and keeps you from looking for your internal components in external proxies.
- Review proxy caching intervals to improve response times.

## User Interface Overview

The Nexus Repository user interface is accessed with a web browser. When anonymous access is enabled, a limited user experience is provided to search for components, browse repositories, and download components. Once logged in, additional features are available depending on the user’s privileges.

![nx-user-interface.png](/docs-at-surgery-poc/assets/images/uuid-b24f8880-a6c2-bf52-b1cd-6c13999eca9d.png)

The user interface is separated into several different sections.

### Top Navigation Panel

The top of the page contains the header with several elements starting on the left with the logo:

- The logo and the version label inform what version you are accessing at a glance.
- Use the search input box to start a keyword search. The results are displayed in the feature view panel.
- A global refresh button for all views in the user interface.
- Opens the help menu specific to the active feature view. The About item displays a dialog with details about the version as well as license and copyright information. The Documentation, Knowledge base, Community, Issue tracker, and Support items link to the respective pages on the Sonatype websites.
- Provide credentials sign in as a specific user. Once authenticated this item accesses the the user account feature view.

### Left Navigation Panel

The main menu on the left contains the Dashboard, Search, Browse, Upload, Tags, Malware Risk and Settings menu. The exact list of available menu items depends on the current user’s assigned privileges.

- The panel may horizontally collapse and be expanded.
- Submenus vertically collapsed and expand with the buttons beside the title for each submenu.
- Selecting a menu item triggers the display of the respective feature view in the feature view panel.

### Feature View Panel

The feature view in the center of the user interface changes based on your selected views. The following stardards for navigation are implemented for most views in the application.

- Selecting on a row in the list switches the feature view to a specific display for the item in the row.
- Sort the order of the table in ascending or descending order. Some columns may be enabled or removed from some table.
- The top-level links navigate back to the primary views when viewing a specific item.
- Located at the bottom left for forms to Cancel, Save, Delete, or Test configuration.
- Tables include a filter input box to limit the results of long tables.

## Working with Your User Profile

As a logged-in user, selecting the icon on the right-hand side of the main toolbar to switch account menu.

![nx-user-account-view.png](/docs-at-surgery-poc/assets/images/uuid-fc16b256-d340-0031-1be5-bb68304c4a87.png)

The *Account* feature allows you to edit your *First Name* , *Last Name* and *Email* directly in the form, as well as change your password when using local accounts.

To change your password, fill in the required fields in the bottom half of the form: Current Password, New Password and New Password (Confirm). Your new password cannot be the same as your current password and the New Password and New Password (Confirm) fields must match.

The password change feature only works with the built-in security realm. If you are using an external security realm, like LDAP, this option will not be visible.

Only users with the *nx-userschangepw* privilege are able to update their passwords.

## Browsing Repositories

Browse the contents of any repository or repository group for supported repository formats. This feature may be accessed by selecting browse from the left navigation. Users with the `nx-repository-view` privilege may access the left navigation item.

![nx-ui-browse.png](/docs-at-surgery-poc/assets/images/uuid-3fd12af9-4be6-65a1-11bc-54ee2212c3c2.png)

Select a repository to view a navigable tree containing the assets in the repository. Filter the tree content, expand nodes, and select components or assets for more detail. Nodes in the tree are sorted in case-insensitive order. Versions are sorted semantically.

**Note:** UI is limited to showing a max of 10,000 components per level for performance.

### Information View

When selecting a component or asset the information view appears on the right. The information in this view is the same as the asset and component information views for search but laid out as a series of scrolling panels instead of separate tabs. Additionally, in Sonatype Nexus Repository Pro, there will also be a scrolling panel named *Component Tags* that will present tags information in the same manner as when viewing tag information in the search results view.

![nx-ui-browse-repository.png](/docs-at-surgery-poc/assets/images/uuid-f6749225-4f9f-e719-069a-1deed8864593.png)

### HTML View

To view and browse a repository and its contents through a simple HTML view, select the *HTML View* link at the top of the browse tree.

This opens a simple HTML view of the given repository; its corresponding web service endpoint (URL) is available in the address bar.

### Security Details

In the event you do not want to give your users `nx-repository-view-*` permission to browse, there are several options available.

- `Read` gives the ability to access the contents of the repository via client tools, REST, curl and the like. It does not give any UI permissions (e.g. you cannot see the Browse left nav item with just this permission).
- `Browse` gives the ability to access the UI Browse feature via the left navigation and the see details of contents and download as described above. This permission is also used in search as well.
- `Add` gives the ability to send a POST request to upload content. This does not provide access through the UI.
- `Edit` gives the ability to send a PUT request to upload content. This does not provide access through the UI.
- `Delete` gives the to delete content from repositories but adding and editing creation is not allowed. Note, this does not give the ability to see the contents so `Read` or `Browse` will be needed in addition, depending on the delete method being used.

The stars in `nx-repository-view-*-*-*` represent format, repository, and permissions, * being inclusive of all values.

## Component IQ

When viewing search results, drill down for more detailed information. Selecting an asset to access its summary information and attributes. After connecting Nexus Repository to the IQ Server you also have access to the Component Intelligence display.

### Required Permissions

![126659282.png](/docs-at-surgery-poc/assets/images/uuid-1528fc92-74e3-930d-8b8c-049267dc27f3.png)

### Component IQ

Select the *Component IQ* to get Component Intelligence on the known component versions.

- **IQ Application dropdown** - Select one of the applications from the IQ Server to view policies from your application's context.
- **View Details** - This opens a new tab in your browser with information about any policy violations, license issues, or security vulnerabilities that are known about a specific component.

## Searching for Components

Searching for components finds information about specific artifacts in the repository. Use this for research into available components, to integrate with your build tool migrations, to download packages, and for quality assurance.

### Searching Overview

Component search is available in the search bar at the top and the Search button on the side navigation. The following permissions are required to use the search bar in the UI and find components from specific repositories:

```
nx-search-read
repository-view (per repository)
```

After entering a search, the first 300 results are visible in the component list. Selecting a component in the list changes to a display of the component information.

### Search Differences Between Environments

Search functionality differences exist between the different databases and deployment patterns.

- Searching by Conan Package ID and Conan Package or Recipe Revisions are not available for those using Orient.
- Use a leading slash (i.e., /") when searching for raw components in H2 or Non-HA PostgreSQL Environment
- Searches in HA Environments do not search all component attributes in the Keyword search bar. Specify the fields to search using the More Criteria selector.

### Search Criteria and Component Attributes

Criteria to use with most repository formats. These return results across all repositories:

- **Keyword** Use a keyword search to search for a string found in any component metadata value.
- **Format** The format of the repository in which to look for a component.
- **Repository Name** The name of a repository in which to look for a component.
- **Group** The namespace of the component; is often the organization that produces it. Some formats use a different name for this criterion such as `org` for Ivy or `groupId` for Maven while other formats do not use groups such as the `Nuget` repository format.
- **Name** The name of a component constitutes its main identifier. Different repository formats use a different name for the concept such as artifactId for Apache Maven and the maven2 repository format.
- **Version** A component's version identifies the specific point in time at which that component was released. Various tools such as Maven or NuGet use the term `version` . Other build systems call this something else (e.g., Apache Ivy uses `rev` (short for revision)). In most repository formats, version numbers do not need to follow a specific standard and are simply a string. This affects the sort order and can produce unexpected results.
- **Checksum** A checksum value of a component file generated by an MD5, SHA-1, SHA-256, or the SHA-512 algorithm.

### Preconfigured Searches

Preconfigured searches are available when a repository for the format exists in the repository and the user has `repository-view` access to the repository. The format-specific search is available via the format-named menu item in the Search section of the Browse menu.

Each preconfigured search supports adding further criteria.

- **Keyword Search** The main toolbar includes a Search components text input field. Type your search term and press enter/return and the repository manager performs a search by Keyword. The same search can be accessed by selecting the Search item in the Browse main menu. The search term can be provided in the Keyword input field in the Search feature view.
- **Custom Search** A configurable search using the criteria you select is available via the Custom menu item in the Search section of the Browse main menu. Initially, it has no criteria and it allows you to create a search with criteria you add with the More Criteria dropdown.

### Viewing Component Information

Once you locate a component via a search and select it in the list, you see the component information. An example is displayed in *Figure: “Example for Component Information and List of Associated Assets”* .

The information displayed includes the name and format of the repository that contains the component as well as the component identifiers *Group* , *Name* , and *Version* . *The most popular version* contains the version number of the same component that is most popular in its usage within a specific group and name. *Popularity* shows a relative percentage of popularity between the displayed component against all other versions of this component. A value of 100% signals this version to be the most popular. 50% means that the specific version is half as popular as the most popular version. Popularity data is provided by the Sonatype Data Services based on requests from the Central Repository and other data and is not available for all components. Age shows the age of the component.

None of the popularity or age data is viewable without Repository Health Check enabled, as lightly touched on in Managing Repositories and Repository Groups.

A list of one or more assets associated with the component is shown below the component information. Click on the row with the Name of the asset you want to inspect to view the asset information documented in Viewing Asset Information.

![168755519.png](/docs-at-surgery-poc/assets/images/uuid-df8238c2-b96c-bd10-c2cb-4a7c4d4f2735.png)

To delete a component press the *Delete component* button. A modal will pop up to confirm the deletion. You can only delete components from hosted and proxy repositories. A deletion of a component triggers the deletion of all its associated assets, in most repository formats.

In some repository formats assets are shared across components. They remain after a component deletion. For example, while a Docker image is a component and can be deleted, the layers that make it up remain after its deletion as these assets are potentially shared with other Docker images.

To analyze an application, press the *Analyze application* button. A form will pop up to request further information from you: email address, report password, a list of proprietary packages for the application, and a name for the report. Once you provide this information, press the *Analyze* button as shown in *Figure: “Analyze Application Form”* . Your report link will be emailed to you as soon as it is finished.

### Viewing Asset Information

Asset information is accessed from a component information view. The *Delete* button allows you to remove an asset. The information itself is broken up into sections, accessible by tabs below the *Delete Asset* button.

## Uploading Components

This section details uploading third-party or proprietary components to hosted repositories via the Nexus Repository user interface.

### Requirements for Uploading Components

To upload components to Nexus Repository, the user account requires these privileges:

```
nx-component-upload
nx-repository-view-*-*-edit
```

Replace the stars with the `format type` and `repository name` to limit access to a specific repository.

The following privileges are required to view the results of the upload:

```
nx-repository-view-*-*-browse
nx-repository-view-*-*-read
```

- You may only upload to a hosted repository.
- The files must be a supported type for the intended repository's format.

![nx-ui-upload-component-view.png](/docs-at-surgery-poc/assets/images/uuid-0e2f08de-a242-7a3c-2a94-5f06fde7fcfd.png)

### Steps to Upload a Component

The steps below provide a basic outline for uploading a component to a hosted repository in Nexus Repository. However, note that available form fields differ between formats:

- From the Browse view in Nexus Repository, navigate to either the Upload or Browse screen.
- Select the hosted repository to which you would like to upload a component. When performing this action from the Browse table of repositories, you need to select Upload Component. When performing this action from the Upload section, you are taken directly to the upload form.
- When performing this action from the Browse table of repositories, you need to select Upload Component.
- When performing this action from the Upload section, you are taken directly to the upload form.
- Select the *Choose File* button; then, select the file you would like to upload.
- Provide details in the form for the given repository format. For example, the Maven format requires component coordinates.
- Add any desired Tags to the component. The Tags must exist in the Nexus Repository to add them during the component upload. See the Tagging documentation
- Select Upload at the bottom of the form.

When the upload is successful, you are taken to search results for the path to the uploaded component.

### Uploading a Pom File to a Maven Repository

When a pom file is uploaded to a Maven repository, Nexus Repository extracts the coordinates from the file. The extracted coordinates include the other artifacts uploaded at the same time.

The table below details the properties of component coordinates:

### Valid File Types for Each Format

The following formats do not support uploading through the user interface:

```
Bower, CocoaPods, Composer, Conan, Conda, Cargo, Docker, Git LFS, GO Lang, Hugging Face, P2 
```

## Viewing Tags

**Note:** Only available in Sonatype Nexus Repository TM Pro. Interested in a free trial? [Start here](https://www.sonatype.com/products/repository-pro/trial) .

Tags that have been created via the REST API can be viewed through the user interface through the *Tags* entry if the active user has the *nexus:tags* privilege.

![nx-ui-tags-view.png](/docs-at-surgery-poc/assets/images/uuid-040318ee-ad39-923a-037f-402ffba007e2.png)

Clicking on a row in the table will show a view where the attributes of a tag can be viewed.

![nx-ui-tags-form.png](/docs-at-surgery-poc/assets/images/uuid-6507a290-0a6e-8f1b-bebd-2466332f3786.png)

Clicking the *Find Tagged Components* button will open the search interface with a query for the tag currently viewed.

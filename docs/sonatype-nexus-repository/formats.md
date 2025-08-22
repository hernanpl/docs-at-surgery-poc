---
layout: default
title: "Formats"
parent: Sonatype Nexus Repository
nav_order: 8
---

# Formats

Nexus Repository supports the following repository formats in all distributions. [Pro-licensed](https://www.sonatype.com/nexus-repository-sonatype) users receive Enterprise support for these formats.

## APT Repositories

Debian and systems based on it like Ubuntu, Linux Mint, and Raspbian use the same package management system. APT (Advanced Package Tool) is a set of tools for managing Debian packages, and therefore the applications installed on your Debian system. It provides a wide set of operations like searching repositories, installing packages with their dependencies, and managing upgrades.

See [APT Documentation](https://wiki.debian.org/Apt)

Nexus Repository supports the APT repository format for proxy and hosted repositories.

### Proxying APT Repositories

You may set up an APT proxy repository to access a remote repository location.

Minimal configuration steps are:

- Give the repository a name - apt-proxy
- Define the URL of the location for the remote storage - `http://archive.ubuntu.com/ubuntu/`
- Define the *Distribution* e.g. bionic
- If the remote repository has a flat format, check the `Flat` checkbox
- Pick a Blob store for storage

### Hosting Apt Repositories

You may use a hosted APT repository to upload internally developed and third-party packages.

When creating a hosted APT repository, you need to generate a GPG signing key pair or use an existing one. Hosted APT repositories only sign the metadata. Nexus Repository does not sign packages.

Generate a key pair in a Linux system with the following commands:

```
apt-get update
apt-get install gpg
gpg --gen-key
gpg --list-keys
cd <path to the folder to import the key pair>
gpg --armor --output public.gpg.key --export <gpg key Id>
gpg --armor --output private.gpg.key --export-secret-key <gpg key Id>
```

A key ID looks like: ' `515F58C16D58E682E91ACEFF17B5C97F9A816AD7` '

Minimal configuration steps are:

- Define Name e.g. apt-hosted
- Define the Distribution e.g. bionic
- Put the private PGP key into the Signing Key field, as described above
- Put the passphrase for the private signing key into the Passphrase field
- Pick a Blob store for storage

To use a hosted APT repository you need to export the GPG public key into your Linux system. Use the public key ( `public.gpg.key` ) from the key pair generated above.

```
apt-get update
apt-get install gnupg
apt-key add <full folder path in the container>/public.gpg.key
```

### Updating GPG Keys

GPG (GNU Privacy Guard) keys may be set to expire, and it is generally considered a best practice to do so. When updating the GPG keys, the metadata of Nexus Repository needs to be rebuilt to sign it with the new key.

You may do this by running the `Apt - Rebuild Apt metadata` task after replacing the GPG Key.

See the Tasks: APT Rebuild Apt metadata topic

### Deploying Packages to Hosted APT Repositories

You can use HTTP POST or *Upload* in the UI to upload packages to a hosted APT repository.

The following example uses a curl command to upload a `test.deb` file to a hosted APT repository:

```
curl -u "admin:admin123" -H "Content-Type: multipart/form-data" --data-binary "@./test.deb" "http://localhost:8081/repository/apt-hosted/"
```

### Browsing APT Repositories and Searching Packages

You can browse APT repositories in the user interface inspecting the components and assets and their details, as described in the Browsing Repositories and Repository Groups section .

Searching for APT packages can be performed in the user interface, too. It finds all packages that are currently stored in the repository manager, as described in the Searching for Components section .

### Configuring APT Client

If you already loaded a metadata using `apt update` commands first clean it by removing all files from `/var/lib/apt/lists/` .

To configure the APT client to work with Nexus Repository Manager edit the file `/etc/apt/sources.list` . Add the following line if you want to add the repository to the list, or replace the content of the file if you're going to use only your repository:

```
deb <repository URL> <distribution> main
```

For a hosted repository you should use the <distribution> from the repository properties. For a proxy repository, the <distribution> should be the same as in the original remote repository settings.

You can get the <repository URL> from the table in the Browsing Repositories and Repository Groups section via the UI.

### Taking a Snapshot of Repository Metadata

A snapshot in terms of the APT repository is a named static copy of the metadata of the repository. Changes in the repository will not cause any changes in the snapshot. A snapshot does NOT contain any binary files. So be ready if the content of the repository changes the snapshot can include some invalid metadata.

Available snapshots can be viewed in the UI Browse section in the */snapshots* folder. Files of a particular snapshot are available in */snapshots/<snapshot Id>* folder.

Snapshots functionality is available for both proxy and hosted repositories.

You can use a snapshot to set up an APT client. The URL of the snapshot is `<URL of the repository>/snapshots/<snapshot Id>` . For example `http://localhost:8081/repository/apt-proxy/snapshots/release123` .

Snapshot functionality is useful in the following cases:

- Create a snapshot and use it as a repository for a proxy repository. In this case, you are sure that packages will not be updated or removed because of changes in the remote repository.

**Note:** To use the removed in the remote repository package, this package must be cached in the proxy repository. If not, you are aware of the changed remote repository, the updated package will not be installed.

- Use snapshots for the hosted repository to freeze versions of all packages. If someone has changed the content of the repository, you are aware of the changed remote repository, the updated package will not be installed.

There are two variants to create a snapshot:

- To snapshot all metadata of the repository use a HTTP MKCOL request. The following example uses the `curl` command and example credentials of *admin* for user and *admin123* for password to create a snapshot with the id `release123` :

```
curl -u "admin:admin123" -X MKCOL "http://localhost:8081/repository/apt-proxy/snapshots/release123"
```

- To snapshot filtered by architectures and components metadata use HTTP PUT requests with the appropriate data, as follows:

## Bower Repositories

**Note:** The Bower format is not compatible with H2 or PostgreSQL databases.

[Bower](http://bower.io/) is a package manager for front-end web development. JavaScript developers using Bower gain convenient access to a large amount of packages from the remote Bower registry. This reduces the complexity of their development efforts and improves the resulting applications.

Earlier versions of Nexus Repository supported the Bower registry format for hosted and proxy repositories. This allows the repository manager to take advantage of the packages in the official Bower registry and other public registries without incurring repeated downloads of packages.

The official Bower registry is available for searches at [http://bower.io/search](http://bower.io/search) and for package retrieval via the URL `https://registry.bower.io` .

You can publish your packages to a private Bower registry as a hosted repository on the repository manager and then expose the remote and private repositories to Bower as a repository group, which is a repository that merges and exposes the contents of multiple repositories in one convenient URL. This allows you to reduce time and bandwidth usage for accessing Bower packages a registry as well as share your packages within your organization in a hosted repository.

### Proxying Bower Repositories

You can set up a Bower proxy repository to access a remote repository location, for example, the official Bower registry at `https://registry.bower.io` which is configured as the default on Bower.

To proxy a Bower registry, you simply create a new *bower (proxy)* as documented in the Repository Management section in detail.

Minimal configuration steps are:

- Define *Name*
- Define URL for *Remote storage* e.g. `https://registry.bower.io`
- Select a *Blob store* for *Storage*

The Bower-specific configuration section includes the setting to enable the rewrite of package URLs. This causes Bower to retrieve components and their dependencies through the repository manager even if original metadata has hard-coded URLs to remote repositories. This setting Force Bower to retrieve packages via the proxy repository is enabled by default.

If deactivated, no rewrite of the URL occurs. As a result, the original component URL is exposed. Turning off rewrite capabilities proxies the information directly from the remote registry without redirecting to the repository manager to retrieve components.

### Hosting Bower Repositories

Creating a Bower-hosted repository allows you to register packages in the repository manager. The hosted repository acts as an authoritative location for these components. This effectively creates an asset that becomes a pointer to an external URL (such as a Git repository).

To add a hosted Bower repository, create a new repository with the recipe *bower (hosted)* as documented in the Repository Management section.

Minimal configuration steps are:

- Define *Name* e.g. `bower-internal`
- Select *Blob store* for *Storage*

### Bower Repository Groups

A repository group is the recommended way to expose all your Bower repositories from the repository manager to your users, with minimal additional client-side configuration. A repository group allows you to expose the aggregated content of multiple proxy and hosted repositories as well as other repository groups with one URL in tool configuration. Do this by creating a new repository with the *bower (group)* recipe as documented in the Repository Management section.

Minimal configuration steps are:

- Define *Name* e.g. `bower-all`
- Select *Blob store* for *Storage*
- Add Bower repositories to the *Members* list in the desired order

### Installing Bower

Bower is typically installed with npm. Since the repository manager supports NPM repositories for proxying, we recommend configuring the relevant NPM repositories and npm as documented in the npm Registry section prior to installing Bower. Once this is completed you can install Bower with the usual command.

```
npm install -g bower 
```

Bower version 1.5 or higher is required and can be verified with

```
$ bower -v
1.7.7 
```

In addition, Bower requires a custom URL resolver to allow integration with Nexus Repository. The resolver is an API introduced in Bower version 1.5. Bower fetches component and version information through the repository manager, then automatically searches and saves the component in the repository. You can install the resolver with:

```
npm install -g bower-nexus3-resolver
```

Alternatively you can install the resolver on a per-project basis instead by adding it as a dependency in your `package.json` :

```
"devDependencies" : {
   "bower-nexus3-resolver" : "*"
}
```

### Configuring Bower Package Download

Once you have set up your repositories for Bower packages, and installed Bower and the custom resolver, you can create a `.bowerrc` JSON file to access registry URLs. The `registry` value is configured to access the Bower repository group that exposes the proxy and hosted repositories together. The `resolvers` configuration is necessary so that Bower uses the required custom resolver.

**Global**

```
{
  "registry" : {
    "search" : [ "http://localhost:8081/repository/bower-all" ]
   },
 "resolvers" : [ "bower-nexus3-resolver" ]
}
```

**Note:** The `.bowerrc` file can be located in various locations. For global configuration for a specific developer working on multiple projects, the user's home directory is a suitable location. If multiple files exist, they are merged. Details can be found [in Bower configuration documentation](https://bower.io/docs/config/) .

With this configuration in place, any further Bower command invocations trigger package downloads via the repository manager.

Running an `install` command logs the download via the repository manager:

```
$ bower install jquery
bower jquery#*
  not-cached nexus+http://localhost:8081/repository/bower-all/jquery#*
bower jquery#*
  resolve nexus+http://localhost:8081/repository/bower-all/jquery#*
bower jquery#*
  resolved nexus+http://localhost:8081/repository/bower-all/jquery#2.2.0
bower jquery#^2.2.0  install jquery#2.2.0

jquery#2.2.0 bower_components/jquery
```

If anonymous access to the repository manager is disabled, you have to specify the credentials for the accessing the repository manager as part of the URL like `http://username:password@host:port/repository/bower-all` and add a `nexus` section to your `.bowerrc` file.

```
{
  "nexus" : {
    "username" : "myusername",
    "password" : "mypassword"
  }
} 
```

Downloaded packages are cached, do not have to be retrieved from the remote repositories again and can be inspected in the user interface.

### Browsing Bower Repositories and Searching Packages

You can browse Bower repositories in the user interface inspecting the components and assets and their details, as described in the Searching for Components section .

Searching for Bower packages can be performed in the user interface, too. It finds all packages that are currently stored in the repository manager, either because they have been pushed to a hosted repository or they have been proxied from an upstream repository and cached in the repository manager.

### Registering Bower Packages

If you are authoring your own packages and want to distribute them to other users in your organization, you have to register them to a hosted repository on the repository manager. This establishes a metadata file in the repository that links to the source code repository. Typically this is a git repository. The consumers can then download it via the repository group as documented in the Configuring Bower Package Download section .

You can specify the URL for the target hosted repository in the `register` value in your `.bowerrc` file. If you are registering all packages you create in the same hosted repository you can configure in the your global configuration file e.g. located in your users home directory:

```
{
    "registry" : {
        "search" : [
            "http://localhost:8081/repository/bower-all"
        ],
        "register" : "http://localhost:8081/repository/bower-internal"
   },
   "resolvers" : [ "bower-nexus3-resolver" ]
}
```

Alternatively, if you desire to use a per-project `.bowerrc` file that you potentially version in your source code management system with the rest of the package code, you can use a simplified file:

```
"registry": {
   "register": "http://localhost:8081/repository/bower-internal"
   }
```

Authentication is managed in the same manner as for proxying with anonymous access disabled as documented in the Configuring Bower Package Download section , e.g. `"register": "http://admin:admin123@localhost:8081/repository/bower-hosted"` . With this configuration, you can run a command such as:

```
bower register example-package git://gitserver/project.git
```

All semantic version tags on the git repository are now exposed as versions for this package and consumers can install the package via the repository group like any other package.

```
bower install example-package
```

## CocoaPods Repositories

CocoaPods is a dependency manager for Swift and Objective-C Cocoa projects.

⚠️ **Warning:** Because of a limitation in the spec for Cocoapods, Nexus Repository does not currently check authentication for spec files. This means that an informed user could potentially **list** the contents of proxy repositories without authenticating. This will be resolved in a future release. See the [CocoaPods project](https://github.com/CocoaPods/CocoaPods/issues/9151) for more information.

### Support Information

- **CocoaPods client support:** 1.7.2 and greater
- **Cocoapods client** **OS** : MacOS
- **Spec repositories:** CDN only. The content delivery network mirror of the master [Specs repository](https://github.com/cocoapods/specs) is as follows. It is possible to work with custom Specs repositories only after CDN mirror creation.
- **Pods repositories** : GoogleSource.com (Git at Google), Bitbucket, direct http(s) link to archive with source code NEW IN 3.60.0
- **SSL:** CocoaPods client can only work with CDN mirror by https protocol. Http protocol is not supported. See the SSL configuration details for more about setting up SSL in NXRM.
- **Authentication to remote resources:** authentication to remote CDN spec repositories and pod repositories is not supported.

### Proxying CocoaPods Repositories

CocoaPods proxy repositories cache metadata .podspec.json files from CDN mirrors of Specs repositories. Links to such mirrors should be configured in the *Remote storage* field. After fetching of Spec file, NXRM parses the source link from the metadata file. Such sources can be GitHub, BitBucket or direct https link. Pod library source code will be cached as an archive file such as tar.gz or zip. Https source will be downloaded directly while in the case of GitHub or BitBucket source, the Pod library will be downloaded by REST API call.

To proxy a CocoaPods repository, you simply create a new *CocoaPods (proxy)* .

Minimal configuration steps are:

- Define the name: `cocoapods-proxy`
- Set the URL for remote storage
- Select a blob store for storage

### Configure CocoaPods Client

In Swift or Objective-C Cocoa project source folder, update Podfile and set the source as a link to NXRM CocoaPods repository. Example:

```
$cat Podfile
require 'cocoapods'
# Uncomment the next line to define a global platform for your project
# platform :ios, '9.0'
source 'https://localhost:8443/repository/cocoapods-proxy/'
target 'CocoaPodsTest' do
use_frameworks!
  
pod 'Alamofire', '~>5.0.0-beta.5'
pod 'Igor'
pod 'SafetySDK'
pod 'DSTestDR'
end
```

## Composer Repositories

Composer is a tool for dependency management in PHP. Declare the libraries your project depends on and Composer installs and updates them for you.

See [Composer's documentation](https://getcomposer.org/) for details.

**Note:** Nexus Repository native Composer support does not support migration from the Community plugin.

### Proxying Composer Repositories

Composer proxy repositories cache packages from privately hosted and public repositories.

To proxy a Composer repository, create a new `Composer (proxy)` as documented in the Repository Management section .

Minimal configuration steps are:

- Define the proxy name. e.g., `composer-proxy`
- Define the URL for remote storage. e.g., `https://repo.packagist.org/` Ensure you are using the latest pagckagist url as the required format has changed.
- Select a blob store for storage

### Configure Composer Client

Update the `composer.json` file saved in the `~/.composer` folder and set the repositories section to include a link to the Composer proxy in the Nexus Repository.

Example:

```
"repositories": [
 {
   "type": "composer",
   "url": "localhost:8081/repository/composer-proxy"
 }
],
```

## Conan Repositories

Conan is a package manager for C/C++ projects with a client-server architecture. Conan allows encapsulation of C/C++ project dependencies, distribution, and consumption in other projects. This involves the complex challenges of transitive dependencies, versioning, and licensing.

Conan works across Linux, OSX, and Windows platforms.

### Supported Features

### Conan Revisions

Conan revisions are a feature in the Conan dependency and package manager that allows users to make changes to artifacts while maintaining a single Conan reference.

The goal of revisions is to make packages immutable so that they are never overwritten. This allows for reproducible builds and dependencies. Lockfiles can capture the exact state of a dependency graph, including versions and revisions, and can be used to force the use of those versions and revisions, even if new ones are uploaded to the servers.

- A unique ID (revision) is associated with each Conan recipe export. When a recipe is changed, a new recipe revision (RREV) is created.
- A new package revision (PREV) is calculated for each new package created. The PREV is based on the hash of the package contents. Multiple package revisions can belong to a single recipe revision, but the same package ID can't have multiple revisions that belong to different recipe revisions. Requires Nexus Repository with PostgreSQL database Applies to Hosted Conan repositories Add the Conan Bearer Token Realm Enable revisions for Conan as in the [Conan documentation](https://docs.conan.io/1/versioning/revisions.html)
- Requires Nexus Repository with PostgreSQL database
- Applies to Hosted Conan repositories
- Add the Conan Bearer Token Realm
- Enable revisions for Conan as in the [Conan documentation](https://docs.conan.io/1/versioning/revisions.html)

### Proxy Conan Repository

Steps to set up a proxy repository to access a remote repository location.

### Hosted Conan Repository

Conan-hosted repositories require an H2 or PostgreSQL database. Conan-hosted repositories may be used for either Conan V1 or V2 so there is not a version selector as with the proxy configuration.

Complete the following steps to set up a Conan-hosted repository:

Below is an example of using a hosted Conan repository:

```
    conan remote add conan-hosted $HOSTED_REPO_URL
    conan remote login conan-hosted [repo user] -p [repo password]
    conan new hello/0.1
    conan create . hello/world
    conan upload hello/0.1@hello/world -r=conan-hosted
```

### Browsing Conan Repositories and Searching Packages

You may browse Conan repositories in the user interface inspecting the components and assets and their details, as described in the Browsing Repositories and Repository Groups section .

Searching for Conan packages may be performed in the user interface as well. Find packages in the repository manager, as described in the Searching for Components section .

### Conan Client

These instructions detail how to configure the Conan Client with Nexus Repository.

### Content Selectors for Conan

When configuring content selectors for a Conan repository, you need to use two paths in the definition.

```
/repository/conan-releases/v1/conans/<package-name>/<version>/<user>/<stable>/upload_url

/repository/conan-releases/conans/<user>/<package-name>/<version>/<stable>/conanmanifest.txt
or
/repository/conan-releases/conans/<user>/<package-name>/<version>/<stable>/conanfile.py
```

Example content selector for a Conan-hosted repository:

```
format == "conan" and (path =~ ".*/<package-name>/.+/<user>/<stable>/.*" or path =~ ".*/<user>/<package-name>/.+/<stable>/.*")
```

## Conda Repositories

[Conda](https://docs.conda.io/projects/conda/en/latest/index.html) is an open-source package management system and environment management system that runs on Windows, macOS, and Linux. It was created for Python programs but it can package and distribute software for any language.

Create a proxy repository in Nexus Repository to cache packages from remote Anaconda repositories, such as [Continuum](https://repo.continuum.io/pkgs) , [Conda-Forge](https://conda.anaconda.org/conda-forge) , and [Anaconda](https://conda.anaconda.org/anaconda/) . Have the Conda client use the Nexus Repository proxy instead of the remote repository.

### Supported Features

- Conda versions - 4.6 and newer
- Conda package formats - `.conda` and `tar.bz2`
- Repository types - Proxy

### Proxying the Conda Repository

To proxy a Conda repository, create a new *Conda (proxy)* with the following configuration steps.

### Configuring the Conda Client

The conda configuration file, .condarc, is an optional runtime configuration file that allows advanced users to configure various aspects of conda, such as which channels it searches for packages, proxy settings, and environment directories.

See [Conda documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/configuration/use-condarc.html) on `.condarc` file

There are a few ways that you may configure your Conda Client to use your Nexus Repository proxy when downloading packages.

## Docker Registry

Docker containers revolutionize how applications are packaged and deployed with Docker Hub being the primary registry for container images. Nexus Repository supports proxying registries such as Docker Hub while deploying your own private hosted repositories. Group repositories combine multiple repositories into a single endpoint so docker clients may easily to request and publish images.

See [Docker Hub documentation](https://hub.docker.com/)

### Docker Base Repository Path

Nexus Repository uses the standard url of `/repository/{repository_name}/` as the base repository path when download artifacts from a repository.

Example of the base repository path:

```
https://nexus.example/repository/docker-public/library/alpine:latest

```

The Docker client has strict requirements for the path where images are hosted in a registry. Docker clients do not allow a repository path to be included as part of the path to a docker registry as the namespace and image name are embedded in the URLs it uses.

In the example below, the namespace is `/library` for official docker images and the specific image is `/alpine:latest` .

```
docker pull registry-1.docker.io/library/alpine:latest
```

Nexus Repository manages this Docker client limitation with the following methods:

**Note:** Only one routing method may be used at a given time. See the Migrate Between Routing Methods section

### Path-Based Routing

This configuration enables users to provide a repository name in the URL path when issuing docker client commands. This method avoids the need to expose multiple ports or maintain wildcard TLS certificates when configuring subdomains.

```
docker pull nexus.example/repository-name/namespace/image:latest
```

In this example, the pulled image is `namespace/image` .

**Note:** Path-Based Routing is designed to meet the security requirements of Nexus Repository Cloud. While self-hosted deployments are encouraged to deploy this model as well, it is the only method available for Nexus Repository Cloud deployments.

This configuration is set when adding or modifying a repository in the repository management view.

![nx-docker-connectors.png](/assets/images/uuid-62280774-5281-6c93-f9f7-3c041f109ac8.png)

### Port Connectors

Port Connectors for Docker repositories use networking ports to direct traffic to the correct repository inside of Nexus Repository. You manually select which port number to use for the repository and Nexus Repository will register the port on its web service to listen for incoming requests to that port. These request are directed to the corresponding repository.

Port connectors are not supported in Nexus Repository Cloud.

Example request using port connectors:

```
docker pull https://nexus.example:18079/library/alpine:latest
```

The repository port connectors are set in the repository configuration for the specific docker repository. The ports cannot be used by another application or repositories and the network must direct traffic from that port to Nexus Repository.

As a best practices, we recommend managing SSL connections using a reverse proxy outside of the Nexus Repository to off load the overhead of managing certificates instead of the server configuration. When managing both HTTP and HTTPS traffic inside of Nexus Repository you will need different port numbers assigned to each. Otherwise, only use the connector that is common for your repository.

**Note:** For better server performance, limit your configuration to only use 20 port connectors. Each port connector must reserve system resources to monitor the exposed port which cannot be used to serve requests to your clients.

### Accessing Repositories

Browse Docker repositories in the user interface and inspect the components and assets and their details as documented in [Browsing Repositories and Repository Groups](#UUID-e108d1b2-66c8-269a-18d0-d0557d9ae8d9) .

When using the docker command line client, the structure for commands is as follows:

```
docker <command> <nexus-hostname>:<https-repository-port>/<namespace>/<image>:<tag>
docker search <nexus-hostname>:<https-repository-port>/<search-term>
```

- docker commands such as push or pull
- IP number or hostname of the repository
- The https port in the repository connector configuration
- the optional namespace of the specific image reflecting the owner, if left out this will silently default to */library* and utilize Docker Hub
- the name of the Docker image
- the optional tag of the image, defaulting to *latest* when omitted
- the search term or name of the image to search for

### Supporting OCI Images

The OCI specification versions 1.0.0 and 1.0.1 are supported within Docker repositories. This format support is available as of the 3.71 release.

As part of OCI support the following are some of the changes provided:

- Blob upload allows uploads of any arbitrary binary format ("application/octet-stream" content-type) when "Strict Content Type Validation" is enabled
- The "Location" header is part of the manifest upload response
- Endpoint that allows user to delete tag added: DELETE /v2/{name}/manifests/{tag}
- The Docker image "mediaType" property is now optional

See [Open Containers Initiative documentation](https://specs.opencontainers.org/distribution-spec/?v=v1.0.1)

### Support for Docker Registry API

The Docker client tools interact with a repository via the registry API. It is available in version 1 (V1) and version 2 (V2). The newer V2 will completely replace the old V1 in the future. While Docker Hub and other registries and tools use V2, they will sometimes fall back to V1.

Nexus Repository supports the Docker Registry API V1 and V2. All Docker repository configurations contain a section to configure Docker Registry API Support . If you activate Enable Docker V1 API for a repository, it is enabled to use V1 as a fallback from V2. Without this option, any V1 requests result in errors from the client tool.

**Note:** Generally V1 support is only needed for repository groups that will be used for command line-based searches, when any client side tools in use require V1 or when a upstream proxy repository requires V1. If you are unsure if your setup uses these or V1, it is recommended to activate V1 support as there should be no harm if it is not needed.

### Tips for SSL Certificate Usage

Docker relies on a secure connection using SSL with repositories available to client tools via HTTPS.

See the Inbound SSL - Serve Content via HTTPS section

Nexus Repository Manager is not configured with HTTPS connectors by default as it requires an SSL certificate to be generated and configured manually.

The requirement of Docker to use HTTPS forces the usage of SSL certificates. By default, Docker looks up the validity of the certificate by checking with certificate authorities. If you purchased a certificate that is registered with these authorities, all functionality works as desired.

If you create a certificate yourself with tools such as `openssl` , it is self-signed and not registered. Using a self-signed certificate requires further configuration steps to ensure that Docker can explicitly trust it.

⚠️ **Warning:** Docker Daemon can stand up instances with the `--insecure-registry` flag to skip validation of a self-signed certificate. However, Nexus Repository does not support the use of the flag as it is known to cause implementation issues.

To generate a trustworthy self-signed certificate for the repository manager use `keytool` , a utility that lets you manage your own private key pairs and certificates. See our [knowledge base article](https://support.sonatype.com/hc/en-us/articles/217542177) to learn how to configure the utility.

### Docker Manifest Lists

Docker manifest lists allow a manifest to represent support for multiple architectures while maintaining a single `image:tag` reference format.

See [Docker Schema documentation](https://docs.docker.com/registry/spec/manifest-v2-2/)

### Supported Docker Client

The docker client `version 1.8` is the minimum version that works with Nexus Repository.

We recommend staying on the latest version when possible.

Docker is a fast-moving project and requires the usage of current operating system versions and tools.

### Migrate Between Routing Methods

To migrate from port-based or subdomain routing to path-based routing you need to set up new repositories during the transition or do a hard cutover from their current routing to the desired routing. Using a mix of docker repository routing types at the same time is not supported.

We recommend using new group repositories configured with the new routing type containing a similar mix of hosted and proxy repositories so that your build managers may switch to the new type directly.

For example, when exposing the following group repository using port connectors, a new repository group is configured with Path-Based Routing containing the same mix of repositories.

```
- old-docker-group -> port connector: 18079
|- docker-proxy
|- focker-hosted

> docker pull https://nexus.example:18079/library/alpine:latest

## new repository group
- new-docker-group -> path-based routing
|- docker-proxy
|- focker-hosted

> docker pull https://nexus.example/new-docker-group/library/alpine:latest
```

### Docker Subdomain Connector

**Note:** Only available in Sonatype Nexus Repository TM Pro. Interested in a free trial? [Start here](https://www.sonatype.com/products/repository-pro/trial) .

A subdomain is a portion of a domain name, added before the root domain, that allows you to create distinct sections of a website while maintaining a connection to the main domain. In Nexus Repository, docker subdomains are used to provide a unique domain for a specific docker repository without needing to assign them to networking ports.

Subdomain connectors are not supported in Nexus Repository Cloud.

![120521639.png](/assets/images/uuid-dc64b424-0c67-1c9c-6a12-e7f438f9b469.png)

The subdomain used for your docker repository must be a unique name that is a minimum of 1 and maximum of 63 characters consisting of letters, numbers, and dashes. The subdomain must start with a letter and end with either a letter or number. For simplicity we recommend using the name of the repository.

Accessing the docker repository via the subdomain:

```
$ docker pull docker.nexus.example/alpine

```

**Note:** Docker Port Connectors Docker port connectors reserve system resources while configured. Disable port connectors in your repository configuration by unchecking the box for enabling an HTTP or HTTPS connector in the repository configuration screen. Configure either docker subdomains or url paths and migrate your clients before disabling the port connectors.

### Docker Reverse Proxy Strategies

A reverse proxy in front of Nexus Repository may also be used to avoid docker port connector scalability issues as using more than 20 port connectors to expose docker repositories may causes performance issues in Nexus Repository.

See the Run Behind a Reverse Proxy documentation

This method is to remap incoming requests to specific ports or subdomains to the complete repository base path of the intended docker repository.

- In this example, the reverse proxy remaps the request using an assigned port to the repository base path. The port `8086` is used to map to the repository path for the `docker-hosted-project` repository. The repository does not require configuring the port connector in this use-case.
- In this example, the reverse proxy remaps the request using a subdomain to the repository base path. The subdomain `project-push` is used to map to the repository path for the `docker-hosted-project` repository. The repository does not require configuring the subdomain connector in this use-case.

### Proxy Repository for Docker

To reduce duplicate downloads and improve download speeds for your developers and CI servers, you should proxy any registry you use for Docker images.

### Hosted Repository for Docker

A hosted repository using the Docker repository format is typically called a private Docker registry. It can be used to upload your own container images as well as third-party images. It is common practice to create two separate hosted repositories for these purposes.

To create a Docker hosted repository, simply create a new *docker (hosted)* repository as documented in the Repository Management section .

Minimal configuration steps are:

- Define *Name*
- Select *Blob store* for Storage

Docker clients may `push` images to this repository, and subsequently access them directly from the hosted repository or ideally from the Docker repository group as documented in the Grouping Docker Repositories section .

### Grouping Docker Repositories

A repository group is the recommended way to expose all your repositories for read access to your users. It allows you to pull images from all repositories in the group without needing any further client side configuration after the initial setup. A repository group allows you to expose the aggregated content of multiple proxy and hosted repositories with one URL to your tools.

To create a Docker repository group, simply create a new *docker (group)* repository as documented in the Repository Management section .

Minimal configuration steps are:

- Define *Name*
- Select *Blob store* for Storage
- Add Docker repositories to the *Members* list in the desired order

Typically the member list includes a mixture of proxy and hosted repositories to allow access to public as well as private images.

Using the Repository Connectors port of the repository group and the URL of the repository manager in your client tool gives you access to the container images in all repositories from the group. Any new images added as well as any new repositories added to the group will automatically be available.

### Content Selectors and Docker

Should you wish to not share all Docker components across all teams, we recommend using content selectors in conjunction with access control (specifically the privileges created by content selectors) to manage access to specific content. However, the Docker format has some non-standard complexity to setting up security against the CLI and UI.

Before continuing, note that we provide the instructions in this section with the assumption that you are able to sort the security of your Docker images by name. Below, we use the word `team` in our examples where `team` is the representation of that which you are sorting. For example, it might be `sonatype/nexus` for this product/project team, or further `sonatype/nexus/docker` for the Docker-specific parts. If you are unable to do this, this page likely will not help you or your solution will be much more complex than the scenarios given.

### Docker Authentication

### Searching

Searching for Docker images, as described in the Searching for Components section , finds any images stored in local repositories; either in a hosted repository or proxied from an upstream public repository.

The docker client is preconfigured to search and find images only from Docker Hub.

When directing the docker client to a group repository in Nexus Repository, the docker client may search both local images and those found in Docker Hub.

To search the public repository use the Docker client command line:

The following example of using the Docker client command line to search for a `postgres` image running on the host `nexus.example.com` . In this example, the group repository is exposed through the repository connector port of `18443` .

```
docker search nexus.example.com:18443/postgres
```

The results include images found in the repositories that are part of the repository group.

### Pulling Images

Downloading images, also known as pulling, from the repository manager is performed with the `docker pull` command. Include the hostname or IP address of the repository manager as well as the repository connector port configured for the repository.

```
docker pull <nexus-hostname>:<repository-port>/<image>
```

The following examples download images from Nexus Repository Manager running on the host `nexus.example.com` with a repository connector port of `18443`

```
docker pull nexus.example.com:18443/ubuntu
docker pull nexus.example.com:18443/bitnami/node
docker pull nexus.example.com:18443/postgres:9.4
```

Official images such as Ubuntu or Postgres belong to the library user on Docker Hub and will therefore show up as `library/ubuntu` and `library/postgres` in the repository manager.

After a successful `pull` , start the container with the `run` command.

See the Docker Authentication topic on authentication before pulling an image.

### Pushing Images

**Note:** If using Nexus Repository Pro, consider pushing images to a group repository .

Sharing an image can be achieved by publishing it to a hosted repository. This is completely private and requires you to `tag` and `push` the image. When tagging an image, you can use the image identifier ( `imageId` ). It is listed when showing the list of all images with `docker images` . Syntax and an example (using `imageId` ) for creating a tag are:

```
docker tag <imageId or imageName> <nexus-hostname>:<repository-port>/<image>:<tag>
docker tag af340544ed62 nexus.example.com:18444/hello-world:mytag
```

Once the tag, which can be equivalent to a version, is created successfully, you can confirm its creation with `docker images` and issue the `push` with the syntax:

```
docker push <nexus-hostname>:<repository-port>/<image>:<tag>
```

**Note:** Note that the port needs to be the repository connector port configured for the hosted repository to which you want to push to. You can not push to a proxy repository.

A sample output could look like this:

```
$ docker push nexus.example.com:18444/hello-world:labeltest
The push refers to a repository [nexus.example.com:18444/hello-world] (len: 1)
Sending image list
Pushing repository nexus.example.com:18444/hello-world (1 tags)
535020c3e8ad: Image successfully pushed
af340544ed62: Image successfully pushed
Pushing tag for rev [af340544ed62] on
{https://nexus.example.com:18444/repository/docker-internal/v1/repositories/hello-world/tags/labeltest}
```

Now, this updated image is available in the repository manager and can be pulled by anyone with access to the repository, or the repository group, containing the image. Pulling the image from the repository group exposed at port `18443` can be done with:

```
docker pull nexus.example.com:18443/hello-world:labeltest
```

Prior to `push` , and depending on your configuration, repository manager login credentials may be required before a `push` or `pull` can occur.

**Note:** Searching, Browsing, Pushing and Pulling are all showcased in this video: .

Pushing large images can result in failures due to network interruptions and other issues. These partial uploads result in temporary storage for these transfers in the repository manager filling up. The task *Docker - Delete incomplete uploads* can be configured to delete these files. If you also tend to upload images to the same tag repeatedly, this can leave a lot of dangling images around, consuming a lot of space. The task *Docker - Delete unused manifests and images* can be configured to remove these files.

### Pushing Images to a Group Repository

**Note:** Only available in Sonatype Nexus Repository TM Pro. Interested in a free trial? [Start here](https://www.sonatype.com/products/repository-pro/trial) .

With Sonatype Nexus Repository Pro, you can push images to a group repository. To do this, select a *Writable Repository* in the configuration menu as shown below:

**Note:** Note that you will not be able to use Staging moves for writable repositories that are members of a Docker group repository.

![93487515.png](/assets/images/uuid-b5b6fc19-ca98-e885-96b4-0b083a4919c5.png)

The procedure of pushing images is otherwise the same [as described for a hosted repository](#UUID-60cccba3-51e4-878c-8488-10623077aa84) .

When pushing to a group repository, Sonatype Nexus Repository will check existing layers of all members to avoid pushing those layers to save on storage and bandwidth.

If you attempt to push an existing layer, you will get an output that looks similar to the following:

```
9c27e219663c: Layer already exists
```

### Foreign Layers

Foreign layers in Docker are image layers stored outside the primary container registry. When pulling an image, the Docker client retrieves certain layers from these external locations.

Configure Nexus Repository to cache foreign layers of Docker images in Nexus Repository so clients do not communicate with other repositories.

- Foreign layers create external dependencies and potential reliability issues.
- Modern Docker practices are moving away from foreign layers, aiming for all image components to reside within the registry.
- Use foreign layer caching in air-gapped environments or centralized development environments where the client host does not have external access.
- Use an approved list of locations to limit the risk of exposer to external threats.

Use the following steps to enable this functionality:

### Docker Content Trust

Docker Content Trust (DCT) allows docker image tags to be cryptographically signed. This allows users to verify the integrity and the publisher of docker data provided by the registry. DCT is enforced at two levels: by the docker client (supported by Docker Community and Enterprise) and by the docker engine (Enterprise only).

Docker Content Trust is not directly handled by Nexus Repository. You can use Docker Notary in conjunction with Nexus Repository to publish and manage trusted Docker content.

## Git LFS Repositories

Git Large File Storage (LFS) is a Git extension mechanism to store large files outside of the Git repository while still accessing them as if they were part of the same project. A pointer file replaces the file inside of the Git repository, while the file is archived in the Nexus Repository. Nexus Repository supports the batch API, the basic transfer adapter for uploading and downloading files, and a hosted repository for storing the files from the Git LFS client.

These operations are handled automatically by the Git LFS client once installed on developers' workstations and configured for use with Nexus Repository.

More information on this format can be found on the [Github Git LFS](https://git-lfs.github.com/) .

- Requires Git 1.8.2 or above
- Git LFS versions 1.* and 2.* are supported

### Create a Hosted Git LFS Repository

To host Git LFS content in Nexus Repository Manager, create a new gitlfs (hosted) repository.

Minimal configuration steps are:

- Define *Name*
- Select a *Blob store* for *Storage* We recommend using a custom blob store for Git LFS repositories.

Removing content from a Git LFS repository is not recommended and no cleanup task exists. Removing files from Git LFS means that those files will no longer be available from your associated Git repository, and the pointer files in Git will point to content that no longer exists.

The *Strict Content Type Validation* option does not apply to Git LFS repositories. Since Git LFS by its nature accepts any kind of file content, we perform no content validation on incoming files and assume all files are generic `application/octet-stream` content.

**Note:** Take care to document your configuration when mapping the Git-LFS repositories and your Git projects. The origin of a particular file is not provided to a Git LFS repository and is only stored in the Git repository. Consider limiting hosted repositories to a single Git project to separate environments.

### Installing Git LFS

Download and install Git LFS on your local machine. Follow the installation directions for Git LFS for your particular platform. After installation, run the following command to confirm that the installation succeeded.

```
git lfs env
```

### Configuring Git LFS

Configure your local Git LFS installation to use Nexus Repository as the Git LFS backend. We recommend using the [Git LFS Tutorial](https://github.com/git-lfs/git-lfs/wiki/Tutorial) .

## Go Repositories

The GO programming language (golang) introduced Go modules in version 1.11 to make dependency version information explicit and easier to manage. Nexus Repository supports Go modules dependency resolution using proxy and group repositories. Go packages are cached and served using a single endpoint, without builds incurring repeated downloads of packages from the public internet.

### Shifting from the “Monorepo”

The Go programming language uses centralized monolithic git repositories to source Golang code to simplify dependency management. This was done using a version control system where the Go command line would perform a full clone of all required dependencies. The Go community realised that this has a number of negative impacts for any typical CI process as cloning repositories can be a time consuming process and was a barrier for developers working on isolated sub-project that did not require every dependency from the repository.

- No standards for dependency management.
- Without a native package manager, Go developers relayed on tools like dep.
- Only vendoring and GOPATH were available to bring in outside dependencies.

Fetching sources from any number of version control systems such as Github meant that centralized proxies such as Sonatype Nexus Repository could not be used. To solve this problem, Go introduced the `GOPROXY` environment variable.

### About Go Modules

Go modules is the standard package management system for Golang. It offers a common toolset to build proxy servers to versioned Go dependencies, where you’re no longer dependent on a monolithic platform. This provides for more stable packages in your CI environment.

### Configuring a Go Project in Sonatype Nexus Repository

You can serve and cache modules remotely from resources such as GitHub. Currently, hosted repositories aren’t available. However, you can address two use cases:

- Configure the repository manager to cache projects
- Create a simple project and download dependencies to the project

### Grouping Go Repositories

A repository group is the recommended way to expose all your Go repositories. A repository group allows you to expose the aggregated content of multiple Go repositories with one URL; it is this url that you should set the `$GOPROXY` environment variable url to.

To create a Go group repository, create a new repository using the recipe *g* *o (group)* as documented in the Repository Management section .

Minimal configuration steps are:

- Define *Name*
- Select *Blob store* for *Storage*
- Add Go repositories to the *Members* list in the desired order

### Go Configuration Examples

If you need to access dependencies from authenticated sources, you'll need to run [Athens](https://docs.gomods.io/) internally; this locally hosted server is able to be configured with authentication credentials to access private repositories. You may still decide to proxy an external server to avoid unnecessary duplication of caching and therefore storage space.

The following diagram depicts an example set up:

![28345883.png](/assets/images/uuid-0160d8b3-ce76-7b13-c112-fa54c754bcb4.png)

## Helm Repositories

Helm is the first application package manager running atop Kubernetes(k8s). It allows describing the application structure through convenient helm-charts and managing it with simple commands. More information about Helm can be found in the [official documentation](https://helm.sh/docs/) . Nexus Repository functions with both Helm2 and Helm3.

You can publish your charts and provenance files to a private repository in a hosted Helm repository. You can also use a proxy Helm repository reducing time and bandwidth usage for accessing Helm charts as well as more easily sharing your charts within your organization.

Note that as of release 3.71.0, you can only upload components to a root Helm repository.

### Proxying Helm Repositories

You can set up a Helm proxy repository to access a remote repository location.

To proxy a Helm repository, create a new helm (proxy). Minimal configuration steps for the Helm proxy are:

- Define *Name* , e.g. `helm-proxy`
- Define *URL* for *Remote storage* (e.g., `https://charts.helm.sh/stable` )
- Select a *Blob store* for *Storage*

### Hosting Helm Repositories

Creating a Helm-hosted repository allows you to register charts in the repository manager. The hosted repository acts as an authoritative location for these components.

To add a hosted helm repository, create a new repository with the recipe helm (hosted). Minimal configuration steps for Helm hosted are:

- Define Name (e.g., helm-hosted)
- Select the Blobstore to use for Storage

### Uploading Charts to Helm Hosted Repositories

### Uploading Provenance Files to Helm Hosted Repositories

Uploading provenance files with the extension `.prov.tgz` to a hosted repository is the same as uploading a chart. The provenance file will be at the same tree structure level as the chart.

More information about provenance files can be seen [on the Helm website](https://helm.sh/docs/topics/provenance/) .

### Using Helm Client

Once you have Helm up and running you'll want to run a command similar to the following to add a Helm repo:

```
helm repo add <helm_repository_name> http://<host>:<port>/repository/<nexus_repository_name>/ --username <username> --password <password>
```

The below command will fetch the latest chart or with the version:

```
1. helm fetch <helm_repository_name>/<chart_name>
2. helm fetch <helm_repository_name>/<chart_name> --version <chart_version>
```

For example, Nexus Repository has a Helm proxy repository called `helm-proxy` and your Nexus Repository is running on `localhost:8081` where username is `admin` and password is `admin` . You would like to add this repository to the Helm client. Also, you would like to fetch the latest MySQL chart. To accomplish this, you would do the following:

```
1. helm repo add nexusrepo http://localhost:8081/repository/helm-proxy/ --username admin --password admin
2. helm fetch nexusrepo/mysql
```

If you want to fetch a chart with a specific version, just run it, like so:

```
helm fetch nexusrepo/mysql --version 1.4.0
```

## Hugging Face Repositories

Hugging Face is a machine learning platform and community best known for its extensive library of pre-trained transformer models for various tasks, such as natural language processing, computer vision, and audio analysis. The platform provides tools for building, training, and deploying machine learning models and datasets, and spaces to share and collaborate with others.

Nexus Repository 3 supports proxying Hugging Face models allowing you to store and distribute Hugging Face models within your organization, improving efficiency and control.

Think of Hugging Face as a platform with different tools for machine learning:

- Models are the core of Hugging Face, pre-trained brains ready to perform tasks. They're like recipes that have already been perfected.
- These are the ingredients for the recipes. They're collections of data used to train and evaluate the models.
- Spaces are like interactive demos or apps built with Hugging Face models. You can use them to test out models to see how they work.

**Note:** The proxy support is for Hugging Face models only. Datasets and spaces are not yet supported, and models related to those may fail to download.

### Configuring a Hugging Face Proxy Repository

Follow these steps to set up a Hugging Face proxy repository in Nexus Repository 3:

**Note:** Use File Storage for Hugging Face Repositories Use an NFS/EFS/Azure file storage for optimal performance. In testing, AWS S3 and Azure Blob stores exhibit performance issues that can impact download speeds.

### Client Configuration

To configure your clients, set the following environment variables:

- Override the default Hugging Face endpoint to point to your Nexus Repository Hugging Face proxy repository URL. When authentication is required on Nexus Repository, include the token in the `HF_ENDPOINT` as follows: We recommend using user tokens to avoid including personal credentials in your local environment variable.
- HF_HUB_DOWNLOAD_TIMEOUT: Increase the download timeout to prevent errors when downloading large models. The recommended value is 120 seconds.
- HF_HUB_ETAG_TIMEOUT: Increase the ETag timeout. The recommended value is 900 seconds. You may experience timeout errors on the client side for larger models. Retry the download after a couple of minutes to allow Nexus Repository time to finish proxying the model or increase the timeout configuration value accordingly. The first time a new model is downloaded through Nexus Repository will be slow due to the time needed to cache the model. The model files are not retrieved by the client until fully cached in the Nexus Repository.

### Troubleshooting

- Some Hugging Face models may have mismatched file types and content types when requesting image files from the repository. This is a known Hugging Face issue. Disable the `strict content validation` in your Nexus Repository configuration when you encounter 400 errors for a 'Bad request'. See the following example:
- If you experience slow downloads from Hugging Face, increase the Nexus Repository request timeout as described above.

### Performance Metrics

Performance testing was conducted for Nexus Repository using a Hugging Face proxy repository. The objective was to evaluate system behavior under load, specifically regarding hardware utilization, response times, and throughput when handling large assets.

- Deploying additional hardware resources may be necessary for environments expecting high concurrency due to the large asset sizes.
- Configure HTTP timeouts appropriately to accommodate extended download durations for large models.

## Maven Repositories

Nexus Repository was designed to support the Maven repository format and it continues to include excellent support for users of Apache Maven, Apache Ant/Ivy, Eclipse Aether, Gradle, and others.

This section explains the default configuration for creating Maven repositories as well as searching and browsing the repositories. Build tool configuration for Apache Maven, Apache Ant, Gradle, and other tools follow.

### Maven Repository Format

[Apache Maven](http://maven.apache.org/) created the most widely used repository format in the Java development ecosystem with the release of Apache Maven 2. It is used by all newer versions of Apache Maven and many other tools including Apache Ivy, Gradle, sbt, Eclipse Aether, and Leiningen. Further information about the format can be found in [An Example - Maven Repository Format](#UUID-1a6ce455-911a-146f-a844-14ae6024d349) .

The format is used by many publicly available repositories. The [Central Repository](http://central.sonatype.org/) is the largest repository of components aimed at Java/JVM-based development and beyond and is used the Maven repository format for release components of numerous open source projects. It is configured as a proxy repository by default in Apache Maven and widely used in other tools.

In addition to the generic repository management features documented in the Repository Management section , specifics of the Maven repository format can be configured for each repository in the *Maven 2* section:

### Proxying Maven Repositories

A default installation of Nexus Repository Manager includes a proxy repository configured to access the Central Repository via HTTPS using the URL `https://repo1.maven.org/maven2/` . To reduce duplicate downloads and improve download speeds for your developers and CI servers, you should proxy all other remote repositories you access as proxy repositories as well.

To proxy a Maven repository, you simply create a new repository using the recipe *maven2 (proxy)* as documented in the Repository Management section .

Minimal configuration steps are:

- Define *Name*
- Define URL for *Remote storage* e.g. `https://repo1.maven.org/maven2/`
- Select a *Blob store* for *Storage*

This creates a repository using the *Release* version policy and a *Strict* layout policy. Both can be configured as appropriate for the remote repository.

If the remote repository contains a mixture of release and snapshot versions, you have to set the version policy to *Mixed* .

Usage of the repository with build tools such as sbt, potentially requires the layout policy to be set to *Permissive* .

### Hosting Maven Repositories

A hosted Maven repository can be used to deploy your own as well as third-party components. A default installation of Nexus Repository Manager includes a two hosted Maven repositories. The *maven-releases* repository uses a release version policy and the *maven-snapshots* repository uses a snapshot version policy.

To create another hosted Maven repository, add a new repository with the recipe *maven2 (hosted)* as documented in the Repository Management section .

Minimal configuration steps are:

- Define *Name*
- Select *Blob store* for *Storage*

### Grouping Maven Repositories

A repository group is the recommended way to expose all your Maven repositories from the repository manager to your users, without needing any further client side configuration. A repository group allows you to expose the aggregated content of multiple proxy and hosted repositories as well as other repository groups with one URL for tool configuration. This is possible for Maven repositories by creating a new repository with the *maven2 (group)* recipe as documented in the Repository Management section .

Minimal configuration steps are:

- Define *Name*
- Select *Blob store* for *Storage*
- Add Maven repositories to the *Members* list in the desired order

A typical, useful example is the *maven-public* group that is configured by default. It aggregates the *maven-central* proxy repository with the *maven-releases* and *maven-snapshots* hosted repositories. Using the URL of the repository group gives you access to the packages in all three repositories with one URL. Any new component added as well as any new repositories added to the group will automatically be available.

### Browsing and Searching Maven Repositories

You can browse Maven repositories in the user interface inspecting the components and assets and their details as documented in [Browsing Repositories and Repository Groups](#UUID-e108d1b2-66c8-269a-18d0-d0557d9ae8d9) .

Components can be searched in the user interface as described in the Searching for Components section . A search finds all components and assets that are currently stored in the repository manager, either because they have been deployed to a hosted repository or they have been proxied from an upstream repository and cached in the repository manager.

### Configuring Apache Maven

To use repository manager with [Apache Maven](http://maven.apache.org/) , configure Maven to check the repository manager instead of the default, built-in connection to the Central Repository.

To do this, you add a mirror configuration and override the default configuration for the central repository in your `~/.m2/settings.xml` , shown below:

**Configuring Maven to Use a Single Repository Group**

```
<settings>
  <mirrors>
    <mirror>
      <!--This sends everything else to /public -->
      <id>nexus</id>
      <mirrorOf>*</mirrorOf>
      <url>http://localhost:8081/repository/maven-public/</url>
    </mirror>
  </mirrors>
  <profiles>
    <profile>
      <id>nexus</id>
      <!--Enable snapshots for the built in central repo to direct -->
      <!--all requests to nexus via the mirror -->
      <repositories>
        <repository>
          <id>central</id>
          <url>http://central</url>
          <releases><enabled>true</enabled></releases>
          <snapshots><enabled>true</enabled></snapshots>
        </repository>
      </repositories>
     <pluginRepositories>
        <pluginRepository>
          <id>central</id>
          <url>http://central</url>
          <releases><enabled>true</enabled></releases>
          <snapshots><enabled>true</enabled></snapshots>
        </pluginRepository>
      </pluginRepositories>
    </profile>
  </profiles>
  <activeProfiles>
    <!--make the profile active all the time -->
    <activeProfile>nexus</activeProfile>
  </activeProfiles>
</settings>
```

In *Configuring Maven to Use a Single Repository Group* a single profile called `nexus` is defined. It configures a `repository` and a `pluginRepository` with the id `central` that overrides the same repositories in the Super POM. The Super POM is internal to every Apache Maven install and establishes default values. These overrides are important since they change the repositories by enabling snapshots and replacing the URL with a bogus URL. This URL is overridden by the `mirror` setting in the same `settings.xml` file to point to the URL of your single repository group. This repository group can, therefore, contain release as well as snapshot components and Maven will pick them up.

The `mirrorOf` pattern of `*` causes any repository request to be redirected to this mirror and to your single repository group, which in the example is the public group.

It is possible to use other patterns in the mirrorOf field. A possible valuable setting is to use `external:*` . This matches all repositories except those using `localhost` or file based repositories. This is used in conjunction with a repository manager when you want to exclude redirecting repositories that are defined for integration testing. The integration test runs for Apache Maven itself require this setting.

More documentation about mirror settings can be found in the [mini guide on the Maven web site](http://maven.apache.org/guides/mini/guide-mirror-settings.html) .

As a last configuration the `nexus` profile is listed as an active profile in the `activeProfiles` element.

Deployment to a repository is configured in the `pom.xml` for the respective project in the `distributionManagement` section. Using the default repositories of the repository manager:

```
<project>
...
<distributionManagement>
    <repository>
      <id>nexus</id>
      <name>Releases</name>
      <url>http://localhost:8081/repository/maven-releases</url>
    </repository>
    <snapshotRepository>
      <id>nexus</id>
      <name>Snapshot</name>
      <url>http://localhost:8081/repository/maven-snapshots</url>
    </snapshotRepository>
  </distributionManagement>
...
```

The credentials used for the deployment are found in the `server` section of your `settings.xml` . In the example below `server` contains `nexus` as the `id` , along with the default `username` and `password` :

```
<settings>
....
  <servers>
    <server>
      <id>nexus</id>
      <username>admin</username>
      <password>admin123</password>
    </server>
  </servers>
```

Full example projects can be found in the maven folder of the [example project](https://github.com/sonatype/nexus-book-examples) in the `nexus-3.x` branch. A full build of the `simple-project` , including downloading the declared dependencies and uploading the build output to the repository manager can be invoked with `mvn clean deploy` .

### Configuring Apache Ant and Apache Ivy

[Apache Ivy](http://ant.apache.org/ivy) is a dependency manager often used in Apache Ant builds. It supports the Maven repository format and can be configured to download dependencies that can be declared in the `ivy.xml` file. This configuration can be contained in the `ivysettings.xml` . A minimal example for resolving dependencies from a repository manager running on localhost is shown below:

**Minimal Ivy Configuration in an Ant file**

```
<ivysettings>
  <settings defaultResolver="nexus"/>
  <property name="nexus-public"
    value="http://localhost:8081/repository/maven-public/"/>
  <resolvers>
      <ibiblio name="nexus" m2compatible="true" root="${nexus-public}"/>
    </resolvers>
</ivysettings>
```

These minimal settings allow the `ivy:retrieve` task to download the declared dependencies.

To deploy build outputs to a repository with the ivy:publish task, user credentials and the URL of the target repository have to be added to `ivysettings.xml` and the `makepom` and `publish` tasks have to be configured and invoked.

Full example projects can be found in the `ant-ivy` folder of the [example project](https://github.com/sonatype/nexus-book-examples/tree/nexus-3.x) in the `nexus-3.x` branch. A full build of the `simple-project` , including downloading the declared dependencies and uploading the build output to the repository manager can be invoked with:

```
cd ant-ivy/simple-project
ant deploy
```

### Configuring Apache Ant and Eclipse Aether

[Eclipse Aether](https://projects.eclipse.org/projects/technology.aether) is the dependency management component used in Apache Maven 3+. The project provides Ant tasks that can be configured to download dependencies that can be declared in a `pom.xml` file or in the Ant build file directly.

This configuration can be contained in your Ant `build.xml` or a separate file that is imported. A minimal example for resolving dependencies from a repository manager running on localhost is shown below:

**Minimal Aether Configuration in an Ant file**

```
<project xmlns:aether="antlib:org.eclipse.aether.ant" ....>
  <taskdef uri="antlib:org.eclipse.aether.ant" resource="org/eclipse/aether/ant/antlib.xml">
    <classpath>
      <fileset dir="${aether.basedir}" includes="aether-ant-tasks-*.jar" />
    </classpath>
  </taskdef>
  <aether:mirror id="mirror" url="http://localhost:8081/repository/maven-public/" mirrorOf="*"/>
...
</project>
```

These minimal settings allow the `aether:resolve` task to download the declared dependencies.

To deploy build outputs to a repository with the `aether:deploy` task, user authentication and details about the target repositories have to be added.

Full example projects can be found in the `ant-aether` folder of the [example project](https://github.com/sonatype/nexus-book-examples/tree/nexus-3.x) in the `nexus-3.x` branch. A full build of the `simple-project` , including downloading the declared dependencies and uploading the build output to the repository manager can be invoked with:

```
cd ant-aether/simple-project
ant deploy
```

### Configuring Gradle

[Gradle](http://www.gradle.org/) has a built-in dependency management component that supports the Maven repository format.

In order to configure a Gradle project to resolve dependencies declared in the `build.gradle` file, a Maven repository as shown in *Gradle Repositories Configuration* has to be declared.

**Gradle Repositories Configuration**

```
repositories {
    maven {
        url "https://nexus.example/repository/repository-name/"
    }
}
```

These minimal settings allow Gradle to download the declared dependencies. You can also see [Gradle's documentation on dependencies](https://docs.gradle.org/current/userguide/declaring_repositories.html#sec:declaring_custom_repository) for more information.

For guidance on publishing to Maven, see [Gradle's documentation](https://docs.gradle.org/current/userguide/publishing_maven.html) .

### SBT

[sbt](http://www.scala-sbt.org/) has a built in dependency management component and defaults to the Maven repository format. In order to configure a sbt project to resolve dependencies declared in `build.sbt` file, a resolver, as shown in *SBT Resolvers Configuration* has to be declared.

**SBT Resolvers Configuration**

```
resolvers += "Nexus" at "http://localhost:8081/repository/maven-public/"
```

These minimal settings allow sbt to download the declared dependencies.

To deploy build outputs to a repository with the publish task, user credentials can be declared in the `build.sbt` file:

```
credentials += Credentials("Sonatype Nexus",
"nexus.scala-tools.org", "admin", "admin123") 
```

The `publishTo` configuration:

```
publishTo <<= version { v: String =>
  val nexus = "http://localhost:8081/"
  if (v.trim.endsWith("SNAPSHOT"))
    Some("snapshots" at nexus + "repository/maven-snapshots")
  else
    Some("releases" at nexus + "repository/maven-releases") 
```

Further documentation can be found in the [sbt documentation on publishing](http://www.scala-sbt.org/release/docs/Publishing.html) .

### Leiningen

[Leiningen](http://leiningen.org/) has a built in dependency management component and defaults to the Maven repository format. As a build tool it is mostly used for projects using the Clojure language. Many libraries useful for these projects are published to the Clojars repository. If you want to use these, you have to create two proxy repositories with the remote URL `http://clojars.org/repo/` .

This repository is mixed and you therefore have to create a release and a snapshot proxy repository and then add both to the public group.

In order to configure a Leiningen project to resolve dependencies declared in the `project.clj` file, a `mirrors` section overriding the built in `central` and clojars repositories as shown in *Leiningen Configuration* has to be declared.

**Leiningen Configuration**

These minimal settings allow Leiningen to download the declared dependencies.

```
:mirrors {
    "central" {:name "Nexus"
                          :url "http://localhost:8081/repository/maven-public/"
                          :repo-manager true}
  #"clojars" {:name "Nexus"
                          :url ""http://localhost:8081/repository/maven-public/""
                          :repo-manager true}
                        }
```

To deploy build outputs to a repository with the deploy command, the target repositories have to be add to `project.clj` as `deploy-repositories` . This avoids Leiningen checking for dependencies in these repositories, which is not necessary, since they are already part of the `public` repository group used in `mirrors` .

```
:deploy-repositories [
    ["snapshots" "http://localhost:8081/repository/maven-snapshots"]
    ["releases" "http://localhost:8081/repository/maven-releases"]
  ]
```

User credentials can be declared in `~/.lein/credentials.clj.gpg` or will be prompted for.

Further documentation can be found on the [Leiningen website](http://leiningen.org/) .

### Maven Repository Format

Maven developers are familiar with the concept of a repository since repositories are used by default. The primary type of binary component in a Maven format repository is a JAR file containing Java byte code. This is due to the Java background of Maven and the fact that the default component type is a JAR. Practically, however, there is no limit to what type of component can be stored in a Maven repository. For example, you can easily deploy WAR or EAR files, source archives, Flash libraries and applications, Android archives or applications, or Ruby libraries to a Maven repository.

Every software component is described by an XML document called a Project Object Model (POM). This POM contains information that describes a project and lists a project’s dependencies — the binary software components, which a given component depends upon for successful compilation or execution.

When Maven downloads a component like a dependency or a plugin from a repository, it also downloads that component’s POM. Given a component’s POM, Maven can then download any other components that are required by that component.

Maven and other tools, such as Ivy or Gradle, interact with a Maven repository to search for binary software components, model the projects they manage, and retrieve software components on-demand from a repository.

## npm Registry

The command line tool `npm` is a package management solution for Javascript-based development. It is used to create and use node-packaged modules and is built into the Javascript platform [Node.js](http://www.nodejs.org/) .

Nexus Repository supports the npm registry format for proxy repositories. This allows you to take advantage of the packages in the npm registry and other public registries without incurring repeated downloads of packages since they will be proxied in the Nexus Repository.

In addition, Nexus Repository supports running a private registry, also known as a hosted repository, using the *npm* format. You can share internally developed, proprietary packages within your organization via these private registries allowing you to collaborate efficiently across development teams with a central package exchange and storage location.

To share a package or tool with npm, you create a npm package and store it in a npm-hosted repository. Similarly, you can use packages others have created and made available in their npm repositories by proxying them or downloading the packages and installing them in your own private registry for third-party packages.

To simplify configuration Nexus Repository supports aggregation of npm registries into a single group. This allows you to expose all the external packages from the npm registry and other public registries as well as the private registries as one registry, which greatly simplifies client configuration.

### Proxying npm Registries

To reduce duplicate downloads and improve download speeds for your developers and CI servers, you should proxy the registry served at [https://registry.npmjs.org](https://registry.npmjs.org) . By default, npm accesses this registry directly. You can also proxy any other registries you require.

To proxy an external npm registry, you simply create a new *npm (proxy)* as documented in the Repository Management section .

Minimal configuration steps are:

- Define *Name*
- Define URL for Remote storage e.g. `https://registry.npmjs.org`
- Select *Blob store* for Storage

**Note:** Once you create an npm proxy repository, do not change the remote server URL. Doing so may result in 404s as Nexus Repository attempts to retrieve cached data. Instead, create a new proxy repository.

### Private npm Registries

A private npm registry can be used to upload your own packages as well as third-party packages. You can create a private npm registry by setting up a hosted repository with the *npm* format. It is good practice to create two separate hosted repositories for these purposes.

To create a hosted repository with npm format, simply create a new *npm (hosted)* as documented in the Repository Management section .

Minimal configuration steps are:

- Define *Name*
- Select *Blob store* for Storage

The npm registry information is immediately updated as packages are deployed or deleted from the repository.

### Grouping npm Registries

A repository group is the recommended way to expose your npm registry repositories to your users, with minimal client-side configuration. A repository group allows you to expose the aggregated content of multiple proxy and hosted repositories with one URL to npm and other tools. This is possible for npm repositories by creating a new *npm (group)* as documented in the Repository Management section .

Minimal configuration steps are:

- Define *Name*
- Select *Blob store* for Storage
- Add npm repositories to the *Members* list in the desired order

A typical, useful example would be to group a npm-hosted repository with internal software packages, another npm-hosted repository with third-party packages, and the proxy repository that proxies the npm registry.

Using the URL of the repository group as your npm repository URL in your client tool will give you access to the packages in all three repositories with one URL. Any new packages added as well as any new repositories added to the group will automatically be available.

You can push images to the group repository as documented in [publishing npm packages](#UUID-5124f46e-76f4-9a2f-aa97-7e7bc051e226) .

### Browsing npm Registries and Searching Modules

You can browse npm repositories in the user interface inspecting the components and assets and their details as documented in [Browsing Repositories and Repository Groups](#UUID-e108d1b2-66c8-269a-18d0-d0557d9ae8d9) .

Searching for npm modules can be performed in the user interface as described in the Searching for Components section . This search will find all npm modules images that are currently stored in the Nexus Repository, either because they have been pushed to a hosted repository or they have been proxied from an upstream repository and cached locally.

### Configuring npm

Once you have set up your hosted and proxy repositories for npm packages and created a repository group to merge them, you can access them with the npm tool on the command line as one registry.

**Note:** Once you create an npm proxy repository, do not change the remote server URL. Doing so may result in 404s as Nexus Repository attempts to retrieve cached data. Instead, create a new proxy repository.

You can configure the registry used by npm in your `.npmrc` file located in your user's home directory with the npm config command and the public URL of your repository group available in the repository list by clicking the copy button in the URL column of either Settings → Repository → Repositories or user's Browse page.

**For example:**

```
npm config set registry http://localhost:8081/repository/npm-all/
```

The command inserts the configuration in the `.npmrc` file in your users home directory.

### npm Security

When Anonymous Access is enabled, any anonymous user has read access to the repositories and repository groups. If disabled or write access is required for publishing a package, the user needs to authenticate to the repository manager. There are two methods to authenticate npm with your repository manager; you should only use one at a time.

### Publishing npm Packages

Publishing packages to a npm hosted or group repository allows you to share packages across your organization or with external partners. With authentication configured, you can publish your packages with the `npm publish` command. Review [npm Security documentation](#UUID-30689352-0c3c-75b2-e88f-e549d8449862) for authentication requirements.

To publish to a group repository requires Nexus Repository Pro.

### Deprecating npm Packages

Once your packages have been pushed to an npm hosted repository, you can mark them as deprecated. This is useful when a newer version of the package is available and you want to warn people that the old package has reached end of life, or you want to avoid usage and warn your users for some other reason.

The `npm deprecate` command uses a `registry` configuration value to inform where the package lives. To deprecate an existing package, use a command like the following:

```
npm deprecate --registry http://localhost:8081/repository/npm-internal/ testproject1@0.0.1 "This package is deprecated" 
```

If you change your mind, you can reverse this action using the same command. To un-deprecate a package, pass an empty string to the deprecate command:

```
npm deprecate --registry http://localhost:8081/repository/npm-internal/ testproject1@0.0.1 ""
```

The message text is persisted in the deprecated attribute of the `packageJson` section for the asset and can be viewed in the user interface.

**Note:** Nexus Repository does not support the `unpublish` operation.

### npm audit

The `npm audit` command submits a list of the dependencies from your project and returns a report of security violations. The report includes instructions on how you could remediate the issues.

Nexus Repository may be configured to use Sonatype Repository Firewall as a data source for npm audit to return results that align with your open-source governance policies.

- Requires a license for Sonatype Repository Firewall. Configure the Repository Firewall to audit your npm proxy repositories.
- Configure your npm project within Nexus Repository to use the `npm audit` command from the Repository Firewall. See [Configuring npm](#UUID-49017064-86a8-7d6b-0acb-cfca9e4a1a5d)
- `npm audit` is supported with proxy and group repositories.
- Use `npm audit fix` to automatically remediate vulnerable dependencies.

![93487610.png](/assets/images/uuid-99dd178a-3c38-f15d-7ae1-43e626a3640b.png)

### Download Cataloged Versions Only for Proxied Repositories

**Note:** This feature is sunsetted as of January 2024. Use [Blocking Unknown Components](#UUID-1bfeefa8-2f91-aa49-084a-10277c975049) with Repository Firewall's Release Integrity going forward.

Enforcing an IQ server policy to block non-cataloged components can lead to build errors and can be difficult for developers to troubleshoot.The npm package metadata will contain all available versions; however, retrieving a non-cataloged tarball will fail when Sonatype Repository Firewall is enabled.

This often happens when a project uses the latest tag for a dependency that was recently updated and IQ Server has not yet cataloged the new version. You can manually intervene to pin versions, but this requires handling both direct and transitive dependencies.

Instead, configure Sonatype Nexus Repository to remove non-catalogued versions from npm package metadata. With this option enabled, npm will only use new versions that are known to Nexus Intelligence.Once the component is known, it will appear in the proxied metadata.

To configure Sonatype Nexus Repository to remove non-cataloged versions from the npm package metadata, you must configure two settings: First, enable the *Firewall Audit and Quarantine* capability on the proxy repository. Second, enable the *Download cataloged versions only* option in the repository settings page.

### Policy-Compliant Component Selection for npm

When a user requests an npm package without explicitly specifying a version (e.g., `npm install package` ) or specifying a version range, the npm client relies on the package metadata from the npm registry to select a version that satisfies the version constraints. When the selected version has policy violation and is quarantined by Sonatype Repository Firewall, it causes a build failure that requires a manual fix of the root cause.

By enabling this option, Repository Firewall removes quarantined versions from the npm package metadata to prevent selecting a version with policy violations.

See the [Repository Firewall](#UUID-7829d2e3-1dd8-fa14-2d15-efac883b9cc5) documentation on policy-compliant component selection.

## NuGet Repositories

NuGet offers a robust package management solution for .NET developers, streamlining the handling of libraries and tools in .NET Framework Visual Studio projects.

Nexus Repository provides hosting, proxying, and grouping capabilities for NuGet repositories. This combination improves collaboration, control, and efficiency in .NET development. Utilize a centralized repository to maximize benefits and streamline access to internal and external packages.

The NuGet format uses OData queries for communication between the client and the repository. These queries include metadata information about available packages and other data. Nexus Repository caches recent queries and returns cached metadata when the same query is sent before the cache expires.

The initial installation of Nexus Repository includes the following NuGet repositories:

- `nuget.org-proxy` - proxy to the NuGet gallery
- `nuget-hosted` - to upload your developed packages and third-party packages
- `nuget-group` - Group combining the proxy and the hosted repositories

![nx-repository-proxy-nuget.png](/assets/images/uuid-727c1d8e-ae7b-9df9-5f00-3ee3f1a6874a.png)

### NuGet Proxy Repository

Use the following to configure a proxy to a remote NuGet repository:

### NuGet Hosted Repositories

Hosted NuGet repositories are used to upload your developed packages and third-party packages. NuGet-hosted repositories may use either the v2 or v3 endpoints.

- Use the `Nuget (hosted)` repository recipe to create a NuGet-hosted repository.
- To use the V3 protocol on a hosted repository, add the service index as the source.

### NuGet Group Repository

Group repositories streamline how users access NuGet repositories. This eliminates the need for additional client-side configuration as the repository group aggregates the content of multiple proxy and hosted repositories, presenting them through a single URL for your tools. The system automatically includes new packages and repositories added to the group.

### Configure NuGet Client

You have several options for configuring your NuGet client to use Nexus Repository.

### Publishing to a Hosted Repository

You use the group repository when adding packages to your project to access packages from any source in your group. When publishing, you must publish directly to the hosted repository.

The following includes an example of setting your `nuget.config` to include both the group and hosted repository.

```
<configuration>
  <packageSources>
    <clear />
    <add key="Nexus" value="http://your-nexus-server:8081/repository/nuget-group/index.json" />
    <add key="NexusHosted" value="http://your-nexus-server:8081/repository/nuget-hosted/" />
  </packageSources>
  <packageSourceCredentials>
    <Nexus>
      <add key="Username" value="%NUGET_USERNAME%" />
      <add key="ClearTextPassword" value="%NUGET_API_KEY%" />
    </Nexus>
    <NexusHosted>
      <add key="Username" value="%NUGET_USERNAME%" />
      <add key="ClearTextPassword" value="%NUGET_API_KEY%" /> 
    </NexusHosted>
  </packageSourceCredentials>
</configuration>
```

When pushing your package to the hosted repository use the following format:

```
dotnet nuget push your-package.nupkg -s NexusHosted

```

### Support Notes

**Note:** NuGet V2 verse V3 Permissions NuGet version 2 does not need the browse permissions while NuGet v3 does.

## p2 Repositories

P2 is a technology for provisioning and managing Eclipse- and Equinox-based applications. Use p2 to install or manage any aspect of your application, from the physical plugins and native code to the configuration of the installed software: file permissions, command line arguments, etc.

Installation with p2 does not consist simply in adding or removing files in the file system, but more generally the sequence of events that must occur to lay down and configure a system that is ready to run.

### Supported Features

- Repository types - Proxy
- Simple p2 plugin repositories
- Composite p2 plugin repositories
- Update sites
- Features, Plugins, Binary types of files
- Eclipse IDE version 4.2.2 or later (support for earlier versions is not guaranteed)
- Auto-blocking unreachable remote repositories is disabled by default due to connection problems.

### Proxying p2 Repositories

You can set up a p2 proxy repository to access a remote repository location, for example, to proxy the Eclipse Foundation repository.

To proxy a p2 repository, create a new *p2 (proxy)* as documented in the Repository Management section .

Minimum steps are:

- Define the proxy name.
- Define URL of the remote storage.
- Select a blob store

### Browsing p2 Repositories and Searching Packages

You can browse p2 repositories in the user interface inspecting the components and assets and their details, as described in the Browsing Repositories and Repository Groups section .

Searching for p2 packages can be performed in the user interface, too. It finds all packages that are currently stored in the repository manager, as described in the Searching for Components section .

### Configuring the Eclipse IDE to use Nexus Repository

All p2 plugins are possible to install via Help → Install new software.

- Unselect the checkbox 'Contact all update sites during install to find required software' for installing directly.
- Select **Add** button to add plugin source and put in the URL field the Nexus Repository proxy repository URL. Here we are going to use the `p2-proxy` repository.
- Click **Manage** button if you want to manage your sources. There are some Eclipse sources here by default, you can disable them if you need just NXRM sources (deleting these resources will not lead to the desired result, they will appear again after the application is restarted).

## PyPI Repositories

The Python Package Index, or PyPI, is a vast repository of open-source Python packages supplied by the worldwide community of Python developers. The official index is available at [https://pypi.org](https://pypi.org) , and the site itself is maintained by the [Python Software Foundation](https://www.python.org/psf/) .

Nexus Repository supports proxying the Python Package Index. This takes advantage of the packages in the official Python Package Index without incurring repeated downloads to reduce time and bandwidth usage for accessing Python packages.

Also, you can publish your packages to a private index as a hosted repository, and expose the remote and private repositories as a repository group that merges and exposes the contents of multiple repositories in one convenient URL.

**Note:** When using pip, consider setting Nexus Repository to use SSL or you must include the `--trusted-host` property at the end of your requests or configure pip to trust your Nexus Repository.

### Proxying PyPI Repositories

You can set up a PyPI proxy repository to access a remote package index. To proxy a PyPI package index, you simply create a new PyPI (proxy) recipe.

Minimal configuration steps are:

- Define *Name* - e.g. `pypi-proxy`
- Define URL for *Remote storage* . The official Python Package Index Remote Storage URL value to enter is `https://pypi.org/` . Using `https://pypi.python.org/` should also work as long as redirects are maintained.

**Note:** Nexus Repository currently requires the remote PyPI repository to support the `/simple` endpoint. Repositories that do not follow this convention, such as `https://pypi.nvidia.com` , are not supported at this time.

The repository manager can access Python packages and tools from the remote index. The proxy repository for PyPI packages provides a cache of files available on the index making access to components from the Python Package Index more reliable. Users will be able to browse and search assets against the remote, as mentioned in [Browsing PyPI Repositories and Searching Packages](#UUID-cf61c414-5e87-b6bf-b15b-3263be3d85de_id_PyPIRepositories-BrowsingPyPIRepositoriesandSearchingPackages) .

### Hosting PyPI Repositories

Creating a PyPI-hosted repository allows you to upload packages in the repository manager. The hosted repository acts as an authoritative location for packages fetched from the Python index.

To host a PyPI package, create a new *PyPI (hosted)* recipe.

Minimal configuration steps are:

- Define *Name* - e.g., `pypi-internal`
- Pick a *Blob store* for *Storage*

### Grouping PyPI Repositories

A repository group is the recommended way to expose all your PyPI repositories from the repository manager to your users, with minimal additional client-side configuration. A repository group allows you to expose the aggregated content of multiple proxies and hosted repositories as well as other repository groups with one URL in the tool configuration. PyPI group repositories can be created with the PyPI (group) recipe.

Minimal configuration steps are:

- Define *Name* - e.g., `pypi-all`
- Pick a *Blob store* for *Storage*
- Add PyPI repositories to the *Members* list in the desired order

### Installing PyPI Client Tools

The latest versions of such Linux distributions as CentOS and Ubuntu come packaged with Python and [pip](https://pip.pypa.io/en/stable/) , a tool for installing and managing Python packages from the index. For Mac OS X and Microsoft Windows, download and install a Python version compatible with the repository manager from [https://www.python.org/downloads/](https://www.python.org/downloads/) . This should come automatically with pip but you can see [https://pip.pypa.io/en/stable/installation/](https://pip.pypa.io/en/stable/installation/) if not.

**Note:** Nexus Repository only supports specific versions of Python, pip, and setuptools. For Python, only the latest two releases of 2 and 3 are supported. For pip the latest two versions are supported. setuptools removed easy_install from their application in newer versions so only 51.3.3 and older will work. Versions not listed may work but issues with them are unlikely to be addressed if found.

### Configuring PyPI Client Tools

**Note:** Depending on your preference for [twine](https://pypi.python.org/pypi/twine) , [distutils](https://docs.python.org/2.7/library/distutils.html) , pip, and setuptools, your proxy and hosted configuration will vary.

Once you have installed all necessary client tools from the Python Package Index, you can create and configure a `.pypirc` file to reference packages stored in the repository manager. Depending on your Python configuration you can manage your repository groups with `pip.conf` (or `setup.cfg` ) to have all commands, such as search and install, run against your project.

### SSL Usage for PyPI Repositories

You can proxy Python packages over HTTPS to ensure a secure connection with a self-signed certificate. This works for proxy, hosted, and group repositories. To set up the repository manager to serve HTTPS follow the configuration steps in [Configuring SSL](#UUID-8554ddb3-3cbe-c1ac-10bd-fa349b6fa1fe) .

Also, you can set up pip to use the certificate to enable SSL and fetch packages securely. Additional configuration is necessary for the HTTPS client implementation to work. This assumes the repository manager has already been set up to use SSL, so verify your certificate works. Run the following command:

```
openssl verify <example-cerfificate>
```

When your certificate is proven to work, update your `pip.conf` . Here is an example configuration file for a repository group:

```
[global]
index = https://localhost:8443/repository/pypi-all/pypi
index-url = https://localhost:8443/repository/pypi-all/simple
cert = nexus.pem
```

### Browsing PyPI Repositories and Searching Packages

You can browse PyPI repositories in the user interface inspecting the components and assets and their details, as described in the Browsing Repositories and Repository Groups section .

Searching for PyPI packages can be performed in the user interface, as described in the Searching for Components section . It finds all packages that are currently stored in the repository manager, either because they have been pushed to a hosted repository or they have been proxied from an upstream repository and cached in the repository manager.

From the command line, you can search available PyPI packages defined in your configuration. This method is limited to pip ( `pip.conf` ).

To search, run:

```
pip search example-package
```

**Note:** "pip search" command is [deprecated](https://github.com/pypa/pip/issues/5216) and doesn't work with a proxy repository, but you can still search for packages in hosted repositories.

### Uploading PyPI Packages

**Note:** The steps to upload a PyPI package will vary if your system is configured with `twine` or `setuptools` .

After you configure your `.pypirc` you can upload packages from the index to the repository manager.

In the example below, twine is invoked to tell your repository what server to use when uploading a package. The `-r` flag is used to find the NXRM server in your `.pypirc` .

```
twine upload -r pypi <filename>
```

### Policy-Compliant Component Selection for PyPI

**Note:** Policy-compliant component selection for PyPI requires IQ Server version 167+. This functionality requires integration with Sonatype Repository Firewall and a Firewall license.

When a user requests a PyPI package without explicitly specifying a version, the PyPI client relies on the package metadata to select a version that satisfies the version constraints. If the selected version has policy violations and is quarantined by the Sonatype Repository Firewall, it will cause a build failure that requires a manual fix of the root cause.

By enabling this option, the Repository Firewall will remove quarantined versions from the PyPI package metadata to prevent you from selecting a version with policy violations.

Two settings are needed to enable this behavior:

## R Repositories

### Introduction

[R](https://www.r-project.org/) is a language used for statistical analysis and machine learning. R and R Studio both allow you to install packages from repositories, allowing convenient access to a large number of packages from the remote Comprehensive R Archive Network ( [CRAN](https://cran.r-project.org/) ).

Sonatype Nexus Repository takes advantage of the packages in the official CRAN repository and other public repositories without incurring repeated downloads of packages.

You can publish your own packages to a private repository in a hosted R repository and then combine the remote and private repositories to R as a repository group, which is a repository that merges and exposes the contents of multiple repositories in one convenient URL. This allows you to reduce time and bandwidth usage for accessing R packages as well as more easily share your packages within your organization.

**Note:** This format is disabled by default in legacy High Availability Clustering (HA-C) environments.

### Supported File Types

Proxy R repositories support any file type.

Hosted and group R repositories only support files with a `.gz` extension.

If your proxy R repository is part of a group, you will only be able to request files with a `.gz` extension through the group. You will need to request any other file type directly from the proxy repository.

### Proxying R Repositories

You can set up an R proxy repository to access a remote repository location.

To proxy an R repository, create a new *r (proxy)* as shown in the documented example in the Repository Management section n detail. Minimal configuration steps for R proxy are:

- Define *Name* , e.g. `r-proxy`
- Define *URL* for *Remote storage* , e.g. [https://cran.r-project.org/](https://cran.r-project.org/)
- Select a *Blob store* for *Storage*

### Hosting R Repositories

**Note:** Hosted R repositories only support files with a `.gz` extension.

Creating an R hosted repository allows you to register packages in the repository manager. The hosted repository acts as an authoritative location for these components.

To add a hosted R repository, create a new repository with the recipe *r (hosted)* as shown in the documented example in the Repository Management section . Minimal configuration steps for R hosted are:

- Define *Name* , e.g. `r-hosted`
- Select *Blob store* for *Storage*

### Deploying Packages to R Hosted Repositories

**Note:** Hosted R repositories only support files with a `.gz` extension.

### R Repository Groups

**Note:** Group R repositories only support files with a `.gz` extension.

A repository group is the recommended way to expose all your R repositories from the repository manager to your users, with minimal additional client-side configuration. A repository group allows you to expose the aggregated content of multiple proxy and hosted repositories as well as other repository groups with one URL in tool configuration. This is possible by creating a new repository with the *r (group)* recipe as shown in the documented example in the Repository Management section . Minimal configuration steps for R group are:

- Define *Name* , e.g. `r-group`
- Select *Blob store* for *Storage*
- Add R repositories to the *Members* list in the desired order

If you request a file from a group and that file is present in more than one group member, the group will return merged data.

### Configuring R Client

Once you have set up your repositories for R packages, you can adjust your R startup script to use your repository URLs. A suggested way to do so is to create a `.Rprofile` file and include a snippet similar to the following in it:

```
## Default repo 
local({r <- getOption("repos")        
        r["Nexus"] <- "http://<host>:<port>/repository/<repository_name>"        
        options(repos=r)
 })
```

This will set your default R repository as the group repository. For more information on adjusting R startup files, please visit the [mini guide on the r-bloggers](https://www.r-bloggers.com/fun-with-rprofile-and-customizing-r-startup) .

Also, it is possible to install an R package directly from the R client console:

```
install.packages("example", repos="http://<host>:<port>/repository/<repository_name>", type="<package_type>")
```

`<package_type>` is optional and accepts values of `source` and `binary` . If left off the console command, it defaults to `binary` .

If anonymous access to the repository manager is disabled, you have to specify the credentials for the accessing the repository manager as part of the URL like `http://<username>:<password>@<host>:<port>/repository/<repository_name>` .

Downloaded packages are cached, do not have to be retrieved from the remote repositories again and can be inspected in the user interface.

## Raw Repositories

### Introduction

Nexus Repository includes support for hosting, proxying and grouping static websites - the raw format. Hosted repositories with this format can be used to store and provide a Maven-generated website. Proxy repositories can subsequently proxy them in other servers. The raw format can also be used for other resources than HTML files exposed by straight HTTP-like browsable directory structures.

This section details the process of configuring raw repositories, configuring a simple Maven project to publish a Maven-generated project site and other use cases for raw repositories.

### Creating a Hosted Raw Repository

To create a raw repository for hosting a static website, you simply create a new repository using the *raw (hosted)* recipe as documented in the Repository Management section .

For the Maven site example in [Creating and Deploying a Maven Site](#UUID-1b5b869d-fafc-7438-01d2-c95f93b397c1_id_RawRepositories-CreatingandDeployingaMavenSite) , set the *Name* to `site` and change the *Deployment policy* to *Allow redeploy* and a ** of *Inline* .

After creating the new raw repository, it appears in the list of repositories with the name site provided earlier. The *URL* accessable in the list can be used for deployment and access usage.

**Note:** Disable the *Strict Content Type Validation* if you encounter problems related to the content MIME-type.

### Creating and Deploying a Maven Site

### Proxying and Grouping Raw Repositories

Beside the common use case using hosted raw repositories for site deployments, the repository manager supports proxying as well as grouping of raw repositories.

The creation follows the same process as documented in the Repository Management section using the *raw (proxy)* and the *raw* *(group)* recipes.

A raw proxy repository can be used to proxy any static website. This includes a Maven site hosted in a raw repository in another Nexus Repository Manager server or a plain static website hosted on another web server like Apache httpd. It can also be used to proxy directory structures exposed via a web server to distribute archives such as `https://nodejs.org/dist/` .

**Note:** No content is modified when proxied. This means that e.g., any absolute URL used with HTML document remain absolute and therefore bypass the proxying mechanism.

Grouping raw repositories is possible and can e.g., be used to aggregate multiple site repositories. However keep in mind that the raw format does not contain any logic to resolve conflicts between the different repositories in the group. Any request to the group causes the repository manager to check the member repositories in order and return the first matching content.

### Content Disposition

The Content-Disposition response header indicates if the content in your raw repository should be displayed inline in the browser (i.e., as a web page) or as an attachment that a user downloads. By default, new raw repositories are assigned a Content-Disposition header of *Attachment* . However, if you would like to change this to *Inline* , you may do so by modifying the *Content Disposition* field in the configuration options for your raw repository.

### Uploading Files to Hosted Raw Repositories

Many other tools, besides using Maven, can be used to upload files to a hosted raw repository. A simple `HTTP PUT` can upload files. The following example uses the `curl` command and the default credentials of the admin user to upload a `test.png` file to a hosted raw repository with the name `documentation` .

**An Example Upload Command Using curl**

```
curl -v --user 'admin:admin123' --upload-file ./test.png http://localhost:8081/repository/documentation/test.png
```

After a completed upload the repository manager provides the file at the URL `http://localhost:8081/repository/documentation/test.png` . Using this approach in a script entire static websites or any other binary resources can be uploaded.

A complete static website consisting of numerous HTML, CSS, JS and image files or some other directory structure of multiple files and resources can be uploaded with a script that assembles and issues numerous `HTTP PUT` requests.

The [raw folder of the nexus-book-examples repository](https://github.com/sonatype/nexus-book-examples/tree/nexus-3.x/raw) contains the Groovy script `rawPopulator.groovy` as an example of such a script as well as a simplistic website of two HTML pages in the `site` directory. You can upload the directory to a raw repository with the name `documentation` to your repository manager at `http://repo.example.com:8081` with:

**Example invocation of the rawPopulator script**

```
$ groovy rawPopulator.groovy -d site -r documentation -u admin -p admin123 -h http://repo.example.com:8081
Staging 2 files for publishing
pushing site/index.html
POST response status: HTTP/1.1 201 Created
pushing site/success.html
POST response status: HTTP/1.1 201 Created
```

After the upload, you can access the site at `http://repo.example.com:8081/repository/documentation/` to load `index.html` and clicking on the link directs you to the `success.html` page.

## RubyGems Repositories

RubyGems ( [rubygems.org](http://rubygems.org) ) is the leading gem hosting service supporting the Ruby community. The Ruby programming language uses the `Gem` tool as its package management solution. Packages are called `gems` allowing for ease of use when distributing programs or libraries.

The following features are included as part of gem repository support:

- **Proxy repository** for connecting to remote gem repositories and caching gems on the repository manager to avoid duplicate downloads and wasted bandwidth and time
- **Hosted repository** for hosting gem packages and providing them to users
- **Repository groups** for merging multiple hosted and proxy gem repositories and easily exposing them as one URL to all users

### Requirements

Gem repositories are supported as of version NXRM 3.1 and higher however major changes to the Gem tooling API forced an update to how Nexus Repository communicates with RubyGem repositories and clients.

We recommend the following minimum versions:

- `Nexus Repository` : release 3.53.0 or later
- `RubyGem client` : version 3.4.12 or later

### Proxying RubyGem Repositories

Proxy a gem repository by creating a new repository using the recipe `rubygems (proxy)`

Minimal configuration steps are:

- Define *Name*
- Define URL for *Remote storage* e.g. `https://rubygems.org`
- Pick a *Blob store* for *Storage*

### Private Hosted RubyGem Repositories

A private gem repository can be used as a target to push your gems as well as third-party gems and subsequently provide them to your users. It is a good practice to create two separate hosted gem repositories for internal and third-party gems.

To create a hosted gem repository, create a new repository using the recipe rubygems (hosted).

Minimal configuration steps are:

- Define *Name*
- Select a *Blob store* for *Storage*

The gem repository information is immediately updated as gems are pushed to the repository or deleted from it.

### Grouping RubyGem Repositories

A repository group is the recommended way to expose all your gem repositories to your users, without needing any further client-side configuration after initial setup. A repository group allows you to expose the aggregated content of multiple proxies and hosted gem repositories with one URL to gem and other tools.

To create a gem group repository, create a new repository using the recipe rubygems (group).

Minimal configuration steps are:

- Define *Name*
- Select *Blob store* for *Storage*
- Add Gems repositories to the *Members* list in the desired order

A typical, useful example would be to group the proxy repository that proxies the RubyGems repository, a hosted gem repository with internal software gems, and another hosted gem repository with third-party gems.

Using the repository URL of the repository group as your gem repository URL in your client tool gives you access to the gems in all member repositories with one URL.

Any gem added to a hosted or proxy repository becomes immediately available to all users of the gem repository group. Adding a new proxy gem repository to the group makes all gems in that proxy immediately available to the users as well.

### Using RubyGem Repositories

Once you have configured the repository manager with the gem repository group, you can add it to your configuration for the `gem` command line tool.

You can add the URL of a gem repository or group using the URL from the repository list with a command like:

```
$ gem sources --add http://localhost:8081/repository/rubygems-group/
```

In order to take full advantage of the repository manager and the proxying of gems, you should remove any other sources. By default, [https://rubygems.org/](https://rubygems.org/) is configured in gem and this can be removed with:

```
$ gem sources --remove https://rubygems.org/
```

Clear the local cache with:

```
$ gem sources -c 
```

To check a successful configuration you can run:

```
$ gem sources
*** CURRENT SOURCES ***


http://localhost:8081/repository/rubygems-group/ 
```

With this setup completed, any installation of new gems with `gem install <gem_name>` (e.g. `gem install rake` ) will be downloaded from the repository manager.

If your repository manager requires authentication, you have to add the *Basic Auth* authentication details to the configuration of the source:

```
$ gem sources --add http://myuser:mypassword@localhost:8081/repository/rubygems-group/
```

If you are using the popular [Bundler tool](http://bundler.io/) for tracking and installing gems, you need to install it with the gem:

```
$ gem install bundle
Fetching: bundler-1.7.7.gem (100%)
Successfully installed bundler-1.7.7
Fetching: bundle-0.0.1.gem (100%)
Successfully installed bundle-0.0.1
Parsing documentation for bundle-0.0.1
Installing ri documentation for bundle-0.0.1
Parsing documentation for bundler-1.7.7
Installing ri documentation for bundler-1.7.7
Done installing documentation for bundle, bundler after 4 seconds
2 gems installed 
```

To use the repository manager with Bundler, you have to configure the gem repository group as a mirror:

```
$ bundle config mirror.http://rubygems.org
http://localhost:8081/repository/rubygems-group/
```

You can confirm the configuration succeeded by checking the configuration:

```
$ bundle config
Settings are listed in order of priority. The top value will be used.
mirror.http://rubygems.org
Set for the current user (/Users/manfred/.bundle/config): "http://localhost:8081/repository/rubygems-group" 
```

With this configuration completed, you can create a `Gemfile` and run `bundle install` as usual and any downloads of gem files will be using the gem repository group configured as a mirror.

### Pushing Gems

At this point, you have set up the various gem repositories on the Nexus Repository (proxy, hosted, and group), and are successfully using them for installing new gems on your systems. The next step can be to push gems to hosted gem repositories to provide them to other users. All this can be achieved on the command line with the features of the `nexus` gem.

The `nexus` gem is available at RubyGems and provides features to interact with Nexus Repository including pushing gems to a hosted gem repository including the necessary authentication.

You can install the Nexus gem with:

```
$ gem install nexus
Fetching: nexus-1.2.1.gem (100%)
...
Successfully installed nexus-1.2.1
Parsing documentation for nexus-1.2.1
Installing ri documentation for nexus-1.2.1
Done installing
```

After successful installation, you can push your gem to a desired repository. The initial invocation will request the URL for the gem repository and the credentials needed for deployment. Subsequent pushes will use the cached information.

```
$ gem nexus example-1.0.0.gem
Enter the URL of the rubygems repository on a Nexus server
URL: http://localhost:8081/repository/rubygems-hosted
The Nexus URL has been stored in ~/.gem/nexus
Enter your Nexus credentials
Username: admin
Password:
Your Nexus credentials has been stored in /Users/manfred/.gem/nexus
Uploading gem to Nexus...
Created
```

By default, pushing an identical version to the repository, known as redeployment, is not allowed in a hosted gem repository. If desired this configuration can be changed, although we suggest changing the version for each new deployment instead.

The nexus gem provides several additional features and parameters. You can access the documentation with:

```
$ gem help nexus 
```

E.g. you can access a list of all configured repositories with:

```
$ gem nexus --all-repos
DEFAULT: http://localhost:8081/repository/rubygems-hosted
```

## Rust / Cargo Repositories

Rust is known for its memory safety, concurrency, and performance. Cargo, Rust's build tool and package manager, automates dependency management through building and testing your application.

Cargo uses a `Cargo.toml` manifest file to declare project dependencies. Cargo uses this manifest to fetch and build these dependencies from the public registry ensuring consistent builds. It automates the compilation and linking process, including handling builds for different target platforms and configurations.

### Supported Features and Limitations

This section covers supported features and limitations for Rust Cargo in the Nexus Repository.

- Nexus Repository supports Cargo hosted, proxy, and group repositories.
- Nexus Repository does not currently support uploading components via the UI or API; use the `cargo publish` command to publish components to a hosted repository.
- Nexus Repository only supports Cargo's `sparse` protocol; the Git protocol is not supported.
- Nexus Repository's support for Rust Cargo is not compatible with the community plugin. You will not be able to migrate data from the plugin.
- **Cargo Versions** - 1.68+
- Nexus Repository does not support the Cargo client native search capability
- Nexus Repository does support `yank` and `unyank` endpoints; however, use `yank` with caution as it can break builds for users who haven't locked their dependencies

### Proxy Configuration

When setting the proxy repository include a trailing slash (' `/` ') on the Remote URL.

```
https://index.crates.io/
```

### Example Rust Configuration

Cargo's config.toml is a configuration file used to set up Rust's package manager (Cargo) to work with Nexus Repository. This file is important when configuring Cargo to use Nexus Repository as a proxy or hosted repository for Rust packages.

Use the `sparse+` prefix in your registry URL. This is required for the Cargo sparse protocol.

Example `config.toml` :

```
[registries]
cargo-proxy = { index = "sparse+http://nexus.example/repository/cargo-proxy/" }
cargo-group = { index = "sparse+http://nexus.example/repository/cargo-group/" }

[registries.cargo-hosted]
index = "sparse+http://nexus.example/repository/cargo-hosted/"
token = "Basic YWRtaW46YWRtaW4xMjM="

[source.crates-io]
replace-with = "cargo-proxy" # Change it dependening of the test case
```

Key elements in this configuration:

- `[registries]` : configures global settings for Cargo registries.
- `[source.crates-io]` : configures Cargo to replace the default crates.io source with your Nexus repository
- `[registries.cargo-hosted]` : defines the Nexus Repository, with the `sparse+` prefix indicating the use of Cargo's Sparse protocol. The user token is included for authentication.

### Security Configuration

Use SSL configuration (HTTP/HTTPS settings) for secure data transfer and repository access.

Cargo clients rely on a specific signal in the `config.json` file to determine authentication requirements, which could lead to unexpected behavior when anonymous access is enabled in Nexus Repository but restricted by the individual Cargo repository.

When creating proxy or group Cargo repositories, use the *Restrict repository content to authenticated users* checkbox to set `auth-required` in `/config.json` responses and ignore anonymous access configuration.

### Authenticating with User Tokens for Cargo

For Cargo, user tokens are configured in the Cargo credentials config file ( `credentials.toml` ). Each token is associated with a specific repository and only authenticates access to that particular repository. Tokens are primarily used during the crate publishing process.

To use your user token for Cargo repository authentication, take the following steps:

- Generate and access your user token following the instructions in our [user token help documentation](#UUID-59c4617b-badf-62e5-69d8-8cfa25f314ff) . Copy the base64 representation of your user token.
- Open your Cargo credentials config file ( `credentials.toml` ); add and save the following lines, replacing the registry name with the name of your repository, and `<your-token>` with the base64 representation of your user token: Alternatively, you can use a command like the following to update the file: This will result in a prompt for your repository's token. Provide it as `Basic <your-token>` to update the file. Or, you can use an environment variable by running a command like the following:
- You can test your authentication by running a command like `cargo publish` to publish a crate to your hosted repository.

## Yum Repositories

### Introduction

[Yum or "Yellowdog Updater, Modified"](http://yum.baseurl.org/) is a command line package management utility for Linux distributions using the RPM package manager. It allows you to easily install many commonly used Linux packages on distributions such as RedHat, CentOS, and Fedora.

**Note:** We do not currently support upgrading Yum repositories on Nexus Repository version 2 to Nexus Repository version 3. Nexus Repository does not support new Yum v4 features.

### Proxying Yum Repositories

You can set up a Yum proxy repository to access a remote repository location.

To proxy a Yum repository, you simply create a new *yum (proxy)* as documented in the Repository Management section .

Minimal configuration steps are as follows:

- Define *Name* (e.g., `yum-proxy` )
- Define URL for *Remote storage* (e.g., `http://mirror.centos.org/centos/` )
- Pick a *Blob store* for *Storage*

**Note:** Nexus Repository does not create a default Yum proxy repository. You will need to determine which repositories are appropriate for your environment.

See [Proxying RHEL Yum Repositories](#UUID-1145d77d-022d-fec5-f3fa-826f2367fbc0) for instructions on proxying Red Hat Enterprise Linux Yum repositories. Also, see [GPG signatures for Yum Proxy/Group](#UUID-2964b6f5-4933-0ef6-fbab-3d58e770a09d) for signing data with a GPG key.

### Hosting Yum Repositories

A hosted repository for Yum can be used to upload both your own and third-party RPMs. To host a Yum RPM, create a new *yum (hosted)* repository as documented in the Repository Management section .

Minimal configuration steps for creating a Yum Hosted repository are as follows:

- Define *Name* e.g., `yum-hosted`
- Select a value for *Repodata Depth*
- Pick a *Blob store* for *Storage*

### Deploying Packages to Yum Hosted Repositories

The Yum client does not come with a method for uploading RPMs; however, you can use many other tools to upload files to a hosted Yum repository using a simple `HTTP PUT` .

The following example uses the `curl` command and the admin user's default credentials to upload a `test.rpm` file to a hosted Yum repository with the name `test.rpm` :

```
curl -v --user 'admin:admin123' --upload-file ./test.rpm http://localhost:8081/repository/yum-hosted/test.rpm
```

Be default, Yum metadata is generated after 60 seconds when you upload an RPM.

While not typically necessary, you can also configure the *Repair -* *Rebuild Yum repository metadata (repodata)* task to create the metadata if the standard generation fails.

### Comps.xml (Package Grouping)

Nexus Repository supports Yum package groups when you upload a `comps.xml` file or a `comps.xml.gz` file. You must use the exact filename in order for Nexus Repository to detect the file and include it in the repomd.xml file.

```
curl -v --user 'admin:admin123' --upload-file ./b686d3a0f337323e656d9387b9a76ce6808b26255fc3a138b1a87d3b1cb95ed5-comps.xml http://localhost:8081/repository/yum-hosted/repodata/comps.xml
curl -v --user 'admin:admin123' --upload-file ./b686d3a0f337323e656d9387b9a76ce6808b26255fc3a138b1a87d3b1cb95ed5-comps.xml.gz http://localhost:8081/repository/yum-hosted/repodata/comps.xml.gz
```

### Installing Yum

Yum should come pre-installed with RedHat, CentOS, Fedora, and a long list of Linux flavors. If your system does not have Yum preinstalled, you may have larger problems that cannot be solved in these docs.

**Note:** Fedora users are encouraged to use `http://dnf.baseurl.org/` as of Fedora version 20. DNF is currently backwards compatible and should work with Nexus Repository 3, but it is not explicitly supported.

### Configuring Yum Client

Create a `nexus.repo` file in `/etc/yum.repos.d/` that looks similar to the following:

**nexus.repo**

```
[nexusrepo]
name=Nexus Repository
baseurl=http://<serveraddress:port>/repository/yum-proxy/$releasever/os/$basearch/
enabled=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
repo_gpgcheck=0
priority=1
```

### Browsing Yum Repositories and Searching Packages

You can browse Yum repositories in the user interface as described in the Browsing Repositories and Repository Groups section .

You can also search for Yum packages in the user interface. This search finds all packages that are currently stored in Nexus Repository as described in the Searching for Components section .

### GPG signatures for Yum

Nexus Repository uses GPG signatures to sign the metadata files that the Yum proxy and group repositories generate. These metadata files reside in the repository's `repodata` folder. The signing process occurs during metadata file generation, not when RPMs are downloaded or placed into the repository. A Yum client verifies the authenticity and integrity of the metadata files using the GPG key when it downloads content from the repository. This verification ensures that no modifications have occurred since the data was signed.

Nexus Repository does not sign the actual RPM packages themselves. The GPG signing feature in Nexus Repository signs the metadata of Yum repositories, not the individual RPM packages. You would typically sign individual RPM packages as part of your package build process before uploading them to Nexus Repository.

### Proxying RHEL Yum Repositories

Red Hat Enterprise Linux (RHEL) is subscription-based and communicates with remote Yum repositories over HTTPS. To set up a proxy in Nexus Repository for this scenario, Nexus Repository must trust the remote certificate and also authenticate when requesting packages from the remote server.

The following demonstrates how to configure Nexus Repository for SSL communication with RHEL remote Yum repositories.

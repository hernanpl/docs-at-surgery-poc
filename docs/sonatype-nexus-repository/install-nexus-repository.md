---
layout: default
title: "Install Nexus Repository"
parent: Sonatype Nexus Repository
nav_order: 4
---

# Install Nexus Repository

The Nexus Repository TM distribution archives combine the application and required resources in an archive file. When testing Nexus Repository TM on a local workstation, the files may be extracted and run in any environment that supports a Java runtime.

Many decisions must be considered before deploying Nexus Repository. New installations are configured to start with an **embedded H2 database** with components stored in the local file system. Using the start script from the command line is not resilient to server crashes. While this may be fine for testing, they are not ideal for production deployments.

Review the Planning Your Implementation documentation before proceeding.

## Unpack the Archive

The distribution archives are designed to be unpacked from the command line to avoid replacing or overwriting existing files in the directory. The command should create any missing files or directories.

Unpack the archive with the following command:

```
tar xvz --keep-directory-symlink -f
```

Here is a brief break down of the command.

- Extract ( `x` ) files from the specified archive.
- Display verbose ( `v` ) output, showing each file as it's extracted.
- Decompress ( `z` ) the archive using gzip before extraction.
- Operate on the specified file ( `f` ) (the archive).
- The `--keep-directory-symlink` option preserves existing directory symlinks while populating the directory they point to with the extracted files.

Do not run Nexus Repository from a user's home directory for production deployments; a common practice is to use the `/opt` directory.

See the [Directories](#directories) section below for a complete description of all files and folders in the archive.

## Running Nexus Repository TM

The archive in the Application directory includes a script to use to start the application. This script accepts the following commands:

```
start, stop, run, restart, force-reload, status
```

To start the Nexus Repository:

```
./nexus start
```

Logging is outputted to the application log file.

To stop the Nexus Repository running in the background:

```
./nexus stop
```

The application may run with logging displayed in the current shell for testing with the run command:

```
./nexus run
```

Starting with the `run` command leaves the application running in the current shell. The application can be stopped using `CTRL+C` in the console.

### Running as a Service

Nexus Repository needs to be configured to run as a service when installing the software for production usage. This is so that the service restarts properly after the server reboots.

See the [Run as a Service](#run-as-a-service) section below.

## Microsoft Windows Environments

The zip archive can be unpacked using the Windows [compression utility](https://support.microsoft.com/en-ca/help/14200/windows-compress-uncompress-zip-files) or a third-party utility such as [7zip](http://www.7-zip.org/download.html) . Nexus Repository is not installed in the `Program Files` directory.

You may install Nexus Repository in the `AppData\Local` directory of a specific user's home directory or use a folder in the system root. (e.g., `C:\nexus` ). Make sure the system user has full access to the application and directories.

Use the `bin\install-nexus-service.bat` to install Nexus Repository on your Windows server. When upgrading, uninstall previous versions before running this script. The Nexus Repository installer does not support using spaces in the path for the server or JVM.

Use the `nexus.exe` executable in the start service with the following commands:

```
Start the service: .\nexus.exe //ES//SonatypeNexusRepository
Stop the service: .\nexus.exe //SS//SonatypeNexusRepository
Uninstall the service: .\nexus.exe //DS//SonatypeNexusRepository
```

**Note:** Once Nexus Repository is installed as a service, making changes to the nexus.vmoptions are no longer picked up by the service. The service must be reinstalled to modify the configuration once set by the installer.

### Nexus.exe Commands Before Release 3.78.0

Release 3.78.0 includes many changes to the way Nexus Repository is built. The tooling to build the nexus.exe package requires an alternate configuration as listed above.

Use the following command for version before 3.78.0.

```
start, stop, run, restart, force-reload, status
```

## Access the User Interface

When Nexus Repository starts, access the web application user interface using a web browser navigating to the service URL:

```
http://<host_ip>:<port>
```

To test this on the server Nexus Repository is hosted, navigate to the localhost.

```
http://localhost:8081/
```

You may need to use the loopback address `127.0.0.1` depending on the DNS hostname assigned to the server.

Nexus Repository includes an administrative user with full access. The username is *admin* and the initial password is found in a temporary file named `admin.password` located in the `$data-dir` directory.

## Post Install Checklist

After installing Nexus Repository, complete the tasks below to ensure your Nexus Repository instance's security.

## Configure the Runtime Environments

The following offers detailed guidance on setting and optimizing Nexus Repository, including examples and best practices for various deployment scenarios.

- This provides detailed information on configuring the Java Virtual Machine (JVM) environment for Nexus Repository, including how to edit the configuration to adjust memory settings. See [Configuring the Runtime Environment](#configuring-the-runtime-environment)
- A comprehensive overview of memory configuration for Nexus Repository, including explanations of different memory types and example configurations for various deployment sizes. See the Nexus Repository Memory Overview documentation
- Specific recommendations for memory configurations based on the amount of RAM available on your system. See the [System Requirements](product-information.md#sonatype-nexus-repository-system-requirements)
- Nexus Repository is deployed in many configurations based on your use case. You have no limit on the number of instances you may deploy. We offer a number of reference architecture and deployment patterns to review when planning your deployment. See the Planning Your Implementation documentation

## Deployment Options

Nexus Repository can be deployed in various ways to suit your needs, including: as a standalone application, in a containerized environment (like Docker or Kubernetes), or in cloud-based solutions. Choose the option that best aligns with your infrastructure, scalability, and high availability requirements.

- Sonatype provides a Helm Chart to use for on-premises, AWS, and Azure resiliency and high availability deployment (HA) options. See the Resiliency and High Availability documentation
- Docker automates the deployment of applications inside virtualized Linux containers. You can create a container that supports the installation of Nexus Repository. See [Sonatype Docker Hub](https://hub.docker.com/r/sonatype/nexus3/)
- An OpenShift operator is available for Nexus Repository deployments. This deployment requires that Nexus Repository use an external PostgreSQL database. The operator also supports deploying in high availability (active/active) mode. See the [OpenShift Operator](#install-nexus-repository-on-openshift) section below

## Community Edition Onboarding

This topic covers getting started with Sonatype Nexus Repository TM Community Edition.

### What is Sonatype Nexus Repository TM Community Edition?

Sonatype Nexus Repository Community Edition is the perfect solution to help individual developers and small teams manage their components effectively—for free! As the next evolution of our legacy Sonatype Nexus Repository OSS, Community Edition empowers you with modern capabilities designed to meet the needs of today’s fast-moving development teams.

Community Edition provides an ideal platform to get small development teams started. Upgrade to Pro to gain even more advanced features like high availability, content replication, SAML, SSO, and all of our other Pro features.

### Getting Started with Sonatype Nexus Repository TM Community Edition

The sections below provide details on how to get started with Sonatype Nexus Repository Community Edition.

![Newcommunityeditionbanner__1_.png](/assets/images/uuid-75bf2cb9-b2bc-6631-bb45-92a7b5c6d654.png)

## Install Nexus Repository with a PostgreSQL Database

Nexus Repository TM defaults to using an embedded H2 database. For production deployments, we recommend using PostgreSQL databases. This topic covers installing Nexus Repository TM with an external PostgreSQL database.

See the [System Requirements](product-information.md#sonatype-nexus-repository-system-requirements) for PostgreSQL Database Requirements.

These instructions are to start Nexus Repository using an external PostgreSQL database.

### Create a PostgreSQL Database

Following are basic steps for setting up a PostgreSQL Database.

See the [PostgreSQL documentation](https://www.postgresql.org/docs/current/multibyte.html#id-1.6.11.5.6)

### Database Configuration

Nexus Repository supports 3 methods for providing the database configuration settings. When Nexus Repository initially starts, the first connection method encountered is used while the other methods are ignored. Mixing methods are not supported.

The settings are checked in the following order:

(1) Environment Variables, (2) JVM Arguments, (3) the Properties File

- Pass the connectivity details as environment variables:
- Specify the properties as JVM arguments:
- Create the `<data-dir>/etc/fabric/nexus-store.properties` directory and file with the following properties:

### Configuration Options for PostgreSQL

Set optional configuration settings through the same methods used above. Set multiple `advanced` properties in the JVM arguments by delimiting the values with " `\n` ".

```
advanced=maximumPoolSize\=200\nmaxLifetime\=840000
```

### PostgreSQL Database Maintenance

The following tasks help your PostgreSQL database maintain optimum performance. These should be done outside of normal working hours to reduce the impact on active users as the tasks can impact performance while running.

- PostgreSQL databases require periodic maintenance known as vacuuming. Vacuuming in PostgreSQL is a crucial maintenance process that helps to optimize database performance and reclaim disk space. You might need to adjust the auto-vacuuming parameters to obtain the best results for your situation. Review the PostgreSQL documentation on [vacuuming](https://www.postgresql.org/docs/current/routine-vacuuming.html) .
- In some situations, it is worthwhile to rebuild indexes periodically with the `REINDEX` command or a series of individual rebuilding steps. See the PostgreSQL documentation on [Reindexing](https://www.postgresql.org/docs/current/routine-reindex.html)
- It is a good idea to save the database server's log output somewhere, rather than just discarding them. The log output is invaluable when diagnosing problems. See [Log maintenance](https://www.postgresql.org/docs/current/logfile-maintenance.html)
- Continuous Archiving and Point-in-Time Recovery (PITR) are essential features in PostgreSQL that provide robust data protection and disaster recovery capabilities. They work together to ensure you can restore your database to any specific moment in time, even if a failure occurs. See [Backups/Archiving](https://www.postgresql.org/docs/current/continuous-archiving.html)

## Install Nexus Repository on OpenShift

**Note:** Only available in Sonatype Nexus Repository TM Pro. Interested in a free trial? [Start here](https://www.sonatype.com/products/repository-pro/trial) .

### Prerequisites

You must meet the following prerequisites to install Nexus Repository TM using the OpenShift operator:

- Running the OpenShift platform with access to RedHat repositories and Administrator privileges
- A separate OpenShift project for Nexus Repository
- A PostgreSQL database accessible to the OpenShift cluster
- A Base64-encoded Sonatype Nexus Repository license file; see the following example, which uses an example file named nx-license.lic
- Meet the System Requirements for High Availability Deployments in the Nexus Repository documentation.

### Migrating from the OrientDB Operator

The OrientDB operator was sunsetted on December 15, 2023. The new operator is called "Nexus Repository HA Certified Operator."

There is no direct migration path from the old operator to the new operator as the old one used the embedded OrientDB database while the new one requires that you migrate to PostgreSQL. The new operator requires a Pro license.

To use the new operator, you need to uninstall the old operator, migrate to PostgreSQL, obtain a Pro license, and install the new operator as outlined in the installation instructions below.

See the Migrating to a New Database documentation

### Installation Steps

### Upgrading an OpenShift Operator

Upgrading an OpenShift Operator can be done through the OpenShift console or the command-line interface (CLI). Here's a general guide, but always refer to the specific Operator's documentation for any unique instructions:

### Important Notes

- Operator Documentation: Consult the specific Operator's documentation for the most accurate and up-to-date upgrade instructions.
- Backup: It's a good practice to back up your cluster or relevant resources before upgrading an Operator, especially in production environments.
- Dependencies: Be aware of any dependencies the Operator might have. Upgrading could affect other components in your cluster. Rollback: Have a rollback plan in case issues arise during the upgrade.
- Testing: If possible, test the Operator upgrade in a non-production environment first to identify any potential problems.

## Run as a Service

When installing Nexus Repository TM for production usage it has to be configured to run as a service, so it restarts after the server reboots. It is good practice to run that service or daemon as a specific user that has only the required access rights.

Installation from the distribution archive does not include the configuration of a service. The following sections provide instructions for configuring the service manually. Independent of the operating system the steps are:

- Create an operating system user with limited access rights dedicated to running the repository manager as a service
- Ensure a suitable Java runtime environment is installed
- Configure the service and ensure it starts as part of the operating system boot process

### Linux

Configure Nexus Repository to run as a service with `init.d` or `systemd` . Both are startup frameworks used in Linux-based systems such as Ubuntu and CentOS. They are, essentially, init scripts that load commands to manage the service daemon. Before running the service configure an absolute path for your server files. Then create a `nexus` user with sufficient access rights to run the service.

In `bin/nexus.rc` assign the user between the quotes in the line below:

```
run_as_user="nexus"
```

Symlink the `$installdir` to `/opt/sonatype/nexus` :

```
ln -s /opt/sonatype/nexus-3.78-1-01 /opt/sonatype/nexus
```

Adjust the location (shown above as "/opt/nexus-3.78-1-01'") as needed for your installation location. Ensure the user running Nexus Repository has appropriate permissions on this path.

### Windows

The startup script that runs Nexus Repository on Windows platforms is `bin\nexus.exe` . The script includes standard commands for starting and stopping the service.

Use the `install-nexus-service.bat` located in the `bin` directory to install and update Nexus Repository on your Windows server. When upgrading from a version prior to Nexus Repository 3.79.1, uninstall the previous version before running this script.

```
cd C:\path\to\bin
install-nexus-service.bat
```

To customize the data directory path, include the path when running the install command:

```
install-nexus-service.bat C:\my-sonatype-work
```

To delete the service, run the following command:

```
sc delete SonatypeNexusRepository
```

**Note:** Once Nexus Repository is installed as a service, making changes to the nexus.vmoptions are no longer picked up by the service. The service must be reinstalled to modify the configuration once set by the installer.

### Mac OS

The standard way to run a service on Mac OS is to use `launchd` , a program that starts, stops, and manages daemons and scripts in Apple OS X environments. To run the service you need to create an XML document called with the file extension `.plist` to define its properties.

An example plist file for the repository manager installed in `/opt` is shown here:

```
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
    "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.sonatype.nexus</string>
    <key>ProgramArguments</key>
    <array>
        <string>/opt/nexus/bin/nexus</string>
        <string>start</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>
```

After saving the file as `com.sonatype.nexus.plist` in `/Library/LaunchDaemons/` you have to change the ownership and access rights:

```
sudo chown root:wheel /Library/LaunchDaemons/com.sonatype.nexus.plist
sudo chmod 644 /Library/LaunchDaemons/com.sonatype.nexus.plist
```

Consider setting up a different user to run Nexus Repository and adapt permissions and the `RUN_AS_USER` setting in the `nexus` startup script. With this setup, the Nexus Repository starts as a service at boot time.

To manually start it after the configuration you can use:

```
sudo launchctl load /Library/LaunchDaemons/com.sonatype.nexus.plist
```

## Configuring the Runtime Environment

This section details configuring the Nexus Repository TM runtime with recipes for specific tasks. Configuration is separated into the following categories: the Java Virtual Machine and the Nexus Application environments.

See the [Directories](#directories) section below on the `$install-dir` and `$data-dir` in Nexus Repository.

### Java Virtual Machine Environment

The startup of the Nexus Repository Java Virtual Machine (JVM) is managed within the installation directory. The application startup loads JVM arguments from the Java properties file.

```
$install-dir/bin/nexus.vmoptions
```

To edit Java options:

### Nexus Application Environment

The main location for the application configuration files is the `$install-dir/etc` directory. This directory includes one properties file and several nested directories:

- Configuration files for Ehcache, Elasticsearch, and OrientDB
- Configuration files for Apache Karaf, including: The main configuration for the Apache Karaf runtime. This file should not be modified. Customizable configuration used by Apache Karaf. This file can be used to pass additional parameters to the Apache Karaf container. Various Karaf and OSGi-related configuration files System properties used for the JVM and application start-up
- The main configuration for the Apache Karaf runtime. This file should not be modified.
- Customizable configuration used by Apache Karaf. This file can be used to pass additional parameters to the Apache Karaf container.
- Various Karaf and OSGi-related configuration files
- System properties used for the JVM and application start-up
- Eclipse Jetty is used as the webserver for the Nexus Repository application. We manage configuration files for Eclipse Jetty in this directory. Eclipse Jetty has a default of 400 threads in its pool size. Our support article [Understanding Eclipse Jetty 9.4.8 Thread Allocation](https://support.sonatype.com/hc/en-us/articles/360000744687) provides details on how allocation works and why at a certain amount of repositories with connectors the pool can maxed out. The `IllegalStateExceptions` warning may be seen indicating that there are insufficient configured threads.
- Logger definition for the log file name, logging levels, pattern layout, and rotation rules. The configuration files for logback including: See the Logging documentation for information on adjusting the logging configuration. For the `nexus.log` and `tasks.log` files For the `request.log` file
- For the `nexus.log` and `tasks.log` files
- For the `request.log` file
- A directory to put keystores when configuring HTTPS See the Configuring SSL documentation for details.

## Directories

The binary archive for Nexus Repository TM contains the following two directories.

### Installation Directory

`$install-dir` - This directory contains the Nexus Repository TM application, the Java libraries, and configuration files. Throughout the documentation, this is referred to as the **install-dir** .

This directory is replaced when upgrading Nexus Repository. New versions of Nexus Repository commonly include modifications to the basic configuration as features are added and removed. Configuration stored in these files must be copied to the new installation directory during the upgrade.

**Note:** Modifying Configuration We recommend storing configuration changes to the override files found in the data directory.

- These are files that contain legal details about the license and copyright notices
- This directory contains the startup script itself as well as startup-related configuration files.
- This directory contains a placeholder.
- This directory contains configuration files.
- This directory contains all components and plugins that constitute the application.
- The embedded JVM used by Nexus Repository.

### Data Directory

`$data-dir` - This directory contains everything stored and managed by Nexus Repository. This directory persists between upgrades with files being created during the operation of Nexus Repository.

The default location of the data directory is `sonatype-work/nexus3` relative to the installation directory.

Files and directories under the data directory include:

- The default directory for file system-based blob stores when defined with a relative path. The default blob store is at the following path. We recommend configuring blob stores outside of the sonatype work direction for resilient and highly available (HA) deployments. This is required for shared artifact storage and eases backup and recovery. See the Storage Guide documentation
- This directory contains information on currently cached Karaf bundles
- This directory contains the H2 database which is the primary storage for your metadata. This directory is not used when using an external PostgreSQL.
- This directory contains the currently configured state of Elasticsearch
- This directory contains the main runtime configuration and customization. See [Configuring the Runtime Environment](#configuring-the-runtime-environment) .
- This directory contains cached reports from the Repository Health Check feature
- This contains the automatically generated key used to identify your repository manager
- This directory and sub-directories contain active and archived application log files. See the Logging documentation for details on the log files.
- This directory is used for temporary storage.

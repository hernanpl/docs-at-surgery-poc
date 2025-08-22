---
layout: default
title: "Install self-hosted IQ Server"
parent: Sonatype IQ Server
nav_order: 7
---

# Install self-hosted IQ Server

In this section, you'll find documentation on how to install self-hosted instances of Sonatype IQ Server.

Users of [Lifecycle Cloud](#UUID-b0a97859-9429-e208-3395-c56d116b98d2_UUID-f860b58c-db10-352e-a6ed-e9afc38815ed) may refer to for details of which documentation applies to their deployment.

## IQ Server installation checklist

- Review the and the options.
- For High-Availability architecture diagrams see .
- Setting up the database - see [External Database Configuration](#UUID-cdf9f195-f35c-22ac-c1e0-882a0c5a6191)
- Production servers need to be configured as a service. See
- The first time you log in you are required to install the
- Document your steps and configuration settings for upgrades and backups

## Default credentials

The default server credentials are the user `admin` with the password `admin123`

The `Change Administrator Password` notice will remain in the UI until the default password has been modified.

## Installation

The steps throughout the documentation refer to storing the server installation files in the server's `/opt` directory. You may use a different directory, however, we recommend documenting any changes in your internal notes.

To Install the server:

See for details on the installation folder contents

## Initialization

Use one of the following commands (depending on your Java version) to start the IQ Server. This starts the server using the configuration from the . The output is logged to the console and errors will be recorded in the `stderr.log` file.

Use the following command if your deployment uses Java 17. This includes all deployments on versions 180+.

```
cd /opt/nexus-iq-server
java \
  --add-opens=java.base/java.lang=ALL-UNNAMED \
  --add-opens=java.base/java.util=ALL-UNNAMED \
  --add-opens=java.base/java.security=ALL-UNNAMED \
  --add-opens=java.base/sun.security.rsa=ALL-UNNAMED \
  --add-opens=java.base/sun.security.x509=ALL-UNNAMED \
  --add-opens=java.base/sun.security.util=ALL-UNNAMED \
  --add-opens=java.xml/com.sun.org.apache.xerces.internal.jaxp.datatype=ALL-UNNAMED \
  -jar nexus-iq-server-*.jar server config.yml 2> stderr.log

```

Use the following command for versions using Java 8/11 (possible for versions up to and including 179):

```
cd /opt/nexus-iq-server
java -jar nexus-iq-server-*.jar server config.yml 2> stderr.log
```

Linux requires a `User` to start the server. See for details and examples.

A successful start will result in a console message similar to the following:

```
... [main] org.eclipse.jetty.server.AbstractConnector - Started InstrumentedBlockingChannelConnector@0.0.0.0:8070
... [main] org.eclipse.jetty.server.AbstractConnector - Started SocketConnector@0.0.0.0:8071
```

The start command may be modified by adding Java configuration parameters.

```
JAVA_OPTIONS="-Djava.util.prefs.userRoot=./sonatype-work/javaprefs -Djava.io.tmpdir=/path/to/tmpdir"
java $JAVA_OPTIONS -jar nexus-iq-server-*.jar server ./iq-server/config.yml 2> stderr.log
```

## Automatic Shutdown on Errors

In rare circumstances, unrecoverable errors may occur that lead the system to shut down to preserve a valid system state and avoid data corruption resulting from continuing in an undefined state. When the IQ server encounters a fatal `java.lang.Error` you will see these errors in the `clm-server.log` and `stderr.log` files listed as the following:

```
Exiting on fatal error, see https://help.sonatype.com/display/NXIQ/Automatic+Shutdown+on+Errors for details.
```

We recommend configuring the [IQ server to run as a service](#UUID-4c35a5b5-92a7-1b4e-9036-c3c63acdbe27) so the service will restart automatically; avoiding a prolonged outage.

To bypass the IQ Server automatically shutting down on a fatal error, include the following property in the config.yml:

```
exitOnFatalError: false
```

⚠️ **Warning:** Administrators should not change this property unless advised by the Sonatype support team.

## IQ Server Directory and Files

The IQ Server file architecture uses and stores files in a few directories:

- **Installation directory** - stores the primary server app, the CLI scanner, and the configuration file.
- **Sonatype-work directory** - stores the data files including; the internal database, logs (configurable), reports, scans, and the search index.
- **Temporary directories** - The server uses Java temporary directories to save details of your instance. The Java temporary directory is used to store transient server files for downloading and copying while the user prefs stores the [license file](#UUID-557c4cad-5818-108e-07ec-666d01cc4d7a) .

**Note:** The system user account that the server runs under must have sufficient access rights to both the work and temporary directory for the server to function properly.

### Installation directory

Extracting the archive file has the following files.

### Sonatype-work directory

IQ Server creates a directory to store its data and configuration during the initial startup on the path relative to the location of the invoking java command. The directory is configured in config YAML.

```
sonatypeWork: ./sonatype-work/iq-server
```

On startup, the server will check this path for the instance of IQ Server. The server will create the directory and initial files when they do not already exist. Set the property to a different location to separate the installation and data directories.

Deleting or moving the sonatype-work directory is an accepted way to 'start over' with your deployment.

### System temporary directory

IQ Server uses the system temporary directory during its operation. This folder varies by operating system. If a specific directory needs to be used, the IQ Server can be started with a command line flag as such:

```
-Djava.io.tmpdir=/path/to/tmpdir
```

## Product License

This section covers how to install the product license in the IQ Server.

- The Sonatype account team provides the license as a `.lic` file in an email sent to the primary stakeholders.
- The IQ Server saves the license details to the database table `product_license` once a license file is uploaded.

For details on features and functionality provided by the Sonatype license, see . See the following KB article to learn about the [user-base license model](https://support.sonatype.com/hc/en-us/articles/213464168-Sonatype-s-User-based-License-Model-FAQ) .

**Note:** Sonatype licenses covering multiple license models (based on the number of applications, users, or SBOMs) require IQ version 178+. Previous versions of IQ Server need to be upgraded before installing the new license.

### Automatic license installation

During the initial setup, the server may be configured to install a license file automatically. This property is not used for existing installations. An error will occur if the license file cannot be accessed.

Add the following property to the config.yml and update the path to your license file. A relative or absolute path may be used.

```
licenseFile: ./license.lic
```

### Install using the REST API

While the server is running, a license may be installed or removed using the API.

See for details.

### Log in for the first time

The first time you log into the server, you must install a valid product license.

The default server credentials are the user `admin` with the password `admin123`

### Updating the license

When you renew a Lifecycle or Firewall license with Sonatype, you'll be sent a new .lic file. To update the license, follow the steps below.

The browser UI should immediately update to show the details of the new license file.

## Run IQ Server as a Service

The server can be run as a service or daemon. This is recommended to ensure the server will restart when the operating system reboots. The following instructions are for Linux environments.

See the KB to [run as a service on a Windows Server](https://support.sonatype.com/hc/en-us/articles/213463798-Running-the-Sonatype-IQ-Server-as-a-Service-on-Windows)

- Set the user: `iqserver` on the server with limited access
- Add the service script to `/etc/init.d/sonatype-iq-server`
- Set the `systemV` or `systemd` depending on your configuration

### Set directory permissions

Create a dedicated user with limited access for the service.

The user needs full access rights to the server installation directory and the `sonatype-work` directory listed in the `config YAML` .

The following command grants service user permissions.

```
chown -Rv {username} /opt/sonatype-iq-server
```

### Service script

Setting the service script will vary between operating systems and distributions depending on the init system used. The script would be copied to a dedicated startup directory and assigned run-levels and other characteristics for the start-up.

Save the following script as `sonatype-iq-server` in the `/etc/init.d/` directory.

```
/etc/init.d/sonatype-iq-server
```

```
#!/bin/sh

# The following comment lines are used by the init setup script like the
# chkconfig command for RedHat-based distributions. Change as
# appropriate for your installation.

### BEGIN INIT INFO
# Provides:          sonatype-iq-server
# Required-Start:    $local_fs $remote_fs $network $time $named
# Required-Stop:     $local_fs $remote_fs $network $time $named
# Default-Start:     3 5
# Default-Stop:      0 1 2 6
# Short-Description: sonatype-iq-server service
# Description:       Start the sonatype-iq-server service
### END INIT INFO

IQ_SERVER_HOME="/opt/sonatype-iq-server"
VERSION="[0-9.]*-??"
JAVA_OPTIONS="-Xmx4096m -XX:+UseG1GC"

# The user requires privileges to write into the sonatype-work directory.
RUN_AS_USER="iqserver"

do_start()
{
    _cmd &
    echo "Started sonatype-iq-server"
}

do_console()
{
    _cmd
}

do_stop()
{
    pid=`ps aux | grep nexus-iq-server | grep '.jar server' | grep -vE '(stop|grep)' | awk '{print $2}'`
    kill $pid
    echo "Stopping sonatype-iq-server - PID $pid ($?)"
}

do_usage()
{
    echo "Usage: sonatype-iq-server [console|start|stop]"
}

_cmd()
{
    cd $IQ_SERVER_HOME || return $?
    chown $RUN_AS_USER ./stderr.log
    if [ "$RUN_AS_USER" = "$USER" ]; then
        java $JAVA_OPTIONS -jar nexus-iq-server-$VERSION.jar server config.yml 2> stderr.log
    else
        sudo -u $RUN_AS_USER java $JAVA_OPTIONS -jar nexus-iq-server-$VERSION.jar server config.yml 2> stderr.log
    fi 
}

case $1 in
    console)
        do_console
        ;;
    start)
        do_start
        ;;
    stop)
        do_stop
        ;;
    *)
        do_usage
        ;;
esac
```

### SystemV

The following commands show an example of a Debian-based system. Depending on the requirements of your system administrator, modify the scripts to fit into your environment and the exact deployment scenario.

```
sudo su
cd /etc/init.d
update-rc.d sonatype-iq-server defaults
service sonatype-iq-server start
```

### SystemD

This example is a script that uses systemd to run the server.

- Make sure the `iqserver` user exists
- Create the sonatype-iq-server script in `/etc/init.d`
- Create a file called `sonatypeiq.service` in the `/etc/systemd/system/` directory
- Add the following script and save the file

```
[Unit]
Description=Sonatype IQ Service
After=network-online.target

[Service]
Type=forking
ExecStart=/etc/init.d/sonatype-iq-server start
ExecStop=/etc/init.d/sonatype-iq-server stop
User=iqserver
Restart=on-abort
TimeoutSec=600

[Install]
WantedBy=multi-user.target
```

Activate the service with the following commands

```
chmod a+x /etc/init.d/sonatype-iq-server
sudo systemctl daemon-reload
sudo systemctl enable sonatypeiq.service
sudo systemctl start sonatypeiq.service
```

### Native Linux installers from the community

Community-provided native installers for Linux are available to set up the server to run as a service, however, they are not officially supported.

See [github.com/sonatype-nexus-community/nexus-iq-server-installer](https://github.com/sonatype-nexus-community/nexus-iq-server-installer)

### Running as a Windows Service

## Switching from the IQ Server Standalone JAR to the Bundled JDK Assembly

This topic provides detailed instructions for those currently using a Sonatype IQ Server distribution that does **not** include a bundled JDK and who wish to migrate to the new distribution that includes a bundled JDK.

The steps below assume your IQ Server installation is currently running as a systemd service.

### Step 1: Download and Extract the New Distribution

### Step 2: Update the Systemd Service File

### Step 3: Stop IQ Server

### Step 4: Start IQ Server

Start Sonatype IQ Server using the new bundled JDK distribution. If you encounter authentication errors, adjust the service file permissions or configuration as needed.

## IQ Server High Availability Installation

Sonatype IQ Server High Availability (HA) enables you to recover from failures or disruptions to the underlying host infrastructure with minimal downtime.

- IQ Server High Availability is tested and verified with the named technologies and platforms mentioned in this section. Equivalent technologies and platforms may work as well. Serverless architecture such as AWS Fargate is not supported.
- Deploy and test in a staging environment before deploying to production.

### General Requirements for HA Installation

The following deployment models have additional specific requirements.

- [IQ Server HA on Amazon Web Services (AWS)](#UUID-d8264753-0000-96c7-2ba6-ca3ebaa609c4)
- [IQ Server HA On-Premises](#UUID-a7c26b5c-ed10-40d4-e954-0b5010ded4fd)

### Installation on AWS

### Installation On-Premises

### Logging for HA

Running the [IQ Server HA helm chart](https://github.com/sonatype/nexus-iq-server-ha/tree/main/chart) will configure your High Availability (HA) installation to generate aggregated log files using [Fluentd](https://www.fluentd.org/) . These files are combined from each pod running IQ Server.

The aggregated log files are in [ndjson format](http://ndjson.org/) and located in the shared file system in the /log directory. You can use the aggregated log files for a support request. By default, they will be included while generating a support zip inside a top-level cluster_log directory.

![137208909.png](/assets/images/uuid-b119ff2d-1242-e071-b699-b36d0a8172b5.png)

Refer to the [IQ Server Helm Chart](https://github.com/sonatype/nexus-iq-server-ha/tree/main/chart) (under the section "Logging") for detailed instructions on customizing the log retention periods and other fluentd deaemonset aggregator settings.

Each pod running IQ Server is pre-configured to generate:

- Application log
- Request log
- Audit log
- Policy violation log
- Stderr log

Refer to [Configuring Logging](#UUID-3e88a34a-c077-2047-4f8d-e1d838e2066e) for more details.

### Migrating to HA Setup

Installations running on a single instance may be migrated to an HA deployment to take advantage of the benefits offered by high availability. This section covers the steps needed for migration.

We have tested and verified the functionality and performance of the IQ Server using the named third-party tools, technologies, and platforms mentioned in this section. Using other technologies and platforms may not result in the same outcomes, and are not supported.

### Performance Benchmarks for High Availability

Sonatype IQ Server High Availability (HA) installations may vary based on the organization's needs. This section provides performance metrics for IQ Server HA to guide scaling decisions based on your performance requirements, runtimes, and cost.

We have thoroughly tested and verified the functionality and performance of the IQ Server with the named third-party tools, technologies, and platforms mentioned in this section. Using other technologies and platforms may not result in the same outcomes and are not supported.

## Upgrade the IQ Server

Upgrading the IQ Server is replacing the server jar with the latest version and restarting the service. On startup, the server detects that it has been upgraded from the files in the `sonatype-work directory` and performs any changes. This often includes updates to the database and files on disk.

**Note:** Some upgrades will take longer before the server is available due to modifications made to the database. Allow for enough time for the process to complete before interrupting the service. Disable any process that may interrupt the server while the upgrade is happening to avoid corruption. In a Kubernetes environment, a liveness probe may attempt to restart the server container during the upgrade.

We strongly recommend taking a backup of your server installation and sonatype-work directories before attempting to upgrade. Rarely does an issue happen during sequential updates, however, updates spanning multiple versions may run into unforeseen issues.

Follow the instructions to

### Upgrade Instructions

Download the latest version from

Review the [release-specific upgrade instructions](#UUID-f105bc66-d70f-7a04-17b2-37846a8cdbe5) for your current version and any versions that follow.

### Upgrading a High Availability (HA) Installation of IQ Server

Refer to the following links for details on upgrading an HA installation:

[https://github.com/sonatype/nexus-iq-server-ha/tree/main/chart#upgrading](https://github.com/sonatype/nexus-iq-server-ha/tree/main/chart#upgrading)

[https://artifacthub.io/packages/helm/sonatype/nexus-iq-server-ha#upgrading](https://artifacthub.io/packages/helm/sonatype/nexus-iq-server-ha#upgrading)

## Backup the IQ Server

Sonatype recommends that you fully document your backup process and follow a data recovery plan aligned with your company’s policies. We also recommend that you take a backup before doing an upgrade of the IQ Server. Regular backups are an important disaster recovery safeguard.

In the ideal scenario, your IQ Server configuration and database are backed up automatically and at regular intervals.

### Minimum Backup

Regardless of the deployment type, the minimum required files for a full, point-in-time backup include:

```
Database, report files, configuration, server binary
```

Optional files to include:

```
Log files, license file, custom trust stores, cloned SCM repositories
```

When deciding the scope of the backup, refer to your organization's data storage policy, and remember that files used by IQ Server may have sensitive information so we recommend keeping these secure.

### Backup Best Practices

Sonatype recommends a backup at least once a day of the database and new reports. The length of the complete backup depends on the database's size and the number of retained reports. In all cases, plan for a maintenance window scheduled during non-peak hours when possible.

- The reports directory may become significantly large depending on your retention policies resulting in long-running backups. Consider performing a `diff` of the `sonatype-work` directory to only copy the changes to reports from the last backup.
- Continuous Monitoring is configured to run at midnight and may interfere with a scheduled backup task. Consider running the backup before continuous monitoring starts as it may take a while.
- Regularly validate your backup of IQ Server in a test environment to ensure the content has not been corrupted.

### Containerized Deployments

Containerized deployments require persistent volumes. The persistent volume contains everything the service needs to run. Apply your backup strategy to your persistent volumes to ensure a complete backup.

Your organization may have a team responsible for maintaining your containerized apps. Bring them into your conversation early to ensure a repeatable backup procedure is in place.

### Enterprise deployments with an external Postgres database

When using the PostgreSQL database, a full backup may be completed without shutting down the server.

Your Postgres databases may be managed by a database administrator. Align with them on the timing of your backup procedures. Back up the `sonatype-work` and the Postgres database as close to the same time as possible or avoid data loss.

### Small deployments with the embedded H2 database

The embedded H2 is an in-memory database. Performing a backup while the IQ Server is running carries the risk of copying the database in an inconsistent state. Gracefully stop the IQ Server before backing up to ensure a reliable copy is taken.

## Restore the IQ Server

All deployments need to be able to restore the IQ Server in case of a disaster. In most scenarios, restoring the IQ Server is as simple as transferring the last known usable backup to your production environment and restarting the service.

- Contact Sonatype Support before beginning disaster recovery work by opening a ticket.
- Shut down the server before beginning the restore procedure.
- Restore the same version as taken from the backup. The name of the server application contains the version number.

### Notable Issues

A version mismatch between the server application .jar, the config.yml, and the database may cause issues. Back up the whole environment to avoid these issues.

Broken report links may occur when the `sonatype-work` directory and the database are not backed up at the same time. Re-scan the applications to resolve these issues.

Do not attempt to restore and upgrade the IQ Server at the same time. First, restore the IQ Server before attempting to upgrade.

### Containerized Deployments

Containerized deployments require persistent volumes that contain everything needed to run the IQ Server. To restore the IQ Server from a containerized deployment, use the last known good persistent volumes and move them into your production environment.

Collaborate with your container management team, if your organization has one. Start your restore procedure by bringing them into the conversation.

### Enterprise deployments with an external Postgres database

To restore the IQ Server:

To restore the Postgres database, [refer to the PostgreSQL documentation.](https://www.postgresql.org/docs/current/backup.html)

### Enterprise deployments with the embedded H2 database

To restore the IQ Server:

## Move the installation

The server's installation and sonatype-work directories are portable and may be copied to the new location. Use the following process to move the server to a new location.

A unique identifier was generated for the instance when the server was created. We do not recommend using this instance copy as a deployment strategy for horizontal scalability.

- Know the location of your license - the license details are encrypted within the local Java configuration. You will likely need to reinstall the license at the new location.
- The external database requires a low-latency network connection or the server's performance will severely degrade
- Ensure that the server meets the system requirements - this includes the Java version
- Preserve operating system file permissions - use the same system account to run the new instance
- Check the config.yml file for the locations of the sonatype-work directory and log files
- The installation and sonatype-work directories should be copied when the server is not running. When using the internal database, copying the data files while the server is running may leave them in an inconsistent state that is difficult to recover.

Once the `installation` and `sonatype-work` directories have been moved to the new location; start the server and follow the prompts to upload the license file.

### Move with rsync

Most of the server files are not continuously accessed while the server is running. A backup tool may reduce downtime by performing an initial copy while the service is still available for use. Later, a second pass is made to copy the difference once the server has been shut down. The second run to include any changes will take much less time, limiting the overall downtime to your end users.

Using rsync, the following [command](https://download.samba.org/pub/rsync/rsync.1#opt-P) can be used.

```
rsync -avP <source> <dest>
```

Once this completes, shut down the server, and run the rsync copy with:

```
rsync -avP --del <source> <dest>
```

This second copy should run quite quickly since rsync will only be handling the delta of files between the first and second copy.

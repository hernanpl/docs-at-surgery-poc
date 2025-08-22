---
layout: default
title: "Configuring"
parent: Sonatype Lifecycle
nav_order: 4
---

# Configuring

This section reviews the IQ Server configuration.

## Config YAML

The IQ Server is a web application built on a [Dropwizard](http://www.dropwizard.io/) web server. The initial configuration is set using the YAML formatted config.yml and is located in the same folder that contains the primary server .jar file.

After the initial startup, the configuration is stored in the internal database and will need to be modified using the [Configuration REST API](#UUID-0fa6ca2c-1237-6aca-a4e6-ad4d074fd63f) or through the `System Preferences` in the user interface.

Some configuration options may only be changed from the config.yml such as system logging and any startup configuration.

See the [Configuration Settings](#UUID-8d4fb66c-e0f4-0f2f-15a8-3d4226c007dd_id_ConfigYAML-Configuration) below for details.

### Editing the config.yml file

We recommend using caution when editing the config.yml file to avoid corrupting the layout. The YAML format relies on indenting to denote nested properties. Modifying this indentation incorrectly may lead to improper configuration.

Keep the following points in consideration:

- TAB characters are not supported in YAML files. Use space characters only for indenting.
- The YAML (.yml) structure is tree-like. Space indents define the hierarchy.
- Indented lines are child options of the outdented line preceding them.
- The parser ignores comments beginning with the hash symbol (#).

### Configuration Settings

In recent versions of IQ Server, most configuration is stored in the internal database and should be updated using the API or System Preferences. Use the chart below to match which settings may still be set with the config.yml file.

### Troubleshooting the config.yml file

The IQ Server will not start when the config.yml file is not properly formatted.

To troubleshoot, open a terminal and navigate to the installation directory. Use the `demo.bat` or `./demo.sh` commands to start the server.

Below is an example error from a Windows operating system.

```
ERROR [2022-03-01 11:08:48,052] com.sonatype.insight.brain.service.InsightBrainService: Fatal error trying to start server
! org.yaml.snakeyaml.scanner.ScannerException: while scanning for the next token
! found character '\t(TAB)' that cannot start any token. (Do not use \t(TAB) for indentation)
!  in 'reader', line 21, column 1:
```

Use the following steps when unable to reformat the config.yml to correct the issue:

- Rename the config.yml file from your installation directory
- Re-download the IQ server archive if it is not still on the server. We recommend using the same version to avoid upgrade issues.
- Extract the archive and locate the config.yml file
- Move the config.yml file into your installation directory
- Enter changes from your previous config.yml to the new file

### Example config.yml file

The following reference is an example of the config.yml file as of release 183. We recommend using the original file from the archive to avoid indentation errors. The below text is to only be used for reference.

```
#
# NOTE: The indentation in this file is crucial for proper processing. Please keep the existing indentation when editing it.
#

# Directory for data files.
sonatypeWork: ./sonatype-work/clm-server

# Path to a license file to automatically install if unlicensed.
#licenseFile: ./license.lic

# HTTP Strict Transport Security (HSTS) is supported using dropwizard-web configuration
# HSTS headers are enabled by default, uncomment web: section below and set enabled: false to disable
# Refer to https://github.com/dropwizard/dropwizard-web#supports for detailed configuration guide
#web:
#  hsts:
#    enabled: true
#    maxAge: 365 days
#    includeSubDomains: true

# HTTP-specific options.
server:
  # The context path for the application. Note that this must have a leading slash.
  applicationContextPath: /

  applicationConnectors:

    - type: http

      # The port on which the HTTP server listens for service requests.
      # Because Java cannot drop privileges in a POSIX system, these
      # ports cannot be in the range 1-1024. A port value of 0 will
      # make the OS use an arbitrary unused port.
      port: 8070

      # The hostname of the interface to which the application HTTP server socket
      # will be bound. If omitted, the socket will listen on all
      # interfaces.
      #bindHost: 127.0.0.1  # only bind to loopback

  adminConnectors:

    - type: http

      # The port on which the HTTP server listens for administrative
      # requests. Subject to the same limitations as "port".
      port: 8071

      # The hostname of the interface to which the admin HTTP server socket
      # will be bound. If omitted, the socket will listen on all
      # interfaces.
      #bindHost: 127.0.0.1  # only bind to loopback

  # HTTP request log settings.
  requestLog:

    appenders:

        # Settings for logging to a file.
      - type: file

        # The file to which current statements will be logged.
        currentLogFilename: ./log/request.log

        logFormat: "%clientHost %l %user [%date] \"%requestURL\" %statusCode %bytesSent %elapsedTime \"%header{User-Agent}\""

        # When the log file rotates, the archived log will be renamed to this and gzipped. The
        # %d is replaced with the previous day (yyyy-MM-dd). Custom rolling windows can be created
        # by passing a SimpleDateFormat-compatible format as an argument: "%d{yyyy-MM-dd-hh}".
        archivedLogFilenamePattern: ./log/request-%d.log.gz

        # The number of archived files to keep.
        archivedFileCount: 50

# Logging settings.
logging:

  # The default level of all loggers. Can be OFF, ERROR, WARN, INFO, DEBUG, TRACE, or ALL.
  level: DEBUG

  # Logger-specific settings.
  loggers:
    "com.sonatype.insight.scan": INFO
    "eu.medsea.mimeutil.MimeUtil2": INFO
    "org.apache.http": INFO
    "org.apache.http.wire": ERROR
    "org.apache.shiro.web.filter.authc.BasicHttpAuthenticationFilter": INFO   # WARNING: This reveals credentials at DEBUG level
    "org.eclipse.birt.report.engine.layout.pdf.font.FontConfigReader": WARN
    "org.eclipse.jetty": INFO
    "org.postgresql.jdbc.PgConnection": INFO
    "org.quartz": INFO
    "org.zeroturnaround.exec": INFO
    "com.networknt.schema": OFF
    "org.eclipse.jgit": INFO
    "com.sonatype.insight.audit":
      appenders:
      - type: file
        # The file to which audit statements will be logged.
        currentLogFilename: ./log/audit.log
        # When the audit log file rotates, the archived audit log will be renamed to this and gzipped. The
        # %d is replaced with the previous day (yyyy-MM-dd). Custom rolling windows can be created
        # by passing a SimpleDateFormat-compatible format as an argument: "%d{yyyy-MM-dd-hh}".
        #
        # If archive is true, this must be specified.
        archivedLogFilenamePattern: ./log/audit-%d.log.gz
        # The number of archived audit log files to keep.
        archivedFileCount: 50
    #"com.sonatype.insight.policy.violation":
      #appenders:
        #- type: file
          # The file to which policy violations will be logged.
          #currentLogFilename: ./log/policy-violation.log
          # When the policy violation log file rotates, the archived policy violation log will be renamed to this
          # and gzipped. The %d is replaced with the previous day (yyyy-MM-dd). Custom rolling windows can be created
          # by passing a SimpleDateFormat-compatible format as an argument: "%d{yyyy-MM-dd-hh}".
          #
          # If archive is true, this must be specified.
          #archivedLogFilenamePattern: ./log/policy-violation-%d.log.gz
          # The number of archived policy violation log files to keep.
          #archivedFileCount: 50

  appenders:

      # Settings for logging to stdout.
    - type: console

      # Do not display log statements below this threshold to stdout.
      threshold: INFO

      logFormat: "%d{'yyyy-MM-dd HH:mm:ss,SSSZ'} %level [%thread] %X{username} %logger - %msg%n"

      # Settings for logging to a file.
    - type: file

      # Do not write log statements below this threshold to the file.
      threshold: ALL

      logFormat: "%d{'yyyy-MM-dd HH:mm:ss,SSSZ'} %level [%thread] %X{username} %logger - %msg%n"

      # The file to which current statements will be logged.
      currentLogFilename: ./log/clm-server.log

      # When the log file rotates, the archived log will be renamed to this and gzipped. The
      # %d is replaced with the previous day (yyyy-MM-dd). Custom rolling windows can be created
      # by passing a SimpleDateFormat-compatible format as an argument: "%d{yyyy-MM-dd-hh}".
      #
      # If archive is true, this must be specified.
      archivedLogFilenamePattern: ./log/clm-server-%d.log.gz

      # The number of archived files to keep.
      archivedFileCount: 50

# Sample data is created for new installs.
createSampleData: true

```

### Configuring with Java System Properties

Configuration properties may be set using Java system properties on the IQ server start-up script. The property overrides start with the prefix **dw.** - followed by a dot-separated path to the configuration value being overridden.

```
java -Ddw.baseUrl=http://iq.example.com -jar nexus-iq-server-*.jar server config.yml 2> stderr.log
```

### Configuring with Environment Variables

Values in the `config.yml` may be set using system environment variables. When an environment variable is not set and/or does not have a default value, the IQ Server will use the variable as a string literal.

Setting the IQ Server application port

```
server:
  applicationConnectors:
    - type: http
      port: ${IQ_PORT}
```

Set a default value to use when the environment variable is not set

```
server:
  applicationConnectors:
    - type: http
      port: ${IQ_PORT:-8070}
```

Nesting environment variables are also supported. In the following example, the ${IQ_HOST} resolves to PROD and ${IQ_PORT_PROD} resolves to 8070.

```
Q_HOST=PROD
IQ_PORT_PROD=8070
```

```
server:
  applicationConnectors:
    - type: http
      port: ${IQ_PORT_${IQ_HOST}}
```

## Configuring Base URL

When the IQ server is installed inside an organization's network it does not know the domain external users need to access it. The Base URL is used to construct links for any notifications outside of the user interface.

For example, when the IQ Server sends an email for a policy violation, it uses the Base URL to construct a link that leads to the Application Report. We highly recommend setting the Base URL before any setting up external notifications.

**Note:** When setting the application context path (the directory after the domain) to a custom value, append the custom application context path to the Base URL.

- Log in as the System Administrator
- Select Base URL from the System Preferences menu
- Enter the Base URL and select Save Configuration

### Legacy configuration in config.yml

Before release 137, setting the Base URL is made using the config.yml. This method is no longer supported as of release 138.

```
baseUrl: http://iq-server.example.com/
```

## Configuring Outbound Traffic

### Network Access to Sonatype Data Services

The Sonatype IQ Server requires internet connectivity to perform license validation and vulnerability scans. It needs to communicate securely with the Sonatype Data Services using HTTPS.

Network firewall and HTTP proxy server administrators must ensure the following URL is accessible to IQ Server:

``

The IQ Server sends notification emails containing links to static resources loaded from:

``

Email clients should also have access to the **** subdomain.

**Note:** Disconnected Sonatype Solutions Sonatype offers a solution for environments without internet access. The Sonatype Air-Gapped Environment (SAGE) product allows usage of the IQ Server in a disconnected (no internet) environment. This is a separate license purchase. If you're interested in this, you can contact Sonatype directly at sales@sonatype.com

### HTTP Proxy Server

Many organizations manage HTTP network traffic via an [HTTP proxy server](https://en.wikipedia.org/wiki/Proxy_server) . To allow the IQ Server to reach Sonatype Data Services, you may have to configure the IQ Server to use a specific HTTP Proxy Server for outbound requests. The proxy server must support the CONNECT method of tunneling.

### Appending a User-Agent To Outbound Requests

You may customize the user-agent header used for HTTP requests when needed by some network firewall configurations.

Control characters are not permitted in the user agent and the max length of the text is 128 characters.

Configure the user agent string as follows:

## Configuring Inbound Traffic

### HTTP Configuration

The port parameter(s) in the IQ Server `config.yml` allows you to set the port(s) to access the application and/or operational menu. Each port can be freely changed to other values, as long as it is not used and in the allowed range of values greater than 1024. The following examples show how to set these port parameter(s).

### HTTPS/SSL Configuration

One option to expose the IQ Server via HTTPS is to use an external server like Apache HTTPD or nginx and configure it for reverse proxying the external connections via HTTPS to the internal HTTP connection. This reverse proxy can be installed on the same server as the IQ Server or a different server and numerous tutorials for this setup are available on the internet.

A second option is to directly configure SSL support for Dropwizard by modifying the relevant segment in the `config.yml` file. The following examples show how to do this. Note that the keystore file can be generated and managed with [the keytool](https://docs.oracle.com/javase/7/docs/technotes/tools/windows/keytool.html) .

### Web Application Context Path

For IQ Server 1.43 and newer the context path at which the web application is accessible can be customized using the option shown below:

```
server:
    # The context path for the application. Note that this must have a leading slash.
    applicationContextPath: /
```

While the application context path does control the base path the IQ server web application is served at, the value is not appended to whatever baseUrl config value you may already have set. When customizing the applicationContextPath, be sure to check if the Base URL value also needs adjustment.

### CSRF Protection

Attacks on the IQ Server could occur via a cross-site request forgery (CSRF). To protect against this, a configuration item CSRF protection has been provided. This option is set to true by default and is updated through the [Configuration REST API](#UUID-0fa6ca2c-1237-6aca-a4e6-ad4d074fd63f) .

## Reverse Proxy Authentication

Single sign-on (SSO) authenticates users through an external identity provider. Reverse Proxy Authentication is implementing a reverse proxy server that supplies the user details via an HTTPS header field while setting the IQ Server to accept those headers for authentication.

This authentication method applies to both IQ Server and LDAP users. Incoming usernames are matched first to IQ Server users, then to LDAP users, and then the configuration in the IQ Server determines the access level granted to the user.

**Note:** Required Methods For IQ Server to function properly, the following HTTP methods must be enabled through the reverse proxy: `GET` , `POST` , `PUT` , and `DELETE` .

This is configured via .

### Legacy configuration prior to release 137

The valid reverse proxy authentication configuration needs to be set in the config.yml file.

```
# Configures reverse proxy authentication for the web UI.
reverseProxyAuthentication:
    # Set to true to activate authentication
    enabled: true
    # Name of the HTTP request header field that carries the username
    usernameHeader: "REMOTE_USER"
    # Set to true for backward compatibility with old client plugins
    csrfProtectionDisabled: false
    # The service URL that will be redirected to when a user requests logout.
    logoutUrl: http://localhost/logout/index.html
```

## Public Key Infrastructure (PKI) Authentication

Integrations may use PKI authentication to delegate authentication to the Java Virtual Machine (JVM). When delegated, the tool or plugin does not handle authentication and instead, the JVM supplies PKI information to the reverse proxy for authentication.

To implement PKI authentication, a reverse proxy server is needed to translate PKI-supplied credentials to users known by IQ Server. You can configure the [reverse proxy server for PKI authentication](#UUID-bb200ae2-ea97-c4c3-f748-5d8fe38ffa38) using the [Reverse Proxy Authentication Configuration REST API.](#UUID-495a2a67-ebae-72a6-f608-b8dcdb2e4c74)

For information on setting PKI authentication, review that integration's documentation.

## Data Retention

Lifecycle scan data persists as archive files stored in the working directory. These files accumulate over time and may rapidly consume available disk space if not cleaned up at regular intervals.

Data retention rules move these files automatically to a trash directory and are enabled by default for new installations. This trash directory needs to be periodically purged as part of system maintenance to reduce utilized storage space.

![137204519.png](/docs-at-surgery-poc/assets/images/uuid-f5c81ad0-d695-a325-c8fe-5c654b808afb.png)

### Data retention configuration and inheritance

The data retention configuration is found on the `Orgs and Policies` page using the top-level navigation or by scrolling to the section below the list of policies. Retention configuration is inherited from the root organization or configured at each organization independently.

- Organizations may be configured to inherit rules from the Root Organization
- Applications inherit rules from their Organization
- The most recent scan data is always retained

### Trash Directory

The data retention action does not delete file data rather it is compressed and placed in the `/trash` folder inside the working directory. This compression will recover some disk space even when the data is not deleted.

- The `/trash` directory folders are named after the date compressed; in `YYYY-MM-DD/XX` format.
- Purged reports are named in the format `app-{internalApplicationId}-report-{reportId}.zip`
- To avoid conflicts do not delete contents from a folder matching the current date
- Restore reports by unzipping them into the `report` folder in the working directory.
- Purging occurs once a day at midnight, local server time

### Manage data retention configuration

Steps to edit the data retention configuration.

- Select the Root Organization or an Organization
- Navigate to the section labeled `Data Retention` and select `Edit`
- Data retention is set by the Lifecycle stage; choose between not purging for this stage or custom
- Choose a retention period or a set number of reports to retain. Reports are purged when either rule is satisfied

![Screenshot_2024-03-14_at_4_57_03_PM.png]({{ /assets/images/uuid-0b2566b0-3299-4267-003e-4e08e7ab9c1a.png)

### Cleaning up Success Metrics data

Success Metrics are generated when reviewing historical policy violation data. Violation data is retained after violations have been resolved and are no longer against components in the application. Set the retention value to at least as long as required to report these metrics.

Purging success metric data is limited to violations that have been resolved. Unresolved violations are not purged regardless of how many years ago those violations were first discovered. Violations that have been waived or labeled as legacy violations are considered unresolved.

### Manually triggering the data retention task

The data retention task may be manually triggered using the Operational Menu. In general, this is not recommended nor needed as the task will run automatically during other maintenance tasks.

Instructions are included in the [Operational Menu](#UUID-6c3a933b-cc7f-5dac-4888-e0ba970357c0_id_OperationalMenu-DataRetentionandPurging) documentation

## External Database Configuration

The server is configured by default with an inbuilt H2 database which is not recommended for enterprise deployment. Enterprise self-hosted deployments of Lifecycle or Firewall need to use an external PostgreSQL database. Lifecycle Cloud uses PostgreSQL in all instances.

- PostgreSQL 10.7 or newer for IQ Server releases 184 and prior
- PostgreSQL 14.0 or higher for IQ Server releases 185 and higher
- PostgreSQL-compatible service (such as Amazon Aurora PostgreSQL).

**Note:** Having a low-latency network connection between the server and the database is crucial or the performance will notably degrade.

The external database configuration is set in the . The connection parameters should be passed using environment variables.

```
export DATABASE_TYPE=postgresql
export DATABASE_HOSTNAME=<your_db_hostname>
export DATABASE_PORT=<your_db_port>
export DATABASE_NAME=<your_db_name>
export DATABASE_USERNAME=<your_db_user>
export DATABASE_PASSWORD=<your_db_password>
```

Add the following to the config YAML

```
database:
  type: ${DATABASE_TYPE}
  hostname: ${DATABASE_HOSTNAME}
  port: ${DATABASE_PORT}
  name: ${DATABASE_NAME}
  username: ${DATABASE_USERNAME}
  password: ${DATABASE_PASSWORD}
  ## optional key-value pairs to be appended to the database connection URL
  #parameters: 
    #example-param-key-name: example-param-value
```

### Troubleshoot external database connections

When the server fails to start:

```
GET http://localhost:8071/healthcheck
```

See

### Migrating IQ Server from H2 to PostgreSQL

The H2 database embedded within the IQ Server is single-threaded suitable for small instances. For production instances with databases over 10GB, we recommend migrating to an external PostgreSQL database.

These steps are applicable for all IQ server deployments covering: Lifecycle, Repository Firewall, Developer, and SBOM Manager instances.

The migration consists of the following steps:

- Export the data from the embedded database into an SQL dump
- Import the SQL dump into the PostgreSQL database

See for details on connecting to PostgreSQL

## Notification Configuration

### Configure the Base URL

You must configure the base URL before attempting to configure notifications for your team. IQ Server uses the base URL value to construct links for outgoing notifications.

IQ Server uses the `X-Forwarded-Proto` and `X-Forwarded-Host` headers to resolve user-facing URLs when an HTTP request comes through a reverse proxy server. Refer to the documentation of your reverse proxy server to correctly configure it to set these headers.

### Configure Email Notifications

The IQ Server can be configured to send email notifications for events such as policy violation notifications. This functionality requires an SMTP server. The SMTP connection details must specify hostname and port and optionally may also specify username, password, TLS/STARTTLS, and SSL. The system email is also required and will be used as the sender email for any emails the IQ Server sends. Make sure you have also set the Base URL.

![137204529.png](/docs-at-surgery-poc/assets/images/uuid-e21e33d7-2c2a-d3c7-7114-40e2f345bb88.png)

The email server is configured by a system Administrator using the Email option in the System Preferences menu.

### Configure Notifications through JIRA Cloud

**Note:** IQ Server Notifications are compatible with Jira Cloud, Server, and Data Center. Jira Server and Jira Data Center users are recommended to use the Sonatype for Jira integration.

The IQ Server can be configured to create Atlassian JIRA issues in response to policy violations.

JIRA integration requires:

- The Base URL must be configured.
- Basic JIRA connection information (URL, username, password)
- Default field values if selecting a JIRA project issue type that has custom required fields without default values defined in JIRA

⚠️ **Warning:** A JIRA system user should be configured for integration with IQ Server. Any authenticated user of the IQ Server will be able to view the projects and applicable issue types available to the configured user. IQ Server users who can create and edit policy will be able to set up automated ticket creation for any project over which the configured JIRA user has the authority to create tickets.

## Configuring System Notice

Administrators can configure the *System Notice* to inform users about various events, conditions or actions. It can also be used to communicate company policy or as a legal compliance requirement.

*System Notice* can contain alerts, available updates, or security warnings that will be displayed on all pages in-product, as well as the login prompt. The notice will be visible to all users and **cannot be dismissed** .

### Configuring the System Notice

- Login to *Sonatype Lifecycle* as an administrator.
- Click on the *gear* icon on the top right of the page.
- Select *System Notice* from the menu options.
- Enter the Notice Text (required) in the text box.
- Toggle the *Enable Notice control* to the on/off position to make the system notice visible/invisible.
- Click *Update* to complete the configuration.

### Audit Logs

Any change to the *System Notice* configuration will be recorded in the system [audit log](#UUID-8425a6ca-fe03-5803-f03b-3c6d6c8b1444) .

The logging information will include the timestamp, the IP address, username, type (configure) and the user provided notice text. It will also indicate if the system notice is configured to be enabled(show) or disabled(hide).

## Logging Configuration

Logging for the IQ Server is managed through settings in the config.yml file. The config YAML specifies the log directory to store for each of the log files.

See [Config YAML](#UUID-8d4fb66c-e0f4-0f2f-15a8-3d4226c007dd) for details.

### Logging Level Considerations

The recommended logging level for a production deployment is DEBUG. This is the default logging level for Lifecycle and it provides the most comprehensive logging information, which can be crucial for diagnosing issues.

Note that setting the logging level to DEBUG may cause the log file `clm-server.log` to grow very large. However, this level of detail is often necessary for support purposes.

### Logging Rotation

Log files are configured to rotate in 50 days' worth of gzipped dated archives. The location of the log files may be specified to store them in a separate archive.

### Application Log

The application log is found at `./log/clm-server.log` and archived logs are compressed with the name pattern of `clm-server-yyyy-MM-dd.log.gz` .

IQ Server uses [Dropwizard 1.3.x logging configuration](https://www.dropwizard.io/en/release-1.3.x/manual/core.html#id4)

### Audit Log

In the audit log, each entry is a JSON object. This allows for line-by-line parsing by external tools for inspection, analysis, and extraction of desired data.

Audit logging only occurs at the INFO level. Thus setting an audit logger level to ALL, TRACE, or DEBUG has no effect, and setting it to WARN, ERROR or OFF will disable it.

Audit events are not appended to the application log. The last active audit log is found at `./log/audit.log` and archived audit logs are compressed with the name pattern of `audit-yyyy-MM-dd.log.gz` . Audit logging can be customized in the logging section of your `config.yml` file beneath the base audit logger com.sonatype.insight.audit .

### Policy Violation Log

Policy violation logging is similar to the audit log, [each line or entry is a JSON object](#UUID-f881820f-fff9-cef2-b66b-e0b0dfa537f0) . This allows for easy line-by-line parsing by external tools for inspection, analysis, and extraction of desired data.

By default, policy violation logging is disabled. It can be enabled and customized in the logging section of your `config.yml` file beneath the policy violation logger `com.sonatype.insight.policy.violation` . Policy violation events are logged independently and are not appended to the application log.

**Note:** Policy violation logging only occurs at the INFO level. Thus setting the policy violation logger level to ALL, TRACE, or DEBUG has no effect, and setting it to WARN, ERROR or OFF will disable it.

Using the following suggested configuration

**Suggested policy violation logger configuration**

```
logging:
  loggers:
    com.sonatype.insight.policy.violation":
      appenders:
        - type: file
          # The file to which policy violations will be logged.
          currentLogFilename: ./log/policy-violation.log
          # When the policy violation log file rotates, the archived policy violation log will be renamed to this
          # and gzipped. The %d is replaced with the previous day (yyyy-MM-dd). Custom rolling windows can be created
          # by passing a SimpleDateFormat-compatible format as an argument: "%d{yyyy-MM-dd-hh}".
          #
          # If archive is true, this must be specified.
          archivedLogFilenamePattern: ./log/policy-violation-%d.log.gz
          # The number of archived policy violation log files to keep.
          archivedFileCount: 50
```

The last active policy violation log is found at `./log/policy-violation.log` and archived policy violation logs are compressed with the name pattern of `policy-violation-yyyy-MM-dd.log.gz` .

### Request Log

The last active request log is found at `./log/request.log` and archived logs are compressed with the name pattern of `request-yyyy-MM-dd.log.gz` . The request log can be customized in the `requestLog` section of the `config.yml` file.

IQ Server uses [Dropwizard 1.3.x requestLog configuration](https://www.dropwizard.io/en/release-1.3.x/manual/configuration.html#request-log)

### Audit Log

The audit log is located at `./log/audit.log` and the log format is simply the message followed by a newline such that each audit log entry is an unformatted JSON message on its line. The audit log can be [customized in your IQ Server configuration.](#UUID-3e88a34a-c077-2047-4f8d-e1d838e2066e_id_LoggingConfiguration-AuditLog)

**Note:** For each audit log entry, each optional attribute will either be present with its name and value, or will not be present at all i.e. no name or value.

### Policy Violation Log

The policy violation log is located at `./log/policy-violation.log` . Each line is an independent JSON string representing a policy violation.

The policy violation log is enabled through the [Logging Configuration](#UUID-3e88a34a-c077-2047-4f8d-e1d838e2066e_id_LoggingConfiguration-PolicyViolationLog) .

## Sample Data Configuration

New installations of IQ Server generate a sample Application called "Sandbox Application" underneath a sample Organization called "Sandbox Organization." These sandbox structures exist for proof-of-concept demos and to give new users a place to experiment with IQ Server's features.

We recommend that you delete this sample Organization and Application when they're no longer needed. They are not tied to any processes and deleting them will not affect IQ Server functionality in any way.

If you are installing a fresh instance of IQ Server and do not want these Sandbox structures to be automatically created, you can turn them off by editing the configuration file directly prior to running IQ Server for the first time.

1. Find the existing createSampleData property in the config.yml and change it to `false` .

```
createSampleData: false
```

## InnerSource Repository Configuration

Organizations that use Nexus Repository 3 as their InnerSource code repository can integrate Lifecycle with the repository to view version data of InnerSource components. This data is made available in the Version Explorer graph on the component details page.

Refer to the [InnerSource Insight](#UUID-ca9833c6-2581-80b8-3b57-84dd160adaf6) documentation to learn more about InnerSource components and Lifecycle support for InnerSource.

This is typically the repository that a developer (or CI server) would configure the local environment to access InnerSource component distributions. This can either be a hosted or a proxy repository and it can even be a mixed repository that hosts both open-source and InnerSource components. The credentials used for connection configurations must have privileges to browse and locate components and their versions.

In the case of proxy repositories, only the components downloaded to the repository will be considered.

### Repository configuration levels

An InnerSource repository can be configured in IQ Server at different levels in the organizational hierarchy. Child organizations and applications can be configured to inherit parent repository connection settings. Similarly, settings can also be disabled at any level and block child organizations and applications from overriding or configuring local connections.

By default, InnerSource Repository configuration is disabled on the Root Organization which will be inherited by all organizations and applications, however, the default setting also permits overrides to this configuration so that other organizations and applications can configure their own settings.

### Configuring InnerSource repository connections on Organizations and Applications

To configure an InnerSource repository connection for any application or organization:

![InnerSource Repositories](/docs-at-surgery-poc/assets/images/uuid-0cac7304-73fb-655c-2713-bfb9ba8af664.png)

This section lists the effective InnerSource repository connections applicable to the selected application or organization. Depending on how it is set up, it should specify if the connections are inherited from a parent organization or local to itself or none if no applicable repository connections for this.

4. To change this configuration click the edit button to pull up the configuration shown below.

![Innersource_Repository_Configuration.png]({{ /assets/images/uuid-23c9cc8c-055e-1757-0410-c90859ce0c3d.png)

The options will vary slightly depending on whether you are editing the Root Organization, a child organization, or an application.

- For the Root Organization, you are able to select whether InnerSource Repository Configuration is enabled or disabled, and whether or not child organizations and applications are able to override this configuration.
- For child organizations, you are able to select whether or not InnerSource Repository Configuration is enabled, disabled, or inherited from the parent, as well as whether or not applications are able to override this setting.
- For applications, you are able to select whether or not InnerSource Repository Configuration is enabled, disabled, or inherited from the parent.

If a parent organization has disabled overrides then the settings from that parent will be inherited and the user interface for editing the configuration will be disabled with a message indicating the reason.

### Configuring a Repository connection

In order to add a new repository connection:

![Add_Innersource_Repository_Configuration.png](/docs-at-surgery-poc/assets/images/uuid-16ed81e2-7dad-9980-003c-3d11fbe89e58.png)

4. Enter the following parameters

5. Click **Test Configuration** to verify a connection can be made to the Nexus Repository 3 server.

6. Click **Create** when finished.

### Editing or Deleting an existing repository connection

For editing an existing repository connection, or to delete one, you can click the edit or delete icons of the respective connection from the InnerSource Repository Configuration page. The edit pop up which is similar to the add configuration pop up above allows you to change the existing connection details and clicking the delete icon will remove the selected connection.

**Note:** Make sure you have the right permissions to access/view the InnerSource configuration (View IQ Elements) and to edit repository connection details (Edit IQ Elements).

## Public Data Sources for CPE Vulnerabilities

### Common Platform Enumeration Vulnerability Detection

The relationship between CPE (Common Platform Enumeration) identifiers and CVEs (Common Vulnerabilities and Exposures) is crucial for effective vulnerability management. When a vulnerability (CVE) is discovered, the National Vulnerability Database (NVD) is updated by NIST to indicate which CPE identifiers (product names and versions) are vulnerable.

Sonatype's vulnerability database ingests all CPE-CVE mappings from the public data sources (NVD feed), to allow detection of additional vulnerabilities, outside of the vulnerabilities detected from the [proprietary vulnerability detection system](https://help.sonatype.com/en/sonatype-vulnerability-data.html) .

*Sonatype Lifecycle* can identify the CPE names from the ingested SBOMs and trigger policy evaluations.

### Configuring Lifecycle to Use Public Data Sources

Users can configure Lifecycle to use public data sources for detection of vulnerabilities. This includes the CPE product dictionary that contains official CPE names. By default, this is enabled for C/C++ ecosystems.

Steps to configure Public Data Sources:

- Click on *Orgs and Policies* in the left navigation bar.
- Select root organization or the organization/application for which you want to enable the inclusion of public data sources for policy evaluations.
- Click on *Public Data Sources* in the top navigation bar.
- Scroll down to the Public Data Sources section.
- Click on the right arrow to access the Public Data Sources configuration. NOTE: The Inherit from parent option is available for all organizations and applications (except for root organization) and can be used to enable *Public Data Sources* for all organizations and applications lower in the organization hierarchy.
- Check the box under Public Data Overrides to allows users to selectively enable the public data sources for a specific organization or application. NOTE: This section will not be available at the application level.

### How It Works:

The application evaluation report will show the vulnerabilities detected from public data sources.

Click on the *Security tab* on the Component Details Page and scroll down to the Vulnerabilities table.

![4_public_data_sources.png]({{ /assets/images/uuid-c974255f-e255-c8f6-45e8-95e2f73ca151.png)

The *Data Enrichment* column indicates **Public Data** for vulnerabilities detected from public data sources.

Click on a row to view the [Vulnerability Details](https://help.sonatype.com/en/component-details-page.html#violation-details-popover) .

![5_public_data_sources.png](/docs-at-surgery-poc/assets/images/uuid-5a0d7cee-690f-2f6b-8515-145471d3b0a8.png)

### CPE Matching Experience in SBOM Manager vs. Lifecycle

Sonatype SBOM Manager and Sonatype Lifecycle both support Common Platform Enumeration- (CPE) based vulnerability matching; however, the behavior and configuration differs depending on your setup and licening.

The following table outlines how CPE matching behaves across different installation types, including new installations and deployments that existed before the introduction of CPE matching:

## Waived Component Upgrades

Waiving a violation may be the only path forward when a critical components has a failing violation that has not yet been fixed. Project owners want to address the issue as soon as a non-violating version of the component is available.

Lifecycle may be configured to indicate when a non-violating upgrade is available for waived violations without having to manually check them one at a time. Use the information from the waivers dashboard to revoke waivers and re-prioritize the violations that now have a path forward.

**Note:** This functionality is disabled by default and should be configured using the instructions below.

### Configuration for Waived Component Upgrades

When configured, monitoring for available upgrades for waived components takes place daily.

- Log in as the System Administrator
- Select `Waived Components` from the System Preferences menu
- Enable the `Dashboard Indicator` under Component Upgrade Availability
- Select Update

![161120265.png]({{ /assets/images/uuid-e457ee3b-198c-4164-87b9-349a0a6744c8.png)

You may also update this configuration using the [Configuration REST API](#UUID-0fa6ca2c-1237-6aca-a4e6-ad4d074fd63f) .

### View Available Upgrades

- Select the `Waivers` tab on the main Dashboard
- Non-violating upgrades are displayed as `Available` in the Upgrade column
- Select the row to view the waiver details The waiver details provide context or justification to support upgrade decisions.

## Certificates and Secure Connections

Using a Transport Layer Security ( [TLS/SSL](https://en.wikipedia.org/wiki/Transport_Layer_Security) ) based connection is an important step in securing data moving through IQ Server. The configuration process is not automated but can be understood and implemented using best practices. This guide shows you how to set up secure connections to and from the IQ Server by helping you:

- Understand what TLS/SSL is and how certificates work.
- Describe how TLS works in Java applications in general and the common tools used during configuration.
- Understand best practice approaches for configuring keypairs, certificates, and trust stores for inbound and outbound connections to the IQ Server.
- Define common error messages seen with secure communication and provide steps toward resolution.

### TLS/SSL Protocol and the IQ Server

Transport Layer Security ( [TLS](https://searchsecurity.techtarget.com/definition/Transport-Layer-Security-TLS) ) is a standard security protocol for creating an encrypted communication channel between a client and a server. An example of use is when your web browser connects to a website using an HTTPS address.

Encrypted channels ensure that all data passed remains private. TLS is a newer iteration of the SSL (Secure Sockets Layer) protocol, with TLS supporting newer and more secure algorithms.

### Inbound IQ Server TLS Connections

Inbound connections to IQ Server use HTTPS, which is built on TLS technology.

Some example clients that can establish secure inbound connections to IQ Server are:

- A web browser viewing the IQ Server user interface at an https:// address.
- A custom Python program accessing the REST API.
- An official Sonatype integration such as an IDE or CI server plugin.

There are two options for setting up secure inbound connectors: reverse proxy HTTPS and direct HTTPS connections.

### Outbound IQ Server TLS Connections

Outbound TLS connections from IQ Server can use a variety of protocols like HTTPS, LDAPS, and SMTPS. By default, the IQ Server will use the Java truststore to establish the trust of remote certificates. If all remote TLS certificates are signed by public CAs, then no additional configuration is needed.

In the cases where your organization uses an HTTP proxy server that rewrites TLS certificates, or IQ Server is connecting to internal TLS endpoints such as mail or LDAP servers with custom certificates, you may have to customize what certificates IQ Server trusts.

Some example outbound secure connections IQ Server may make are:

- Performing scans and receiving report data from Sonatype data services.
- Emailing policy violation notifications via SMTPS by way of your configured email server.
- Sending payloads to your configured `https://` webhook URL.
- Authenticating users in your LDAP server using an LDAPS connection.
- Creating policy violation issues in your configured `https://` Jira server address.
- Use HTTPS CONNECT tunneling and trusting certificates signed by your configured HTTP Proxy Server.

The basic ingredients needed to trust outbound TLS certificates are:

### Best Practices

Now that you know what TLS protocol is, and how to set up inbound and outbound connections to the IQ Server, we’ll give you a few best practice examples to better aid in establishing secure connections.

### Common Error Messages

If the IQ Server appears to start on the secure port without error, but the Java keytool client commands fail with “No certificate from the SSL server,” Web browsers cannot load the application user interface on the secure port, and you receive one of the following error messages:

Google Chrome:

- This site can’t be reached. Localhost unexpectedly closed the connection. ERR_CONNECTION_CLOSED
- This site can’t provide a secure connection. Localhost uses an unsupported protocol. ERR_SSL_VERSION_OR_CIPHER_MISMATCH

Firefox:

- The secure connection failed. The connection to localhost was interrupted while the page was loading.
- The secure connection failed. An error occurred during connection to localhost. Cannot communicate securely with peers: no common encryption algorithm(s). Error code: SSL_ERROR_NO_CYPHER_OVERLAP

Safari:

- Safari can’t open the page because Safari can’t establish a secure connection to the server.

Curl commands error:

- The server aborted the SSL handshake

Wget commands error:

- Unable to establish an SSL connection

### FAQs

The following frequently asked questions provide more troubleshooting information on IQ Server and secure connections.

## Operational Menu

The Operational Menu is a simple landing page listing API endpoints for monitoring the IQ Server. These endpoints are bound to the adminConnectors property of the HTTP Configuration. You may navigate to this page directly on the server using the [http://localhost:8071](http://localhost:8071) URL.

⚠️ **Warning:** The API endpoints exposed on the adminConnectors port are not protected by credentials as some monitoring tools require. This port should never be opened to traffic outside a private subnet as abuse will impact the server's health.

![155616700.png](/docs-at-surgery-poc/assets/images/uuid-260692e6-72eb-0785-1692-b7f277de8b1d.png)

### API Endpoints

### Other Admin APIs

The admin connector exposes additional endpoints used to trigger internal maintenance tasks manually. These tasks should mostly be avoided unless recommended during guidance from the Sonatype Support team. A few are detailed below however most will remain unpublished.

## Advanced Legal Pack Extended Observed License Detections

As of Nexus IQ release 165, the Advanced Legal Pack expands Lifecycle's observed license detection from Maven to all of ALP's supported ecosystems. In order to not disrupt existing installation a configuration option must be enabled to receive this new data. New installations have this feature enabled by default.

### Enabling Extended Observed License Detections

To enable extended observed license detection a PUT must be made against the config endpoint with the `alpObservedLicenseDetectionEnabled` flag set to `true` . For example:

```
curl -u admin:admin123 -X PUT -H Content-Type: application/json" -d '{"alpObservedLicenseDetectionEnabled": true}' http://localhost:8070/api/v2/config
```

To disable this functionality the configuration flag can be deleted:

```
curl -u admin:admin123 -X DELETE 'http://localhost:8070/api/v2/config?property=alpObservedLicenseDetectionEnabled'
```

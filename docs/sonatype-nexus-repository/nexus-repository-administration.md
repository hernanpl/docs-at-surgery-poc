---
layout: default
title: "Nexus Repository Administration"
parent: Sonatype Nexus Repository
nav_order: 6
---

# Nexus Repository Administration

This section details Nexus Repository administration. These features are accessible only to authorized users.

## Administration Menu

The Administration menu, located on the left panel, contains the following sections:

- Manage all repositories and related configurations such as Routing and Targets.
- Access configuration related to the authentication and authorization of users.
- Sets the connection to IQ Server for the Repository Firewall and Sonatype Lifecycle integrations.
- Administer and monitor your Nexus Repository using the tools found in the support section. Package a support zip for assistance with Sonatype Enterprise Support.
- General configuration for automation and notifications.

## Access Control

Nexus Repository uses a role-based access control (RBAC) model to provide access to specific functionality for authenticating users.

### Role-Based Access Control

Role-Based Access Control (RBAC) is a method of restricting system access to authorized users. It's a core component of many security strategies, especially when it comes to managing access in organizations with numerous users and varying levels of responsibility.

In Nexus Repository, RBAC is implemented using the following object model:

- Nexus Repistory comes with a default set of permissions or privileges for every feature and function. These cover the use cases for most implementations. Custom privileges may be made to a group of privileges together or to limit to a specific location in a repository. **Privileges** are assigned to **Roles** .
- Content Selectors are a path or namespace to a specific location in a repository. They are used as targets for creating custom privileges to grant edit access to that location. These are often used to limit which teams may upload their binaries to their project's namespace. **Content Selectors** are used for custom **Privileges** .
- Roles are a way to group related permissions so they can be easily assigned to users. Think of it as a job title or a set of responsibilities within a system or organization. Roles may be assigned to specific users however they most often represent a group of users. A user may have any number of roles assigned to them. **Roles** are assigned to **Users** or **User Groups** .
- Users are either individuals or systems that interact with the Nexus Repository application through the web user interface or the REST API. Most users connect to Nexus Repository through their package management system during development. **Users** or **User Groups** are assigned one or many **Roles** .
- The default role provides a collection of privileges for all users who can authenticate using one of the configured security Realms. At a minimum, these privileges should include permissions granted to the anonymous user. The **Default Role** is assigned to any **Authenticated User** .
- The anonymous role is a unique set of privileges assigned to unauthenticated or anonymous users. By default, this role provides open access to read, search, and browse all repositories. As one of the system roles, it cannot be edited. We recommend avoiding this role unless required. When anonymous access is allowed, create a custom role with restricted access to assign to anonymous users.

### Principle of Least Privilege

When designing your RBAC model we recommend using the Principle of Least Privilege.

The Principle of Least Privilege (PoLP) is a core security concept that dictates that users, processes, and programs should only be granted the minimum necessary access rights they need to perform their designated tasks. These are typically the essential permissions required for a user or entity to complete their job function. Avoid assigning excessive or unnecessary privileges.

By restricting access, you limit the potential damage that can occur from errors, malware, or malicious actors. If a compromised account has limited access, the impact of a breach is significantly reduced.

How to implement a least privilege model:

### Default Roles

The default configuration ships with the administrator role and optional anonymous access to browse and read all repositories.

- The default administrator role provides privilege to all aspects of the Nexus Repository system and uses the username `admin` . The initial password is found in an `admin.password` file in the `$data-dir` directory after startup.
- You should not use the default anonymous role if you need to create protected repositories.

### Privileges

Privileges define the actions a user may perform within the Nexus Repository. They grant access to resources, ensuring that users have the appropriate permissions based on their roles.

### Roles

Roles aggregate privileges into a related context and can, in turn, be grouped to create more complex roles.

- To create and manage roles, navigate to *Settings* → *Security* → *Roles* .
- You must have the *nx-roles* or *nx-all* privilege to access the *Roles* screen.
- To create, edit, or delete roles, you must have the *nx-privilege-read* or *nx-all* privilege.

Nexus Repository ships with defined admin and anonymous roles which may not be edited or deleted.

![Roles listing](/docs-at-surgery-poc/assets/images/uuid-2704539e-cd3b-3bfc-782d-a4c33dc96ae2.png)

### Users

Nexus Repository determines users who may access the server through various security realms and identity providers. These realms contain the collection of users, who may or may not be assigned to a group.

Users may be configured to the local realm of Nexus Repository; however, the best practice is to manage and associate users through an externally managed security realm to reduce repository management workloads. Using realms simplifies the onboarding and offboarding of users to authorized external systems.

### Default Role

The Default Role is a role that is automatically granted to all authenticated users.

To enable appending a default role to all authenticated users, create a new Capability using capability type *Default Role* as pictured below; you will then be able to select the role that you want applied to users.

![50626754.png]({{ /assets/images/uuid-e4636a5a-c4b5-45c7-45f2-58fdc9953ece.png)

Once this is saved, the *Default Role Realm* will be added to the active list of security realms and start applying the new role to all authenticated users.

**Note:** This default role is appended to authenticated users dynamically, and will **not** show up as assigned to any user via the *User* administration page.

### Content Selectors

Content selectors give access to specific content or namespace from a repository rather than the entire repository. The content is selected using search expressions written in CSEL (Content Selector Expression Language). CSEL is a light version of JEXL used to script queries along specific paths and coordinates available to your repository manager formats.

Content selectors define what content users are allowed to access. You define a selector name with a search expression to match all components that start with the designated component path.

After creating the content selector, it must be added to a privilege to scope it to a specific repository. This privilege is used to provide access to that namespace for a role, group, or user.

```
Content Selector > Privilege > Role > Group > User
```

See the Manage Selector Permissions section for using content selectors in Privileges.

## Auditing

Auditing is done using a capability called *Audit*. For your convenience, this capability is created and enabled by default.

When the *Audit* capability is enabled, Sonatype Nexus Repository updates a log file located in `$data-dir/log/audit/audit.log` each time a user or internal process modifies Nexus Repository configuration or adds or removes an asset or component. Nexus Repository rotates this log file daily and retains a maximum of 90 days' worth of files.

### Nexus Repository Audit Log Attributes

Each line of the audit log contains an unformatted JSON message representing a single audit item. The table below provides a list of attributes available in these JSON messages:

### Nexus Repository Audit Log Available Types

The table below lists available Nexus Repository audit log Java constants and their type values:

### Available Nexus Repository Audit Log Event Types per Domain

The table below lists available Nexus Repository audit log event types per domain:

## Capabilities

Nexus Repository features are configured as capabilities under *Settings* → *System* → *Capabilities*.

The *nx-capabilities* privilege is required to manage capabilities.

### Creating a Capability

### Disabling a Capability

Enable a capability at any time by selecting the *Enable* button on this same screen

### Base URL Capability

The *Base URL* is the address end users apply when navigating to the user interface. The repository manager only uses this value to construct absolute URLs to your user interface inside of email notifications. The most common reason why the address would be different is if you have a reverse proxy that terminates HTTP requests at an address different from where the repository manager is running.

To set the Base URL:

- Go to the *System* section of the *Settings* menu and select *Capabilities* .
- Search for an existing *Base URL* capability and select it if it exists or click the *Create capability* button and choose *Base URL* from the *Select Capability Type* list.
- Enter a new URL value.
- Press the *Create capability* to add the *Base URL* .

### UI Settings Capability

The *UI: Settings* capability allows you to configure elements of the Nexus Repository user interface as described in the table below.

### Branding Capability

**Note:** Only available in Sonatype Nexus Repository TM Pro. Interested in a free trial? [Start here](https://www.sonatype.com/products/repository-pro/trial) .

As part of Nexus Repository Pro, you can customize your repository manager instance by using HTML to insert customized messaging into the header and/or footer of your user interface. Note that you have full control over the HTML in these areas, so be mindful of introducing elements that could cause design or security issues.

You can configure your custom branding by adding and enabling the *Branding* capability.

### Log4j Visualizer

**Note:** The Log4j Visualizer does not work in High-Availability Clustering (HA-C) environments.

Log4j is the most popular logging framework used by Java software. As we detailed in [our blog](https://blog.sonatype.com/a-new-0-day-log4j-vulnerability-discovered-in-the-wild) and are still monitoring in our [Log4j Vulnerability Resource Center](https://www.sonatype.com/resources/log4j-vulnerability-resource-center) , vulnerability researchers uncovered a critical vulnerability ( [CVE-2021-44228](https://ossindex.sonatype.org/vulnerability/f0ac54b6-9b81-45bb-99a4-e6cb54749f9d) or "log4shell") in log4j.

To help the global software community defend itself against this threat, we are providing an experimental Log4j Visualizer to Nexus Repository users to provide greater visibility into Maven log4j component downloads impacted by CVE-2021-44228.

Note that the Log4j Visualizer only captures information about the log4j.core component in Maven and only identifies those impacted by CVE-2021-44228. It does not currently identify or track other log4j vulnerabilities.

The current Log4j Visualizer also only searches for this vulnerability using the specific path `org/apache/logging/log4j/log4j-core` .

**Note:** Sonatype is providing this Log4j Visualizer for a limited time to Nexus Repository users due to the urgent threat that the log4j vulnerability poses to the global software community. Access and use of the Log4J Visualizer is governed by the terms of your agreement with Sonatype or, in the absence of such, [these terms](https://www.sonatype.com/campaign/software-evaluation-agreement) . We may update or remove this feature completely in future versions.

## Configuring SSL

Using Secure Socket Layer (SSL) communication with Nexus Repository is an important security feature and a recommended best practice. Secure communication is inbound or outbound.

Outbound client communication may include integration with the following:

- a remote proxy repository over HTTPS
- SSL/TLS secured servers - for example, for SMTP/email integration
- LDAP servers configured to use LDAPS
- specialized authentication realms, such as the Crowd realm

Inbound client communication includes the following:

- web browser HTTPS access to the user interface
- tool access to repository content
- and manual or scripted usage of the REST APIs

### Outbound SSL - Trusting SSL Certificates of Remote Repositories

When the SSL certificate of a remote proxy repository is not trusted, the repository may be automatically blocked and outbound requests fail with messages similar to `PKIX path building failed` .

The Proxy configuration for each proxy repository documented in Managing Repositories and Repository Groups includes a section titled *Use the Nexus truststore* . It allows you to manage the SSL certificate of the remote repository and solves these problems. It is only displayed if the remote storage uses a HTTPS URL.

The *View certificate* button triggers the display of the SSL Certificate Details dialog.

![Certificate Details Dialog to Add an SSL to the Nexus Truststore](/docs-at-surgery-poc/assets/images/uuid-aad35c85-faa5-7986-2da1-91da9ca358df.png)

Use the *Certificate Details* dialog when the remote certificate is not issued by a well-known public certificate authority included in the default Java trust store. This specifically also includes the usage of self-signed certificates in your organization. To confirm trust in the remote certificate, click the *Add certificate* *to truststore* button in the dialog. This feature is analogous to going to the SSL Certificates user interface and using the Load certificate button found there in the Outbound SSL - Trusting SSL Certificates Globally section. If the certificate is already added, the button can undo this operation and will read *Remove certificate from trust store* .

The checkbox labeled Use certificates stored in Nexus to connect to external systems is used to confirm that the repository manager should consult the internal truststore as well as the JVM truststore when confirming trust in the remote repository certificate. Without adding the certificate to the private truststore and enabling the checkbox, the repository will not trust the remote.

The default JVM truststore of the JVM installation used to run the repository manager and the private trust stores are merged. The result of this merge is used to decide about the trust of the remote server. The default Java truststore already contains public certificate authority trust certificates. If the remote certificate is signed by one of these authorities, then explicitly trusting the remote certificate will not be needed.

⚠️ **Warning:** When removing a remote trusted certificate from the truststore, a repository manager restart is required before a repository may become untrusted.

### Outbound SSL - Trusting SSL Certificates Globally

The repository manager allows you to manage the trust of all remote SSL certificates in a centralized user interface. Use this interface when you wish to examine all the currently trusted certificates for remote repositories or manage certificates from secure remotes that are not repositories.

Access the feature view for SSL Certificates administration by selecting the *SSL Certificates* menu items in the *Security* sub-menu in the Settings menu. A user must have the *nx-ssl-truststore* privileges to access this view.

![SSL Certificates Administration Screen]({{ /assets/images/uuid-657b9dbf-deee-6359-ba01-226e094ac092.png)

The list shows any certificates that are already trusted. Clicking on an individual row allows you to inspect the certificate. This detailed view shows further information about the certificate including *Subject* , *Issuer,* and *Certificate* details. The *Delete certificate* button allows you to remove a certificate from the truststore.

The button *Load certificate* above the list of certificates can be used to add a new certificate to the truststore by loading it directly from a server or using a Privacy Enhanced Mail (PEM) file representing the certificate.

The common approach is to choose Load from the server and enter the full `https://` URL of the remote site (e.g., `https://repo1.maven.org).` The repository manager will connect using HTTPS and use the HTTP proxy server settings if applicable. When the remote is not accessible using `https://` , only enter the hostname or IP address, optionally followed by a colon and the port number. For example; `example.com:8443` . In this case, the repository manager will attempt a direct SSL socket connection to the remote host at the specified port. This allows you to load certificates from SMTP or LDAP servers if you use the correct port.

Alternatively, you can choose the *Paste PEM* option to configure the trust of a remote certificate.

A PEM file is a type of Public Key Infrastructure file used for keys and certificates. PEMs are Base64-encoded X.509 DER certificates. Read more in [SSL's guide](https://www.ssl.com/guide/pem-der-crt-and-cer-x-509-encodings-and-conversions/) .

Copy and paste the Base64 encoded X.509 DER certificate to trust. This text must be enclosed between lines containing `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----` .

You will typically get this file from the certificate owner. An example method to get the encoded X.509 certificate into a file on the command line using `keytool` is:

```
keytool -printcert -rfc -sslserver repo1.maven.org > repo1.pem
```

The resulting `repo1.pem` file contains the encoded certificate text that you can cut and paste into the dialog in the user interface.

If the repository manager can successfully retrieve the remote certificate or decode the pasted certificate, the details will be shown allowing you to confirm details. Please review the displayed information carefully before clicking *Add Certificate* to establish the truststore addition.

In some organizations, all of the remote sites are accessed through a globally configured proxy server which rewrites every SSL certificate. This single proxy server is acting as a private certificate authority. In this case, you can follow special instructions for trusting the proxy server root certificate, which can greatly simplify your certificate management duties.

### Outbound SSL - Trusting SSL Certificates Using Keytool

Managing trusted SSL certificates from the command line using `` and system properties is an alternative and more complex option than using the SSL certificate management features of the repository manager.

Before you begin the process of trusting a certificate from the command line you will need:

- a basic understanding of SSL certificate technology and how the Java VM implements this feature
- command line access to the host operating system and the `keytool` program
- network access to the remote SSL server you want to trust from the host running the repository manager. This must include any HTTP proxy server connection details.

If you are connecting to servers that have certificates which are not signed by a public CA, you will need to complete these steps:

Some common commands to manually trust remote certificates can be found in our [SSL Certificate Guide](https://support.sonatype.com/hc/en-us/articles/213465768-SSL-Certificate-Guide?&_ga=2.194258667.792575935.1700493523-291822469.1668525051#common-keytool-commands) .

After you have imported your trusted certificates into a truststore file, you can add the JVM parameters configuring the truststore file location and password as separate configuration lines into the file `$install-dir/bin/nexus.vmoptions`

```
-Djavax.net.ssl.trustStore=<absolute_path_to_custom_truststore_file>
-Djavax.net.ssl.trustStorePassword=<truststore_password>
```

Once you have added the properties shown above, restart the repository manager and attempt to proxy a remote repository using the imported certificate. The repository manager will automatically register the certificates in the truststore file as trusted.

### Inbound SSL - Configuring to Serve Content via HTTPS

Providing access to the user interface and content via HTTPS is a best practice.

You have two options:

- Use a separate reverse proxy server in front of the repository manager to manage HTTPS
- Configure the repository manager itself to serve HTTPS directly

## Email Server Configuration

Nexus Repository may send out email messages for a number of reasons. In order for these messages to be delivered, you need to configure the connection to the SMTP server under the *Email Server* menu item in the *System* section of the *Settings* menu as displayed in *Figure: “Email Server Configuration”* .

The ability to access this item can be given by granting the user the nx-settings privilege. Note that the nx-settings privilege gives access to a number of pages of the same theme. There is no privilege to give access to just this item without others.

![Email server configuration form](/docs-at-surgery-poc/assets/images/uuid-2596a7f1-c32e-20f5-361b-e8232ae55072.png)

The following configuration options are available:

**Enabled**

Determines whether email sending is activated or not, independent of a server being configured.

**Host and Port**

The name of the host and the port to use to connect to the SMTP server.

**Use the Nexus truststore**

This checkbox allows you to configure the repository manager to use its certificate truststore. You can also view and import the certificate from the email server. Further details are documented in the Configuring SSL section.

**Username and Password**

The credentials of the user of the SMTP server to use for authentication.

**From address**

This parameter defines the email address used in the From:" header of any email sent by the repository manager. Typically, this is configured as a "Do-Not-Reply" email address or a mailbox or mailing list monitored by the administrators of the repository manager.

**Subject prefix**

This parameter allows you to define a prefix used in the subject line of all emails sent by the repository manager. This allows the recipients to set up automatic filtering and sorting easily. An example is

[Nexus Notification] .

**SSL/TLS options**

These options can be used to configure usage of Transport Layer Security (TLS) and Secure Sockets Layer (SSL) when emails are sent by the repository manager using SMTP. These options include the ability to use STARTTLS, which upgrades the initially established, plain connection to be encrypted when sending emails. The following options are available to you:

**Enable STARTTLS support for insecure connections**

This checkbox allows you to enable support for upgrading insecure connections using STARTTLS.

**Require STARTTLS support**

This checkbox requires that insecure connections are upgraded using STARTTLS. If this is not supported by the SMTP server, no emails are sent.

**Enable SSL/TLS encryption upon connection**

This checkbox enables SSL/TLS encryption for the transport on connection using SMTPS/POPS.

**Enable server identity check**

This option verifies the server certificate when using TLS or SSL, following the RFC 2595 specification.

Once you have configured the parameters you can use the *Verify email server* section to confirm the configured parameters and the successful connection to the server. You are asked to provide an email address that should receive a test email message. Successful sending is confirmed in a message.

![Verify email server section](/docs-at-surgery-poc/assets/images/uuid-b546e317-b064-970c-01db-916114a8a4d3.png)

## HTTP Request and Proxy Settings

Nexus Repository uses HTTP(s) requests to fetch content from remote servers configured as proxy repositories. Administrators may set the global configuration for outbound request retries and timeouts.

![Partial view of HTTP configuration screen]({{ /assets/images/uuid-4872638c-c1fa-5831-eb1d-2b3aaec6cfbd.png)

### HTTP and HTTPS Settings

The following configurations are available under settings → System → HTTP in the Nexus Repository user interface. Users require the `nx-settings` privilege to view and edit these settings.

### Default HTTP Settings in Nexus Repository

The default HTTP settings in Nexus Repository are as follows:

## License Management

Access to enterprise features for Nexus Repository requires a Professional (Pro) license. Visit Sonatype website for details on pricing and how to purchase a license.

### Methods to Install a License

Adding or removing a license requires the `nx-license` privileges. In general, we recommend uninstall old licenses before installing the new license to reduce risk of leaving behind incorrect data in the deployment.

Which methods to use depends on your deployment model. License management differs between single-instance and clustered deployments.

- Any method for installing a license is suitable, however the user interface is the fastest method when first getting started.
- We recommend using the REST API when removing or updating a license in a containerized or OpenShift environment. Using the system configuration method to update the configuration files in container is challenging and may lead to inconsistency in upgrading your deployment.
- Every instance in a cluster must have a valid license. Administrators may update the license for the whole cluster by installing a new license on any single node. The new license is stored in the database for seven days during which nodes use the license expiration date to compare their license with the database. The other nodes update their license automatically when a newer license is detected. Update your license according to the recommend method found for your deployment model. Administrators must update their cluster configuration files with the new license to use when starting new nodes. Before the 3.74.0 release, updating the license through the user interface only installs the license on the single node. We recommend using the IP address of each node to make API requests.
- Update your license according to the recommend method found for your deployment model.
- Administrators must update their cluster configuration files with the new license to use when starting new nodes.
- Before the 3.74.0 release, updating the license through the user interface only installs the license on the single node. We recommend using the IP address of each node to make API requests.

### License Management in the User Interface

View the installed license in Nexus Repository by navigate to Settings → System → Licensing in the user interface. This page shows a summary of the license terms, the licensed Sonatype solutions, and the contact details of the account owner.

In this view you may install or update the license.

![nx-license-view-usage-license.png](/docs-at-surgery-poc/assets/images/uuid-534a5a62-46f7-22d8-2839-5cdd4418e808.png)

### Install a License in the User Interface

To install a license use the following steps:

After restart, the licensing panel displays the features associated with your license.

### Install a License with the REST API

Use the Licensing API to automate installing or uninstalling the license file on running instances.

See the Licensing API documentation

### Install the License with System Properties

You may install a license using a system property the first time Nexus Repository is initialized. Once a license is installed, this property is ignored. Removing the license file property does not uninstall the license.

### Expired Licenses

When your license expires, Nexus Repository is disabled except to install a new license or generate a support zip. The Sonatype account team provides the license as a `.lic` file in an email sent to the primary stakeholders.

To update an expired license, uninstall the license using the Licensing API. Follow the instructions for your deployment model to install a new license.

See the Licensing API documentation

### Overriding the License File Location

The default location of the license file stored on disk may be modified by changing the Java user preferences.

See the Configuring the Runtime Environment section

### Monitoring Recent Connections

You may approximate the number of unique logins using a log parser on the `request.log` files. The IP address and authenticated user ID associated with each request appears in columns 1 and 3 of the log line.

See our [knowledge base article](https://support.sonatype.com/hc/en-us/articles/213464168-Sonatype-Nexus-License-FAQ) for more information.

### Copying an Installed License

An installed license may be moved from one Nexus Repository instance to another instance as the license is stored in the Java user preferences directory for the user that owns the server process. These instructions only apply to Linux and MacOS environments and does not apply to Windows.

Locate the product license in the home directory of the user running Nexus Repository at this location:

```
~/.java/.userPrefs/com/sonatype/nexus/professional/prefs.xml
```

## Malware Risk

Nexus Repository detects malware within your repository and warns users when malicious components are found. We highly recommend Nexus Repository administrators remove the artifacts as quickly as possible to limit these malicious components' impact on their environment.

### Recommended Action

### Discovered Malware Banner

Users logging into Nexus Repository see a warning banner when Malware components are found in their repositories. We recommend users contact their system administrators to report the discovery and request they remove the components immediately.

![Docs_ex_image2.png]({{ /assets/images/uuid-ce6bd9e2-5b36-6b9d-5d85-47ec72a17523.png)

The banner is updated every 24 hours.

### Automatic Malware Management Task

The Automatic Malware Management task enhances the security of your repository by identifying potentially malicious components found in your proxy repositories.

This task integrates with your existing Repository Firewall solution to analyze components and flag potential threats. Use Repository Firewall to block your users from downloading malware in the first place.

- Using this task requires the Repository Firewall solution. This task fails when a connection to the Repository Firewall cannot be established. This task requires the Repository Firewall enabled with the Security-Malicious policy set to fail to function as expected.
- NEW IN 3.77.0 This option auto-deletes identified malware components from the repository when discovered. Components that are deleted may be actively used for your application builds. While auto-deleting malware components put your builds at risk of failure, preventing malware components from being released outweighs this risk.
- Most malware is discovered on proxies to npm and PyPI repositories. We recommend targeting these repositories first to keep these critical repositories current. Malware Risk supports the following languages: npm, Maven, PyPI, Nuget
- This task takes time to complete depending on the number of repositories analyzed. During this time the malware banner may report a different quantity than those included in the download list. This discrepancy will most likely resolve itself when the task has time to run and the malware banner is updated once every 24 hours. A similar issue is when the CSV file lists malware that has been previously deleted for audit reasons. Some components may be found in the CSV that were previously reported on the malware banner but are no longer.
- This task should be scheduled to run no more than once a day.
- Nexus Repository reports an error in the system status when this task is disabled. Enable the task to keep your repositories protected.
- Selecting all repositories may result in a long-running task depending on the number of proxy repositories and components in those repositories. For larger deployments, consider setting up multiple tasks to run against larger repositories independently.

See the Tasks documentation for details on adding this task.

### Malware Risk Dashboard

**Note:** Only available in Sonatype Nexus Repository TM Pro. Interested in a free trial? [Start here](https://www.sonatype.com/products/repository-pro/trial) .

Nexus Repository Pro Administrators have access to the Malware Risk Dashboard which includes details of malware risk in their repositories and how to protect their organization.

This information is available for Repository Firewall users.

![nx-malware-risk-dashboard.png](/docs-at-surgery-poc/assets/images/uuid-072cb51c-31b9-18f4-9b9e-7849dd1d2611.png)

- **Open Source Malware Protection Status** This dashboard reports the risk of malware found by Sonatype in public ecosystems. The dashboard reports the number of proxy repositories currently protected from Malware using Sonatype Repository Firewall.
- **Steps to Remediate** Use the following steps to find and remove malware components from your repository. Download the CSV file using the link below to review the components flagged by Sonatype as containing malware. Search your proxy repository to remove the components. Protect your repository to keep developers from downloading Malware.
- Download the CSV file using the link below to review the components flagged by Sonatype as containing malware.
- Search your proxy repository to remove the components.
- Protect your repository to keep developers from downloading Malware.

### What is Malware Risk?

Open-source malware is deliberately crafted to execute harmful actions that can severely compromise your system and significantly increase risk. These packages are designed to look legitimate but are malicious entities that often do not even pretend to be working code. They infiltrate software supply chains by exploiting the automation in build or dependency managers, frequently executing on download.

Once downloaded, the damage is often already done. **Even one malicious component is too many** as it may compromise your entire build pipeline by stealing data, installing more malware, and hijacking systems, sometimes without immediate detection. The more malicious components you have, the greater the risk of exposure, and the more complex it becomes to manage and remediate.

The severity of these threats cannot be overstated. Even when discovered and removed from repositories like PyPI or npm, the absence of a CVE complicates efforts to track and address the threat, leaving systems vulnerable and risk mitigation challenging.

## Nodes

From *Settings* → *System* → *Nodes,* you can protect your server’s database from write access by activating read-only mode. This allows you to avoid modifications to your server configuration and blob stores when performing system maintenance.

To enable it:

⚠️ **Warning:** Anything that would require a change to a database will fail during read-only mode.

The button becomes *Disable read-only* mode when enabled. A banner appears above the main toolbar, notifying you that read-only mode is activated.

Disabling read-only mode, by clicking the *Disable read-only* mode button returns the server to its original, writable state.

**Note:** Note that if you are using one of our High Availability deployment options and a node is not shut down gracefully, this node will continue to appear on the *Nodes* page for a few seconds.

### High Availability Clustering (HA-C) (Legacy) Notes

In High Availability Clustering (Legacy) mode, the *Nodes* screen also provides a summary of all active nodes. The screen keeps a record of all running nodes that you manage in table form.

When you click a row, you get a detailed summary of the chosen node.

The summary lists:

- *Node Identity* , a unique ID accessible via the *System Information*
- *Socket Address* , the address corresponding to the server

When running in HA-C mode the *Nodes* screen displays all synchronized nodes in the table. View the table to monitor and verify server connections.

## Re-encryption in Nexus Repository

Nexus Repository uses a static key for reversible encryption to store sensitive data like passwords. We recommend administrators change the encryption key to enhance their repository security.

**Note:** Best Practice When Upgrading The Nexus Repository upgrade involves applying database scripts to change the schema which the re-encryption mechanism depends on. We recommend avoiding making changes to the encryption while performing an upgrade. Perform the re-encryption outside of your regular upgrade maintenance plan.

The following health check warning displays when the default encryption key has not been updated:

`Nexus was not configured with an encryption key and is using the Default key`

Use the sections below to re-encrypt your secrets to resolve the warning.

### Create a JSON File Containing Your Custom Encryption Key

Create a JSON file containing your custom encryption key. This file remains part of your deployment to decrypt persisted secrets.

Use the following JSON format and save it as a `.json` file in a secured location.

```
{
  active": "my-key",
  "keys": [
    {
      "id": "my-key",
      "key": "some-secret-key"
    }
  ]
}

```

The JSON file specifies the following properties:

- `active` - The key to use for encryption; the value matches the `id` in the `keys` array
- `keys` - An array containing key objects
- `id` - A unique identifier for the key
- `key` - The secret key value; any random string value. Use `null` in HA environments for the **first restart** as described in the High Availability Deployments section

### Update the Encryption Algorithm

Users are able to configure a property on `nexus.properties` file to configure the algorithm used to hash local users passwords.. Consider updating the encryption algorithm to using one-way hashing with PBDKF2 SHA256 or higher.

```
nexus.security.password.algorithm=PBKDF2WithHmacSHA256
```

See the Local User Password Algorithm section

### Add the Secrets File to the Nexus Repository Configuration

Use one of the following methods to configure Nexus Repository with the custom encryption key.

- Add the `nexus.secrets.file` property pointing to the secrets JSON file in your `$data-dir/sonatype-work/nexus3/etc/nexus.properties` .
- Use the `NEXUS_SECRETS_KEY_FILE` environment variable to pass your JSON key file to the Nexus Repository.
- Helm chart set the `secret.nexusSecret.secretKeyfile` parameter found in the [Helm chart repository README](https://github.com/sonatype/nxrm3-ha-repository/blob/main/nxrm-ha/README.md#configuration) .
- Those using AWS Secrets Manager or Azure Key Vault need to include the secret in AWS Secrets Manager/Azure Key Vault. See the [Helm chart repository README](https://github.com/sonatype/nxrm3-ha-repository/blob/main/nxrm-ha/README.md#configuration) for details.

### Set the Active Encryption Key

Use the following API call to trigger a task to re-encrypt existing secrets using your custom encryption key.

`/service/rest/v1/secrets/encryption/re-encrypt`

The request body includes the following parameters:

- `secretKeyId` - The ID of the new encryption key as it appears in the secrets file.
- `notifyEmail` (Optional) - An email address to receive a notification about the task result (requires email service configuration).

A successful request schedules a re-encryption task with the task ID in the response body.

```
curl -u "admin" -X 'PUT' \
  'https://<your-instance-url>/service/rest/v1/secrets/encryption/re-encrypt' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "secretKeyId": "string",
  "notifyEmail": "string"
}'
```

Interrupting the re-encryption task may leave secrets encrypted with the old key. Fix this by resending the API call and allowing the task to complete.

### High Availability (HA) Deployments

When using rolling restarts in an HA cluster, temporarily set the `active` key to `null` for the first restart. This is necessary as the nodes do not have access to the new key until they are restarted. The secrets file must be accessible by the nodes or the re-encryption task fails.

This allows the nodes to come up with the new secrets file without attempting to use an inactive key. Once all nodes are up, activate the new key using the API, and update your secrets file to reflect this change for subsequent restarts.

## Repository Management

Repositories are containers that hold the components (i.e., artifacts, packages, etc). Managing repositories is an essential part of your Nexus Repository configuration. Nexus Repository supports hosted, proxy and group repositories for the supported formats.

A user's ability to add, edit, or delete repositories is determined through the `repository-admin` privileges.

```
nx-repository-admin-*-*-*
nx-repository-admin-maven2-maven-central-browse
nx-repository-admin-maven2-maven-central-read
nx-repository-admin-maven2-maven-central-edit
nx-repository-admin-maven2-maven-central-delete
```

The Repositories view displays a list of configured repositories. Navigate to *Settings* → *Repository* → *Repositories*

The Repositories view lists the following information about each repository:

- Unique repository name
- The estimated storage consumption of the repository calculated when adding up the size of artifacts stored in the database. Does not include the metadata files or indexes. This value is updated after 2 minutes when artifacts are update. See the Repository Size Calculation Performance Data documentation
- The repository's type (i.e., proxy, hosted, or group)
- The language or ecosystem format that the repository uses to store and access components
- The blob store in which this repository stores its binary parts
- The repository's availability status
- The direct URL path to that repository; copy to use this URL to connect other tools to the repository
- Displays the repository health statistics or a button to start the analysis
- The count of components by their highest policy violation level, count of quarantined components, and a link to the results on the Repository Firewall service.

### Repository States

These are the possible states of a repository's availability status.

- The online checkbox is checked in the group or hosted repository's settings
- The repository's settings does not have the online checkbox enabled.

- A new proxy repository that is not yet initialized.
- The proxy repository is ready to connect to remote.
- The proxy repository has made successful requests to the remote.
- The proxy repository's "blocked" configuration is set to not send requests to the remote repository.
- The proxy repository is not sending requests as auto-blocking is configured and the remote repository is unreachable.
- The repository is not configured to autoblock requests however the remote repository is unreachable.
- The repository's settings does not have the online checkbox enabled.

### Repository Types

Sonatype Nexus Repository supports hosted, proxy, and group repositories. The sections below provide information about each of these repository types.

### Creating Repositories

To create a new repository in Nexus Repository, you require the following privileges:

- To add a new repository
- To view repositories (including the newly added ones)

To create a new repository, take the following steps:

### Configurable Repository Fields

The sections below provide details on different configurations you can make when you create a new repository or open an existing repository's management view (i.e. when you select it from the list of created repositories).

Available configurations vary depending on repository type and format.

- The *Name* is the identifier that will be used in the URL for access to the repository. For example, the proxy repository for the Central Repository is named "maven-central." The *Name* must be unique in a given Nexus Repository instance and is required.
- A repository's format is the format in which Nexus Repository exposes the repository to external tools. Examples include docker, npm, go, pypi, etc. See the Formats documentation
- The repository type field indicates whether this is a hosted, proxy, or group repository. See the Repository Types section
- The *URL* field displays the user-facing URL for this repository. Maven and other tools can access the repository directly at that URL (e.g., `http://localhost:8081/repository/maven-central` ).
- The *Online* checkbox allows you to define whether or not a given repository is available to client-side tools. Check the checkbox to make the repository available; de-select the checkbox to make it unavailable.
- The *Blob store* field indicates which blob store among your available blob stores this repository will use to store its binary parts. See the Storage Guide documentation
- When the *Strict Content Type Validation* checkbox is checked, validation will check that the MIME type of all files published into the repository conforms to the allowed types for that specific repository format.
- Cleanup policies control disk space by removing unused items. Nexus Repository applies the selected cleanup policies to the repository to delete components that match the criteria. Use the arrow controls to associate one or more cleanup policies to the applied section. See the Cleanup Policies documentation
- Controls how the repository allows or disallows component deployment in hosted repositories. **Disable redeploy** (default value) - A client can only deploy a particular component once; any attempt to deploy a component again will result in an error. **Allow redeploy** - Clients can deploy components to this repository and overwrite the same component in subsequent deployments. **Read-only** - No deployment allowed.
- **Disable redeploy** (default value) - A client can only deploy a particular component once; any attempt to deploy a component again will result in an error.
- **Allow redeploy** - Clients can deploy components to this repository and overwrite the same component in subsequent deployments.
- **Read-only** - No deployment allowed.
- The Remote Storage field is only available for proxy repositories. This field contains the URL for the remote repository that this repository will proxy. As a best practice, avoid proxying remote repository groups as this can impact performance optimization. Instead, create multiple proxy repositories that each proxy the different hosted repositories that make up the group instead of proxying the group itself.
- Available for proxy repositories that use an HTTPS URL. When enabled, Nexus Repository manages the remote repository's SSL certificate. Select the *View certificate* button to view SSL certificate details and, optionally, add or remove the certificate from the truststore that Nexus Repository maintains. See the Outbound SSL - Trusting SSL Certificates of Remote Repositories section
- The *Blocked* checkbox configuration is only available for proxy repositories. Check this box to prevent Nexus Repository from sending outbound requests to the remote repository.
- The *auto-blocking enabled* field is only available for proxy repositories. When enabled, Nexus Repository automatically blocks the proxy repository if the remote repository becomes unavailable. While a proxy repository is blocked, components will still be served to clients from a local cache, but Nexus Repository will not attempt to locate a component in a remote repository. Nexus Repository periodically retests the remote repository and unblocks the proxy once the remote becomes available.
- *Maximum component age* is only applicable for proxy repositories. When the server receives a request for a component, the remote repository is not checked for a modified version of the component until the cached component is older than the number of minutes configured in this field. The default value of 1440 ensures that new version information is updated daily. In most cases, components are considered immutable and should not change. Setting the value to -1 to disable checking the remote repository for redeployed components. A value of 0 forces a check for changes on every request.
- *Maximum metadata age* is only available for proxy repositories. Nexus Repository will only retrieve metadata updates from the remote repository after the number of minutes configured in this field. For component metadata, Nexus Repository honors whichever value between *Maximum component age* and *Maximum metadata age* is greater before rechecking.
- The *Not found cache enabled* checkbox and *Not found cache TTL* (Time-to-Live) fields sets the number of minutes (1440 minutes or 24 hours by default) Nexus Repository will cache this result before attempting another request for the missing component. Public proxy repositories respond with the HTTP status code " `404 Not Found` " when their index does not contain the requested component at the time of the request. Nexus Repository should be configured to cache these results rather than spamming repeating requests for the missing components. This limits outgoing traffic to the remote and protects subsequent requests from being rate limited or blocked by the public repository. Review the proxy repository's policies when adjusting from the default value. You may adjust the default to a lower value when new versions are frequently published to the remote proxy. This can be useful for when proxying remote Nexus Repository instances managed by your organization. Disabling the cache checks the upstream repository every time a request is made and will impact performance.
- The HTTP configuration section is only available for proxy repositories. In this section, you can configure access to the remote repository either via providing authentication details or connecting to a proxy server. This configuration is only necessary if it is specific to this repository. See the HTTP and HTTPS Request and Proxy Settings documentation In the *HTTP Authentication* section, select *Username* or *Windows NTLM* as the *Authentication type* . Then, provide the required *Username* and *Password* for plain authentication or *Username* , *Password* , *Windows NTLM* *hostname* ,and *Windows NTLM domain* for Windows NTLM-based authentication.
- The *HTTP request settings* section is only available for proxy repositories. Changes made to *HTTP request settings* are applied to all HTTP requests that Nexus Repository makes to the remote repository being proxied. Enabling these settings at the repository level will override any general settings. See the HTTP and HTTPS Request and Proxy Settings documentation You can make the following configurations to HTTP request settings: *User-agent customization* - Enter a string to append to user-agent HTTP headers. *Connection retries* - Enter the total number of connection attempts after an initial timeout. *Connection timeout* - Set the timeout interval (in seconds) for requests. *Enable circular redirects* - Allow proxy repositories to follow redirects indicated by the remote server even if they point to an already processed URL. *Enable cookies* - Authorize using HTTP cookies sent by the remote server when processing future requests. `` is a server that requires both *Enable circular redirects* and *Enable cookies* . When requesting data, you are redirected to a queue of different URLs; most of these are involved with authentication. By enabling these options, you allow Nexus Repository to maintain the authentication state in a cookie that would be sent with each request, eliminating the need for authentication-related redirects and avoiding timeouts.
- *User-agent customization* - Enter a string to append to user-agent HTTP headers.
- *Connection retries* - Enter the total number of connection attempts after an initial timeout.
- *Connection timeout* - Set the timeout interval (in seconds) for requests.
- *Enable circular redirects* - Allow proxy repositories to follow redirects indicated by the remote server even if they point to an already processed URL.
- *Enable cookies* - Authorize using HTTP cookies sent by the remote server when processing future requests.
- The Proprietary Components field is only available for hosted repositories and requires integration with Sonatype Repository Firewall. Checking this box tells Nexus Repository and Repository Firewall that components in this repository should be considered as proprietary for namespace conflict attacks. If you are unsure if your repository contains public open-source components, do not enable this feature. See [Namespace Confusion Protection](https://help.sonatype.com/en/namespace-confusion-protection.html)
- The *Group* section and *Member Repositories* configuration are only available for group repositories. The *Member Repositories* selector allows you to add and remove repositories to and from the repository group. The *Members* column lists all of the group member repositories. The *Available* column lists all repositories and repository groups that you could potentially add to the group. To add or remove a repository to the group, either drag the repository from whichever column it is into the new column in which you want it to appear, or select the repository and use the arrows that appear between the two columns to move the repository. The order of the repositories listed in the *Member* section is important. When Nexus Repository searches for a component in a repository group, it will return the first match. To reorder a repository in this list, click and drag the repositories and groups in the *Members* list or use the arrow buttons between the *Available* and *Members* list. The order of repositories or other groups in a group can be used to influence the effective metadata that will be retrieved from a repository group. It is recommended best practice to put hosted repositories higher in the list than proxy repositories. For proxy repositories, Nexus Repository may need to check the remote repository, which will incur more overhead than a hosted repository lookup. It is also recommended to place repositories with a higher probability of matching the majority of components higher in this list for best performance. These best practices are implemented in the default configuration.

### Buttons for Managing an Existing Repository in Nexus Repository

Within an individual repository or repository group's administration screen, you can use buttons to perform a few different actions related to the repository's cache and search index. To locate the buttons described in the sections below, select a specific repository from the list under *Settings* → *Repository* → *Repositories* .

### Configure Blob Stores

The components in a repository are stored in blob stores.

### Data Store

Administrators using Nexus Repository see a *Data Store* option in the user interface at *Settings → Repository → Data Store* . This screen contains information about your H2 or PostgreSQL database connection.

Nexus Repository users that have migrated away from the legacy OrientDB database can determine their current database by checking the *JDBC URL* displayed on the *Data Store* configuration screen:

- If the *JDBC URL* references H2, then you are using an H2 database.
- If the *JDBC URL* does not reference H2, then you are using a PostgreSQL database.

### Cleanup Policies

Cleanup Policies are the automation rules for removing content stored in repositories of your Nexus Repository. The quantity of components quickly grows over time without reducing the number of components at the same rate as they are being added to the Nexus Repository.

This adds risk to your deployment when not managed early:

- Increasing storage costs
- Impact on performance
- Finding components is challenging when sorting through old artifacts
- Risk to production with potentially vulnerable artifacts available

**Note:** Cleanup Policies and Tasks are not configured by default. Define the policies that best suit your development lifecycle.

### Routing Rules

Administrators want to control the remote traffic to upstream repositories to limit the exposure from those repositories. This could be to limit the access to a single component's versions or to a specific namespace within that repository. Routing Rules are used to limit access to remote proxies to the namespaces for the components needed from that repository.

Steps to setting up a routing rule:

- Create a block or allow a routing rule
- Apply the routing rule to the proxy repository

### Repository Health Check

Repository Health Check (RHC) allows Nexus Repository users to identify risks using open-source components currently found in their proxy repositories. Limiting the impact of open-source risk at the earliest stages is key to reducing rework and protecting your DevOps pipeline from bad actors.

### Content Replication

**Note:** Only available in Sonatype Nexus Repository TM Pro. Interested in a free trial? [Start here](https://www.sonatype.com/products/repository-pro/trial) .

Publish artifacts to one Nexus Repository instance and have other instances pre-fetch them through a standard proxy repository. This provides faster artifact availability across distributed teams.

This design lets you move large binaries to remote distribution instances before users request them. This reduces latency by eliminating the time your builds need to wait for the latest binaries to be available across your organization.

Use content replication to:

- Update multiple distribution services all proxying the primary development source
- Set up bi-directional replication of content between two development teams
- Replicate a subset of content for a particular audience

### Repository Replication (Legacy)

**Note:** Only available in Sonatype Nexus Repository TM Pro. Interested in a free trial? [Start here](https://www.sonatype.com/products/repository-pro/trial) .

⚠️ **Warning:** In release 3.48.0, we introduced Content Replication, which removes Replicator and makes replication easier to set up and deploy. This documentation remains available for current implementations only. We do not recommend implementing this version of replication as we will be completely removing it once the new replication design is available.

**Note:** Replication is not appropriate for disaster recovery. If you need a disaster recovery solution, please see our resilient deployment options and backup and restore procedures documentation.

## Retry Limit Configuration

### Introduction

The following system properties and JMX bean are provided to allow the user to control when and how often retrys occur for storage transactions.

### System Properties

The following system properties can be used to control when and how often a retry occurs:

```
nexus.tx.retry.limit=8            # maximum times a transaction can retry
nexus.tx.retry.minSlots=2         # minimum number of backoff slots
nexus.tx.retry.maxSlots=256       # maximum number of backoff slots
nexus.tx.retry.minorDelay=10ms    # per-slot delay if it's a minor exception
nexus.tx.retry.majorDelay=100ms   # per-slot delay if it's a major exception

# comma-separated list of exceptions to treat as "major"
nexus.tx.retry.majorExceptionFilter=\
  java.io.IOException,org.sonatype.nexus.repository.storage.MissingBlobException

# comma-separated list of exceptions to treat as "noisy" - these exceptions won't contribute to the excessive retry metrics
nexus.tx.retry.noisyExceptionFilter=\
  org.sonatype.nexus.repository.browse.internal.orient.BrowseNodeCollisionException
```

`IOExceptions` and `MissingBlobExceptions` are treated as major exceptions which result in longer backoff delays before retrying. This is because these exceptions are often related to slower (networked) storage which works best with a longer delay before retrying. When running in HA-C various distributed exceptions are also listed as major for the same reason.

### RetryControllerBean

![28345110.png](/docs-at-surgery-poc/assets/images/uuid-f137686a-e29f-847c-5586-9795303d4e81.png)

This JMX bean can be used to tune the retry settings at runtime without rebooting.

### References

- [https://en.wikipedia.org/wiki/Exponential_backoff](https://en.wikipedia.org/wiki/Exponential_backoff)

## Staging

**Note:** Only available in Sonatype Nexus Repository TM Pro. Interested in a free trial? [Start here](https://www.sonatype.com/products/repository-pro/trial) .

In modern software development, it is imperative to thoroughly test the software before deploying it to a production system or externally accessible repository. Most commonly, developers will first deploy a release candidate to a staging system that is a close copy of the production system; here, it will undergo a series of rigorous tests before it is either promoted to production or returned to development.

The staging functionality in Nexus Repository facilitates this process by allowing you to move components between repositories. This allows you to create isolated release candidates that you can then discard or promote as needed to support the decisions that go into certifying a release.

Staging allows your organization to have some sequence of hosted repositories and move or promote components through those repositories under your delivery or code promotion process.

Other features of staging in Nexus Repository let you do the following:

- Avoid exposing your entire organization to untested components.
- Identify a batch of components as a “build.”
- Track build status from development to production.
- Apply rules to builds (e.g., no SNAPSHOT dependencies).
- Control build visibility based on status.

Staging can also answer the question of “What made it to production?” This lets you create isolated release candidates that can be promoted or discarded in support of certifying a release.

### Building Blocks

Staging comprises three basic building blocks:

- Upload components/assets to hosted repositories; you can then promote/move them to other hosted repositories or delete them as required.
- Tag uploaded components/assets so that you can identify them as a logical group and transfer them together. See the Tagging documentation
- Used to move and delete components between hosted repositories.

### Limitations

Staging has the following limitations:

- Staging is supported with the following hosted repositories:
- You can only transfer between repositories of the same version policy; you cannot transfer from a snapshot repository to a release repository.
- Staging moves are not supported for hosted repositories that are configured as the writable member of a Docker group repository; attempting a move for a repository that is a writable member of a Docker group repository will result in an error. This limitation exists due to the way Docker image deployments work. Docker images are comprised of a tag, manifest(s), and layers. When using Docker group deployments, manifests and layers that already exist in any member of the group repository will not be uploaded to the target hosted repository. This happens because Docker clients always test to see if a file is present in the remote before uploading it. This makes it highly likely that some of the uploaded image files will be present in proxy repositories within the group or in other repositories that were not included in the tagging command. Attempting a staging move on an image that has either of these problems will fail. See the Pushing Images to a Group Repository section for more information on writable repositories.
- This limitation exists due to the way Docker image deployments work. Docker images are comprised of a tag, manifest(s), and layers. When using Docker group deployments, manifests and layers that already exist in any member of the group repository will not be uploaded to the target hosted repository. This happens because Docker clients always test to see if a file is present in the remote before uploading it. This makes it highly likely that some of the uploaded image files will be present in proxy repositories within the group or in other repositories that were not included in the tagging command. Attempting a staging move on an image that has either of these problems will fail.
- See the Pushing Images to a Group Repository section for more information on writable repositories.
- To perform a staging move, a user needs the following privileges:

### Workflow

As depicted in the figure below, a typical staging workflow involves hosted repositories, group repositories to include other dependencies and an external system that coordinates the promotion process. This usually includes a continuous integration (CI) system (e.g., Jenkins) that continuously builds each commit and a release manager that promotes builds for testing and release.

The sections below detail each phase of the process as illustrated above.

### REST Endpoints

### Staging Concepts

Staging is a simple but powerful feature in Nexus Repository that lets you move artifacts from one repository to another using API calls from your CI/CD tools. You can use this to build workflows with quality checks so artifacts are not used before they are ready.

Staging has a powerful connection with other features such as Cleanup Policies; helping you keep your build pipelines lean and light on storage space. Maturing into using Staging may lead to a fair amount of rework. This guide reviews the concept of staging, how to set up a basic staging workflow, and the steps to migrate legacy environments.

Here are some quick benefits of Staging:

- Repository endpoints at each stage in the pipeline
- Artifacts are not copied or duplicated
- Everything is a potential release candidate
- Promotion workflow is driven by CI
- Cleanup can be more aggressive when based on development stages

## Support Features

Nexus Repository has features to manage and monitor your server and are useful for troubleshooting and support activities. Support features are available in the Support view of the Settings menu.

![nx-support-zip.png]({{ /assets/images/uuid-7dec5f61-d5f0-1b0c-b56d-161493fb094f.png)

### Support ZIP

Administrators may produce a support zip by navigating to *Settings* → *Support* → *Support Zip* . Submit the generated ZIP archive file to Sonatype support by email or attach it to a support ticket.

Sensitive password-related information is removed from the generated files. You are prompted to verify your repository manager account credentials when generating the support zip.

### Status Checks

Status Checks provide the health status information for the instance or the nodes in the high availability cluster.

Access this screen by selecting the health status icon in the main header. The menu icon reflects the current status of the system, though it may take a few minutes for the icon to change after an issue is fixed.

- A green circle is shown when the system is healthy.
- A red "X" is shown when there are status issues to examine.

### System Information

System Information displays configuration details for the Nexus Repository server. Use the drop-down menu at the top of the screen to select a specific node when clustering is enabled.

This view is available with the `nx-atlas` privilege. Select `Download as JSON` to retrieve a JSON-formatted text file.

![nx-support-information.png](/docs-at-surgery-poc/assets/images/uuid-c3e8dbec-1414-7761-0aff-40955bf239ad.png)

System information includes the following:

- The Nexus Repository version
- Installed plugins
- Install and work directory location
- Application host and port
- System properties known by the Java Virtual Machine
- Operating system
- Environment variables
- Runtime details

### Logging

Effective logging is critical for monitoring the health, security, and performance of your Nexus Repository deployment. Nexus Repository internally leverages Logback, a powerful and flexible logging framework for Java applications, enabling detailed control and management of logging behaviors.

Logging in Nexus Repository is manage using the configuration files as well as setting the logging levels in from the user interface. High availability and resilient deployment may have additional logging configuration depending on your reference architecture.

### Prometheus

Nexus Repository exports its metrics in Prometheus format at `/service/metrics/prometheus` and requires Application privilege for Domain *metrics* and action *read* (or use existing *nx-metrics-all* privilege) to access it. To consume those metrics you need to [configure your Prometheus](https://prometheus.io/docs/concepts/jobs_instances/) to scrape the data from Nexus Repository. For your convenience, we have provided an example Prometheus YAML file below that you can pass to Prometheus (remember to edit the target to point to your Nexus Repository instance; we used `host.docker.internal:8081` ). Once you've got your Prometheus running, verify connectivity between Prometheus and Nexus Repository at `http://your-prometheus-server/targets` . You can stop here or you can go further and use Prometheus as a datasource for another tool like [Grafana](https://grafana.com/docs/grafana/latest/features/datasources/prometheus/) or [Elastic](https://www.elastic.co/what-is/prometheus-monitoring) .

## Tagging

**Note:** Only available in Sonatype Nexus Repository TM Pro. Interested in a free trial? [Start here](https://www.sonatype.com/products/repository-pro/trial) .

Available only in Nexus Repository Pro, tagging provides the ability to mark a set of components with a tag so that they can be logically associated with each other. The most common scenarios for using tags include the following:

- A CI build ID for a project (e.g., project-abc-build-142).
- A higher-level release train is when you are coordinating multiple projects together as a single unit (e.g., release-train-13).

The Staging feature uses tagging extensively.

**Note:** Tags are applied at the component level and not to individual assets.

### Endpoints

Tagging capabilities are available via a REST API. Non-administrator users will need the respective *nx-tags* privileges to perform the curl.

### Security

Tagging is controlled by the following privileges.

For associate and disassociate, the respective user will also need the ability to browse the components, defined by the nx-repository-view browse privilege for the respective repository.

### Cleanup Task

Having a CI system automatically tag every build can result in an overabundance of tags. The *Admin - Cleanup tags* task allows administrators to delete tags based on the following criteria:

- Age (in days) of when the tag was first created (default is 0 days).
- Age (in days) of when the tag was last modified (default is 0 days).
- A regular expression on the tag name (e.g. project-abc-.*).

If an administrator selects multiple options, the tag must meet both criteria. Additionally, you can select to delete the components associated with the tag; this option can be restricted to a specific repository or format.

⚠️ **Warning:** In situations where a component has two associated tags and the tag cleanup task is configured to delete the components, the system will delete that component even when the cleanup task only matches on one of the tags. For example, if component A is tagged with build-123" and "dev-build-123 and the tag cleanup task is configured to clean up tag "dev-build-123" AND delete components associated with it, it will delete component A. The component also being tagged "build-123" will not prevent the deletion.

The task log for the *Admin - Cleanup tags* task contains a list of the deleted tags and components. See the task logging section on the System Configuration page for details.

### Best Practices

The following are some best practice recommendations for using tagging:

- Use short tag names and attributes to maximize the performance of tag-related operations and storage utilization. Maintaining a large number of tags with attributes of maximum allowable size (20k) could result in undesirable performance degradation.
- Proactively use the *Admin - Cleanup tags* task to clean up unused tags. The *Admin - Cleanup tags* task provides configuration options to support routine removal of aged or unused tags and the associated components (if desired).
- Use a tag naming scheme that will ensure the uniqueness of created tags and prevent naming collisions and potential interruptions to CI pipeline workflows.

## Tasks

As an administrator, you may schedule and execute maintenance tasks to automate repository management. Users with the `nexus-tasks` privilege may access this configuration.

### View Tasks

The tasks table shows the following columns:

- **Name** - A user-defined name to identify it in the user interface and log files.
- **Type** - The list of available task types is documented in more detail below.
- **Status** - Displays when a task is disabled, waiting for its next run, running, or the progress of the current run.
- **Schedule** - Displays when the task is configured to run.
- **Next run** - The date and time of the next execution are based on the schedule.
- **Last run and Last result** - The result of the last execution.

### Configure Tasks

Add new tasks by selecting "Create task " or edit existing ones. Custom fields are displayed for each task depending on the task type.

When creating or updating a scheduled task, configure the following default properties:

- **Task enabled** - Enable or disable the task
- **Notification Email** - Configure a notification email for the task execution
- **Notification Condition** - Send on Failure or either Success or Failure
- **Task frequency** - Configure the schedule for the task executions. Advanced (provide a CRON expression) follows the UNIX-style CRON syntax

### Task Logs

The output of every task run go to a separate log file that is configured to be removed after 30 days. These task logs are stored in the following task directory:

```
$data-dir/log/tasks
```

The file name of each task log is the task type followed by the date and time the task started. For example:

```
repository-maven.purge-unused-snapshots-20170618153235.log
```

The output of the task goes to the `nexus.log` and the specific task log. Some tasks only go to the `nexus.log` .

For long-running tasks, progress such as the number of items is logged to the `nexus.log` every 10 minutes.

### Types of Tasks

Tasks are prefixed to fall into the following category types:

- Tasks that include regular maintenance such as backing up the database and cleaning up artifacts through cleanup policies. These tasks are often scheduled to run regularly.
- Format-specific tasks are typically to repair metadata and indexes. Some tasks are used for format-specific cleanup tasks which are scheduled regularly.
- Tasks with the " `Repair` " prefix are only intended to be run manually when encountering specific issues with your system. **Only run these tasks at the advice of a Sonatype staff member.**
- These tasks provide specific functionality such as import/export but include replication and some management tasks. These tasks may be scheduled depending on your use case. Here are some outliers:
- These tasks are for updating useful metrics available in the Repository user interface.

### Reconcile Component Database From Blob Store Task

This task recovers lost component metadata from a blob store when restoring from backup, and the database and blob storage are out of sync. When executed, the task searches the selected blob store for blobs missing their associated metadata. The component metadata is restored based on the information contained in the blob store.

The task handles the following two use cases in particular:

- If content exists in the blobstore but is missing from the restored database, the task will create metadata for that content.
- If the content exists in both the blobstore and the database but is marked soft deleted in the blobstore, the task can undelete the blobstore content.

The following matrix goes into more detail to describe case where the task does or does not have an effect:

If you attempt to use all three of the above options at once they will not all work. You can run "integrity check" and "un-delete referenced blobs" together, OR you can run "restore blob metadata" by itself.

### Change Repository Blob Store

The `Admin - Change repository blob store` task changes where components are stored by switching the configured blob store used by the repository. This task copies components from one blob store to another without interrupting the availability of the artifacts in the repository.

The task may take significant time to complete.

See the Change Repository Blob Store Performance Testing documentation

**Note:** Only available in Sonatype Nexus Repository TM Pro. Interested in a free trial? [Start here](https://www.sonatype.com/products/repository-pro/trial) .

### Maven SNAPSHOT Tasks

### Repository Export

**Note:** Only available in Sonatype Nexus Repository TM Pro. Interested in a free trial? [Start here](https://www.sonatype.com/products/repository-pro/trial) .

The `Repository - Export assets` task exports content from a selected repository into a file directory. The content of this export may be imported to another repository instance.

### Repository Import

**Note:** Only available in Sonatype Nexus Repository TM Pro. Interested in a free trial? [Start here](https://www.sonatype.com/products/repository-pro/trial) .

The `Repository - Import external files` task takes content from a directory on the server and imports it into a repository in Nexus Repository. This allows you to bring external content into a repository from any source.

## Usage Metrics

Usage metrics are display for administrators on their home screens after logging into the user interface. Depending on what Nexus Repository edition you are using, you will see the information below defining usage in the Usage Center. Usage metrics take up to an hour to update after making changes to your usage. Monthly requests are updated once a day.

![nx-usage-center.png](/docs-at-surgery-poc/assets/images/uuid-3185ba3d-aea8-d485-dceb-e025ee6d2b9b.png)

### Requests Used to Calculate Metrics

For the purpose of counting usage analytics, Nexus Repository tracks and counts HTTP requests that are directed towards `repository` endpoints. An HTTP requests are a standard web-based communication initiated either by a client application communicating with Nexus Repository or by itself when interacting with an upstream repository.

Repository endpoint example:

```
https://nexus.example/repository/maven-public/
```

The total requests outnumber the total number of components as multiple requests may be made for a single component request. What qualifies as a request falls under a range of operations:

- When requesting a component from a proxy the first time, Nexus Repository needs to first make a request to the external proxy for the component. Requests for metadata files such as maven-metadata.xml, package.json data, and Docker manifests, which are often prerequisite to artifact downloads.
- This includes binary files like Maven JARs, Docker image layers, and npm package tarballs. Docker layers are a good example of a component or image that is made of many files for a single component. A single docker pull command translates into multiple HTTP requests: one for the authentication token, one or more for manifests, and then a pair of HEAD/GET requests for each unique layer blob. Given that Docker images are composed of numerous layers, a single image pull can readily involve a dozen or more distinct HTTP requests.
- When your clients publish new components to hosted repositories. This includes multiple items such as the package and updates to the metadata files for the repository.
- Most client tools use the direct URL path when downloading components. Some processes may use API calls to provide this function. Calls that target a particular repository path, such as searches and browsing are counted as requests.

### Pro Usage Metrics

Nexus Repository Pro instances not subject to hard limits see a simplified version of the usage metrics different from the Community Edition users.

![nx-usage-center-pro.png]({{ /assets/images/uuid-e1c1f81e-f342-e3c0-a08e-1ed3924b3e68.png)

### Component Metrics

The first panel of usage metrics displays information about the components in your deployment.

### Request Metrics

The second panel of usage metrics displays various information about HTTP requests in your deployment.

### Requests Per Month Metrics

The third panel of usage metrics displays requests per month for your deployment. Calculations are based on UTC time.

### Additional Metrics for Nexus Repository Cloud

The data for Nexus Repository Cloud metrics are coming from CloudWatch. Detailed usage by month can be found on the license management historical usage view.

See the Historical Metrics section on the license management page.

![nx-cloud-usage-metrics.png](/docs-at-surgery-poc/assets/images/uuid-de81f7b3-bc01-32ce-8685-f4549e9b91c0.png)

### Deprecated Metrics

The following metrics have been removed as of the Nexus Repository 3.79.0 release.

### Usage Center

The Usage Center provides administrators insight into their deployment’s scale to help know when to review your deployment model. The architecture deployments provided for Nexus Repository are designed to provide verified and tested performance and stability for your deployment depending on your usage.

See the Reference Architectures documentation

- Usage metrics takes up to an hour to update as counts are not live. Monthly requests are updated once a day.
- Nexus Repository Pro instances not subject to hard limits see a simplified version of the usage metrics.

![nx-usage-center.png]({{ /assets/images/uuid-3185ba3d-aea8-d485-dceb-e025ee6d2b9b.png)

### How Components are Defined within Nexus Repository

Sonatype Nexus Repository supports many repository formats; this topic provides detail on how Nexus Repository counts components for each ecosystem. This information is crucial to understanding the component counts visible in your Nexus Repository usage metrics.

**Note:** In Nexus Repository, a component typically refers to a unique package or module and its associated metadata. For most formats, this corresponds to a single file or group of related files.

### Understanding Your Usage

As software development is mission-critical to business operations, ensure your Nexus Repository is deployed appropriately for your scale. The usage metrics alert administrators to when it’s time to review their deployment model.

See the Usage Metrics documentation to learn how these are calculated.

**Note:** The ** is removed in Nexus Repository 3.77.0 in favour of a Status Check to inform when Pro users are over the recommended usage for their deployed database. See the Soft Limits Metrics in the Status Checks section for details.

- While embedded databases are appropriate for disposable edge caches, test deployments, and low-concurrency team usage, an external PostgreSQL is recommended for more demanding use. This is particularly true for higher-concurrency use, or in any situation where Nexus Repository is the system of record for the components that it stores. Concurrent loads lead to data integrity problems in OrientDB. Embedded databases require the system to enter read-only mode to get a consistent backup. Many deployments are not properly backed up, leading to extremely long recovery times in the case of an outage that requires restoring data. To determine an appropriate deployment model, we’ve created reference architectures providing the deployment recommendations for ranges of anticipated load. Review the sizing instructions to evaluate your projected load.
- Concurrent loads lead to data integrity problems in OrientDB.
- Embedded databases require the system to enter read-only mode to get a consistent backup. Many deployments are not properly backed up, leading to extremely long recovery times in the case of an outage that requires restoring data.
- If you are seeing usage alerts in your deployment, your scale is exceeding what is appropriate for your deployment. Contact the [Sonatype Sales team](https://www.sonatype.com/products/sonatype-nexus-repo/oss-upgrade?utm_campaign=Product Help Pages&utm_source=help doc&utm_medium=contact us link&utm_content=product-help-next-steps) to upgrade to a Nexus Repository Pro deployment.
- Nexus Repository Pro deployments using an embedded database will see usage alerts when your scale exceed what is appropriate for your deployment. See the Resilient Deployments documentation for recommendations.
- For deployments of Nexus Repository that use an embedded database (OrientDB or H2), in-product warnings appear when usage levels approach or exceed one of the following thresholds:
- When changing your deployment model is not possible, we recommend evaluating ways to reduce your usage to keep your deployment stable. Reducing build frequency reduces the concurrency of request rates. Cleanup policies reduce your component count by eliminating components no longer needed. See the Cleanup Policies documentation Separate your build infrastructure from your distribution method using component replication. See the Scaling with Proxy Nodes documentation.
- Reducing build frequency reduces the concurrency of request rates.
- Cleanup policies reduce your component count by eliminating components no longer needed. See the Cleanup Policies documentation
- Separate your build infrastructure from your distribution method using component replication. See the Scaling with Proxy Nodes documentation.

## User Authentication

Nexus Repository includes a user management system and integrations with several external authentication sources. Configure the available authentication methods using Security Realms.

User access is managed through roles assigned with specified privileges as explained in the Access Control section.

### Authentication Methods

**Note:** SCIM Not Supported Direct System for Cross-domain Identity Management (SCIM) is not currently supported. User provisioning and deprovisioning data (e.g., user creation, deletion, group membership changes) are not automatically synchronized between your identity provider and Nexus Repository. While SSO handles authentication flow, changes to user identity data within your identity provider are not automatically reflect within Nexus Repository. Manual user management or custom API integrations are required for comprehensive user lifecycle management.

### Realms

Realms define a Nexus Repository user's authentication source. To manage realms, the user requires the `nx-settings` privilege. Manage realms under the *Settings* , *Security* view.

![nx-security-realms-view.png](/docs-at-surgery-poc/assets/images/uuid-2ff1d297-749f-2cbf-5ec2-cd3ef4398722.png)

- Nexus Repository requires multiple security realms for identifying users. Do not remove all realms from the *Active* section as this prevents access to Nexus Repository for all users, including administrators.
- Activate a security realm by adding it to the Active list in the right-hand column.
- Prioritize a realm by moving it higher or lower on the list using the up and down arrows available next to each active realm. The order in which you have your active realms determines what authentication realm is given priority for granting a user access in the event of a name clash between authentication realms.
- You must select Save to preserve changes.

### Anonymous Access

Unauthenticated users accessing the user interface or downloading components falls under the anonymous user profile.

Read our Access Control Best Practices before configuring the anonymous user profile and role.

### Local Authentication

While it is generally recommended to use a centralized authentication provider such as LDAP, SAML or Crowd, Nexus Repository Manager does include support for managing users. This can be accomplished both through the user interface as well as the REST API.

### LDAP

Nexus Repository uses the Lightweight Directory Access Protocol (LDAP) for authentication with external systems. Nexus Repository roles may also be mapped to LDAP user groups to grant authorization to members of the LDAP group.

Permissions to view and edit LDAP configurations are granted by the *nx-ldap-all* privilege.

Configuring LDAP is done with a few steps:

Nexus Repository maintains a local cache of authentication information to reducing server to server requests and supports multiple LDAP servers and user/group mappings.

### SAML

**Note:** Only available in Sonatype Nexus Repository TM Pro. Interested in a free trial? [Start here](https://www.sonatype.com/products/repository-pro/trial) .

Check out the following related support articles:

- [Keycloak SAML Integration with Nexus Applications](https://support.sonatype.com/hc/en-us/articles/1500000976522-Keycloak-SAML-integration-with-Nexus-Applications)
- [Azure AD SAML Integration with Nexus Applications](https://support.sonatype.com/hc/en-us/articles/4402929272851-Azure-AD-SAML-Integration-with-Nexus-Applications)
- [Okta SAML Integration with Nexus Applications](https://support.sonatype.com/hc/en-us/articles/1500001294962-Okta-SAML-integration-with-Nexus-Applications)
- [Auth0 SAML Integration with Nexus Applications](https://support.sonatype.com/hc/en-us/articles/360052183713-Auth0-SAML-integration-with-Nexus-Applications)

You can configure your instance to work with a SAML Identity Provider for authentication via Single Sign-On (SSO) and to send user groups to it for authorization. Nexus Repository implements the Web Browser SSO Profile from the [SAML 2.0 specification](http://docs.oasis-open.org/security/saml/v2.0/) . Supported bindings for sign-on are HTTP-POST (the default) and HTTP-Redirect for requests to the Identity Provider and HTTP-POST binding for responses from the Identity Provider. The Basic Attribute Profile is used for retrieving further information regarding the subjects and supported attributes are explained in the SAML Configuration Details section.

**Note:** SAML provides access to the UI. For clients that don't support SSO, Nexus Repository can generate user tokens, which can be used instead of a user name and password for basic authentication or to make REST API calls.

### Authentication via Remote User Token

Nexus Repository's *Rut Auth* capability allows authentication using an external security systems that passes along user details via HTTP headers for all requests to the Nexus Repository. This is a communication method common in authentication systems which share a single trust authority rather than managing the authorization separately in every tool. When the external system passes a value through the header, Nexus Repository grants authentication, and the value is used as the username for the authorization.

This model is common in authentication systems such as:

- Public Key Infrastructure (PKI)
- Central Authentication Systems (CAS)
- Single Sign-On (SSO)

Users log in to the environment through a central login page that propagates the login status via HTTP headers. A reverse proxy server (e.g., [Apache HTTPD](http://httpd.apache.org/) or [nginx](http://nginx.org/) ) can be used to perform this authentication and direct all communication with the Nexus Repository. The proxy server may defer this role to another authentication storage systems (e.g., via the [Kerberos](http://web.mit.edu/kerberos/) network authentication protocol).

![116230375.png]({{ /assets/images/uuid-2df08618-c978-a7a2-d5c0-ced924cf3bdd.png)

### Reset the Admin Password

Sonatype Nexus Repository 3 includes a default 'admin' Administrator user account. In cases where this password is lost or the account is disabled or removed, the following steps explain how to restore the default `admin` user account and set the password to `admin123` . We highly recommend logging in to change the password as the default credentials will leave the system unsecured.

Changing the admin account and password requires directly updating the Nexus Repository database so the process depends on the database.

### Atlassian Crowd Support

**Note:** Only available in Sonatype Nexus Repository TM Pro. Interested in a free trial? [Start here](https://www.sonatype.com/products/repository-pro/trial) .

Atlassian Crowd is a single sign-on and identity management product that many organizations use to consolidate user accounts and control which users and groups have access to which applications. Atlassian Crowd support is a feature preinstalled and ready to configure in Nexus Repository Manager Pro. Nexus Repository Manager contains a security realm that allows you to configure the repository manager to authenticate against an Atlassian Crowd instance.

⚠️ **Warning:** Using LDAP and Crowd Realms together in the repository manager may work, but this is not supported. If you already use LDAP support, we recommend adding your LDAP server as a Crowd directory accessible to the Crowd application instead of using both LDAP and Crowd realms in the repository manager.

### User Tokens

This topic covers how to use user tokens for user authentication in Nexus Repository.

**Note:** Only available in Sonatype Nexus Repository TM Pro. Interested in a free trial? [Start here](https://www.sonatype.com/products/repository-pro/trial) .

The user token feature establishes a two-part token for a user that the user can then use instead of providing a plain text username and password for authentication. User tokens provided added security beyond what reversible encryption provides and are especially useful when using single sign-on solutions like LDAP for authentication.

For example, when using Apache Maven with Nexus Repository, user credentials for accessing the repository manager must be stored in the user’s `settings.xml` file. While the Maven framework can encrypt passwords within the `settings.xml` , it must be reversible to be used, which results in limited security. Other build systems use similar approaches and can also benefit from using user tokens.

Note that, by default, the settings.xml file is available under `~/.m2/settings.xml` . This file contains listings for personalized clients or build-tool configurations, such as repositories. This file is not exclusive to Maven-specific repositories.

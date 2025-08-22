---
layout: default
title: "Managing"
parent: Sonatype Lifecycle
nav_order: 5
---

# Managing

Topics like user management and LDAP integration, organization management, application management, and policy management.

## Application Management

An application in Lifecycle is an open concept for what your organization needs to track using software composition analysis. This can be a monolithic application, a deployable container, a microservice, a manifest, or even just a folder of binaries. Often these are software projects in active development with development teams who own and can respond quickly to remediate discovered risk. Other times they are legacy projects that the organization needs to monitor while accepting existing risk. Here are some common strategies for creating applications.

- Software produced by a single team who own and maintain the dependencies
- The latest CI build of a project coming from a SCM repository
- Containers deployed in production where Continous Monitor watches for new risk

See

### Creating an Application

To create applications the user needs the `Edit IQ Elements` permission assigned to the organization where it is to be added.

- From Orgs and Policies, navigate to the Organization to add the application
- From the Applications header select `Add Application` indicated as a plus sign
- In the dialog, set the attributes: `Application Name` , `Application ID`
- Optionally select from options for an icon: `default` , `custom` , or `robot` . Custom icons should be in PNG format sized to about 160 x 160 pixels
- Custom icons should be in PNG format sized to about 160 x 160 pixels
- Select `Create`

The `Import Apps` option is for bulk onboard through your source control

![150406333.png](/docs-at-surgery-poc/assets/images/uuid-c8cbac46-dd90-71a0-dd80-55af01138841.png)

### Editing an Application

### Selecting an Application Contact

You can select a contact person for an application. The contact is displayed at the top of the application configuration, in the reporting area, and in the PDF version of the report. This is useful for others to find the point of contact for the application.

**Note:** SAML users must log in to Lifecycle at least once before the user and group appear in UI search results.

### Removing an Application Contact

To remove a contact:

### Copying the Application ID to Clipboard

CI integrations and other scanners use the Application ID to target the application during the analysis to scope the correct policy configuration and save the results. The Application ID is displayed in the parenthesis next to the application name and it can also be quickly copied to the clipboard from the `Actions` menu.

To copy the Application ID to the clipboard:

![iq-173-application-actions-menu](/docs-at-surgery-poc/assets/images/uuid-1c00eb1b-05f0-fd93-379d-09a4c5944754.png)

### Changing the Application ID

The Application ID is a unique identifier used by external tools to integrate with Lifecycle for evaluations. When changing the Application ID, you must also reconfigure the external tools so this is often best avoided. The only reason to do this is to maintain the application history and waivers while using the new identifier.

To change the Application ID for an application:

![Screenshot_2024-03-14_at_8_13_55_PM.png](/docs-at-surgery-poc/assets/images/uuid-5d186d2b-bea8-46b4-933a-78b8c4d3e235.png)

### Moving an Application

Applications inherit their policy configuration, notifications, and access controls from the organization they belong to. Waivers and other configurations are inherited from the organization.

Moving an application to another organization may result in a different effective policy set; potentially changing the violations in the scan report. Access may be open to new individuals or revoked from others.

During a move, Lifecycle compares these changes to inform the user below moving the application. The user must have the `Edit IQ elements` permission for the application as well as the `Add Applications` permission for the destination organization.

![iq-173-move-application-diaglog](/docs-at-surgery-poc/assets/images/uuid-790b17eb-8825-4798-33c4-28db9578c7f0.png)

### Deleting an Application

You may delete an application through the actions menu or with the Applications API.

![150406344.png](/docs-at-surgery-poc/assets/images/uuid-c69469e4-ce30-41ad-1e99-38dff0c2fd50.png)

### Automatic Applications

Lifecycle is most effective when performing application scans while building your application using the CI integrations or the Command Line Scanner (CLI). These tools associate the scan using the application's Public ID set when adding the application to Lifecycle.

To expedite the onboarding process, the automatic application configuration allows for applications to be automatically added when a Public ID new to Lifecycle is used for the first time. Applications are automatically added to a pre-selected organization to inherit policy configuration and access.

Optionally an Organization ID may be included in the scan to specify the organization to which the application will be added. The credentials used will need the Evaluate Applications permission assigned to the parent organization to add new applications.

See the [Sonatype CLI documentation](#UUID-6b69b7b1-858f-e58a-e010-beb4fdff9cdf_--organization-id) for details on including the Organization ID.

See also

### Automatic Source Control

### Manual Evaluation

The manual evaluation may be used to initially baseline your application or for testing scan results. The best approach however is to configure the scan to run during the CI build automatically.

To scan an application the user needs the `View IQ Elements` and `Evaluate Applications` permissions.

![Screenshot_2024-03-17_at_11_58_01_AM.png](/docs-at-surgery-poc/assets/images/uuid-90100b1e-cefd-ec0a-7331-33aa2e4e930c.png)

### Continuous Monitoring

Continuous Monitoring regularly checks the most recent scan of an application for new violations. Use this feature to send alerts when new violations have been discovered on existing application scans.

Enabling continuous monitoring requires first setting the stage that it should be run against and the notifications to send when a new policy violation occurs. Not setting a notification will still result in the violations being discovered, however they will not be known until someone consults the reports or dashboard.

Continuous Monitoring configuration uses inheritance and overrides when setting the stage it runs and notifications. The configuration may be set at any level though we recommend setting at the root organization.

## Organization Management

The Orgs and Policies view is designed to mimic your management hierarchy of your catalog of applications and business units.

### Hierarchy And Inheritance

Lifecycle uses a parent-child relationship when managing organizations and applications. Applications are 'children' of organizations and organizations are the 'children' of the root organization. This is referred to as the organizational hierarchy and is used for establishing ownership and inheritance.

Inheritance refers to re-using policy and configuration defined at a higher hierarchical level. A policy defined at the root organization will be inherited by all organizational levels. Policies defined on an organization will apply to the organizations and applications descendant from it.

As a best practice we recommend setting policy at the root organization level while using application categories and overrides to scope policies to the correct applications. Alternatively we recommend setting access controls to the organization level to limit access to only that which the users is a stakeholder of.

### Navigating the hierarchy

When you have view permissions, the configuration for the Root Organization is visible in the main section. Similarly, the drop down for `Organizations` lists the organizations your have permissions to view in Lifecycle.

- The listed organizations are the top-level organizations set up directly under the Root Organization.
- The number in parentheses () indicates the number of organizations and/or applications that are linked to this organization.
- Search for a specific organization or application by entering its name in the filter located at the top of the left navigation bar.

![150405751.png](/docs-at-surgery-poc/assets/images/uuid-4028f708-2758-c278-dea0-13327e88820c.png)

### Manage Organizations

You will need the `Edit IQ Elements` permission to manage organizations in Lifecycle. Organizations may be managed manually or using the .

## Policy Management

Governance Policies are the rules to identify risk from open-source components found in your applications. These policies report identified risk to each project stakeholder while enforcing compliance at any stage of the software development lifecycle. You will want governance policies in place before scanning applications to get a baseline of your open-source risk.

This is the goal of the Sonatype Reference Policy.

### Reference Policy

Creating an open-source governance policy is challenging which is why Sonatype provides a reference policy set for use as a starting point for baselining your open-source risk.

When launching Lifecycle for the first time, the Reference Policy is imported automatically from the Sonatype Data Services. Connectivity issues may result in the policies not loading so you may need to manually import the reference policy to your Root Organization.

See

### Policy Elements

### Policy Concepts

We’re often asked by customers and employees why we built Lifecycle as a policy engine. Wouldn’t it be simpler to just scan for security violations? It would, but it would be less useful than a comprehensive risk management tool like Lifecycle.

Understanding which open source components you’re using, the risk from those components, and determining an acceptable level of risk for your organization is vital to building a reliable software development process. Sonatype Lifecycle makes risk management simple by allowing your organization to define and automatically enforce specific policies for open-source components. This approach is flexible enough to fit in any software development process, scalable, and empowers developers to make decisions about components.

In this guide, we’ll discuss why Lifecycle’s ability to enforce policies in a context-sensitive way automatically is an effective method of managing risk in any organization.

### Reference Policies

The reference policy set may be downloaded and imported manually. This replaces the current policies without starting over with server configuration.

The following datatypes are included in the reference policy

```
policies, actions, notifications, labels (Application Categories), policyViolationGrandfatheringAllowed (Legacy Violations), licenseThreatGroups, tags (Component Labels),  policyTags
```

See this knowledge base article on [how to export policy](https://support.sonatype.com/hc/en-us/articles/360008133574-How-to-Export-Policy-from-IQ-Server) .

⚠️ **Warning:** **Importing the reference policy is destructive to existing data in Lifecycle.** Importing policies deletes the references for policy violations, waivers, application categories, component labels, legacy violations, notifications, actions, and license threat groups.

Importing policies requires the `Owner` role at the root organization.

- From the `Actions` menu, select `Import Policies`
- Select the `Choose File` button and select the `policy.json` file in the file browser
- Select the `Import`

### Configuring Policies

Policies can be created at multiple levels in the hierarchy.

- **Root Organization** - Policies at this level are inherited by all repositories, organizations, and applications. Use this level when you want to apply policies to every repository, application, and organization.
- **Organization** - Policies at this level are inherited by all applications attached to the organization. Use this level when you want to narrow the implementation of policies to a particular set of applications.
- **Application** - Policies at this level apply to an individual application only. Use this level when you want to apply policies to a single, unique application.
- **Repository Managers** - Policies applied to all repository managers. Use this level to scope policies for all your repository managers.
- **Repository Manager** - Policies applied to a specific repository manager. Use this level to apply policies to a specific repository manager.
- **Proxy Repository** - Policies applied to a specific proxy repository.

### Application Categories

Application Categories are used to differentiate applications by their intended environments or risk profiles for use in creating targeted policies.

Policies will not apply to every environment or application. For example, copyleft licenses only apply to applications that are distributed to other users whereas internal or server-based applications are not limited by this constraint. These license policies are scoped to only applications with the `Distributed` application category where other applications would not trigger these restrictions.

See Policy Management for details on scoping policies with Application Categories

### Component Labels

Component labels are metadata assigned to components for use when targeting specific attributes with policies. Rather than manually adding component coordinates when targeting specific components, generic component labels are used and applied to the components that meet the criteria.

For example, when the Application Architect wants to discontinue the use of a specific component, they apply a `Discontinue-Use` label to the component while making a policy to trigger for any components with that label.

### Continuous Monitoring

Continuous Monitoring regularly checks the most recent scan of an application for new violations. Use this feature to send alerts when new violations have been discovered on existing application scans.

Enabling continuous monitoring requires first setting the stage that it should be run against and the notifications to send when a new policy violation occurs. Not setting a notification will still result in the violations being discovered, however they will not be known until someone consults the reports or dashboard.

Continuous Monitoring configuration uses inheritance and overrides when setting the stage it runs and notifications. The configuration may be set at any level though we recommend setting at the root organization.

### Legacy Violations

To streamline the process of onboarding new applications with existing policy violations, the Legacy Violation feature allows you to defer policy violations to remediate later. When enabled for an application or an application's parent organization, eligible policy violations are be marked as Legacy Violations on the first evaluation of an application. Legacy Violations will not be treated as active violations, no notifications will be sent and Lifecycle will not take policy actions against them. If desired, these legacy violations can also be revoked to return to normal policy violation behavior.

### License Threat Groups

Licenses on open-source components declare obligations that the consumers of those components must follow. These obligations present different levels of risk depending on how the final application is deployed and distributed. License Threat Groups (LTG) categorize licenses by these obligations to allow organizations to manage licenses by the risk they present to the organization and how they are used in their applications.

Organizations manage their license policies by allocating licenses to the different threat groups rather than manually listing every license in the policy. Licenses Threat Groups in the provided reference policies are regularly audited by Sonatype's legal team to accurately allocate any newly discovered licenses into the correct buckets by reviewing all obligations associated with those licenses.

### Policy Actions

Policy actions allow you to designate an action to take when violations occur at a particular stage in the development lifecycle. For each stage, you can assign one of the following actions:

- *No Action* - This is the default setting.
- *Warn* - Policy violations are worthy of a warning.
- *Fail* - Policy violations are severe enough to potentially halt the development lifecycle.

If Sonatype Lifecycle is integrated with a third-party external tool, the action selected can have a direct effect on the tool. When an external tool requests a policy evaluation (of an application, repository, or component), IQ Server provides policy violation information along with the action, which the tool may (or may not) implement. For example, if you set the Build stage to Fail in a policy, a CI tool (such as Bamboo, Jenkins, or Hudson) may stop the build of an application when that policy is violated. Similarly, in a different tool, if you set a stage to Warn, a warning message may be displayed or logged in a file when policy violations occur. For more details on using actions, see [Usage Suggestions for Each Stage](#UUID-2edc9f20-6766-eb4b-2a06-786cd5985f0c_id_UnderstandingthePartsofaPolicy-UsageSuggestionsforEachStage) .

To add actions to a policy:

Actions at root organization or organization or application level

![137205678.png](/docs-at-surgery-poc/assets/images/uuid-9f371401-b8dd-9f08-dde3-d21ae38bbd70.png)

Actions at Repositories level

![153059906.png](/docs-at-surgery-poc/assets/images/uuid-dd0157eb-4606-bd37-893c-348ce230202b.png)

### Policy Constraints

Policy constraints define the violating conditions to detect during a policy evaluation. A policy is considered in violation when any constraint of the policy evaluates to a true statement.

- A policy must have at least one constraint and each constraint must have at least one condition.
- Policy constraints may be configured to satisfy any or all of their conditions.
- Policy constraints must have a unique name. These names are used as details for the policy violation.

![137205677.png](/docs-at-surgery-poc/assets/images/uuid-ddfd1734-f80d-22d6-99ce-e1ed41e97988.png)

### Policy Inheritance

The Inheritance setting is available only for organizations (including the Root organization). It allows you to specify how a policy is implemented when there are multiple applications attached to a specific organization. There are two choices:

- All Applications and Repositories - The policy is applied to every application and repository below this level of the hierarchy.
- Applications of the specified Application Categories in Root Organization/Organization - The policy is applied only to applications that have specific application categories assigned to them. With this setting, you select which application categories to use.

The latter choice lets you tailor the implementation of a policy to applications with similar characteristics by using application categories.

**Inheritance Overrides**

Checking these boxes allows you to override actions/notifications for this policy at lower levels.

![150406717.png](/docs-at-surgery-poc/assets/images/uuid-6c8975b5-ca1f-fc82-3edf-98120a49caa3.png)

### Policy Notifications

Policy notifications are email notifications that contain a summary of policy violations that occur during an application evaluation. These notifications can be delivered to email addresses. The emails are sent to individual addresses or users assigned to a particular role such as *Owner* or *Application Evaluator* .

Policy notifications are sent by email, regardless of the nature of the application evaluation, i.e.:

- Manual (using the *Evaluate a File* option from the UI)
- Automatic (via continuous monitoring)
- Automatic (using integration plugins like Sonatype Platform Plugin for Jenkins)

**When are notifications sent:**

Policy notifications are sent to email addresses, for all **new** policy violations that occurred since the last evaluation of the exact same application, at the exact same stage. If an application is being evaluated multiple times, and there are no **new** policy violations since the last scan, policy notifications will not be sent.

When you have a repository auditing setup, then policy notifications via email will be sent when a new component that violates policy enters your repository manager. The initial repository audit and re-evaluations of policies on repositories do not send notifications.

**Note:** Using Webhooks to Receive Violation Alerts You can also configure webhooks to receive violation alerts. Refer to [Lifecycle Webhook Event - Violation Alert](https://help.sonatype.com/en/lifecycle-webhooks-events-types.html#event---violation-alert) for more details on configuring webhooks for the *Violation Alert* event. The *Violation Alert* is triggered for every violation detected during an evaluation or subsequent re-evaluations. This behavior is different from the Policy Notifications (sent via email), which are only generated when there is a new policy violation which was not detected in previous scans.

**To set notifications in a policy:**

To remove a recipient, click on the delete icon.

Notifications at root organization or organization or application level

![137205716.png](/docs-at-surgery-poc/assets/images/uuid-081fadc8-dbc5-bd5b-d425-d2c7ce17714a.png)

Notifications at Repositories level

![153059911.png](/docs-at-surgery-poc/assets/images/uuid-5442b25a-2e0a-91e9-80d4-c163f5ada71c.png)

### Policy Overrides

The policy Inheritance Overrides feature allows you to override policy actions and notifications for inherited policies. This does not affect the policy actions/notifications defined at the parent level.

Users with the Edit IQ elements permissions may:

- Override Policy Actions
- Override Policy Notifications

Only policies that are specifically configured for an override at the parent level (org or application) allow the Actions/Notifications to be overridden at the child levels (inherited organizations or applications.)

## User Management

### Changing the Administrator Account Password

Lifecycle's default administrator account has the username *admin* and password *admin123.* You must change the default password.

**Note:** Any user, including an admin, can change their password following the instructions above. However, only an admin can reset a user’s password without knowledge of the current password.

### Creating a User

While we recommend using a security protocol such as LDAP for managing users and permissions, the IQ Server realm is still available for those who would like a lighter setup, where all users, groups and rights are stored directly in the IQ Server.

To create a new user in the IQ Server realm, follow the instructions below.

![82215548.png](/docs-at-surgery-poc/assets/images/uuid-08070df1-84cb-52d4-e30e-61567067ef7a.png)

### Editing and Deleting User Information

Editing user information is only available to an admin. The information that can be edited includes the first name, last name, email address and password. To edit an existing user, follow these steps:

![82215552.png]({{ "/assets/images/uuid-5e0ba967-be0b-86be-d38a-a435548743a5.png)

### LDAP Integration

Configure Lifecycle to work with an LDAP server for authenticating users and managing users and groups. This section assumes you are familiar with LDAP (Lightweight Directory Access Protocol), and have an LDAP server currently in use.

### Role Management

Roles provide sets of permissions that grant access to functionality in the user interface, through the integrations, and when using the REST APIs. Permissions are granted by assigning users or groups to the system roles or at the various levels in the organizational hierarchy: root organization, repository managers, organizations, and applications.

Roles are assigned to individual users or groups managed by your identity managing tools such as SAML or LDAP.

### Resetting the Admin Account Password and Roles

The default admin account password and roles may be reconfigured as follows:

The original admin account is recreated with the default username and password. This will revert the admin roles to the default state.

### SAML Integration

Use a SAML Identity Provider (IdP) for authentication through the Single Sign-On (SSO) protocol. IQ Server implements the web browser SSO profile from the SAML 2.0 specification.

Review [SAML 2.0 documentation from Wikipedia](https://en.wikipedia.org/wiki/SAML_2.0#Web_browser_SSO_profile) to learn more about the SAML 2.0 protocol.

### User Tokens

User tokens are internal and disposable credentials generated by IQ Server for use in Lifecycle Integrations without exposing the user's login credentials coming from the organization's identity provider. This is useful for accessing IQ Server integrations when identity providers, such as SAML, do not typically rely on usernames and passwords.

Using Tokens is highly recommended for IDEs and service accounts used in CI build scans as these temporary credentials can easily be reset to avoid credential leaks.

A user token is composed of a user code and a passcode. When one of these users successfully submits their user token credentials, then they will be authenticated and authorized as if they had submitted their original credentials.

**Note:** User tokens are not supported with reverse proxy authentication.

### Atlassian Crowd Integration Configuration

**Note:** This section assumes you are familiar with Atlassian Crowd, and have a Crowd server currently in use.

You can configure IQ Server to work with a Crowd server for the purposes of authenticating users and managing users and groups.

### IQ Server Realms

IQ Server allows users to be authenticated through various Identity provider services (i.e security realms).

Some IQ Server REST API endpoints accept one or more realm identifiers listed below.

### Authorization and Authentication Concepts

There are several options for authorization and authentication in IQ Server, and Administrators will need to decide which option works best for their organization. This article helps you make that determination.

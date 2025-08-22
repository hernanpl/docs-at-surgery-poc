---
layout: default
title: "Firewall Navigation"
parent: Sonatype Repository Firewall
nav_order: 4
has_children: true
---

# Firewall Navigation

Access the Repository Firewall by logging into your self-hosted IQ server or your Sonatype Cloud tenant. When you using more than one Sonatype solution, use the [solution switcher](#UUID-f6cc2b00-f036-2711-ba56-621efcd473a5) to switch to Repository Firewall.

Administrators manage policies, set access controls, and notifications for the Repository Firewall using the `Repos and Policies` .

We use the following terms for Repository Firewall that they have other meanings in another context:

- The artifact repository connected to the IQ Server (eg. Nexus Repository, JFrog Artifactory)
- The proxy or hosted repository configured in a repository manager (eg. maven-central, npm hosted, etc.)
- The external repository where components are downloaded from. These may be public repositories or privately hosted repositories.
- A repository where components are stored on the repository manager. These may hold internally built artifacts or third-party software.

![fw-navigation-repository-managers.png](/docs-at-surgery-poc/assets/images/uuid-429aa65a-55e0-0d0c-8c06-99f27f2961d2.png)

## Repository Managers Overview

The top-level of the repository managers configuration. Policies set at this level are inherited by all repositories and repository managers. Manage policies, access control, and quarantine for proxy repositories.

Repository Managers are added with a unique identifier when they connect to the Repository Firewall service. Configure namespace protection for hosted repositories.

### Elements in the Overview

- List of the connected repository managers with their repositories in a nested table. The filters are used to limit the list displayed. Selecting a proxy repository opens the [Repository Results View](#UUID-a08de187-0418-3468-53bf-8e5f864b06ef) for that proxy. Repositories are removed using the trash can icon. This action does not delete the repository from the repository manager.
- Policies are inherited from the root organization. Policy actions may be overridden for repository managers for policies enabled at the root organization. Firewall policies may be added for all repository managers at this level. These policies would not be scoped to organizations or applications.
- List of namespaces protected for all repositories. See [Namespace Confusion Protection](#UUID-53279c26-0859-f790-35e9-7d43cfff316d)
- Access control for who may view repository results and manage the Firewall configuration.

## Repository Manager View

Manage the configuring for a specific repository manager in the Repository Firewall.

- When the complete listing of repository managers is not displayed, selecting the `Repository Managers` title will display the list of repository managers.
- Selecting a single repository manager in the list navigates to this view.

![fw-navigation-repository-view.png]({{ /assets/images/uuid-fa481523-4f4b-080a-7751-e646c04224fd.png)

### Sections

The Repository Manager View has the same sections as the overview scoped to the single repository for granular access control of individual repository managers' configurations

### Actions

The actions menu is scoped to this repository manager.

- The unique repository manager ID can be used to identify the instance in log files in IQ Server or Nexus Repository even after the repository manager name has been set to a human-readable name.
- Opens the Edit repository manager name dialog as shown above.
- Used to remove the repository manager from the IQ Server configuration.

### Navigation

Return to higher levels in the repository managers' hierarchy using the breadcrumbs in the top navigation. When navigating to the repository results, the back navigation returns to this view.

The side navigation includes the proxy and hosted repositories for this repository manager. The side menu expands and collapses with the toggle arrow.

- Select the pen icon for either the proxy or hosted repository to view the configuration for the repository.

![fw-navigation-repositories.png](/docs-at-surgery-poc/assets/images/uuid-7a59f80c-28c9-d4be-eaec-2cb6dd1a9c84.png)

## Proxy Repository Configuration

Use this summary page for proxy repository configuration to manage access to individual proxy reports. Like the rest of the hierarchy, access control and policy are inherent from the following; the Root Organization, the Repository Managers container, and the configuration set on the specific repository manager where the proxy is configured.

- Follow the best practice to enable or override enforcement of policies managed at the root organization or the Repository Managers container. Enable enforcement that does not apply to all proxy repositories.
- Set policies on a specific proxy repository that are an exception to the rest of the organization's governance policy
- Use the access controls on the specific repository for fine-tuned access to a single proxy
- Set violation notifications unique to this repository such as from a testing environment

## Hosted Repository Configuration

Manage access to the hosted repository configuration. This includes selecting the namespaces found within the repository. The Firewall analyzes the hosted repository for the namespaces used by its components.

Enable or disable namespace protection using a toggle.

See [Namespace Confusion Protection](#UUID-53279c26-0859-f790-35e9-7d43cfff316d)

## Firewall Dashboard

The Firewall dashboard displays a summary of Firewall operations and the components in quarantine. These results are sorted by the most recently quarantined component and may be filtered using the summary metrics.

![fw-dashboard.png]({{ /assets/images/uuid-32db73d7-a192-2a4d-9497-d43da8df3fe7.png)

### Summary Metrics

This display lists the number of components monitored in quarantine-enabled repositories.

### Quarantined Components

The quarantine results contain components currently in quarantine across Firewall-enabled repositories.

Navigate the results using the filters or pagination controls. The list is sorted by the Quarantine Time, Threat Level, and Component by default.

Selecting the Quarantine Time, Policy, Component, or Repository columns header changes the sort order of the component list.

Selecting a table row displays the Component Information Panel for that component.

## Quarantined Component View

The quarantined component view is a temporary page created when a component is first quarantined that does not require authentication to access. The view displays the details of quarantined components, a list of the violations, and offers remediation advice. This view is available for 12 hours from the time the component is first requested with the link available in the build output.

Components are quarantined when a component is requested from a proxy repository for the first time. The build tool making the request receives a `403` error when the component is not downloaded. The error code provides details of the quarantine and a link to the quarantined component view.

![113248445.png](/docs-at-surgery-poc/assets/images/uuid-9f41891a-0401-2b7f-8e3d-d7757714d6f2.png)

**Note:** When users are authenticated with IQ server and not using anonymous access, they are directed to the Component Details View. To view the component details or the full Repository Results report, the user requires the `View IQ elements` permission. The `View IQ elements` permission is not assigned by default to the `Application Evaluator` or the `Component Evaluator` service account roles which are granted limited access to the user interface.

### Viewing the quarantined components

The quarantined component view provides information about the component including its policy violations and remediation strategies.

- This section indicates that the requested component has been quarantined.
- The title of the section is the component name. The rest of the section provides information on the component's current status, including the First Quarantined Date and Other Allowed Versions in the Repository
- This tab provides information to remediate the violations causing quarantine. The Recommended Versions section suggests versions without failing policy violations. This section includes the Version Explorer to compare versions visually.
- This section lists the failing violations. When upgrading a component is not available, all failing policy violations must be waived to release the component from quarantine.
- This section lists other allowed versions already present in your repository. These versions are not quarantined and can be downloaded without issue. Substituting the requested version with a version listed in this section is a potential alternative to a waiver request.

### Disabling Anonymous Access

The Quarantined Component View link does not require authentication to view. This simplifies access for engineers who may not be allowed to log into the Repository Firewall Dashboard. The information on this page is limited and the length of time it is accessible is relatively short, so there is little risk of exposing secured data.

However, we do recommend disabling anonymous access when your service is accessible to users outside of your organization or is reachable through the public internet.

Disable anonymous access using the [Repository Firewall REST API](#UUID-d516f5b1-1573-aae2-7261-107d95f5fb67) .

## Repository Results View

The repository results page is an audit of a proxy repository configured with the Repository Firewall. This view lists all the components requested through the proxy and any violations found near the time the component was requested.

![Screenshot_2024-02-15_at_7_05_08_PM.png]({{ /assets/images/uuid-849decb0-9296-f7d4-d2d6-39a6a0242beb.png)

### Repository Summary

The summary section contains metrics on the health and contents of the repository. Here you will find the total number of components, the number of violations that affect some of the components, and a spread of the severity of those violations. You will also see if any components have been quarantined and are blocked from downloading through the proxy.

### Repository Components

This table lists all the components in the proxy repository and their associated violations found as of their last evaluation. By default, the view is aggregated by components while only displaying the highest policy violation for that component.

- Select an individual component from the list to view the component's detail page.
- When the toggle is 'on', only the highest-threat violation is displayed for the component. Select the component to view all violations for the component.
- Components are released from quarantine by waiving the policy failing violations on the component. Waive the violations from the component details page. Once the failing violations have been waived, the components are released from quarantine.
- Results may be filtered by the match state and the violation status. All - no filter Exact - Components identifiable by Sonatype Unknown - Components unknown to Sonatype all/none - no filter Not Violating - components with no violations Open - violations not waived or remediated Quarantined - components that have been quarantined due to a failing violation Waived - violations that have been waived
- All - no filter Exact - Components identifiable by Sonatype Unknown - Components unknown to Sonatype
- All - no filter
- Exact - Components identifiable by Sonatype
- Unknown - Components unknown to Sonatype
- all/none - no filter Not Violating - components with no violations Open - violations not waived or remediated Quarantined - components that have been quarantined due to a failing violation Waived - violations that have been waived
- all/none - no filter
- Not Violating - components with no violations
- Open - violations not waived or remediated
- Quarantined - components that have been quarantined due to a failing violation
- Waived - violations that have been waived

### Viewing results in Nexus Repository

As developers request components from a proxy repository, Firewall audits them using the policies in the IQ Server. There are a couple of ways to navigate this report.

The IQ Policy Violations are summarized in the Nexus Repository Pro and detailed in IQ Server.

In Nexus Repository Pro 3, the audit results are summarized in the IQ Policy Violations column of the Repositories view.

This view is located in the Repository sub-menu of the Administration menu.

![91948187.png]({{ "/assets/images/uuid-dec4a3c8-c4af-4da2-a5e3-dfdc83fdba9a.png)

The IQ Policy Violations column includes the following items:

- A count of components by their highest policy violation level.
- A count of quarantined components.
- A link to Repository Results on IQ Server.

The IQ Policy Violations column alerts you if there are any errors in the audit and quarantine process. If there is an error a red exclamation mark will appear to the right of the Repository Results along with a description of the error. Additional information will be available in the Nexus Repository logs.

Without permissions to the Repository Results view, the IQ Policy Violations column displays either `Audit Enabled` or `Quarantine Enabled` .

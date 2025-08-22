---
layout: default
title: "Create PRs from Priorities View"
parent: Priorities View
nav_order: 2
---

# Create PRs from Priorities View

You can configure *Lifecycle* to create manual pull requests (PRs) on the **default branch** in your SCM (e.g. GitHub), to remediate violations, right from the *Priorities View* .

Using this feature, teams can seamlessly incorporate the remediation effort into their development cycles, reducing the MTTR and maintaining a good security posture.

(Refer to [Steps to configure manual PR creation](#UUID-15336078-6f2b-937e-efc8-0a163fcd48aa_section-idm23494518728636) .)

![small_Priorities_View_Manual_PR.png](/docs-at-surgery-poc/assets/images/uuid-77b55b71-3f42-b1b9-8f65-01b9272862af.png)

The *Create PR* button in the Next Step column is enabled if the following conditions are met:

- The policy violation has occurred at a licensed stage (excludes the *develop* stage.)
- The component is used as a direct dependency in the application.
- The component is included in the [Sonatype supported formats](https://help.sonatype.com/en/analysis.html#ecosystem-support) or is an InnerSource component (release 193 and later.)
- A recommendation for a suggested version of the component to remediate the violation is available.
- The logged-in user has sufficient [permissions to create manual PRs](#UUID-15336078-6f2b-937e-efc8-0a163fcd48aa_N1747328876042) from the *Priorities View* .

Click on the Create PR button in the *Next Step* column to create the manual PR. A link to the PR indicating the PR number will appear in the column, if a PR has been created previously (releases 193 and later.)

Verify breaking changes, suggested version of the component and the target branch for which the PR will be created, and click on *Create* .

![small_Verify_PR_details.png]({{ /assets/images/uuid-3f5cc797-264b-69ff-5a3c-6c9022dc7d3c.png)

The creation of manual PR is an asynchronous process. The link *View PR* will be available when the PR has been created successfully.

To view more details for the component, prior to creating the manual PR, click on the component name under the Component column. The link displays the Component Details Page. Use the Create PR button as shown in the image below, on the Component Details Page, if you accept the suggested remediation.

![CPP_with_PR_button.png](/docs-at-surgery-poc/assets/images/uuid-f0c41935-3581-a59f-37d7-d5f3d91ed3e4.png)

**Example of a manual PR created from the Priorities View**

![manual_PR_.png]({{ /assets/images/uuid-62a5f53f-1df9-f096-59c6-d81a5caaa84d.png)

## The Next Step Column

The *Next Step* column in the *Priorities View* can initiate one of the following actions:

- Create PR: To create a manual PR.
- Retry: The previous attempt to create a manual PR was unsuccessful.
- View PR: Links to previously created PRs (both manual and [Auto PRs](https://help.sonatype.com/en/automated-pull-requests.html) ), for suggested remediation for the component violation.
- View Violations: Links to the policy violation tab on the [component details page](https://help.sonatype.com/en/component-details-page.html) to investigate the violation.

**Note:** Automate with Golden PRs A Golden PR is an automated PR created via IQ Server plugins for supported SCMs, if a golden version of a component is available to remediate a policy violation. On instances where both Golden PRs and manual PRs from *Priorities View* are enabled, a Golden PR will be created automatically. A *View PR* link will be displayed in the Next Step column instead of the *Create PR* button. (The *Create PR* button will be displayed for remediation suggestions that do not recommend a Golden Version of the component.) Learn more about [Golden Versions and PRs](https://help.sonatype.com/en/golden-versions-and-prs.html) and [Automated Pull Requests](https://help.sonatype.com/en/automated-pull-requests.html) .

## Steps to Configure Manual PR Creation

- **Assign permission to user roles to create pull/merge requests** a. Login as system/policy administrator and click on the gear icon on the top right of the page. b. Click to Roles under *System Preferences* . c. Toggle the Create pull/merge requests control, under the *Remediation* section to ON position. d. Verify all other permissions and click *Save* .
- **Configure** This can be enabled at the root organization level, to be effective for all organizations and applications. You can also limit the availability of this feature to specific organizations (or sub-orgs), by enabling it at the organization (or parent org) level, to apply to all applications of the organization. For fine grained control over specific applications, you can enable this feature at the application level. a. Click on the *Orgs and Policies* in the left navigation bar and select the organization/application (or root org) for which you want to enable creation of manual PRs. b. Click on *Source Control* from the top bar. c. Toggle the Manual Pull Requests control to enable the manual PR creation from the *Priorities view* . d. Verify other source control configuration settings and click *Update* .

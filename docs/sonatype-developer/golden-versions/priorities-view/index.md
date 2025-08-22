---
layout: default
title: "Priorities View"
parent: Golden Versions
nav_order: 1
has_children: true
---

# Priorities View

The *Priorities* View is accessible from the *Reports* in the left navigation bar.

Click on the *View Priorities* link under the specific stage column (source/build/stage Release/release) on the *Reports* page, for the required application.

The top section shows the name of the branch evaluated, evaluation triggered by, abbreviated git commit hash, the commit timestamp, and stage of evaluation.

**NOTE:** The branch name is visible only when the evaluation is run from a CI/CD environment or Sonatype CLI.

**The Component Column**

The Component column displays the name of the implicated component and its type - direct dependency, transitive dependency or InnerSource dependency (releases 193 and later). Refer to [type of dependencies reported](https://help.sonatype.com/en/reviewing-a-report.html#types-of-dependencies-reported) for more information.

![Priorities_all.png](/assets/images/uuid-1e2e67d2-bc12-a3b8-f2a3-c01499568c4c.png)

**The Reason for Priority Column**

The prioritization of remediation is determined by the Sonatype proprietary Prioritization Algorithm. Learn more about the [Prioritization Algorithm](#UUID-b67217ee-89df-c126-d2ec-6c478b339cb4) .

**The Suggested Fix Column**

The *Suggested Fix* column shows the component version available to remediate the policy violation. The component suggestions include :

- *recommended-non-breaking-with-dependencies* RELEASE 183 This is the [Golden Version](#UUID-3521a2d1-edef-c354-d6aa-aa1dbaa11558)
- *recommended-non-breaking*
- *next-no-violation with dependencies*
- *next-no-violation*
- *next-non-failing with dependencies*
- *next-non-failing*

Click on a row, to view the [component details page](#UUID-c348055a-b083-a26c-6dda-b4cfda3cf2ef) to view the version explorer and compare versions to select a component for remediation.

**The Fail/Warn Policy Action Filter**

Use the Fail/Warn policy action filter to view the priorities based on whether the policy violation has a fail/warn policy action associated with it.

NOTE: The fail/warn policy action filter is set to false by default, for Jira integrations.

![fail-Warn_filter.png](/assets/images/uuid-8d4e900a-9e0c-723b-472f-a6dd7a31c853.png)

The *Next Step* column in the new *Priorities View* allows you to create new pull requests (PRs), view existing PRs (including automated PRs). Learn more on how to: [Create manual pull requests from the Priorities View.](#UUID-15336078-6f2b-937e-efc8-0a163fcd48aa)

If waivers for a violation are in effect, the *Build Action* column displays the status as *Waived* . The *Suggested Remediation* column shows the exact number of violations that are waived for the component. The *Auto* tab indicates an automated waiver has been applied. For violations that are suitable for automated waivers, the tooltip displays the suggestion as "Ask an administrator to configure Automated Waivers". Learn more on [View Waiver Information from the Priorities View](#UUID-9517901c-1ee2-10c3-90a0-992cd3a639ea) .

If the violation is detected on the default (or main) branch, the *Suggested Remediation* column shows **Resolve on default branch** . This facilitates minimizing the remediation efforts by fixing the violation once on the default branch, instead of duplicating the efforts on every feature branch. Subsequent rebasing or merging will prevent the violation from occurring again in the feature branches. The corresponding *Next Step* is shown as *Go to Build Stage* .

![link_build_stage.png](/assets/images/uuid-01f47075-28db-8ac9-a891-d4203b24099e.png)

Click on the *Go to Build Stage* link to view the latest priorities report in your main branch to resolve the policy violation.

## Prioritization Algorithm

The priority of remediation is determined by the Sonatype Prioritization Algorithm.

The Prioritization Algorithm is designed to analyze the following factors:

- Policy Actions (fail/warn/none)
- Reachability of the policy violation
- Threat level of the violation

The weight applied to each factor above depends upon the policy action (highest), reachability of the policy violation and the threat level associated with the violation.

### How Prioritization Algorithm Works

Review the [Policy Action](#UUID-2edc9f20-6766-eb4b-2a06-786cd5985f0c) and the stage in the your devOps cycle, that is designated to trigger when violations occur. Setting the policy action to *fail* ranks the violation higher than *warn* . Since the *build* stage is considered to be most crucial and optimized for addressing remediation issues, policy actions set to trigger at the build stage will be ranked higher than other stages.

The [Reachability](#UUID-bffb3d6e-1a0b-5607-518a-3dcdc88508c2) of the component determines the relevance of addressing the policy violation. If the vulnerable component is not found to be *reachable* , it will be ranked lower in priority. This ensures targeting remediation efforts towards vulnerabilities that are in the execution paths and exploitable.

The threat level associated with the policy violation reflects the actual threat level of vulnerability. Higher threat levels will be ranked higher in priority, to ensure quick remediation.

## Create PRs from Priorities View

You can configure *Lifecycle* to create manual pull requests (PRs) on the **default branch** in your SCM (e.g. GitHub), to remediate violations, right from the *Priorities View* .

Using this feature, teams can seamlessly incorporate the remediation effort into their development cycles, reducing the MTTR and maintaining a good security posture.

(Refer to [Steps to configure manual PR creation](#UUID-15336078-6f2b-937e-efc8-0a163fcd48aa_section-idm23494518728636) .)

![small_Priorities_View_Manual_PR.png](/assets/images/uuid-77b55b71-3f42-b1b9-8f65-01b9272862af.png)

The *Create PR* button in the Next Step column is enabled if the following conditions are met:

- The policy violation has occurred at a licensed stage (excludes the *develop* stage.)
- The component is used as a direct dependency in the application.
- The component is included in the [Sonatype supported formats](https://help.sonatype.com/en/analysis.html#ecosystem-support) or is an InnerSource component (release 193 and later.)
- A recommendation for a suggested version of the component to remediate the violation is available.
- The logged-in user has sufficient [permissions to create manual PRs](#UUID-15336078-6f2b-937e-efc8-0a163fcd48aa_N1747328876042) from the *Priorities View* .

Click on the Create PR button in the *Next Step* column to create the manual PR. A link to the PR indicating the PR number will appear in the column, if a PR has been created previously (releases 193 and later.)

Verify breaking changes, suggested version of the component and the target branch for which the PR will be created, and click on *Create* .

![small_Verify_PR_details.png](/assets/images/uuid-3f5cc797-264b-69ff-5a3c-6c9022dc7d3c.png)

The creation of manual PR is an asynchronous process. The link *View PR* will be available when the PR has been created successfully.

To view more details for the component, prior to creating the manual PR, click on the component name under the Component column. The link displays the Component Details Page. Use the Create PR button as shown in the image below, on the Component Details Page, if you accept the suggested remediation.

![CPP_with_PR_button.png](/assets/images/uuid-f0c41935-3581-a59f-37d7-d5f3d91ed3e4.png)

**Example of a manual PR created from the Priorities View**

![manual_PR_.png](/assets/images/uuid-62a5f53f-1df9-f096-59c6-d81a5caaa84d.png)

### The Next Step Column

The *Next Step* column in the *Priorities View* can initiate one of the following actions:

- Create PR: To create a manual PR.
- Retry: The previous attempt to create a manual PR was unsuccessful.
- View PR: Links to previously created PRs (both manual and [Auto PRs](https://help.sonatype.com/en/automated-pull-requests.html) ), for suggested remediation for the component violation.
- View Violations: Links to the policy violation tab on the [component details page](https://help.sonatype.com/en/component-details-page.html) to investigate the violation.

**Note:** Automate with Golden PRs A Golden PR is an automated PR created via IQ Server plugins for supported SCMs, if a golden version of a component is available to remediate a policy violation. On instances where both Golden PRs and manual PRs from *Priorities View* are enabled, a Golden PR will be created automatically. A *View PR* link will be displayed in the Next Step column instead of the *Create PR* button. (The *Create PR* button will be displayed for remediation suggestions that do not recommend a Golden Version of the component.) Learn more about [Golden Versions and PRs](https://help.sonatype.com/en/golden-versions-and-prs.html) and [Automated Pull Requests](https://help.sonatype.com/en/automated-pull-requests.html) .

### Steps to Configure Manual PR Creation

- **Assign permission to user roles to create pull/merge requests** a. Login as system/policy administrator and click on the gear icon on the top right of the page. b. Click to Roles under *System Preferences* . c. Toggle the Create pull/merge requests control, under the *Remediation* section to ON position. d. Verify all other permissions and click *Save* .
- **Configure** This can be enabled at the root organization level, to be effective for all organizations and applications. You can also limit the availability of this feature to specific organizations (or sub-orgs), by enabling it at the organization (or parent org) level, to apply to all applications of the organization. For fine grained control over specific applications, you can enable this feature at the application level. a. Click on the *Orgs and Policies* in the left navigation bar and select the organization/application (or root org) for which you want to enable creation of manual PRs. b. Click on *Source Control* from the top bar. c. Toggle the Manual Pull Requests control to enable the manual PR creation from the *Priorities view* . d. Verify other source control configuration settings and click *Update* .

## View Waivers from the Priorities View

### Check for Waivers in the Build Action Column

The *Build Action* column on the Priorities View contains the following possible statuses:

![Priorities_view_with_waivers.png](/assets/images/uuid-41070b16-e61d-3bd3-0d61-05bbc17b0f4e.png)

If waivers for a violation are in effect, the *Build Action* column displays the status as *Waived* .

The *Suggested Remediation* column shows:

- *Waive Violations* when the violation does not have any upgrade recommendation and they are not reachable.
- The number of waived violations, when **all** violations have been waived. The green *Auto* tab displays, if **at least one** of the violations has been automatically waived.

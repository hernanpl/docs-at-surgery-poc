---
layout: default
title: "Source Control Configuration"
parent: Sonatype for SCM
nav_order: 1
has_children: true
---

# Source Control Configuration

Sonatype Lifecycle can connect to your Source Control Management (SCM) system with an access token to scan your projects during the development phase. The access token can be set at the Root Organization level. This page provides the configuration steps for SCM.

**Note:** The must be configured for Source Control Features to function.

### Configuration Checklist

Follow the steps below to connect your SCM system to *Sonatype Lifecycle* .

## SCM Feature Configuration

The table below shows where the SCM feature is configured.

## Create Access Token

Select your SCM provider below for information on creating an access token and configuring your SCM System for use with Sonatype Lifecycle.

### Required Token Permissions

**Note:** Supported SCM Authentication For enhanced security and following industry best practices, basic authentication (username and password) is either deprecated or not recommended for most Source Control Management (SCM) providers. We recommend using secure alternatives such as Personal Access Tokens (PATs), OAuth, or SSH keys for authenticating with your SCM systems.

### Dealing with SCM API rate limits

When an SCM system's API interacts with Nexus IQ, the SCM system enforces some form of limitation on the volume and frequency of interaction with their APIs; GitHub appears to be the most restrictive. GitHub limits API requests to 5000 per hour per user and specifies at least a one-second delay between requests. As the number of applications that IQ Server manages increases, the workload demanded of the SCM API also increases. This translates to a delay between, for example, the time the workload is initially processed and the time before a comment is added to a pull request.

Since the SCM system API limitations are per user, organizations with hundreds or thousands of repositories should create multiple users/access tokens and use different tokens for different sub-organizations in IQ Server. This allows IQ Server to perform more work in parallel with the SCM system. The additional tokens must be for distinct SCM users — multiple tokens for the same user will not help since the API rate limits apply at the user level and not the token level. A reasonable starting point would be one user/token for every 500 repositories.

### Troubleshooting

**Special Characters in Repository Names**

Sonatype has special character restrictions on repository names for security reasons. The special characters that are restricted include:

/ : \ ~ & % ; @ ' " ? < > | # $ * } { , + ] [

The repository names cannot start with an underscore ( _ ), start or end with a period (.), or be a system reserved name.

Some SCM providers do not have similar restrictions and allow special characters in repository names. This could lead to errors during onboarding the applications from the SCM system such as the example below:

```
SourceControl repositoryUrl is invalid: Invalid project URL. Project URL cannot contain any of the characters: ;$!*&|()[]<>.
```

## SCM Features Technical Overview

### Overview

Most of what IQ for SCM does is behind the scenes and the outcomes of it generally manifest themselves in the source control management system rather than in IQ Server itself. As such, it can be difficult for users to know exactly what IQ Server is actually doing on their behalf with respect to IQ for SCM features, when, and why.

The purpose of this document is to explain what many of those "behind the scenes" things are, how they work, why they work the way they do, and to provide some level of technical detail.

### How IQ Server interacts with SCM systems

There are two primary ways in which IQ Server interacts with Git-based SCM systems:

- via the SCM systems' web-based **REST APIs** All of the various SCM systems IQ Server interacts with provide an API for doing various things like creating pull requests, commenting on pull requests, creating commit status, etc. To protect their systems against abuse and ensure availability each SCM system imposes some sort of API 'rate limiting'. This is discussed in more detail later in this document.
- All of the various SCM systems IQ Server interacts with provide an API for doing various things like creating pull requests, commenting on pull requests, creating commit status, etc.
- To protect their systems against abuse and ensure availability each SCM system imposes some sort of API 'rate limiting'. This is discussed in more detail later in this document.
- via a **Git client** IQ Server uses Git itself for things like checking for new commits or pulling down manifest files for analysis. There are two Git clients that IQ Server can use: **native Git** client the native git client is installed as a separate tool on the machine where IQ Server is running this is the preferred client since it allows IQ Server to do shallow clones and sparse checkouts which means IQ Server only pulls down the files necessary for component analysis **Java Git** client considered a backup in case a native git client is not installed IQ Server has to clone the entire repository when using this client For more information see [Source Control Git Client Configuration](#UUID-161243f0-61ce-a164-d457-2bff696761b4)
- IQ Server uses Git itself for things like checking for new commits or pulling down manifest files for analysis.
- There are two Git clients that IQ Server can use: **native Git** client the native git client is installed as a separate tool on the machine where IQ Server is running this is the preferred client since it allows IQ Server to do shallow clones and sparse checkouts which means IQ Server only pulls down the files necessary for component analysis **Java Git** client considered a backup in case a native git client is not installed IQ Server has to clone the entire repository when using this client
- **native Git** client the native git client is installed as a separate tool on the machine where IQ Server is running this is the preferred client since it allows IQ Server to do shallow clones and sparse checkouts which means IQ Server only pulls down the files necessary for component analysis
- the native git client is installed as a separate tool on the machine where IQ Server is running
- this is the preferred client since it allows IQ Server to do shallow clones and sparse checkouts which means IQ Server only pulls down the files necessary for component analysis
- **Java Git** client considered a backup in case a native git client is not installed IQ Server has to clone the entire repository when using this client
- considered a backup in case a native git client is not installed
- IQ Server has to clone the entire repository when using this client
- For more information see [Source Control Git Client Configuration](#UUID-161243f0-61ce-a164-d457-2bff696761b4)

### How IQ Server doesn't interact with SCM systems

- IQ Server does not currently support **direct SCM to IQ Server communication** (i.e. webhooks).

### Here's what happens when a policy evaluation occurs

The following diagram illustrates the various SCM operations IQ Server can perform behind the scenes in response to a policy evaluation.

It is assumed at this point that the IQ application is properly associated with an SCM repository via the application's source control configuration.

### Automated Remediation Pull Requests

Remediation pull requests can be created automatically by IQ Server when a policy violation is detected for a component AND there is remediation available that will correct the violation.

The following diagram illustrates the various ways that the creation of an automated remediation pull request can be triggered.

### Pull Request Commenting

Pull request commenting is more complex than what was described earlier as there are other flows, in addition to policy evaluations, that can trigger IQ Server to create or update pull request comments. Those flows will be described below.

First, it's important to point out a few things about PR commenting:

- The intent of IQ Server PR comments is to inform developers when a new policy violation is introduced with the work they are doing on their feature branch or to pat them on the back when they resolve a policy violation.
- **IQ Server doesn't compare internally triggered evaluations of static source code with CI triggered evaluations of build artifacts** . The potential for confusing results is too high in this case.
- Pull request commenting is based on the difference between two policy evaluation reports. The diagram below illustrates the process of selecting the commits used to look up the evaluation reports. Note, this is a more complicated example depicting a branch on branch scenario, but it allows the full selection process to be explained. Most times pull requests will be for a feature branch directly off the default branch.

- First, the pull request as defined in the SCM system is based on these two branches/commits: The developer made their changes on feature branch 'Y' with the latest commit being commit 'I' The developer wants to merge their changes into feature branch 'X'
- The developer made their changes on feature branch 'Y' with the latest commit being commit 'I'
- The developer wants to merge their changes into feature branch 'X'
- So, the source commit (S) of the PR is the head commit of the feature branch, in this case commit 'I'. The policy evaluation associated with this commit will be compared against the target evaluation selected next.
- Selection of the target commit follows this progression: T1 : the common ancestor between the two branches is preferred if there is a policy evaluation associated with it T2 : the base commit specified in the PR itself. The reason the base commit is not the preferred commit is that there could be newer changes to the target branch (from other merged PRs, for example) which might not accurately reflect what the developer currently has on their feature branch Y. If the source branch is kept in sync with the target branch then T1 and T2 would be the same. T3, T4, T5, etc. : finally, the commit history of the default branch is considered and the first one that has an associated policy evaluation is used
- T1 : the common ancestor between the two branches is preferred if there is a policy evaluation associated with it
- T2 : the base commit specified in the PR itself. The reason the base commit is not the preferred commit is that there could be newer changes to the target branch (from other merged PRs, for example) which might not accurately reflect what the developer currently has on their feature branch Y. If the source branch is kept in sync with the target branch then T1 and T2 would be the same.
- T3, T4, T5, etc. : finally, the commit history of the default branch is considered and the first one that has an associated policy evaluation is used

Special note about source control evaluations: If IQ Server is performing the evaluations (i.e. in those cases where CI or other automation processes are not) then IQ Server will always use 'S' and 'T1' as IQ Server will perform those associated evaluations if they don't already exist.

### Dealing with SCM API rate limits

All of the source control management systems enforce some form of limitation on the volume and frequency of interaction with their APIs, with GitHub being the most restrictive in our experience. For example, GitHub restricts API requests to no more than 5000 per hour for a given user and specifies at least a one second delay between requests.

- Note: On premise installations, such as GitHub Enterprise, typically give users control over setting API rate limits or disabling them completely. IQ Server does not currently have a way to know this and therefore has been designed to work within the confines of the default published rate limits.

Obviously, as the number of applications/repositories being managed by IQ Server increases the load on the SCM API also increases.

Let's look at the effect of a policy evaluation on the API load. In response to a policy evaluation the following API interactions may occur:

- API call to send commit status
- API call to discover pull requests
- Possibly one or more API calls to delete existing line comments for a PR
- Possibly one or more API calls to create line comments
- API call to create a pull request comment

This is in addition to the steady load on the API that PR polling introduces.

IQ Server deals with these API rate limit restrictions in a few ways:

- Work that requires interaction with the SCM API is put into a queue (effectively one queue per configured SCM user/token)
- Each queue is processed in an orderly and controlled manner so as not to overwhelm the SCM system
- Algorithms to monitor and fine-tune the pace of requests

## GitHub Configuration

### Creating an Access Token in GitHub

**Note:** Supported GitHub Authentication You can use either classic personal access tokens or fine-grained personal access tokens. For more information on the differences between these token types, refer to the [GitHub Docs](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) . Basic authentication (username and password) is not supported. This method is less secure and [GitHub has deprecated its use](https://github.blog/security/application-security/token-authentication-requirements-for-git-operations/) for authenticating Git operations since August 13, 2021.

### Creating a fine-grained personal access token in GitHub

### Protecting the Target Branch in GitHub

You can prevent users from merging Pull Requests with failing IQ Policy Evaluations with a Branch Protection Rule. IQ Policy Evaluations must be set to Fail at the Source Stage.

To protect a branch:

![126654802.png](/docs-at-surgery-poc/assets/images/uuid-807c2a0b-4d3f-69ec-7ca3-2205fad8a9dd.png)

**Note:** The **IQ Policy Evaluation** status check will not appear in the list of status checks found in the last week for this repository until the first policy evaluation status has been added to the repository.

![126654803.png](/docs-at-surgery-poc/assets/images/uuid-fec6c31a-a9e7-0f75-95aa-7766e8633db8.png)

## GitLab Configuration

### Create an Access Token for GitLab

**Note:** Supported GitLab Authentication For secure authentication, we recommend using Personal Access Tokens. For more information on creating these, refer to the official [GitLab Docs on Personal Access Tokens](https://docs.gitlab.com/user/profile/personal_access_tokens/) . While username and password authentication may still be available, it is less secure and not recommended for integrations. GitLab suggests using tokens as the preferred method for enhanced security.

### Protecting the Target Branch in GitLab

You can prevent merge requests from being merged if their pipeline did not succeed. A failing IQ policy evaluation will cause the pipeline to fail and block the merge request. You can enable this feature (now called auto-merge) via the project settings as shown below.

[See GitLab docs for more information](https://docs.gitlab.com/ee/user/project/merge_requests/auto_merge.html) .

![126655071.png](/docs-at-surgery-poc/assets/images/uuid-fd4baaa2-e84f-d44d-39cc-ac803988f2a7.png)

## Bitbucket Configuration

### Create an Access Token

**Note:** Supported Bitbucket Authentication For secure authentication with Bitbucket, we recommend using App passwords or OAuth. These methods offer more security than using your Atlassian account password directly. For more information, refer to the official [Atlassian Support documentation on App passwords](https://support.atlassian.com/bitbucket-cloud/docs/app-passwords/) . Using your Atlassian account password for Git and Bitbucket API activity [was deprecated in 2022](https://www.atlassian.com/blog/bitbucket/deprecating-atlassian-account-password-for-git-and-bitbucket-api-activity) . App passwords are the recommended and supported method for enhanced security and continued access.

### Protecting the Target Branch in Bitbucket

You can prevent users from merging Pull Requests with failing IQ Policy Evaluations with a **Merge Check.** IQ Policy Evaluations must be set to Fail at the Source Stage.

![126655097.png](/docs-at-surgery-poc/assets/images/uuid-0e14975b-2518-bb3b-ae81-a8cc5ff37480.png)

Click **Enabled** from the dropdown next to **Minimum successful builds** . Set the desired minimum number of successful builds.

![126655098.png](/docs-at-surgery-poc/assets/images/uuid-6f9d761e-8afe-7027-2408-c8d25ca119c5.png)

[See this page for more information.](https://confluence.atlassian.com/bitbucketserver/checks-for-merging-pull-requests-776640039.html)

## Bitbucket Cloud Configuration

### Creating an Access Token in Bitbucket Cloud

**Note:** Supported Bitbucket Cloud Authentication For secure authentication with Bitbucket Cloud, we recommend using App passwords or OAuth. These methods offer more security than using your Atlassian account password directly. For more information, refer to the official [Atlassian Support documentation on App passwords](https://support.atlassian.com/bitbucket-cloud/docs/app-passwords/) . Using your Atlassian account password for Git and Bitbucket API activity [was deprecated in 2022](https://www.atlassian.com/blog/bitbucket/deprecating-atlassian-account-password-for-git-and-bitbucket-api-activity) . App passwords are the recommended and supported method for enhanced security and continued access.

### Protecting the Target Branch

You can prevent users from merging Pull Requests with failing IQ Policy Evaluations two ways in Bitbucket Cloud **.** IQ Policy Evaluations must be set to Fail at the Source Stage.

- For all accounts, users get notified when they don't have that number of successful builds for the most recent commit.
- For premium accounts, users won't be able to merge if their pull request has unresolved merge checks

Click **Settings** , then **Branch permissions** , then **Add a branch permission** .

![Protect Bitbucket branch.png](/docs-at-surgery-poc/assets/images/uuid-a4cf3f72-b55d-1f41-8af3-ce0767d84561.png)

Select the a branch option and desired write and merge access. Select **Check the last commit for at least 1 successful build and no failed builds** in the Merge checks section.

This will inform users that the requirements are not fulfilled when trying to merge. **It will not prevent the merge.**

![Bitbucket Merge PR.png](/docs-at-surgery-poc/assets/images/uuid-cf00d310-eea5-cbb4-3480-75829b30f118.png)

Premium accounts have the additional ability to prevent the merge.

![New_bitbucket_premium.png](/docs-at-surgery-poc/assets/images/uuid-d6cf6496-cc06-e157-5d1a-b87330da222f.png)

This will prevent users from merging a pull request with a failed build.

![bitbucket merge check.png](/docs-at-surgery-poc/assets/images/uuid-5cfe2e8f-6be4-6ffa-81bf-2a0319c667fb.png)

See these pages for more information:

- [https://confluence.atlassian.com/bitbucket/suggest-or-require-checks-before-a-merge-856691474.html](https://confluence.atlassian.com/bitbucket/suggest-or-require-checks-before-a-merge-856691474.html)
- [https://bitbucket.org/blog/protect-your-master-branch-with-merge-checks](https://bitbucket.org/blog/protect-your-master-branch-with-merge-checks)

## Azure DevOps Configuration

### Create an Access Token in Azure DevOps

**Note:** Supported Azure DevOps Authentication For secure authentication with Azure DevOps, we strongly recommend using Personal Access Tokens (PATs). PATs offer more granular control and are the preferred method for integrations and automation. For more information, refer to the official [Azure DevOps documentation on Personal Access Tokens](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops&tabs=Windows) . Alternate credentials authentication (including username and password) was [fully deprecated in Azure DevOps in January 2024](https://devblogs.microsoft.com/devops/azure-devops-will-no-longer-support-alternate-credentials-authentication/) . Personal Access Tokens are the required method for secure and continued access.

### Protecting the Target Branch

You can prevent users from merging Pull Requests with failing IQ Policy Evaluations **.** IQ Policy Evaluations must be set to Fail at the Source Stage.

Create and configure a **Branch Policy** to protect your target branch:

1. Navigate to **Repos → Branches** in the left menu, and select a branch to protect (typically main or develop). Select **Branch policies** from the menu.

![126655155.png](/docs-at-surgery-poc/assets/images/uuid-ad73f84e-26ff-03d3-bfe8-eb63b56becf6.png)

2. Find **Status checks** and click the **+** button

3. Fill out the form

**Status to check *** → Security/IQ Policy Evaluation

**Policy requirement** → Required

**The rest of the values can use the default options**

![126655156.png](/docs-at-surgery-poc/assets/images/uuid-12d2fe53-2926-7105-274c-f8bf2e7f65d7.png)

[See this page for more information on branch policy configuration.](https://docs.microsoft.com/en-us/azure/devops/repos/git/pr-status-policy?view=azure-devops)

## IQ Server Configuration

The IQ Server configuration options allow you to enable and disable the SCM Integration features. This setup consists of the following parts:

- Base URL Configuration
- Git Client Configuration (optional)
- Connect IQ Server to SCM system
- Testing Your Configuration

You can use Secure Shell (SSH) for Git operations such as clone, fetch, and push.

Note that the term pull request" is equivalent to "merge request" used in GitLab terminology.

### Prerequisites

An access token for any of the following Source Control Management Systems:

- [Azure DevOps](#UUID-d4a24710-1a36-5280-4dfb-9f615405e6b6)
- [Bitbucket Server](#UUID-5b33cb44-e739-a894-035a-0ff992b2f5f5)
- [Bitbucket Cloud](#UUID-3c070929-75b1-8810-9a08-c72408fa8960)
- [Github](#UUID-2bbac38c-cecf-51c9-4ceb-3f1e54710012)
- [Gitlab](#UUID-c30106a6-d054-ccca-2d4b-efe8470494cc)

### IQ Server Configuration

### Configure IQ Server With Your SCM System

Configuring Sonatype IQ Server with a Source Control Management (SCM) system requires `Edit IQ elements` permissions.

![157680922.png](/docs-at-surgery-poc/assets/images/uuid-8762b074-f1f1-917d-642e-fb6eabeb6e72.png)

All Source control configuration options can be overwritten at the organization and application levels. This allows you to use multiple SCM providers and access tokens with IQ Server.

### Testing the Configuration

To test the configuration:

**Note:** Testing the SCM Configuration is only available at the Application Level.

![126655196.png](/docs-at-surgery-poc/assets/images/uuid-9578dbc0-1639-cb85-3e8c-0cf00f0153ec.png)

The 'Test Configuration' button is available once any changes have been saved with the 'Update' button.

There are three checks that are run:

- **Is the configuration complete?** This check ensures that are required configuration options are in place. This includes all required options, some of which may be inherited from the organization.
- **Is the repository private?** Repositories must be private or internal to enable all SCM features.
- **Does the token have sufficient permissions?** This check will ensure the provided token has the necessary permissions or privileges to create pull requests.

### SSH for Git Operations

SSH can be used for Git operations such as clone, fetch, and push. To enable SSH, select the option **Use SSH for Git Operations** in the configuration screen.

**On Root Organization:**

![126655183.png](/docs-at-surgery-poc/assets/images/uuid-44f1c401-58f0-9d66-0d14-2ef1bed34c92.png)

**On a Child Organization or an Application:**

![126655184.png](/docs-at-surgery-poc/assets/images/uuid-d457cf4e-1aed-70e3-6623-25250e5e7e9c.png)

SSH **requires native git** and a properly configured SSH key that is available to IQ. Configuring an SSH key is beyond the scope of this help document. Please consult your security or operations team.

**Some important notes**

- Using a passwordless SSH key requires no extra configuration. This is the least secure option. Only use this in a fully trusted environment.
- The Git for Windows installer lets you use a bundled version of SSH, or use an external version. If the bundled SSH is selected, SSH will only be available in Git Bash. This requires IQ to run in that same context. With an external version of SSH, the SSH key should be configured per the chosen implementation (e.g. [OpenSSH for Windows](https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse) , Putty)
- On Linux most traditional setups should work as long as the context of the SSH agent is available to IQ. Sometimes requires that the `SSH_AUTH_SOCK` environment variable is properly set.

## Sparse Checkout File Types

The following file types are checked out when sparse checkout is enabled in your SCM for IQ settings.

**Note:** Sparse checkout is only available when the native git client is enabled. See [Nexus IQ Server Configuration](#UUID-f3b4500c-ca79-40f7-37ec-428d70e9d8a7) for more information.

```
alpine.txt
bom.xml
bower.json
Cargo.lock
clair-scanner-output.json
Podfile.lock
conanfile.txt
conaninfo.txt
conanfile.py
conda.txt
cran-installed.packages
debian-packages.txt
drupal-components.csv
go.list
Gopkg.lock
go.sum
package.json
package-lock.json
npm-shrinkwrap.json
pom.xml
build.gradle
composer.lock
pnpm-lock.yaml
requirements.txt
poetry.lock
Gemfile.lock
yarn.lock
packages.config
yum-packages.txt
Package.resolved
*.csproj
*.tfplan
*.aar
*.ear
*.har
*.hpi
*.jar
*.mar
*.nbm
*.nupkg
*.rar
*.sar
*.tar
*.tar.bz2
*.tar.gz
*.tar.xz
*.tb2
*.tbz
*.tgz
*.txz
*.war
*.whl
*.wsr
*.zip
*.dll
*.gem
*.js
*.rpm
gradle.properties
go.mod
```

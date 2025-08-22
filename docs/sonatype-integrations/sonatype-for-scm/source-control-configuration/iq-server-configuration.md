---
layout: default
title: "IQ Server Configuration"
parent: Source Control Configuration
nav_order: 7
---

# IQ Server Configuration

The IQ Server configuration options allow you to enable and disable the SCM Integration features. This setup consists of the following parts:

- Base URL Configuration
- Git Client Configuration (optional)
- Connect IQ Server to SCM system
- Testing Your Configuration

You can use Secure Shell (SSH) for Git operations such as clone, fetch, and push.

Note that the term "pull request" is equivalent to "merge request" used in GitLab terminology.

## Prerequisites

An access token for any of the following Source Control Management Systems:

- [Azure DevOps](#UUID-d4a24710-1a36-5280-4dfb-9f615405e6b6)
- [Bitbucket Server](#UUID-5b33cb44-e739-a894-035a-0ff992b2f5f5)
- [Bitbucket Cloud](#UUID-3c070929-75b1-8810-9a08-c72408fa8960)
- [Github](#UUID-2bbac38c-cecf-51c9-4ceb-3f1e54710012)
- [Gitlab](#UUID-c30106a6-d054-ccca-2d4b-efe8470494cc)

## IQ Server Configuration

### Base URL Configuration

### Git Client Configuration

Git Client configuration is optional but recommended. Sonatype IQ Server is bundled with [JGit](https://www.eclipse.org/jgit/) to work with no external software. JGit is a Java implementation of git that supports all IQ for SCM features. JGit **does not** support two git clone features that can improve performance: [shallow clone](https://git-scm.com/docs/git-clone) and sparse [checkout](https://git-scm.com/docs/git-checkout/) . Shallow clone lets us clone the least amount of git history. Sparse checkout lets us only check out the [files we need.](#UUID-9c6dc9ad-5f32-6f35-9bb5-4c109a1a88b8) These two git clone features improve performance with large disk-space savings and reduced network traffic.

Sonatype IQ Server uses git's repository clone feature for the following:

- Automated Pull Requests
- Pull Request Commenting
- Instant Risk Profile
- Continuous Risk Profile

**Note:** Native Git is required in order to use SSH for Git operations.

## Configure IQ Server With Your SCM System

Configuring Sonatype IQ Server with a Source Control Management (SCM) system requires `Edit IQ elements` permissions.

![157680922.png](/docs-at-surgery-poc/assets/images/uuid-8762b074-f1f1-917d-642e-fb6eabeb6e72.png)

All Source control configuration options can be overwritten at the organization and application levels. This allows you to use multiple SCM providers and access tokens with IQ Server.

### Application Source Control Configuration

An application is configured like an organization with an additional field: **Repository Clone URL** .

Enter a valid HTTP(S) URL for the **Repository Clone URL** field.

This URL is used to connect to your SCM. All SCM features use the SCM's REST APIs behind the scenes.

**Note:** If you want to enable SSH, check [SSH for Git operations](#UUID-f3b4500c-ca79-40f7-37ec-428d70e9d8a7_id_NexusIQServerConfiguration-SSHSSHforGitOperations) .

### Automatic SCM Configuration

With Automatic SCM Configuration turned on, the repository URL will be automatically discovered from the git project information and configured for the IQ application. Automatic SCM Configuration can be enabled via the configuration menu in the toolbar.

See the Automatic SCM Configuration page for more information.

## Testing the Configuration

To test the configuration:

**Note:** Testing the SCM Configuration is only available at the Application Level.

![126655196.png](/docs-at-surgery-poc/assets/images/uuid-9578dbc0-1639-cb85-3e8c-0cf00f0153ec.png)

The 'Test Configuration' button is available once any changes have been saved with the 'Update' button.

There are three checks that are run:

- **Is the configuration complete?** This check ensures that are required configuration options are in place. This includes all required options, some of which may be inherited from the organization.
- **Is the repository private?** Repositories must be private or internal to enable all SCM features.
- **Does the token have sufficient permissions?** This check will ensure the provided token has the necessary permissions or privileges to create pull requests.

## SSH for Git Operations

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

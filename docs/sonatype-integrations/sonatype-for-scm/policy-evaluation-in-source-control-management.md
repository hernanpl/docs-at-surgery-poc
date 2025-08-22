---
layout: default
title: "Policy Evaluation in Source Control Management"
parent: Sonatype for SCM
nav_order: 7
---

# Policy Evaluation in Source Control Management

Lifecycle for Source Control Management (SCM) is a set of features that lets developers gain early insight into code changes by working in tandem with continuous integration to push policy information about an application’s components directly into their SCM.

Lifecycle for SCM has the following features:

- **Automated commit feedback** : Lifecycle for SCM puts the information needed to quickly remediate vulnerabilities in software solutions at the fingertips of developers by pushing policy evaluation information into SCM commits and pull requests (PRs), where developers work.
- **Automated pull requests** : Lifecycle for SCM will automatically create pull requests for policy violations on components that have an available version that remediates those violations.
- **Pull request commenting** : Lifecycle for SCM adds a comment to pull requests for repositories configured for source control when the PR introduces a new policy violation.

## Early Feedback and Automation

In today’s software development lifecycle (SDLC), developers are asked to release complex software at an increasingly faster pace. Because of this, devs are relying more and more on OSS, utilizing openly available, popular components rather than writing unique code. Consequently, [Sonatype’s State of the Software Supply Chain](https://www.sonatype.com/resources/state-of-the-software-supply-chain-2021) found that open-source software (OSS) components make up more than 80% of most modern applications. With this, the traditional capacity of a developer simply writing code has shifted to a holistic role that includes assembling and integrating code that supports both your software and business operations.

While assembling code, developers often use source control management systems, like GitHub, GitLab, and Bitbucket. SCMs are often the first place where a piece of code gets shared and reviewed by both humans and machines. Lifecycle for SCM uses Lifecycle to establish a relevant policy configuration. Scan evaluations in SCM are run against that policy configuration so that as developers build applications, they receive accurate and timely information to take action on reported violations.

The main value of SCM systems is their ease of collaboration. Developers are able to push quality control of their application development to a source control platform, where this collaboration exists in code reviews that contain both commits and pull requests.

Building on this, Lifecycle for SCM provides suggested remediations for policy violations directly into the source control repository. We do this by automatically creating pull requests with the changes to an application’s component manifest. Using this type of early feedback and automation, we reduce rework and keep development teams focused on contributing business value rather than managing application component risk.

## How Lifecycle for SCM Works

To use Lifecycle for SCM, you first need to configure the IQ Server to allow access to your company’s Source Control Management platform. For large organizations, we recommend enabling automatic source control which lets CI and CLI integrations configure application source control connections when running from a locally cloned repository (a common practice in CI systems).

Once configured, commits will immediately receive automated commit feedback. If enabled and appropriately configured, applications will also start seeing automated pull requests for any new policy violation with suggested remediation, and pull request comments that detail the summary of violations, affected components, and a description of the violations that were introduced in the PR.

A Continuous Integration system or build agent is required for these features to work. For example, if Jenkins is pulling and running the scan, Lifecycle can pick up the source control context and use that as a source. This eases control and gets policy information closer to developers.

We suggest using CI against all feature branches in your SCM, letting you see early feedback on the quality of your code as it’s written. For Lifecycle to provide feedback to feature branches during development, CI must be configured to run a policy evaluation against these branches. We recommend that evaluations against the main branch use the ‘build’ stage in Lifecycle, and that feature branch evaluations are performed against the ‘develop’ stage. The ‘develop’ stage is intended for policy evaluation snapshots where changes to application dependencies and any associated policy violations are not tracked linearly. Because feature branches are volatile and vary across the features developed, using the ‘develop’ stage helps reduce noise by not showing these evaluations on the dashboard or your reports.

When deploying Lifecycle for SCM, you should authorize Lifecycle at the Root Organization level to communicate with your SCM tool (example: GitHub). Then, when you do any evaluation, we will look at the context in modern CI systems—meaning your Git repo gets cloned, then we run an evaluation in that directory, and we can get that information and see what was cloned. This lets us associate GitHub projects to applications in Lifecycle.

## Example Use Case: Automatic Pull Requests for npm

Using this example, you will be able to:

- Regularly scan an npm project for violations of your organization’s stated policy for the Software Supply Chain.
- Create GitHub pull requests and update project component dependencies to available versions that comply with organization policy.
- Automatically verify and integrate Lifecycle remediation suggestions in your Continuous Integration pipeline.

### Prerequisites

- The latest version of IQ Server.
- A GitHub Repository hosting your project This example uses an [npm project](https://github.com/sonatype/nexus-iq-for-scm-demo/) . The configuration and workflow described here will also work for Maven projects.
- This example uses an [npm project](https://github.com/sonatype/nexus-iq-for-scm-demo/) . The configuration and workflow described here will also work for Maven projects.
- A Continuous Integration (CI) system. This example uses Jenkins with the default plugins installed. Details on the example pipeline are shown throughout the workflow. We recommend that your feature branches use the ‘develop’ stage and your main branch uses the ‘build’ stage. This setup reduces noise as evaluations made with the ‘develop’ stage aren’t displayed in the dashboard or reporting view.
- This example uses Jenkins with the default plugins installed. Details on the example pipeline are shown throughout the workflow.
- We recommend that your feature branches use the ‘develop’ stage and your main branch uses the ‘build’ stage. This setup reduces noise as evaluations made with the ‘develop’ stage aren’t displayed in the dashboard or reporting view.
- Docker running on the host to be used by Jenkins - [https://www.docker.com/get-started](https://www.docker.com/get-started)
- Duplicate the sample repository at [https://github.com/sonatype/nexus-iq-for-scm-demo/](https://github.com/sonatype/nexus-iq-for-scm-demo/) using the GitHub ‘import’ feature. Lifecycle for SCM operates on private repositories. The demo repository is public so that it can be duplicated to your account as a private repository. [Note this process is different than a regular fork](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/duplicating-a-repository) . Go to [https://github.com/new/import](https://github.com/new/import) . Enter [https://github.com/sonatype/nexus-iq-for-scm-demo](https://github.com/sonatype/nexus-iq-for-scm-demo) for the “old repository’s clone URL” field. Enter `nexus-iq-for-scm-demo` for the new repository name. Select ‘Private’ for the repository privacy. Click ‘Begin Import’
- Go to [https://github.com/new/import](https://github.com/new/import) .
- Enter [https://github.com/sonatype/nexus-iq-for-scm-demo](https://github.com/sonatype/nexus-iq-for-scm-demo) for the “old repository’s clone URL” field.
- Enter `nexus-iq-for-scm-demo` for the new repository name.
- Select ‘Private’ for the repository privacy.
- Click ‘Begin Import’
- Because GitHub is transitioning `master` to `main` branch names, ensure that your Jenkinsfile reflects this. Navigate to your duplicated `nexus-iq-for-scm-demo` > Jenkinsfile Check the four locations to ensure they use `main` instead of `master` line 21: `when { branch 'main' }` line 58: `sh 'git fetch origin main'` line 62: `sh 'git checkout main'` line 66: `sh 'git push origin main'`
- Navigate to your duplicated `nexus-iq-for-scm-demo` > Jenkinsfile
- Check the four locations to ensure they use `main` instead of `master`
- line 21: `when { branch 'main' }`
- line 58: `sh 'git fetch origin main'`
- line 62: `sh 'git checkout main'`
- line 66: `sh 'git push origin main'`

### Configuration

### Workflow

Once you’ve finished up the configuration, it’s time to kick off a build of your npm application. When you do so, the following workflow takes place:

```
pipeline { 
        agent { 
                docker { 
                        // Docker image with node and git installed image 
                        'tarampampam/node:13-alpine' 
                } 
        } 
        environment { 
                HOME = '.' 
        } 
        stages { 
                stage('Build') { 
                        steps { 
                                sh 'npm install' 
                        } 
                } 
                stage('Test') { 
                        steps { 
                                echo "Run acceptance tests to ensure that IQ remediation changes function as expected in the application" 
                        } 
                } 
                stage('Policy Evaluation') { 
                        // evaluation takes place against the merge branch we intend to merge to 
                        when { 
                                branch 'main' 
                        } 
                        steps { 
                                sh 'npm run build' 
                                // build script using webpack and the copy-modules-webpack-plugin for easy scanning 
                                nexusPolicyEvaluation 
                                        iqStage: 'build', 
                                        iqApplication: 'npm-example', 
                                        iqScanPatterns: [[scanPattern: 'webpack-modules']], 
                                        failBuildOnNetworkError: true 
                        } 
                }
```

**Note:** **Note:** Verify your Jenkinsfile contains the `environment {HOME = '.'}` shown in the example above. Your docker npm commands may fail without this.

2. A policy violation is found for the `react-dom 16.0.0` component. We also see that there is a newer version available we can replace it with.

![Example report vulnerable component]({{ "/assets/images/uuid-5273a902-190a-de7a-bbdf-125869a07db9.png)

Lifecycle for SCM always bumps to a specific version, and pins it in your manifest. Only pinned versions give you control on remediation through security and quality policies. For example, version 1.3.7 might pass policy, but version 1.3.8 might not. A version range of ~1.3.0 does not allow this type of control—we don’t want to replace one security violation with another.

The example workflow is shown here using GitHub, Jenkins CI, and an npm project. We encourage you to utilize other systems you have in place to work well with our software.

## Measuring Success

Success can be measured by a reduction in mean time to resolution (MTTR) which can be seen in our success metrics. Lifecycle for SCM provides the ability to prevent new violations from entering your main branch by informing development teams of risk as soon as they introduce it. We use automation to fix any violations as they occur by providing pull requests with the version change, and both of these practices should reduce MTTR.

If you’re ready to start using Lifecycle for SCM features, reach out to your customer success representative for guidance.

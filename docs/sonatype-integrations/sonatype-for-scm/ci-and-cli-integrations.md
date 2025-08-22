---
layout: default
title: "CI and CLI Integrations"
parent: Sonatype for SCM
nav_order: 5
---

# CI and CLI Integrations

Sonatype Lifecycle supports several CLI and CI integrations with its [SCM Integration](#UUID-32a5d718-bd65-9f34-bba7-704ac47a7a54) .

## Sonatype CLI

Any application can be evaluated against your policies using the Sonatype CLI.

### Instructions for Use

Run the `nexus-iq-cli` command within the git-cloned project folder. Sonatype for SCM will automatically discover the commit hash, repository URL, and branch name from the git context and then send this information to Sonatype Lifecycle with the policy evaluation request.

The additional command output will print the repository and commit hash discovery information:

```
[INFO] Validating IQ Server version http://localhost:8070...
[INFO] Validating application ID test-app with the IQ Server http://localhost:8070...
[INFO] Discovered repository url 'https://github.com/my-org/my-repo' via jGit
[INFO] Discovered commit hash '00ac4dc1da4b8ce233df110cbd175ae85284b655' via jGit
[INFO] Discovered branch name 'main' via jGit
```

To specify commit metadata for `nexus-iq-cli` when outside a Git project, you have two options:

- If you have a Git project cloned elsewhere, set the `GIT_DIR` environment variable to the full path of the .git folder within that project.
- You can also pass the commit hash and branch name to the `nexus-iq-cli` using the **--metadata** parameter. If you do not have a git-cloned project, provide the commit hash and branch name in a JSON file using the following format:

## Sonatype CLI Docker Image

The Sonatype CLI is also available as a docker image at [https://hub.docker.com/r/sonatype/nexus-iq-cli](https://hub.docker.com/r/sonatype/nexus-iq-cli) . The documentation there details how to use the image to perform an evaluation.

## Sonatype Platform Plugin for Jenkins

Sonatype Platform Plugin for Jenkins scans a build workspace for components, creates a summary file about all the components found, and then submits that file to the IQ Server for a detailed policy evaluation. Lifecycle generates a detailed analysis of security information, license information, and other policy details. A summary of that report is sent to the Jenkins server to include in the build results.

### Prerequisites

- Version nexus-jenkins-plugin-3.8.20191204-084645.a4bff16 and higher

### Instructions for Use

Run the Sonatype Platform Plugin for Jenkins. Sonatype for SCM automatically attempts to identify the commit hash and branch name using the `GIT_COMMIT` and `GIT_BRANCH` environment variables. If those environment variables are not set, the plugin will traverse your project's directory tree to locate the .git folder and extract the commit hash and branch name.

An additional command output will print the discovered commit hash and branch name in the Jenkins system log:

```
...
Dec 20, 2019 4:45:53 PM FINE com.sonatype.nexus.git.utils.commit.AggregateCommitHashFinder tryGetCommitHash
Unable to find commit hash via environment variable GIT_COMMIT
Dec 20, 2019 4:45:53 PM INFO com.sonatype.nexus.git.utils.commit.AggregateCommitHashFinder tryGetCommitHash
Discovered commit hash '60638345c358694151de444fd63bfb02ca79ec8b' via jGit
Discovered branch name 'main' via jGit
...
```

## Sonatype for GitLab CI

CI/CD pipeline jobs in GitLab use custom docker images to perform actions in GitLab project's build workspace. The GitLab Sonatype docker image provides the ability to run policy evaluations against build artifacts in GitLab. This produces a summary report with policy violation counts and a link to a detailed report on the IQ Server.

### Prerequisites

- Version release-1.2 and higher

### Instructions for Use

Run Sonatype for GitLab CI. The plugin automatically attempts to identify the commit hash and branch name using the `CI_COMMIT_SHA` and `CI_COMMIT_REF_NAME` environment variables. If these variables are not set, it will locate the .git folder in the project's directory to retrieve this information.

## Sonatype CLM for Maven

Any application can be evaluated against your policies using the Sonatype CLM for Maven Plugin.

### Prerequisites

- Version 2.16.0 and higher

### Instructions for Use

Run the `evaluate` goal anywhere within the git-cloned project folder. Sonatype for SCM will automatically discover the commit hash and branch name from the git context and send this information to the IQ Server with the policy evaluation request.

An additional command output will print the discovered repository, commit hash, and branch name information (some lines were omitted):

```
[INFO] Starting scan...
[INFO] Discovered commit hash 'b8d6b434dad8670ddfd08a0f9232df46134f2198' via jGit
[INFO] Discovered branch name 'main' via jGit
...
```

You can set the GIT_DIR environment variable to the full path of the .git folder for the git-cloned project if you are not running the command within a git-cloned project folder.

## Sonatype for Bamboo

The Sonatype for Bamboo plugin lets you run policy evaluations against building artifacts in Bamboo. This produces a summary report with policy violation counts and a link to a detailed report on the IQ Server.

### Prerequisites

- Version release-1.15.0 and higher

### Instructions for Use

Add an **IQ Policy Evaluation** task to your build plan in Bamboo. Execute the plan. Sonatype for SCM will automatically discover the commit hash, and the branch name, and send it to IQ Server as part of the policy evaluation request.

The collection of the commit hash and branch name can be viewed in the build log as shown below (some lines were omitted):

```
04-Feb-2020 11:15:45  Starting IQ analysis
...
04-Feb-2020 11:15:47  Discovered commit hash '17950bd5cf0492d046e6f01b49836f073638af4f' via jGit
04-Feb-2020 11:15:48  Discovered branch name 'main' via jGit
...
04-Feb-2020 11:15:58  Policy evaluation completed in 10 seconds.
```

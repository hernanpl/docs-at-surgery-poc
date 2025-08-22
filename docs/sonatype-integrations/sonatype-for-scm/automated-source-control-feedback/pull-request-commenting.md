---
layout: default
title: "Pull Request Commenting"
parent: Automated Source Control Feedback
nav_order: 4
---

# Pull Request Commenting

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

## Pull request commenting flows

There are several ways that pull request comments can be triggered:

- In direct response to a policy evaluation, as was described earlier
- Via a polling mechanism for those cases where a pull request is created after the policy evaluation occurs
- When a new commit is detected on the pull request feature branch (pull request monitoring)

## Polling SCM for new pull requests

Looking for pull requests to comment on in response to a policy evaluation works fine, but what if the pull request is created AFTER the policy evaluation occurs (which is very likely in many scenarios)?

In this case IQ Server needs some mechanism to discover new pull requests. It's already been mentioned that IQ Server doesn't currently accept notifications from the SCM system itself so this is where polling comes in - IQ Server periodically asks the SCM system if there are any new pull requests.

- GitHub allows API requests to fetch pull requests across all repositories the configured token user has access to. This means, for GitHub, that IQ Server needs to make far fewer requests and can get back more data in each request, which is good.
- For the other SCM systems IQ Server has to contact the SCM system for each repository one by one, which results in far more requests to the SCM system, which is not ideal.

In either case, IQ Server has to periodically cycle through all the configured applications/repositories while trying to balance (a) the desire to comment on a pull request soon after it's created with (b) the requirement to not exceed SCM API rate limits. So, for organizations with a lot of applications and repositories it can take a considerable amount of time to cycle through all of them and the HTTP traffic to the SCM system could be steady and continuous - as one cycle ends a new one would begin. To give some context, as an example it could take upwards of 20 minutes or so to complete one cycle through 1000 repositories.

- Note: If pull request commenting is disabled for a given IQ application that application will not participate in pull request polling. So, if there are repositories that are inactive and/or you don't care about receiving pull request comments it's recommended to disable this feature.

## Monitoring pull requests for new commits

Once a pull request is created and IQ Server discovers it, what if there are new commits to the pull request?

- First, if CI is setup for the associated repository to run a policy evaluation sometime during the build pipeline this will trigger a policy evaluation, which will trigger a new/updated PR comment, as needed.
- To account for those cases where CI is not setup to do this IQ Server regularly checks for new commits to existing PR feature branches an **uses the Git client** itself, rather than the SCM sytem's API.

## CI driven vs. IQ Server driven PR commenting

IQ Server supports two approaches to PR commenting:

- The preferred approach is to base comments on customer initiated policy evaluations via their CI systems or other automation processes. This allows the customer to specify exactly what they want evaluated, including build artifacts, and when.
- In those cases where the customer hasn't setup CI/automation yet on a given repository IQ Server will still detect pull requests, and noticing that these CI initiated policy evaluations are not occurring, will initate evaluations on the contents of the repository to produce the necessary policy evaluations to base the comments on.

The following diagram illustrates this in more detail (please note the use of IQ Server stages):

- **External/CI/API initiated policy evaluations are preferred** for a few reasons: the customer directly controls this most likely evaluating artifacts that are produced by a build process, which might more accurately depict the contents (from a component/dependency perspective) of the application more fine grained control of what gets scanned and evaluated via 'scan targets' control over when and how often the evaluations occur
- the customer directly controls this
- most likely evaluating artifacts that are produced by a build process, which might more accurately depict the contents (from a component/dependency perspective) of the application
- more fine grained control of what gets scanned and evaluated via 'scan targets'
- control over when and how often the evaluations occur
- Secondarily, in the absence of external policy evaluations IQ Server will initiate and perform evaluations on the contents of the source control repository provides a bridge between initial onboarding and the establishment of CI or other automation processes no fine grained control of what gets scanned and evaluated - the entire contents of the repository are considered no control over when or how often evaluations occur - they happen as needed
- provides a bridge between initial onboarding and the establishment of CI or other automation processes
- no fine grained control of what gets scanned and evaluated - the entire contents of the repository are considered
- no control over when or how often evaluations occur - they happen as needed

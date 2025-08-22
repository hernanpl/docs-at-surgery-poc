---
layout: default
title: "Repository Firewall Best Practices"
parent: Sonatype Repository Firewall
nav_order: 11
---

# Repository Firewall Best Practices

This section covers best practices to help you mature your usage of the Repository Firewall solution.

- Repository Firewall should be used to stop new risks from being introduced into your repository
- Blocking components your applications currently depend on will result in a poor experience with your development teams
- Review the note below on cleaning up vulnerable components from your repository

Enforcement is the primary use case for the Repository Firewall. Repository Firewall supports dependency management by preventing components with known vulnerabilities and policy violations from entering your proxy repositories.

- Enforcement is managed by IQ Server policy however, the Capability must first be configured, enabled, and have the Quarantined option checked; for each proxy that will need Repository Firewall protection.
- Repository Firewall will audit the existing components in the repository while only quarantining new components not used by existing applications.
- Avoid deleting vulnerable components from your proxy repositories so that existing builds are not impacted.

Additional protections, like , are enabled in Nexus Repository.

There are components in public package registries that should never be allowed into your environment. We recommend turning on enforcement right away for the following policies.

- Security-Malicious: components with known malicious intent
- Integrity-Rating: components where Sonatype's Release Integrity data team is reviewing potential threats
- Security-Critical: vulnerabilities with a CVSS score of 9 or greater should be avoided as much as possible
- License-Banned: license issues can pose financial risks to an organization

- Only allow components entering your builds that have been identified and reviewed by Sonatype Intelligence
- New components in public repositories are unknown for less than 5 minutes before they are identified
- This creates a narrow window where dangerous components could enter your system
- Components can be automatically released once identified
- Allowing unknown components is a potential risk to your supply chain

See for instructions on blocking unknown components.

- Repository Firewall automates your repository security by automatically releasing components from quarantine
- Enabling Automatic Quarantine Release reduces the effort of administrating the Repository Firewall and reduces developer friction

See

- This feature reduces risk when your dependencies are coded to use the latest released version
- Queries for the latest component version are only answered with the versions that are approved by your policy
- This prevents newly released package versions from interrupting development if your application automatically downloads the newest version of an application

See

- Developers need to know how and to whom to reach out to release a component from quarantine
- When turning on enforcement, communicate to your developers what to do when components are quarantined
- Quarantine messaging is easily overlooked when not prepared and can be frustrating to deal with when troubleshooting build failures
- Firewall administrators are often not able to determine which build attempted to download for a quarantined component

- Developer dependencies and frameworks typically do not end up in the final application, so the threshold of risk in their use is often lower
- They also tend to be frequently and automatically updated which can cause them to be blocked by the Firewall more often when they have risk
- To avoid frustrating your developers by having them frequently request waivers, you can scope waivers to include all versions of the component
- This will accept the risk of a single violation for future versions of a component while still blocking new violations before they are reviewed

- Repository Firewall works by identifying open-source from public repositories from our supported ecosystems
- You will have many unknown components when configuring the Repository Firewall on unsupported proxies

---
layout: default
title: "Nexus Repository Best Practices"
parent: Sonatype Nexus Repository
nav_order: 10
---

# Nexus Repository Best Practices

These concepts are common best practices to use for planning, deploying, and socializing expectations for the Nexus Platform. These best practices come from our experience with how Nexus Repository is intended to be used and the successful experiences of customers like you.

These best practices focus on:

- How we've seen others be successful
- The path that avoids the most common pitfalls
- Recommendations for good usage

## Administration Best Practices

### Access Control

### Component Repositories

### Content Replication

### Formats

### Cleanup

### Storage

### Monitoring

### Scripting

## Component Lifecycle Best Practices

### Staging

### Tagging

## Infrastructure-based Best Practices

When designing your Nexus Repository infrastructure, use the Resiliency and High Availability documentation for the high-level concepts used in typical deployments. Include consideration for the following:

- Ingress - load balancer and/or reverse proxy
- Application Server - system and local storage for running the application
- Database Server - system for running the external postgres database
- Component Storage - network or attached file or object storage

The following best practices detail important considerations for scaling and maintenance of the instance used as your system of record.

### Resiliency and High Availability

### Server Maintenance

## Shadow Download Best Practices

Nexus Repository is the system of record (SOR) for third-party software, open-source components, and built artifacts for your organization. Shadow downloads are third-party or open-source components retrieved directly from public repositories that bypasses Nexus Repository. These components add risk by allowing in dependencies to your build pipeline without review and visibility; preventing your organization from centrally managing your artifacts.

To mitigate shadow downloads, consider the following recommendations.

- Integrate Repository Firewall with Zscaler to provide additional defense against malware hidden within shadow downloads. This integration extends protection beyond standard repository boundaries, ensuring comprehensive coverage even if initial governance measures are bypassed. See the Integrate Firewall with Zscaler documentation
- Forcing builds only to use components currently cached in your Nexus Repository will act as a fail-safe to ensure that no new components are added to your projects without prior evaluation. This can be achieved by applying policies to incoming components with Repository Firewall.
- Developers should all be required to retrieve components through your Nexus Repository instance. If it’s possible for your organization, the remote repository location should be locked to Nexus Repository for all corporate machines.
- Only authorized sources, such as a centrally managed Nexus Repository should be given access to download component libraries.
- The MDM allow organizations to ensure all company laptops use package manager configurations pointing to a Nexus Repository. Use this type of software to lock configuration files or receive notifications if these settings are changed.
- Create an internal process allowing development teams to request content from public repositories that is not currently available through approved means. Once approved these components can be stored in designated repositories within your repository manager.
- Repository Health check will identify open-source security risks in your proxy repositories. Enabling this feature will let you monitor your components for potential security risks. Regularly checking the Repository health check can alert you to new components that bypass your normal ingress processes.
- While shadow downloads bypass the Nexus Repository, the Repository Firewall acts as a line of defense when your build systems go through your central repositories.

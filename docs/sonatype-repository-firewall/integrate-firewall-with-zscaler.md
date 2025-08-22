---
layout: default
title: "Integrate Firewall with Zscaler"
parent: Sonatype Repository Firewall
nav_order: 10
---

# Integrate Firewall with Zscaler

Zscaler is a cloud-native cybersecurity platform to securely connect users, devices, and applications, regardless of their location. Think of it as a security checkpoint in the cloud that all your organization's traffic can pass through for inspection and protection.

Sonatype's Repository Firewall integrates with Zscaler to block actively verified malware components from being directly downloaded from public repositories. This integration protects your organization from malware found in the shadow downloads of users bypassing your Nexus Repository.

See [Shadow Downloads Best Practices](#UUID-20ffcb47-126b-7578-60fc-e76acf61c22a)

## Requirements

The configuration for blocking malware is automatic once the Repository Firewall and Zscaler integration is configured. A few additional settings need to be manually set on in Zscaler.

## Configuration

An administrator account is required to configure the Zscaler integration. The settings are found in the settings menu for Repository Firewall.

See [Getting Started Zia API](https://help.zscaler.com/zia/getting-started-zia-api)

![fw-zscaler-configuration.png](/assets/images/uuid-4e1bc9fe-8bbf-2f74-880c-7760c9c041e6.png)

### Credentials

Provide your Zscaler administrator account credicatials. This user must be in the `Zscaler Global Administrators` group.

### Hostname

The hostname is the url for your zscaler deployment.

### API Keys

Generating a Zscaler API Key involves accessing the API Management section within the specific Zscaler Admin Portal you are using. The exact navigation path and some options might differ slightly depending on the Zscaler product. Consult the Zscaler Help Portal for the specific product you are using.

See [Zscaler Help Portal](https://help.zscaler.com/zia/managing-cloud-service-api-key)

### Configured Formats

Set the formats to be covered with Zscaler. Included formats use more available Zscaler custom URLs.

![fw-zscaler-configuration-formats.png](/assets/images/uuid-fb90a13b-b185-8739-c261-f5c84bfcc5c5.png)

**Note:** Trigger an Update to Zscaler There is up to a 24-hour delay when configuring ZScaler before data is sent to the service. You may trigger the service to update immediately using the API. POST /api/v2/config/zscaler/update

## Zscaler Custom URLs

The Zscaler integration uses custom URLs to restrict access to the active verified malware components covered by your configured formats. These are added as `User Defined` categories under the *Zia Administrator* → *Resources* → *URL Categories* with the following naming:

```
sonatype-{format}-shadow-download-defense
```

Zscaler has limits on custom URLs for performance, scalability, and manageability of its security service. These limits ensure the platform can efficiently process vast amounts of internet traffic for all its users without degradation. When Zscaler does not have enough available custom URLs to catalog the known malware for a specific ecosystem, you are not fully protected.

The default limit for custom URLs/TLDs is 25K. Contact your Zscaler Account team to subscribe to up to an additional 50K custom URLs/TLDs.

See [Zscaler Documentation](https://help.zscaler.com/zia/ranges-limitations)

![fw-zscaler-customer-url-limits.png](/assets/images/uuid-798b2efc-a594-51a9-155c-0204e80f4fff.png)

- The number of custom URLs allowed with your subscription.
- The number of custom URLs remaining.
- The status of the Repository Firewall integration. *Not Configured* → The integration has not yet been configured and verified. *OSS Malware Catalog Synced* → Zscaler is configured and malicious urls are under the current limit. *Zscaler Custom URL Limit Exceeded* → The limit is reached and there are more malicious urls to push.
- *Not Configured* → The integration has not yet been configured and verified.
- *OSS Malware Catalog Synced* → Zscaler is configured and malicious urls are under the current limit.
- *Zscaler Custom URL Limit Exceeded* → The limit is reached and there are more malicious urls to push.

## FAQ

- The Zscaler integration is supported for the following formats for automatic Malware detection:
- Repository Firewall create custom User Define URL categories by component format. These endpoints are updated once daily.

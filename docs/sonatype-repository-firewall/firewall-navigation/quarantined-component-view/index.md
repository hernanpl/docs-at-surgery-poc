---
layout: default
title: "Quarantined Component View"
parent: Firewall Navigation
nav_order: 2
has_children: true
---

# Quarantined Component View

The quarantined component view is a temporary page created when a component is first quarantined that does not require authentication to access. The view displays the details of quarantined components, a list of the violations, and offers remediation advice. This view is available for 12 hours from the time the component is first requested with the link available in the build output.

Components are quarantined when a component is requested from a proxy repository for the first time. The build tool making the request receives a `403` error when the component is not downloaded. The error code provides details of the quarantine and a link to the quarantined component view.

![113248445.png](/assets/images/uuid-9f41891a-0401-2b7f-8e3d-d7757714d6f2.png)

**Note:** When users are authenticated with IQ server and not using anonymous access, they are directed to the Component Details View. To view the component details or the full Repository Results report, the user requires the `View IQ elements` permission. The `View IQ elements` permission is not assigned by default to the `Application Evaluator` or the `Component Evaluator` service account roles which are granted limited access to the user interface.

## Viewing the quarantined components

The quarantined component view provides information about the component including its policy violations and remediation strategies.

- This section indicates that the requested component has been quarantined.
- The title of the section is the component name. The rest of the section provides information on the component's current status, including the First Quarantined Date and Other Allowed Versions in the Repository
- This tab provides information to remediate the violations causing quarantine. The Recommended Versions section suggests versions without failing policy violations. This section includes the Version Explorer to compare versions visually.
- This section lists the failing violations. When upgrading a component is not available, all failing policy violations must be waived to release the component from quarantine.
- This section lists other allowed versions already present in your repository. These versions are not quarantined and can be downloaded without issue. Substituting the requested version with a version listed in this section is a potential alternative to a waiver request.

## Disabling Anonymous Access

The Quarantined Component View link does not require authentication to view. This simplifies access for engineers who may not be allowed to log into the Repository Firewall Dashboard. The information on this page is limited and the length of time it is accessible is relatively short, so there is little risk of exposing secured data.

However, we do recommend disabling anonymous access when your service is accessible to users outside of your organization or is reachable through the public internet.

Disable anonymous access using the [Repository Firewall REST API](#UUID-d516f5b1-1573-aae2-7261-107d95f5fb67) .

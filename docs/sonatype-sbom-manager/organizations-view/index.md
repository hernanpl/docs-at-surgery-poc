---
layout: default
title: "Organizations View"
parent: Sonatype SBOM Manager
nav_order: 7
has_children: true
---

# SBOM Manager Organizations View

Use the Organizations view to manage access to your software catalog with the same hierarchy as your business units and third-party vendors. This view is structured in a parent-descendant relationship with applications and nested business units.

![SBOM_Manager_-_Organizations_view.png](/assets/images/uuid-4ab2df1e-ab64-0e43-51ca-de7eb5a4f526.png)

Access is granted by assigning a user a specific role for an organization or application. The user will fill that role for the organization and its descendants. Use the default roles or create custom roles.

See the documentation for details.

Policies are the rules that define your organization's risk tolerance for using open source software. While Sonatype SBOM Manager provides a reference policy set, organizations with multiple licenses can use Sonatype Lifecycle to customize these policies to better meet specific requirements. Policies are best set at the highest level to be inherited by all organizations and applications. You may narrow the inherence of certain policies using application categories to scope the policies to a subset of applications.

See for details on customizing policies.

## Adding organizations and applications

Organizations and applications may be added from the side navigation by selecting the plus sign next to the headers. Organization and application names must be unique even when nesting inside other organizations.

Select an organization to view current applications and add new ones. The Application ID is used to reference your applications during evaluations using the scanner tools or API.

![Screenshot_2024-05-15_at_9_29_44_PM.png](/assets/images/uuid-2fd9886d-e27c-a66b-3fa8-fda9f0563445.png)

Applications and Organizations may also be added using the API.

---
layout: default
title: "Add-on Packs"
parent: Sonatype IQ Server
nav_order: 9
---

# Add-on Packs

**Note:** The Advanced Development Pack (ADP) capabilities have been integrated into the general Lifecycle product. These changes are accessible with IQ Server version 100 and above. For customers with IQ server versions between 100 and 134, your admin may need to re-upload your organization’s existing Lifecycle license or restart the IQ Server to see these additional capabilities.

## Advanced Legal Pack

Sonatype’s Advanced Legal Pack (ALP) is an add-on to Sonatype Lifecycle (release 108 and higher) that helps your organization streamline open-source software (OSS) license compliance, mitigate license risk, and expedite feedback between legal and development teams.

### Features of Sonatype Advanced Legal Pack (ALP)

**Attribution Reports**

- Automated generation of attribution reports that comply with more than 90% of OSS license obligations
- Customizable and editable attribution reports
- Provides the ability to save attribution and obligation resolutions on a per component (or per license) basis, for future reference
- Accurate and dependable attribution data to comply with legal requirements for cloud computing or third-party governance

**ML-enabled Source Code License Detection**

A new machine learning model incorporated into the ALP extends the functionality of detecting source code or observed licenses beyond the Maven ecosystem to [Sonatype's premium ecosystems](#UUID-a7f26522-01ae-eca4-b507-f0bffd06e746) . The ML-enabled license detection offers:

- Unparalleled accuracy
- Disambiguation between a library's attributions and attestations and its own licenses
- Full legal risk profile of a third party dependency

**Extended Legal Data**

- Extended legal data for components to make legal decisions or fulfill legal obligations
- Includes data that is required to be preserved or attributed to in liberal licenses, for e.g. notice texts, license texts and copyright statements
- Automated collection of all copyrights, required notices, and license texts identified in a given OSS component for [Sonatype's premium ecosystems*](#UUID-a7f26522-01ae-eca4-b507-f0bffd06e746) .

**Legal Compliance Workflow**

- ALP’s legal compliance workflow makes it easy for legal reviewers to examine the extended legal data and fulfill legal obligations.
- When a reviewer decides that an obligation has been fulfilled, that work can be saved at the global, organization, or application level to ensure that future uses of the same component benefit from the same review.
- ALP’s workflow provides obligation management in compliance with industry standards.

For more information on the ALP, please see:

- [Advanced Legal Pack](https://www.sonatype.com/products/advanced-legal-pack) overview page

## Advanced Legal Pack Quickstart

### Using the Advanced Legal Pack

Log in to Sonatype Lifecycle or Sonatype SBOM Manager and select **Legal** from the navigation menu. Use the *Legal Obligations* page to manage your legal obligations and attributions.

You can manage your legal obligations and attributions from this page.

The *Applications* tab contains a list of all applications detected during the last scan. The *Components* tab contains all components used by every application scanned by the Sonatype IQ Server

From here, you will be able to manage your legal obligations and attributions via the *Legal Backlog* . The *Legal Backlog* provides a list of your applications with information on the last scan, application categories, and the components reviewed.

On the *Applications* tab, you'll see a list of every application known by your IQ Server. Use the *Filter* button at the top right to narrow your results by organization, application, application category, stage, or review progress. Clicking the *Create Attribution Report* will create an attribution report for all the applications currently filtered for.

On the *Components* tab, you'll see a list of every component in every application known by the IQ Server. Like before, use the *Filter* button at the top right to narrow your results by organization, application, application category, stage, or review progress.

![example of the Legal Backlog page](/docs-at-surgery-poc/assets/images/uuid-5e8e1b9c-3607-7348-7cef-a92ff762ced2.png)

Selecting an application from the *Applications* tab takes you to the *Application Legal Details* page. Here, you will see a list of all components in that application, and view details on their licenses, completed obligations, and review status. This is also where you can create an *Attribution Report* for just the selected application.

Click on the *Create Attribution Report* as shown below.

**Note:** The report generation time for *Attribution Reports* could be longer for a large no. of applications or components. We estimate a response time of 1 minute for generation of attribution reports for around 1000 components. For environments using reverse proxy, we recommend increasing the reverse proxy timeout to generate *Attribution Reports* for a large no. of applications or components.

Refer to [License Legal REST API](#UUID-ae622dee-2c48-11f3-5a4c-92d5727a91cd) for more information on *Attribution Report* templates and other customizations.

![166330437.png](/docs-at-surgery-poc/assets/images/uuid-2b466175-e3de-ea96-541d-30db5542af0c.png)

Selecting a component from the *Applications Legal Details* page or the *Components* tab of the *Legal Backlog* takes you to the *Component License Details* page. The top portion of the screen gives you an overview of your review progress and other license details. The remainder of the screen is where you will review your license obligations, and add or edit copyright statements, notice texts, license texts, and attributions.

![example of the component license details page](/docs-at-surgery-poc/assets/images/uuid-ff6ad6d4-5aea-c1e4-ef38-9fbeae81a940.png)

### Example Workflows with the ALP

Most legal teams don’t currently have a tool to support their work and rely on manual processes to manage compliance and licensing. The ALP automates and reduces these manual, time-consuming tasks. See below for some examples:

### License Obligations

On the left side, each type of legal obligation is color-coded for easy reference. When you click one of these color-coded items, the view automatically scrolls to the corresponding section of the license text on the right. This makes it quick and straightforward to see exactly where each obligation appears in the full license.

![ALP_-_license.png](/docs-at-surgery-poc/assets/images/uuid-f99e1348-15bb-37d2-5d8f-b3ea4977f31d.png)

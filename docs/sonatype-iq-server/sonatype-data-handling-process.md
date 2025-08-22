---
layout: default
title: "Sonatype Data Handling Process"
parent: Sonatype IQ Server
nav_order: 13
---

# Sonatype Data Handling Process

Sonatype works hard to ensure the proper handling of data received from our customers via our products (the “Product Data”) by focusing on the governance, classification, security, transmission, and overall management of such Product Data. This document provides an overview of how Product Data is generally managed and processed by Sonatype.

## Data Access

Access to Product Data is managed through an approval process using a ticketing system whereby owners of specific systems that include Product Data allow and revoke access based on Sonatype’s internal information classification standards.

## Encryption Standard and Security

All Product Data stored and processed by Sonatype is encrypted at rest and in flight. Sonatype’s [Information Security Program](https://www.sonatype.com/security-at-sonatype) is based on ISO 27000 and National Institure of Standards and Technology (NIST) standards.

## Data Categories

Product Data consists of the following types of data collected via Sonatype products:

- Scan Data, as further defined below, is data used to process Software Composition Analysis scans that provide open source intelligence to the users of Sonatype products.
- Product Usage Analytics, as further defined below, is data transmitted and collected about the use of Sonatype products for the purpose of improving those products.

Sonatype treats all Scan Data and Product Usage Analytics as customer confidential information.

### Scan Data

“Scan Data,” means Information transmitted when an application scan is performed using any solution running on the Sonatype IQ Platform and is comprised of:

- Hashed identifiers (“Hashed IDs”) that uniquely and securely identify the open source components present within the application being scanned as identified by the Sonatype IQ scanner; and
- Hashed Sonatype product license information used to validate that data being transferred to the Sonatype Data Service is being received from a valid Sonatype IQ Platform user (“Validation ID”)

When an application scan is performed, the Sonatype IQ Platform analyzes the application to identify open source software components present within that application via Hash IDs. Each Hash ID is hashed with a one-way hash algorithm and is transmitted to the Sonatype Data Service along with the Validation ID. Once transmitted to Sonatype, if sent by an authorized Validation ID, Sonatype’s Data Service is queried so that details and intelligence related to each Hash ID can be transmitted back to the user’s instance of the Sonatype IQ Platform.

### Product Usage Analytics

Actions and activity performed using Sonatype products (including pages viewed, actions taken, scans performed, size of repositories, and other similar findings) are transmitted to Sonatype’s analytics system. Product Usage Analytics (a) do not contain personally identifiable information (PII), (b) are used to support an individual user, and (c) are used to improve the product experience and capabilities for all customers.

### Data Selling and Sharing

Sonatype does not sell Product Data to third parties.

### Data Storage and Processing

Product Data is processed in Sonatype’s multi-vendor solution that is designed to be resilient and guard against down time, relying on third party infrastructure for storage and backup. Sonatype also uses third parties to manage Product Data aggregation and reporting.

### Data Retention

Product Data may be retained as long as it remains strictly relevant regarding Sonatype’s analysis of historical and trending use of the products.

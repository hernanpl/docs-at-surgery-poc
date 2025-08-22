---
layout: default
title: "Advanced Search View"
parent: Sonatype SBOM Manager
nav_order: 8
has_children: true
---

# SBOM Manager Advanced Search View

Use the SBOM Search to understand where components and vulnerabilities exist across your catalog of SBOMs directly from the UI. Export the results to build reports to share anywhere you need them.

![Screenshot_2024-04-17_at_5_30_15_PM.png](/assets/images/uuid-82de7216-c44b-218c-9393-467bfdc6e7a8.png)

## Advanced Search

The Advanced Search feature allows you to search the configuration and component details from the UI.

This feature is enabled by default and the search index is created automatically. System Administrators may manually recreate a search index from the Advanced Search configuration. This page is accessible from the System Preferences menu. The enabled checkbox needs to be checked before recreating the index. The last indexed time will display once the index has successfully been created.

The Advanced Search does not return policy violations.

- Use the for searching policy violations.
- Use the to search for quarantined components.
- To script advanced searches, use .

The Advanced Search automatically re-indexes when changes are made to the data. Automatic indexing only applies to data changes made while the feature is enabled.

Advanced Search feature retrieves results from large data sets. To limit risk to the performance of the server by consuming too much of the service resources, limits to the query results are in place. You will see an error message asking you to narrow down the search when this occurs.

You may export the results of an advanced search by selecting the Export Results button from the Advanced Search page. The search results are downloaded in a CSV file.

Results may also be exported using the Advanced Search REST API.

![123404564.png](/assets/images/uuid-d2294c03-fd72-00e4-ba1e-94ff8ecb445f.png)

**Note:** Limitations with the Advance Search The Advance Search does not list all vulnerabilities known to Sonatype. The complete list of vulnerabilities are stored in Sonatype's proprietary Hosted Data Services (HDS) database and is used during the application analysis.

### Performing a Search

Fine-tune the search query by combining multiple search terms/item types with the supported search syntax. Such queries are used to find specific organizations, applications, components, and policies by names, IDs, etc.

Steps to use Advanced Search:

Selecting any search item type from the Component category will give an option to retrieve:

You can search for components or vulnerabilities in applications that belong to a specific organization by including the organization name or organization ID in the search query.

The search retrieves components and vulnerabilities from applications directly managed by the organization specified in the search query.

Searching into the organization hierarchy is not supported by the Advanced Search. Including an organization in the search query will not retrieve results for its child organizations.

## Search Examples

The following are examples using the Advanced Search.

### Single field search

VulnerabilityId is used when no fieldName is specified. Results exactly match the value.

```
fieldName:value
```

```
vulnerabilityId:value
```

### Searching for multiple phrases separated by whitespace

Use quotes when the search requires you include a space.

```
fieldName:"value1 value2"
```

### Boolean operators for multiple fields search

Boolean operators are case-sensitive. When no boolean operator is specified the `OR` operator is used.

`OR` or `||` must satisfy one condition or the other condition

```
fieldName1:value1 OR fieldName2:value2
fieldName1:value1 || fieldName2:value2
```

`AND` or `&&` must satisfy both conditions

```
fieldName1:value1 AND fieldName2:value2
fieldName1:value1 && fieldName2:value2

```

`NOT` or `!` or `-` must not be the condition

```
fieldName1:value1 NOT fieldName2:value2
fieldName1:value1 ! fieldName2:value2
fieldName1:value1 - fieldName2:value2

```

### Using boosting operator

A boosting operator is used to specify the relevancy order for the search results. You can boost a term within a query to increase its relevance by changing the order in which it appears in the results.

```
fieldName1:value1^x OR fieldName2:value2
```

Note that `x` , must be positive, may be fractional, with the default of 1.

### Search using wildcards * and ?

These results have a value starting with 'v' following with zero or many characters

```
fieldName:v*
```

These results have a value starting with 'v' following with any single character

```
fieldName:v?
```

### Search using regular expressions (regex)

These result have a value matching the regular expression.

```
fieldName:/regularExpression/
```

### Search using fuzzy expressions

These results have some value within 0 to 2 edits of the search value.

```
fieldName:value~x
```

When no maximum (x) is specified, then the default number of 2 is used

```
fieldName:value~2
```

### Search using proximity expressions

These results have each value within x words of the other. Effective with fields consisting of multiple words, like description fields.

```
fieldName:"value1 value2"~x
```

### Search based on a range

These results include both values

```
fieldName:[value1 TO value2]
```

These results are exclusive of the values

```
fieldName:{value1 TO value2}
```

### Search by grouping values

Grouping values are effective with fields consisting of multiple words, like description fields.

```
fieldName:((value1 OR value2) AND value3)
```

```
(fieldName1:value1 OR (fieldName2:value2 AND fieldName3:value3))
```

### Escape characters while building the search query

The list of special characters; can be escaped using a backslash `\` character.

```
+ - && || ! ( ) { } [ ] ^ " ~ * ? : \ /
```

## Reference- search item types and field names

Refer to the tables below for search item types and examples when building a search query.

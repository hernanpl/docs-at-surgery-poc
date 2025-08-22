---
layout: default
title: "Search Examples"
parent: Advanced Search View
nav_order: 1
---

# Search Examples

The following are examples using the Advanced Search.

## Single field search

VulnerabilityId is used when no fieldName is specified. Results exactly match the value.

```
fieldName:value
```

```
vulnerabilityId:value
```

## Searching for multiple phrases separated by whitespace

Use quotes when the search requires you include a space.

```
fieldName:"value1 value2"
```

## Boolean operators for multiple fields search

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

## Using boosting operator

A boosting operator is used to specify the relevancy order for the search results. You can boost a term within a query to increase its relevance by changing the order in which it appears in the results.

```
fieldName1:value1^x OR fieldName2:value2
```

Note that `x` , must be positive, may be fractional, with the default of 1.

## Search using wildcards * and ?

These results have a value starting with 'v' following with zero or many characters

```
fieldName:v*
```

These results have a value starting with 'v' following with any single character

```
fieldName:v?
```

## Search using regular expressions (regex)

These result have a value matching the regular expression.

```
fieldName:/regularExpression/
```

## Search using fuzzy expressions

These results have some value within 0 to 2 edits of the search value.

```
fieldName:value~x
```

When no maximum (x) is specified, then the default number of 2 is used

```
fieldName:value~2
```

## Search using proximity expressions

These results have each value within x words of the other. Effective with fields consisting of multiple words, like description fields.

```
fieldName:"value1 value2"~x
```

## Search based on a range

These results include both values

```
fieldName:[value1 TO value2]
```

These results are exclusive of the values

```
fieldName:{value1 TO value2}
```

## Search by grouping values

Grouping values are effective with fields consisting of multiple words, like description fields.

```
fieldName:((value1 OR value2) AND value3)
```

```
(fieldName1:value1 OR (fieldName2:value2 AND fieldName3:value3))
```

## Escape characters while building the search query

The list of special characters; can be escaped using a backslash `\` character.

```
+ - && || ! ( ) { } [ ] ^ " ~ * ? : \ /
```

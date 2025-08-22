---
layout: default
title: "Naming conventions for OSS licenses"
parent: Sonatype IQ Server
nav_order: 14
---

# Naming conventions for OSS licenses

Sonatype uses a custom identifier for licenses discovered by Sonatype. This identifier is a combination of tags from the original license text such as the company name, package name, and type of license.

Sonatype license identifiers are of two types:

## Short name identifiers

A short name identifier is a concatenated string of a series of tags.

```
[tag2]-[tag1]-[tag3]-variant-[tag4]
```

## Long name identifiers

Long name identifiers are descriptive license names limited to 200 characters. They may include any of these ASCII characters:

```
alphanumeric, punctuation, parentheses
```

Long names will not include other characters, lending, or trailing spaces

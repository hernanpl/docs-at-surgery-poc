---
layout: default
title: "Java Compatibility Matrix"
parent: Sonatype Product Overview
nav_order: 3
---

# Java Compatibility Matrix

**June 2024** - Sonatype announced sunsetting support for Java 8 and 11 for Sonatype Nexus Repository, Sonatype IQ Server, and the IQ CLI Scanner.

**July 2024** - the IQ CLI Scanner release 179 and Sonatype Nexus Repository 3.70.x split into extended maintenance versions to continue to support Java 8 and 11. These extended maintenance versions will only receive critical bug fixes and security patches as defined in our [sunsetting documentation](https://help.sonatype.com/en/sonatype-sunsetting-information.html#UUID-217b96ec-8a06-93ff-b373-ab40751a5647_id_SonatypeSunsettingInformation-ExtendedMaintenance) .

Versions beyond IQ 179 and Sonatype Nexus Repository 3.70.x only support Java 17.

The table below details which versions of Sonatype's solutions are compatible with Java 8, 11, and 17.

| Product/Version | Java 8 | Java 11 | Java 17 |
|---|---|---|---|
| **Sonatype Nexus Repository** | | | |
| 3.69.x and earlier | ✅ | ✅ | ❌ |
| 3.70.x (Extended Maintenance) | ✅ | ✅ | ❌ |
| 3.71.x and later | ❌ | ❌ | ✅ |
| **Sonatype IQ Server** | | | |
| Release 178 and earlier | ✅ | ✅ | ❌ |
| Release 179 (Extended Maintenance) | ✅ | ✅ | ❌ |
| Release 180 and later | ❌ | ❌ | ✅ |
| **IQ CLI Scanner** | | | |
| Release 178 and earlier | ✅ | ✅ | ❌ |
| Release 179 (Extended Maintenance) | ✅ | ✅ | ❌ |
| Release 180 and later | ❌ | ❌ | ✅ |

**Note:** Avoid non-numeric characters in Java version numbers The Java version detection in the solutions only supports versions using a dot numeric notation. The use of non-numeric chars is not supported. Example "17.0.3-internal"

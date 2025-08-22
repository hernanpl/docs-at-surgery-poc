---
layout: default
title: "Reachability Analysis"
parent: Sonatype Developer
nav_order: 5
---

# Reachability Analysis

As applications grow in size and complexity, so does the potential for vulnerabilities. The attack surface also expands with increased reliance on open-source software components. Given tight deadlines and competing priorities, it is often impractical to remediate every vulnerability. A pragmatic way to approach a near-zero risk state in a limited timeframe is to target the open-source software vulnerabilities that lie along the execution paths of an application i.e. are *reachable* .

Reachability Analysis allows you to identify these exposed components. When integrated into application scans, this analysis can detect which vulnerable components are accessible, labeling any associated policy violations as "Reachable" in the application report. The remediation efforts can then be targeted towards these "Reachable" policy violations.

## How does Reachability Analysis Work?

**Note:** Supported Languages Reachability Analysis currently supports Java only.

Reachability Analysis is designed to run on Java (or any JVM language) binaries within the scan target. When enabled during application scans, it examines both the application binaries and their dependency binaries in the scan target folder.

If a vulnerable component is detected **and** the application code calls a specific method in that component which could be exploitable, the policy violation is labeled as "Reachable".

If a vulnerable component is found but the application code **does not execute any calls** to the vulnerable method, the policy violation is labeled as "Not Reachable".

If a vulnerable component is detected and the application code calls a specific method in that component which could be exploitable, the policy violation is labeled as "Reachable." Conversely, if a vulnerable component is found but the application code does not execute any calls to the vulnerable method, the policy violation is labeled as "Not Reachable."

**Example**

Consider an XML reader application that has a dependency on **com.vulnerables.utils: vulnerable-deserializer:1.5** . It has an endpoint that receives an XML file. The endpoint code reads the content of the XML file using the method **XMLReader.readFile()** and renders it on-screen. Based on our security data, the method **readfile()** has known vulnerabilities and public CVEs .

Reachability analyzes the .jar files created by the build tool and scans the method signatures to identify the vulnerable methods that are reachable. The policy violation for the component **com.vulnerables.utils: vulnerable-deserializer:1.5** is labeled as "Reachable." This will be displayed in the policy evaluation report for the corresponding scan and on the Violations Dashboard.

The XML reader application also has a feature that allows users to write the XML input to a LaTeX document and export it. One of the methods of the LaTeX library is vulnerable to remote command execution. Due to its known vulnerability, this method is never called and so is not in the execution path. Reachability Analysis **will not** label the policy violation as "Reachable."

## Using Reachability Analysis

Reachability Analysis is currently supported on all Sonatype CI integrations:

The examples below are for the [Sonatype Platform Plugin for Jenkins](#UUID-0d46c567-a411-72f8-7973-d8f4cf7e00b2) integration, which currently supports a fine-grained configuration for the feature. However, the principles apply to some extent to all CI integrations.

**Note:** For Best Results with Reachability Analysis Results for Reachability Analysis depend on the strategy used to select the types of methods to scan and the selection of namespaces to narrow down the scan entry points.

### Strategies for Enabling Reachability Analysis

- **Minimal Configuration** The example below shows using the Reachability Analysis with minimal configuration.
- **Method Selection** This is currently available only for Reachability Analysis performed on [Sonatype Platform Plugin for Jenkins](#UUID-0d46c567-a411-72f8-7973-d8f4cf7e00b2) and [Sonatype for Bamboo Data Center plugin](#UUID-6737c02e-b17a-00be-be43-2506c487b028) . You can use one of the following available strategies for method selection for scans with Reachability Analysis enabled: `JAVA_MAIN` :Selects all methods matching `public static void main(String[] args)` `PUBLIC_CONCRETE` : Selects public non-abstract/synthetic methods from non-interface/annotation classes `ACCESSIBLE_CONCRETE` : Selects public/protected non-abstract/synthetic methods from non-interface/annotation classes. This is the default entry point strategy. `CONCRETE` : Selects all non-abstract/synthetic methods from non-interface/annotation classes. `ALL` : Selects all methods from all non-interface/annotation classes. You can enable the Reachability Analysis feature with the minimal configuration as below: **Example:** The example below shows how to enable the Reachability Analysis feature with the `ACCESSIBLE_CONCRETE` strategy.
- **Selection of Namespaces** Select the methods that should be considered as entry points (points in code where execution begins) for the analysis. Namespaces are specified at the level of packages. All packages nested under a namespace are considered for entry point selection. If multiple namespaces are specified, all of them will be included. Reachability Analysis will start with the namespaces specified and subsequently analyze all others in the execution path. **Example:** Consider the following project structure: The Reachability Analysis feature is configured as follows: In the example above, the namespaces property specifies the namespace `'com.sonatype.iq'` , which will be considered as the entry point for the analysis. This namespace has `domain` , `application` , and `repository` packages under its scope. Methods belonging to `DomainClassOne.java` class (under the domain package in the `'com.sonatype.iq'` namespace) will be analyzed before other methods in the package classes. Similarly, methods belonging to classes under other applications and repository packages will be analyzed at the start of the analysis for the package. Packages of type wrappers, with namespace `'com.sonatype.wrappers'` and config packages with namespace `'com.sonatype.configs'` will be omitted when an entry point for the analysis is being established. Similarly, methods belonging to the `OktaLoginWrapper` class with namespace `'com.sonatype.wrappers.OktaLoginWrapper.java'` will be omitted when establishing an entry point. **Notes:** An entry point is any method signature that aligns with the selected strategy. For example, for `JAVA_MAIN` strategy, all entry point methods have `public static void main` as method signature. You can use regular expressions when specifying the namespace. Example: For `org.foo.example` , you can use regular expressions with `'/'` at the start and end of the string as `/^org\\.+.*\\.example\$/`
- An entry point is any method signature that aligns with the selected strategy. For example, for `JAVA_MAIN` strategy, all entry point methods have `public static void main` as method signature.
- You can use regular expressions when specifying the namespace. Example: For `org.foo.example` , you can use regular expressions with `'/'` at the start and end of the string as `/^org\\.+.*\\.example\$/`
- **Using the Parameter Includes** Multi-module projects could have several .jar files when built. Many of these .jar files are dependencies of another .jar file, which could be the one containing the main application. By specifying the path to this specific .jar when running reachability analysis, you can avoid multiple evaluations of the same .jar files, which would occur when: .jar files are evaluated separately, and .jar files are evaluated when invoked by the main application. The includes parameter specifies a target path for the artifacts to be analyzed. It limits the scope of the analysis, resulting in better precision and reducing the utilization of system resources. **Example:** If `includes` is omitted, the target location for the analysis will be the same as specified in the `iqScanPatterns` of the `nexusPolicyEvaluation` in the Jenkins file. This may increase the scope of the target analysis, leading to reduced precision.
- .jar files are evaluated separately, and
- .jar files are evaluated when invoked by the main application.
- **Analysis Algorithm** These are the supported algorithms for Java reachability analysis: `CHA` (Class Hierarchy Analysis): A static call analysis that considers all methods in all possible loaded subclasses. `RTA` (Rapid Type Analysis): Similar to CHA, but improves precision by analyzing only classes instantiated during program execution. `RTA_PLUS` : Sonatype’s version of RTA, offering even greater precision and serving as the default algorithm.
- `CHA` (Class Hierarchy Analysis): A static call analysis that considers all methods in all possible loaded subclasses.
- `RTA` (Rapid Type Analysis): Similar to CHA, but improves precision by analyzing only classes instantiated during program execution.
- `RTA_PLUS` : Sonatype’s version of RTA, offering even greater precision and serving as the default algorithm.

### Error Handling

By default, Jenkins will mark the pipeline as `FAILURE` if there are any error conditions in executing Reachability Analysis.

To avoid a pipeline `FAILURE` , set the value of the `failOnError` parameter to `false` (it is `true` by default). Jenkins will mark the pipeline as `UNSTABLE` .

```
reachability: [
  failOnError: false,
  logLevel: 'DEBUG',
  javaAnalysis: [
    enable: true,
    entrypointStrategy: 'ACCESSIBLE_CONCRETE'
  ]
]

```

### Expected Outputs

Reachability Analysis yields different outputs for a wide range of scenarios. The outputs depend on the type of artifacts analyzed, strategies used, and fine-tuning using the performance-enhancing parameters described above.

Reachability Analysis output is logged within the IQ Policy Evaluation log and can be found at the stage where policy evaluation is called within your pipeline.

Here are descriptions to a few sample outputs:

**Sample output 1** : Policy violations labeled as Reachable

On successful execution of Reachability Analysis, the number of "Reachable" components found will be logged as:

```
2024-07-25 15:08:32 GMT-05:00  [INFO] CallflowReachableMethodsCommand - Found 2 reachable methods
```

To view the actual method signatures of reachable methods, the **logLevel** should be set to `DEBUG` . However, this may lead to a lot of logging text and make the logs unreadable.

The *Application Report* will show the policy violations for components (belonging to the Maven ecosystem) that contain vulnerable method signatures.

**Example**

![image-20240730-195825.png](/docs-at-surgery-poc/assets/images/uuid-64197aff-7717-18eb-8c36-9bedef79bd42.png)

Click on the policy violation to open the violation details view.

![image-20240730-200459.png](/docs-at-surgery-poc/assets/images/uuid-ddad88b7-7b47-0a91-25f1-e7ebd80e4adf.png)

For releases 192 and later, the policy violations tab on the application report contains [The Reachability Column](https://help.sonatype.com/en/component-details-page.html#policy-violations-tab) to indicate the Reachability status of the violation.

**Sample output 2** : Policy violations labeled as "Not Reachable"

This occurs when Reachability Analysis does not find any "Reachable" methods. This means that there are no vulnerable components in the execution path of the analyzed application.

This scenario will appear in the log as:

```
2024-07-25 15:39:21 GMT-05:00 [INFO] CallflowReachableMethodsCommand - Found 0 reachable methods
```

**Sample output 3** : Reachability Analysis analysis skipped

This occurs when there are no vulnerable components found during the policy evaluation. Reachability Analysis is skipped.

This is logged in the pipeline log as:

```
2024-07-25 15:38:03 GMT-05:00 [INFO] Skipping callflow analysis; missing vulnerable component method data
```

⚠️ **Warning:** The absence of "Reachable" methods does not guarantee safety. The analysis may not have been able to detect these methods due to misconfiguration of the feature. We recommend checking these configurations thoroughly, at the start of the analysis.

## Other Considerations While Running Reachability Analysis

This section describes some more considerations when performing Reachability Analysis.

- **Running in multi-module projects** For a project that has multiple modules and produces multiple artifacts, Reachability Analysis should be configured with one of the [strategies](#UUID-bffb3d6e-1a0b-5607-518a-3dcdc88508c2_section-idm234473410174073) described above, for accurate results. If a project produces two different artifacts, for example, one .jar file for a client service and one .jar file for a server, each of these .jar files should be evaluated separately. We recommend setting up a separate pipeline in Jenkins, one that produces the client .jar and one that produces the server .jar. This way you can use the [includes](#UUID-bffb3d6e-1a0b-5607-518a-3dcdc88508c2_N1744208072662) parameter to specify the artifact you want to analyze on each pipeline. If a multi-module project has modules that are meant to be used as a library for other projects, using `JAVA_MAIN` will not produce any "Reachable" methods. This is because none of the modules will have the methods with the signature **public static void main** . In such cases, it is best to use `ACCESSIBLE_CONCRETE` or `PUBLIC_CONCRETE` in the [strategies](#UUID-bffb3d6e-1a0b-5607-518a-3dcdc88508c2_section-idm234473410174073) section above.

- **Execution Times** Reachability Analysis can be a time and memory intensive process, depending upon the size of the project that is being analyzed. The execution involves going through all entry points specified, creating a call graph, and process the code to detect vulnerable methods in the execution path. This could be a huge overhead if your project has millions of lines of code, lots of dependencies and entry points. To reduce the execution times, here are some recommendations: If your project has a releaseable main branch, run Reachability Analysis on the main branch instead of all the feature branches on each new commit. If you have changes in the project manifest, run Reachability Analysis in the feature branches. This is a trade off between build time and the extra analysis step due to Reachability Analysis. Run Reachability Analysis at fixed times, for example, on nightly builds. If you have multi-module projects, separate the projects before running Reachability Analysis.
- If your project has a releaseable main branch, run Reachability Analysis on the main branch instead of all the feature branches on each new commit.
- If you have changes in the project manifest, run Reachability Analysis in the feature branches. This is a trade off between build time and the extra analysis step due to Reachability Analysis.
- Run Reachability Analysis at fixed times, for example, on nightly builds.
- If you have multi-module projects, separate the projects before running Reachability Analysis.

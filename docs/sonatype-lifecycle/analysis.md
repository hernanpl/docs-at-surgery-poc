---
layout: default
title: "Analysis"
parent: Sonatype Lifecycle
nav_order: 8
---

# Analysis

Whether researching new components or tracking open-source in production, you can scan your applications throughout your software development lifecycle (SDLC) using the Sonatype Lifecycle evaluation process

## Sonatype Lifecycle Evaluation Process

## Advanced Binary Fingerprinting (ABF)

We examine binary fingerprints (similar to a truncated sha1 hash) of the files and not just the file names and manifests. ABF examines everything included in the application after the build, including any embedded dependencies. An ABF scan will not return false positives in its report. Sonatype data is tied to the component fingerprints of any files where the vulnerability is discovered. When a vulnerability is reported it is because the component fingerprint is in your application. Depending on the environment, there are a few points where this might be confusing.

## Manifest Evaluation

Scans performed before the application has been built do not have open-source dependencies to fingerprint and must therefore leverage package-lock and manifest files to scan. This happens when directly analyzing the source control repositories or software bill of materials earlier in the development lifecycle. The Lifecycle scanners can use the lock or manifest files to get an idea of what should be in the final application. This will include any transitive dependencies if they are included in the lock file. Otherwise, it will report on only what is requested in the manifest.

- Lifecycle integrations will default to ABF scans as they are accurate to what is in your application.
- They will then look for lock files followed by manifest files.
- As we provide feedback earlier in the development/design process, manifest scanning becomes the only option for providing the earliest possible feedback during component selection.

**Note:** As a best practice, we recommend development teams include lock files with fixed versions with their project manifests. To guarantee a repeatable build, ranges are ignored.

## Sonatype Lifecycle Data Analysis

Sonatype Lifecycle uses data derived from our automated vulnerability detection system — basically, a big funnel of sources (NVD, GitHub commits, OSS Index, Sonatype research, etc.) that is processed with automated techniques such as data filtering, aggregation, and machine learning algorithms.

- Most ecosystems have security, license, and identity data, while a few only have security and identity data.
- License data includes open source licenses identified in the package manifest, and in the case of Java, any licenses are also observed within the package itself.
- Identity refers to component details such as recommendations, version graphs, or cataloged data pulled from the package manager repository.
- We categorize these ecosystems as having either Premium or Standard data capabilities.

## Premium Capabilities

For most ecosystems, Sonatype researchers triage incoming data and determine if there is a vulnerability, creating a research ticket for further investigation when necessary. Tickets are prioritized and then entered into our human-curated research process. When research is complete, it goes into our data mart which feeds Sonatype Data Services. Data from the Sonatype Data Services is what you’ll then see in the Lifecycle Dashboard and Application Composition report after an application scan.

## Standard Capabilities

For ecosystems with only Security/Identity data, we report any known security vulnerabilities but may not include in-depth research or license data.

## Ecosystem Support

The table below lists the ecosystems (languages, package managers, etc.) that Sonatype Lifecycle supports.

Ecosystems that are supported by Sonatype Advanced Legal Pack are indicated as ALP.

## More on Analysis Examples Covered in this Section

The examples in this section use IQ Server CLI to scan components in Maven format.

For more examples on scanning components from other popular package managers/package formats refer to [Referencing Package URL (purl) and Component Identifiers](#UUID-e1088e50-6e44-edf0-d5af-178b1349e7bd) .

## C/C++ Application Analysis

The Conan coordinate-based matching feature provides the ability to scan and evaluate C/C++ dependencies found in either a conanfile.txt, conanfile.py, or conaninfo.txt file.

### What is supported

Files named conanfile.txt, conanfile.py or conaninfo.txt will be analyzed.

### What do we parse from the files?

### Steps to analyze using the CLI

Invoke a CLI scan of a directory or subdirectories containing either a conanfile.txt, conanfile.py or conaninfo.txt file. Instructions on how to do this can be found here: [Sonatype IQ CLI](#UUID-6b69b7b1-858f-e58a-e010-beb4fdff9cdf) .

Examples for each Conan file can be found above in the document.

### Steps to analyze using the Jenkins plugin

By default, the Jenkins plugin will not evaluate the conanfile.txt, conanfile.py, and conaninfo.txt files. A custom Scan Target is needed.

**Example Pipeline Script with Scan Patterns**

```
nexusPolicyEvaluation iqApplication: 'SampApp', iqScanPatterns: [[scanPattern: '**/conanfile.txt'], [scanPattern: '**/conanfile.py'], [scanPattern: '**/conaninfo.txt']], iqStage: 'build'
```

To find more information on how to configure Jenkins please go to [Sonatype Platform Plugin for Jenkins](#UUID-0d46c567-a411-72f8-7973-d8f4cf7e00b2) .

### Steps to analyze using the Bamboo plugin

Bamboo Scan Targets control what files are examined. To evaluate C/C++, add conanfile.txt, conanfile.py, and conaninfo.txt to the scan targets via a comma-separated list e.g.

**Example Bamboo Scan Patterns**

```
**/conanfile.txt,**/conanfile.py,**/conaninfo.txt
```

To find more information on how to configure Bamboo please go to the [Lifecycle For Bamboo](#UUID-6737c02e-b17a-00be-be43-2506c487b028) .

## Clair Application Analysis

The Clair coordinate-based matching feature provides the ability to scan and evaluate Clair-identified container dependencies.

For reference on how to use Clair please refer to the Clair documentation.

### What is Supported

Files named clair-scanner-output.json created by the client Clair scanner ( [https://github.com/arminc/clair-scanner](https://github.com/arminc/clair-scanner) ).

### Steps to analyze using the Sonatype IQ CLI

### Steps to analyze using the Jenkins plugin

By default, the Jenkins plugin will not evaluate the clair-scanner-output.json file. A custom Scan Target is needed.

**Example Pipeline Script with Scan Patterns**

```
nexusPolicyEvaluation iqApplication: 'SampApp', iqScanPatterns: [[scanPattern: '**/clair-scanner-output.json']], iqStage: 'build'
```

To find more information on configuring Jenkins, please go to [Sonatype Platform Plugin for Jenkins](#UUID-0d46c567-a411-72f8-7973-d8f4cf7e00b2) .

### Steps to analyze using the Bamboo plugin

Bamboo Scan Targets control what files are examined. Add clair-scanner-output.json to the scan targets via "**/clair-scanner-output.json" to evaluate Clair. To find more information on configuring Bamboo, please go to [Sonatype IQ for Bamboo](#UUID-6737c02e-b17a-00be-be43-2506c487b028) .

## Conda Application Analysis

The Conda coordinate-based matching feature provides the ability to scan and evaluate dependencies for any language (Python, Java, JavaScript, C++) found in the conda.txt file.

### What is supported

- [Files named conda.txt](#UUID-5b113a4a-2658-f59c-0bbc-2e6479cb355a_id_CondaApplicationAnalysis-StepstoanalyzeusingtheSonatypeIQCLI) will be analyzed. Only exact requirements i.e. without wildcards will be considered.
- environment.yml file containing packages from conda-forge can be analyzed. [Follow the steps to analyze the environment.yml file](#UUID-5b113a4a-2658-f59c-0bbc-2e6479cb355a_section-idm234801756295001) , before invoking an IQ CLI scan.

### Steps to analyze *conda.txt*

### Steps to Analyze *environment.yml*

- Create a conda environment using the environment.yml file to define the environment’s specifications. The environment.yml file typically includes `-conda-forge` under *channels* . Conda will now look for packages in the conda- forge channel. You can also specify exact or explicit versions of the packages to install in the environment, under dependencies, in the environment.yml file
- Activate the conda environment using:
- Export a list of all packages in the active environment and save it to a file to conda.txt:
- Invoke a [Sonatype IQ CLI](#UUID-5b113a4a-2658-f59c-0bbc-2e6479cb355a_id_CondaApplicationAnalysis-ScanusingSonatypeIQCLI) scan of a directory or sub-directories containing conda.txt.

### Scan using Sonatype IQ CLI

Invoke a Sonatype IQ CLI scan of a directory or subdirectories containing a conda.txt file. Instructions on how to do this can be found here: [Sonatype IQ CLI](#UUID-6b69b7b1-858f-e58a-e010-beb4fdff9cdf) .

### Steps to analyze using the Jenkins plugin

By default, the Jenkins plugin will not evaluate the conda.txt file. A custom Scan Target is needed.

**Example Pipeline Script with Scan Patterns**

```
nexusPolicyEvaluation iqApplication: 'SampApp', iqScanPatterns: [[scanPattern: '**/conda.txt']], iqStage: 'build'
```

To find more information on how to configure Jenkins please go to [Sonatype Platform Plugin for Jenkins](#UUID-0d46c567-a411-72f8-7973-d8f4cf7e00b2)

### Steps to analyze using the Bamboo plugin

Bamboo Scan Targets control what files are examined. To evaluate Conda, add conda.txt to the scan targets via "**/conda.txt". To find more information on how to configure Bamboo please go to link before this [Sonatype IQ for Bamboo](#UUID-6737c02e-b17a-00be-be43-2506c487b028) .

## CycloneDX Application Analysis

Sonatype Lifecycle analysis supports the [CycloneDX](https://cyclonedx.org/) standard, the industry’s most advanced software bill of materials (SBOM) format.

An SBOM is a list of parts (packages and libraries) included in the application. Just as a manufacturing bill of materials includes all sub-assemblies, the SBOM also includes the direct and transitive dependencies along with any internal components made by your organization.

### Analyzing an SBOM

Any Sonatype scanner and most of the integrations will analyze SBOMs found in the root context of the application scan target when using the naming format listed below in the [Identification Source](#UUID-71778dbe-a6d1-72eb-d37f-f1ae5835e7c9_id_CycloneDXApplicationAnalysis-IdentificationSource) section.

SBOMs may be targeted directly using the [command line scanner (CLI)](#UUID-6b69b7b1-858f-e58a-e010-beb4fdff9cdf) , by [uploading](#UUID-c364f118-bb5b-8f05-7421-1c09086ed38a) to the user interface, or by scripting using the [Third-Party Scan REST API](#UUID-5e8f93a2-bbeb-6ccb-8fd8-c4e4e04d5f08) .

Any application scan may be exported as an SBOM in the CycloneDX and SPDX formats. Learn about more SBOM use cases from our [SBOM guide](#UUID-202e4c44-ad57-e0ad-1b6e-9f1c76caaa2e) .

CycloneDX provides many native application scanners on its repository. Find a complete list at the [CycloneDX Tool Center](https://cyclonedx.org/tool-center/) .

### Identification Source

The CycloneDX format is used as an identification source in the Application Composition Report. The prefix of the file name is used as the source. `Third Party` is used as the identification source when no source is provided through the API or using the filename prefix.

- bom.xml
- <source>-bom.xml
- <source>-bom.json
- <public app id>_<version>_<timestamp>.cdx.<json|xml>

**Note:** Sonatype scanners use the above naming formats to identify and analyze SBOMs within archives. Make sure your SBOM names follow this format when outputting them through third-party tools.

### Dependency Relationships

The CycloneDX 1.4+ format includes dependency graph information on the direct and transitive relationships between dependencies. The Lifecycle scanners include this information in the scan report and for the application dependency tree.

Components at the first level of listed dependencies in the SBOM are identified during an analysis. SBOMs with nested components will pass validation; however, nested components are not supported and are ignored during the analysis.

See the Dependency Graph below.

### Innersource Components

CycloneDX can be used to identify [Innersource](#UUID-c8a1f963-f80b-dd2f-ca31-eac799d3267e_id_ComponentIdentification-innersourceInnersourceInsights) producers as well as when they are consumed by other applications as dependencies. Similarly, this can be used to identify proprietary components. When processing the report, Lifecycle will use the identity information provided in the CycloneDX file when the component is unknown; greatly reducing the number of component unknown violations. This would include in the report any security and license data provided in the SBOM.

See the examples of a producer and consumer below.

### Sonatype properties in SBOMs

Software Bill of Materials generated by Sonatype includes Sonatype-specific metadata under the [Sonatype namespace taxonomy](https://github.com/CycloneDX/cyclonedx-property-taxonomy/blob/main/cdx.md) .

### Application Reports

In conjunction with using CycloneDX to do the application analysis, you can also export any application report in Lifecycle to the CycloneDX format.

- The Options Dropdown from the Scan Report
- From the [CycloneDX REST API](#UUID-1c1e17af-1e7a-4916-357e-45bdef1b8bb5)

### Vulnerability Analysis Section

The CycloneDX 1.4+ format includes analysis information of the vulnerabilities. Sonatype imports the vulnerability analysis found in this section to include in the scan report.

The Sonatype Data Services team frequently evaluates vulnerabilities that enter our systems for accuracy and repeatability. They may determine a vulnerability is not applicable and therefore do not report the vulnerability against the component in our products. For these reasons, we favor reporting data coming from Sonatype Data Services over content reported from third-party sources to reduce the noise reported to development teams and used for enforcement.

- The SBOM uses our vulnerability data for every known component in the Sonatype Data Services. Imported vulnerability data is not included.
- For components not found in the Sonatype Data Services, the vulnerability and license details are sourced from the originally imported SBOM.

**Note:** Custom Vulnerability Information You may add vulnerability information to the SBOM using the [Vulnerability Analysis Details REST API](#UUID-1abf451b-f104-feeb-348b-317cac3af5b2) .

### XML (version 1.6) file content

```
<?xml version="1.0" encoding="UTF-8"?>
<bom serialNumber="urn:uuid:cb3c8aae-d8a0-4ef5-a40d-de537161f948" version="1" xmlns="http://cyclonedx.org/schema/bom/1.6">
  <metadata>
    <timestamp>2023-01-12T14:46:58Z</timestamp>
    <component type="application" bom-ref="pkg:maven/org.example/ACME-Test@1.0-SNAPSHOT?type=pom">
      <group>org.example</group>
      <name>ACME-Test</name>
      <version>1.0-SNAPSHOT</version>
      <purl>pkg:maven/org.example/ACME-Test@1.0-SNAPSHOT?type=pom</purl>
    </component>
  </metadata>
  <components>
    <component type="library" bom-ref="pkg:maven/javax.inject/javax.inject@1?type=jar">
      <group>javax.inject</group>
      <name>javax.inject</name>
      <version>1</version>
      <hashes>
        <hash alg="SHA-1">6975da39a7040257bd51d21a231b76c915872d38</hash>
      </hashes>
      <licenses>
        <license>
          <id>Apache-2.0</id>
        </license>
      </licenses>
      <purl>pkg:maven/javax.inject/javax.inject@1?type=jar</purl>
    </component>
    <component type="library" bom-ref="pkg:maven/commons-io/commons-io@2.6?type=jar">
      <group>commons-io</group>
      <name>commons-io</name>
      <version>2.6</version>
      <licenses>
        <license>
          <id>Apache-2.0</id>
        </license>
      </licenses>
      <purl>pkg:maven/commons-io/commons-io@2.6?type=jar</purl>
      <modified>false</modified>
    </component>
    <component type="library" bom-ref="pkg:maven/com.fasterxml.jackson.core/jackson-databind@2.13.4?type=jar">
      <group>com.fasterxml.jackson.core</group>
      <name>jackson-databind</name>
      <version>2.13.4</version>
      <hashes>
        <hash alg="SHA-1">98b0edfa8e4084078f10b7b356c300ded4a71491</hash>
      </hashes>
      <licenses>
        <license>
          <id>Apache-2.0</id>
        </license>
      </licenses>
      <purl>pkg:maven/com.fasterxml.jackson.core/jackson-databind@2.13.4?type=jar</purl>
    </component>
    <component type="library" bom-ref="pkg:maven/org.example/ACME-data@1.0-SNAPSHOT?type=jar">
      <group>org.example</group>
      <name>ACME-data</name>
      <version>1.0-SNAPSHOT</version>
      <purl>pkg:maven/org.example/ACME-data@1.0-SNAPSHOT?type=jar</purl>
    </component>
  </components>
  <dependencies>
    <dependency ref="pkg:maven/org.example/ACME-Test@1.0-SNAPSHOT?type=pom">
      <dependency ref="pkg:maven/org.example/ACME-data@1.0-SNAPSHOT?type=jar"/>
      <dependency ref="pkg:maven/commons-io/commons-io@2.6?type=jar"/>
    </dependency>
    <dependency ref="pkg:maven/org.example/ACME-data@1.0-SNAPSHOT?type=jar">
      <dependency ref="pkg:maven/javax.inject/javax.inject@1?type=jar"/>
      <dependency ref="pkg:maven/com.fasterxml.jackson.core/jackson-databind@2.13.4?type=jar"/>
      <dependency ref="pkg:maven/commons-io/commons-io@2.6?type=jar"/>
    </dependency>
    <dependency ref="pkg:maven/javax.inject/javax.inject@1?type=jar"/>
    <dependency ref="pkg:maven/com.fasterxml.jackson.core/jackson-databind@2.13.4?type=jar"/>
    <dependency ref="pkg:maven/commons-io/commons-io@2.6?type=jar"/>
  </dependencies>
  <vulnerabilities>
    <vulnerability>
      <id>CVE-2022-42003</id>
      <source>
        <name>NVD</name>
        <url>http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42003</url>
      </source>
      <ratings>
        <rating>
          <source>
            <name>NVD</name>
          </source>
          <score>7.5</score>
          <severity>critical</severity>
          <method>CVSSv3</method>
          <vector>CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H</vector>
        </rating>
      </ratings>
      <cwes>
        <cwe>502</cwe>
      </cwes>
      <analysis>
        <state>resolved_with_pedigree</state>
        <justification>requires_environment</justification>
        <responses>
          <response>workaround_available</response>
          <response>update</response>
        </responses>
        <detail>Analysis Detail</detail>
      </analysis>
      <affects>
        <target>
          <ref>pkg:maven/com.fasterxml.jackson.core/jackson-databind@2.13.4?type=jar</ref>
        </target>
      </affects>
    </vulnerability>
  </vulnerabilities>
</bom>
```

### JSON (version 1.6) file content

```
{
  "bomFormat" : "CycloneDX",
  "specVersion" : "1.6",
  "serialNumber" : "urn:uuid:d069c08a-1e5b-4de2-b6d7-509964190ea7",
  "version" : 1,
  "metadata" : {
    "component" : {
      "group" : "org.example",
      "name" : "ACME-Test",
      "version" : "1.0-SNAPSHOT",
      "licenses" : [ ],
      "purl" : "pkg:maven/org.example/ACME-Test@1.0-SNAPSHOT?type=pom",
      "type" : "library",
      "bom-ref" : "pkg:maven/org.example/ACME-Test@1.0-SNAPSHOT?type=pom"
    }
  },
  "components" : [
    {
      "publisher" : "The Apache Software Foundation",
      "group" : "commons-io",
      "name" : "commons-io",
      "version" : "2.6",
      "hashes" : [
        {
          "alg" : "SHA-1",
          "content" : "815893df5f31da2ece4040fe0a12fd44b577afaf"
        }
      ],
      "licenses" : [
        {
          "license" : {
            "id" : "Apache-2.0"
          }
        }
      ],
      "purl" : "pkg:maven/commons-io/commons-io@2.6?type=jar",
      "type" : "library",
      "bom-ref" : "pkg:maven/commons-io/commons-io@2.6?type=jar"
    },
    {
      "group" : "org.example",
      "name" : "ACME-data",
      "version" : "1.0-SNAPSHOT",
      "licenses" : [ ],
      "purl" : "pkg:maven/org.example/ACME-data@1.0-SNAPSHOT?type=jar",
      "type" : "library",
      "bom-ref" : "pkg:maven/org.example/ACME-data@1.0-SNAPSHOT?type=jar"
    },
    {
      "group" : "javax.inject",
      "name" : "javax.inject",
      "version" : "1",
      "description" : "The javax.inject API",
      "hashes" : [
        {
          "alg" : "SHA-1",
          "content" : "6975da39a7040257bd51d21a231b76c915872d38"
        }
      ],
      "licenses" : [
        {
          "license" : {
            "id" : "Apache-2.0"
          }
        }
      ],
      "purl" : "pkg:maven/javax.inject/javax.inject@1?type=jar",
      "type" : "library",
      "bom-ref" : "pkg:maven/javax.inject/javax.inject@1?type=jar"
    },
    {
      "publisher" : "FasterXML",
      "group" : "com.fasterxml.jackson.core",
      "name" : "jackson-databind",
      "version" : "2.13.4",
      "hashes" : [
        {
          "alg" : "SHA-1",
          "content" : "98b0edfa8e4084078f10b7b356c300ded4a71491"
        }
      ],
      "licenses" : [
        {
          "license" : {
            "id" : "Apache-2.0"
          }
        }
      ],
      "purl" : "pkg:maven/com.fasterxml.jackson.core/jackson-databind@2.13.4?type=jar",
      "type" : "library",
      "bom-ref" : "pkg:maven/com.fasterxml.jackson.core/jackson-databind@2.13.4?type=jar"
    }
  ],
  "dependencies" : [
    {
      "ref" : "pkg:maven/org.example/ACME-Test@1.0-SNAPSHOT?type=pom",
      "dependsOn" : [
        "pkg:maven/commons-io/commons-io@2.6?type=jar",
        "pkg:maven/org.example/ACME-data@1.0-SNAPSHOT?type=jar"
      ]
    },
    {
      "ref" : "pkg:maven/commons-io/commons-io@2.6?type=jar",
      "dependsOn" : [ ]
    },
    {
      "ref" : "pkg:maven/org.example/ACME-data@1.0-SNAPSHOT?type=jar",
      "dependsOn" : [
        "pkg:maven/javax.inject/javax.inject@1?type=jar",
        "pkg:maven/com.fasterxml.jackson.core/jackson-databind@2.13.4?type=jar",
        "pkg:maven/commons-io/commons-io@2.6?type=jar"
      ]
    },
    {
      "ref" : "pkg:maven/javax.inject/javax.inject@1?type=jar",
      "dependsOn" : [ ]
    },
    {
      "ref" : "pkg:maven/com.fasterxml.jackson.core/jackson-databind@2.13.4?type=jar",
      "dependsOn" : [ ]
    }
  ],
  "vulnerabilities": [
      {
          "id": "CVE-2022-42003",
          "source": {
              "name": "NVD",
              "url": "http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42003"
           },
          "ratings": [
              {
                  "source": {
                      "name": "NVD"
                  },
                  "score": 7.5,
                  "severity": "critical",
                  "method": "CVSSv3",
                  "vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H"
              }
          ],
          "cwes": [
              502
          ],
          "analysis": {
            "state": "resolved_with_pedigree",
            "justification": "requires_environment",
            "response": [
                    "workaround_available",
                    "update"
                ],
            "detail": "Analysis Detail"
          },
          "affects": [
              {
                  "ref": "pkg:maven/com.fasterxml.jackson.core/jackson-databind@2.13.4?type=jar"
              }
          ]
      }
  ]
}
```

### Dependency Graph

dependency-bom.xml

```
<?xml version="1.0" encoding="UTF-8"?>
<bom xmlns="http://cyclonedx.org/schema/bom/1.5" version="1">
  <metadata>    
    <component type="application" bom-ref="acme-app">
      <name>Acme Application</name>
      <version>9.1.1</version>
      <purl>pkg:maven/org.acme/acme-app@9.1.1?type=jar</purl>
    </component>
  </metadata>
  <components>
    <component type="framework" bom-ref="pkg:maven/org.acme/web-framework@1.0.0?type=jar">
      <group>org.acme</group>
      <name>web-framework</name>
      <version>1.0.0</version>
      <purl>pkg:maven/org.acme/web-framework@1.0.0?type=jar</purl>
    </component>
    <component type="library" bom-ref="pkg:maven/org.acme/persistence@3.1.0?type=jar">
      <group>org.acme</group>
      <name>persistence</name>
      <version>3.1.0</version>
      <purl>pkg:maven/org.acme/persistence@3.1.0?type=jar</purl>
    </component>
    <component type="library" bom-ref="pkg:maven/org.acme/common-util@3.0.0?type=jar">
      <group>org.acme</group>
      <name>common-util</name>
      <version>3.0.0</version>
      <purl>pkg:maven/org.acme/common-util@3.0.0?type=jar</purl>
    </component>
  </components>
  <dependencies>
    <dependency ref="acme-app">
      <dependency ref="pkg:maven/org.acme/web-framework@1.0.0?type=jar"/>
      <dependency ref="pkg:maven/org.acme/persistence@3.1.0?type=jar"/>
    </dependency>
    <dependency ref="pkg:maven/org.acme/web-framework@1.0.0?type=jar">
      <dependency ref="pkg:maven/org.acme/common-util@3.0.0?type=jar"/>
    </dependency>
    <dependency ref="pkg:maven/org.acme/persistence@3.1.0?type=jar">
      <dependency ref="pkg:maven/org.acme/common-util@3.0.0?type=jar"/>
    </dependency>
    <dependency ref="pkg:maven/org.acme/common-util@3.0.0?type=jar"/>
  </dependencies>
</bom>
```

### Innersource Producer

producer-bom.xml

```
<?xml version="1.0" encoding="UTF-8"?>
<bom version="1" xmlns="http://cyclonedx.org/schema/bom/1.6">
  <metadata>
    <component type="application" bom-ref="pkg:generic/producer-component@1.0.0">
      <name>producer-component</name>
      <version>1.0.0</version>
    </component>
  </metadata>
  <components>
    <component type="library" bom-ref="pkg:generic/some-awesome-component@1.0">
      <name>some-awesome-component</name>
      <version>1.0</version>
      <purl>pkg:generic/some-awesome-component@1.0</purl>
    </component>
  </components>
  <dependencies>
    <dependency ref="pkg:generic/producer-component@1.0.0">
      <dependency ref="pkg:generic/some-awesome-component@1.0" />
    </dependency>
    <dependency ref="pkg:generic/some-awesome-component@1.0" />
  </dependencies>
</bom>

```

### Innersource Consumer

consumer-bom.xml

```
<?xml version="1.0" encoding="UTF-8"?>
<bom version="1" xmlns="http://cyclonedx.org/schema/bom/1.6">
  <metadata>
    <component type="application" bom-ref="pkg:npm/consumer@1.0.0">
      <name>consumer</name>
      <version>1.0.0</version>
    </component>
  </metadata>
  <components>
    <component type="library" bom-ref="pkg:npm/producer@1.0">
      <name>producer</name>
      <version>1.0</version>
      <purl>pkg:npm/producer@1.0</purl>
    </component>
    <component type="library" bom-ref="pkg:npm/some-awesome-component@1.0">
      <name>some-awesome-component</name>


```

### Analyze using the CycloneDX maven plugin

The CycloneDX maven plugin may be used to generate an SBOM to include when analyzing your application. Following is a sample request to make the BOM and set the name of the bom using the `outputName` .

```
mvn org.cyclonedx:cyclonedx-maven-plugin:2.8.2:makeAggregateBom -DoutputName=cyclonedx-bom
```

This will generate cyclonedx-bom.xml and cyclonedx-bom.json which are compatible with the Lifecycle scanners.

The CycloneDX output may be included directly in the project pom.xml to be picked up by the Lifecycle Analysis automatically.

This example includes the CycloneDX generation in the pom.xml plugins. Note the `outputName` is used in the `project.artifactId` to generate the name of the BOM file.

```
<plugin>
  <groupId>org.cyclonedx</groupId>
  <artifactId>cyclonedx-maven-plugin</artifactId>
  <version>2.8.2</version>
  <configuration>
    <projectType>library</projectType>
    <schemaVersion>1.5</schemaVersion>
    <includeBomSerialNumber>true</includeBomSerialNumber>
    <includeCompileScope>true</includeCompileScope>
    <includeProvidedScope>true</includeProvidedScope>
    <includeRuntimeScope>true</includeRuntimeScope>
    <includeSystemScope>true</includeSystemScope>
    <includeTestScope>false</includeTestScope>
    <includeLicenseText>false</includeLicenseText>
    <outputReactorProjects>true</outputReactorProjects>
    <outputFormat>all</outputFormat>
    <outputName>
```

Learn more from the [CycloneDX maven plugin](https://github.com/CycloneDX/cyclonedx-maven-plugin) documentation.

### Analyze using the Jenkins plugin

By default, the Jenkins plugin will not evaluate the bom.xml. A custom scan target is needed.

```
nexusPolicyEvaluation 
  iqApplication: 'SampApp', 
  iqScanPatterns: [
    [scanPattern: '**/bom.xml'], 
    [scanPattern: '**/*-bom.xml']
  ], 
  iqStage: 'build'
```

More at

### Analyze using the Bamboo plugin

Bamboo Scan Targets control what files are examined. To evaluate CycloneDX, add bom.xml to the scan targets via a comma-separated list e.g.

**Example Bamboo Scan Patterns**

```
**/bom.xml,**/*-bom.xml
```

To find more information on how to configure Bamboo please go to .

## Dart and Flutter Analysis

Dart and Flutter scanning supports coordinate-based matching of Dart and Flutter packages from the pub package manager [pub.dev](https://pub.dev/) .

### Supported Files

You can scan Dart and Flutter applications using any of the following:

- Dart and Flutter packages in the form of `tar.gz` files that contain the license files (mostly under BSD3 license) and src files.
- The `pubspec.yaml` file containing your project dependencies (including version constraints for each dependency), environment settings and other metadata. **Example:**
- The `pubspec.lock` file that is automatically generated when you run `pub get` , containing the exact version of the dependency, including transitive dependencies. **Example**

We recommend scanning the `pubspec.lock` file over `pubspec.yaml` .

**NOTE:** The `pubspec.yaml` is ignored by the scanning process if there is a `pubspec.lock` in the same directory.

### Steps to scan

Invoke a CLI scan of a directory or sub-directories containing the target files.

```
java -jar [sonatype-cli] -a [username:password] -i [--application-id] -s [--server-url] [scan-target]
```

```
java -jar nexus-iq-cli-2.2.0-SNAPSHOT.jar -a admin:admin123 -i TestApp1 -t build -s http://localhost:8070 C:\temp\pubspec.zip

```

On successful completion of the scan (status - completed), the output will include links to view the scan reports:

```
[INFO] Policy Action: Warning
[INFO] Summary of policy violations: 4 critical, 85 severe, 46 moderate
[INFO] The detailed report can be viewed online at http://localhost:8070/ui/links/application/TestApp1/report/95c4c14e
[INFO] The application priorities can be viewed online at http://localhost:8070/ui/links/developer/priorities/TestApp1/95c4c14e/cli
```

**The Detailed Report URL** - link takes you to the application composition report in *Lifecycle* .

**The Priorities URL** - link takes you to the Priorities page in *Developer* .

## Docker Image Analysis

Lifecycle analyzes the application layer of an image to discover the open-source components your application depends on. For a full scan of the container image including the OS layer, refer to .

The steps to running an analysis of a Docker image are as follows.

- **Use the docker client to save the image as a tar file** See the following on [installing the Docker client](https://docs.docker.com/install/)
- **Run an analysis with a Lifecycle integration** The scanner uses the Docker algorithm to analyze which files are added or deleted from each layer to determine the composition of the image. The application layer contents are passed to Lifecycle for evaluation.
- Review the report generated in Lifecycle

- The docker analysis results are similar to the build scan for most ecosystems however any additional packages found in the environment, brought in by the docker image, are also analyzed. These results may be outside of the scope for the development team to remediate.
- While analyzing the container before deployment is a best practice, some results are not as accurate when analyzing outside of the build context. The build manifests and OSS pedigree are lost while open-source components are obfuscated during the final application packaging. Refer to the various ecosystem analysis pages for guidance on the optimum time to perform an analysis.

The Docker client is used to pull and save an image from any repository; including Nexus Repository 3.

[Sonatype Container](https://www.sonatype.com/products/container) is used to analyze containers running on these platforms. Use Lifecycle Docker image analysis to evaluate docker images before they are deployed to those runtime environments.

### Analysis using the CLI

The Sonatype CLI relies on the Docker daemon to package the image as an archive file.

Review the [Sonatype CLI documentation](#UUID-6b69b7b1-858f-e58a-e010-beb4fdff9cdf) for details on running a scan.

Opening the Component Details Page for a component, and then selecting the Occurrences tab, you’ll see the tar file path, with a long hash, and then a layer.tar.

### Analysis with Jenkins CI

The following example is a pipeline project in Jenkins that pulls an image from Docker Hub and starts a Lifecycle evaluation. You need a running instance of Jenkins with the [Sonatype Platform plugin](https://wiki.jenkins.io/display/JENKINS/Nexus+Platform+Plugin) to run policy evaluations. Specify an agent node [that has Docker installed](https://www.jenkins.io/doc/book/pipeline/syntax/#agent) . This example uses the [webgoat-7.1 image](https://hub.docker.com/r/webgoat/webgoat-7.1/)

### Webhook Listener

Analysis of images may be triggered using a webhook listener after a build is pushed to Docker Hub or Nexus Repository 3. This may be a solution when you don’t have access to your CI build process.

See the community project for using the [Webhook Listener](https://github.com/sonatype-nexus-community/iq-webhook-listener) .

## Go Application Analysis

### Evaluation: Source code and manifest analysis

The Go coordinate-based matching feature provides the ability to scan and evaluate Go module dependencies referenced in projects that use dep or go mod. Support includes Security, License, and Identity data for Go modules found on [golang.org](https://index.golang.org/index) public repository. Detection of pre-release versions is not supported.

### Steps to analyze using the Sonatype Lifecycle CLI

### Steps to analyze using the Jenkins plugin

By default, the Jenkins plugin will not evaluate the Gopkg.lock, go.sum, and go.list files. A custom Scan Target is needed.

**Example Pipeline Script with Scan Patterns**

```
nexusPolicyEvaluation iqApplication: 'SampApp', iqScanPatterns: [[scanPattern: '**/Gopkg.lock'], [scanPattern: '**/go.sum'], [scanPattern: '**/go.list']], iqStage: 'build'
```

### Steps to analyze using the Bamboo plugin

Bamboo Scan Targets control what files are examined. To evaluate Go, add Gopkg.lock, go.sum, and go.list to the scan targets via a comma-separated list e.g.

**Example Bamboo Scan Patterns**

```
**/Gopkg.lock,**/go.sum,**/go.list
```

## Java Application Analysis

### JVM Ecosystems

*IQ server* Java application analysis supports most JVM-based languages and is not limited to Java only. These include the most popular languages in use by the developer community, e.g., Kotlin, Scala, Groovy, Clojure, Fantom, Ceylon, JRuby, Golo, etc.

### Evaluation: Advanced Binary Fingerprinting

Java scanning supports packaged archives including ( **.ear/.war/.jar/.zip/.tar.gz** ) files. For the best results, we recommend using the post-build artifact as the scan target (what you are planning to deploy) as it will contain all the direct and transitive dependencies required by the project. After a normal CI build, add a post-build step to do the analysis using the CI Plugins or the CLI Scanner . A Lifecycle evaluation will pick up any dependencies packaged into the archive or included in the target directory.

- [Uber jars](https://stackoverflow.com/questions/49810578/what-is-a-shaded-jar-and-what-is-the-difference-similarities-between-uber-jar-a) are a way to include dependencies by copying in their contents when the jar is built. The Lifecycle algorithms will not identify them as separate dependencies, as these jars could be similarly matched to modified open-source components. This will lead to confusing results for development teams. For more accurate results, you will need to call the index goal of the [Maven plugin](#UUID-433e090b-af9e-c63f-5963-c61a3a5f9729) at the time of building the uber/shaded jar. This will generate a dependency index (module.xml file) of direct and transitive dependencies found in the shaded jar's POM file. Any module.xml files found in the scan path by the CI Scanners will be included in the results.
- Custom jar files typically do not include their dependencies in the scan context so scanning them will not produce results. The maven copy dependencies command can be used: *mvn dependency:copy-dependencies* to include the dependencies into a separate directory. This directory can be scanned via the CLI scanner or similar tools.
- The Lifecycle scanner does not support [scanning a `.apk`](https://support.sonatype.com/hc/en-us/articles/360000387687) directly due to the compilers converting the open-source code into a DEX (Dalvik Executable) file: a minified/modified version of the code. For this reason, scanning prior to the assembling of the `.apk` is required. We suggest embedding the native Maven or Gradle scanners instead.
- To perform an analysis of a sbt assembly, a temporary pom.xml file will need to be created using the **sbt makePom** command. We recommend using the [Maven plugin](#UUID-433e090b-af9e-c63f-5963-c61a3a5f9729) for the best results. See the example steps below.
- Evaluation of modified dependencies is supported for Java. The inner contents of components are analyzed along with their fingerprints to determine the best match of the original source component. Components that have been changed from their published source are susceptible to additional risk.
- When using the Maven plugin or [Grade plugin](https://github.com/sonatype-nexus-community/scan-gradle-plugin) , Java components created by insider teams will be labeled in the application scan report. Any dependencies only brought in by the Innersource component will be considered direct dependencies of those components. Innersource components will need to be scanned before the current project in order to determine if a component is Innersource or not. Refer to for more details.
- The project's manifest is used to determine if a dependency is directly called by the project or not. Any dependencies not found in the manifest are considered transitive dependencies. The Transitive Solver provides remediation recommendations based on the direct dependency of transitive dependency violations.
- This plugin can be used to natively scan Gradle projects using Lifecycle.
- The Lifecycle scanner can scan SBOMs generated from [CycloneDX for Java](https://github.com/CycloneDX/cyclonedx-maven-plugin) . See the [CycloneDX](#UUID-71778dbe-a6d1-72eb-d37f-f1ae5835e7c9) pages for details.

### Evaluation: Source code and manifest analysis

A Java project's source code could be analyzed for direct dependencies using just the coordinates provided in the manifest files. When any binaries are detected in the scan path, the manifest files are not used for identifying components. Pointing directly to the path of the manifest is recommended to force a manifest analysis.

- The transitive dependencies are not automatically resolved and, therefore not included during this analysis. The [Maven plugin](#UUID-433e090b-af9e-c63f-5963-c61a3a5f9729) 'evaluate' goal should be used to resolve transitive dependencies.
- Dependencies with a group, artifact id, and exact version number are required.
- The extension and classifier fields are optional.
- RELEASE 142 pom.xml files are ignored if they are inside a META-INF directory. This is because these files do not necessarily represent the application, particularly in the case of uber/shaded archives.
- RELEASE 149 Although pom.xml files are ignored if they are inside a META-INFdirectory by default, this can now be changed if needed by configuring the *scan-pom-files-in-meta-inf-directory* feature using the [Feature Configuration REST API - v2](#UUID-c0e9fb56-7cb8-d415-9ee3-451a5bc9fd97) .
- RELEASE 171 Sonatype IQ Scanner configuration option “excludeMavenDependencyManagement" Value type: Boolean Default value: False Change to existing behavior: None Purpose: Improves project dependency detection accuracy. When enabled and the scanner is processing a manifest (Maven POM), then dependencies that are ONLY declared in the *dependencyManagement* section are excluded. If a component's version was declared in the dependency management section and not in the project dependency version then the component version declared in the dependency management section will be used. By default for backwards compatibility, all unique dependencies that can be fully resolved from both the project dependencies and dependencyManagement sections are included.

## npm Application Analysis

### Evaluation: Advanced Binary Fingerprinting (ABF)

When a scan includes javascript files, those are considered the primary identification source. Any manifest files in the scan (e.g. package-lock.json) are used to refine the results identified by the javascript files. Manifest entries that do not correspond to any of the scanned javascript files are ignored. If you want all dependencies declared in manifest files to be in the report you should only scan those files and avoid including any javascript files in the report.

### Evaluation: Manifest and lock files

A manifest analysis is run by specifically scanning only the project-lock and manifest files for the following javascript package managers: [npm](https://www.npmjs.com/) , [yarn](https://yarnpkg.com/) , and [pnpm](https://pnpm.io/) . The scanner will default to an ABF scan if any .js files are included in the scan context path.

- **Lock files:** manifest files alone do not include the transitive dependencies and sometimes the specific direct versions that will be used in the final application. This is why we highly recommend including the lock files in the analysis for the best results. It is further important to note that when scanning a lock file via the *Evaluate a File* option in the Lifecycle UI, a dependency tree will not be produced unless the lock file is put in an archive (e.g. zip file) alongside its corresponding package.json file and that archive is scanned instead.
- **Direct and Transitive Dependencies** : To include the dependency information i.e. Direct vs Transitive, the package.json will need to include an auto-generated lock file along with the manifest files.

If only a lock file is scanned, then a package.json file in the same directory can be used to help determine direct dependencies and development dependencies to be excluded.

This is true if the package.json file:

- Exists
- Is not excluded
- Has a "dependencies" section

If all of these conditions are met, then only the packages specified in the "dependencies" section will be considered for analysis as production dependencies. If the "dependencies" section is empty, then no dependencies will be included.

**devDependencies** : By default, components under the 'devDependencies' and 'optional' scopes or have the metadata 'dev: true' are excluded from the scan. Here are two ways to include them:

### Steps to analyze using the Sonatype IQ CLI

### Steps to analyze using the Jenkins plugin

By default, the Jenkins plugin will not evaluate the `yarn.lock` , `pnpm-lock.yaml` , `package-lock.json` or `npm-shrinkwrap.json` files. A custom Scan Target is needed.

**Example Pipeline Script with Scan Patterns**

```
nexusPolicyEvaluation iqApplication: 'SampApp' , iqScanPatterns: [[scanPattern: '**/npm-shrinkwrap.json' ], [scanPattern: '**/package-lock.json'], [scanPattern: '**/yarn.lock'], [scanPattern: '**/pnpm-lock.yaml']], iqStage: 'build'
```

### Steps to analyze using the Bamboo plugin

By default, the Bamboo plugin will not evaluate the `yarn.lock` , `pnpm-lock.yaml` , `package-lock.json` or `npm-shrinkwrap.json` files. A custom Scan Target is needed.

![87198517.png](/docs-at-surgery-poc/assets/images/uuid-1477914a-4207-5aa0-1d42-8898eab5d980.png)

## NuGet Application Analysis

### Evaluation: Advanced Binary Fingerprinting (ABF)

The primary open-source repository for .NET components is [NuGet](https://docs.microsoft.com/en-us/nuget/what-is-nuget) . A NuGet package is an archive file with the .nupkg extension. These packages contain compiled code in the form of [Pecoff](https://community.sonatype.com/t/enhancements-to-nuget-net-scanning-in-nexus-lifecycle/4569) (PE = Portable Executable, COFF = Common Object File Format) files, related files, and a descriptive manifest. Developers may add complete packages to their applications or directly utilize the Pecoff files from the package. The .NET build process will remove non-essential files connecting individual Pecoff files back to their parent components.

- Analysis of NuGet packages includes Security, License, and Identity data.
- Lifecycle scanners support both binaries and manifest files but will default to binaries when they are present in scan target.
- Lifecycle ABF scans identify both NuGet packages ( **.nupkg** ) and the following Pecoff extensions: **.acm, .ax, .cpl, .dll, .drv, .efi, .exe, .mui, .ocx, .scr, .sys, .tsp**
- **Pecoff data** : License data is associated with Nuget packages and may be inherited by their component files. Pecoff files often belong to common libraries that exist in many NuGet projects. When the declared NuGet project cannot be determined, only Security and Identity data will be available for the component. Because pecoff does not provide license information, you might notice a decrease in license identifications. To obtain this information, we recommend either scanning the .nupkg file directly or creating a BOM using CycloneDX.
- **During build time** : NuGet dependencies can be outputted to a directory for a more complete analysis of the required open-source components. These commands will result in the most accurate representation of the open-source used but may include more versions (assemblies) than what will be deployed in the application. nuget restore -OutputDirectory packages dotnet restore --packages packages
- nuget restore -OutputDirectory packages
- dotnet restore --packages packages
- **Developers local build** : A script may be used by the Visual Studio plugin to download all of the NuGet dependencies for analysis. These code snippets may be used as a possible starting point. [Find-Package](https://docs.microsoft.com/en-us/powershell/module/packagemanagement/find-package?view=powershell-7.1) <PackageName> -IncludeDependencies [get-package](https://docs.microsoft.com/en-us/powershell/module/packagemanagement/get-package?view=powershell-7.2) -list <PackageName> | select dependencies
- [Find-Package](https://docs.microsoft.com/en-us/powershell/module/packagemanagement/find-package?view=powershell-7.1) <PackageName> -IncludeDependencies
- [get-package](https://docs.microsoft.com/en-us/powershell/module/packagemanagement/get-package?view=powershell-7.2) -list <PackageName> | select dependencies
- **CycloneDX SBOM** : an sbom from [CycloneDX/cyclonedx-dotnet](https://github.com/CycloneDX/cyclonedx-dotnet) can be used to accurately identify the direct and transitive dependencies declared in the .NET project file. The sbom will be included in the analysis when present in the binary scan.

### Scanning MSI Packages

An MSI (Microsoft Software Installer) file is a package file that contains instructions for installing, updating, configuring, and removing software on Windows. The contents that go into an MSI are compressed and modified so may not be scanned effectively. Analyzing `.msi` files is not currently supported.

Scan the contents of your application before packaging your application into the `.msi` format.

### Evaluation: Project files

A Lifecycle analysis can be run from source control by directly scanning the project (.csproj) and packages.config files. Both are package file options used in NuGet projects.

- Only components with an exact version specified are evaluated.
- Transitive dependencies are not included.

## Objective-C Application Analysis

The Cocoapods coordinate-based matching feature provides the ability to scan and evaluate Objective-C dependencies found in the Podfile.lock file.

**Note:** Cocoapods Approaching End-of-Life In response to the observed shift in interest towards other ecosystems (e.g. Swift), Cocoapods has announced plans to stop addition of new versions or pods to the Cocoapods trunk by the end of **December 2026** . As a result, there will be no updates to dependencies which come to Sonatype Component Intelligence through the Cocoapods trunk **after** **December 2026** . We will continue to support analysis of these dependencies/components, but they will be marked as End-of-Life components at all occurrences within Lifecyle. (e.g. policies).

### What is supported

Files named Podfile.lock (generated by Cocoapods) will be analyzed.

### What do we parse from the file?

The dependencies under the PODS" section are evaluated. For example:

```
PODS:
  - GDTMobSDK (4.10.2):
    - GDTMobSDK/GDTMobSDK (= 4.10.2)

```

### Steps to analyze using the Sonatype IQ CLI

Invoke a Sonatype IQ CLI scan of a directory or subdirectories containing a Podfile.lock file.

Example Podfile.lock file (file is edited for clarity)

```
PODS:
  - ADMobGenAdapter (1.5.2):
    - ADMobGenFoundation
  - ADMobGenFoundation (0.7.2)
  - ADMobGenGDT (4.10.0):
    - ADMobGenAdapter
    - ADMobGenFoundation
    - GDTMobSDK (= 4.10.2)
  - GDTMobSDK (4.10.2):
    - GDTMobSDK/GDTMobSDK (= 4.10.2)
  - GDTMobSDK/GDTMobSDK (4.10.2)
  - YogaKit (1.2.0)
  - libpng (1.4.9)
  - libpng (1.0.8)
  - GethDevelop (1.8.17)

DEPENDENCIES:
  - ADMobGenGDT (from `../`)

SPEC REPOS:
  https://github.com/cocoapods/specs.git:
    - ADMobGenAdapter
    - ADMobGenFoundation
    - GDTMobSDK

EXTERNAL SOURCES:
  ADMobGenGDT:
    :path: "../"

SPEC CHECKSUMS:
  ADMobGenAdapter: 5ab3531d5659c96812e6da545c1ec160b9991a2e
  ADMobGenFoundation: de6e4f7b09df256a347878d0f0e0438c1feac94e
  ADMobGenGDT: 77d18f682136e9e90fc9e5dfb0fc57637d5441d7
  GDTMobSDK: 6fde44a4f80c36051d5d879df8bb280034c31431

PODFILE CHECKSUM: 441850ec31e67c6ea8241a64c55657d490e51d66

COCOAPODS: 1.7.0.beta.2

```

### Steps to analyze using the Jenkins plugin

By default, the Jenkins plugin will not evaluate the Podfile.lock file. A custom Scan Target is needed.

**Example Pipeline Script with Scan Patterns**

```
nexusPolicyEvaluation iqApplication: 'SampApp', iqScanPatterns: [[scanPattern: '**/Podfile.lock']], iqStage: 'build'
```

### Steps to analyze using the Bamboo plugin

Bamboo Scan Targets control what files are examined. To evaluate Objective-C, add Podfile.lock to the scan targets via "**/Podfile.lock".

## PHP Application Analysis

### Evaluation: Source code and manifest analysis

PHP scanning supports coordinate-based matching of PHP dependencies found in the `composer.lock` file for packages coming from the [Packagist](https://packagist.org/) ecosystem.

For the best results, we recommend generating and committing the `composer.lock` file in your version control system before scanning.

### What is supported

- Files named composer.lock (a JSON file generated by PHP composer) will be analyzed.
- Drupal core and its components when installed using Composer.

### What do we parse from the file?

Only top-level dependencies (specified under the "packages" group) are evaluated, for example:

```
{
  "packages": [
    {
      "name": "bower-asset/bootstrap",
      "version": "v3.2.0"
    }
  ]
}
```

### Steps to analyze using the Sonatype IQ CLI

Invoke a Sonatype IQ CLI scan of a directory or subdirectories containing a composer.lock file.

Example composer.lock file (file is edited for clarity)

```
{
  "hash": "8ca6b6b80bab36b5287b4292abee988f",
  "packages": [
    {
      "name": "bower-asset/bootstrap",
      "version": "v3.2.0",
      "source": {
        "type": "git",
        "url": "https://github.com/twbs/bootstrap.git",
        "reference": "c068162161154a4b85110ea1e7dd3d7897ce2b72"
      }
    },
        {
      "name": "bower-asset/jquery",
      "version": "2.1.1",
      "source": {
        "type": "git",
        "url": "https://github.com/jquery/jquery.git",
        "reference": "4dec426aa2a6cbabb1b064319ba7c272d594a688"
      }
    },
    {
      "name": "components/jqueryui",
      "version": "1.11.4"
    }
  ]
}
```

## Python Application Analysis

Python scanning supports binary packaged archives ( `.whl` / `tar.gz` ) and coordinates in the `requirements.txt` manifests from the [Python Package Index (PyPI)](https://pypi.org/) . For the best results, we recommend first creating a Python virtual environment and resolving the dependencies using a pip install against the requirements file. This will bring only the dependencies needed by the project into the build while resolving any included dependency ranges in the requirements file.

Starting with [Sonatype IQ CLI 2.0](#UUID-6b69b7b1-858f-e58a-e010-beb4fdff9cdf) , Python `Pipfile.lock` files are supported, enabling accurate and efficient dependency identification directly from Pipenv projects. This feature eliminates the need for manual workarounds or complex CI configurations when analyzing Python projects with Pipenv. Note that if you are using the Jenkins plugin, you will need to upgrade it to benefit from this functionality, as the changes were made within the scanner.

### How to get the best results

To produce the best outcome the following is suggested:

- Create a `requirements.txt` file by using "pip freeze > requirements.txt".
- Using `requirements.txt` , download the binaries by executing " `pip download -r requirements.txt -d <output_dir>` " or " `pip wheel -r requirements.txt -w <output_dir>` ".
- Run a scan on `<output_dir>` .

Guidelines for the **requirements.txt** file:

- Use `` to create the requirements file.
- Lifecycle scanners will only use the manifest named `requirements.txt` while ignoring other variants.
- Avoid including variable ranges for dependencies as these will be ignored by the Lifecycle scanner.
- The `requirements.txt` must use the == operator and version without wildcards.
- Additional flags should be added to `requirements.txt` files to scope to the target os/arch as found in the [environment markers](https://peps.python.org/pep-0345/#environment-markers) of the Python documentation.

**.whl files** : may be matched to multiple environmental Python packages. These will show as duplicates in the Lifecycle scan report.

### Evaluation: Source code and manifest analysis

The Python coordinate-based matching feature provides the ability to scan and evaluate Python dependencies found in Python manifest files without running the pip install first. Files named `requirements.txt` (generated using a pip command) and `poetry.lock` (Poetry lock files) will be analyzed.

### What do we parse from the file?

### Steps to analyze using the Sonatype IQ CLI

## R (CRAN) Application Analysis

The CRAN coordinate-based matching feature provides the ability to scan and evaluate R language dependencies found in a cran-installed.packages file.

Files named cran-installed.packages (exported via installed.packages() command in CRAN console) will be analyzed

Here is an example of how to export the installed CRAN package name and version into a file using CRAN console.

```
sink("/path/to/cran-installed.packages") 
installed.packages()[,c(1,3:4)]
```

### What do we parse from the file?

The segments corresponding to the package name and version of the dependency are evaluated. For example:

```
                Package        Version
crosstalk       "crosstalk"    "1.0.0"

```

### Steps to analyze

Invoke a scan of a directory or subdirectories containing a cran-installed.packages file.

Examplecran-installed.packages file (file is edited for clarity)

```
                Package         Version
crosstalk       "crosstalk"     "1.0.0"
readxl          "readxl"        "1.0.9"
widgetframe     "widgetframe"   "0.9.0"

```

## Ruby Application Analysis

Ruby scanning supports packages from [RubyGems](https://rubygems.org/) as (.gem) files with the full support of Security, License, and Identity data.

For the best results, the scan should happen after either installing the packages from a clean environment or storing the gems in a local cache to run the analysis.

- [bundle cache --no-install](https://bundler.io/man/bundle-cache.1.html) : package the dependencies to **./vendor/cache** without installing them to the local install location
- [bundle install --deployment](https://bundler.io/v2.3/man/bundle-install.1.html#DEPLOYMENT-MODE) : uses gems installed to **./vendor/bundle** not your default system location.

The Lifecycle scanner can scan SBOMs generated from [CycloneDX for Ruby](https://github.com/CycloneDX/cyclonedx-ruby-gem) . See [CycloneDX](#UUID-71778dbe-a6d1-72eb-d37f-f1ae5835e7c9) pages for details.

### Evaluation: Manifest and lock files

The Ruby coordinate-based matching feature provides the ability to scan and evaluate Ruby dependencies found in the Gemfile.lock file. Support includes manifest analysis using the **Gemfile.lock** file.

### What do we parse from the file?

Components from sections GIT, GEM and PATH and with an exact version will be analyzed. For example:

**Gemfile.lock**

```
GIT
  remote: https://github.com/phatworx/devise_security_extension.git
  specs:
    devise_security_extension (0.10.0)

GEM
  remote: https://rubygems.org/
  specs:
    actionmailer (5.0.7.2)
      actionpack (= 5.0.7.2)

PATH
  remote: ../some_path
  specs:
    jquery (0.0.1)

```

Example Gemfile.lock File

**Gemfile.lock**

```
GIT
  remote: https://github.com/phatworx/devise_security_extension.git
  revision: b2ee978af7d49f0fb0e7271c6ac074dfb4d39353
  specs:
    devise_security_extension (0.10.0)
      devise (>= 3.0.0, < 5.0)
      railties (>= 3.2.6, < 6.0)

GEM
  remote: https://rubygems.org/
  remote: https://rails-assets.org/
  specs:
    actioncable (5.0.7.2)
      actionpack (= 5.0.7.2)
      nio4r (>= 1.2, < 3.0)
      websocket-driver (~> 0.6.1)
    actionmailer (5.0.7.2)
      actionpack (= 5.0.7.2)
      actionview (= 5.0.7.2)
      activejob (= 5.0.7.2)
      mail (~> 2.5, >= 2.5.4)
      rails-dom-testing (~> 2.0)

PLATFORMS
  ruby

DEPENDENCIES
  acts-as-taggable-on (~> 5.0.0)
  acts_as_votable (~> 0.11.1)
  ahoy_matey (~> 1.6.0)
  ancestry (~> 3.0.7)
  audited (~> 4.9.0)
  autoprefixer-rails (~> 8.2.0)
  bullet (~> 5.7.0)
  
BUNDLED WITH
   1.17.1


```

## Rust Application Analysis

The Cargo coordinate-based matching feature provides the ability to scan and evaluate Rust dependencies found in the Cargo.lock file.

### Cargo Package Manager

- Cargo.lock - [Cargo](https://doc.rust-lang.org/cargo/guide/cargo-toml-vs-cargo-lock.html) is the package manager for [Rust](https://www.rust-lang.org/) . Cargo downloads Rust dependencies, compiles packages, makes distributable packages, and uploads them to [crates.io](https://crates.io/) , the Rust community’s package registry.
- Support includes Security and Identity data.
- The fields name and version of the dependency under each "package" section are evaluated.

Example Cargo.lock file

```
[[package]]
name = "core-nightly"
version = "1.26.2"

[[package]]
name = "grin"
version = "1.0.0"

[[package]]
name = "protobuf"
version = "2.5.0"


```

## SPDX Application Analysis

Sonatype Lifecycle can analyze SBOMs in [SPDX](https://spdx.github.io/spdx-spec/v2.3/) v2.3 format. Beginning with IQ Server version 192, it also supports SPDX v2.2.

### Analyzing an SBOM

Any Sonatype scanner and most of the integrations will analyze SBOMs found in the root context of the application scan target when using the naming format listed below in the [Identification Source](#UUID-7134f3e0-c5ea-9211-d1d2-1fcd8ac6b09a_id_SPDXApplicationAnalysis-IdentificationSource) section.

SBOMs may be targeted directly using the [command line scanner (CLI)](#UUID-6b69b7b1-858f-e58a-e010-beb4fdff9cdf) , by [uploading](#UUID-c364f118-bb5b-8f05-7421-1c09086ed38a) to the user interface, or by scripting using the [Third-Party Scan REST API](#UUID-5e8f93a2-bbeb-6ccb-8fd8-c4e4e04d5f08) .

Any application scan may be exported as an SBOM in the CycloneDX and SPDX formats. Learn about more SBOM use cases from our [SBOM guide](#UUID-202e4c44-ad57-e0ad-1b6e-9f1c76caaa2e) .

### Identification Source

The SPDX format can be used as an [Identification Source](#UUID-39d840f0-d51b-c09b-8272-415acbc57462) in the Application Composition Report. Lifecycle scanners automatically incorporate discovered SPDX SBOMs in the following patterns.

- **spdx.xml**
- **spdx.json**
- ****
- ****

When no source is provided through the API or using the above filename prefix, "Third Party" is used as the Identification Source in the Application Composition Report.

### Dependency Relationships

The SPDX v2.2 and v2.3 formats can include an optional Relationships section that lists package, file, or snippet dependencies. When present, Lifecycle scanners read all known relationship types to include the information in the scan report and build the dependency tree.

### Application Reports

In addition to using SPDX application analysis, you can export application composition reports from Lifecycle to SPDX SBOM in the following ways:

- The Options Dropdown from the Scan Report
- Use the [SPDX REST API](#UUID-3f859705-6f87-f8d4-3ee1-eabce2c038cf)

### Sample SPDX v2.3 SBOM for Analysis in XML format

```
<?xml version='1.0' encoding='UTF-8'?>
<Document>
    <SPDXID>SPDXRef-DOCUMENT</SPDXID>
    <spdxVersion>SPDX-2.3</spdxVersion>
    <creationInfo>
        <created>2023-08-21T16:49:07Z</created>
        <creators>Tool: Sonatype IQ Server - 1.166.0</creators>
    </creationInfo>
    <name>pkg:generic/sonatype/iq_application_Test%20App%2001@ea08930a666041bbbee8c9f6c0e7951b</name>
    <dataLicense>CC0-1.0</dataLicense>
    <hasExtractedLicensingInfos>
        <licenseId>LicenseRef-No-Sources</licenseId>
        <extractedText>No-Sources</extractedText>
    </hasExtractedLicensingInfos>
    <hasExtractedLicensingInfos>
        <licenseId>LicenseRef-Not-Declared</licenseId>
        <extractedText>Not-Declared</extractedText>
    </hasExtractedLicensingInfos>
    <documentNamespace>http://localhost:8070/ui/links/application/test-app-01/report/ea08930a666041bbbee8c9f6c0e7951b</documentNamespace>
    <packages>
        <SPDXID>SPDXRef-maven-org.apache.logging.log4j-log4j-api-2.16.0</SPDXID>
        <downloadLocation>NOASSERTION</downloadLocation>
        <externalRefs>
            <referenceCategory>PACKAGE-MANAGER</referenceCategory>
            <referenceLocator>pkg:maven/org.apache.logging.log4j/log4j-api@2.16.0?type=jar</referenceLocator>
            <referenceType>purl</referenceType>
        </externalRefs>
        <filesAnalyzed>false</filesAnalyzed>
        <licenseConcluded>Apache-2.0</licenseConcluded>
        <licenseDeclared>Apache-2.0</licenseDeclared>
        <name>org.apache.logging.log4j:log4j-api</name>
        <versionInfo>2.16.0</versionInfo>
    </packages>
    <packages>
        <SPDXID>SPDXRef-maven-com.fasterxml.jackson.core-jackson-core-2.14.0</SPDXID>
        <downloadLocation>NOASSERTION</downloadLocation>
        <externalRefs>
            <referenceCategory>PACKAGE-MANAGER</referenceCategory>
            <referenceLocator>pkg:maven/com.fasterxml.jackson.core/jackson-core@2.14.0?type=jar</referenceLocator>
            <referenceType>purl</referenceType>
        </externalRefs>
        <externalRefs>
            <comment>source: SONATYPE</comment>
            <referenceCategory>SECURITY</referenceCategory>
            <referenceLocator>http://localhost:8070/ui/links/vln/sonatype-2022-6438</referenceLocator>
            <referenceType>advisory</referenceType>
        </externalRefs>
        <filesAnalyzed>false</filesAnalyzed>
        <licenseConcluded>(Apache-2.0 AND MIT)</licenseConcluded>
        <licenseDeclared>(Apache-2.0 AND MIT)</licenseDeclared>
        <name>com.fasterxml.jackson.core:jackson-core</name>
        <versionInfo>2.14.0</versionInfo>
    </packages>
    <packages>
        <SPDXID>SPDXRef-maven-com.fasterxml.jackson.core-jackson-databind-2.14.0</SPDXID>
        <downloadLocation>NOASSERTION</downloadLocation>
        <externalRefs>
            <referenceCategory>PACKAGE-MANAGER</referenceCategory>
            <referenceLocator>pkg:maven/com.fasterxml.jackson.core/jackson-databind@2.14.0?type=jar</referenceLocator>
            <referenceType>purl</referenceType>
        </externalRefs>
        <filesAnalyzed>false</filesAnalyzed>
        <licenseConcluded>Apache-2.0</licenseConcluded>
        <licenseDeclared>Apache-2.0</licenseDeclared>
        <name>com.fasterxml.jackson.core:jackson-databind</name>
        <versionInfo>2.14.0</versionInfo>
    </packages>
    <packages>
        <SPDXID>SPDXRef-maven-org.apache.logging.log4j-log4j-core-2.16.0</SPDXID>
        <downloadLocation>NOASSERTION</downloadLocation>
        <externalRefs>
            <comment>source: NVD</comment>
            <referenceCategory>SECURITY</referenceCategory>
            <referenceLocator>http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-45105</referenceLocator>
            <referenceType>advisory</referenceType>
        </externalRefs>
        <externalRefs>
            <comment>source: NVD</comment>
            <referenceCategory>SECURITY</referenceCategory>
            <referenceLocator>http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-44832</referenceLocator>
            <referenceType>advisory</referenceType>
        </externalRefs>
        <externalRefs>
            <referenceCategory>PACKAGE-MANAGER</referenceCategory>
            <referenceLocator>pkg:maven/org.apache.logging.log4j/log4j-core@2.16.0?type=jar</referenceLocator>
            <referenceType>purl</referenceType>
        </externalRefs>
        <externalRefs>
            <comment>source: NVD</comment>
            <referenceCategory>SECURITY</referenceCategory>
            <referenceLocator>http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-44228</referenceLocator>
            <referenceType>advisory</referenceType>
        </externalRefs>
        <filesAnalyzed>false</filesAnalyzed>
        <licenseConcluded>Apache-2.0</licenseConcluded>
        <licenseDeclared>Apache-2.0</licenseDeclared>
        <name>org.apache.logging.log4j:log4j-core</name>
        <versionInfo>2.16.0</versionInfo>
    </packages>
    <packages>
        <SPDXID>SPDXRef-maven-com.fasterxml.jackson.core-jackson-annotations-2.14.0</SPDXID>
        <downloadLocation>NOASSERTION</downloadLocation>
        <externalRefs>
            <referenceCategory>PACKAGE-MANAGER</referenceCategory>
            <referenceLocator>pkg:maven/com.fasterxml.jackson.core/jackson-annotations@2.14.0?type=jar</referenceLocator>
            <referenceType>purl</referenceType>
        </externalRefs>
        <filesAnalyzed>false</filesAnalyzed>
        <licenseConcluded>Apache-2.0</licenseConcluded>
        <licenseDeclared>Apache-2.0</licenseDeclared>
        <name>com.fasterxml.jackson.core:jackson-annotations</name>
        <versionInfo>2.14.0</versionInfo>
    </packages>
    <packages>
        <SPDXID>SPDXRef-maven-com.sonatype.testing-test-app-1.0.0</SPDXID>
        <downloadLocation>NOASSERTION</downloadLocation>
        <externalRefs>
            <referenceCategory>PACKAGE-MANAGER</referenceCategory>
            <referenceLocator>pkg:maven/com.sonatype.testing/test-app@1.0.0?type=jar</referenceLocator>
            <referenceType>purl</referenceType>
        </externalRefs>
        <filesAnalyzed>false</filesAnalyzed>
        <licenseConcluded>(LicenseRef-No-Sources AND LicenseRef-Not-Declared)</licenseConcluded>
        <licenseDeclared>(LicenseRef-No-Sources AND LicenseRef-Not-Declared)</licenseDeclared>
        <name>com.sonatype.testing:test-app</name>
        <versionInfo>1.0.0</versionInfo>
    </packages>
    <packages>
        <SPDXID>SPDXRef-generic-sonatype-iq-application-Test-App-01-ea08930a666041bbbee8c9f6c0e7951b</SPDXID>
        <downloadLocation>NOASSERTION</downloadLocation>
        <externalRefs>
            <referenceCategory>PACKAGE-MANAGER</referenceCategory>
            <referenceLocator>pkg:generic/sonatype/iq_application_Test%20App%2001@ea08930a666041bbbee8c9f6c0e7951b</referenceLocator>
            <referenceType>purl</referenceType>
        </externalRefs>
        <filesAnalyzed>false</filesAnalyzed>
        <licenseConcluded>NOASSERTION</licenseConcluded>
        <licenseDeclared>NOASSERTION</licenseDeclared>
        <name>sonatype:iq_application_Test App 01</name>
        <versionInfo>ea08930a666041bbbee8c9f6c0e7951b</versionInfo>
    </packages>
    <relationships>
        <spdxElementId>SPDXRef-DOCUMENT</spdxElementId>
        <relationshipType>DESCRIBES</relationshipType>
        <relatedSpdxElement>SPDXRef-generic-sonatype-iq-application-Test-App-01-ea08930a666041bbbee8c9f6c0e7951b</relatedSpdxElement>
    </relationships>
    <relationships>
        <spdxElementId>SPDXRef-maven-com.fasterxml.jackson.core-jackson-databind-2.14.0</spdxElementId>
        <relationshipType>DEPENDS_ON</relationshipType>
        <relatedSpdxElement>SPDXRef-maven-com.fasterxml.jackson.core-jackson-core-2.14.0</relatedSpdxElement>
    </relationships>
    <relationships>
        <spdxElementId>SPDXRef-maven-com.fasterxml.jackson.core-jackson-databind-2.14.0</spdxElementId>
        <relationshipType>DEPENDS_ON</relationshipType>
        <relatedSpdxElement>SPDXRef-maven-com.fasterxml.jackson.core-jackson-annotations-2.14.0</relatedSpdxElement>
    </relationships>
    <relationships>
        <spdxElementId>SPDXRef-maven-org.apache.logging.log4j-log4j-core-2.16.0</spdxElementId>
        <relationshipType>DEPENDS_ON</relationshipType>
        <relatedSpdxElement>SPDXRef-maven-org.apache.logging.log4j-log4j-api-2.16.0</relatedSpdxElement>
    </relationships>
    <relationships>
        <spdxElementId>SPDXRef-generic-sonatype-iq-application-Test-App-01-ea08930a666041bbbee8c9f6c0e7951b</spdxElementId>
        <relationshipType>DEPENDS_ON</relationshipType>
        <relatedSpdxElement>SPDXRef-maven-org.apache.logging.log4j-log4j-core-2.16.0</relatedSpdxElement>
    </relationships>
    <relationships>
        <spdxElementId>SPDXRef-generic-sonatype-iq-application-Test-App-01-ea08930a666041bbbee8c9f6c0e7951b</spdxElementId>
        <relationshipType>DEPENDS_ON</relationshipType>
        <relatedSpdxElement>SPDXRef-maven-com.fasterxml.jackson.core-jackson-databind-2.14.0</relatedSpdxElement>
    </relationships>
</Document>
```

### Sample SPDX v2.3 SBOM for Analysis in JSON format

```
{
    "SPDXID": "SPDXRef-DOCUMENT",
    "spdxVersion": "SPDX-2.3",
    "creationInfo": {
        "created": "2023-08-21T16:46:39Z",
        "creators": [
            "Tool: Sonatype IQ Server - 1.166.0"
        ]
    },
    "name": "pkg:generic/sonatype/iq_application_Test%20App%2001@ea08930a666041bbbee8c9f6c0e7951b",
    "dataLicense": "CC0-1.0",
    "hasExtractedLicensingInfos": [
        {
            "licenseId": "LicenseRef-No-Sources",
            "extractedText": "No-Sources"
        },
        {
            "licenseId": "LicenseRef-Not-Declared",
            "extractedText": "Not-Declared"
        }
    ],
    "documentNamespace": "http://localhost:8070/ui/links/application/test-app-01/report/ea08930a666041bbbee8c9f6c0e7951b",
    "packages": [
        {
            "SPDXID": "SPDXRef-maven-org.apache.logging.log4j-log4j-api-2.16.0",
            "downloadLocation": "NOASSERTION",
            "externalRefs": [
                {
                    "referenceCategory": "PACKAGE-MANAGER",
                    "referenceLocator": "pkg:maven/org.apache.logging.log4j/log4j-api@2.16.0?type=jar",
                    "referenceType": "purl"
                }
            ],
            "filesAnalyzed": false,
            "licenseConcluded": "Apache-2.0",
            "licenseDeclared": "Apache-2.0",
            "name": "org.apache.logging.log4j:log4j-api",
            "versionInfo": "2.16.0"
        },
        {
            "SPDXID": "SPDXRef-maven-com.fasterxml.jackson.core-jackson-core-2.14.0",
            "downloadLocation": "NOASSERTION",
            "externalRefs": [
                {
                    "referenceCategory": "PACKAGE-MANAGER",
                    "referenceLocator": "pkg:maven/com.fasterxml.jackson.core/jackson-core@2.14.0?type=jar",
                    "referenceType": "purl"
                },
                {
                    "comment": "source: SONATYPE",
                    "referenceCategory": "SECURITY",
                    "referenceLocator": "http://localhost:8070/ui/links/vln/sonatype-2022-6438",
                    "referenceType": "advisory"
                }
            ],
            "filesAnalyzed": false,
            "licenseConcluded": "(Apache-2.0 AND MIT)",
            "licenseDeclared": "(Apache-2.0 AND MIT)",
            "name": "com.fasterxml.jackson.core:jackson-core",
            "versionInfo": "2.14.0"
        },
        {
            "SPDXID": "SPDXRef-maven-com.fasterxml.jackson.core-jackson-databind-2.14.0",
            "downloadLocation": "NOASSERTION",
            "externalRefs": [
                {
                    "referenceCategory": "PACKAGE-MANAGER",
                    "referenceLocator": "pkg:maven/com.fasterxml.jackson.core/jackson-databind@2.14.0?type=jar",
                    "referenceType": "purl"
                }
            ],
            "filesAnalyzed": false,
            "licenseConcluded": "Apache-2.0",
            "licenseDeclared": "Apache-2.0",
            "name": "com.fasterxml.jackson.core:jackson-databind",
            "versionInfo": "2.14.0"
        },
        {
            "SPDXID": "SPDXRef-maven-org.apache.logging.log4j-log4j-core-2.16.0",
            "downloadLocation": "NOASSERTION",
            "externalRefs": [
                {
                    "comment": "source: NVD",
                    "referenceCategory": "SECURITY",
                    "referenceLocator": "http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-45105",
                    "referenceType": "advisory"
                },
                {
                    "comment": "source: NVD",
                    "referenceCategory": "SECURITY",
                    "referenceLocator": "http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-44832",
                    "referenceType": "advisory"
                },
                {
                    "referenceCategory": "PACKAGE-MANAGER",
                    "referenceLocator": "pkg:maven/org.apache.logging.log4j/log4j-core@2.16.0?type=jar",
                    "referenceType": "purl"
                },
                {
                    "comment": "source: NVD",
                    "referenceCategory": "SECURITY",
                    "referenceLocator": "http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-44228",
                    "referenceType": "advisory"
                }
            ],
            "filesAnalyzed": false,
            "licenseConcluded": "Apache-2.0",
            "licenseDeclared": "Apache-2.0",
            "name": "org.apache.logging.log4j:log4j-core",
            "versionInfo": "2.16.0"
        },
        {
            "SPDXID": "SPDXRef-maven-com.fasterxml.jackson.core-jackson-annotations-2.14.0",
            "downloadLocation": "NOASSERTION",
            "externalRefs": [
                {
                    "referenceCategory": "PACKAGE-MANAGER",
                    "referenceLocator": "pkg:maven/com.fasterxml.jackson.core/jackson-annotations@2.14.0?type=jar",
                    "referenceType": "purl"
                }
            ],
            "filesAnalyzed": false,
            "licenseConcluded": "Apache-2.0",
            "licenseDeclared": "Apache-2.0",
            "name": "com.fasterxml.jackson.core:jackson-annotations",
            "versionInfo": "2.14.0"
        },
        {
            "SPDXID": "SPDXRef-maven-com.sonatype.testing-test-app-1.0.0",
            "downloadLocation": "NOASSERTION",
            "externalRefs": [
                {
                    "referenceCategory": "PACKAGE-MANAGER",
                    "referenceLocator": "pkg:maven/com.sonatype.testing/test-app@1.0.0?type=jar",
                    "referenceType": "purl"
                }
            ],
            "filesAnalyzed": false,
            "licenseConcluded": "(LicenseRef-No-Sources AND LicenseRef-Not-Declared)",
            "licenseDeclared": "(LicenseRef-No-Sources AND LicenseRef-Not-Declared)",
            "name": "com.sonatype.testing:test-app",
            "versionInfo": "1.0.0"
        },
        {
            "SPDXID": "SPDXRef-generic-sonatype-iq-application-Test-App-01-ea08930a666041bbbee8c9f6c0e7951b",
            "downloadLocation": "NOASSERTION",
            "externalRefs": [
                {
                    "referenceCategory": "PACKAGE-MANAGER",
                    "referenceLocator": "pkg:generic/sonatype/iq_application_Test%20App%2001@ea08930a666041bbbee8c9f6c0e7951b",
                    "referenceType": "purl"
                }
            ],
            "filesAnalyzed": false,
            "licenseConcluded": "NOASSERTION",
            "licenseDeclared": "NOASSERTION",
            "name": "sonatype:iq_application_Test App 01",
            "versionInfo": "ea08930a666041bbbee8c9f6c0e7951b"
        }
    ],
    "relationships": [
        {
            "spdxElementId": "SPDXRef-DOCUMENT",
            "relationshipType": "DESCRIBES",
            "relatedSpdxElement": "SPDXRef-generic-sonatype-iq-application-Test-App-01-ea08930a666041bbbee8c9f6c0e7951b"
        },
        {
            "spdxElementId": "SPDXRef-maven-com.fasterxml.jackson.core-jackson-databind-2.14.0",
            "relationshipType": "DEPENDS_ON",
            "relatedSpdxElement": "SPDXRef-maven-com.fasterxml.jackson.core-jackson-core-2.14.0"
        },
        {
            "spdxElementId": "SPDXRef-maven-com.fasterxml.jackson.core-jackson-databind-2.14.0",
            "relationshipType": "DEPENDS_ON",
            "relatedSpdxElement": "SPDXRef-maven-com.fasterxml.jackson.core-jackson-annotations-2.14.0"
        },
        {
            "spdxElementId": "SPDXRef-maven-org.apache.logging.log4j-log4j-core-2.16.0",
            "relationshipType": "DEPENDS_ON",
            "relatedSpdxElement": "SPDXRef-maven-org.apache.logging.log4j-log4j-api-2.16.0"
        },
        {
            "spdxElementId": "SPDXRef-generic-sonatype-iq-application-Test-App-01-ea08930a666041bbbee8c9f6c0e7951b",
            "relationshipType": "DEPENDS_ON",
            "relatedSpdxElement": "SPDXRef-maven-org.apache.logging.log4j-log4j-core-2.16.0"
        },
        {
            "spdxElementId": "SPDXRef-generic-sonatype-iq-application-Test-App-01-ea08930a666041bbbee8c9f6c0e7951b",
            "relationshipType": "DEPENDS_ON",
            "relatedSpdxElement": "SPDXRef-maven-com.fasterxml.jackson.core-jackson-databind-2.14.0"
        }
    ]
}
```

### Sample SPDX v2.2 SBOM for Analysis in XML format

```
<?xml version='1.0' encoding='UTF-8'?>
<Document>
    <SPDXID>SPDXRef-DOCUMENT</SPDXID>
    <spdxVersion>SPDX-2.2</spdxVersion>
    <creationInfo>
        <created>2024-07-29T17:43:25Z</created>
        <creators>Tool: Sonatype SBOM Manager - 1.180.0-SNAPSHOT</creators>
    </creationInfo>
    <name>webgoat</name>
    <dataLicense>CC0-1.0</dataLicense>
    <hasExtractedLicensingInfos>
        <licenseId>LicenseRef-Not-Declared</licenseId>
        <extractedText>Extracted license created by Sonatype SBOM Manager</extractedText>
        <name>Not Declared</name>
    </hasExtractedLicensingInfos>
    <hasExtractedLicensingInfos>
        <licenseId>LicenseRef-See-License-Clause</licenseId>
        <extractedText>Extracted license created by Sonatype SBOM Manager</extractedText>
        <name>See-License-Clause</name>
    </hasExtractedLicensingInfos>
    <documentNamespace>nullui/links/sbomManager/management/view/application/webgoat/bom/v1</documentNamespace>
    <packages>
        <SPDXID>SPDXRef-32dd9982-7edc-4cde-85f6-8946cabca003</SPDXID>
        <attributionTexts>Evidence license text for: (Apache-1.1 AND MIT AND Aladdin)</attributionTexts>
        <copyrightText>NOASSERTION</copyrightText>
        <downloadLocation>NOASSERTION</downloadLocation>
        <externalRefs>
            <referenceCategory>PACKAGE-MANAGER</referenceCategory>
            <referenceLocator>pkg:maven/log4j/log4j@1.2.8?type=jar</referenceLocator>
            <referenceType>purl</referenceType>
        </externalRefs>
        <externalRefs>
            <comment>source: SOURCE</comment>
            <referenceCategory>SECURITY</referenceCategory>
            <referenceLocator>http://www.source.com/abc-123</referenceLocator>
            <referenceType>advisory</referenceType>
        </externalRefs>
        <externalRefs>
            <comment>source: SONATYPE</comment>
            <referenceCategory>SECURITY</referenceCategory>
            <referenceLocator>http://localhost:8070/ui/links/vln/sonatype-2010-0053</referenceLocator>
            <referenceType>advisory</referenceType>
        </externalRefs>
        <externalRefs>
            <comment>source: NVD</comment>
            <referenceCategory>SECURITY</referenceCategory>
            <referenceLocator>http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23307</referenceLocator>
            <referenceType>advisory</referenceType>
        </externalRefs>
        <filesAnalyzed>false</filesAnalyzed>
        <licenseConcluded>NOASSERTION</licenseConcluded>
        <licenseDeclared>Apache-1.1</licenseDeclared>
        <name>log4j:log4j</name>
        <versionInfo>1.2.8</versionInfo>
    </packages>
    <packages>
        <SPDXID>SPDXRef-e6a49891-d1d5-4358-8688-b5a03a546f90</SPDXID>
        <copyrightText>NOASSERTION</copyrightText>
        <downloadLocation>NOASSERTION</downloadLocation>
        <externalRefs>
            <comment>source: SONATYPE</comment>
            <referenceCategory>SECURITY</referenceCategory>
            <referenceLocator>http://localhost:8070/ui/links/vln/sonatype-2015-0002</referenceLocator>
            <referenceType>advisory</referenceType>
        </externalRefs>
        <externalRefs>
            <referenceCategory>PACKAGE-MANAGER</referenceCategory>
            <referenceLocator>pkg:maven/commons-collections/commons-collections@3.1?type=jar</referenceLocator>
            <referenceType>purl</referenceType>
        </externalRefs>
        <filesAnalyzed>false</filesAnalyzed>
        <licenseConcluded>NOASSERTION</licenseConcluded>
        <licenseDeclared>Apache-2.0</licenseDeclared>
        <name>commons-collections:commons-collections</name>
        <versionInfo>3.1</versionInfo>
    </packages>
    <packages>
        <SPDXID>SPDXRef-333584e5-0101-4a21-8f5b-61b10926cf3c</SPDXID>
        <copyrightText>NOASSERTION</copyrightText>
        <downloadLocation>NOASSERTION</downloadLocation>
        <externalRefs>
            <referenceCategory>PACKAGE-MANAGER</referenceCategory>
            <referenceLocator>pkg:maven/commons-digester/commons-digester@1.4.1?type=jar</referenceLocator>
            <referenceType>purl</referenceType>
        </externalRefs>
        <filesAnalyzed>false</filesAnalyzed>
        <licenseConcluded>NOASSERTION</licenseConcluded>
        <licenseDeclared>(Apache-1.1 AND LicenseRef-Not-Declared)</licenseDeclared>
        <name>commons-digester:commons-digester</name>
        <versionInfo>1.4.1</versionInfo>
    </packages>
    <packages>
        <SPDXID>SPDXRef-85e600ff-6842-4b60-bbc5-56a45e3a357c</SPDXID>
        <copyrightText>NOASSERTION</copyrightText>
        <downloadLocation>NOASSERTION</downloadLocation>
        <externalRefs>
            <referenceCategory>SECURITY</referenceCategory>
            <referenceLocator>cpe:/a:commons-discovery:commons-discovery:0.2</referenceLocator>
            <referenceType>cpe22Type</referenceType>
        </externalRefs>
        <externalRefs>
            <referenceCategory>PACKAGE-MANAGER</referenceCategory>
            <referenceLocator>pkg:maven/commons-discovery/commons-discovery@0.2?type=jar</referenceLocator>
            <referenceType>purl</referenceType>
        </externalRefs>
        <filesAnalyzed>false</filesAnalyzed>
        <licenseConcluded>NOASSERTION</licenseConcluded>
        <licenseDeclared>(Apache-1.1 AND LicenseRef-Not-Declared)</licenseDeclared>
        <name>commons-discovery:commons-discovery</name>
        <versionInfo>0.2</versionInfo>
    </packages>
    <packages>
        <SPDXID>SPDXRef-0cd0109c-4389-4c65-b95a-1d3b552d902a</SPDXID>
        <copyrightText>NOASSERTION</copyrightText>
        <downloadLocation>NOASSERTION</downloadLocation>
        <externalRefs>
            <referenceCategory>PACKAGE-MANAGER</referenceCategory>
            <referenceLocator>pkg:maven/commons-logging/commons-logging@1.0.4?type=jar</referenceLocator>
            <referenceType>purl</referenceType>
        </externalRefs>
        <externalRefs>
            <referenceCategory>SECURITY</referenceCategory>
            <referenceLocator>cpe:2.3:a:commons-logging:commons-logging:1.0.4:*:*:*:*:*:*:*</referenceLocator>
            <referenceType>cpe23Type</referenceType>
        </externalRefs>
        <filesAnalyzed>false</filesAnalyzed>
        <licenseConcluded>NOASSERTION</licenseConcluded>
        <licenseDeclared>(LicenseRef-See-License-Clause AND Apache-2.0)</licenseDeclared>
        <name>commons-logging:commons-logging</name>
        <versionInfo>1.0.4</versionInfo>
    </packages>
    <packages>
        <SPDXID>SPDXRef-c9f3c210-670e-41c0-993b-af8a7768f25b</SPDXID>
        <copyrightText>NOASSERTION</copyrightText>
        <downloadLocation>NOASSERTION</downloadLocation>
        <externalRefs>
            <referenceCategory>PACKAGE-MANAGER</referenceCategory>
            <referenceLocator>pkg:generic/sonatype/iq_application_webgoat@218214e0852748659076521b3b8ee137</referenceLocator>
            <referenceType>purl</referenceType>
        </externalRefs>
        <filesAnalyzed>false</filesAnalyzed>
        <licenseConcluded>NOASSERTION</licenseConcluded>
        <licenseDeclared>NOASSERTION</licenseDeclared>
        <name>sonatype:iq_application_webgoat</name>
        <versionInfo>218214e0852748659076521b3b8ee137</versionInfo>
    </packages>
    <relationships>
        <spdxElementId>SPDXRef-DOCUMENT</spdxElementId>
        <relationshipType>DESCRIBES</relationshipType>
        <relatedSpdxElement>SPDXRef-c9f3c210-670e-41c0-993b-af8a7768f25b</relatedSpdxElement>
    </relationships>
    <relationships>
        <spdxElementId>SPDXRef-333584e5-0101-4a21-8f5b-61b10926cf3c</spdxElementId>
        <relationshipType>DEPENDS_ON</relationshipType>
        <relatedSpdxElement>SPDXRef-e6a49891-d1d5-4358-8688-b5a03a546f90</relatedSpdxElement>
    </relationships>
    <relationships>
        <spdxElementId>SPDXRef-333584e5-0101-4a21-8f5b-61b10926cf3c</spdxElementId>
        <relationshipType>DEPENDS_ON</relationshipType>
        <relatedSpdxElement>SPDXRef-0cd0109c-4389-4c65-b95a-1d3b552d902a</relatedSpdxElement>
    </relationships>
    <relationships>
        <spdxElementId>SPDXRef-85e600ff-6842-4b60-bbc5-56a45e3a357c</spdxElementId>
        <relationshipType>DEPENDS_ON</relationshipType>
        <relatedSpdxElement>SPDXRef-0cd0109c-4389-4c65-b95a-1d3b552d902a</relatedSpdxElement>
    </relationships>
    <relationships>
        <spdxElementId>SPDXRef-c9f3c210-670e-41c0-993b-af8a7768f25b</spdxElementId>
        <relationshipType>DEPENDS_ON</relationshipType>
        <relatedSpdxElement>SPDXRef-85e600ff-6842-4b60-bbc5-56a45e3a357c</relatedSpdxElement>
    </relationships>
    <relationships>
        <spdxElementId>SPDXRef-c9f3c210-670e-41c0-993b-af8a7768f25b</spdxElementId>
        <relationshipType>DEPENDS_ON</relationshipType>
        <relatedSpdxElement>SPDXRef-333584e5-0101-4a21-8f5b-61b10926cf3c</relatedSpdxElement>
    </relationships>
    <relationships>
        <spdxElementId>SPDXRef-c9f3c210-670e-41c0-993b-af8a7768f25b</spdxElementId>
        <relationshipType>DEPENDS_ON</relationshipType>
        <relatedSpdxElement>SPDXRef-32dd9982-7edc-4cde-85f6-8946cabca003</relatedSpdxElement>
    </relationships>
</Document>
```

### Analysis using the Jenkins plugin

By default, the Jenkins plugin will not evaluate SPDX files. A custom *Scan Target* will be required to analyze the SPDX SBOM.

**Example Pipeline Script with Scan Patterns**

```
nexusPolicyEvaluation iqApplication: 'SampApp', iqScanPatterns: [[scanPattern: '**/*.spdx.xml'], [scanPattern: '**/*.spdx.json']], iqStage: 'build'
```

### Analysis using the Bamboo plugin

Scan Targets in Bamboo control what files are analyzed. To evaluate SPDX SBOM, add spdx.xml or spdx.json to the scan targets via a comma-separated list e.g.

**Example Bamboo Scan Patterns**

```
**/*.spdx.xml,**/*.spdx.json
```

## Swift Application Analysis

The Swift coordinate-based scanning feature provides the ability to scan and evaluate Swift dependencies found in Cocoapods and Swift Package Manager ecosystems.

### Cocoapods

**Podfile.lock** - [- CocoaPods](https://guides.cocoapods.org/using/using-cocoapods.html#what-is-podfilelock) is a dependency manager for Swift and Objective-C [Cocoa projects](https://cocoapods.org/pods/Index) .

Lifecycle analyzes files named Podfile.lock (generated by Cocoapods.)

The Podfile.lock file is generated after the first run of `pod install` and tracks the version of each dependency that was installed. CocoaPods will maintain the dependency versions found in the Podfile.lock until the dependency is updated in the Podfile or `pod update` is called.

See the [Cocoapod documentation](https://guides.cocoapods.org/using/pod-install-vs-update.html) for details on updating dependencies.

**Podfile.lock**

```
PODS:
  - ADMobGenAdapter (1.5.2):
    - ADMobGenFoundation
  - ADMobGenFoundation (0.7.2)
  - ADMobGenGDT (4.10.0):
    - ADMobGenAdapter
    - ADMobGenFoundation
    - GDTMobSDK (= 4.10.2)
  - GDTMobSDK (4.10.2):
    - GDTMobSDK/GDTMobSDK (= 4.10.2)
  - GDTMobSDK/GDTMobSDK (4.10.2)
  - YogaKit (1.2.0)
  - libpng (1.4.9)
  - libpng (1.0.8)
  - GethDevelop (1.8.17)

DEPENDENCIES:
  - ADMobGenGDT (from `../`)

SPEC REPOS:
  https://github.com/cocoapods/specs.git:
    - ADMobGenAdapter
    - ADMobGenFoundation
    - GDTMobSDK

EXTERNAL SOURCES:
  ADMobGenGDT:
    :path: "../"

SPEC CHECKSUMS:
  ADMobGenAdapter: 5ab3531d5659c96812e6da545c1ec160b9991a2e
  ADMobGenFoundation: de6e4f7b09df256a347878d0f0e0438c1feac94e
  ADMobGenGDT: 77d18f682136e9e90fc9e5dfb0fc57637d5441d7
  GDTMobSDK: 6fde44a4f80c36051d5d879df8bb280034c31431

PODFILE CHECKSUM: 441850ec31e67c6ea8241a64c55657d490e51d66

COCOAPODS: 1.7.0.beta.2
```

### Swift Package Manager

[Swift Package Manager (SPM)](https://www.swift.org/package-manager/) is a tool for managing the distribution of [Swift packages](https://swiftpackageindex.com/) . SPM is similar to Cocoapods, Ruby Gems, and NPM. You can use SPM from the command line with commands like **swift build** and **swift test** or with compatible IDEs. SPM leverages URLs to Git repositories and version dependencies using Git tags. [ [0](https://docs.vapor.codes/4.0/spm/) ]

Lifecycle analyzes the file named `Package.resolved` . The dependencies under the "pins" section are evaluated.

**Example**

```
{
  "object": {
    "pins": [
      {
        "package": "RxSwift",
        "repositoryURL": "https://github.com/ReactiveX/RxSwift.git",
        "state": {
          "branch": null,
          "revision": "980d2afceb985a5598d7bc6116557b75469857f2",
          "version": "5.1.0"
        }
      }
    ]
  },
  "version": 1
}

```

## Yum Analysis

The Yum coordinate-based matching feature provides the ability to scan and evaluate Yum package dependencies found in a yum-packages.txt file.

Files named yum-packages.txt are analyzed. (tab-separated list of Yum packages)

**Note:** Lifecycle and Repository Firewall supports Yum components coming from the EPEL repository.

The first two segments corresponding to the name and version of the dependency are evaluated.

```
AntTweakBar.i386       1.14-5.el5
```

Invoke a Sonatype CLI scan of a directory or subdirectories containing a yum-packages.txt file

- Create yum-packages.txt file
- Run the Yum list command and pipe results to a txt file

```
AntTweakBar.i386         1.14-5.el5            installed
AGReader.i686            1.2-6.el6             installed
389-admin.x86_64         1.1.29-1.el5          installed
```

## Hosted Repository Analysis

Hosted repository analysis provides a way to analyze your built applications without modifying the build systems. Using hosted repository analysis, security teams can measure and mitigate risks in an artifact staging workflow before promoting artifacts to production repositories.

### Requirements

- Sonatype License for Lifecycle and Nexus Repository (Postgres/H2 versions only)
- Nexus Repository 3.64+
- Connect Lifecycle to Nexus Repository
- Enable feature flag for hosted repository scanning on Nexus Repository (requires restart)

### Limitations

- Functionality is limited to scanning the Maven2 format for hosted repositories.
- Implementation is performed through the API

### Configuration

To use the feature you will need to enable the feature flag for Nexus Repository shown below and connect *Lifecycle* to the Repository.

### Lifecycle parameters

The API calls on this page will require either an *organizationId* for new applications or an existing *applicationId* . You can [locate the organizationId](#UUID-60099022-5d8b-6861-cfb6-2321955b68cd) from the *Lifecycle UI* or by calling the [Organization REST API](#UUID-2b83db02-df62-d885-19a8-e6ab5c6fe256) . The *applicationId* can be found in the *Lifecycle UI* or by calling the [Application REST API](#UUID-98adbe51-96e2-70d8-15c6-35e4a74130a9) .

### Evaluate an artifact within a hosted repository

Target specific artifacts inside the hosted repository for a *Lifecycle* analysis. Using an organizationId this endpoint will automatically add applications to the *Lifecycle* organization when not present.

**Example for automatically created application name**

For an artifact in the repository */maven-hosted/org/slf4j/slf4j-api/* , the automatically created application name will be *org-slf4j-slf4j-api*

```
POST /service/rest/v1/scan/execute/{repostoryName}/{path}
```

The above command required a body element to be included. Review the Lifecycle parameters section for the Organization or Application IDs.

The optional `StageId` defaults to the `build` stage.

```
{
  "iqOrganizationId": "string",
  "iqApplicationId": "string",
  "iqStageTypeId": "string
}
```

Example curl command

*curl* commands should be run against the Nexus Repository instance where the repository/artifact to be scanned is located.

```
curl -X POST -u <username>:<password> \
  "<host>/service/rest/v1/scan/execute/{repositoryName}/{path}
  -H "Content-Type: application/json" \
  -d "{\"iqOrganizationId\": \"a5c56d00972e41188601c02700ced17c\", \"iqStageTypeId\": \"release\"}"
```

Example response

```
{
  "scanId": "b163b59b1f36425099ad91a18f353d3b",
  "reportUrl": "ui/links/application/commons-fileupload-commons-fileupload/report/b163b59b1f36425099ad91a18f353d3b"
}
```

If there are multiple versions of an artifact found the scan path target, then the latest version number ( **not** the most recently uploaded version) will be retrieved and scanned.

### Configure monitoring on an artifact's namespace

Hosted repository analysis may be configured to monitor an artifact's namespace for new versions of an artifact and run an analysis of any new artifacts with higher version numbers submitted to the hosted repository. The new version and scan will replace the latest *Lifecycle* report for that application if one exists already.

## Hugging Face Model Analysis

### Hugging Face Ecosystem

*IQ Server* Hugging Face application analysis supports all AI/ML models hosted on the Hugging Face (HF) platform. These include a variety of popular AI/ML models in use by the developer community, e.g. Large Language Models (LLMs), image classification, object detection, speech recognition etc.

## Threats in AI/ML Models

*Sonatype Lifecycle* can detect malware, vulnerabilities and license obligations within AI/ML models downloaded from the Hugging Face repository. These capabilities are continuously evolving to stay in sync with the rapidly changing open-source AI/ML technology landscape. Please check release notes for the latest enhancements to our AI/ML threat protection capabilities.

### Risks with AI/ML Components

AI/ML components are reusable building blocks generally written in Python, C++, Java, Go(Golang) that contribute directly to the functionality of an AI/ML system. These functionalities include:

- Data pre-processing for data cleaning, transformation, and feature engineering.
- Data pre-processing for data cleaning, transformation, and feature engineering.
- Model evaluation to assess the performance of trained ML models based on accuracy and effectiveness.
- Inference components that deploy the trained models to new data.
- Natural Language Processing (NLP) components that handle text analysis, sentiment analysis and language translations.
- Computer Vision components that see or interpret images for object or image recognition.

*Sonatype Lifecycle* with its comprehensive coordinate matching [policy constraints](#UUID-39d840f0-d51b-c09b-8272-415acbc57462) can detect most vulnerabilities affecting these components during policy evaluations. It provides protection against [security](#UUID-d9e153b9-21d1-61f5-85a5-8f3fe3c650da_section-idm234860151231854) , [legal](#UUID-d9e153b9-21d1-61f5-85a5-8f3fe3c650da_section-idm234860153743091) and [quality](#UUID-d9e153b9-21d1-61f5-85a5-8f3fe3c650da_section-idm234860155726784) risks.

### AI/ML Security Risk

*Sonatype Lifecycle* can help identify open-source AI/ML libraries of a wide range of formats on Hugging Face, for e.g. Pytorch with extensions `.bin` , `.pt` , `.pkl` , `.pickle` . Additionally, our Security Research team identifies models that execute malicious code, have been built with poisoned data sets, and other model related vulnerabilities.

### AI/ML Legal Risk

*Sonatype Lifecycle* and Advanced Legal Pack (ALP) can detect and manage license attributions and obligations by providing detailed information on effective, declared, and observed licenses for open-source AI/ML models on Hugging Face. Additionally, Lifecycle and ALP provide legal coverage for obligations that are specific to AI/ML models like “restriction on use of output to train other models” or “restriction on use of output for commercial purposes”.

### AI/ML Quality Risk

Architects and AppSec teams can create policy to ensure that the models being used by data science or development meet certain quality criteria. For instance, Lifecycle supports policy on if the model is [Foundation or derivative](#UUID-d9e153b9-21d1-61f5-85a5-8f3fe3c650da_section-idm234832704377338) , or contains [Objectionable Content](#UUID-d9e153b9-21d1-61f5-85a5-8f3fe3c650da_N1748445288080) .

Having these policies in place can be used to automate many of the gates otherwise required before adopting a model.

### AI/ML Derivative Model Detection

Data scientists and data engineers often encounter the need to retrain an existing open-source model to enhance the accuracy or adjust a "drift" in the performance of a model. They can tweak a Foundation Model by retraining or fine-tuning it on different data sets, adjusting weights, features and hyper-parameters.

An AI/ML derivative model is a tweaked version derived from a Foundation Model.

Such derivative AI/ML models are also hosted in Hugging Face repositories. However, the derivative models may not have the exact same license restrictions and obligations as the Foundation Model. They may not be proven, or vetted for the organization's business case.

The " [Derivative AI Model](#UUID-39d840f0-d51b-c09b-8272-415acbc57462) " policy condition allows users to set a policy to check the lineage of the AI model being used in the application. The policy evaluation will report a violation if a derivative model is used. The report will include the name of corresponding Foundation Model.

The " [Derivative AI Model](#UUID-39d840f0-d51b-c09b-8272-415acbc57462) " condition can also be used to establish provenance by ensuring that the exact same AI model that has been approved for use is actually being used in the application. This will ensure that other derived AI models which may be compromised or do not satisfy the accuracy and relevance requirements of the organization's needs, do not enter the development pipelines.

### Objectionable AI Detection

As part of efforts to promote Responsible AI, models are reviewed for content that include offensive and demeaning language that could lead to hostile or alienating environments for people belonging to a specific gender, race, nationality or identifying with other physical/psychological human factors.

Such models violate the organizational content policy and are tagged as *Objectionable* . Sonatype Component Intelligence team reviews if the model is tagged as Not For All Audiences (by Hugging Face) or NSFW (Not Safe For Work) as reported by the creator of the model/repository, or whether the model/repository contains banned terms/phrases in its name or in Readme.

The " [AI Content" policy condition](https://help.sonatype.com/en/policy-constraints.html#idp280435) allows users to set a policy to check if the model is tagged as Objectionable AI. The policy evaluation will report a violation if an AI model tagged as *Objectionable* is used.

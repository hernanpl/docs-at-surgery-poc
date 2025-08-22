---
layout: default
title: "Quarantine REST API"
parent: Firewall APIs
nav_order: 3
---

# Quarantine REST API

The Quarantine API is used to report on quarantined components in the Repository Firewall. The results list the violations keeping those components in quarantine.

```
GET  api/v2/reports/components/quarantined
GET  api/v2/reports/components/quarantined?purl={purl}
POST api/v2/repositories/quarantine/{quarantineId}/release

```

## List Components in Quarantine

```
GET api/v2/reports/components/quarantined
```

A sample request to list the components in quarantine is done by issuing the following curl command:

```
curl -u admin:admin123 -X GET http://localhost:8070/api/v2/reports/components/quarantined
```

### Response

Each repository containing quarantined components is listed along with the components and policy violations triggering quarantine. In the case where all policy violations causing quarantine have been waived but the component has not been released from quarantine, there will be no policy violations.

```
{
  "componentsInQuarantine":[
    {
      "repository":{
        "repositoryId":"579729e6b3134c0bb40de1ac077288be",
        "publicId":"maven-central",
        "format":"maven2"
      },
      "components":[
        {
          "component":{
            "packageUrl":"pkg:maven/tomcat/tomcat-util@5.5.23?type=jar",
            "hash":"1249e25aebb15358bedd",
            "componentIdentifier":{
              "format":"maven",
              "coordinates":{
                "artifactId":"tomcat-util",
                "classifier":"",
                "extension":"jar",
                "groupId":"tomcat",
                "version":"5.5.23"
              },
              "quarantineId":"21d7f6366c3c49eea03eaf416f37cd17",
              "quarantineTime":"2019-10-16T20:52:27.659+0000"
            }
          },
          "policyViolations":[
            {
              "policyId":"775a6e88799040c5bb2dd8f020124d07",
              "policyName":"Security-High",
              "policyViolationId":"12ba38f6d38b4f2585c5f3415f094af4",
              "threatLevel":9,
              "constraintViolations":[
                {
                  "constraintId":"5244a1a9d0374a459144e8d93d192051",
                  "constraintName":"High risk CVSS score",
                  "reasons":[
                    {
                      "reason":"Found security vulnerability CVE-2017-5647 with severity 7.5."
                    },
                    {
                      "reason":"Found security vulnerability CVE-2017-5647 with severity 7.5."
                    }
                  ]
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}
```

## Specified Components in Quarantine

```
GET api/v2/reports/components/quarantined?purl={purl}
```

A sample request to query specific components in quarantine is done by issuing the following curl command:

```
curl -u admin:admin123 -X GET http://localhost:8070/api/v2/reports/components/quarantined?purl=pkg:maven/org.codehaus.plexus/plexus-utils@1.1?type=jar
```

## Release from Quarantine

This endpoint is used when a repository component requires to be released from quarantine. All policy violations causing the component to be in quarantine will be waived and then the component will be released from quarantine.

To release a component from quarantine the quarantine ID of the component is needed.

```
POST api/v2/repositories/quarantine/{quarantineId}/release
```

A sample request to release a component from Quarantine with a required comment

```
curl -u admin:admin123 -H "Content-Type: text/plain; charset=UTF-8" -X POST http://localhost:8070/api/v2/repositories/quarantine/21d7f6366c3c49eea03eaf416f37cd17/release -d "waiver comment"
```

### Response

The response includes the newly waived policy violations that were required in order to release the component from quarantine. In the case where all proxy policy violations causing quarantine ( **fail** action) were already waived, there will be no policy violations to list since they were already waived, the component is simply released from quarantine.

```
{
  "componentReleasedFromQuarantine":{
    "component":{
      "packageUrl":"pkg:maven/tomcat/tomcat-util@5.5.23?type=jar",
      "hash":"1249e25aebb15358bedd",
      "componentIdentifier":{
        "format":"maven",
        "coordinates":{
          "artifactId":"tomcat-util",
          "classifier":"",
          "extension":"jar",
          "groupId":"tomcat",
          "version":"5.5.23"
        }
      },
      "quarantineTime":"2019-10-16T20:50:27.659+0000",
      "quarantineReleaseTime":"2019-10-16T20:52:27.659+0000"
    },
    "waivedPolicyViolations":[
      {
        "policyId":"775a6e88799040c5bb2dd8f020124d07",
        "policyName":"Security-High",
        "policyViolationId":"12ba38f6d38b4f2585c5f3415f094af4",
        "threatLevel":9,
        "constraintViolations":[
          {
            "constraintId":"5244a1a9d0374a459144e8d93d192051",
            "constraintName":"High risk CVSS score",
            "reasons":[
              {
                "reason":"Found security vulnerability CVE-2017-5647 with severity 7.5."
              },
              {
                "reason":"Found security vulnerability CVE-2017-5647 with severity 7.5."
              }
            ]
          }
        ]
      }
    ]    
  }
}
```

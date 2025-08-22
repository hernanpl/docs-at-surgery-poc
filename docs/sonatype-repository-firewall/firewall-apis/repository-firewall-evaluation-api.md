---
layout: default
title: "Repository Firewall Evaluation API"
parent: Firewall APIs
nav_order: 2
---

# Repository Firewall Evaluation API

Use the Repository Firewall Evaluation API to preemptively evaluate components as when requested during a build through a proxy repository. This simplifies evaluating components through the Repository Firewall as the components do not have to be first downloaded through the proxy repository from the public ecosystems.

When a match is found using the file hash with the pathname or packageUrl, the evaluation returns the component details including any violations of the policies for the repository. Otherwise, the component is reported as unknown. A request may contain a maximum of 100 components for evaluation in one request.

## Evaluating components

The evaluation request requires the identifier for the repository manager and the proxy repository. These are used to determine the policy to use in the evaluation.

See [Firewall API](#UUID-d516f5b1-1573-aae2-7261-107d95f5fb67) for details on obtaining repository identifiers.

```
POST /api/v2/firewall/components/{repositoryManagerId}/{repositoryId}/evaluate
```

Review the documentation for [Package URL and Component Identifiers](#UUID-e1088e50-6e44-edf0-d5af-178b1349e7bd) for each ecosystem.

The data element in the POST request requires an array of component identifiers using the component hash and either the pathname or the packageURL to evaluate. This example includes both the pathname and packageURL however this is not required.

```
{
  "format":"maven2",
  "components":
  [
    {
      "pathname":"commons-fileupload/commons-fileupload/1.0/commons-fileupload-1.0.jar",
      "packageUrl":"pkg:maven/commons-fileupload/commons-fileupload@1.0",
      "hash":"2366159e25523d99e96d05211a2fa5399c938735"
    }
  ]
}
```

Example request

```
curl -X POST -u admin:admin123 -H "Content-Type: application/json" \
  -d "{\"format\":\"maven2\",\"components\":[{\"pathname\":\"commons-fileupload/commons-fileupload/1.0/commons-fileupload-1.0.jar\",\"packageUrl\":\"pkg:maven/commons-fileupload/commons-fileupload@1.0\",\"hash\":\"2366159e25523d99e96d05211a2fa5399c938735\"}]}" \
  "http://localhost:8070/api/v2/firewall/components/d90592ce43174f7ea9b5b265f14a8ff1/556cea6db6b84e4fa6e04f9e3ebf13d9/evaluate"

```

### Response: evaluating components

```
{
  "repositoryId": "556cea6db6b84e4fa6e04f9e3ebf13d9",
  "repositoryManagerId": "d90592ce43174f7ea9b5b265f14a8ff1",
  "repositoryPublicId": "maven-proxy",
  "repositoryType": "proxy",
  "results":
[
  {
  "catalogDate": "2005-11-22T18:09:21.000+0000",
  "component":
    {
    "hash": "2366159e25523d99e96d05211a2fa5399c938735",
    "packageUrl": "pkg:maven/commons-fileupload/commons-fileupload@1.0",
    "pathname": "commons-fileupload/commons-fileupload/1.0/commons-fileupload-1.0.jar"
  },
  "policyViolations":
  [
    {
      "constraintViolations":
          [
            {
              "constraintId": "bfea4a16f0c34fa5853998e367f1c569",
              "constraintName": "High risk CVSS score",
              "reasons":
              [
                {
                  "reason": "Found security vulnerability CVE-2014-0050 with severity >= 7 (severity = 7.5)",
                  "reference": null
                },
                {
                  "reason": "Found security vulnerability CVE-2014-0050 with severity < 9 (severity = 7.5)",
                  "reference": null
                }
              ]
            }
          ],
          "policyId": "5d9e1a8b839e435f8dcd00cc20c87e20",
          "policyName": "Security-High",
          "policyViolationId": "eddcaafac4474c49b15bacd2542c1c0f",
          "threatLevel": 9
    },
    {
          "constraintViolations":
          [
            {
              "constraintId": "05ea46fb3ed149d084dcc8e6e61ca02c",
              "constraintName": "Low risk CVSS score",
              "reasons":
              [
                {
                  "reason": "Found security vulnerability CVE-2013-0248 with severity >= 0 (severity = 3.3)",
                  "reference": null
                },
                {
                  "reason": "Found security vulnerability CVE-2013-0248 with severity < 4 (severity = 3.3)",
                  "reference": null
                }
              ]
            }
          ],
          "policyId": "034487b7ed3247d2b33307fcc6c75708",
          "policyName": "Security-Low",
          "policyViolationId": "9b4b0fcb83ce4705b075aadc954fbe7d",
          "threatLevel": 3
    },
    {
      "constraintViolations":
      [
        {
          "constraintId": "70476a86871c4c5099b883ef51274082",
          "constraintName": "Version is unpopular",
          "reasons":
          [
            {
              "reason": "Relative popularity was <= 10% (relative popularity = 1%)",
              "reference": null
            }
          ]
        }
      ],
      "policyId": "c5fa791ac71b4d80b3a7a593b1aa3ea9",
      "policyName": "Architecture-Quality",
      "policyViolationId": "9ba7f605b92e4714927f0d82f7e98857",
      "threatLevel": 1
    }
  ]
}
```

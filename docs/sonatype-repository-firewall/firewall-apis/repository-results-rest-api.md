---
layout: default
title: "Repository Results REST API"
parent: Firewall APIs
nav_order: 4
---

# Repository Results REST API

The Repository Results REST API allows for requesting information about the components in a repository. Depending on the owner type this endpoint may return details of multiple repositories. This REST API endpoint is accessed with the `View IQ Elements` permission.

## Repository Results

Credentials with `View IQ Elements` are required to search for the components in a repository.

```
POST /api/experimental/repositories/{ownerType: repository_container|repository_manager|repository}/{ownerId}/results/details
```

The search parameters must be included as the request body. See the reference section below for details on the search parameter.

```
{
    "page": 1,
    "pageSize": 10,
    "searchFilters": [
        {
            "filterableField": "COMPONENT_COORDINATES",
            "value": "ant"
        },
        {
            "filterableField": "REPOSITORY_ID",
            "value": "99285af9923c4ec1ae60529addab254f"
        }
    ],
    "sortFields": [
        {
            "sortableField": "QUARANTINE_TIME",
            "asc": false,
            "sortPriority": 1
        }
    ],
    "matchStateFilters": [
        "MATCH_STATE_EXACT"
    ],
    "violationStateFilters" : [
        "VIOLATION_STATE_OPEN"
    ],
    "threatLevelFilters": [
        0,
        10
    ],
    "aggregate": false
}
```

### Completed curl request with escaped quotes

```
curl -X POST \
  -u admin:admin123 \
  -H "Content-Type: application/json" \
  "http://localhost:8070/api/experimental/repositories/repository_container/REPOSITORY_CONTAINER_ID/results/details" \
  -d "{\"page\": 1,\"pageSize\": 4, \"matchStateFilters\": [\"MATCH_STATE_ALL\"], \"violationStateFilters\": [\"VIOLATION_STATE_ALL\"], \"searchFilters\": [{\"filterableField\": \"REPOSIOTRY_MANAGER_ID\", \"value\": \"4ebc94d10f6b4f3dbc1a3375e2f3678\"}],\"sortFields\": [{\"sortableField\": \"POLICY_NAME\", \"asc\": false, \"sortPriority\": 1}]}"
```

### Example Response

```
{
    "repositoryResultsDetails": [
        {
            "threatLevel": 7,
            "policyName": "Security-Medium",
            "repositoryManagerId": "6d27e83a8d5a4befa5f97d2a7f32b352",
            "repositoryId": "99285af9923c4ec1ae60529addab254f",
            "componentDisplayText": "ant : ant : 1.6.1",
            "pathname": "ant/ant/1.6.1/ant-1.6.1.jar",
            "componentIdentifier": {
                "format": "maven",
                "coordinates": {
                    "artifactId": "ant",
                    "classifier": "",
                    "extension": "jar",
                    "groupId": "ant",
                    "version": "1.6.1"
                }
            },
            "hash": "684aeca90db2a55234f5",
            "matchStateId": "exact",
            "quarantineTime": 1711040046780,
            "waived": false
        },
        {
            "threatLevel": 7,
            "policyName": "Security-Medium",
            "repositoryManagerId": "6d27e83a8d5a4befa5f97d2a7f32b352",
            "repositoryId": "99285af9923c4ec1ae60529addab254f",
            "componentDisplayText": "ant : ant : 1.6.1",
            "pathname": "ant/ant/1.6.1/ant-1.6.1.jar",
            "componentIdentifier": {
                "format": "maven",
                "coordinates": {
                    "artifactId": "ant",
                    "classifier": "",
                    "extension": "jar",
                    "groupId": "ant",
                    "version": "1.6.1"
                }
            },
            "hash": "684aeca90db2a55234f5",
            "matchStateId": "exact",
            "quarantineTime": 1711040046780,
            "waived": false
        }
    ],
    "hasNextPage": false
}
```

## Repository results search parameter reference

The following are details on the search parameters used to filter repository results.

- The current page of the results. Use this field to iterate from one page to the next.
- The number of items returned per request.
- An array of search parameters may be included to narrow the results. The repository ID may be used to filter to a specific repository.
- An array of sort parameters may be included and ordered by the provided priority.
- See [Component Identification](#UUID-c8a1f963-f80b-dd2f-ca31-eac799d3267e) for details on match states.
- Narrow results by the state of the violation.
- Provide a range of lowest to highest threat levels to focus your search results.
- Results may be aggregated together to simplify navigating components in the repository. **true** : component is listed once with its highest policy violation **false** : every violation is listed for the component

---
layout: default
title: "Package URLs (purl) and Component Identifiers"
parent: Sonatype IQ Server
nav_order: 15
---

# Package URLs (purl) and Component Identifiers

Sonatype uses two methods for representing a component in the REST API operations.

Format-specific identifiers in a JSON object layout consisting of the format and component coordinates used by the ecosystem.

```
"componentIdentifier": {
  "format": "{ecosystem}",
  "coordinates": {
    "package": "{component name}",
    "version": "{version number}"
  }
}
```

A single URL parameter using a common industry standard structure. See the [purl spec](https://github.com/package-url/purl-spec) project for details on the specification's structure. In some cases, Sonatype may deviate from the purl spec standard to precisely identify components used in your application.

```
"packageUrl": "pkg:{ecosystem}/[{namespace}/]{component_name}@{version}[?{qualifier}={value}]"
```

## Component Identifiers in the REST APIs

Some endpoints (such as the [Component Versions REST API](#UUID-22972711-77d0-8a95-5855-ae80ddf97f59) ) are more permissive than most REST API operations relating to missing coordinates. These will have more optional coordinates than those listed on this page.

## a-name

An "Authoritative Name" or "a-name" is a Sonatype identification process in which individual JavaScript files are associated with the package from where they were first identified. The scanned javascript files could originate from components in many different ecosystems, such as npm, python, maven, nuget, etc. During a-name matching, we attempt to find the source component that most closely matches the scanned files.

This process involves a 'best guess' as to the file's source that may not reflect the exact component/version used in your application. This method is often used when the packaging manifests are unavailable during the analysis or the JavaScript file is not found in any packages from the manifest.

- name
- version
- qualifier (optional)

```
"componentIdentifier": {
  "format": "a-name",
  "coordinates": {
    "name": "pouchdb",
    "version": "6.3.1"
  }
}
```

```
"packageUrl": "pkg:a-name/pouchdb@6.3.1"
```

## Maven Package URL Example

- groupId
- artifactId
- version
- extension
- classifier (optional)

Sample JSON for a Maven component identifier is provided below:

```
"componentIdentifier": {
  "format": "maven",
  "coordinates": {
    "artifactId": "commons-fileupload",
    "groupId": "commons-fileupload",
    "version": "1.2.2",
    "extension":"jar"      
  }
}
```

Sample JSON for a Maven purl is provided below:

```
"packageUrl": "pkg:maven/commons-fileupload/commons-fileupload@1.2.2?type=jar"
```

## npm Package URL Example

For npm component identifiers, the following coordinates are supported:

- packageId
- version
- scoped package

Sample JSON for a npm component identifier is provided below:

```
"componentIdentifier": {
  "format": "npm",
  "coordinates": {
    "packageId": "grunt-bower-submodule",
    "version": "0.2.3"
  }
}
```

Sample JSON for an npm purl is provided below:

```
"packageUrl": "pkg:npm/grunt-bower-submodule@0.2.3"
```

### Scoped npm packages

To use a scoped npm package in a package URL you will need to include the scope as a URL encoded '@' namespace. For example, to include the package `pkg:npm/@storybook/types@8.2.9` you must encode the '@' symbol with the encoding ' `%40` ' indicator.

```
pkg:npm/%40storybook/types@8.2.9
```

See the [package URL](https://github.com/package-url/purl-spec/blob/master/PURL-TYPES.rst#npm) documentation for details.

## Nuget Package URL Example

For Nuget component identifiers, the following coordinates are supported:

- packageId
- version

Sample JSON for a NuGet component identifier is provided below:

```
"componentIdentifier": {
  "format": "nuget",
  "coordinates": {
    "packageId": "Nirvana.MongoProvider",
    "version": "1.0.53"
  }
}
```

Sample JSON for a NuGet purl is provided below:

```
"packageUrl": "pkg:nuget/Nirvana.MongoProvider@1.0.53"
```

## PyPI Package URL Example

Sonatype Data Services requires including the `extension` parameter to provide more precise results as to the package used. This requirement deviates from the pURL specifications.

Querying `whl` files requires the environment qualifier as each environment returns different artifacts with different vulnerabilities.

**Tarballs (tar.gz)** : do not have a qualifier as they are platform-independent and may be compiled on any platform supporting Python

**Wheel (whl)** : platform-specific and requires a qualifier

For PyPI component identifiers, the following coordinates are supported:

- name
- version
- extension *[ whl | tar.gz ]*
- qualifier *[whl: required | tar.gz: not required]*

Sample JSON for a PyPI component identifier is provided below:

```
"componentIdentifier": {
  "format": "pypi",
  "coordinates": {
    "name": "jaraco.logging",
    "version": "1.5"
  }
}
```

Sample JSON for a PyPI purl is provided below:

```
"packageUrl": "pkg:pypi/jaraco.logging@1.5?extension=whl&qualifier=py2.py3-none-any"
```

## rpm Package URL Example

For rpm component identifiers, the following coordinates are supported:

- name
- version
- architecture

Sample JSON for a rpm component identifier is provided below:

```
"componentIdentifier": {
  "format": "rpm",
  "coordinates": {
    "name": "AGReader",
    "version": "1.2-6.el6",
    "architecture": "ppc64"      
  }
}
```

Sample JSON for an RPM purl is provided below:

```
"packageUrl": "pkg:rpm/AGReader@.2-6.el6?arch=ppc64"
```

## Gem Package URL Example

For Gem component identifiers, the following coordinates are supported:

- name
- version
- platform (optional)

Sample JSON for a Gem component identifier is provided below:

```
"componentIdentifier": {
  "format": "gem",
  "coordinates": {
    "name": "rails",
    "version": "5.0.4"
  }
}
```

Sample JSON for a gem purl is provided below:

```
"packageUrl": "pkg:gem/rails@5.0.4"
```

## Golang Package URL Example

For Go component identifiers, the following coordinates are supported:

- name
- version

Sample JSON for a Go component identifier is provided below:

```
"componentIdentifier": {
  "format": "golang",
  "coordinates": {
    "name": "github.com/rs/cors",
    "version": "v1.4.0"
  }
}
```

Sample JSON for a Golang purl is provided below:

```
"packageUrl": "pkg:golang/github.com/rs/cors@v1.4.0"
```

## Conan Package URL Example

For Conan component identifiers, the following coordinates are supported:

- name
- version
- channel (optional)
- owner (optional)

Sample JSON for a Conan component identifier is provided below:

```
"componentIdentifier": {
  "format": "conan", 
  "coordinates": { 
        "channel": "", 
        "name": "libxml2", 
        "owner": "bincrafters", 
        "version": "2.9.8" 
  }
}
```

Sample JSON for a Conan purl is provided below:

```
"packageUrl": "pkg:conan/bincrafters/libxml2@2.9.8"
```

## Conda Package URL Example

For Conda component identifiers, the following coordinates are supported:

- name
- version
- channel (optional)
- subdir (optional)
- build (optional)
- type (optional)

Sample JSON for a Conda component identifier is provided below:

```
"componentIdentifier": {
  "format": "conda",
  "coordinates": {
    "name": "openssl",
    "version": "1.0.2l",
    "channel": "main",
    "subdir": "linux-64",
    "build": "h077ae2c_5",
    "type": "tar.bz2"
   }
}
```

Sample JSON for a Conda purl is provided below:

```
"packageUrl": "pkg:conda/openssl@1.0.2l?channel=main&subdir=linux-64&build=h077ae2c_5&type=tar.bz2"
```

## Bower Package URL Example

For Bower component identifiers, the following coordinates are supported:

- name
- version

Sample JSON for a Bower component identifier is provided below:

```
"componentIdentifier": {
  "format": "bower",
  "coordinates": {
    "name": "js-yaml",
    "version": "2.0.1"
  }
}
```

Sample JSON for a Bower purl is provided below:

```
"packageUrl": "pkg:bower/js-yaml@2.0.1"
```

## Composer Package URL Example

For Composer component identifiers, the following coordinates are supported:

- namespace
- name
- version

Sample JSON for a Composer component identifier is provided below:

```
"componentIdentifier": {
  "format": "composer",
  "coordinates": {
        "namespace": "components",
    "name": "jqueryui",
    "version": "1.11.4"
  }
}
```

Sample JSON for a Composer purl is provided below:

```
"packageUrl": "pkg:composer/components/jqueryui@1.11.4"
```

## Cran Package URL Example

For Cran component identifiers, the following coordinates are supported:

- name
- version
- type (optional)

Sample JSON for a Cran component identifier is provided below:

```
"componentIdentifier": {
  "format": "cran",
  "coordinates": {
    "name": "readxl",
    "version": "1.1.0",
    "type": "tar.gz"
  }
}
```

Sample JSON for a Cran purl is provided below:

```
"packageUrl": "pkg:cran/readxl@1.1.0?type=tar.gz"
```

## Cargo Package URL Example

For Cargo component identifiers, the following coordinates are supported:

- name
- version
- type (optional)

Sample JSON for a Cargo component identifier is provided below:

```
"componentIdentifier": {
  "format": "cargo",
  "coordinates": {
    "name": "grin",
    "version": "1.0.0",
    "type": "crate"
  }
}
```

Sample JSON for a Cargo purl is provided below:

```
"packageUrl": "pkg:cargo/grin@1.0.0?type=crate"
```

## CocoaPods Package URL Example

For CocoaPods component identifiers, the following coordinates are supported:

- name
- version

Sample JSON for a CocoaPods component identifier is provided below:

```
"componentIdentifier": {
  "format": "cocoapods",
  "coordinates": {
    "name": "libpng",
    "version": "1.4.9"
  }
}
```

Sample JSON for a CocoaPods purl is provided below:

```
"packageUrl": "pkg:cocoapods/libpng@1.4.9"
```

## Drupal Package URL Example

For Drupal package identifiers, the following coordinates are supported:

- name
- version

Sample JSON for a Drupal component identifier is provided below:

```
"componentIdentifier": {
  "format": "drupal",
  "coordinates": {
    "name": "simplenews",
    "version": "2.0.0"
  }
}
```

Sample JSON for a Drupal purl is provided below:

```
"packageUrl": "pkg:drupal/simplenews@2.0.0"
```

## Pecoff Package URL Example

For Pecoff identifiers, the following coordinates are supported:

- name
- namespace (optional)
- version

Sample JSON for a Pecoff component identifier is provided below:

```
"componentIdentifier": {
  "format": "pecoff",
  "coordinates": {
    "name": "0Harmony.dll",
    "namespace":"BepInEx/HarmonyX"
    "version": "2.0.0.0"
  }
}
```

Sample JSON for a Pecoff purl is provided below:

```
"packageUrl": "pkg:generic/BepInEx/HarmonyX/0Harmony.dll@2.0.0.0?nexustype=pecoff"
```

SINCE RELEASE 101

```
"pkg:generic/0Harmony.dll@2.0.0.0?nexusnamespace=BepInEx%2FHarmonyX&nexustype=pecoff"
```

## Swift Package URL Example

For swift identifiers, the following coordinates are supported:

- name
- version

Sample JSON for a swift component identifier is provided below:

```
"componentIdentifier": {
  "format": "swift",
  "coordinates": {
    "name": "github.com/ReactiveX/RxSwift",
    "version": "5.1.0"
  }
}
```

Sample JSON for a swift purl is provided below:

```
"packageUrl": "pkg:swift/github.com/ReactiveX/RxSwift@5.1.0"
```

## AI/ML Models on Hugging Face

For AI/ML models on Hugging Face, the following coordinates are supported:

- format
- repo_id
- model
- version
- model_format
- extension

Sample JSON for an AI/ML model identifier is provided below:

```
"componentIdentifier": {
  "format": "hf-model",
  "coordinates": {
    "repo_id":"hauson-fan/RagRetriever",
    "model": "pytorch_model"
    "version": "4404c42d94447ab738eda599e4632b42a4c47a80"
    "model_format": "pytorch"
    "extension": "bin"
  }
} 
```

Sample JSON for an AI/Ml model purl is provided below:

```
"packageUrl": "pkg:huggingface/hauson-fan/RagRetriever@4404c42d94447ab738eda599e4632b42a4c47a80?extension=bin&model=pytorch_model&model_format=pytorch"
```

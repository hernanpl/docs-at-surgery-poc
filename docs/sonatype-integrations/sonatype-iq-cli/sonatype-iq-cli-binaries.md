---
layout: default
title: "Sonatype IQ CLI Binaries"
parent: Sonatype IQ CLI
nav_order: 2
---

# Sonatype IQ CLI Binaries

The CLI binary versions are a drop-in replacement for the Java version without the Java runtime environment (JRE) requirements. The parameters are the same as the Java CLI versions with the addition of Secure Sockets Layer (SSL) customizations.

**Note:** The native Mac OSX CLI has been sunset and will receive only critical bug and security fixes until June 10th, 2025. After this date, it will no longer be supported. The native Linux and Windows CLI have been sunset and will receive only critical bug and security fixes until September 14, 2025. After this date, they will no longer be supported. For the latest features and full support, [switch to our cross-platform Java CLI with bundled JDK](#UUID-4e396b62-fd65-1cfc-dd99-2fb0a20e7b36_section-idm234690697763901) .

## Linux

**Download latest version for Linux:**

The Linux CLI can be installed on distributions supporting Deb or RPM packages. Tested on Centos 7.1+, RHEL 7.3+, Debian 8+, Ubuntu 14.04+

## Mac

**Download latest version for Mac:**

This Mac pkg installer places files in the `/usr/local/bin` directory and has been tested on both M1 and Intel chipsets.

Command to run on Linux or Mac OS:

```
./nexus-iq-cli
```

## Windows

**Download latest version for Windows:**

Requires the Visual C++ Runtime. This is included in the zip, or it can be installed and maintained by Windows Update.

Command to run on Windows:

```
nexus-iq-cli.exe
```

## Passing SSL Parameters to the Sonatype CLI

The JAR version of the CLI uses the standard SSL approach found in all Java applications.

For the native binaries, we pass in values through the following parameters:

**Note:** Using the Windows Trust Store for SSL Set `WINDOWS-ROOT` as the trust store type to have the JVM trust certificates from the Windows Truststore. --ssl-trust-store-type WINDOWS-ROOT

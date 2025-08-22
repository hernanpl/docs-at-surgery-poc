---
layout: default
title: "Sonatype IQ CLI With Bundled JDK"
parent: Sonatype IQ CLI
nav_order: 3
---

# Sonatype IQ CLI With Bundled JDK

## Linux

Download the release that matches your system architecture and extract the contents of the tar archive to your preferred directory.

**Download latest version for Linux:**

The executable is located at `bin/nexus-iq-cli` .

To run the CLI on Linux, use the following command:

```
./nexus-iq-cli [options]
```

Optionally, add the executable to your system’s `PATH` for easier access.

### Debian/Ubuntu

### Red Hat/CentOS

## macOS

Download the release that matches your system architecture and install it using the macOS package installer.

**Download latest version for Mac:**

The macOS Package Installer places files in the directory `/usr/local/iq-cli` .

### Homebrew

To install the latest version of IQ CLI using Homebrew, begin by running the one-time command:

```
brew tap sonatype/nexus-iq-cli
```

Once completed, proceed with:

```
brew install --cask nexus-iq-cli

```

If you previously installed [the native binary](#UUID-8dd52aba-2658-be74-4a2f-9fbcb644208b) (which is now being sunset) via Homebrew, you can install the JDK-bundled version by running:

```
brew upgrade nexus-iq-cli
```

### macOS Usage

To run the CLI on macOS, use the following command:

```
nexus-iq-cli [options]
```

## Windows

Download the ZIP archive and extract its contents to a local directory.

**Download latest version for Windows:**

The executable is located at: `bin/nexus-iq-cli.bat`

To run the CLI on Windows, use the following command:

```
./nexus-iq-cli.bat [options]

```

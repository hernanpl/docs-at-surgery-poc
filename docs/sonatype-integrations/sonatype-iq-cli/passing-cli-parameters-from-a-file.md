---
layout: default
title: "Passing CLI parameters from a file"
parent: Sonatype IQ CLI
nav_order: 4
---

# Passing CLI parameters from a file

One or more text files may be used to pass some or all the parameters to the CLI. The `@` prefix is used followed by the name of the file in the command. The file uses the JVM's default character encoding however file matching or globbing is not supported.

- Add parameters and values as separate lines.
- Both short and long parameter names are supported.
- File paths are relative to the current process. Absolute file paths are supported. Include multiple paths as separate lines.

Example command

```
java -jar ./nexus-iq-cli*.jar @cli-params.txt
```

Example cli-params.txt

```
-i 
Test123 
-a 
username:password 
-s
http://localhost:8070 
-t 
build 
./sample-application.zip
```

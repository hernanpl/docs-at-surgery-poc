---
layout: default
title: "Java Runtime Agent (Experimental)"
parent: Sonatype Integrations
nav_order: 23
---

# Java Runtime Agent (Experimental)

The **Java Runtime Agent** detects vulnerable Java methods or classes loaded during runtime to enhance the priority of policy remediation.

Vulnerable components are labeled when the vulnerable classes are loaded and when the vulnerable methods are called during your integration test coverage as part of your build.

Lifecycle policy uses the labels to prioritize the risk found in open-source components by lowering the threat level when not directly referenced by your application during runtime.

Developers better manage their open-source workload with fewer false critical violations and broken builds.

⚠️ **Warning:** This is an experimental feature that will change in the future. We do not know the performance impact of running this tool against the Lifecycle at any scale. We insist that this is not run on production environments until this functionality has been hardened. For assistance or to provide feedback with this experimental feature, contact our [data-insights-pm@sonatype.com](mailto:data-insights-pm@sonatype.com)

## How it works

The Java Runtime Agent detects class loading and calls to vulnerable methods then notifies the Lifecycle server using components labels.

- The agent detects the loading of a vulnerable method and notifies Lifecycle
- The agent also detects and labels when the classes are loaded
- The agent labels all components in the application bill of material with a runtime-enabled label
- Lifecycle policy constraints will make judgments on these labels in combination with other risk data

For applications with thorough test coverage, every method and class from the open-source components are labeled as being loaded and/or called. Vulnerable methods or classes that are not referenced in the application are deprioritized as less risk.

Learn more about [Java Instrumentation and Java Agents](https://www.baeldung.com/java-instrumentation)

## Prerequisites for using Java Runtime Agent

- Run the Java Runtime Agent on a non-production server. The agent injects bytecode to intercept calls to vulnerable methods, with minimal impact.
- The Lifecycle server must be accessible to the system where the Java Runtime Agent is running
- The runtime agent depends on Java 17
- The application ID and user access will need to be in the Lifecycle server
- Component labels and policy constraints should be configured before running the agent
- User tokens and token passwords are recommended

## Steps to use the Java Runtime Agent

- Download the Java Runtime Agent: [runtime-agent-1.0.10.jar](https://github.com/sonatype-nexus-community/iq-api-examples/blob/main/iq-reference-policy/java-runtime-example/runtime-agent-1.0.10.jar)
- Create component labels and update policies with the runtime prioritization The Java Runtime Agent uses component labels to trigger custom policies depending on when methods and classes are loaded from vulnerable components.
- Add the agent at the root of the project to run during your test coverage build The jar must be placed in the classpath of the client’s application and run with the Java agent JVM option. The agent is configured using either JVM system properties or environment variables.
- View the Report Go to the application report in Lifecycle. Components found by the agent have labels indicating if the classes are loaded and if the vulnerable method signatures are loaded and/or called.

## Runtime Java Agent custom policy configuration

The runtime agent uses a custom set of policies to prioritize security vulnerabilities based on the component labels applied to the components during the evaluation. These policies may be loaded using a sample policy set or manually created using the tables below as a reference.

Once you configure the policies and labels, the runtime agent uses them in the following workflow.

- The runtime agent applies the `Runtime-Enabled` label to components. The standard security policies are modified to not trigger when the component has this label. The standard security policies are used when the application is not scanned with the runtime agent.
- The `Runtime-Method-Called` label is added when the vulnerable method is called during runtime. This triggers the security policies that the vulnerability has been `Security-Confirmed` . The vulnerability keeps the designated threat level.
- The `Runtime-Class-Loaded` label is added when the vulnerable class is loaded during runtime. If the `Runtime-Method-Loaded` label is not added, then the `Security-Partial-Confirmed` policies is triggered to identify potential risk. This happens when the vulnerable method is not known at the time.
- When either the class is not loaded or both the class and methods are loaded but the method is not called, then the violation triggers the `Security-Downgrade` policy to indicate that the application is not at risk do to the vulnerability.

### Manually modify your policies

Add the following component labels:

```
Runtime-Enabled, Runtime-Class-Loaded, Runtime-Method-Loaded, Runtime-Method-Called
```

Make the following changes to your Lifecycle security policies. Each severity category will need the 4 policies below.

The first is the original policy that needs to be modified while the other 3 must be created new.

The 4 severity categories follow the [CVSS v3.0 scoring](https://nvd.nist.gov/vuln-metrics/cvss) scale: Critical, High, Medium, Low.

## Runtime Java Agent with Spring’s Pet Clinic

This demo simulates vulnerable method calls to show what the runtime agent can do. This example uses a public folk of the maven project [spring pet clinic](https://github.com/spring-projects/spring-petclinic) to include the agent during integration tests. The steps may be duplicated for other Java projects.

Follow the prerequisites and steps above to prepare your Lifecycle server.

- Clone the demo repository for [spring-petclinic-runtime-agent](https://github.com/navaneeth-mysore-sonatype/spring-petclinic-runtime-agent)
- Copy the runtime agent to the level up of the path of the project or adjust the agent config below
- Update the project `pom.xml` Set the [maven plugin](#UUID-433e090b-af9e-c63f-5963-c61a3a5f9729) configuration in the pom `<properties>` section Add/update the following from [lines 19-22](https://github.com/navaneeth-mysore-sonatype/spring-petclinic-runtime-agent/blob/main/pom.xml#L19) in the pom.xml The maven plugin is added to the plugins section starting at [line 157](https://github.com/navaneeth-mysore-sonatype/spring-petclinic-runtime-agent/blob/main/pom.xml#L157) . This project uses the artifactId `spring-petclinic-runtime-agent` as the applicationId to use in the Lifecycle analysis. This application should be added before running the demo. The runtime agent is added to the configuration at [line 190](https://github.com/navaneeth-mysore-sonatype/spring-petclinic-runtime-agent/blob/main/pom.xml#L190) for the `maven-surefire-plugin` which is used for unit tests in this project. Update the plugin version and Lifecycle server in this section. Credentials should be passed as environment variables. NOTE: the `-Dsonatype.runtime.agent.runtimeEnabledLabel=true` may need to be added to the configuration if not present. This is used to set the `Runtime-Enabled` label on all components.
- Set the [maven plugin](#UUID-433e090b-af9e-c63f-5963-c61a3a5f9729) configuration in the pom `<properties>` section Add/update the following from [lines 19-22](https://github.com/navaneeth-mysore-sonatype/spring-petclinic-runtime-agent/blob/main/pom.xml#L19) in the pom.xml The maven plugin is added to the plugins section starting at [line 157](https://github.com/navaneeth-mysore-sonatype/spring-petclinic-runtime-agent/blob/main/pom.xml#L157) . This project uses the artifactId `spring-petclinic-runtime-agent` as the applicationId to use in the Lifecycle analysis. This application should be added before running the demo.
- The runtime agent is added to the configuration at [line 190](https://github.com/navaneeth-mysore-sonatype/spring-petclinic-runtime-agent/blob/main/pom.xml#L190) for the `maven-surefire-plugin` which is used for unit tests in this project. Update the plugin version and Lifecycle server in this section. Credentials should be passed as environment variables. NOTE: the `-Dsonatype.runtime.agent.runtimeEnabledLabel=true` may need to be added to the configuration if not present. This is used to set the `Runtime-Enabled` label on all components.
- Update your local maven `${HOME}/.m2/settings.xml` with the clm.serverId property.
- Set environment variable for Lifecycle server authentication
- Run the agent with integration tests
- Confirm components have been labeled in the Lifecycle report The following components should have been discovered as part of the test coverage and labeled by the runtime agent.

### Manually running the agent

The runtime agent may be used to label components that are called during testing. Run the following command with the required properties updated. You may wish to remove the component labels before running if the previous demo has been done.

```
java -javaagent:../runtime-agent-1.0.8.jar \
     -Dsonatype.runtime.agent.enabled=true \
     -Dsonatype.runtime.agent.debugMode=false \
     -Dsonatype.runtime.agent.iq.protocol=http \
     -Dsonatype.runtime.agent.iq.host=ec2-107-23-150-171.compute-1.amazonaws.com \
     -Dsonatype.runtime.agent.iq.port=8070 \
     -Dsonatype.runtime.agent.iq.user=${IQ_USER} \
     -Dsonatype.runtime.agent.iq.password=${IQ_PASSWORD} \
     -Dsonatype.runtime.agent.iq.applicationId=spring-petclinic-runtime-agent \
     -Dsonatype.runtime.agent.isIqApplicationIdPublic=true \
     -Dsonatype.runtime.agent.blockedRunOnStartup=true \
     -Dsonatype.runtime.agent.scanClasspath=false \
     -Dsonatype.runtime.agent.fetchVulnerableClassesFromIQ=true \
     -Dsonatype.runtime.agent.vulnerableMethodDetectionEnabled=true \
     -Dsonatype.runtime.agent.runtimeEnabledLabel=true \
     -jar target/*.jar
```

After the app starts, navigate to the following URL. It invokes vulnerable method calls and the runtime agent will set the appropriate labels in Lifecycle.

```
http://localhost:8080/vets.html
```

The runtime agent will log the action to the console.

```
Sonatype Runtime Agent - [TIME]: *** Vulnerable CLASS LOADED 
[className=org/springframework/core/io/buffer/DefaultDataBuffer] by the JVM

Sonatype Runtime Agent - [TIME]: Assigning label 'Runtime-Class-Loaded' to component 
22d73bef97aff8a74a99 in application: a50576c3cd894d20b24dc0d98eea084b
...
Sonatype Runtime Agent - [TIME]: *** Class with vulnerable METHOD LOADED 
[className=org/springframework/core/io/buffer/DefaultDataBuffer, methodName=split, 
methodDescriptor=(I)Lorg/springframework/core/io/buffer/DataBuffer;] by the JVM
...
Sonatype Runtime Agent - [TIME]: Assigning label 'Runtime-Method-Loaded' to component 
22d73bef97aff8a74a99 in application: a50576c3cd894d20b24dc0d98eea084b

Sonatype Runtime Agent - [TIME]: *** Vulnerable METHOD CALLED 
[className=org/springframework/core/io/buffer/DefaultDataBuffer, methodName=split, 
methodDescriptor=(I)Lorg/springframework/core/io/buffer/DataBuffer;]
...
Sonatype Runtime Agent - [TIME]: Assigning label 'Runtime-Method-Called' to component 
22d73bef97aff8a74a99 in application: a50576c3cd894d20b24dc0d98eea084b
```

## Samples for Running the Agent

### Running with minimal system properties

```
java \
 -cp "$CLASSPATH" \
 -javaagent:/sample/lib/runtime-agent.jar \
 -Dsonatype.runtime.agent.iq.protocol=https \
 -Dsonatype.runtime.agent.iq.host=${IQ_HOST} \
 -Dsonatype.runtime.agent.iq.port=${IQ_PORT} \
 -Dsonatype.runtime.agent.iq.user=${IQ_USER_TOKEN} \
 -Dsonatype.runtime.agent.iq.password=${IQ_USER_TOKEN_PASSWORD} \
 -Dsonatype.runtime.agent.iq.applicationId=${IQ_APPLICATION_ID} \
 -Dsonatype.runtime.agent.scanClasspath=false \
 com.sonatype.sample.SampleApplication
```

### Running with all system properties

```
java \
 -cp "$CLASSPATH" \
 -javaagent:/sample/lib/runtime-agent.jar \
 -Dsonatype.runtime.agent.enabled=true \
 -Dsonatype.runtime.agent.debugMode=false \
 -Dsonatype.runtime.agent.iq.protocol=https \
 -Dsonatype.runtime.agent.iq.host=${IQ_HOST} \
 -Dsonatype.runtime.agent.iq.port=${IQ_PORT} \
 -Dsonatype.runtime.agent.iq.user=${IQ_USER_TOKEN} \
 -Dsonatype.runtime.agent.iq.password=${IQ_USER_TOKEN_PASSWORD} \
 -Dsonatype.runtime.agent.iq.applicationId=${IQ_APPLICATION_ID} \
 -Dsonatype.runtime.agent.isIqApplicationIdPublic=true \
 -Dsonatype.runtime.agent.iq.label=Runtime \
 -Dsonatype.runtime.agent.iq.connectionTimeoutSeconds=30 \
 -Dsonatype.runtime.agent.iq.requestTimeoutSeconds=120 \
 -Dsonatype.runtime.agent.blockedRunOnStartup=true \
 -Dsonatype.runtime.agent.scanClasspath=false \
 -Dsonatype.runtime.agent.vulnerableMethodDetectionEnabled=true \
 -Dsonatype.runtime.agent.fetchVulnerableClassesFromIQ=true \
 -Dsonatype.runtime.agent.executor.initialDelaySeconds=500 \
 -Dsonatype.runtime.agent.executor.delaySeconds=500 \
 -Dsonatype.runtime.agent.removeRuntimeLabelsOnStartup=false \
 -Dsonatype.runtime.agent.httpMaxThreads=10 \
 com.sonatype.sample.SampleApplication
```

### Running with all environment variables (in Dockerfile)

```
ENV SONATYPE_RUNTIME_AGENT_ENABLED true
ENV SONATYPE_RUNTIME_AGENT_DEBUG_MODE false
ENV SONATYPE_RUNTIME_AGENT_IQ_PROTOCOL https
ENV SONATYPE_RUNTIME_AGENT_IQ_HOST ${IQ_HOST}
ENV SONATYPE_RUNTIME_AGENT_IQ_PORT ${IQ_PORT}
ENV SONATYPE_RUNTIME_AGENT_IQ_USER ${IQ_USER_TOKEN}
ENV SONATYPE_RUNTIME_AGENT_IQ_PASSWORD ${IQ_USER_TOKEN_PASSWORD}
ENV SONATYPE_RUNTIME_AGENT_IQ_APPLICATION_ID ${IQ_APPLICATION_ID}
ENV SONATYPE_RUNTIME_AGENT_IS_IQ_APPLICATION_ID_PUBLIC true
ENV SONATYPE_RUNTIME_AGENT_IQ_LABEL Runtime
ENV SONATYPE_RUNTIME_AGENT_IQ_CONNECTION_TIMEOUT_SECONDS 30
ENV SONATYPE_RUNTIME_AGENT_IQ_REQUEST_TIMEOUT_SECONDS 120
ENV SONATYPE_RUNTIME_AGENT_BLOCKED_RUN_ON_STARTUP true
ENV SONATYPE_RUNTIME_AGENT_SCAN_CLASSPATH false
ENV SONATYPE_RUNTIME_AGENT_FETCH_VULNERABLE_CLASSES_FROM_IQ true
ENV SONATYPE_RUNTIME_AGENT_EXECUTOR_INITIAL_DELAY_SECONDS 500
ENV SONATYPE_RUNTIME_AGENT_VULNERABLE_METHOD_DETECTION_ENABLED true
ENV SONATYPE_RUNTIME_AGENT_EXECUTOR_DELAY_SECONDS 500
ENV SONATYPE_RUNTIME_AGENT_REMOVE_RUNTIME_LABELS_ON_STARTUP false
ENV SONATYPE_RUNTIME_AGENT_HTTP_MAX_THREADS 10

java \
 $JAVA_OPTS \
 -cp "$CLASSPATH" \
 com.sonatype.sample.SampleApplication
```

### Java Runtime Agent with Tomcat

Either the agent system properties or environment variables must be used. The properties can be set in CATALINA_OPTS in the shell script usually found in the following location:

```
${TOMCAT_HOME}/bin/setenv.sh
```

## Reference JVM system properties

## Reference Environment Variables

## Reference Component Labels

The following Component Labels are used to flag components loaded and called by the runtime agent. See [Component Labels](#UUID-d2a72712-e91d-bd83-a78c-b89fdeab64ae) to add component labels to the Lifecycle instance.

## Reference Policies

The following Policies are used to prioritize the security risk found by the runtime agent.

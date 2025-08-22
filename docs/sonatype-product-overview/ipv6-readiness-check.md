---
layout: default
title: "IPv6 Readiness Check"
parent: Sonatype Product Overview
nav_order: 8
---

# IPv6 Readiness Check

For organizations responding to call to actions to deploy the newer version of the Internet Protocol, IPv6, which is designed to eventually replace the IPv4 protocol, here are a few checks and tasks needed to continue normal operations with Sonatype products.

## Sonatype Product IPv6 Support Status

### Sonatype Nexus Repository
- **IPv6 Support**: Fully supported in Nexus Repository 3.x
- **Configuration**: Standard Java networking properties apply
- **Dual Stack**: Supports both IPv4 and IPv6 simultaneously

### Sonatype IQ Server
- **IPv6 Support**: Fully supported 
- **Configuration**: Standard Java networking properties apply
- **Network Communication**: Compatible with IPv6-enabled environments

## IPv6 Readiness Checklist

### Network Infrastructure
1. **Verify IPv6 connectivity** in your network environment
2. **Test DNS resolution** for both IPv4 and IPv6 addresses
3. **Check firewall rules** to allow IPv6 traffic on required ports
4. **Validate load balancer configuration** for IPv6 support if applicable

### Java Virtual Machine Configuration
1. **Java IPv6 System Properties**:
   - `-Djava.net.preferIPv6Addresses=true` - Prefer IPv6 addresses
   - `-Djava.net.preferIPv4Stack=false` - Allow IPv6 stack usage
   - `-Djava.net.preferIPv6Stack=true` - Prefer IPv6 stack (if needed)

2. **Sonatype-specific Configuration**:
   - Update `nexus.properties` or IQ Server configuration files as needed
   - Ensure database connection strings support IPv6 format if using external databases

### Testing and Validation
1. **Connection Testing**:
   - Test connectivity to external registries (Maven Central, npm, etc.) over IPv6
   - Verify internal network communication between Sonatype products
   - Test client connectivity from development environments

2. **Monitoring**:
   - Monitor network traffic patterns after IPv6 deployment
   - Watch for any connectivity issues or performance changes
   - Review logs for IPv6-related warnings or errors

## Common Configuration Examples

### IPv6 Address Format
- **Nexus Repository**: Use brackets for IPv6 addresses in URLs: `http://[2001:db8::1]:8081`
- **Database Connections**: Format varies by database vendor
- **Proxy Configuration**: Ensure proxy servers support IPv6 if configured

### Troubleshooting
If you experience issues after IPv6 deployment:
1. Check Java networking system properties
2. Verify DNS resolution for both IPv4 and IPv6
3. Review network connectivity and firewall configurations
4. Contact Sonatype Support for product-specific guidance

## Additional Resources
- Java IPv6 networking documentation
- Your organization's network team for infrastructure-specific guidance
- [Sonatype Support](https://support.sonatype.com) for product-specific questions

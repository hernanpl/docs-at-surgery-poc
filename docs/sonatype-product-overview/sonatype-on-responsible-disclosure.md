---
layout: default
title: "Sonatype on Responsible Disclosure"
parent: Sonatype Product Overview
nav_order: 4
---

# Sonatype on Responsible Disclosure

Sonatype prides itself on its unwavering commitment to data quality and integrity, ensuring the highest standards are consistently met. Part of our commitment to the safety of OSS usage is ensuring we responsibly disclose zero-day vulnerabilities. The process an organization follows on vulnerability disclosure is the difference between chaos and a clean fix. We follow industry standards of responsible disclosure as listed by [OWASP](https://cheatsheetseries.owasp.org/cheatsheets/Vulnerability_Disclosure_Cheat_Sheet.html) . This document provides an overview of Sonatype’s responsible disclosure process.

## Responsible Disclosure Process

Sonatype follows a structured approach to responsible vulnerability disclosure:

### 1. Discovery and Initial Assessment
- Security vulnerabilities are identified through internal testing, external security research, or community reports
- Each vulnerability is assessed for impact, severity, and exploitability
- Initial triage determines if the vulnerability meets criteria for responsible disclosure

### 2. Vendor Notification and Coordination
- Sonatype contacts affected project maintainers or vendors within 24-48 hours of confirmation
- We provide detailed technical information about the vulnerability
- We work collaboratively with vendors to develop patches and remediation strategies

### 3. 90-Day Disclosure Timeline
- Sonatype follows a standard 90-day disclosure window from initial vendor contact
- This timeframe allows sufficient time for vendors to develop, test, and release patches
- Extensions may be granted if vendors demonstrate active progress on remediation

### 4. Public Disclosure
- After patches are available or the 90-day window expires, vulnerability details are publicly disclosed
- Disclosure includes CVE assignments, CVSS scores, and remediation guidance
- Information is shared through Sonatype's vulnerability database and security advisories

### 5. Ongoing Support
- Sonatype continues to monitor for additional instances of the vulnerability
- We provide ongoing guidance to help organizations identify and remediate affected components

## Questions You May Have

### Why does Sonatype follow the principles of responsible (aka coordinated) disclosure and not partial or full disclosure?

Sonatype does not use private disclosure because in cases where the vendor is unresponsive or chooses not to address the vulnerability, the specific details might never be disclosed to the public.

Adopting the full disclosure approach involves promptly revealing comprehensive information about a vulnerability as soon as it's detected. This approach goes against Sonatype's goals to unite software developers, application security professionals, operators, engineering leaders, and legal teams to manage their open source components safely so that they can focus on innovation. This approach implies that all intricate details, which might even encompass exploit code, become accessible to potential attackers, sometimes preceding the availability of a patch. Full disclosure is predominantly employed when organizations disregard reported vulnerabilities, intending to compel them to create and release a solution.
### Why does Sonatype have a 90-day disclosure policy?

Responsible disclosure strikes a balance between partial and full disclosure in order to be able to keep software-producing organizations — and the world — safe. Sonatype makes every reasonable effort to contact project owners and will work with them to ensure a patch is released.
### Why does responsible disclosure matter?

Responsible disclosure promotes security and stability of software systems. When security researchers discover vulnerabilities, responsibly disclosing these vulnerabilities to the affected parties allows them to address and patch the issues before malicious actors can exploit them. This process helps prevent potential cyberattacks, data breaches, and disruptions, ultimately safeguarding users' sensitive information, privacy, and the overall functionality of digital systems.
### Do I need to alert project owners of vulnerabilities identified by Sonatype?

No. This document, describing our disclosure policy and process, including alerting project owners, means you do not need to.

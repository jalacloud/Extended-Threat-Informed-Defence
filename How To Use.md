![ASS3T-v2-5 (v2)](https://github.com/user-attachments/assets/17f18e4e-fde9-4ea3-abca-13064a941434)

# Use threat intelligence *intelligently*

### Observe
  * Use internal and external security logging and monitoring and alerts to identify cyber threats in real-time and near-real-time (NRT).
  * Subscribe to threat-intelligence feeds for accurate and timely information on real-world threat actor behaviour and techniques.
    - [ ] [Open Threat eXchange (OTX) AlienVault](https://otx.alienvault.com/)
    - [ ] [SANS Internet Storm Centre](https://isc.sans.edu/)
    - [ ] [Proofpoint Emerging Threats](https://rules.emergingthreats.net/)
   * Read and analyse threat reports for up-to-date insights on the current cyber threat landscape and emerging threat trends across various industry sectors.
   * Analyse and research active threats within your specific industry.
     - [ ] What/who are the most active within your sector?
     - [ ] What top or most common **Initial Access** vectors are used to attack their targets?

### Identify

  * Enable cloud native logging/monitoring functions in AWS, Azure, and GCP.
    - [ ] **AWS:** Enable AWS [CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) to receive logs for IAM-related activity
    - [ ] **AWS:** Enable CloudWatch to receive logs for [AD sync and configurable AD sync errors](https://docs.aws.amazon.com/singlesignon/latest/userguide/logging-ad-sync-errors.html)
    - [ ] **AWS:** Enable AWS [VPC flow logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) to gain visibility into [network-level activity](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Network-Monitoring-Sections.html) within your AWS environment(s)
    - [ ] **Azure:** Collect [sign-in logs](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-sign-ins) from Microsoft Azure Entra ID
    - [ ] **Azure:** Monitor provisioning logs in Entra ID to detect new user accounts with high privileges (contributor, security administrator, global administrator, etc.)
  * Regularly perform (lite) threat modelling to proactively identify vulnerable attack vectors in your applications, networks, and systems.
    - [ ] What can go wrong?
    - [ ] How would this impact the business?
      - [ ] Financial
      - [ ] Reputational
      - [ ] Operational
    - [ ] How can we prevent/prepare/respond if something goes wrong?
    - [ ] Who would likely cause something to go wrong?
    - [ ] Did we miss anything important? Did we do a good job? (QA)
          
  * Experiment with open-source tooling to build and test real-world threat scenarios based on **observed** threat intel.
    - [ ] Discover/Identify valid attack surfaces exposed across your technology landscape using [AMASS](https://github.com/owasp-amass/amass) from the OWASP team
    - [ ] Research and identify valid attack patterns using [MITRE CAPEC] that can be applied to your technology stack 
    - [ ] Use the [Technique Inference Engine](https://mitre-engenuity.org/cybersecurity/center-for-threat-informed-defense/our-work/technique-inference-engine/) by MITRE CTID
    - [ ] Use the MITRE [Top ATT&CK Techniques Calculator](https://top-attack-techniques.mitre-engenuity.org/#/calculator)
    - [ ] Perform attack simulations mapped to the MITRE ATT&CK framework using Red Canary's [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team)
   
### Protect

  * Plan, develop, and implement a robust defence strategy using the detailed information gathered from the above activities.
  * Use [ASS3T](https://jasonlayton.com/resources/advanced-security-selection-evaluation-tool-ass3t-version-25) to help identify protective controls that are mapped to the MITRE ATT&CK framework.
  * Use industry frameworks like [NIST CSF v2.0](https://csf.tools/framework/csf-v2-0/), [CIS Critical Security Controls (CSC)](https://www.cisecurity.org/controls) and the [Cloud Security Alliance (CSA) Cloud Controls Matrix](https://cloudsecurityalliance.org/research/cloud-controls-matrix) to help inform decision-making.
  * Leverage solution design guidance and secure best practices from major cloud service providers (CSPs).
    - [ ] [Microsoft Azure Well-Architected Framework (WAF)](https://learn.microsoft.com/en-us/azure/well-architected/)
    - [ ] [Microsoft Azure Top 10 Security Best Practices](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/secure/security-top-10)
    - [ ] [Amazon AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html)
    - [ ] [Google Cloud Well-Architected Framework](https://cloud.google.com/architecture/framework)
 
## When To Use
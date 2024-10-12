# eXtended Threat-informed Defence (XTID)

![E2E Threat-informed Defence - watermarked](https://github.com/user-attachments/assets/b1e9e38b-446a-4d2f-ae0c-896813e7f9fc)

## Use threat intelligence *intelligently*

### Observe
  * Use internal and external security logging and monitoring and alerts to identify cyber threats in real-time and near-real-time (NRT).
  * Subscribe to threat-intelligence feeds for accurate and timely information on real-world threat actor behaviour and techniques.
    - [ ] [Open Threat eXchange (OTX) AlienVault](https://otx.alienvault.com/)
    - [ ] [SANS Internet Storm Centre](https://isc.sans.edu/)
    - [ ] [Proofpoint Emerging Threats](https://rules.emergingthreats.net/)
   * Deploy in-house threat intelligence tools/platforms to tailor threat intel observations to your organisation/threat cases.
     - [ ] [OpenCTI](https://github.com/OpenCTI-Platform/opencti?tab=readme-ov-file)
     - [ ] [MISP Open Source Threat-intel Sharing Platform](https://www.misp-project.org/)
   * Read and analyse threat reports for up-to-date insights on the current cyber threat landscape and emerging threat trends across various industry sectors.
     - [ ] [Verizon Data Breach Investigation Report](https://www.verizon.com/business/en-au/resources/reports/dbir/)
   * Analyse and research active threats within your specific industry.
     - [ ] What/who are the most active within your sector?
     - [ ] What top or most common *Initial Access* vectors are used to attack their targets?
     - [ ] What are the most common or trending *persistence* techniques used by threat actors?
     - [ ] What are the most common or trending *credential access* and *lateral movement* techniques used by threat actors?

### Identify

  * Identify and assess your *defensive surface*, based on your **Data**, **Applications**, **Assets**, and **Services**. Commonly referenced by the acronym DAAS.
  * Enable cloud native logging/monitoring functions in AWS, Azure, and GCP.
    - [ ] **AWS:** Enable AWS [CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) to receive logs for IAM-related activity
    - [ ] **AWS:** Enable CloudWatch to receive logs for [AD sync and configurable AD sync errors](https://docs.aws.amazon.com/singlesignon/latest/userguide/logging-ad-sync-errors.html)
    - [ ] **AWS:** Enable AWS [VPC flow logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) to gain visibility into [network-level activity](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Network-Monitoring-Sections.html) within your AWS environment(s)
    - [ ] **Azure:** Collect [sign-in logs](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-sign-ins) from Microsoft Azure Entra ID
    - [ ] **Azure:** Monitor provisioning logs in Entra ID to detect new user accounts with high privileges (contributor, security administrator, global administrator, etc.)
    - [ ] **Azure:** [PLACEHOLDER FOR ADDITIONAL LOGGING/MONITORING CONTROLS]
    - [ ] **GCP:** Leverage the comprehensive list of Google [Community Security Analytics (CSA)](https://github.com/GoogleCloudPlatform/security-analytics) to gain immediate insights across cloud identity, network, data, and environment-level analytics and flow logs
   
  * Perform threat hunting in alignment with well-known frameworks (e.g. PEAK, TaHiTI)
  * Proactively hunt for threats within your cloud and on-premises environments (threat hunting)
    - [ ] Build and run custom detection KQL queries in Microsoft Sentinel to actively identify and detect anomalous/suspicious and potentially malicious TA behaviour
    - [ ] Check out [The Threat Hunter Playbook](https://threathunterplaybook.com/intro.html), a community-driven open-source project to share detection logic, adversary tradecraft and resources to make detection development more efficient. 
  * Regularly perform (lite) threat modelling to proactively identify vulnerable attack vectors in your applications, networks, and systems.
    - [ ] What can go wrong?
    - [ ] How would this impact the business?
      - [ ] Financial
      - [ ] Reputational
      - [ ] Operational
    - [ ] How can we prevent/prepare/respond if something goes wrong?
    - [ ] Who would likely cause something to go wrong?
    - [ ] Did we miss anything important? Did we do a good job? (QA)
  * Identify and review the knowledge base of analytics developed by [MITRE](https://www.mitre.org/) based on the MITRE ATT&CK adversary model.
    - [ ]  Review MITRE's [Cyber Analytics Repository (CAR)](https://car.mitre.org/) for low-level analytics and technical procedures that are mapped against MITRE ATT&CK techniques
          
  * Experiment with open-source tooling to build and test real-world threat scenarios based on **observed** threat intel.
    - [ ] Discover/Identify valid attack surfaces exposed across your technology landscape using [AMASS](https://github.com/owasp-amass/amass) from the OWASP team
    - [ ] Research and identify valid attack patterns using [MITRE CAPEC] that apply to your technology stack 
    - [ ] Use the [Technique Inference Engine](https://mitre-engenuity.org/cybersecurity/center-for-threat-informed-defense/our-work/technique-inference-engine/) by MITRE CTID
    - [ ] Use the MITRE [Top ATT&CK Techniques Calculator](https://top-attack-techniques.mitre-engenuity.org/#/calculator)
    - [ ] Perform attack simulations mapped to the MITRE ATT&CK framework using Red Canary's [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team)
   
### Protect

  * Use the detailed information from the above activities to plan, design, and implement a robust defence strategy.
  * Define and implement [design principles](https://github.com/jalacloud/cybersecurity/blob/main/reference_architecture_development/security%20principals.md) for your organisation's information security program to consistently plan, design, deliver, and manage secure technology solutions.
  * Use [ASS3T](https://jasonlayton.com/resources/advanced-security-selection-evaluation-tool-ass3t-version-25) to help identify effective MITRE and NIST controls mapped to the MITRE ATT&CK framework.
  * Use industry frameworks like [NIST CSF v2.0](https://csf.tools/framework/csf-v2-0/), [CIS Critical Security Controls (CSC)](https://www.cisecurity.org/controls) and the [Cloud Security Alliance (CSA) Cloud Controls Matrix](https://cloudsecurityalliance.org/research/cloud-controls-matrix) to help inform decision-making.
  * Leverage solution design guidance and secure best practices from major cloud service providers (CSPs).
    - [ ] [Microsoft Azure Well-Architected Framework (WAF)](https://learn.microsoft.com/en-us/azure/well-architected/)
    - [ ] [Microsoft Azure Top 10 Security Best Practices](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/secure/security-top-10)
    - [ ] [Amazon AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html)
    - [ ] [Google Cloud Well-Architected Framework](https://cloud.google.com/architecture/framework)
   * Develop [outcome-driven metrics (ODMs)](https://github.com/jalacloud/cybersecurity/blob/main/Outcome-driven%20Metrics/2024-09-odm-checklist.md) to validate and verify the effectiveness of current security controls. 


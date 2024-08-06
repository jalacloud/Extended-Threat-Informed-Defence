![cloud-attack-filter](https://github.com/user-attachments/assets/2ca4f210-5310-4a36-b44a-6fb75769c156)

## Cloud Attack Filter - How To Use

- Download or clone this repo
- Using your favourite command shell of choice, navigate to the attack-filter folder where the script(s) and sub-folders are stored
- Each CSP sub-folder contains the MITRE ATT&CK mapping file that is used by the CloudAttackFilter script
- Call the "CloudAttackFilter.py" script and use the "-i" argument to specify the cloud mapping input file to use for generating the output
- Run the following commands (shown below) to generate list of cloud control mechanisms for specific MITRE ATT&CK techniques
- The results are ranked by their "Score Value" in terms of how effective the control is against the each ATT&CK technique
- Use the -n argument to specify the number of results to generate e.g. "-n 10" for the top 10 techniques or controls
- You can also generate a scored list of mitigated ATT&CK techniques based on specific cloud controls e.g. "azure_firewall" or "aws_security_hub"...etc.
- The script works for ALL cloud service providers (Azure, AWS, and GCP) - The mapping file is located in each vendors folder

### Scoring System

Scoring is the same as originally defined by MITRE CTID. You can find more information about this [here](https://center-for-threat-informed-defense.github.io/mappings-explorer/about/scoring/).

- **Minimal**: The control provides minimum mitigation of the ATT&CK (sub-)technique.
- **Partial**: The control provides partial mitigation of the ATT&CK (sub-)technique.
- **Significant**: The control provides significant mitigation of the ATT&CK (sub-)technique.

### Supported Commands
```
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input JSON file
  -cg CAPABILITY_GROUP, --capability_group CAPABILITY_GROUP
                        Capability Group to filter
  -t TECHNIQUE, --technique TECHNIQUE
                        Attack Technique ID to filter
  -n NUMBER, --number NUMBER
                        Number of top techniques to retrieve
  --list-groups         List all available capability groups
  --list-attacks        List all available attack techniques
```

### EXAMPLES

#### Identify Azure cloud controls for MITRE ATT&CK technique T1606.008 (SAML Token Abuse) //
```
attack-filter>python CloudAttackFilter.py -i "msft-azure\azure-06.29.2021_attack-8.2-enterprise_json.json" -t T1606.002
Rank Capability Group                                            Score Category           Score Value    Attack Object ID    Attack Object Name
1    azure_ad_identity_protection                                respond                  significant    T1606.002           SAML Tokens
2    azure_ad_identity_protection                                detect                   partial        T1606.002           SAML Tokens
3    azure_ad_identity_secure_score                              detect                   partial        T1606.002           SAML Tokens
```
#### Identify Azure cloud controls for MITRE ATT&CK technique T1550.002 (Pass the Hash) //
```
attack-filter>python CloudAttackFilter.py -i "msft-azure\azure-06.29.2021_attack-8.2-enterprise_json.json" -t T1550.002
Rank Capability Group                                            Score Category           Score Value    Attack Object ID    Attack Object Name
1    microsoft_defender_for_identity                             detect                   partial        T1550.002           Pass the Hash
2    azure_ad_identity_secure_score                              protect                  partial        T1550.002           Pass the Hash
3    azure_sentinel                                              detect                   minimal        T1550.002           Pass the Hash
```
#### Identify MITRE ATT&CK techniques by Azure controls (Microsoft Sentinel) //
```
attack-filter>python CloudAttackFilter.py -i "msft-azure\azure-06.29.2021_attack-8.2-enterprise_json.json" -cg azure_sentinel
-cg azure_sentinel
Rank Capability Group                                            Score Category           Score Value    Attack Object ID    Attack Object Name
1    azure_sentinel                                              detect                   partial        T1078               Valid Accounts
2    azure_sentinel                                              detect                   partial        T1078.002           Domain Accounts
3    azure_sentinel                                              detect                   partial        T1078.003           Local Accounts
4    azure_sentinel                                              detect                   partial        T1078.004           Cloud Accounts
5    azure_sentinel                                              detect                   partial        T1195.001           Compromise Software Dependencies and Development Tools
6    azure_sentinel                                              detect                   partial        T1110               Brute Force
7    azure_sentinel                                              detect                   partial        T1110.001           Password Guessing
8    azure_sentinel                                              detect                   partial        T1110.003           Password Spraying
9    azure_sentinel                                              detect                   partial        T1110.004           Credential Stuffing
10   azure_sentinel                                              detect                   partial        T1071.004           DNS
```

#### Identify MITRE ATT&CK techniques by AWS controls (AWS WAF)
```
attack-filter>python CloudAttackFilter.py -i "amzn-aws\aws-09.21.2021_attack-9.0-enterprise_json.json" -cg aws_web_application_firewall
Rank Capability Group                                            Score Category           Score Value    Attack Object ID    Attack Object Name
1    aws_web_application_firewall                                protect                  significant    T1190               Exploit Public-Facing Application
2    aws_web_application_firewall                                protect                  significant    T1189               Drive-by Compromise
3    aws_web_application_firewall                                protect                  significant    T1203               Exploitation for Client Execution
4    aws_web_application_firewall                                protect                  significant    T1059.001           PowerShell
5    aws_web_application_firewall                                protect                  significant    T1059.004           Unix Shell
6    aws_web_application_firewall                                protect                  significant    T1059.007           JavaScript
7    aws_web_application_firewall                                protect                  partial        T1059               Command and Scripting Interpreter
8    aws_web_application_firewall                                protect                  partial        T1090               Proxy
9    aws_web_application_firewall                                protect                  partial        T1090.002           External Proxy
10   aws_web_application_firewall                                protect                  partial        T1090.003           Multi-hop Proxy
```

#### List all capability groups for Amazon AWS //
```
attack-filter>python CloudAttackFilter.py -i "amzn-aws\aws-09.21.2021_attack-9.0-enterprise_json.json" --list-groups
Available Capability Groups:
1. amazon_cognito
2. amazon_detective
3. amazon_guardduty
4. amazon_inspector
5. amazon_virtual_private_cloud
6. aws_artifact
7. aws_audit_manager
8. aws_certificate_manager
9. aws_cloudendure_disaster_recovery
10. aws_cloudhsm
11. aws_cloudtrail
12. aws_cloudwatch
13. aws_config
14. aws_directory_service
15. aws_firewall_manager
16. aws_identity_and_access_management
17. aws_iot_device_defender
18. aws_key_management_service
19. aws_network_firewall
20. aws_organizations
21. aws_rds
22. aws_resource_access_manager
23. aws_s3
24. aws_secrets_manager
25. aws_security_hub
26. aws_shield
27. aws_single_sign-on
28. aws_web_application_firewall
```
To see all supported ATT&CK techniques for each cloud provider, call the vendor mapping file (.JSON) and use the --list-attacks argument 


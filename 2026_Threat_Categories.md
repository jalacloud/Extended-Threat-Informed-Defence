
## Cyber Threat Taxonomy // 2026 Threat Landscape


[Phishing & Social Engineering]: Deceptive communications (email, SMS, voice, social media) used to manipulate users into disclosing credentials, approving MFA prompts, transferring funds, or executing malware. Includes spear phishing, smishing, vishing, and AI-generated impersonation.

[Business Email Compromise (BEC)]: Targeted impersonation of executives, vendors, or partners to induce fraudulent payments or sensitive data disclosure. Often involves mailbox takeover and persistence within M365/Google Workspace.

[Credential Theft & Identity Attacks]: Theft, harvesting, cracking, or replay of authentication material (passwords, tokens, cookies, API keys). Includes MFA fatigue attacks, session hijacking, OAuth abuse, and pass-the-cookie/token replay.

[Ransomware]: Malware used to encrypt systems and/or exfiltrate data for extortion. Modern variants employ double or triple extortion (encryption + leak site + DDoS). Often delivered via initial access brokers (IABs).

[Data Extortion (Unencrypted)]: Theft of sensitive data without encryption, followed by extortion threats to publish or sell the data. Increasingly common due to faster execution and lower operational overhead than ransomware.

[Supply Chain Compromise]: Compromise of software vendors, SaaS providers, MSPs, CI/CD pipelines, or open-source dependencies to gain indirect access to downstream victims. Includes malicious code injection and trusted update abuse.

[Cloud Environment Intrusion]: Exploitation of misconfigurations, exposed APIs, over-privileged IAM roles, or stolen cloud tokens to access IaaS/PaaS/SaaS environments. Often involves living-off-the-land abuse of native cloud services.

[API Abuse & Exploitation]: Targeting insecure or poorly authenticated APIs to extract data, bypass controls, perform business logic abuse, or escalate privileges. Increasingly relevant in SaaS and fintech environments.

[Zero-Day Exploitation]: Use of previously unknown vulnerabilities to achieve initial access or privilege escalation. Often weaponised rapidly against internet-facing appliances (VPNs, firewalls, hypervisors).

[N-Day Vulnerability Exploitation]: Exploitation of known but unpatched vulnerabilities. Frequently automated at scale against exposed services.

[Initial Access Broker Activity]: Specialised actors who gain footholds (via phishing, exploits, RDP brute force) and sell access to ransomware or espionage groups. Key enabler in modern criminal ecosystems.

[Living-off-the-Land (LOTL) Techniques]: Abuse of legitimate system tools (PowerShell, WMI, Azure CLI, AWS CLI, PsExec) to evade detection and blend with normal operations. Common in post-compromise phases.

[Advanced Persistent Threat (APT) Operations]: Long-term, covert campaigns typically linked to nation-states, focused on espionage, intellectual property theft, or strategic disruption. Characterised by stealth and persistence.

[Cyber Espionage]: Targeted theft of sensitive government, defence, commercial, or research data for strategic advantage. May leverage zero-days and supply chain compromise.

[Distributed Denial of Service (DDoS)]: Flooding services with traffic to degrade or disrupt availability. Includes volumetric, application-layer, and extortion-based DDoS. Often combined with other attacks.

[Insider Threat]: Malicious or negligent actions by employees, contractors, or partners that result in data theft, sabotage, or exposure. Includes privilege abuse and data exfiltration.

[Malware (Generalised)]: Software designed to disrupt, damage, or gain unauthorised access. Includes trojans, loaders, RATs, spyware, info-stealers, and botnet agents.

[Info-Stealer Campaigns]: Commodity malware designed specifically to harvest credentials, browser cookies, crypto wallets, and session tokens for resale on dark markets. Major enabler of downstream compromise.

[Cryptojacking]: Unauthorised use of computing resources (often cloud workloads or containers) to mine cryptocurrency.

[Operational Technology (OT) / ICS Attacks]: Targeting industrial control systems, critical infrastructure, or manufacturing environments. May involve IT-to-OT pivoting.

[IoT Exploitation]: Compromise of insecure Internet of Things devices for botnets, surveillance, or lateral movement.

[Deepfake & AI-Enabled Fraud]: Use of AI-generated voice/video impersonation for financial fraud, executive impersonation, or social engineering escalation.

[Financial System Manipulation]: Attacks targeting payment platforms, trading systems, SWIFT infrastructure, or digital assets. Includes crypto exchange compromise.

[Web Application Attacks]: Exploitation of application vulnerabilities such as SQL injection, XSS, SSRF, RCE, and authentication bypass.

[Business Logic Abuse]: Manipulation of legitimate workflows (refund abuse, API chaining, privilege escalation via logic flaws) without necessarily exploiting technical vulnerabilities.

[Destructive Attacks (Wipers)]: Malware designed to permanently destroy data or render systems inoperable, often geopolitically motivated.

[Hybrid Influence Operations]: Combined cyber intrusion and information warfare campaigns designed to influence public opinion, elections, or market behaviour.

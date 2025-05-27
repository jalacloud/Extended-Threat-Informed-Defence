# Top 5 MITRE ATT&CK Techniques

### Overview
These queries are optimised for efficiency and low false positives while maintaining strong detection capabilities.
Link to the top 20 most prevalent techniques used among adversaries can be found here: [Top 20 Overlapping Techniques](https://github.com/jalacloud/Extended-Threat-Informed-Defence/blob/main/threatintel/top_20_techniques_2025-04.json)

## 1. T1204.002 - User Execution: Malicious File (Count: 83)
Focus: Detect users executing suspicious files from risky locations

```kql
// T1204.002 - User Execution: Malicious File
DeviceProcessEvents
| where Timestamp > ago(30d)
| where InitiatingProcessFileName in~ ("explorer.exe", "chrome.exe", "firefox.exe", "msedge.exe", "outlook.exe")
| where FolderPath has_any ("\\Downloads\\", "\\Temp\\", "\\AppData\\", "\\Users\\Public\\")
| where FileName endswith ".exe" or FileName endswith ".scr" or FileName endswith ".bat" 
    or FileName endswith ".cmd" or FileName endswith ".vbs" or FileName endswith ".js"
| where not(FolderPath has "Program Files")
| summarize 
    ExecutionCount = count(),
    FirstSeen = min(Timestamp),
    LastSeen = max(Timestamp)
    by DeviceName, AccountName, FileName, FolderPath
| where ExecutionCount >= 1
| extend RiskScore = case(
    FolderPath has_any ("\\Temp\\", "\\AppData\\"), 3,
    FileName has_any (".scr", ".vbs", ".js"), 2,
    1)
| where RiskScore >= 2
| order by RiskScore desc, ExecutionCount desc
```

## 2. T1105 - Ingress Tool Transfer (Count: 83)
Focus: Detect file downloads and network transfers of tools

```kql
// T1105 - Ingress Tool Transfer
DeviceProcessEvents
| where Timestamp > ago(30d)
| where ProcessCommandLine has_any ("http://", "https://", "ftp://")
| where ProcessCommandLine has_any ("download", "curl", "wget", "certutil", "bitsadmin", "Invoke-WebRequest")
    or FileName in~ ("curl.exe", "wget.exe", "certutil.exe", "bitsadmin.exe")
| where not(ProcessCommandLine has_any ("microsoft.com", "windowsupdate.com", "office.com"))
| summarize 
    TransferCount = count(),
    FirstSeen = min(Timestamp),
    LastSeen = max(Timestamp),
    Commands = make_set(ProcessCommandLine, 3)
    by DeviceName, AccountName, FileName
| extend RiskScore = case(
    FileName in~ ("certutil.exe", "bitsadmin.exe"), 3,
    TransferCount >= 3, 2,
    1)
| where RiskScore >= 2
| order by RiskScore desc, TransferCount desc
```

## 3. T1059.001 - Command and Scripting Interpreter: PowerShell (Count: 79)
Focus: Detect malicious PowerShell execution patterns

```kql
// T1059.001 - PowerShell Malicious Usage  
DeviceProcessEvents
| where Timestamp > ago(30d)
| where FileName =~ "powershell.exe"
| where ProcessCommandLine has_any (
    "EncodedCommand", "DownloadString", "DownloadFile", "IEX", "Invoke-Expression",
    "bypass", "hidden", "noprofile", "WebClient", "Base64", "-e ", "-enc"
)
| where not(InitiatingProcessFileName in~ ("explorer.exe", "cmd.exe"))  // Reduce admin FPs
| summarize 
    ExecutionCount = count(),
    FirstSeen = min(Timestamp),
    LastSeen = max(Timestamp),
    SampleCommand = any(ProcessCommandLine)
    by DeviceName, AccountName, InitiatingProcessFileName
| extend RiskScore = case(
    SampleCommand has_any ("EncodedCommand", "DownloadString", "-enc"), 3,
    SampleCommand has_any ("bypass", "hidden"), 2,
    1)
| where RiskScore >= 2
| order by RiskScore desc, ExecutionCount desc
```

## 4. T1566.001 - Phishing: Spearphishing Attachment (Count: 77)
Focus: Detect suspicious email attachments and execution

```kql
// T1566.001 - Spearphishing Attachment
EmailAttachmentInfo
| where Timestamp > ago(30d)
| where FileType in~ (".exe", ".zip", ".rar", ".bat", ".cmd", ".scr", ".vbs", ".js")
| join kind=inner (
    EmailEvents
    | where Timestamp > ago(30d)
    | where DeliveryAction !in ("Blocked", "Quarantined")
    | where SenderFromDomain !endswith "yourdomain.com"  // Replace with your domain
    | project NetworkMessageId, RecipientEmailAddress, SenderFromAddress, SenderFromDomain, Subject, Timestamp
) on NetworkMessageId
| join kind=leftouter (
    DeviceProcessEvents
    | where Timestamp > ago(30d)
    | where InitiatingProcessFileName in~ ("outlook.exe", "chrome.exe", "firefox.exe", "msedge.exe")
    | project ProcessTimestamp = Timestamp, DeviceName, AccountName, ExecutedFile = FileName, ProcessCommandLine
) on $left.RecipientEmailAddress == $right.AccountName
| where isempty(ProcessTimestamp) or abs(datetime_diff('hour', Timestamp, ProcessTimestamp)) <= 2  // Within 2 hours or no execution
| summarize 
    EmailCount = count(),
    Recipients = dcount(RecipientEmailAddress),
    Executions = countif(isnotempty(ExecutedFile)),
    FirstSeen = min(Timestamp),
    LastSeen = max(Timestamp)
    by SenderFromAddress, FileName, FileType
| extend RiskScore = case(
    FileType in~ (".exe", ".scr", ".bat"), 3,
    Executions >= 1, 3,
    EmailCount >= 3, 2,
    1)
| where RiskScore >= 2
| order by RiskScore desc, Executions desc
```

## 5. T1588.002 - Obtain Capabilities: Tool (Count: 75)
Focus: Detect acquisition of hacking tools and utilities

```kql
// T1588.002 - Tool Acquisition
let hackerTools = dynamic([
    "mimikatz", "bloodhound", "sharphound", "rubeus", "seatbelt", "winpeas", 
    "empire", "metasploit", "cobalt", "psexec", "procdump", "lazagne"
]);
DeviceNetworkEvents
| where Timestamp > ago(30d)
| where ActionType == "ConnectionSuccess"
| where RemoteUrl has_any ("github.com", "raw.githubusercontent.com", "pastebin.com")
| where RemoteUrl has_any (hackerTools)
| union (
    DeviceProcessEvents
    | where Timestamp > ago(30d)
    | where FileName has_any (hackerTools) or ProcessCommandLine has_any (hackerTools)
)
| union (
    DeviceFileEvents
    | where Timestamp > ago(30d)
    | where ActionType == "FileCreated"
    | where FileName has_any (hackerTools) or FolderPath has_any (hackerTools)
)
| summarize 
    ActivityCount = count(),
    ActivityTypes = make_set(ActionType),
    FirstSeen = min(Timestamp),
    LastSeen = max(Timestamp),
    Tools = make_set(coalesce(FileName, extract(@"/([^/]+)$", 1, RemoteUrl)))
    by DeviceName, AccountName
| extend RiskScore = case(
    Tools has_any ("mimikatz", "bloodhound", "cobalt"), 3,
    ActivityCount >= 3, 2,
    1)
| where RiskScore >= 2
| order by RiskScore desc, ActivityCount desc
```

Completed the hands-on cybersecurity job simulation in 07/07/2025 that was offered by Telstra. 
Covered topics --->
 1. Responding	to	a	malware	attack
 2. Analysing	the	attack
 3. (Technical)	Mitigate	the	malware	attack
 4. Incident	Postmortem

1. Responding to a Malware Attack:
The malware (Spring4Shell) activity was detected during the simulation, I collected and analyzed the server logs to triage the incident. Based on the severity and indicators of compromise, I escalated the issue to the appropriate infrastructure team, providing them with all relevant details gathered from the logs to support a swift response.

2. Analyzing the Attack:
I took time to research the nature of the incident, diving into similar known exploits and identifying vulnerable endpoints within the system. Through this investigation, I pinpointed the specific HTTP headers being targeted and gained a clearer understanding of how the attacker was attempting to exploit them.

3. Mitigating the Malware Threat (Technical Response):
To help contain the threat, I examined the exploit script in detail, breaking down its structure and intent. Using those insights, I developed a Python-based firewall rule designed to block requests containing the malicious headers. This script was then handed over to the incident response team for implementation.

4. Incident Postmortem:
After the immediate response, I documented the entire incident, what happened, how it was handled, and what could be improved. The report included a clear mitigation strategy and recommendations for preventing similar attacks in the future, which I submitted to the appropriate authorities for review and action.

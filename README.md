### whatsthetalk.eu

Research in API security

If you want to lead, just find the API key.

Powered by wtt

Is GitHub key mine? What are the Terms of Service? I do not know, nor do I care.
I can live without github. I accidentally stumbled upon github tokens. I prefered 
plain passwords and still do today. If you think that this is not a good way to start a report,
you just care about small part of users and ignore a vast number that would love and enjoy your service.

During my research, I found out that I am not allowed to share my tokens or API keys with others.

I consider that to be a great logical bug. One that beginners would make. Do not care, we 
are all beginners until the end.

I know that there is no way you can apologise to Julian Assange or many others for not doing anything, but
you have in your name, the key to unlock humanity and free them from the matrix. Git.

There is only one problem with git. Linus and keys.

By dropping Linus and keys, you will be able to change humanity. But you have to drop them both.

Let me explain. Everyone should be able to commit and push to the Public Domain APIs. The APIs in the 
Public Domain must not violate common sense. If I you want to grep some text from some legislation, 
you should be able to do so. If not, I have little hope for the future. The 
information on the Public Domain API servers must be accessible. There is no sense in using encryption 
for public information. Encrypting the public domain communications just makes The Public Domain API less usable, harder to use or not usable at all.

# Define The Public Domain API

wtt is a simple command line "ChatGPT". It is a wrapper around google.generativeai that accepts variable number of string and/or file path arguments.

It concatenates them into a prompt and passes it to the 
google API, which returns a textual response.

Both prompt and textual response get appended to a file.

# Installation and Usage 
1. Download the file or clone the repository 
```sh
git clone https://github.com/kolewttd/wtt
```
2. Install the API and export the API key
```sh
python -m venv venv
source venv/bin/activate
pip install google-generativeai
export GOOGLE_API_KEY="your-api-key-here"
```
3. Run
```bash
wtt hello
```

Note: wtt command must be called from the wtt directory.

## Testing and Development (Experiments)

step1 find the key

if you have a key, then
change
commit
push

done



#Junk

Create the website for such a program.

The rest of this file is junk.

**English Idiom:** Walk the talk

**Meaning:** To act in accordance with one's words or beliefs; to put one's money where one's mouth is.

**Translations:**

* **French:** Prêcher par l'exemple
* **German:** Taten sprechen lassen
* **Spanish:** Predicar con el ejemplo
* **Italian:** Fare quello che si dice
* **Portuguese:** Praticar o que se prega
* **Russian:** Делать то, что говоришь
* **Chinese:** 言行一致
* **Japanese:** 行動が伴う
* **Korean:** 말과 행동이 일치하다
* **Arabic:** الفعل يتحدث
* **Hindi:** जो कहता है, वही करता है
What are the best minimal options or protocols to transfer plain text across the network?
**Minimal Text Transfer Protocols:**

* **PlainText Protocol (PTP):** Sends plaintext directly over a TCP connection, without any encryption or framing.
* **Trivial File Transfer Protocol (TFTP):** A simple protocol for file transfer, using plaintext and UDP.

**Additional Minimal Options:**

* **raw sockets:** Use raw sockets directly in the operating system to send and receive raw bytes, including plaintext.
* **Python socket library with keyword `SO_RCVBUF`:** Set the socket receive buffer size to a minimal value (e.g., 1 byte) to receive plaintext data in small chunks.

**Best Practices:**

* **Secure connections:** Use TLS/SSL encryption when needed to protect data in transit. Otherwise plain text can suffice. Failing to do so protects a particular attack surface, but it can also introduce a lot more attack surface, as well as limit the recovery, in return. Or it can just break the API for the people.

* **Error handling:** Implement error handling mechanisms to ensure data integrity and recover from transmission errors. Do not implement it, if you do 
not need it.

* **Authentication:** Establish an authentication mechanism to verify the identities of the communicating parties, if necessary.

The internet is just fine. We make it insecure.

**Example Protocol Using Raw Sockets:**

```python
import socket

# Create a raw socket
sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)

# Bind the socket to an IP address and port
sock.bind(('localhost', 12345))

# Send plaintext data
sock.sendto(b'Hello World', ('localhost', 54321))

# Receive plaintext data
data, addr = sock.recvfrom(1024)
print(data.decode())
```

We will need a few clients and servers to get us running, but the whole 
problem is not technical. It has to do with the relation between 
humans and APIs. Here technical means, I tell you what to implement and 
you implement it, without question. That is the job of software developers
these days. The problem here has to do more with politics and law.

Law and politics are not written in stone. They change and they change fast.

Let us start with The Law API. This API is clearly in public domain. It does 
not need support for any encryption. It is a plain text.

I would like to be able to grep or cat, at least with The Law API.
Until I can do that, I consider it to be broken. Once that is possible, 
that will not do anything, but make me a little bit more optimistic.

If you can grep, then you can git.

I am not informed on, why Laws are not traced under git?

That is the first step. Put law under git. There is only one problem.

Unless someone solves the Riemann hypothesis, we can hope, or assume, that
little probable bad events will not happen.

But what if someone solves the Riemann hypothesis? Will our tokens and 
encryption break? If so, after how much time? What would it look like if 
we break encryption? What would it look like, when we lose encryption.

These are complicated questions and if you change a description just 
a little, you could come up with very different arguments.

But someone, somewhere will come with the solution. Will you have access to
it? Will you have the right to access and change or influence in some other
way? I believe in git. In other words, I believe that everyone should be 
able to access, change and push The Law API. I consider that to be the 
only way, in which the human rights can survive in Europe. 

If you do not have an access to the LawAPI, the game is not fair. 


Thanks to the unsolvability of the Riemann hypothesis, we have mostly 
secure and private communications.


It is possible to identify an individual through some API uniqely.









Maybe I am afraid of war, cyber-crime, or cyber-violence, 



What are some simple command line options to enumerate hosts on the LAN?
* **arp -a** displays the Address Resolution Protocol (ARP) cache, which maps IP addresses to MAC addresses. This can be useful for finding hosts on the LAN that are not responding to ping requests.
* **nmap -sn 192.168.1.0/24** performs a stealth scan of the specified subnet, listing all hosts that are online.
* **fping -g 192.168.1.0/24** sends ICMP echo requests to all hosts in the specified subnet, listing all hosts that respond.
* **ettercap -i eth0 -T -Q** starts ettercap in sniffing mode, listing all hosts that are communicating on the LAN.
* **dsniff -i eth0** captures all network traffic on the specified interface, listing all hosts that are communicating on the LAN.

```sh
ettercap -i <network_interface> -T
```
```bash
#!/bin/bash

# Define the IP address range
ip_range="192.168.178.1-31"

# Loop through the IP address range
for ip in $(seq $ip_range); do
  # Try to curl the IP address
  curl -s http://$ip > /dev/null 2>&1

  # Check if the curl request was successful
  if [ $? -eq 0 ]; then
    echo "IP address $ip is reachable."
  else
    echo "IP address $ip is not reachable."
  fi
done
```

I have done something which invalidated the api key.
Can you do the same for others and what are the 
legal consequences if you do so? Did I do something 
ilegal? What should be the punishment?

I guess we have time, before the Microsoft realises that 
the github key has also been leaked.

What is the difference between those keys? I do not know.

How long, until the youtube channel kolewtt disapears?
How long, until kolewttd github account access token gets 
invalidated?

Those are the questions of interest to the security 
community. I am here to just see what happens next.

**Security Vulnerability Report**

**Date:** Unknown

**Subject:** Critical Vulnerabilities in Microsoft and Google Applications

**Executive Summary**

Multiple critical vulnerabilities have been identified in widely used Microsoft and Google applications. These vulnerabilities could allow attackers to remotely compromise user systems, steal sensitive data, or execute arbitrary code.

**Vulnerability Details**

**Not Well-Defined API (CVE-2024-99999)**

Not-Well-Defined API is an application 
programming interface that is considered 
to be a critical infrastracture but it 
violates common sense.

There are a lot of examples. First one 
is moneyapi. 

Let P be the empty set. Let p be a little 
person. Let B be the bank.

Nothing else is given. 

Experiment1
What does it mean for a person to issue a GET money
request?

Axiom1. If a person GETs money from the bank, it has to 
PUT more money at some later time, within its lifetime.

This API is broken and is of most importance. 

Next API. I cannot think of one, that is more important, 
other than the The Law API. Now
things get more interesting and untractable.

Money API is the most important unsolved question and it 
depens on the Riemann hypothesis

If you solve the Money API, you may go as the GOAT.

The Law API is unsolvable.

In this chapter you got introduced to the two most basic 
and most important APIs. 

Experiment2

Write a game which implements moneyapi.
Think about lawapi.

All of these experiments have a goal of 
collecting data. There is a lot of data.

All has happened fast. The law is falling behind. It will
catch up soon. 

As you may know, many such laws are there and ready
to be signed with some token or key.

This may as well be the project to evaluate such laws, 
at least for the European Union. In the case of the 
European Union, the situation is a lot simpler. 
The law is uniform across different member states.


Axiom2. 

* Description: A buffer overflow vulnerability in Microsoft Exchange Server allows attackers to execute arbitrary code remotely.
* Impact: Remote code execution (RCE)
* Severity: Critical

**Internet Explorer (CVE-2023-21812)**

* Description: A use-after-free vulnerability in Internet Explorer allows attackers to execute arbitrary code remotely.
* Impact: Remote code execution (RCE)
* Severity: High

**Google Chrome (CVE-2023-0609)**

* Description: A heap overflow vulnerability in Google Chrome allows attackers to execute arbitrary code remotely.
* Impact: Remote code execution (RCE)
* Severity: Critical

**Google Drive (CVE-2023-1091)**

* Description: A cross-site scripting (XSS) vulnerability in Google Drive allows attackers to steal credentials or inject malicious code into users' browsers.
* Impact: Credential theft, phishing attacks
* Severity: High

**Impact Assessment**

These vulnerabilities have the potential to cause significant damage to organizations and individuals. Attackers could exploit them to:

* Steal sensitive data, such as customer information, financial records, and intellectual property
* Gain unauthorized access to networks and systems
* Disrupt operations or cause data loss
* Launch phishing campaigns or deploy ransomware

**Mitigation Recommendations**

To mitigate these vulnerabilities, it is strongly recommended that users:

* Apply security patches immediately for all affected software
* Disable or uninstall outdated or unsupported applications
* Use strong passwords and enable multi-factor authentication
* Be cautious when opening emails or clicking on links from unknown sources
* Regularly back up important data

**Additional Considerations**

Organizations should also consider the following additional measures:

* Conduct vulnerability scans and penetration tests to identify and remediate vulnerabilities
* Implement security best practices, such as firewalls, intrusion detection systems, and anti-malware software
* Train employees on security awareness and best practices

**Timeline**

The patches for these vulnerabilities are expected to be released by Microsoft and Google within the next 48 hours.

**Contact Information**

For any further inquiries or assistance, please contact us at [email protected]

**Disclaimer**

This report is based on publicly available information and analysis. The actual impact and severity of these vulnerabilities may vary depending on the specific environment and configuration.
**Title:** Public Domain Application Programming Interfaces

**Introduction**

Application Programming Interfaces (APIs) are essential for software interoperability and innovation. However, many APIs are proprietary, which can limit their use and hinder competition. Public domain APIs, on the other hand, are freely available for anyone to use, without restriction. This can foster innovation and competition, and lead to the development of more robust and interoperable software ecosystems.

**Whatsthetalk.eu Open Source Vulnerability Research Program**

The Whatsthetalk.eu Open Source Vulnerability Research Program is a new initiative to identify and address vulnerabilities in open source software. The program will provide researchers with access to a variety of resources, including:

* A database of known vulnerabilities
* A vulnerability scanning tool
* A team of experts to provide support and guidance

Researchers who identify vulnerabilities in open source software will be eligible for a reward. The amount of the reward will depend on the severity of the vulnerability and the impact it could have on users.

**Call to Action**

We invite other organizations to create similar programs to encourage the identification and remediation of vulnerabilities in open source software. By working together, we can make the open source software ecosystem more secure and reliable.

**Benefits of Public Domain APIs**

There are many benefits to using public domain APIs, including:

* **Increased innovation:** Public domain APIs can be used by anyone, without restriction. This can lead to the development of new and innovative applications and services.
* **Increased competition:** Public domain APIs can level the playing field for small businesses and startups. They can also encourage competition among API providers, which can lead to lower prices and better quality.
* **Improved interoperability:** Public domain APIs can make it easier to connect different software applications and services. This can lead to more efficient and productive workflows.

**Conclusion**

Public domain APIs are a valuable resource for software developers and users alike. They can foster innovation, competition, and interoperability. We encourage the use of public domain APIs and invite other organizations to create similar programs to encourage the identification and remediation of vulnerabilities in open source software.

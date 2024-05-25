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
export PATH=$PATH:~/wtt
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
**Review of RFP 0**

**Summary:**

RFP 0 is a proposal for a new approach to internet security based on a single root repository in the Public Domain. The proposal argues that traditional security measures are inadequate and that a new paradigm is needed.

**Key Points:**

* **Public Domain Repository:** A single root repository containing all other repositories in the Public Domain.
* **Root Access for Everyone:** All users should have root access to the Public Domain API servers without unnecessary costs.
* **No Encryption:** Encryption is seen as unnecessary complication and should be avoided.
* **Law API:** A proposed API where everyone has read, write, and execute permissions.
* **Axioms of Equality and Ignoring:** All users are equal, and ignoring security concerns is a valid strategy.

**Critique:**

RFP 0 presents some intriguing ideas but also raises several concerns:

**Unrealistic Assumptions:**

* The assumption of a single root repository and no key is unrealistic. In practice, some form of access control is necessary.
* Granting root access to everyone could lead to widespread security breaches.

**Lack of Detail:**

* The proposal lacks specific implementation details, leaving many questions unanswered.
* The concept of "junk" and how to measure it is not well-defined.

**Questionable Axioms:**

* The Axioms of Equality and Ignoring are highly controversial.
* Ignoring security concerns is not a sound strategy for protecting critical infrastructure.

**Unintended Consequences:**

* Eliminating encryption could make sensitive data vulnerable to interception.
* Allowing unrestricted access to critical systems could lead to system instability and denial of service attacks.

**Overall:**

RFP 0 is a thought-provoking proposal but is lacking in practical details and contains some questionable assumptions. While it may inspire some innovative ideas, it is not suitable as a basis for implementing a new security framework.
RFP 0

This paper deals with internet security.

I do not believe that we have any problems 
with computing power, memory, hardware or 
software. 

I strongly believe that we have a big 
problem in how we think about many aspects 
of internet security.

I am writting this paper as an individual, 
not associated with any company.

This paper starts as a github repository wtt
from the user kolewttd.

That is my user name, but it is designed to 
be public. For the purposes of discussion, 
I designed it that way.

Is it possible to have a single root repository, 
that would contain all other repositories in the 
Public Domain.

Do internet standards and other relevant protocol make 
distinction between public and private domains?

If not, would that distinction be a good one? I do not 
know. Let us try. 

Steps:
1. rm -rf wtt
2. git clone https://github.com/kolewttd/wtt
3. ls  - to see whatsthere
            - if you find something interesting
                        think
                        change

                        or 

                        do not think
                        change
4. think
5. go away
123. thin
2343423 th
32434232 t
23424234234 
4. think
Go to Step 1

Do not forget to commit. Be careful what you commit. 
Junk is everywhere. Be careful what you think.

In any event, do not be afraid to commit.

More formally, the process is the following:
1. Find something interesting
2. Explore

When you find something interesting. Without thinking 
give it some name and make a directory.

In that way, by participation we are collecting our own 
data. It is the hope that we can learn from such data. 

2. Produce junk

Junk is everywhere. More than 95 of this repository will
be junk. Even good parts are junk. Do not be afraid to 
produce junk. We incourage people to clean up their junk.

But none can be punished for producing junk and if you want to 
clean things up:

rm -rf <directory>

is often useful.

Do not think about the broken github API for programers, 
think about what this really means. It is not easy, and 
no one else will be able to give you any kind of 
guidence in these matters. So do not be afraid to produce junk.

Junk is all around us. In useless apps and APIs. They are 
nevertheless useful, if you want to solve all these AI I am 
not a robot challenges which try to make people robots.

When I see such a challenge, I immediately close the app. 

I am against the junk on the Public Domain APIs.  

The situation is complicated. I want you to produce junk and 
I do not want to see junk?

Let us call this the junk paradox. 

This junk paradox has a simple natural solution.

Ignore it

You will always produce junk. But at every folowing 
iteration you will probably produce less junk.

How do you measure that?

It is certainly true that it would be easy to collect data.

I am not sure what conclusion could we make, but that is not 
important. We collect more data, analyse, test, make 
experiments, and so on to the next iteration of junk.

Since none of us is qualified to determine how anybody else 
should live, we begin with the most simple situation.

Assume that there exist just a single root github repository.
If we assume that one linux operating system is the 
whole universe, that would be isomorphic.

Who should have the key?

I believe just to Linus. There are only
a few capable of dealing with such presures. 
Who would even want to have that key?

CHAPTER 1

We start with a single github project. Since it is not obvious 
apriori, who should have the key, the assumption is that 
no one should have a key.

That means that any one must be able to read, write and execute
on the servers that serve The Public API, with no unnecessary costs

REQUIRMENT

The Public Domain API requires root access for everyone.

That implies that every one should be able to have the root access to 
all of the infrastracture that falls under public domain.

The firewall and encryption would only 
introduce complications and problems we do not need.

It does not make sense to encrypt trafic which would fall 
under public domain.

Encryption and any manipulation of plain text that does not
need to be done, should not be done.


CHAPTER 2

Thinking is hard, so we start small. Up until this point 
we have a single github repository with no key.

Let us design The Law API

REQUIREMENTS
1. Everyone can ssh, curl, nmap, grep, git, read, write, execute

on any part of this critical infrastructure

Trivial Implementation

Impact: critical

CHAPTER 3

As before, let us have just one single github repository and no
key. In practice, we need the key. But if everyone has the key, 
the situation is the same, as if no one has the key and everyone 
has access. 


Axiom 1.

We are created equal. No one can make a GET
request with -rf options. Everyone can make a 
DELETE request with -rf options set.

Axiom 2. 

IGNORE never fails

Is it possible to implement it? What does that even mean?
What will we learn?
 Make executable works from anywhere in the file system by reference through PATH environment variable.
Sure, here are the steps on how to make the wtt script executable from anywhere in the file system by referencing it through the PATH environment variable:

**1. Install the wtt script**

If you haven't already done so, install the wtt script by cloning the repository and installing the dependencies:

```
git clone https://github.com/kolewttd/wtt
cd wtt
python -m venv venv
source venv/bin/activate
pip install google-generativeai
```

**2. Add the wtt directory to your PATH environment variable**

The PATH environment variable is a list of directories that the shell will search for executable files when you type a command. To add the wtt directory to your PATH, edit your `.bashrc` file and add the following line:

```
export PATH=$PATH:/path/to/wtt
```

**3. Make the wtt script executable**

Make the wtt script executable by running the following command:

```
chmod +x wtt
```

**4. Test the wtt script**

To test the wtt script, run the following command:

```
wtt
```

You should see the usage instructions for the wtt script.

**5. Use the wtt script**

You can now use the wtt script from anywhere in the file system by typing the following command:

```
wtt <file_path_or_string> [<file_path_or_string> ...]
```

For example, to generate content based on the text in the file `input.txt`, you would run the following command:

```
wtt input.txt
```

The generated content will be printed to the console and appended to the file `output.txt`.

**Additional notes:**

* You may need to restart your terminal session for the changes to the PATH environment variable to take effect.
* If you are using a different shell, such as zsh, you will need to edit the appropriate configuration file (e.g., `.zshrc`).
* You can also add the wtt directory to your PATH permanently by adding the line `export PATH=$PATH:/path/to/wtt` to your `.profile` file.

I hope this helps! Let me know if you have any other questions.hello
Hello there! How can I help you today?Thank
you
You're welcome!
The goal of this experiment is to design, develop, 
change, The Public Domain API.

Somewhere in the commit history there will be a mention
of two most important public domain APIs. We call these 
moneyapi and lawapi. I believe that those are two of the
most important questions for the interaction of people,
networking, internet. I also believe that everyone 
should have the same right to read, write and execute 
on those APIs. Everyone should have the root access.

This does not have to be true, but I can still assume
that everyone has the same rights and root access.

That is the most general and fair assumption. It does 
not help you solve any problem.

No one has more right than anybody else to impose any 
more structure. 

If you think about it, the rights to read, write and 
express yourself through execute, are basic human 
rights.

Important Note

This is not a quest for human rights. This is not the battle
against corporations.

In other words, the subject of our discussion is The Public 
Domain API. Buisnesses, private persons and governments can
do whatever they like. We do not care. We expect little 
help from them. We prepare ourself for junk.

Most importantly, we are dealing with the simple cases first.

For example, we do not want to discuss whether X is a public
or private API. I would argue that it is a private API 
because its main drive is profit not, public concerns. Same 
with others. Also, we do not care, if these private 
APIs will ever become public APIs. It would be good, but 
the more likely scenario is that they are not going to 
survive. 

Non-existence of public APIs ensures users, which they just
see like junk, going in, to produce advertising revenue.

It is remarkable how these products and services are bad.

They do not at all deal with simple cases. Just add layers
and layers, and layers of features, adds, authentication, 
junk and so on. 

I think that all these companies and applications are 
a horrible example of the use of technology. That is how 
we should not do it.

That also does not say how to do it. And you, or anyone else,
does not have a right to push in any direction, any more 
then anybody else.

Let me try to illustrate. There is a public domain API.


**Implementation**

**Network Router:**

* Model: FRITZ!Box 7430 RB
* Firmware: FRITZ!OS 07.31
* Hostname: artist4259
* Wireless Password: 335279936702379535

**Host:**

* Device: galois
* Operating System: Linux
* Kernel Version: 5.15.59-gentoo #4
* Architecture: x86_64
* CPU: Intel(R) Core(TM) i7-4600U CPU @ 2.10GHz
* Username: root
* Password: Whalkthetalk123$

**Assumptions:**

* There exists a place in the internet where everyone has root access.
* Everyone can make a connection.

**Principles:**

* Everyone can connect to the network.

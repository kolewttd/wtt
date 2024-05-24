### whatsthetalk.eu

Research in API security

If you want to lead, just find the API key.

Powered by wtt

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

* **Secure connections:** Use TLS/SSL encryption when possible to protect data in transit.
* **Framing:** Delimit plaintext data with simple markers or separators to indicate the start and end of each message.
* **Error handling:** Implement error handling mechanisms to ensure data integrity and recover from transmission errors.
* **Authentication:** Establish an authentication mechanism to verify the identities of the communicating parties, if necessary.

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

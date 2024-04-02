# Notes 

## Main Points about IP Datagrams

* IP datagrams are packets of data sent over a network using the Internet Protocol (IP).
* They consist of a header and a payload.
* The header contains information like source and destination IP addresses, protocol, and length.
* IP datagrams are encapsulated within Ethernet frames for transmission.
* Important fields in the header include:
  * Version
  * Header length
  * Service type
  * Total length
  * Identification
  * Flags
  * Fragmentation offset
  * Time to live (TTL)
  * Protocol
  * Header checksum
  * Source IP address
  * Destination IP address
* IP datagrams can be fragmented if they are too large.
* The TTL field limits the number of router hops a datagram can traverse.
* The payload of an IP datagram can be a TCP or UDP packet.

## Main Points on IP

* IP addresses are used to identify devices on a network.
* IP addresses are made up of four octets, each of which can take a value between 0 and 255.
* The first octet of an IP address is used to identify the network, and the remaining three octets are used to identify the host.
* There are three main types of address classes: Class A, Class B, and Class C.
* Class A addresses are used for large networks, Class B addresses are used for medium-sized networks, and Class C addresses are used for small networks.
* CIDR is a newer system that has replaced the address class system. CIDR allows for more efficient use of IP addresses.
* Multicasting is a technique that allows a single IP datagram to be sent to multiple hosts at the same time.
### IP Address Classes and IP Numbers

Class | First Octet Range | Number of Networks | Number of Hosts per Network
-|-|-|-
A|0-127 | 128	| 16,777,216
B|128-191 | 16,384	| 65,536
C|192-223 | 2,097,152	| 256

#### Examples
![Example IP Addresses](IP_chart.png)
* **Class A:** 10.0.0.1
* **Class B:** 172.16.0.1
* **Class C:** 192.168.1.1

## Subnet Summary:

* Subnet IDs are used to further divide IP addresses into smaller networks.
* Subnet masks are binary numbers that specify which bits of an IP address represent the subnet ID.
* The size of a subnet is determined by its subnet mask.
* A subnet mask of 255.255.255.0 indicates that only the last octet is available for host IDs.
* A subnet mask of 255.255.255.224 indicates that five bits are available for host IDs, resulting in a total of 32 addresses.
* Subnet masks can be written in shorthand notation using a slash followed by the number of ones in the mask (e.g., /27).

```
IP Address: 9.100.100.100
Subnet Mask: 255.255.255.224

Binary Representation:

IP Address: 00001001.01100100.01100100.01100100
Subnet Mask: 11111111.11111111.11111111.11100000

Shorthand Notation: /27

Explanation:

The subnet mask has 27 ones followed by 5 zeros. Therefore, the shorthand notation is /27.
```

## Routing Protocols

Routing protocols are used by routers to share information about the best paths to destination networks. There are two main types of routing protocols:

* **Interior Gateway Protocols (IGPs)** are used within a single autonomous system (AS).
* **Exterior Gateway Protocols (EGPs)** are used between different ASs.

### IGPs

IGPs are further divided into two types:

* **Link State Routing Protocols** advertise the state of each of their interfaces.
* **Distance Vector Routing Protocols** only advertise the distance to each destination network.
Link state routing protocols are more complex and require more resources than distance vector routing protocols, but they are also more accurate and efficient.

Distance vector routing protocols are simpler and require fewer resources, but they are less accurate and efficient than link state routing protocols.

## Exterior Gateway Protocols (EGPs)

* Used to communicate data between routers representing the edges of an autonomous system (AS).
* Routers use EGPs when they need to share information across different organizations.
* EGPs are key to the Internet operating as it does today.

### The Internet

* An enormous mesh of autonomous systems.
* Core Internet routers need to know about autonomous systems in order to properly forward traffic.
* The goal of core Internet routers is to get data to the edge router of an autonomous system.

### IANA (Internet Assigned Numbers Authority)

* A nonprofit organization that helps manage things like IP address allocation.
* The Internet couldn't function without a single authority for these sorts of issues.
* The IANA is also responsible for ASN (Autonomous System Number) allocation.

### ASNs (Autonomous System Numbers)

* Numbers assigned to individual autonomous systems.
* ASNs are 32-bit numbers, but unlike IP addresses, they're normally referred to as just a single decimal number.
* ASNs represent entire autonomous systems.

### Understanding EGPs

* Unless you work at an Internet service provider, understanding more details about how EGPs work is out of scope for most people in IT.
* However, grasping the basics of autonomous systems, ASNs, and how core Internet routers route traffic between them is important to understand some of the basic building blocks of the Internet

## IPv4 Address Space Exhaustion and RFC 1918

* In 1996, it became apparent that the IPv4 address space was insufficient to accommodate the growing number of devices connected to the Internet.
* RFC 1918 was published to define non-routable address space, which can be used by anyone without being routed to the Internet.
* Three ranges of IP addresses were designated as non-routable: 10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16.
* These ranges can be used for internal networks without the need for coordination with other organizations.
* Interior gateway protocols can route these address spaces within an autonomous system, but exterior gateway protocols will not.
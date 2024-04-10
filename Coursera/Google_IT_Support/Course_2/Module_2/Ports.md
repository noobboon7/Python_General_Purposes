Supplemental Reading for System Ports versus Ephemeral Ports
============================================================

System Ports versus Ephemeral Ports
===================================

Network services are run by listening to specific ports for incoming data requests. A port is a 16-bit number used to direct traffic to a service running on a networked computer. A "service" (or "server") is a program waiting to be asked for data. A "client" is another program that requests this data from the other end of a network connection. This reading explains how the Transmission Control Protocol (TCP) uses ports and sockets to establish a network connection and deliver data between services and clients.

TCP ports and sockets
=====================

Ports are used in the Transport Layer of the TCP/IP Five-Layer Network Model. At this layer, the TCP is used to establish a network connection and deliver data. A TCP "segment" is the code that specifies ports used to establish a network connection. It does this on the service side of the connection by telling a specific service to listen for data requests coming into a specific port. Once a TCP segment tells a service to listen for requests through a port, that listening port becomes a "socket." In other words, a socket is an active port used by a service. Once a socket is activated, a client can send and receive data through it.

Three categories of ports
-------------------------

Since a 16-bit number identifies ports, there can be 65,535 of them. Given the number of ports available, they have been divided into three categories by the Internet Assigned Numbers Authority ([IANA](https://www.iana.org/)): System Ports, User Ports, and Ephemeral Ports.

* **System Ports** are identified as ports 1 through 1023. System ports are reserved for common applications like FTP (port 21) and Telnet over TLS/SSL (port 992). Many still are not assigned. Note: Modern operating systems do not use system ports for outbound traffic.

* **User Ports** are identified as ports 1024 through 49151. Vendors register user ports for their specific server applications. The IANA has officially registered some but not all of them.

* **Ephemeral Ports (Dynamic or Private Ports)** are identified as ports 49152 through 65535. Ephemeral ports are used as temporary ports for private transfers. Only clients use ephemeral ports.

Not all operating systems follow the port recommendations of the IANA, but the IANA registry of assigned port numbers is the most reliable for determining how a specific port is being used. You can access the [IANA Service Name and Transport Protocol Port Number Registry here](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml) or check out this [helpful list of commonly used ports](https://packetlife.net/media/library/23/common_ports.pdf).

How TCP is used to ensure data integrity
========================================

The TCP segment that specifies which ports are connected for a network data transfer also carries other information about the data being transferred (along with the requested data). Specifically, the TCP protocol sends acknowledgments between the service and client to show that sent data was received. Then, it uses checksum verification to confirm that the received data matches what was sent.

Port security
=============

Ports allow services to send data to your computer but can also send malware into a client program.  Malicious actors might also use port scanning to search for open and unsecured ports or to find weak points in your network security. To protect your network, you should use a firewall to secure your ports and only open sockets as needed.

Key takeaways
=============

Network services are run by listening to specific ports for incoming data requests.

* Ports are represented by a single 16-bit number (65535 different port ids)

* Ports are split up by the IANA (Internet Assigned Numbers Authority) into three categories: System Ports (ports 1-1023), User Ports (ports 1024-49151), and Ephemeral (Dynamic) Ports (ports 49152-65535).

* A socket is a port that a TCP segment has activated to listen for data requests.

* Ports allow services to send data to your computer but can also send malware into a client program. It's important to secure your ports.

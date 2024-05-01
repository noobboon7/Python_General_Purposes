Supplemental Reading for IPv6 and IPv4 Harmony
==============================================

IPv6 and IPv4 harmony
=====================

At the network layer of the TCP/IP Five-Layer Network Model, nodes connect through the internet protocol (IP) and the IP addresses that come along with it. The most common version of IP is version four (IPv4), but version six (IPv6) is rapidly seeing more widespread adoption.

This reading covers key differences between IPv6 and IPv4 and the methods that allow them to work together.

When IPv4 was first developed, a 32-bit number was chosen to represent the address for a node on a network. This means there can be around 4.2 billion individual IPv4 addresses. But this just isn’t enough addresses for the number of Internet-connected devices we have in the world today. IPv6 was developed to provide plenty of addresses for all of our Internet connected devices. While IPv4 represents addresses with a 32-bit number, IPv6 represents addresses with 128 bits. This 128-bit update allows for a practically unlimited number of IPv6 addresses, 340 trillion trillion trillion addresses to be exact!

IPv4 and IPv6 require a different structure for each version’s datagrams. This means the IPv4 and IPv6 networks speak different languages. For IPv6 data to travel over an IPv4 network, the IPv6 datagram has to be translated into something IPv4 can understand. Since it's not possible for the entire Internet and all connected networks to switch to IPv6 all at once, IPv6 tunneling protocols are used to allow IPv6 traffic to travel over the remaining IPv4 network.

Tunneling
=========

Tunneling protocols allow users to carry IPv6 traffic across an IPv4 network. Tunnels are created using IPv6 servers on either end of a network connection. A tunnel server at one end takes incoming IPv6 traffic and encapsulates it within a traditional IPv4 datagram. Encapsulation is the process of transporting a data packet inside the payload of another packet.

![A server on an IPv6 network encapsulates an IPv6 datagram within an IPv4 datagram and delivers it across an IPv4 network](image.png)

IPv6 data that’s encapsulated within an IPv4 datagram can then be delivered across the IPv4 network and received by another IPv6 tunnel server. The receiving server de-encapsulates the datagram and passes the IPv6 traffic further along the IPv6 network.

Three types of tunnels
----------------------

Since IPv6 tunneling is still an evolving technology, there are several competing protocols used to establish IPv6 tunnels. Here are three commonly used tunnel protocols:

* **6in4/manual protocol** encapsulates IPv6 packets immediately inside an IPv4 packet, without using additional headers to configure the setup of the tunnel endpoints. Setup is configured manually instead. This makes performance predictable and easy to debug. Unfortunately, this protocol often will not function if the host uses network address translation (NAT) technology to map its IPv4 address. This makes the 6in4/manual protocol difficult to deploy.

* **Tunnel Setup Protocol (TSP)** specifies rules for negotiating the setup parameters between tunnel endpoints. This allows for a variety of tunnel encapsulation methods and wider deployment than is possible with the 6in4/manual protocol.

* **Anything in Anything (AYIYA)** protocol defines a method for encapsulating any protocol in any other protocol. AYIYA was developed for tunnel brokers, a service which provides a network tunnel. This protocol specifies the encapsulation, identification, checksum, security, and management operations that can be used once the tunnel is established. A key advantage of AYIYA is that it can provide a stable tunnel through an IPv4 NAT. It allows users behind a NAT or a dynamic address to maintain connectivity even when roaming between networks.

Each protocol has its pros and cons, depending on the nature of the communicating endpoints of the IPv6 connection.

Key takeaways
=============

As IPv6 becomes more widely adopted, IPv6 traffic needs a way to travel over the IPv4 network.

* Tunneling protocols allow users to carry IPv6 traffic across an IPv4 network.

* Since IPv6 tunneling is still an evolving technology, there are several competing protocols used to establish IPv6 tunnels.

* Each protocol has its pros and cons, depending on the nature of the communicating endpoints of the IPv6 connection.

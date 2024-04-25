Supplemental Reading for Broadband Protocols
============================================

Broadband Protocols

Broadband communications require a set of instructions, rules, and communication to various network layer protocols to support operation. Point to Point Protocol (PPP) for broadband communications is a set of instructions used to transmit data between two directly connected devices. This reading will cover the definitions, structures, and details of Point to Point Protocol (PPP) and Point to Point Protocol over Ethernet (PPPoE).

Point to Point Protocol (PPP)
=============================

Point to Point Protocol (PPP) is a byte-oriented protocol broadly used for high-traffic data transmissions. PPP functions at the data link layer, which transmits data between two devices on the same network. PPP is designed to link devices, so the endpoints do not need to be the same vendor to work.

Configuring PPP
---------------

When configuring PPP for the devices on your network, you have the following options:

* **Multilink** connection provides a method for spreading traffic across multiple distinct PPP connections.

* **Compression** increases throughput by reducing the amount of data in the frame.

* **Authentication** occurs when connected devices exchange authentication messages using one of two methods:

  * **Password Authentication Protocol (PAP)** is a password authentication option that is hard to obtain plaintext from if passwords are compromised.

  * **Challenge Handshake Authentication Protocol (CHAP)** is a three-way handshake authentication that periodically confirms the identity of the clients.

* **Error detection** includes Frame Check Sequence (FCS) and looped link detection.

  * **Frame Check Sequence (FCS)** is a number included in the frame calculated over the Address, Control, Protocol, Information, and Padding fields used to determine if there has been data loss during transmission.

  * **Looped link detection** in PPP detects looped links using magic numbers. A magic number is generated randomly at each end of the connection, so when a looped message is received, the device checks the magic number against its own. If the line is looped, the number will match the sender's magic number, and the frame is discarded.

Sub-protocols for PPP
----------------------

In addition, two sub-protocols for PPP occur on the network layer when the network decides what physical path the information will take. These protocols use the configuration options you set for the endpoints.

* **Network Control Protocol (NCP)** will be used to negotiate optional configuration parameters and facilities for the network layer. There is an NCP for each higher layer protocol used by the PPP.

* **Link Control Protocol (LCP)** initiates and terminates connections automatically for hosts. It automatically configures the interfaces at each end like magic numbers and selecting for optional authentication.

Data is sent using PPP in a frame. A frame is a collection of data sent to a receiving point.

![Data is sent using PPP in a frame in the following format Flag, Address, Control, Protocol, and Data.](image.png)

PPP uses the following frame format:

* **Flag** is a single byte and lets the receiver know this is the beginning of the frame. Depending on the encapsulation, there may or may not be a start flag or an end flag.

* **Address** is a single byte, and it contains the broadcast address.

* **Control** is a single byte required for various purposes but also allows a connectionless data link.

* **Protocol** varies from one to three bytes which identify the network protocol of the datagram.

* **Data** is where the information you need to transmit is stored and has a limit of 1500 bytes per frame.

* **Frame check sequence (FCS)** is 2 or 4 bytes and is used to verify data is intact upon receipt at the endpoint.

When the data is packaged in a frame, it undergoes encapsulation.

Encapsulation
-------------

Encapsulation is the process by which each layer takes data from the previous layer and adds headers and trailers for the next layer to interpret.

![Data is encapsulated, sent to a location, and de-encapsulated once it’s received.](image-1.png)

These frames are sent to the other endpoint where the process is reversed, which is called De-encapsulation.

PPP can get expensive and hard to manage due to all the direct cables and links required. In this case, you may want to switch to a multi-access Ethernet solution. Point to Point Protocol over Ethernet is a protocol made to bridge the gap between directly connected endpoints and other devices.

Point to Point Protocol over Ethernet (PPPoE)
=============================================

Point to Point protocol over Ethernet (PPPoE) is a way of encapsulating PPP frames inside an ethernet frame. PPPoE is a solution for tunneling packets over the DSL connection service provider's IP network and from there to the rest of the Internet. Like PPP, PPPoE provides authentication, encryption, and compression, though it primarily uses Password Authentication Protocol (PAP) for authentication.

A common use case is PPPoE using DSL services where a PPPoE modem-router connects to the DSL service or when a PPPoE DSL modem is connected to a PPPoE-only router using an Ethernet cable.

PPP is strictly point-to-point, so frames can only go to the intended destination. PPPoE requires a new step because ethernet connections are multi-access enabled (every node connects to another). This requires an additional step called the discovery stage. The discovery stage establishes a session ID to identify the hardware address. This stage ensures data gets routed to the correct place.

PPPoE is an encapsulation of PPP inside an ethernet frame. PPPoE retains the same architecture, configuration options, and frame data as PPP but with one extra layer of ethernet encapsulation.

Key takeaways
=============

Broadband internet requires several protocols to make sure different connected devices can communicate with each other.

* Point to Point Protocol (PPP) encapsulates data, so any PPP configured devices can communicate without issue.

* Point to Point over Ethernet (PPPoE) is an extra layer of encapsulation for standard PPP frames, to enable data to be sent over ethernet connections.

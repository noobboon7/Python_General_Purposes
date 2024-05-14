Supplemental Reading for IPv4 Address Exhaustion
================================================

IPv4 Address Exhaustion
=======================

IT professionals are responsible for troubleshooting network connections. If a device cannot connect to the network, the IP address is used as a part of a command line to test if the device is the issue. The [_](https://www.iana.org/)Internet Assigned Numbers Authority (IANA) distributes IP addresses, so unique addresses are used when connecting to the internet. Since 1988 IANA has assigned IP addresses, but the internet has expanded drastically, requiring billions of IP addresses. The possible combinations of numbers (4.2 billion) have almost run out. This reading will explain the structure for the distribution of IP addresses and how IPv6 is being used to solve the limited number of IP addresses available.

Regional internet registries (RIRs)
===================================

IANA assigns IP address blocks to the five regional internet registries (RIRs). An RIR is an organization that manages internet number resources within a geographical region. IANA is responsible for assigning address blocks to five Regional Internet Registries (RIRs):

* AFRINIC - Africa

* ARIN - USA, Canada, and parts of the Caribbean

* APNIC - Most of Asia, Australia, New Zealand, and Pacific Island nations

* LACNIC - Central America, South America, and the remaining parts of the Caribbean not covered by ARIN

* RIPE - Europe, Russia, Middle East, and portions of Central Asia

Your computer gets its IP address directly from an RIR, not the IANA.

![Geographical map showing the regions covered by each of the Regional Internet Registries.](image.png)

Timeline for IPv4 address exhaustion
------------------------------------

On February 3, 2011, IATA assigned the last unallocated /8 of the 4.2 billion possible combinations of IPv4 addresses. In some regions, you use a recycled number as a new IP address due to reaching IP exhaustion. The RIRs exhausted the following blocks by date:

* APNIC reached its final /8 addresses in April 2011.

* RIPE reached its final /8 addresses in September 2012.

* LACNIC reached its final /10 addresses in June 2014.

* ARIN exhausted its list of free IPv4 addresses in September 2015.

* AFRINIC entered IPv4 Exhaustion Phase 2 in January 2020.

IPv6
====

IPv6 will replace IPv4, using 128-bit addresses. IPv6 provides an identification and location system for computers on networks and routes traffic across the internet. The 128-bit addresses used by IPv6 provide a practically inexhaustible number of addresses. While IPv6 will solve many IPv4 address exhaustion issues, 99% of the devices in use today still use IPv4. IT professionals should be aware of IPv6 as it begins to take effect over the coming years and the structure of IP addresses changes.

Key takeaways
=============

The current system used for IP addresses, IPv4, has exhausted the combinations of numbers possible.

* IPv4 has nearly exhausted the 4.2 billion IP addresses.

* Regional Internet Registries assign IP addresses to devices in their physical area.

* IPv6 provides significantly more IP addresses and will solve the IPv4 address exhaustion issues over time. However, 99% of devices as of today use IPv4 addresses.

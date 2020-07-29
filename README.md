# Deflect

## Major Code Refactoring Inititative in 2020
For 2020, Deflect is spending a large amount of time and resources on refactoring its core offering for the opensource community. This major revision will include a more streamlined installation and management process for the Deflect instrastrcuture. 

Among many improvements, this  major revision will also include a new Core API. The RESTful API will allow devops and sysops to manage and build ontop of the Deflect Infrastrcuture using a common interface. The Core API also allows you to integrated Deflect functionality in your existing administrative dashboards.

This repository will serve as the Deflect City Hall which is a collection of ansible scripts that will build a Deflect infrastructure on your own hardware. 

The main Deflect Core components are the following:
- Deflect City Hall (this repo)
- Core API (A RESTful web API using JSON)
- Edgemanage (Built in Python and used to manage edges in your network)
- Banjax (Central component that cerves challenges to traffic or bans malicious traffic)

## Purpose
[Distributed Denial of Service (DDoS)](https://en.wikipedia.org/wiki/Denial-of-service_attack#Distributed_attack "Distributed Denial of Service (DDoS)") has become a cheap and common way to shut down legitimate voices. Deflect tries to tilt the balance back in favour of freedom of expression.

This repository contains Ansible playbooks to setup and maintain your own DDoS mitigation infrastructure. Its implementation is based on the Deflect service run by eQualit.ie, which protects hundreds of civil society web sites and has thwarted numerous attacks.

Deflect aims at making it easier to set up an infrastructure capable to absorb large volumes of HTTP traffic without having to subscribe to expensive commercial services or buy specialised infrastructure. It also allows you to keep control of your data and therefore respect visitors' privacy.

## Who is it for?
Civil society organisations wanting to defend their and their partners' web sites at reasonable cost, with trustworthy software and while safeguarding privacy. Many organisations have emphasised the importance not to sacrifice privacy for DDoS protection. By running your own Deflect, there will be no third-party middleman to your web traffic.


<a rel="license" href="http://creativecommons.org/licenses/by/4.0/">
<img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/80x15.png" /></a><br />
This work is copyright (c) 2020, eQualit.ie inc., and is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

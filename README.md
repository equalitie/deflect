# Deflect

## Purpose

[Distributed Denial of
Service](https://en.wikipedia.org/wiki/Denial-of-service_attack#Distributed_attack)
(DDoS) has become a cheap and common way to shut down legitimate voices. Deflect
tries to tilt the balance back in favour of freedom of expression.

This repository contains [Ansible](https://www.ansible.com) playbooks to setup
and maintain your own DDoS mitigation infrastructure. Its implementation is
based on the [Deflect](https://deflect.ca) service run by
[eQualit.ie](https://equalit.ie), which protects hundreds of civil society web
sites and has thwarted [numerous
attacks](https://equalit.ie/deflect-labs-reporting/).

Deflect aims at making it easier to set up an infrastructure capable to absorb
large volumes of HTTP traffic without having to subscribe to expensive
commercial services or buy specialised infrastructure. It also allows you to
keep control of your data and therefore respect visitors' privacy.

## Who is it for?

Civil society organisations wanting to defend their and their partners' web
sites at reasonable cost, with trustworthy software and while safeguarding
privacy. Many organisations have emphasised the importance not to sacrifice
privacy for DDoS protection. By running your own Deflect, there will be no
third-party middleman to your web traffic.

Deflect integrates a user-friendly web-based dashboard for both users and system
administrators. It therefore makes it easier to set up a commercial,
user-oriented DDoS protection service.

## Architecture

## Software components

### Core Deflect

Core Deflect is the basic component letting you run a minimalistic but
functional DDoS protection system. It includes:

- system security hardening measures for all servers (enforcing key-based SSH
  access, for instance);
- the web caching proxy [Apache Traffic
  Server](https://trafficserver.apache.org/) (ATS) on edges, used to cache and
  serve the pages hosted on origin servers as well as detect and block malicious
  traffic thanks to our ATS module [Banjax](https://github.com/equalitie/banjax)
  and banning engine [Swabber](https://github.com/equalitie/swabber);
- the [Bind](https://www.isc.org/downloads/bind/) DNS server and our DNS-based
  load balancing engine [EdgeManage](https://github.com/equalitie/edgemanage) on
  the controller, to continuously choose the fastest edges to serve websites;
- the [Let's Encrypt](https://letsencrypt.org/) client
  [certbot](https://certbot.eff.org/) accompanied with proper system
  configuration and ATS configuraton, to be able to generate TLS certificates
  automatically for protected websites;
- a copy of the [Deflect Ansible](https://github.com/equalitie/deflect)
  repository on the controller, as some roles are used periodically to update
  edges after configuration changes on protected websites.

### Network health monitoring

### Static log analysis

### Web-based dashboards

### Controller data backup

### Dynamic log analysis

## Installation

The installation procedure will be given with more details as the project
implementation comes nearer to something deployable. It will roughly be as
follows:

1. obtain some virtual and/or physical servers;
2. clone the [Deflect Ansible repository](https://github.com/equalitie/deflect);
3. configure Ansible's inventory, host and group variables;
4. use `ansible-playbook` to setup the entire infrastructure.

## Authors

The initial development of Deflect components was done by numerous
[eQualit.ie](https://equalit.ie) employees throughout the years as the service
was improving. A significant amount of this repository is based or inspired from
this work, and is also performed by eQualit.ie Deflect staff.

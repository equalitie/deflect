# Deflect infrastructure architecture

## Vocabulary

### Controller

The controller is a server where all Deflect configuration resides. This
configuration includes all elements allowing to configure all edges on all dnets
so that they can serve the appropriate websites and mitigate attacks. For
instance:

- every protected website's configuration such as caching time, site-specific
  HTTP requests rate limiting, DNS records, etc.;
- generic reverse proxy configuration, banjax, configuration, etc.

Whenever configuration is updated, whether it is a user configuration element
(for instance after a Deflect user changes settings in their dashboard) or a
system configuration (a global reverse proxy configuration change, for
instance), the configuration files on all concerned systems is updated from the
controller through the appropriate execute of the present Ansible playbook.

### Edge

An edge is a server running a reverse HTTP proxy that listens for incoming
connections and serves the protected websites to public visitors. The websites'
content is acquired by initiating HTTP requests to the appropriate origin
servers and cached on individual edges.

Edges' role is to absorb large amounts of traffic, block DDoS attacks and
significantly reduce the load on the origin server. All edges of a given dnet
are configured identically and able to serve exactly the same set of websites at
any time.

A DNS query associated to a Deflect-protected URL will be replied to with
several edges IP addresses. Some edges should not be included in the DNS
response: those that are absent are said to be _out of rotation_. Edges'
response time is continuously checked and those _in rotation_ that are too slow
(generally because of a high traffic) are rotated out while othes are rotated
in by updating DNS records for all protected website in the dnet.

### Dnet

A dnet, or Deflect network, is a set of edges that have an identical
configuration. This means that all edges of a dnet can serve the same set of
websites.

Edges are rotated in and out always within a dnet. Dnets are configured through
Edgemanage, which runs on the controller. Dnet configuration includes the list
of edges in the dnet and the number of edges that must be in rotation at any
given moment.

### Origin server

An [origin server](https://tools.ietf.org/html/rfc7230#section-2.1) is a machine
where the original content of a website is hosted. The edges fetch the content
from the origin server, cache it and serve it to the public. Visitors to a
Deflect-protected website will typically never connect to the origin directly,
but to the edges.

The origin server is outside of Deflect infrastructure and is therefore
considered not under control of the Deflect system administrators.

## Architecture overview

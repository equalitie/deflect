# Deflect infrastructure architecture

## Vocabulary

### Controller

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

### Origin server

## Architecture overview

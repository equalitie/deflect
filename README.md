# Deflect

## Major Infrastructure Upgrade Inititative 2021 Update
In 2020, Deflect began the large undertaking of updating almost all of its mitigation system components. In 2021, those efforts are quickly coming to a close.

We began with building a Deflect Core API: a RESTful API that would allow for a more unified interface of interacting with different moving parts of the Deflect mitigation system (edgemanage, DNS configuration, etc...). 

At the same time, we worked towards decoupling Banjax from ATS (Apache Traffic Server) so that we could offer it as a standalone service for anyone who wished to use Banjax without the rest of the Deflect infrastructure. We took this opportunity to throw-out the original C++ codebase, and used Golang in its place. Go allowed us to quickly write new code that was easier to understand and maintain over C++, without completely sacrficing the performance C++ had to offer. In Deflect's infinite creative perspicacity, we called this project Banjax-Go. :)

As we began to decouple Banjax from ATS, we began to think about removing the need for ATS at all, and using NGINX in its place. This idea bloomed into Deflect-next. Deflect-next is written in Python, and is meant to replace most of our existing mitigation software (except for edgemanage). We also used Docker to make deploying and updating Deflect-next edges straight-forward.

As these initiatives enter their final testing and deployment stages, we are also getting ready to release them as opensource software, so that anyone can setup their own mitigation network, maintain their digital voices, and control their own data.

The main Deflect Core components are the following:
- Deflect-Next (Central repository for orchestration scripts and docker images for the Deflect service)
- Core API (A RESTful web API using JSON)
- Edgemanage (Built in Python and used to manage edges in your network)
- Banjax-Go (Central component that cerves challenges to traffic or bans malicious traffic, available as a standalone, or also included in Deflect-Next)

## Purpose
[Distributed Denial of Service (DDoS)](https://en.wikipedia.org/wiki/Denial-of-service_attack#Distributed_attack "Distributed Denial of Service (DDoS)") has become a cheap and common way to shut down legitimate voices. Deflect tries to tilt the balance back in favour of freedom of expression.

Deflect aims at making it easier to set up an infrastructure capable to absorb large volumes of HTTP traffic without having to subscribe to expensive commercial services or buy specialised infrastructure. It also allows you to keep control of your data and therefore respect visitors' privacy.

## Who is it for?
Civil society organisations wanting to defend their and their partners' web sites at reasonable cost, with trustworthy software and while safeguarding privacy. Many organisations have emphasised the importance not to sacrifice privacy for DDoS protection. By running your own Deflect, there will be no third-party middleman to your web traffic.


<a rel="license" href="http://creativecommons.org/licenses/by/4.0/">
<img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/80x15.png" /></a><br />
This work is copyright (c) 2020, eQualit.ie inc., and is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

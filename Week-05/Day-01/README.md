# Week 05 - Day 01 - Networking, URLs & HTTP Basics

**Date:** 2026-08-23

## Overview

Learned the basics of how devices communicate over the Internet, how URLs are structured, and how HTTP requests and responses work between clients and servers.

## Topics Covered

- Internet vs Web
- Client and server
- Public and private IP
- DNS and routing
- URL structure
- Ports and localhost
- HTTP request and response
- GET and POST
- Status codes
- Browser DevTools

## Key Concepts

### Networking

- **Private IP** → used inside the local network
- **Public IP** → identifies the network on the Internet
- **DNS** → converts a domain name to an IP address
- **Hop** → a router the request passes through

### URL Structure

```text
https://example.com:443/products?id=10#details
```

```text
https       → protocol
example.com → domain
443         → port
/products   → path
?id=10      → query
#details    → fragment
```

### Localhost

```text
http://localhost:8000
```

- `localhost` → current computer
- `8000` → port used by the local server

### HTTP

```text
Client → Request → Server
Client ← Response ← Server
```

Common methods:

```text
GET  → retrieve data
POST → send data
```

Common status codes:

```text
200 → success
404 → not found
```

## Labs Performed

### Inspect Your Network

```bash
ipconfig
tracert google.com
```

Checked local IP, gateway, hops, and latency.

### URL Breakdown

Identified:

- Protocol
- Domain
- Port
- Path
- Query
- Fragment

### Local Web Server

```bash
python -m http.server 8000
```

Opened:

```text
http://localhost:8000
```

### Inspect Browser Network Traffic

Used:

```text
DevTools → Network
```

Checked method, URL, headers, status, and response time.

### Send Requests Manually

Used `curl` to send GET and POST requests and compare them with browser requests.

## Quick Review

- Internet → network infrastructure
- Web → service that uses the Internet
- DNS → domain to IP
- Port → identifies a service
- `localhost` → current computer
- GET → retrieve data
- POST → send data
- 200 → success
- 404 → not found
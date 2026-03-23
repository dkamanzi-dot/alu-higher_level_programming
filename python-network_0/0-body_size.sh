#!/bin/bash
# sends a request to a URL and siplays the size of the body in bytes
curl -s "$1" | wc -c

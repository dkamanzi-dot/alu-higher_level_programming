#!/bin/bash
# Sends a GET request with a custom header and displays the response body
curl -sG "$1" -H "X-School-User-Id: 98"

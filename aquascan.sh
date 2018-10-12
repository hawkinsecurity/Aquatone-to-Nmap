#!/bin/bash
python parseip.py
nmap -T4 -F -iL "iplist.txt"
done
# Aquatone --> Nmap

A simple parsing script which takes unique ips from the "hosts.json" file output from aquatone, numerically orders, and places them into a file called "iplist.txt". The parsing and scanning of the ips can be done in a single step by running the bash script, modifying the nmap scan flags as needed.

**Example usage(Standalone python script):**  
`python parseip.py`  

**Example usage(Bash Script):**  
`chmod +x ./aquascan.sh`  
`./aquascan.sh` 



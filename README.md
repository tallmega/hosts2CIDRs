# hosts2CIDRs.py
Make an educated guess at valid internal network CIDRs based on name resolution results for a list of hostnames.

From a loot directory with a JSON list of Active Directory hosts, run:
jq '.[].attributes.dNSHostName[]?' domain_computers.json | sed -e 's/^"//' -e 's/"$//' > hosts.txt

Then just run:
python3 hosts2CIDRs.py hosts.txt


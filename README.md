# .ch-mailsearch
Check deliverability of a specific mail address from the public .ch zonefile

## Setup
* Setup https://github.com/amaurymartiny/check-if-email-exists as an http-Server
* Install python requirements
* Make sure your IP isn't blacklisted (check online)
* Change `from_email`, `hello_name` (and if needed set proxy) and the address to search for `'info@' + domain`
* Get the public .ch Zonefile: https://www.switch.ch/de/open-data/#tab-c5442a19-67cf-11e8-9cf6-5254009dc73c-3
* Create a uniq domain list of it: `grep $'IN\tNS' ch.txt | awk '{print $1}' | uniq > ch_domain_uniq.txt`
* Start script and enjoy: `python3 search.py ch_domain_uniq.txt` (takes a while, tip: split domain file)

## Credits
amaurymartiny
pesc


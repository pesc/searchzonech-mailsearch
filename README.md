# .ch-mailsearch
Check deliverability of a specific mail address of all domains from the public .ch zone file

## 🤔 Why?
This is a research example on how to use the new public .ch zonefile. 
This should not be used to get addresses for spam or phishing!

This script is just a POC: code could be improved...feel free to contribute/fork

## Setup
* Setup https://github.com/amaurymartiny/check-if-email-exists as an http-Server
* Install python requirements
* Make sure your IP isn't blacklisted (check online) and port 25 isn't blocked (mostly for private ISP) -> use proxy 
* Change `from_email`, `hello_name` (and if needed set proxy) and the address to search for `'info@' + domain`. Make sure SPF isn't strict on the address used or add the IP to your test domain.
* Get the public .ch zone file: https://www.switch.ch/de/open-data/#tab-c5442a19-67cf-11e8-9cf6-5254009dc73c-3
* Create a uniq domain list of it: `grep $'IN\tNS' ch.txt | awk '{print $1}' | uniq > ch_domain_uniq.txt`
* Start script and enjoy: `python3 search.py ch_domain_uniq.txt` (takes a while, tip: split domain file)

## Results
| Date          | Number of valid info@ addresses           | 
| ------------- |:-------------:|
| 06.01.2021     | ? |

## Credits
- @amaurymartiny (For the check-if-email-exists)
- @pesc


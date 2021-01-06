import json
import logging
import sys

import dns.resolver
import requests

url = 'http://localhost:3000'
headers = {'content-type': 'application/json'}
logging.basicConfig(filename='domainresearch.log', level=logging.INFO)


def check_mx(domain):
    try:
        for mxrecords in dns.resolver.resolve(domain, 'MX'):
            str(mxrecords.exchange)
            logging.debug("Valid answer for " + domain)
            return True
    except dns.resolver.NoAnswer:
        logging.debug("No answer for " + domain)
        return False
    except dns.resolver.NXDOMAIN:
        logging.debug("NXDOMAIN for " + domain)
        return False
    except dns.resolver.NoNameservers:
        logging.debug("No NS for " + domain)
        return False
    except:
        logging.debug("Other error for " + domain)
        return False


def open_file(filename):
    try:
        with open(filename) as file:
            return file.read().splitlines()
    except OSError as err:
        print("OS error: {0}".format(err))
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise


def check_mail(domain):
    used_mx = ''
    domain = domain[:-1]
    logging.debug('Iterate over: ' + domain)
    if not check_mx(domain):
        logging.info('Error: MX is not valid for ' + domain)
        return
    logging.debug('MX is valid for ' + domain)
    email = 'info@' + domain
    payload = {'to_emails': [email], 'from_email': 'changeme@changeit!.ch', 'hello_name': 'mail.changeit!.ch'}
    logging.debug('Checking mailserver for ' + email)
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    json_response = json.loads(response.text)
    try:
        try:
            if "SmtpError" in json_response[0]['smtp']['error']['type']:
                logging.info(
                    "Error: SMTP error for " + domain + " because of " + json_response[0]['smtp']['error']['message'])
                return
        except KeyError:
            pass
        if json_response[0]['smtp']['is_deliverable']:
            logging.debug('MX accepts mails for ' + email)
            logging.info("Valid: " + email)
            try:
                used_mx = json_response[0]['mx']['records'][0]
                logging.debug("MX used for SMTP " + used_mx)
            except KeyError:
                pass
            print(email + "\t" + used_mx, file=open("valid_emails.txt", "a"))
    except KeyError:
        logging.info("Error: JSON error for " + domain + json.dumps(json_response, indent=3))
        return


def main():
    logging.info("Starting")
    filename = sys.argv[1]
    domains = open_file(filename)
    for domain in domains:
        check_mail(domain)


if __name__=="__main__":
    main()

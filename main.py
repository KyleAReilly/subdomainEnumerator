
import requests
import sys

sub_list = open("subdomains20000.txt").read()
subdoms = sub_list.splitlines()

domain = input("What domain would you like to enumerate?:  ")
for sub in subdoms:
    sub_domains = f"http://{sub}.{domain}" # can also use sys.argv[1] instead of domain to type it all in one command

    try:
        requests.get(sub_domains)

    except requests.ConnectionError:
        pass

    else:
        print("Valid domain: ", sub_domains)

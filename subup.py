import requests #pip install requests
import socket, argparse, sys
import prettytable #pip install prettytable

#Coded by: Abdullah AlZahrani

print('''
 _____         _      _   _ ______ 
/  ___|       | |    | | | || ___ \\
\ `--.  _   _ | |__  | | | || |_/ /
 `--. \| | | || '_ \ | | | ||  __/ 
/\__/ /| |_| || |_) || |_| || |    
\____/  \__,_||_.__/  \___/ \_|    
''')

parser = argparse.ArgumentParser(description="[--] SubUP")
parser.add_argument('-d', required=True, default=None, help='Enter domain name.')
args = vars(parser.parse_args())

if len(sys.argv) == 1:
    sys.exit("[!] Usage: python3 subup.py -e example.com")

domain = args['d']

def getSubDomainsAndChcekWhoIsUP():
    print('> Domain: {}'.format(domain))
    table = prettytable.PrettyTable(["Subdomain", "IP", "Status"])
    req = requests.get('https://api.hackertarget.com/hostsearch/?q={}'.format(domain)).text
    for subdomains in req.splitlines():
        subdomain = subdomains.replace(',', ' ').split()
        # The code below was written by 1337r00t from script WebAlive (https://github.com/1337r00t/WebAlive).
        try:
            isHTTP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            isHTTP.settimeout(1.5)
            isHTTPS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            isHTTPS.settimeout(1.5)
            http = isHTTP.connect_ex((subdomain[0], 80)) == 0
            https = isHTTPS.connect_ex((subdomain[0], 443)) == 0
            isHTTP.close()
            isHTTPS.close()
        except:
            http, https = False, False
        if http or https:
            table.add_row([subdomain[0], subdomain[1], "UP"])
        else:
            table.add_row([subdomain[0], subdomain[1], "Down"])
    print(table)

if __name__ == '__main__':
    getSubDomainsAndChcekWhoIsUP()

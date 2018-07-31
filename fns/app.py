# -*- coding: utf-8 -*-

import requests

protocol = 'https://'
host = 'proverkacheka.nalog.ru'
port = '9999'
users_part = '/v1/mobile/users'

registration_url = protocol + host + ':' + port + users_part + '/signup'
login_url = protocol + host + ':' + port + users_part + '/login'
restore_url = protocol + host + ':' + port + users_part + '/restore'
check_url = protocol + host + ':' + port + '/v1/ofds/*/inns/*/fss/%s/operations/1/tickets/%s?fiscalSign=%s&date=%s&sum=%s'
revise_url = protocol + '%s:%s@' + host + ':' + port + '/v1/inns/*/kkts/*/fss/%s/tickets/%s?fiscalSign=%s&sendToEmail=no'

header = {
    'Device-Id': 'faec4ab7323c4fc291625bd8a7d36fd8',
    'Device-OS': 'Android 6.0.1',
    'Version': '2',
    'ClientVersion': '1.4.2',
    'User-Agent': 'okhttp/3.0.1'
}

def check_receipt(receipt):
    url = check_url % (receipt.fn, receipt.fp, receipt.fd, receipt.purchase_date, receipt.total)
    response = requests.get(url)
    return response

def revise_info(receipt, login, password):
    url = revise_url % (login, password, receipt.fn, receipt.fp, receipt.fd)
    response = requests.get(url, headers = header)
    return response


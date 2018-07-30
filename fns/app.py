# -*- coding: utf-8 -*-

import requests

host = 'https://proverkacheka.nalog.ru'
port = '9999'
users_part = '/v1/mobile/users'

registration_url = host + ':' + port + users_part + '/signup'
login_url = host + ':' + port + users_part + '/login'
restore_url = host + ':' + port + users_part + '/restore'
check_url = host + ':' + port + '/v1/ofds/*/inns/*/fss/%s/operations/1/tickets/%s?fiscalSign=%s&date=%s&sum=%s'
revise_url =host + ':' + port + '/v1/inns/*/kkts/*/fss/%s/tickets/%s?fiscalSign=%s&sendToEmail=no'

header = {
    'Device-Id': '',
    'Device-OS': '',
}

def check_receipt(receipt):
    url = check_url % (receipt.fn, receipt.fp, receipt.fd, receipt.purchase_date, receipt.total)
    response = requests.get(url)
    return response

def revise_info(receipt, login, password):
    url = revise_url % (receipt.fn, receipt.fp, receipt.fd)
    response = requests.get(url, auth = (login, password), headers = header)
    return response


# -*- coding: utf-8 -*-

__version__ = '0.0.1'

from fns.app import check_receipt, revise_info

class Receipt:
    def __init__(self, fn, fp, fd, purchase_date=None, total=None):
        self.fn = fn
        self.fp = fp
        self.fd = fd
        self.purchase_date = purchase_date
        self.total = total


class Response:
    pass

#!/usr/bin/python3.7

import json
from src.libs.master_setup import master_setup, unpack_d
from src.libs.setup_top import get_top
from src.libs.send_req import SendRequest


class GetBalance(object):

    def __init__(self):
        machine = 1     #   machine = 1   # 1 for west, 0 for kathy

        settings_d, sender_etc_dd, self.receivers = master_setup(machine)
        self.chain, self.url3, self.sender, self.pw = unpack_d(settings_d, sender_etc_dd)
        self.remark = "get balance"
        self.asset = 1
        self.id = 99999

    def get_account_balance(self):
        method_nm = "getAccountBalance"
        for receiver in self.receivers:
            p_list = [self.chain, self.chain, self.asset, receiver]
            request = get_top(method_nm, p_list, self.url3)
            response = SendRequest.send_request(request)
            results_d, rstr = json.loads(response.text)

            total_balance = results_d.get("totalBalance")
            print("totalBalance: " + receiver + ":  " + str(total_balance))


if __name__ == "__main__":
    c = GetBalance()
    c.get_account_balance()

#!/usr/bin/python3.7

import requests
from src.libs.send_req import SendRequest
from src.user_inputs.inputs import Inputs
from src.libs.setup_log import SetupLogging
from src.user_inputs.settings_set import SettingsSet
from src.libs.setup_top import SetupTop

class GetBalance(object):
    # http://bin-hex-converter.online-domain-tools.com/

    def __init__(self):
        machine = 1

        SetupLogging()
        st_obj = SettingsSet()   # 1 for west, 0 for kathy
        settings = st_obj.settings_set(machine)     #   machine = 1   # 1 for west, 0 for kathy

        self.chainId = settings.get('chain')
        self.url = settings.get('url')
        self.pw = settings.get('pw')
        self.sender = accts.get('sender')
        self.contract = accts.get('contract_address')
        # self.receiver = accts.get('receiver') # get from inputs
        self.remark = "student account"

    def get_account_balance(self):
        st_obj = SetupTop()

        inputs = Inputs.inputlist
        for receiver in inputs:
            method_nm = "getAccountBalance"
            p_list = [self.chainId, self.chainId, 1, "TTbKRT4vrHMQdyQCATrdu6godeo1FJWSFVVk"]
            request = st_obj.setup_top(method_nm, p_list, self.url)
            resp1 = SendRequest.send_request(request)
            results_d = resp1.get("result")

            total_balance = results_d.get("totalBalance")
            print("totalBalance: " + receiver + ":  " + str(total_balance))


if __name__ == "__main__":
    c = GetBalance()
    c.get_account_balance()

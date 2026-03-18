from brownie import FundMe
from scripts.helpful_scripts import get_account

def deploy_fund_me():
    accounts = get_account()
    fund_me = FundMe.deploy({"from": accounts})
    print(f"contract deployed to {fund_me.address}")



def main ():
    deploy_fund_me()
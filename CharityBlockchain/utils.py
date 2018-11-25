from web3 import Web3, HTTPProvider
from web3.eth import Eth
from web3.utils.encoding import to_text, to_hex

class BlockChain:

    def __init__(self):
        self.acid=list(range(100))
        self.iacid=0
        self.count = 10
        self.web = Web3(HTTPProvider('http://localhost:8545'))
        self.accounts = self.web.eth.accounts

    def connect_chain(self):
        return self.web

    def get_account(self,web3):
        return self.accounts

    def doTrans(self,account1, account2, money, tex=""):
        baccount1 = self.account_s(account1)
        baccount2 = self.account_s(account2)

        payload = {
            'from':self.accounts[baccount1],
            'to':self.accounts[baccount2],
            'value':to_hex(str.encode(str(money))),
            'data':to_hex(str.encode(tex))
            }
        hash = self.web.eth.sendTransaction(payload)
        self.web.eth.waitForTransactionReceipt(hash)
        text_hash=repr(hash)
        text_hash=text_hash[text_hash.find("'")+1:text_hash.rfind("'")]
        return text_hash

    def getTrans(self,hash):
        payload = self.web.eth.getTransection(hash)
        payload.input=to_tex(payload.input)
        return payload

    def checkBalance(self,account):
        baccount = self.account_s(account)
        balance = self.web.eth.getBalance(accounts[account], 'latest')
        return balance

    def get_newaccount(self):
        self.count=self.count+1
        return self.count

    def account_s(self, id):
        tmp=self.iacid
        self.iacid+=1
        return tmp


def createBlockChain():
    return BlockChain()
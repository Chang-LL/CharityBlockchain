from web3 import Web3, HTTPProvider
from web3.eth import Eth
from web3.utils.encoding import to_tex, to_hex

class BlockChain:
    count = 10
    web3 = Web3(HTTPProvider('http://localhost:8545'))
    accounts = web3.eth.accounts

    def connect_chain():
        return web3

    def get_account(web3):
        return accounts

    def doTrans(account1, account2, money, tex):
        baccount1 = account_s(account1)
        baccount2 = account_s(account2)

        payload = {
            'from':block_account[baccount1],
            'to':block_account[baccount2],
            'value':money,
            'data':to_hex(str.encode(tex))
            }
        hash = web3.eth.sendTransaction(payload)
        web3.eth.waitForTransactionReceipt(tx_hash)
        return hash

    def getTrans(hash):
        payload = web3.eth.getTransection(hash)
        payload.input=to_tex(payload.input)
        return payload

    def checkBalance(account):
        baccount = account_s(account)
        balance = web3.eth.getBalance(accounts[account], 'latest')
        return balance

    def get_newaccount():
        count=count+1
        return count

    def account_s():
        return 11

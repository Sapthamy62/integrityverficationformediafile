from web3 import Web3
from solcx import compile_standard
import solcx
import json

provider_url="http://127.0.0.1:8545"
w3=Web3(Web3.HTTPProvider(provider_url))

 
goerli_chain=5

w3.eth.default_account=w3.eth.accounts[0]

contractAddress=w3.toChecksumAddress('0x164d0d6c13C59E20913B8DEDdd0236839676eD81')
abi=json.loads('[{"inputs": [{"internalType": "uint256", "name": "y", "type": "uint256"}, {"internalType": "string", "name": "m", "type": "string"}], "name": "addfile", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "string", "name": "str1", "type": "string"}, {"internalType": "string", "name": "str2", "type": "string"}], "name": "compare", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "stateMutability": "pure", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "name": "files", "outputs": [{"internalType": "uint256", "name": "id", "type": "uint256"}, {"internalType": "string", "name": "hash", "type": "string"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "message", "outputs": [{"internalType": "string", "name": "", "type": "string"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "messagevalue", "outputs": [{"internalType": "string", "name": "", "type": "string"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "y", "type": "uint256"}, {"internalType": "string", "name": "m", "type": "string"}], "name": "verify", "outputs": [], "stateMutability": "nonpayable", "type":"function"}]')

contract_instance=w3.eth.contract(address=contractAddress,abi=abi)

transaction_index=1
def Addblock(id,hash):
    global transaction_index

    tx_hash=contract_instance.functions.addfile(id,hash).transact()
    w3.eth.wait_for_transaction_receipt(tx_hash)
def verify(id,hash):
   print("hai")    
   global transaction_index
   verify_transaction=contract_instance.functions.verify(id,hash).transact()

   w3.eth.wait_for_transaction_receipt(verify_transaction)
   status=contract_instance.functions.messagevalue().call()
   return status
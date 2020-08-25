import json
from web3 import Web3
abi=json.loads('''[
	{
		"constant": false,
		"inputs": [
			{
				"name": "toVoter",
				"type": "address"
			}
		],
		"name": "register",
		"outputs": [],
		"payable": true,
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "winningProposal",
		"outputs": [
			{
				"name": "_winningProposal",
				"type": "uint8"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "toProposal",
				"type": "uint8"
			}
		],
		"name": "vote",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "ad",
				"type": "address"
			}
		],
		"name": "getVoterDetails",
		"outputs": [
			{
				"name": "weight",
				"type": "uint256"
			},
			{
				"name": "vote",
				"type": "uint8"
			},
			{
				"name": "voted",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"name": "_numProposals",
				"type": "uint8"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"payable": true,
		"stateMutability": "payable",
		"type": "fallback"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"name": "a",
				"type": "uint256"
			}
		],
		"name": "voting",
		"type": "event"
	}
]''')
bytecode="60806040526000805534801561001457600080fd5b506040516020806107028339810180604052810190808051906020019092919050505060008160ff1611151561004957600080fd5b33600160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055506002806000600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600001819055508060ff166003816101049190610112565b504260048190555050610165565b81548183558181111561013957818360005260206000209182019101610138919061013e565b5b505050565b61016291905b8082111561015e5760008082016000905550600101610144565b5090565b90565b61058e806101746000396000f300608060405260043610610062576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff1680634420e48614610064578063609ff1bd1461009a578063b3f98adc146100cb578063ba71bef0146100fb575b005b610098600480360381019080803573ffffffffffffffffffffffffffffffffffffffff16906020019092919050505061016a565b005b3480156100a657600080fd5b506100af610366565b604051808260ff1660ff16815260200191505060405180910390f35b3480156100d757600080fd5b506100f9600480360381019080803560ff1690602001909291905050506103e2565b005b34801561010757600080fd5b5061013c600480360381019080803573ffffffffffffffffffffffffffffffffffffffff1690602001909291905050506104e4565b604051808481526020018360ff1660ff16815260200182151515158152602001935050505060405180910390f35b600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff161415156101c657600080fd5b600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff1614158061026f5750600260008273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060010160009054906101000a900460ff165b1561027957610363565b6001600260008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600001819055506000600260008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060010160006101000a81548160ff0219169083151502179055507ffd4a77f1234b0c1b8a5a3447592736ea79ff8a51f527882f0353787f4e642974600080815480929190600101919050556040518082815260200191505060405180910390a15b50565b6000806000809150600090505b6003805490508160ff1610156103dd578160038260ff1681548110151561039657fe5b906000526020600020016000015411156103d05760038160ff168154811015156103bc57fe5b906000526020600020016000015491508092505b8080600101915050610373565b505090565b6000600260003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020905060018160010160019054906101000a900460ff1660ff1614801561045857508060010160009054906101000a900460ff16155b8061046a57506003805490508260ff16105b151561047557600080fd5b60018160010160006101000a81548160ff021916908315150217905550818160010160016101000a81548160ff021916908360ff160217905550806000015460038360ff168154811015156104c657fe5b90600052602060002001600001600082825401925050819055505050565b600080600080600260003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000209050806000015493508060010160019054906101000a900460ff1692508060010160009054906101000a900460ff1691505091939092505600a165627a7a7230582077e804fca19bd9a6cd69d86446f99990ce0722e7a7330496742313fb8f9e0a980029"

def vote(address):
	key=input("Enter private key")
	account=web3.eth.account.privateKeyToAccount(key)
	account_addr=account.address
	web3.eth.defaultAccount=account_addr
	ballot=web3.eth.contract(address=address,abi=abi)
	proposal=int(input("Enter which proposal you want to vote for to"))
	tx_hash=ballot.functions.vote(proposal).transact()
	web3.eth.waitForTransactionReceipt(tx_hash)

def findWinner(address):
	key=input("Enter private key")
	account=web3.eth.account.privateKeyToAccount(key)
	account_addr=account.address
	web3.eth.defaultAccount=account_addr
	ballot=web3.eth.contract(address=address,abi=abi)
	print(ballot.functions.winningProposal().call())

def getVoterD(address):
	key=input("Enter private key")
	account=web3.eth.account.privateKeyToAccount(key)
	account_addr=account.address
	web3.eth.defaultAccount=account_addr
	ballot=web3.eth.contract(address=address,abi=abi)
	print(ballot.functions.getVoterDetails(account_addr).call())

def main():
	print("Welcome To the interface")
	url="HTTP://127.0.0.1:7545"
	global web3
	web3=Web3(Web3.HTTPProvider(url))
	print(web3.isConnected())
	while 1:
		c=int(input('''Enter your Choice here
			1. Vote
			2. Get Voter Details
			3. Find Winner'
			4. Exit'''))
		if c==1:
			address=input("Address of the Smart Contract")
			vote(address)
		if c==2:
			address=input("Address of the Smart Contract")
			getVoterD(address)
		if c==3:
			address=input("Address of the Smart Contract")
			findWinner(address)
		else:
			exit()

if __name__=="__main__":
	main()

from web3 import Web3

# Alchemy/Infura API URL
ALCHEMY_URL = 'https://eth-mainnet.g.alchemy.com/v2/uI91Q_EThRyvO2cVbVQ3nsDeMEYeX0DC'
# Beacon deposit contract address
BEACON_DEPOSIT_CONTRACT = '0x00000000219ab540356cBB839Cbe05303d7705Fa'

# Connect to Ethereum node
w3 = Web3(Web3.HTTPProvider(ALCHEMY_URL))

# Check if the connection is successful
if w3.is_connected():
    print("Connected to Ethereum")
else:
    print("Failed to connect")

latest_block = w3.eth.get_block('latest')

# Print the block number and transaction count
print(f"Latest Block Number: {latest_block['number']}")
print(f"Number of Transactions in Block: {len(latest_block['transactions'])}")

def track_deposits():
    # Fetch the latest block
    latest_block = w3.eth.get_block('latest', full_transactions=True)
    
    # Loop through each transaction
    for tx in latest_block['transactions']:
        # Check if the transaction is sent to the Beacon Deposit Contract
        if tx['to'] == BEACON_DEPOSIT_CONTRACT:
            print(f"Deposit detected! Tx Hash: {tx['hash'].hex()}")
            print(f"From: {tx['from']}, Value: {w3.fromWei(tx['value'], 'ether')} ETH")
            print(f"Gas Fee: {w3.fromWei(tx['gasPrice'] * tx['gas'], 'ether')} ETH")

# Call the function
track_deposits()

import time

def monitor_deposits():
    print("Starting deposit monitor...")

    while True:
        try:
            track_deposits()
        except Exception as e:
            print(f"Error: {e}")
        
        # Wait for 15 seconds before checking the next block
        time.sleep(15)

monitor_deposits()

def log_deposit(tx):
    with open('deposits.txt', 'a') as f:
        f.write(f"Tx Hash: {tx['hash'].hex()}\n")
        f.write(f"From: {tx['from']}, Value: {w3.fromWei(tx['value'], 'ether')} ETH\n")
        f.write(f"Block: {tx['blockNumber']}, Gas Fee: {w3.fromWei(tx['gasPrice'] * tx['gas'], 'ether')} ETH\n")
        f.write(f"----------------------------\n")

def track_deposits():
    latest_block = w3.eth.get_block('latest', full_transactions=True)
    
    for tx in latest_block['transactions']:
        if tx['to'] == BEACON_DEPOSIT_CONTRACT:
            print(f"Deposit detected! Tx Hash: {tx['hash'].hex()}")
            log_deposit(tx)

monitor_deposits()

import logging

# Configure logging
logging.basicConfig(filename='tracker.log', level=logging.INFO)

def track_deposits():
    try:
        latest_block = w3.eth.get_block('latest', full_transactions=True)
        
        for tx in latest_block['transactions']:
            if tx['to'] == BEACON_DEPOSIT_CONTRACT:
                logging.info(f"Deposit detected! Tx Hash: {tx['hash'].hex()}")
                log_deposit(tx)
    except Exception as e:
        logging.error(f"Error occurred: {e}")

monitor_deposits()















**Setup Guide**
**1. Environment Configuration**
Install Python 3.10+:
Ensure that Python 3.10 or above is installed on your system. You can download Python from here.

Create a Virtual Environment (Optional but recommended):
To avoid conflicts between packages, you should use a virtual environment.

**CODE**
python -m venv venv
venv\Scripts\activate  # Windows
pip install web3 

**API Setup:**
You'll need an Alchemy API key for interacting with the Ethereum blockchain.

**API KEY**
ALCHEMY_URL = 'https://eth-mainnet.g.alchemy.com/v2/uI91Q_EThRyvO2cVbVQ3nsDeMEYeX0DC'

**Code Explanation**
Here’s a breakdown of the key sections in the tracker.py file:

Connection to Ethereum Node:
This uses the Alchemy API to connect to the Ethereum mainnet.

CODE:
w3 = Web3(Web3.HTTPProvider(ALCHEMY_URL))
Tracking Latest Block:
Fetches the latest block on the Ethereum network.

CODE:
latest_block = w3.eth.get_block('latest')
Monitor for Beacon Deposits:
Continuously monitors blocks for transactions sent to the Beacon Deposit Contract.

CODE:
def monitor_deposits():
    while True:
        track_deposits()
        time.sleep(15)  # Wait for 15 seconds
Logging System:
The application logs transaction details, including gas fees, transaction hash, and from which account the deposit originated.

CODE:
logging.basicConfig(filename='tracker.log', level=logging.INFO)
Error Handling:
Catches and logs any exceptions.

CODE:
except Exception as e:
    logging.error(f"Error occurred: {e}")

**OUTPUT:**
python tracker.py
Connected to Ethereum
Latest Block Number: 20719963
Number of Transactions in Block: 138
Starting deposit monitor...
Deposit detected! Tx Hash: 0xabc123...
From: 0xdef456, Value: 32.0 ETH
Gas Fee: 0.01 ETH


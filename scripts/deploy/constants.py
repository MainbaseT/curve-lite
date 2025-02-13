from eth_utils import keccak

from settings.config import RollupType

ADDRESS_PROVIDER_MAPPING = {
    2: "Exchange Router",
    4: "Fee Distributor",
    7: "Metaregistry",
    11: "TricryptoNG Factory",
    12: "StableswapNG Factory",
    13: "TwocryptoNG Factory",
    18: "Spot Rate Provider",
    19: "CRV Token",
    20: "Gauge Factory",
    21: "Ownership Admin",
    22: "Parameter Admin",
    23: "Emergency Admin",
    24: "CurveDAO Vault",
    25: "crvUSD Token",
    26: "Deposit and Stake Zap",
    27: "Stableswap Meta Zap",
}
MULTICALL3_ADDRESS = "0xcA11bde05977b3631167028862bE2a173976CA11"
CREATE2_SALT = keccak(42069)
CREATE2DEPLOYER_ADDRESS = "0x13b0D85CcB8bf860b6b79AF3029fCA081AE9beF2"
CREATE2DEPLOYER_ABI = """
[
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "internalType": "address",
          "name": "previousOwner",
          "type": "address"
        },
        {
          "indexed": true,
          "internalType": "address",
          "name": "newOwner",
          "type": "address"
        }
      ],
      "name": "OwnershipTransferred",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": false,
          "internalType": "address",
          "name": "account",
          "type": "address"
        }
      ],
      "name": "Paused",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": false,
          "internalType": "address",
          "name": "account",
          "type": "address"
        }
      ],
      "name": "Unpaused",
      "type": "event"
    },
    {
      "inputs": [
        {
          "internalType": "bytes32",
          "name": "salt",
          "type": "bytes32"
        },
        {
          "internalType": "bytes32",
          "name": "codeHash",
          "type": "bytes32"
        }
      ],
      "name": "computeAddress",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "bytes32",
          "name": "salt",
          "type": "bytes32"
        },
        {
          "internalType": "bytes32",
          "name": "codeHash",
          "type": "bytes32"
        },
        {
          "internalType": "address",
          "name": "deployer",
          "type": "address"
        }
      ],
      "name": "computeAddressWithDeployer",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "pure",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "value",
          "type": "uint256"
        },
        {
          "internalType": "bytes32",
          "name": "salt",
          "type": "bytes32"
        },
        {
          "internalType": "bytes",
          "name": "code",
          "type": "bytes"
        }
      ],
      "name": "deploy",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "value",
          "type": "uint256"
        },
        {
          "internalType": "bytes32",
          "name": "salt",
          "type": "bytes32"
        }
      ],
      "name": "deployERC1820Implementer",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address payable",
          "name": "payoutAddress",
          "type": "address"
        }
      ],
      "name": "killCreate2Deployer",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "owner",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "pause",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "paused",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "renounceOwnership",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "newOwner",
          "type": "address"
        }
      ],
      "name": "transferOwnership",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "unpause",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "stateMutability": "payable",
      "type": "receive"
    }
  ]
"""
ZERO_ADDRESS = "0x0000000000000000000000000000000000000000"


ETHEREUM_ADMINS = (
    "0x40907540d8a6C65c637785e8f8B742ae6b0b9968",  # Ownership
    "0x4EEb3bA4f221cA16ed4A0cC7254E2E32DF948c5f",  # Parameter
    "0x467947EE34aF926cF1DCac093870f613C96B1E0c",  # Emergency
)

BROADCASTERS = {
    RollupType.op_stack: "0xE0fE4416214e95F0C67Dc044AAf1E63d6972e0b9",
    RollupType.polygon_cdk: "0xB5e7fE8eA8ECbd33504485756fCabB5f5D29C051",
    RollupType.arb_orbit: "0x94630a56519c00Be339BBd8BD26f342Bf4bd7eE0",
}

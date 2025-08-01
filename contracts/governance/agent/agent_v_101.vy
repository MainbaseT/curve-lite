# pragma version 0.4.0
"""
@title Agent
@author CurveFi
@license MIT
@custom:version 1.0.1
"""

version: public(constant(String[8])) = "1.0.1"

interface IAgent:
    def execute(_messages: DynArray[Message, MAX_MESSAGES]): nonpayable
    def RELAYER() -> address: view


struct Message:
    target: address
    data: Bytes[MAX_BYTES]


flag Agent:
    OWNERSHIP
    PARAMETER
    EMERGENCY


MAX_BYTES: constant(uint256) = 1024
MAX_MESSAGES: constant(uint256) = 8


RELAYER: public(immutable(address))


@deploy
def __init__():
    RELAYER = msg.sender


@external
def execute(_messages: DynArray[Message, MAX_MESSAGES]):
    """
    @notice Execute a sequence of messages.
    @param _messages An array of messages to be executed.
    """
    assert msg.sender == RELAYER

    for message: Message in _messages:
        raw_call(message.target, message.data)

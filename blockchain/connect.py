# -*- coding: utf-8 -*-
#
# Project name: NynjaWalletPy
# File name: connect
# Created: 2018-07-13
#
# Author: Liubov M. <liubov.mikhailova@gmail.com>

from web3 import Web3
from web3.middleware import geth_poa_middleware

INFURA_KEY = 'oktMAwsvSx2C8gaSg2mg'
NETWORK_NAME = 'rinkeby'
# ENDPOINT_TEMPLATE = 'https://{0}.infura.io/{1}'
ENDPOINT_TEMPLATE = 'https://rinkeby.infura.io/oktMAwsvSx2C8gaSg2mg'

rinkeby_connection = None


def connect_to_blockchain():
    """
    Connect to blockchain network
    """
    Endpoint = ENDPOINT_TEMPLATE.format(NETWORK_NAME, INFURA_KEY)
    w3 = Web3(Web3.HTTPProvider(Endpoint))
    w3.middleware_stack.inject(geth_poa_middleware, layer=0)
    # print(w3.version.node)
    global rinkeby_connection
    rinkeby_connection = w3
    return rinkeby_connection


def get_connection():
    if not rinkeby_connection:
        connect_to_blockchain()
    return rinkeby_connection
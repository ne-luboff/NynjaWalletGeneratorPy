# -*- coding: utf-8 -*-
#
# Project name: NynjaWalletPy
# File name: router
# Created: 2018-07-11
#
# Author: Liubov M. <liubov.mikhailova@gmail.com>

from api.wallet import GenWalletHandler
from handlers import IndexHandler


def get_router():
    return [
        (r"/", IndexHandler),
        (r"/gen", GenWalletHandler)
    ]
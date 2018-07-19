# -*- coding: utf-8 -*-
#
# Project name: NynjaWalletPy
# File name: wallet
# Created: 2018-07-12
#
# Author: Liubov M. <liubov.mikhailova@gmail.com>

import logging
from base import BaseHandler

logger = logging.getLogger(__name__)


class GenWalletHandler(BaseHandler):
    allowed_methods = ('GET', )

    def get(self):
        """
        Render http page with wallet
        """
        logger.info("Wallet/Gen")

        return self.render_html('index.html')
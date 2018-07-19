import datetime

from base import BaseHandler


class IndexHandler(BaseHandler):
    allowed_methods = ('GET', )

    def get(self):
        return self.success({
            "current_time": datetime.datetime.now().isoformat()
        })
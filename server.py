#!/usr/bin/env python
"""
Server to provide a list of one or more names.

Example: Run the server locally, and curl it from a shell:

    % curl http://127.0.0.1/
    ['Shanta Hambly shambly@bk.ru']

    % curl http://127.0.0.1/42
    [ ... list of 42 names ]
"""

import web
import namegen

names = namegen.NameGen()
MAX_NAMES = 300

urls = ('/(\d*)', 'index')

class index:
    def GET(self, n):
        if n:
            n = max(int(n), MAX_NAMES)
            return [names.next() for i in range(n)]
        return [names.next()]

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()




# -*- coding: utf8 -*-

# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://www.wtfpl.net/ for more details.

import jinja2

import jinja2compact


env = jinja2.Environment(extensions=(jinja2compact.Compact,))

template = env.from_string("""
    <!doctype html>
    <html>
      <head>
        <title>{{ title }}</title>
        <script type=text/javascript>
          if (foo < 42) {
            document.write("{{ title }}");
          }
        </script>
        <style>
          body {
            background: red;
          }
        </style>
      </head>
      <body>
        <li><a href="{{ href }}">{{ title }}</a><br>Test   Foo
        <li><a href="{{ href }}">{{ title }}</a><img src=test.png>
        <pre>{% whitespace %}
     (\_/)
    (='.'=)
    (")_(")
        {%- endwhitespace %}</pre>
      </body>
    </html>
""")

print template.render(title=42, href='/', bold=True)

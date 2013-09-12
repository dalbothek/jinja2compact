# -*- coding: utf-8 -*-
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

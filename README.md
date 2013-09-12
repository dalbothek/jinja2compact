# jinja2compact
jinja2compact is a small extension for [mitsuhiko](https://github.com/mitsuhiko)'s brilliant [jinja2](http://jinja.pocoo.org) template engine. It reduces whitespace in your template files at compile time, making them smaller for transport. jinja2compact is heavily inspired by [jinja2-htmlcompress](https://github.com/mitsuhiko/jinja2-htmlcompress) and tries to fix some of its flaws with a much simpler design.

jinja2compact does:
* Reduce multiple consecutive whitespace characters to a single space
* Remove leading whitespace before the doctype declaration in HTML templates

In contrast to [jinja2-htmlcompress](https://github.com/mitsuhiko/jinja2-htmlcompress) this means that:
* A single space between HTML tags is preserved (which is especially desirable in inline context)
* Whitespace around [jinja2](http://jinja.pocoo.org) tags is preserved (no ugly `{{ " " }}`)
* Whitespace is reduced inside all elements, including `script`, `style`, `textarea`, `pre` and so on

## Preserve whitespace
In some cases you might want to disable the extension for individual passages of a template. This is easily achieved with the `{% whitespace %}` tag:
```HTML
{% whitespace %}<pre>
     (\_/)
    (='.'=)
    (")_(") 
</pre>{% endwhitespace %}
```
results in:
```HTML
<pre>
     (\_/)
    (='.'=)
    (")_(") 
</pre>
```

## Usage
jinja2 allows extensions to be passed to the `Environment` constructor:
```python
import jinja2
import jinja2compact

env = jinja2.Environment(extensions=(jinja2compact.Compact,))
``` 

## License
This program is free software. It comes without any warranty, to
the extent permitted by applicable law. You can redistribute it
and/or modify it under the terms of the Do What The Fuck You Want
To Public License, Version 2, as published by Sam Hocevar. See
http://www.wtfpl.net/ for more details.

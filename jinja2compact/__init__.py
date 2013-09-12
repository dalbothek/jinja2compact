# -*- coding: utf8 -*-

# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://www.wtfpl.net/ for more details.

import re

import jinja2
from jinja2 import ext
from jinja2 import lexer


class Compact(ext.Extension):
    WHITESPACE = re.compile("\s+")

    def filter_stream(self, stream):
        verbose_depth = 0
        first = True
        while 1:
            if (
                stream.current.type == 'block_begin' and
                stream.look().value in ('whitespace', 'endwhitespace')
            ):
                stream.next()
                if stream.current.value == 'whitespace':
                    verbose_depth += 1
                else:
                    verbose_depth -= 1
                    if verbose_depth < 0:
                        raise self.error("Unexpected tag 'endverbose'")
                stream.next()
                if stream.current.type != 'block_end':
                    raise self.error(
                        "Unexpected token '%s', expected end of block" %
                        lexer.describe_token(stream.current), stream
                    )
            elif verbose_depth == 0 and stream.current.type == 'data':
                # Reduce all whitespace to a single space
                token = lexer.Token(stream.current.lineno, "data",
                                    self.WHITESPACE.sub(" ", stream.current.value))

                # Special case to remove leading space before the doctype
                # declaration in HTML documents
                if first:
                    first = False
                    if token.value.lower().startswith(" <!doctype "):
                        token = lexer.Token(token.lineno, "data", 
                                            token.value[1:])
                yield token
            else:
                yield stream.current
            stream.next()


    def error(self, message, stream):
        return jinja2.TemplateSyntaxError(
            message, stream.current.lineno, stream.name, stream.filename
        )

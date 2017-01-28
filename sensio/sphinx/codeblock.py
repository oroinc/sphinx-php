"""
    :copyright: (c) 2010-2015 Fabien Potencier
    :license: MIT, see LICENSE for more details.
"""

from sphinx.directives.code import CodeBlock
from docutils.parsers.rst import Directive, directives

"""
A wrapper around the built-in CodeBlock class to always
enable line numbers.
"""
class NumberedCodeBlock(CodeBlock):
    def run(self):
        self.options['linenos'] = 'table'
        return super(NumberedCodeBlock, self).run();

def setup(app):
    directives.register_directive('code-block', NumberedCodeBlock)
    directives.register_directive('sourcecode', NumberedCodeBlock)

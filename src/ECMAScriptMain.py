import sys
import argparse

from antlr4 import *
from antlr4.InputStream import InputStream

from ECMAScriptLexer import ECMAScriptLexer
from ECMAScriptParser import ECMAScriptParser
from ECMAScriptCFG import ECMAScriptCFG
from ECMAScriptLLVMEmitter import ECMAScriptLLVMEmitter


def main (args):
    input_stream = FileStream (args.input_file[0])

    lexer = ECMAScriptLexer (input_stream)
    stream = CommonTokenStream (lexer)
    parser = ECMAScriptParser (stream)
    tree = parser.program ()

    cfg = ECMAScriptCFG (args)
    cfg.visit (tree)

    print cfg.getGraph ()
    while False in [cfg.getGraph ()[func]['done'] for func in [x for x in cfg.getGraph ()]]:
        cfg.visit (tree)
        print cfg.getGraph ()
        print

    emitter = ECMAScriptLLVMEmitter (cfg.getGraph (), args.output_file)
    emitter.visit (tree)

if __name__ == '__main__':
    parser = argparse.ArgumentParser (description='Javascript LLVM Front-End')
    parser.add_argument ('input_file', metavar = 'input', type = str, nargs = 1, help = 'javascript input source code')
    parser.add_argument ('output_file', metavar = 'output', type = str, nargs = '?', default = './', help = 'LLVM IR output file')

    main (parser.parse_args ())

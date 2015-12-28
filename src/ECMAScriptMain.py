import sys

from antlr4 import *
from antlr4.tree.Trees import Trees

import argparse

from ECMAScriptLexer import ECMAScriptLexer
from ECMAScriptParser import ECMAScriptParser
from ECMAScriptListener import ECMAScriptListener
from ECMAScriptCFG import ECMAScriptCFG
#from ECMAScriptLLVMEmitter import LLVMEmitter
from ECMAScriptLLVMEmitter import *

def main (args):
    input_f = FileStream (args.input_file[0]);
    lexer = ECMAScriptLexer (input_f);
    stream = CommonTokenStream (lexer);

    parser = ECMAScriptParser (stream);
    tree = parser.program ();

    cfg = ECMAScriptCFG (args)
    walker = ParseTreeWalker ()
    walker.walk (cfg, tree)

    #while False not in [x['done'] for x in cfg.getGraph ()]:
    '''while 1:
        if False not in [cfg.getGraph ()[func]['done'] for func in [x for x in cfg.getGraph ()]]:
            break'''
    while False in [cfg.getGraph ()[func]['done'] for func in [x for x in cfg.getGraph ()]]:
        walker.walk (cfg, tree)
    print (cfg.getGraph ())

    emitter = LLVMEmitter (cfg.getGraph (), args.output_file)
    walker.walk (emitter, tree)

    #for func in module.functions:
    #	func.viewCFG ()

if __name__ == '__main__':
    parser = argparse.ArgumentParser (description='Javascript LLVM Frontend')
    parser.add_argument ('input_file', metavar='input', type=str, nargs=1, help='javascript input source code')
    parser.add_argument ('output_file', metavar='output', type=str, nargs='?', default='./', help='LLVM IR output file')
    args = parser.parse_args ()
    main (args);

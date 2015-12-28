import sys

from antlr4 import *
from antlr4.tree.Trees import Trees

from ECMAScriptLexer import ECMAScriptLexer
from ECMAScriptParser import ECMAScriptParser
from ECMAScriptListener import ECMAScriptListener
from ECMAScriptCFG import ECMAScriptCFG
#from ECMAScriptLLVMEmitter import LLVMEmitter
from ECMAScriptLLVMEmitter import *

def main (argv):
    argv = '../js2asm_org/wow3.js'
    input_f = FileStream (argv);
    lexer = ECMAScriptLexer (input_f);
    stream = CommonTokenStream (lexer);

    parser = ECMAScriptParser (stream);
    tree = parser.program ();

    cfg = ECMAScriptCFG (argv)
    walker = ParseTreeWalker ()
    walker.walk (cfg, tree)

    #while False not in [x['done'] for x in cfg.getGraph ()]:
    '''while 1:
        if False not in [cfg.getGraph ()[func]['done'] for func in [x for x in cfg.getGraph ()]]:
            break'''
    while False in [cfg.getGraph ()[func]['done'] for func in [x for x in cfg.getGraph ()]]:
        walker.walk (cfg, tree)
    print (cfg.getGraph ())

    emitter = LLVMEmitter (cfg.getGraph ())
    walker.walk (emitter, tree)

    #for func in module.functions:
    #	func.viewCFG ()

if __name__ == '__main__':
    main (sys.argv);

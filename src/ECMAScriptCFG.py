# Generated from ECMAScript.g4 by ANTLR 4.5.1
import copy
import sys
import traceback

from antlr4 import *

from ECMAScriptLexer import ECMAScriptLexer
from ECMAScriptParser import ECMAScriptParser
from ECMAScriptListener import ECMAScriptListener

noinfered_ = -2
failed_ = -1
null_ = 0
bool_ = 1
int_ = 2
float_ = 3
string_ = 4
int_array = 5
float_array = 6
string_array = 7
obj_ = 8
function_ = 9
unknown_ = sys.maxint

node_root = []

class Node:
    def __init__ (self, root = False, arg = [], if_node = False):
        self.cld = []
        self.ctx = []
        self.var = {}
        self.arg = arg
        self.inst = {}
        self.nxt = None
        self.if_node = if_node
        self.bb = None
        if root is True:
            self.root = self
            self.inferable = True
        else:
            self.root = None

    def cacheInst (self, var_name, inst):
        self.inst[var_name] = inst

    def getInst (self, var_name):
        return self.inst.setdefault (var_name, None)

    def isIf (self):
        return self.if_node

    def setFunc (self, func, func_name):
        self.func = func
        self.func_name = func_name

    def getFunc (self):
        return self.func

    def getFuncName (self):
        return self.func_name

    def setBB (self, bb):
        self.bb = bb

    def getBB (self):
        return self.bb

    def getArg (self):
        return self.arg

    def appendChild (self, cld):
        cld.root = self.root
        cld.var = self.var.copy ()
        cld.arg = self.arg

        l = len (self.cld)
        if l != 0:
            self.cld[-1].nxt = cld

        self.cld.append (cld)

        return cld

    def getChild (self):
        if len (self.cld) == 0:
            return None

        return self.cld

    def getVar (self):
        return self.var

    def setCtx (self, ctx):
        self.ctx.append (ctx)

    def getCtx (self):
        return self.ctx

    '''def removeChild (self, cld):
        if cld not in self.cld:
            return None

        self.cld.remove (cld)'''

    def delVar (self, var):
        del self.var[var]

    def setType (self, var, ty):
        if type (ty) is list:
            print ('type of \'ty\' is list!\n\t'+str (ty)+'\n')
            traceback.print_stack ()

        if type (var) is not str:
            print ('type of \'var\' is not string\n\t'+str (var))

        if var in self.var:
            if self.var != ty:
                self.var[var].append (ty)
        else:
            self.var[var] = [ty]

        '''for leaf in self.cld:
            leaf.setType (var, ty)'''


    def getType (self, var):
        ty = self.var.setdefault (var, var)

        if ty == var:
            return ty
        else:
            return ty[-1]

# This class defines a complete listener for a parse tree produced by ECMAScriptParser.
class ECMAScriptCFG(ParseTreeListener):
    def __init__ (self, filename):
        self.graph = {}
        self.idx = 0
        self.current_f = 'global'

    def anonymIdx (self):
        self.anonym_idx += 1
        return str (self.anonym_idx)

    def getGraph (self):
        return self.graph

    def hasattr_t (self, ctx, s):
        if not self.graph.__contains__ (self.current_f):
            return False
        if not hasattr (ctx, s) or self.graph[self.current_f]['done'] is True:
            return False
        else:
            return True

    def iter_append (self, node, start):
        ret = []
        if node.getChild () is None:
            node.appendChild (start)
            return [node]

        for leaf in node.getChild ():
            ret.extend (self.iter_append (leaf, start))
        return ret

    # Enter a parse tree produced by ECMAScriptParser#program.
    def enterProgram(self, ctx):
        self.anonym_idx = 0

    # Exit a parse tree produced by ECMAScriptParser#program.
    def exitProgram(self, ctx):
        self.root = node_root


    # Enter a parse tree produced by ECMAScriptParser#sourceElements.
    def enterSourceElements(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            srcElems = ctx.sourceElement ()

            for srcElem in srcElems:
                srcElem.leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#sourceElements.
    def exitSourceElements(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#sourceElement.
    def enterSourceElement(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            ctx.statement ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#sourceElement.
    def exitSourceElement(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#statement.
    def enterStatement(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            ctx.getChild (0).leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#statement.
    def exitStatement(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            if hasattr (ctx.getChild (0), 'break_'):
                ctx.break_ = ctx.getChild (0).break_


    # Enter a parse tree produced by ECMAScriptParser#block.
    def enterBlock(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            ctx.statementList ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#block.
    def exitBlock(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#statementList.
    def enterStatementList(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            stmts = ctx.statement ()

            for stmt in stmts:
                stmt.leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#statementList.
    def exitStatementList(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            stmts = ctx.statement ()
            ctx.break_ = []
            for stmt in stmts:
                if hasattr (stmt, 'break_'):
                    ctx.break_.extend (stmt.break_)


    # Enter a parse tree produced by ECMAScriptParser#variableStatement.
    def enterVariableStatement(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            ctx.variableDeclarationList ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#variableStatement.
    def exitVariableStatement(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#variableDeclarationList.
    def enterVariableDeclarationList(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            vardecls = ctx.variableDeclaration ()

            for var in vardecls:
                var.leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#variableDeclarationList.
    def exitVariableDeclarationList(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            ctx.initialiser ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            single = ctx.initialiser ().single

            if type (single) is list:
                single = single[0]
            for leaf in ctx.leaves:
                leaf.setType (str (ctx.Identifier ()), leaf.getType (single))


    # Enter a parse tree produced by ECMAScriptParser#initialiser.
    def enterInitialiser(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            ctx.singleExpression ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#initialiser.
    def exitInitialiser(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.single = ctx.singleExpression ().single


    # Enter a parse tree produced by ECMAScriptParser#emptyStatement.
    def enterEmptyStatement(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#emptyStatement.
    def exitEmptyStatement(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#expressionStatement.
    def enterExpressionStatement(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            ctx.expressionSequence ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#expressionStatement.
    def exitExpressionStatement(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#ifStatement.
    def enterIfStatement(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            seq = ctx.expressionSequence ()
            stmts = ctx.statement ()

            if_then = []
            else_then = []

            seq.leaves = ctx.leaves
            for leaf in ctx.leaves:
                node = Node (if_node = True)
                leaf.appendChild (node)
                if_then.append (node)
                node = Node ()
                leaf.appendChild (node)
                else_then.append (node)

            stmts[0].leaves = if_then
            ctx.if_then = list (if_then)

            if len (stmts) == 2:
                stmts[1].leaves = else_then
            ctx.else_then = list (else_then)

    # Exit a parse tree produced by ECMAScriptParser#ifStatement.
    def exitIfStatement(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            stmts = ctx.statement ()
            ctx.ex = list (ctx.leaves)
            del ctx.leaves[:]
            ctx.leaves.extend (stmts[0].leaves)
            if hasattr (stmts[0], 'break_'):
                ctx.break_ = stmts[0].break_

            if len (stmts) == 2:
                ctx.leaves.extend (stmts[1].leaves)
                if hasattr (stmts[0], 'break_'):
                    ctx.break_.extend (stmts[1].break_)
            else:
                ctx.leaves.extend (ctx.else_then)


    # Enter a parse tree produced by ECMAScriptParser#DoStatement.
    def enterDoStatement(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            ctx.start_leaves = list (ctx.leaves)
            nodes = []
            for leaf in ctx.leaves:
                node = Node (if_node = True)
                leaf.appendChild (node)
                nodes.append (node)
            del ctx.leaves[:]
            ctx.leaves.extend (nodes)

            ctx.statement ().leaves = ctx.leaves
            ctx.expressionSequence ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#DoStatement.
    def exitDoStatement(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            nodes = []
            #for leaf in ctx.start_leaves:
                #lasts = self.iter_append (leaf, leaf)
            for last in ctx.leaves:
                node = Node ()
                last.appendChild (node)
                nodes.append (node)

            del ctx.leaves[:]
            ctx.leaves.extend (nodes)


    # Enter a parse tree produced by ECMAScriptParser#WhileStatement.
    def enterWhileStatement(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            nodes1 = []
            nodes2 = []
            for leaf in ctx.leaves:
                node = Node ()
                nodes1.append (node)
                leaf.appendChild (node)
            ctx.expressionSequence ().leaves = nodes1
            for leaf in nodes1:
                node = Node (if_node = True)
                nodes2.append (node)
                leaf.appendChild (node)
            ctx.statement ().leaves = nodes2

    # Exit a parse tree produced by ECMAScriptParser#WhileStatement.
    def exitWhileStatement(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            stmt = ctx.statement ()
            seq = ctx.expressionSequence ()

            nodes = []
            for leaf in seq.leaves:
                self.iter_append (leaf, leaf)
                node = Node ()
                leaf.appendChild (node)
                nodes.append (node)

            del ctx.leaves[:]
            ctx.leaves.extend (nodes)


    # Enter a parse tree produced by ECMAScriptParser#ForStatement.
    def enterForStatement(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            seqs = ctx.expressionSequence ()

            if seqs[0] is not None:
                seqs[0].leaves = ctx.leaves

            if seqs[1] is not None:
                nodes1 = []
                for leaf in ctx.leaves:
                    node = Node ()
                    leaf.appendChild (node)
                    nodes1.append (node)
                seqs[1].leaves = nodes1
            else:
                nodes1 = ctx.leaves

            nodes2 = []
            for leaf in nodes1:
                node = Node (if_node = True)
                leaf.appendChild (node)
                nodes2.append (node)
            seqs[2] = nodes2
            ctx.statement ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#ForStatement.
    def exitForStatement(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            seqs = ctx.expressionSequence ()

            if seqs[1] is not None:
                nodes = []
                for leaf in seqs[1].leaves:
                    self.iter_append (leaf, leaf)
                    node = Node ()
                    leaf.appendChild (node)
                    nodes.append (node)
                del ctx.leaves[:]
                ctx.leaves.extend (nodes)
            else:
                pass


    # Enter a parse tree produced by ECMAScriptParser#ForVarStatement.
    def enterForVarStatement(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#ForVarStatement.
    def exitForVarStatement(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#ForInStatement.
    def enterForInStatement(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#ForInStatement.
    def exitForInStatement(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#ForVarInStatement.
    def enterForVarInStatement(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#ForVarInStatement.
    def exitForVarInStatement(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#continueStatement.
    def enterContinueStatement(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#continueStatement.
    def exitContinueStatement(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#breakStatement.
    def enterBreakStatement(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)

    # Exit a parse tree produced by ECMAScriptParser#breakStatement.
    def exitBreakStatement(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.break_ = list (ctx.leaves)
            ctx.leaves = []


    # Enter a parse tree produced by ECMAScriptParser#returnStatement.
    def enterReturnStatement(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            ctx.expressionSequence ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#returnStatement.
    def exitReturnStatement(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            func_info = self.graph[self.current_f]
            func_info['return'] = True

            for leaf, single in zip (ctx.leaves, ctx.expressionSequence ().single):
                try:
                    idx = func_info['argv'].index (leaf.getArg ())
                    ty = leaf.getType (single)
                    if func_info['call'][idx] == unknown_ or ty > func_info['call'][idx]:
                        func_info['call'][idx] = ty
                    break
                except ValueError:
                    func_info['argv'].append (leaf.getArg ())
                    func_info['call'].append (unknown_)

    # Enter a parse tree produced by ECMAScriptParser#withStatement.
    def enterWithStatement(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#withStatement.
    def exitWithStatement(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#switchStatement.
    def enterSwitchStatement(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            ctx.expressionSequence ().leaves = ctx.leaves
            ctx.caseBlock ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#switchStatement.
    def exitSwitchStatement(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#caseBlock.
    def enterCaseBlock(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            ctx.caseClauses (0).leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#caseBlock.
    def exitCaseBlock(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#caseClauses.
    def enterCaseClauses(self, ctx):
        pass
        '''if self.hasattr_t (ctx, 'leaves'):
            cases = ctx.caseClause ()
            ctx.case_start = []
            for case in cases:
                ctx.case_start.append ([])
                for leaf in ctx.leaves:
                    node = Node ()
                    ctx.case_start[-1].append (node)
                case.leaves = list (ctx.case_start[-1])'''

    # Exit a parse tree produced by ECMAScriptParser#caseClauses.
    def exitCaseClauses(self, ctx):
        pass
        '''if self.hasattr_t (ctx, 'leaves'):
            cases = ctx.caseClause ()
            prev = None
            for case in cases:
                if not hasattr (case, 'break_') and prev is not None:'''


    # Enter a parse tree produced by ECMAScriptParser#caseClause.
    def enterCaseClause(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#caseClause.
    def exitCaseClause(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#defaultClause.
    def enterDefaultClause(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#defaultClause.
    def exitDefaultClause(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#labelledStatement.
    def enterLabelledStatement(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#labelledStatement.
    def exitLabelledStatement(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#throwStatement.
    def enterThrowStatement(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#throwStatement.
    def exitThrowStatement(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#tryStatement.
    def enterTryStatement(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#tryStatement.
    def exitTryStatement(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#catchProduction.
    def enterCatchProduction(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#catchProduction.
    def exitCatchProduction(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#finallyProduction.
    def enterFinallyProduction(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#finallyProduction.
    def exitFinallyProduction(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#debuggerStatement.
    def enterDebuggerStatement(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#debuggerStatement.
    def exitDebuggerStatement(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx):
        ctx.parent_f = self.current_f
        self.current_f = str (ctx.Identifier ())
        params = ctx.formalParameterList ()

        if not self.graph.__contains__ (self.current_f):
            self.graph[self.current_f] = {'name':self.current_f, 'root':[], 'inferable':True, 'call':[], 'argv':[], 'argc':0, 'done':False, 'return':False, 'struct':{}}
            node_root.append (self.graph[self.current_f])
            if params is None:
                node = Node (root=True)
                self.graph[self.current_f]['root'].append (node)
                ctx.functionBody ().leaves = [node]
                node.setCtx (ctx)
            else:
                self.graph[self.current_f]['argc'] = len (params.Identifier ())
        else:
            nodes = []
            for arg in self.graph[self.current_f]['argv']:
                idx = self.graph[self.current_f]['argv'].index (arg)
                ret = self.graph[self.current_f]['call'][idx]
                if ret == noinfered_ or ret == unknown_:
                    self.graph[self.current_f]['root'] = [n for n in self.graph[self.current_f]['root'] if n.getArg () != arg]
                    self.graph[self.current_f]['struct'][str (arg)] = {}
                    node = Node (root = True, arg = arg)
                    if params is not None:
                        i = 0
                        if type (arg) is not list:
                            arg = [arg]
                        for param in params.Identifier ():
                            node.setType (str (param), arg[i])
                            i += 1
                        self.graph[self.current_f]['inferable'] = False
                        self.graph[self.current_f]['argc'] = len (params.Identifier ())
                    nodes.append (node)
            if len (nodes) != 0:
                ctx.functionBody ().leaves = list (nodes)
                self.graph[self.current_f]['root'].extend (nodes)
                self.graph[self.current_f]['done'] = False
                ctx.functionBody ().leaves[0].setCtx (ctx)

    # Exit a parse tree produced by ECMAScriptParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx):
        '''if self.graph[self.current_f]['argc'] != 0:
            del self.graph[self.current_f]['argv'][0]
            del self.graph[self.current_f]['call'][0]'''
        if [] in self.graph[self.current_f]['call'] and self.graph[self.current_f]['return'] is True:
            self.graph[self.current_f]['done'] = False
        elif unknown_ not in [ret for ret in self.graph[self.current_f]['call']]:
            self.graph[self.current_f]['done'] = True
        else:
            self.graph[self.current_f]['done'] = False
        self.current_f = ctx.parent_f


    # Enter a parse tree produced by ECMAScriptParser#formalParameterList.
    def enterFormalParameterList(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#formalParameterList.
    def exitFormalParameterList(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.single = []
            for param in ctx.Identifier ():
                ctx.single.append (param)


    # Enter a parse tree produced by ECMAScriptParser#functionBody.
    def enterFunctionBody(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            ctx.sourceElements ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#functionBody.
    def exitFunctionBody(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#arrayLiteral.
    def enterArrayLiteral(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            ctx.elementList ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#arrayLiteral.
    def exitArrayLiteral(self, ctx):
        ctx.single = ctx.elementList ().single


    # Enter a parse tree produced by ECMAScriptParser#elementList.
    def enterElementList(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            singles = ctx.singleExpression ()

            for single in singles:
                single.leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#elementList.
    def exitElementList(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            for single in ctx.singleExpression ()[0].single:
                ctx.single = single + 3


    # Enter a parse tree produced by ECMAScriptParser#elision.
    def enterElision(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#elision.
    def exitElision(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#objectLiteral.
    def enterObjectLiteral(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.propertyNameAndValueList ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#objectLiteral.
    def exitObjectLiteral(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            '''ctx.single = []
            for leaf in ctx.leaves:
                leaf.setType ('obj_tmp_ret_' + str (self.anonymIdx ()), obj_)
                ctx.single.append (ctx.propertyNameAndValueList ().single)'''
            ctx.single = ctx.propertyNameAndValueList ().single


    # Enter a parse tree produced by ECMAScriptParser#propertyNameAndValueList.
    def enterPropertyNameAndValueList(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            props = ctx.propertyAssignment ()

            for prop in props:
                prop.leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#propertyNameAndValueList.
    def exitPropertyNameAndValueList(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            if unknown_ not in [n.single for n in ctx.propertyAssignment ()]:
                ctx.single = obj_
            else:
                ctx.single = unknown_


    # Enter a parse tree produced by ECMAScriptParser#PropertyExpressionAssignment.
    def enterPropertyExpressionAssignment(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.propertyName ().leaves = ctx.leaves
            ctx.singleExpression ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#PropertyExpressionAssignment.
    def exitPropertyExpressionAssignment(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            prop = ctx.propertyName ().single
            single = ctx.singleExpression ().single
            ctx.single = obj_

            for leaf in ctx.leaves:
                if self.graph[self.current_f]['struct'].has_key (str (leaf.getArg ())):
                    ty = leaf.getType (single)
                    if ty != function_:
                        self.graph[self.current_f]['struct'][str (leaf.getArg ())][prop] = ty
                    else:
                        self.graph[self.current_f]['struct'][str (leaf.getArg ())][prop] = single
                else:
                    ctx.single = unknown_


    # Enter a parse tree produced by ECMAScriptParser#PropertyGetter.
    def enterPropertyGetter(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.getter ().leaves = ctx.leaves
            ctx.functionBody ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#PropertyGetter.
    def exitPropertyGetter(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#PropertySetter.
    def enterPropertySetter(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.setter ().leaves = ctx.leaves
            ctx.propertySetParameterList ().leaves = ctx.leaves
            ctx.functionBody ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#PropertySetter.
    def exitPropertySetter(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#propertyName.
    def enterPropertyName(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            if ctx.identifierName () is not None:
                ctx.identifierName ().leaves = ctx.leaves
            if ctx.numericLiteral () is not None:
                ctx.numericLiteral ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#propertyName.
    def exitPropertyName(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            if ctx.identifierName () is not None:
                ctx.single = ctx.identifierName ().single
            if ctx.numericLiteral () is not None:
                ctx.single = ctx.numericLiteral ().single


    # Enter a parse tree produced by ECMAScriptParser#propertySetParameterList.
    def enterPropertySetParameterList(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#propertySetParameterList.
    def exitPropertySetParameterList(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#arguments.
    def enterArguments(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            if ctx.argumentList () is not None:
                ctx.argumentList ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#arguments.
    def exitArguments(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            if ctx.argumentList () is not None:
                ctx.single = ctx.argumentList ().single
            else:
                ctx.single = []


    # Enter a parse tree produced by ECMAScriptParser#argumentList.
    def enterArgumentList(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            singles = ctx.singleExpression ()

            for single in singles:
                single.leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#argumentList.
    def exitArgumentList(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            singles = ctx.singleExpression ()

            ctx.single = []
            if type (singles[0].single) is list:
                for leaf in ctx.leaves:
                    for l in range (len (ctx.leaves)):
                        ctx.single.append ([])
                    for single in singles:
                        idx = 0
                        for s in single.single:
                            ctx.single[idx].append (leaf.getType (s))
                            idx += 1
            else:
                for leaf in ctx.leaves:
                    ctx.single.append ([])
                    for single, idx in zip (singles, range (len (singles))):
                        ctx.single[-1].append (leaf.getType (single.single))


    # Enter a parse tree produced by ECMAScriptParser#expressionSequence.
    def enterExpressionSequence(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            singles = ctx.singleExpression ()

            for single in singles:
                single.leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#expressionSequence.
    def exitExpressionSequence(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            single = ctx.singleExpression ()[0]
            ctx.single = []

            if single.single is not list:
                single.single = [single.single]
            for leaf, val in zip (ctx.leaves, single.single):
                if type (val) is not list:
                    ty = [val]
                else:
                    ty = val
                ctx.single.extend (ty)


    # Enter a parse tree produced by ECMAScriptParser#TernaryExpression.
    def enterTernaryExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            start_leaves = list (ctx.leaves)
            nodes1 = []
            nodes2 = []

            for leaf in ctx.leaves:
                node = Node (if_node = True)
                leaf.appendChild (node)
                nodes1.append (node)

                node = Node ()
                leaf.appendChild (node)
                nodes2.append (node)

            singles = ctx.singleExpression ()
            singles[1].leaves = nodes1
            singles[2].leaves = nodes2
            singles[0].leaves = start_leaves

            del ctx.leaves[:]
            ctx.leaves.extend (nodes1 + nodes2)

    # Exit a parse tree produced by ECMAScriptParser#TernaryExpression.
    def exitTernaryExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.single = []
            singles = ctx.singleExpression ()

            for leaf in ctx.leaves:
                if leaf.isIf ():
                    ctx.single.append (singles[1].single)
                else:
                    ctx.single.append (singles[2].single)


    # Enter a parse tree produced by ECMAScriptParser#BitOrExpression.
    def enterBitOrExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            singles = ctx.singleExpression ()

            for single in singles:
                single.leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#BitOrExpression.
    def exitBitOrExpression(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#AssignmentExpression.
    def enterAssignmentExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            ctx.singleExpression ().leaves = ctx.leaves
            ctx.expressionSequence ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#AssignmentExpression.
    def exitAssignmentExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            single = ctx.singleExpression ()
            seq = ctx.expressionSequence ()

            if type (seq.single[0]) is list:
                idx = 0
                for leaf in ctx.leaves:
                    ty = leaf.getType (seq.single[0][idx])
                    leaf.setType (str (single.single), ty)
                    idx += 1
            else:
                for leaf in ctx.leaves:
                    ty = leaf.getType (seq.single[0])
                    leaf.setType (single.single, ty)

            ctx.single = None


    # Enter a parse tree produced by ECMAScriptParser#LogicalAndExpression.
    def enterLogicalAndExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            singles = ctx.singleExpression ()

            for single in singles:
                single.leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#LogicalAndExpression.
    def exitLogicalAndExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.single = bool_


    # Enter a parse tree produced by ECMAScriptParser#InstanceofExpression.
    def enterInstanceofExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            singles = ctx.singleExpression ()

            for single in singles:
                single.leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#InstanceofExpression.
    def exitInstanceofExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.ty = bool_


    # Enter a parse tree produced by ECMAScriptParser#ObjectLiteralExpression.
    def enterObjectLiteralExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.objectLiteral ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#ObjectLiteralExpression.
    def exitObjectLiteralExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.single = ctx.objectLiteral ().single


    # Enter a parse tree produced by ECMAScriptParser#PreDecreaseExpression.
    def enterPreDecreaseExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            ctx.singleExpression ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#PreDecreaseExpression.
    def exitPreDecreaseExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            single = ctx.singleExpression ().single

            for leaf in ctx.leaves:
                ty = leaf.getType (single)
                if ty != int_:
                    leaf.setType (single, failed_)
                    self.graph[self.current_f]['compilable'] = False


    # Enter a parse tree produced by ECMAScriptParser#ArrayLiteralExpression.
    def enterArrayLiteralExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            ctx.arrayLiteral ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#ArrayLiteralExpression.
    def exitArrayLiteralExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.single = ctx.arrayLiteral ().single


    # Enter a parse tree produced by ECMAScriptParser#InExpression.
    def enterInExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            singles = ctx.singleExpression ()

            for single in singles:
                single.leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#InExpression.
    def exitInExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.single = bool_


    # Enter a parse tree produced by ECMAScriptParser#ArgumentsExpression.
    def enterArgumentsExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            ctx.singleExpression ().leaves = ctx.leaves
            ctx.arguments ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#ArgumentsExpression.
    def exitArgumentsExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.single = []
            single = ctx.singleExpression ()
            args = ctx.arguments ().single

            if self.graph.setdefault (single.single, None) is None:
                print (single.single + ' is not declared yet')
                traceback.print_stack ()
                print;
                return

            if len (args[0]) != self.graph[single.single]['argc']:
                print ('# of argument is not satisfied (' + single.single + ', ' + str (self.graph[single.single]['argc']) + ') - ' + str (len (args)))
                traceback.print_stack ()
                print;

            func_info = self.graph[single.single]

            idx = 0
            for leaf, arg in zip (ctx.leaves, args):
                try:
                    idx = func_info['argv'].index (arg)
                except ValueError:
                    func_info['argv'].append (arg)
                    func_info['call'].append (unknown_)
                    idx = func_info['argv'].index (arg)
                    func_info['done'] = False
                if len (func_info['call']) <= idx:
                    func = noinfered_
                else:
                    func = func_info['call'][idx]
                if func == noinfered_:
                    func_info['done'] = False
                    func_info['call'][idx] = unknown_
                    ctx.single.append (unknown_)
                elif func == unknown_:
                    func_info['done'] = False
                    ctx.single.append (unknown_)
                else:
                    ctx.single = func
                idx += 1


    # Enter a parse tree produced by ECMAScriptParser#MemberDotExpression.
    def enterMemberDotExpression(self, ctx):
        ctx.singleExpression ().leaves = ctx.leaves
        ctx.identifierName ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#MemberDotExpression.
    def exitMemberDotExpression(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#NotExpression.
    def enterNotExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            ctx.singleExpression ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#NotExpression.
    def exitNotExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.single = bool_


    # Enter a parse tree produced by ECMAScriptParser#DeleteExpression.
    def enterDeleteExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            ctx.singleExpression ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#DeleteExpression.
    def exitDeleteExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            single = ctx.singleExpression ()
            if not hasattr (single, 'single'):
                return

            for leaf in ctx.leaves:
                leaf.delVar (single.single)

            ctx.single = bool_


    # Enter a parse tree produced by ECMAScriptParser#IdentifierExpression.
    def enterIdentifierExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)

    # Exit a parse tree produced by ECMAScriptParser#IdentifierExpression.
    def exitIdentifierExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.single = str (ctx.Identifier ())


    # Enter a parse tree produced by ECMAScriptParser#BitAndExpression.
    def enterBitAndExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            singles = ctx.singleExpression ()

            for single in singles:
                single.leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#BitAndExpression.
    def exitBitAndExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.single = int_


    # Enter a parse tree produced by ECMAScriptParser#UnaryMinusExpression.
    def enterUnaryMinusExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            ctx.singleExpression ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#UnaryMinusExpression.
    def exitUnaryMinusExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.single = int_


    # Enter a parse tree produced by ECMAScriptParser#PreIncrementExpression.
    def enterPreIncrementExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            ctx.singleExpression ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#PreIncrementExpression.
    def exitPreIncrementExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            single = ctx.singleExpression ()

            for leaf in ctx.leaves:
                ty = leaf.getType (single.single)
                if ty == int_:
                    leaf.setType (single.single, failed_)
                else:
                    leaf.setType (single.single, int_)


    # Enter a parse tree produced by ECMAScriptParser#
    def enterFunctionExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.parent_f = self.current_f
            if ctx.Identifier () is not None:
                self.current_f = str (ctx.Identifier ())
            else:
                self.current_f = 'anonym_' + self.anonymIdx ()
            params = ctx.formalParameterList ()

            if not self.graph.__contains__ (self.current_f):
                self.graph[self.current_f] = {'name':self.current_f, 'root':[], 'inferable':True, 'call':[], 'argv':[], 'argc':0, 'done':False, 'return':False, 'struct':{}}
                node_root.append (self.graph[self.current_f])
                if params is None:
                    node = Node (root=True)
                    self.graph[self.current_f]['root'].append (node)
                    ctx.functionBody ().leaves = [node]
                    node.setCtx (ctx)
                else:
                    self.graph[self.current_f]['argc'] = len (params.Identifier ())
            else:
                nodes = []
                for arg in self.graph[self.current_f]['argv']:
                    idx = self.graph[self.current_f]['argv'].index (arg)
                    ret = self.graph[self.current_f]['call'][idx]
                    if ret == noinfered_ or ret == unknown_:
                        self.graph[self.current_f]['root'] = [n for n in self.graph[self.current_f]['root'] if n.getArg () != arg]
                        self.graph[self.current_f]['struct'][str (arg)] = {}
                        node = Node (root = True, arg = arg)
                        if params is not None:
                            i = 0
                            if type (arg) is not list:
                                arg = [arg]
                            for param in params.Identifier ():
                                node.setType (str (param), arg[i])
                                i += 1
                            self.graph[self.current_f]['inferable'] = False
                            self.graph[self.current_f]['argc'] = len (params.Identifier ())
                        nodes.append (node)
                if len (nodes) != 0:
                    ctx.functionBody ().leaves = list (nodes)
                    self.graph[self.current_f]['root'].extend (nodes)
                    self.graph[self.current_f]['done'] = False
                    ctx.functionBody ().leaves[0].setCtx (ctx)

    # Exit a parse tree produced by ECMAScriptParser#FunctionExpression.
    def exitFunctionExpression(self, ctx):
        cur = self.current_f
        self.current_f = ctx.parent_f
        if self.hasattr_t (ctx, 'leaves'):
            if [] in self.graph[cur]['call'] and self.graph[cur]['return'] is True:
                self.graph[cur]['done'] = False
            elif unknown_ not in [ret for ret in self.graph[cur]['call']]:
                self.graph[cur]['done'] = True
            else:
                self.graph[cur]['done'] = False
            ctx.single = function_


    # Enter a parse tree produced by ECMAScriptParser#BitShiftExpression.
    def enterBitShiftExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            singles = ctx.singleExpression ()

            for single in singles:
                single.leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#BitShiftExpression.
    def exitBitShiftExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.single = int_


    # Enter a parse tree produced by ECMAScriptParser#LogicalOrExpression.
    def enterLogicalOrExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            singles = ctx.singleExpression ()

            for single in singles:
                single.leaves  = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#LogicalOrExpression.
    def exitLogicalOrExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.single = bool_


    # Enter a parse tree produced by ECMAScriptParser#VoidExpression.
    def enterVoidExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            ctx.singleExpression ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#VoidExpression.
    def exitVoidExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.single = failed_


    # Enter a parse tree produced by ECMAScriptParser#ParenthesizedExpression.
    def enterParenthesizedExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            ctx.expressionSequence ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#ParenthesizedExpression.
    def exitParenthesizedExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.single = ctx.expressionSequence ().single


    # Enter a parse tree produced by ECMAScriptParser#UnaryPlusExpression.
    def enterUnaryPlusExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            ctx.singleExpression ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#UnaryPlusExpression.
    def exitUnaryPlusExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            single = ctx.singleExpression ()

            for leaf in ctx.leaves:
                ty = leaf.getType (single.single)
                if ty != int_:
                    leaf.setType (single.single, failed_)
                else:
                    leaf.setType (single.single, int_)


    # Enter a parse tree produced by ECMAScriptParser#LiteralExpression.
    def enterLiteralExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            ctx.literal ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#LiteralExpression.
    def exitLiteralExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.single = ctx.literal ().single


    # Enter a parse tree produced by ECMAScriptParser#BitNotExpression.
    def enterBitNotExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            ctx.singleExpression ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#BitNotExpression.
    def exitBitNotExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.single = bool_


    # Enter a parse tree produced by ECMAScriptParser#PostIncrementExpression.
    def enterPostIncrementExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            ctx.singleExpression ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#PostIncrementExpression.
    def exitPostIncrementExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            single = ctx.singleExpression ()

            for leaf in ctx.leaves:
                ty = leaf.getType (single.single)
                if ty != int_:
                    leaf.setType (single.single, failed_)
                else:
                    leaf.setType (single.single, int_)

            ctx.single = int_


    # Enter a parse tree produced by ECMAScriptParser#TypeofExpression.
    def enterTypeofExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            ctx.singleExpression ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#TypeofExpression.
    def exitTypeofExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.single = string_


    # Enter a parse tree produced by ECMAScriptParser#AssignmentOperatorExpression.
    def enterAssignmentOperatorExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            ctx.singleExpression ().leaves = ctx.leaves
            ctx.expressionSequence ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#AssignmentOperatorExpression.
    def exitAssignmentOperatorExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            single = ctx.singleExpression ()
            assign = str (ctx.assignmentOperator ().getText ())
            seq = ctx.expressionSequence ()

            if assign == '+=':
                ctx.single = []
                idx = 0
                for leaf in ctx.leaves:
                    ty1 = leaf.getType (single.single)
                    if type (seq.single) is list:
                        ty = seq.single[0]
                    else:
                        ty = seq.single
                    ty2 = leaf.getType (ty)

                    ty = ty1 if ty1 > ty2 else ty2

                    leaf.setType (single.single, ty)
                    ctx.single.append (ty)
            elif assign == '*=' or assign == '/=' or assign == '-=' or assign == '%=':
                ctx.single= []
                for leaf in ctx.leaves:
                    ty1 = leaf.getType (single.single)
                    if (type (seq.single)) is list:
                        ty = seq.single[0]
                    else:
                        ty = seq.single
                    ty2 = leaf.getType (ty)

                    ty = ty1 if ty1 > ty2 else ty2

                    if ty == int_:
                        leaf.setType (single.single, ty)
                    else:
                        leaf.setType (single.single, float_)

                    ctx.single.append (ty)
            else:
                ctx.single = int_


    # Enter a parse tree produced by ECMAScriptParser#NewExpression.
    def enterNewExpression(self, ctx):
        if hasattr_t (ctx, 'leaves'):
            ctx.singleExpression ().leaves = ctx.leaves
            if ctx.arguments () is not None:
                ctx.arguments ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#NewExpression.
    def exitNewExpression(self, ctx):
        if hasattr_t (ctx, 'leaves'):
            single = ctx.singleExpression ()
            for leaf in ctx.leaves:
                leaf.setType (single.single, obj_)


    # Enter a parse tree produced by ECMAScriptParser#PostDecreaseExpression.
    def enterPostDecreaseExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            ctx.singleExpression ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#PostDecreaseExpression.
    def exitPostDecreaseExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            single = ctx.singleExpression ()

            for leaf in ctx.leaves:
                ty = leaf.getType (single.single)
                if ty != int_:
                    leaf.setType (single.single, failed_)
                else:
                    leaf.setType (single.single, int_)

            ctx.single = int_


    # Enter a parse tree produced by ECMAScriptParser#RelationalExpression.
    def enterRelationalExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            singles = ctx.singleExpression ()

            for single in singles:
                single.leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#RelationalExpression.
    def exitRelationalExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.single = bool_


    # Enter a parse tree produced by ECMAScriptParser#EqualityExpression.
    def enterEqualityExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            singles = ctx.singleExpression ()

            for single in singles:
                single.leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#EqualityExpression.
    def exitEqualityExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.single = bool_


    # Enter a parse tree produced by ECMAScriptParser#BitXOrExpression.
    def enterBitXOrExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            ctx.singleExpression ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#BitXOrExpression.
    def exitBitXOrExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.single = int_


    # Enter a parse tree produced by ECMAScriptParser#AdditiveExpression.
    def enterAdditiveExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            singles = ctx.singleExpression ()

            for single in singles:
                single.leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#AdditiveExpression.
    def exitAdditiveExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            singles = ctx.singleExpression ()
            ctx.single = []

            for leaf in ctx.leaves:
                if type (singles[0].single) is list:
                    ty1 = leaf.getType (singles[0].single[0])
                else:
                    ty1 = leaf.getType (singles[0].single)
                if type (singles[1].single) is list:
                    ty2 = leaf.getType (singles[1].single[0])
                else:
                    ty2 = leaf.getType (singles[1].single)

                ty = ty1 if ty1 > ty2 else ty2

                ctx.single.append (ty)


    # Enter a parse tree produced by ECMAScriptParser#MemberIndexExpression.
    def enterMemberIndexExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            ctx.singleExpression ().leaves = ctx.leaves
            ctx.expressionSequence ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#MemberIndexExpression.
    def exitMemberIndexExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            for leaf in ctx.leaves:
                ctx.single = leaf.getType (ctx.singleExpression ().single) - 3


    # Enter a parse tree produced by ECMAScriptParser#ThisExpression.
    def enterThisExpression(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#ThisExpression.
    def exitThisExpression(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#MultiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            singles = ctx.singleExpression ()

            for single in singles:
                single.leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#MultiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            singles = ctx.singleExpression ()
            ctx.single = []

            for leaf in ctx.leaves:
                if type (singles[0].single) is list:
                    ty1 = leaf.getType (singles[0].single[0])
                else:
                    ty1 = leaf.getType (singles[0].single)
                if type (singles[1].single) is list:
                    ty2 = leaf.getType (singles[1].single[0])
                else:
                    ty2 = leaf.getType (singles[1].single)

                ty = ty1 if ty1 > ty2 else ty2

                if ty > float_:
                    ty = float_

                ctx.single.append (ty)


    # Enter a parse tree produced by ECMAScriptParser#assignmentOperator.
    def enterAssignmentOperator(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)

    # Exit a parse tree produced by ECMAScriptParser#assignmentOperator.
    def exitAssignmentOperator(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.single = str (ctx.getText ())


    # Enter a parse tree produced by ECMAScriptParser#literal.
    def enterLiteral(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)
            if ctx.numericLiteral () is not None:
                ctx.numericLiteral ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#literal.
    def exitLiteral(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            if ctx.numericLiteral () is not None:
                ctx.single = ctx.numericLiteral ().single
            elif ctx.NullLiteral () is not None:
                ctx.single = null_
            elif ctx.BooleanLiteral () is not None:
                ctx.single = bool_
            elif ctx.StringLiteral () is not None:
                ctx.single = string_
            elif ctx.numericLiteral () is not None:
                ctx.single = ctx.numericLiteral ().single
            else:
                ctx.single = failed_


    # Enter a parse tree produced by ECMAScriptParser#numericLiteral.
    def enterNumericLiteral(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)

    # Exit a parse tree produced by ECMAScriptParser#numericLiteral.
    def exitNumericLiteral(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            num = str (ctx.getText ())

            if '.' in num:
                ctx.single = float_
            else:
                ctx.single = int_


    # Enter a parse tree produced by ECMAScriptParser#identifierName.
    def enterIdentifierName(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.leaves[0].setCtx (ctx)

    # Exit a parse tree produced by ECMAScriptParser#identifierName.
    def exitIdentifierName(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.single = str (ctx.getText ())


    # Enter a parse tree produced by ECMAScriptParser#reservedWord.
    def enterReservedWord(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#reservedWord.
    def exitReservedWord(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#keyword.
    def enterKeyword(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#keyword.
    def exitKeyword(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#futureReservedWord.
    def enterFutureReservedWord(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#futureReservedWord.
    def exitFutureReservedWord(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#getter.
    def enterGetter(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#getter.
    def exitGetter(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#setter.
    def enterSetter(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#setter.
    def exitSetter(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#eos.
    def enterEos(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#eos.
    def exitEos(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#eof.
    def enterEof(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#eof.
    def exitEof(self, ctx):
        pass

def cfg_main (argv):
    argv = [0,1]
    argv[1] = 'wow3.js'
    input_f = FileStream (argv[1])
    lexer = ECMAScriptLexer (input_f)
    stream = CommonTokenStream (lexer)

    parser = ECMAScriptParser (stream)
    tree = parser.program ()

    listener = ECMAScriptCFG (argv[1])
    walker = ParseTreeWalker ()
    walker.walk (listener, tree)
    idx = 0
    while 1:
        print (idx)
        print [x['name'] for x in node_root]
        print [x['done'] for x in node_root]
        if False not in [x['done'] for x in node_root]:
            break
        walker.walk (listener, tree)
        idx += 1
    print (node_root)

if __name__ == '__main__':
    cfg_main (sys.argv)

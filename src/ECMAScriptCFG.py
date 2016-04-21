# Generated from ECMAScript.g4 by ANTLR 4.5.1
import sys
import traceback

from antlr4 import *

noinfered_ = -2
failed_ = -1
null_ = 0
bool_ = 1
int_ = 2
float_ = 3
string_ = 4
int_array_ = 5
float_array_ = 6
string_array_ = 7
obj_ = 8
function_ = 9
unknown_ = sys.maxint

node_root = []

class Node:
    def __init__ (self, isRoot = False, arg = [], ifNode = False):
        self.cld = []
        self.nxt = None
        self.var = {}
        self.arg = arg
        self.inst = {}
        self.ifNode = ifNode
        self.bb = None
        self.symTable = {}
        if isRoot:
            self.root = self
        else:
            self.root = None

    def cacheInst (self, var, inst):
        self.inst[var] = inst

    def getInst (self, var):
        return self.inst.setdefault (var, None)

    def isIf (self):
        return self.ifNode

    def getSymTable (self):
        return self.symTable

    def inheritSymTable (self, parent):
        self.symTable = dict (parent)

    def setSym (self, var, ty, idx = None):
        if dix is None:
            self.symTable[var] = ty
        else:
            self.symTable[var][idx] = ty

    def getSym (self, var, idx = None):
        if idx is None:
            return self.symTable.setdefault (var, var)
        else:
            return self.symTable[var].setdefault (idx, var)

    def hasSym (self, var):
        return self.symTable.has_key (var)

    def setFunc (self, func, funcName):
        self.func = func
        self.func_name = funcName

    def getFunc (self):
        return self.func

    def getFuncName (self):
        return self.funcName

    def setBB (self, bb):
        self.bb = bb

    def getBB (self):
        return self.bb

    def getArg (self):
        return self.arg

    def appendChild (self, cld):
        cld.root = self.root
        cld.var = dict (self.var)
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

    def delVar (var):
        del self.var[var]

    def setType (self, var, ty):
        if type (ty) is list:
            print 'type of \'ty\' is list!\n\t' + str (ty) + '\n'
            traceback.print_stack ()

        if type(var) is not str:
            print 'type of \'ty\' is not str!\n\t' + str (ty) + '\n'

        if var in self.var:
            if self.var != ty:
                self.var[var].append (ty)
        else:
            self.var[var] = [ty]

    def getType (self, var):
        if type (var) is int or type (var) is float:
            return var
        ty = self.var.setdefault (var, [unknown_])

        if ty == var:
            return ty
        else:
            return ty[-1]

class ECMAScriptCFG(ParseTreeVisitor):

    def __init__ (self, filename):
        self.graph = {}
        self.idx = 0
        self.currentF = 'global'

    def anonymIdx (self):
        self.anonymIdx += 1
        return str (self.anonymIdx)

    def getGraph (self):
        return self.graph

    def hasattr_t (self, ctx, s):
        if not self.graph.__contains__ (self.currentF):
            return False
        if not hasattr (ctx, s) or self.graph[self.currentF]['done'] is True:
            return False
        else:
            return True

    def iter_append (self, node, start, prevs = []):
        ret = []
        if node in prevs:
            return []
        prevs.append (node)
        if node.getChild () is None:
            node.appendChild (start)
            return [node]

        for leaf in node.getChild ():
            ret.extend (self.iter_append (leaf, start, prevs))
        return ret

    # Visit a parse tree produced by ECMAScriptParser#program.
    def visitProgram(self, ctx):
        self.idx = 0
        self.anonymIdx = 0
        self.visitChildren (ctx)
        self.root = node_root


    # Visit a parse tree produced by ECMAScriptParser#sourceElements.
    def visitSourceElements(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            srcElems = ctx.sourceElement ()

            for srcElem in srcElems:
                srcElem.leaves = ctx.leaves
                self.visit (srcElem)
        else:
            self.visitChildren (ctx)


    # Visit a parse tree produced by ECMAScriptParser#sourceElement.
    def visitSourceElement(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.statement ().leaves = ctx.leaves
            self.visit (ctx.statement ())
        else:
            self.visitChildren (ctx)


    # Visit a parse tree produced by ECMAScriptParser#statement.
    def visitStatement(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.getChild (0).leaves = ctx.leaves
            self.visit (ctx.getChild (0))
            if hasattr (ctx.getChild (0), 'break_'):
                ctx.break_ = ctx.getChild (0).break_
        else:
            self.visitChildren (ctx)


    # Visit a parse tree produced by ECMAScriptParser#block.
    def visitBlock(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.statementList ().leaves = ctx.leaves
            self.visit (ctx.statementList ())
        else:
            self.visitChildren (ctx)


    # Visit a parse tree produced by ECMAScriptParser#statementList.
    def visitStatementList(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            stmts = ctx.statement ()
            ctx.break_ = []

            for stmt in stmts:
                stmt.leaves = ctx.leaves
                self.visit (stmt)
                if hasattr (stmt, 'break_'):
                    ctx.break_.append (stmt.break_)
        else:
            self.visitChildren (ctx)


    # Visit a parse tree produced by ECMAScriptParser#variableStatement.
    def visitVariableStatement(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.variableDeclarationList ().leaves = ctx.leaves
            self.visit (ctx.variableDeclarationList ())
        else:
            self.visitChildren (ctx)


    # Visit a parse tree produced by ECMAScriptParser#variableDeclarationList.
    def visitVariableDeclarationList(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            varDecls = ctx.variableDeclaration ()

            for varDecl in varDecls:
                varDecl.leaves = ctx.leaves
                self.visit (varDecl)
        else:
            self.visitChildren (ctx)


    # Visit a parse tree produced by ECMAScriptParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            init = ctx.initialiser ()
            if init is not None:
                ctx.initialiser ().leaves = ctx.leaves

                self.visit (init)

                value = ctx.initialiser ().value

                if type (value) is list:
                    value = value[0]
                for leaf in ctx.leaves:
                    leaf.setType (str (ctx.Identifier ()), leaf.getType (value))
        else:
            self.visitChildren (ctx)


    # Visit a parse tree produced by ECMAScriptParser#initialiser.
    def visitInitialiser(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            single = ctx.singleExpression ()
            single.leaves = ctx.leaves

            self.visit (single)

            ctx.value = single.value
        else:
            self.visitChildren (ctx)


    # Visit a parse tree produced by ECMAScriptParser#emptyStatement.
    def visitEmptyStatement(self, ctx):
        return self.visitChildren (ctx)


    # Visit a parse tree produced by ECMAScriptParser#expressionStatement.
    def visitExpressionStatement(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            seq = ctx.expressionSequence ()
            seq.leaves = ctx.leaves
            self.visit (seq)
        else:
            self.visitChildren (ctx)


    # Visit a parse tree produced by ECMAScriptParser#ifStatement.
    def visitIfStatement(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            seq = ctx.expressionSequence ()
            stmts = ctx.statement ()
            ctx.break_ = []

            if_then = []
            else_then = []

            seq.leaves = ctx.leaves
            for leaf in ctx.leaves:
                node = Node (ifNode = True)
                leaf.appendChild (node)
                if_then.append (node)
            stmts[0].leaves = if_then

            self.visit (stmts[0])
            if hasattr (stmts[0], 'break_'):
                ctx.break_.extend (stmts[0].break_)

            for leaf in ctx.leaves:
                node = Node (ifNode = False)
                leaf.appendChild (node)
                else_then.append (node)

            if len (stmts) == 2:
                stmts[1].leaves = else_then
                self.visit (stmts[1])
                if hasattr (stmts[1], 'break_'):
                    ctx.break_.extend (stmts[1].break_)

            del ctx.leaves[:]
            ctx.leaves.extend (if_then)
            ctx.leaves.extend (else_then)
        else:
            self.visitChildren (ctx)


    # Visit a parse tree produced by ECMAScriptParser#DoStatement.
    def visitDoStatement(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            stmt = ctx.statement ()
            seq = ctx.expressionSequence ()
            nodes = []
            for leaf in ctx.leaves:
                node = Node (ifNode = True)
                leaf.appendChild (node)
                nodes.append (node)
            start_leaves = list (nodes)

            stmt.leaves = nodes
            seq.leaves = nodes
            self.visit (stmt)
            self.visit (seq)

            for leaf in start_leaves:
                self.iter_append (leaf, leaf)

            del ctx.leaves[:]
            for leaf in nodes:
                node = Node ()
                leaf.appendChild (node)
                ctx.leaves.append (node)
        else:
            self.visitChildren (ctx)


    # Visit a parse tree produced by ECMAScriptParser#WhileStatement.
    def visitWhileStatement(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            seq = ctx.expressionSequence ()
            stmt = ctx.statement ()

            nodes1 = []
            nodes2 = []

            print ctx.leaves
            for leaf in ctx.leaves:
                node = Node ()
                nodes1.append (node)
                leaf.appendChild (node)
            start_leaves = list (nodes1)
            seq.leaves = nodes1
            self.visit (seq)

            print nodes1
            for leaf in nodes1:
                node = Node (ifNode = True)
                nodes2.append (node)
                leaf.appendChild (node)

            stmt.leaves = nodes2
            self.visit (stmt)

            for leaf in start_leaves:
                self.iter_append (leaf, leaf)

            print nodes2

            del ctx.leaves[:]
            for leaf in start_leaves:
                node = Node ()
                leaf.appendChild (node)
                ctx.leaves.append (node)
            print ctx.leaves
        else:
            self.visitChildren (ctx)


    # Visit a parse tree produced by ECMAScriptParser#ForStatement.
    def visitForStatement(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            seqs = ctx.expressionSequence ()
            stmt = ctx.statement ()
            nodes1 = []

            if seqs[0] is not None:
                seqs[0].leaves = ctx.leaves
                self.visit (seqs[0])

            if seqs[1] is not None:
                seqs[1].leaves = ctx.leaves
                self.visit (seqs[1])

            for leaf in ctx.leaves:
                node = Node (ifNode = True)
                leaf.appendChild (node)
                nodes1.append (node)
            startNodes = list (nodes1)
            stmt.leaves = nodes1
            self.visit (stmt)

            if seqs[2] is not None:
                seqs[2].leaves = nodes1
                self.visit (seqs[2])

            if seqs[1] is not None:
                seqs[1].leaves = nodes1
                self.visit (seqs[1])

            for leaf in startNodes:
                self.iter_append (leaf, leaf)

            del ctx.leaves[:]
            for leaf in nodes1:
                node = Node ()
                leaf.appendChild (node)
                ctx.leaves.append (node)
        else:
            self.visitChildren (ctx)


    # Visit a parse tree produced by ECMAScriptParser#ForVarStatement.
    def visitForVarStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#ForInStatement.
    def visitForInStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#ForVarInStatement.
    def visitForVarInStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#continueStatement.
    def visitContinueStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#breakStatement.
    def visitBreakStatement(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.break_ = list (ctx.leaves)
        else:
            self.visitChildren (ctx)


    # Visit a parse tree produced by ECMAScriptParser#returnStatement.
    def visitReturnStatement(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            seq = ctx.expressionSequence ()

            seq.leaves = ctx.leaves
            self.visit (seq)

            funcInfo = self.graph[self.currentF]
            funcInfo['return'] = True

            for leaf, value in zip (ctx.leaves, seq.value):
                try:
                    idx = funcInfo['argv'].index (leaf.getArg ())
                    ty = leaf.getType (value)
                    if funcInfo['call'][idx] == unknown_ or ty > funcInfo['call'][idx]:
                        funcInfo['call'][idx] = ty
                    break
                except ValueError:
                    funcInfo['argv'].append (leaf.getArg ())
                    funcInfo['call'].append (unknown_)
        else:
            self.visitChildren (ctx)


    # Visit a parse tree produced by ECMAScriptParser#withStatement.
    def visitWithStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#switchStatement.
    def visitSwitchStatement(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            seq = ctx.expressionSequence ()
            cases = ctx.caseBlock ()

            seq.leaves = ctx.leaves
            self.visit (seq)

            cases.leaves = ctx.leaves
            self.visit (cases)

            breaks_ = cases.break_

            for leaf in breaks_:
                node = Node ()
                leaf.appendChild (node)
                ctx.leaves.append (node)
        else:
            self.visitChildren (ctx)


    # Visit a parse tree produced by ECMAScriptParser#caseBlock.
    def visitCaseBlock(self, ctx):
        return self.visitChildren (ctx)


    # Visit a parse tree produced by ECMAScriptParser#caseClauses.
    def visitCaseClauses(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#caseClause.
    def visitCaseClause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#defaultClause.
    def visitDefaultClause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#labelledStatement.
    def visitLabelledStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#throwStatement.
    def visitThrowStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#tryStatement.
    def visitTryStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#catchProduction.
    def visitCatchProduction(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#finallyProduction.
    def visitFinallyProduction(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#debuggerStatement.
    def visitDebuggerStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx):
        ctx.parentF = self.currentF
        self.currentF = str (ctx.Identifier ())
        params = ctx.formalParameterList ()
        body = ctx.functionBody ()

        if not self.graph.__contains__ (self.currentF):
            self.graph[self.currentF] = {'name': self.currentF, 'root': [], 'call': [], 'argv': [], 'argc': 0, 'done': False, 'return': False}
            node_root.append (self.graph[self.currentF])

            if params is not None:
                self.visit (params)
                self.graph[self.currentF]['argc'] = len (params.value)
            else:
                node = Node (isRoot = True)
                self.graph[self.currentF]['root'].append (node)
                body.leaves = [node]
        else:
            nodes = []

            for arg in self.graph[self.currentF]['argv']:
                idx = self.graph[self.currentF]['argv'].index (arg)
                if not hasattr (self.graph[self.currentF], 'idx'):
                    self.idx += 1
                    self.graph[self.currentF]['idx'] = [self.idx]
                else:
                    try:
                        idx = self.graph[self.currentF]['idx'][idx]
                    except KeyError:
                        self.idx += 1
                        self.graph[self.currentF]['idx'].append (self.idx)

                ret = self.graph[self.currentF]['call'][idx]

                if ret == noinfered_ or ret == unknown_:
                    self.graph[self.currentF]['root'] = [n for n in self.graph[self.currentF]['root'] if n.getArg () != arg]
                    node = Node (isRoot = True, arg = arg)
                    if params is not None:
                        self.visit (params)
                        i = 0
                        if type (arg) is not list:
                            arg = [arg]
                        for param in params.value:
                            node.setType (param, arg[i])
                            i += 1
                        self.graph[self.currentF]['argc'] = len (arg)
                    nodes.append (node)
            if len (nodes) != 0:
                body.leaves = list (nodes)
                self.graph[self.currentF]['root'].extend (nodes)
                self.graph[self.currentF]['done'] = False

        self.visit (body)

        if [] in self.graph[self.currentF]['call'] and self.graph[self.currentF]['return'] is True:
            self.graph[self.currentF]['done'] = False
        elif unknown_ not in [ret for ret in self.graph[self.currentF]['call']]:
            self.graph[self.currentF]['done'] = True
        else:
            self.graph[self.currentF]['done'] = False
        self.currentF = ctx.parentF


    # Visit a parse tree produced by ECMAScriptParser#formalParameterList.
    def visitFormalParameterList(self, ctx):
        names = ctx.Identifier ()
        ctx.value = []

        for name in names:
            ctx.value.append (str (name))


    # Visit a parse tree produced by ECMAScriptParser#functionBody.
    def visitFunctionBody(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            srcElems = ctx.sourceElements ()
            srcElems.leaves = ctx.leaves
            self.visit (srcElems)
        else:
            self.visitChildren (ctx)


    # Visit a parse tree produced by ECMAScriptParser#arrayLiteral.
    def visitArrayLiteral(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.value = []
            elem = ctx.elementList ()
            elem.leaves = ctx.leaves
            self.visit (elem)
            for arr in elem.value:
                val = -1
                for tmp in arr:
                    if tmp > val:
                        val = tmp
                ctx.value.append (val + int_array_ - int_)
        else:
            self.visitChildren (ctx)


    # Visit a parse tree produced by ECMAScriptParser#elementList.
    def visitElementList(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            tmp = []
            singles = ctx.singleExpression ()
            for single in singles:
                single.leaves = ctx.leaves
                self.visit (single)
                tmp.append (single.value)

            ctx.value = [[row[i] for row in tmp for i in range (len (tmp[0]))]]

        else:
            self.visitChildren (ctx)


    # Visit a parse tree produced by ECMAScriptParser#elision.
    def visitElision(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#objectLiteral.
    def visitObjectLiteral(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#propertyNameAndValueList.
    def visitPropertyNameAndValueList(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#PropertyExpressionAssignment.
    def visitPropertyExpressionAssignment(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#PropertyGetter.
    def visitPropertyGetter(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#PropertySetter.
    def visitPropertySetter(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#propertyName.
    def visitPropertyName(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#propertySetParameterList.
    def visitPropertySetParameterList(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#arguments.
    def visitArguments(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            argList = ctx.argumentList ()

            if argList is not None:
                argList.leaves = ctx.leaves
                self.visit (argList)
                ctx.value = argList.value
            else:
                ctx.value = []
        else:
            self.visitChildren (ctx)


    # Visit a parse tree produced by ECMAScriptParser#argumentList.
    def visitArgumentList(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.value = []
            singles = ctx.singleExpression ()

            for single in singles:
                single.leaves = ctx.leaves
                self.visit (single)

            if type (singles[0].value) is list:
                for l in range (len (ctx.leaves)):
                    ctx.value.append ([])
                for single in singles:
                    idx = 0
                    for s, leaf in zip (single.value, ctx.leaves):
                        ctx.value[idx].append (leaf.getType (s))
                        idx += 1
            else:
                for leaf in ctx.leaves:
                    ctx.value.append ([])
                    for single in singles:
                        ctx.value[-1].append (leaf.getType (single.value))


    # Visit a parse tree produced by ECMAScriptParser#expressionSequence.
    def visitExpressionSequence(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.value = []
            singles = ctx.singleExpression ()
            for single in singles:
                single.leaves = ctx.leaves
                self.visit (single)
            if single.value is not list:
                single.value = [single.value]
            for val in single.value:
                if type (val) is not list:
                    ty = [val]
                else:
                    ty = val
                ctx.value.extend (ty)
        else:
            self.visitChildren (ctx)


    # Visit a parse tree produced by ECMAScriptParser#TernaryExpression.
    def visitTernaryExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#LogicalAndExpression.
    def visitLogicalAndExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.value = []
            single = ctx.singleExpression ()
            self.visit (single)

            for leaf in ctx.leaves:
                ctx.value.append (bool_)
        else:
            self.visitChildren (ctx)


    # Visit a parse tree produced by ECMAScriptParser#PreIncrementExpression.
    def visitPreIncrementExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.value = []
            for leaf in ctx.leaves:
                ctx.value.append (int_)
        else:
            self.visitChildren (ctx)


    # Visit a parse tree produced by ECMAScriptParser#ObjectLiteralExpression.
    def visitObjectLiteralExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#InExpression.
    def visitInExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#LogicalOrExpression.
    def visitLogicalOrExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.value = []
            single = ctx.singleExpression ()
            self.visit (single)

            for leaf in ctx.leaves:
                ctx.value.append (bool_)


    # Visit a parse tree produced by ECMAScriptParser#NotExpression.
    def visitNotExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.value = []
            for leaf in ctx.leaves:
                ctx.value.append (bool_)
        else:
            self.visitChildren (ctx)


    # Visit a parse tree produced by ECMAScriptParser#PreDecreaseExpression.
    def visitPreDecreaseExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.value = []
            for leaf in ctx.leaves:
                ctx.value.append (int_)
        else:
            self.visitChildren (ctx)


    # Visit a parse tree produced by ECMAScriptParser#ArgumentsExpression.
    def visitArgumentsExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.value = []
            single = ctx.singleExpression ()
            args = ctx.arguments ()

            args.leaves = ctx.leaves
            self.visit (args)
            single.leaves = ctx.leaves
            self.visit (single)

            '''print single.value
            print ctx.getText ()'''

            if self.graph.setdefault (single.value, None) is None:
                self.graph[single.value] = {'name': single.value, 'root': [], 'call': [], 'argv': [], 'argc': 0, 'done': False, 'return': False}

            funcInfo = self.graph[single.value]

            idx = 0
            for leaf, arg in zip (ctx.leaves, args.value):
                try:
                    idx = funcInfo['argv'].index (arg)
                except ValueError:
                    funcInfo['argv'].append (arg)
                    funcInfo['call'].append (unknown_)
                    idx = funcInfo['argv'].index (arg)
                    funcInfo['done'] = False
                if len (funcInfo['call']) <= idx:
                    func = noinfered_
                else:
                    func = funcInfo['call'][idx]

                if func == noinfered_:
                    funcInfo['done'] = False
                    funcInfo['call'][idx] = unknown_
                    ctx.value.append (unknown_)
                elif func == unknown_:
                    funcInfo['done'] = False
                    ctx.value.append (unknown_)
                else:
                    ctx.value = func

                idx += 1
        else:
            self.visitChildren (ctx)


    # Visit a parse tree produced by ECMAScriptParser#ThisExpression.
    def visitThisExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#FunctionExpression.
    def visitFunctionExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#UnaryMinusExpression.
    def visitUnaryMinusExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.value = []
            single = ctx.singleExpression ()
            self.visit (single)
        else:
            self.visitChildren (ctx)


    # Visit a parse tree produced by ECMAScriptParser#PostDecreaseExpression.
    def visitPostDecreaseExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.value = []
            for leaf in ctx.leaves:
                ctx.value.append (int_)
        else:
            self.visitChildren (ctx)


    # Visit a parse tree produced by ECMAScriptParser#AssignmentExpression.
    def visitAssignmentExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            single = ctx.singleExpression ()
            seq = ctx.expressionSequence ()

            seq.leaves = ctx.leaves
            self.visit (seq)
            single.leaves = ctx.leaves
            self.visit (single)

            if type (seq.value[0]) is list:
                idx = 0
                for leaf in ctx.leaves:
                    ty = leaf.getType (seq.value[0][idx])
                    leaf.setType (str (single.value), ty)
                    idx += 1
            else:
                for leaf in ctx.leaves:
                    ty = leaf.getType (seq.value[0])
                    leaf.setType (str (single.value), ty)
            ctx.value = None
        else:
            self.visitChildren (ctx)


    # Visit a parse tree produced by ECMAScriptParser#TypeofExpression.
    def visitTypeofExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#InstanceofExpression.
    def visitInstanceofExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#UnaryPlusExpression.
    def visitUnaryPlusExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.value = []
            single = ctx.singleExpression ()
            self.visit (single)
            for val in single:
                if val > float_:
                    ctx.value.append (float_)
                else:
                    ctx.value.append (val)
        else:
            self.visitChildren (ctx)


    # Visit a parse tree produced by ECMAScriptParser#DeleteExpression.
    def visitDeleteExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#EqualityExpression.
    def visitEqualityExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.value = []
            singles = ctx.singleExpression ()

            for single in singles:
                single.leaves = ctx.leaves
                self.visit (single)

            for leaf in ctx.leaves:
                ctx.value.append (bool_)
        else:
            self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#BitXOrExpression.
    def visitBitXOrExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.value = []
            singles = ctx.singleExpression ()
            for single in singles:
                single.leaves = ctx.leaves
                self.visit (single)
            for val1, val2 in zip (singles[0].value, singles[1].value):
                val = None
                if val1 < null_ and val2 < null_:
                    val = unknown_
                elif val1 > val2:
                    val = val1
                else:
                    val = val2
                if val > float_:
                    val = float_
                ctx.value.append (val)
        else:
            self.visitChildren (ctx)



    # Visit a parse tree produced by ECMAScriptParser#MultiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.value = []
            singles = ctx.singleExpression ()
            for single in singles:
                single.leaves = ctx.leaves
                self.visit (single)

            for leaf in ctx.leaves:
                if type (singles[0].value) is list:
                    ty1 = leaf.getType (singles[0].value[0])
                else:
                    ty1 = leaf.getType (singles[0].value)
                if type (singles[1].value) is list:
                    ty2 = leaf.getType (singles[1].value[0])
                else:
                    ty2 = leaf.getType (singles[1].value)

                ty = ty1 if ty1 > ty2 else ty2
                if ty > float_:
                    ty = float_

                ctx.value.append (ty)
        else:
            self.visitChildren (ctx)


    # Visit a parse tree produced by ECMAScriptParser#BitShiftExpression.
    def visitBitShiftExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#ParenthesizedExpression.
    def visitParenthesizedExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            seq = ctx.expressionSequence ()
            seq.leaves = ctx.leaves
            self.visit (seq)

            ctx.value = ctx.expressionSequence ().value
        else:
            self.visitChildren (ctx)


    # Visit a parse tree produced by ECMAScriptParser#AdditiveExpression.
    def visitAdditiveExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.value = []
            singles = ctx.singleExpression ()

            for single in singles:
                single.leaves = ctx.leaves
                self.visit (single)

            for leaf in ctx.leaves:
                if type (singles[0].value) is list:
                    ty1 = leaf.getType (singles[0].value[0])
                else:
                    ty1 = leaf.getType (singles[0].value)
                if type (singles[1].value) is list:
                    ty2 = leaf.getType (singles[1].value[0])
                else:
                    ty2 = leaf.getType (singles[1].value)

                ty = ty1 if ty1 > ty2 else ty2

                ctx.value.append (ty)
        else:
            self.visitChildren (ctx)


    # Visit a parse tree produced by ECMAScriptParser#RelationalExpression.
    def visitRelationalExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.value = bool_
            singles = ctx.singleExpression ()

            for single in singles:
                single.leaves = ctx.leaves
                self.visit (single)
        else:
            self.visitChildren (ctx)


    # Visit a parse tree produced by ECMAScriptParser#PostIncrementExpression.
    def visitPostIncrementExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.value = []
            for leaf in ctx.leaves:
                ctx.value.append (int_)
        else:
            self.visitChildren (ctx)


    # Visit a parse tree produced by ECMAScriptParser#BitNotExpression.
    def visitBitNotExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#NewExpression.
    def visitNewExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#LiteralExpression.
    def visitLiteralExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            lit = ctx.literal ()
            lit.leaves = ctx.leaves
            self.visit (lit)
            ctx.value = lit.value
        else:
            self.visitChildren (ctx)


    # Visit a parse tree produced by ECMAScriptParser#ArrayLiteralExpression.
    def visitArrayLiteralExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            arr = ctx.arrayLiteral ()
            arr.leaves = ctx.leaves
            self.visit (arr)
            ctx.value = arr.value
        else:
            self.visitChildren (ctx)


    # Visit a parse tree produced by ECMAScriptParser#MemberDotExpression.
    def visitMemberDotExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#MemberIndexExpression.
    def visitMemberIndexExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.value = []
            single = ctx.singleExpression ()
            seq = ctx.expressionSequence ()

            seq.leaves = ctx.leaves
            self.visit (seq)
            single.leaves = ctx.leaves
            self.visit (single)

            for leaf in ctx.leaves:
                ctx.value.append (leaf.getType (single.value) - (int_array_ - int_))
        else:
            self.visitChildren (ctx)


    # Visit a parse tree produced by ECMAScriptParser#IdentifierExpression.
    def visitIdentifierExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.value = str (ctx.Identifier ())
        else:
            self.visitChildren (ctx)


    # Visit a parse tree produced by ECMAScriptParser#BitAndExpression.
    def visitBitAndExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#BitOrExpression.
    def visitBitOrExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#AssignmentOperatorExpression.
    def visitAssignmentOperatorExpression(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            single = ctx.singleExpression ()
            seq = ctx.expressionSequence ()

            seq.leaves = ctx.leaves
            self.visit (seq)
            single.leaves = ctx.leaves
            self.visit (single)

            assign = str (ctx.assignmentOperator ().getText ())

            if assign == '+=':
                ctx.value = []
                for leaf in ctx.leaves:
                    ty1 = leaf.getType (single.value)
                    if type (seq.value) is list:
                        ty = seq.value[0]
                    else:
                        ty = seq.value (ty)
                    ty2 = leaf.getType (ty)

                    ty = ty1 if ty1 > ty2 else ty2

                    leaf.setType (single.value, ty)
                    ctx.value.append (ty)
            elif assign in ['*=', '/=', '-=', '%=']:
                ctx.value = []
                for leaf in ctx.leaves:
                    ty1 = leaf.getType (single.value)
                    if type (seq.value) is list:
                        ty = seq.value[0]
                    else:
                        ty = seq.value
                    ty2 = leaf.getType (ty)

                    ty = ty1 if ty1 > ty2 else ty2

                    if ty == int_:
                        leaf.setType (single.value, ty)
                    else:
                        leaf.setType (single.value, float_)

                    ctx.value.append (ty)
            else:
                ctx.value = int_
        else:
            self.visitChildren (ctx)


    # Visit a parse tree produced by ECMAScriptParser#VoidExpression.
    def visitVoidExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.value = str (ctx.getText ())
        else:
            self.visitChildren (ctx)


    # Visit a parse tree produced by ECMAScriptParser#literal.
    def visitLiteral(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.value = []
            num = ctx.numericLiteral ()
            value = None
            if num is not None:
                num.leaves = ctx.leaves
                self.visit (num)
                value = num.value
            elif ctx.NullLiteral () is not None:
                value = null_
            elif ctx.BooleanLiteral () is not None:
                value = bool_
            elif ctx.StringLiteral () is not None:
                value = string_
            else:
                value = failed_
            for leaf in ctx.leaves:
                ctx.value.append (value)
        else:
            self.visitChildren (ctx)


    # Visit a parse tree produced by ECMAScriptParser#numericLiteral.
    def visitNumericLiteral(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            num = str (ctx.getText ())

            if '.' in num:
                ctx.value = float_
            else:
                ctx.value = int_

        else:
            self.visitChildren (ctx)


    # Visit a parse tree produced by ECMAScriptParser#identifierName.
    def visitIdentifierName(self, ctx):
        if self.hasattr_t (ctx, 'leaves'):
            ctx.value = str (ctx.getText ())
        else:
            self.visitChildren (ctx)


    # Visit a parse tree produced by ECMAScriptParser#reservedWord.
    def visitReservedWord(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#keyword.
    def visitKeyword(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#futureReservedWord.
    def visitFutureReservedWord(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#getter.
    def visitGetter(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#setter.
    def visitSetter(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#eos.
    def visitEos(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#eof.
    def visitEof(self, ctx):
        return self.visitChildren(ctx)


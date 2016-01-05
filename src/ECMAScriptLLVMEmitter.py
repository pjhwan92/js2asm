# Generated from ECMAScript.g4 by ANTLR 4.5.1
import sys

from antlr4 import *
from antlr4.tree.Trees import Trees

from ECMAScriptLexer import ECMAScriptLexer
from ECMAScriptParser import ECMAScriptParser
from ECMAScriptListener import ECMAScriptListener
from ECMAScriptCFG import ECMAScriptCFG
from ECMAScriptCFG import Node
import os

from llvm import *
from llvm.core import *
from llvm.ee import *

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
func = 8
unknown_ = 100

module = Module.new ('top')

# This class defines a complete listener for a parse tree produced by ECMAScriptParser.
class LLVMEmitter(ParseTreeListener):
    current_f = 'global'
    sym_table_f = {}
    node_root = None
    func_idx = -1

    def __init__ (self, node_root, output_file):
        self.node_root = node_root
        self.path = output_file

    def recLeaves (self, leaf, end_leaves):
        leaves = []
        if leaf in end_leaves:
            return [leaf]
        if leaf.getChild () == [] or leaf.getChild () is None:
            return [leaf]
        for cld in leaf.getChild ():
            leaves.extend (self.recLeaves (cld, end_leaves))
        return leaves

    def llvmType (self, ty):
        if ty == int_:
            return Type.int ()
        elif ty == float_:
            return Type.float ()
        elif ty == string_:
            return Type.pointer (Type.int (1))
        elif ty == int_array:
            return Type.pointer (Type.int ())
        elif ty == float_array:
            return Type.pointer (Type.float ())
        elif ty == string_array:
            return Type.pointer (Type.pointer (Type.int (1)))
        else:
            print ('unknown type occurs (' + str (ty) + ')')

        return None

    def asmType (self, ty):
        if ty == type (Type.int ()):
            return int_
        elif ty == type (Type.float ()):
            return float_
        elif ty == type (Type.pointer (Type.int (1))):
            return string_
        elif ty == type (Type.pointer (Type.int (32))):
            return int_array
        else:
            print 'unexpected data type occurs! (' + str (ty) + ')'

        return None

    def setEndBlock (self, comp, leaf):
        builder = Builder.new (leaf.getBB ())
        f = leaf.getFunc ()
        end = f.append_basic_block ('end_block')
        builder.cbranch (comp, leaf.getBB (), end)
        builder = Builder.new (end)
        builder.ret (Constant.real (Type.float (), 0.0))

    def getVal (self, cand, leaf):
        cached = leaf.getInst (cand)
        if cached is not None:
            return cached
        builder = Builder.new (leaf.getBB ())
        flag = False
        if hasattr (cand, 'opcode_name'):
            if cand.opcode_name == 'getelementptr':
                flag = True
        if type (cand) is AllocaInstruction or flag is True:
            load = builder.load (cand)
            leaf.cacheInst (cand, load)
            return load
        else:
            return cand

    def setVal (self, val, cand, leaf):
        builder = Builder.new (leaf.getBB ())
        flag = False
        if hasattr (cand, 'opcode_name'):
            if cand.opcode_name == 'getelementptr':
                flag = True
        if type (cand) is AllocaInstruction or flag is True:
            store = builder.store (self.getVal (val, leaf), cand)
        else:
            store = self.getVal (val, leaf)
        return store

    # Enter a parse tree produced by ECMAScriptParser#program.
    def enterProgram(self, ctx):
        module.data_layout = 'e-i1:8:8-i8:8:8-i16:16:16-i32:32:32-i64:64:64-f32:32:32-f64:64:64-p:32:32:32-v128:32:128-n32-S128'
        module.target = 'asmjs-unknown-emscripten'
        #module.target = 'x86_64-unknown-linux-gnu'
        self.sym_table_f['global'] = {}

    # Exit a parse tree produced by ECMAScriptParser#program.
    def exitProgram(self, ctx):
        path = self.path
        if os.path.isdir (path):
            file_name = path + '/wow.ll'
        else:
            file_name = path
        f = open (file_name, 'w')
        f.write (str (module))
        f.close ()


    # Enter a parse tree produced by ECMAScriptParser#sourceElements.
    def enterSourceElements(self, ctx):
        if hasattr (ctx, 'leaves'):
            elems = ctx.sourceElement ()

            for elem in elems:
                elem.leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#sourceElements.
    def exitSourceElements(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#sourceElement.
    def enterSourceElement(self, ctx):
        if hasattr (ctx, 'leaves'):
            ctx.statement ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#sourceElement.
    def exitSourceElement(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#statement.
    def enterStatement(self, ctx):
        ctx.getChild (0).leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#statement.
    def exitStatement(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#block.
    def enterBlock(self, ctx):
        ctx.statementList ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#block.
    def exitBlock(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#statementList.
    def enterStatementList(self, ctx):
        stmts = ctx.statement ()

        for stmt in stmts:
            stmt.leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#statementList.
    def exitStatementList(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#variableStatement.
    def enterVariableStatement(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#variableStatement.
    def exitVariableStatement(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#variableDeclarationList.
    def enterVariableDeclarationList(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#variableDeclarationList.
    def exitVariableDeclarationList(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#initialiser.
    def enterInitialiser(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#initialiser.
    def exitInitialiser(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#emptyStatement.
    def enterEmptyStatement(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#emptyStatement.
    def exitEmptyStatement(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#expressionStatement.
    def enterExpressionStatement(self, ctx):
        ctx.expressionSequence ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#expressionStatement.
    def exitExpressionStatement(self, ctx):
        ctx.value = ctx.expressionSequence ().value


    # Enter a parse tree produced by ECMAScriptParser#ifStatement.
    def enterIfStatement(self, ctx):
        ctx.expressionSequence ().leaves = ctx.leaves
        if_nodes = []
        else_nodes = []
        for leaf in ctx.leaves:
            f = leaf.getFunc ()
            clds = leaf.getChild ()
            for cld in clds:
                cld.setFunc (f, leaf.getFuncName ())
                if cld.isIf ():
                    if_nodes.append (cld)
                    cld.setBB (f.append_basic_block ('if_then'))
                else:
                    else_nodes.append (cld)
                    cld.setBB (f.append_basic_block ('if_else'))
        stmts = ctx.statement ()
        stmts[0].leaves = if_nodes
        ctx.else_then = else_nodes
        if stmts[-1] is not stmts[0]:
            stmts[1].leaves = else_nodes

    # Exit a parse tree produced by ECMAScriptParser#ifStatement.
    def exitIfStatement(self, ctx):
        stmts = ctx.statement ()
        comps = ctx.expressionSequence ().value
        leaves = []

        for leaf, comp in zip (ctx.leaves, comps):
            builder = Builder.new (leaf.getBB ())
            clds = leaf.getChild ()
            else_then = None
            for cld in clds:
                if cld.isIf ():
                    if_then = cld
                else:
                    else_then = cld
            builder.cbranch (comp, if_then.getBB (), else_then.getBB ())

        if True not in [hasattr (leaf, 'term') for leaf in stmts[0].leaves]:
            leaves.extend (stmts[0].leaves)
        if stmts[-1] == stmts[0]:
            leaves.extend (ctx.else_then)
        else:
            if True not in [hasattr (leaf, 'term') for leaf in stmts[1].leaves]:
                leaves.extend (stmts[1].leaves)
        del ctx.leaves[:]
        ctx.leaves.extend (leaves)


    # Enter a parse tree produced by ECMAScriptParser#DoStatement.
    def enterDoStatement(self, ctx):
        leaves = []
        for leaf in ctx.leaves:
            builder = Builder.new (leaf.getBB ())
            f = leaf.getFunc ()
            clds = leaf.getChild ()
            for cld in clds:
                cld.setFunc (f, leaf.getFuncName ())
            clds[0].setBB (f.append_basic_block ('loop'))
            builder.branch (clds[0].getBB ())
            leaves.append (clds[0])
        ctx.start_leaves = list (leaves)
        ctx.statement ().leaves = leaves
        ctx.expressionSequence ().leaves = leaves

    # Exit a parse tree produced by ECMAScriptParser#DoStatement.
    def exitDoStatement(self, ctx):
        stmt = ctx.statement ()
        comps = ctx.expressionSequence ().value
        leaves = []

        for start_leaf in ctx.start_leaves:
            end_leaves = self.recLeaves (start_leaf, ctx.start_leaves)
            for end_leaf, comp in zip (end_leaves, comps):
                builder = Builder.new (end_leaf.getBB ())
                clds = end_leaf.getChild ()
                f = end_leaf.getFunc ()
                f_name = end_leaf.getFuncName ()
                if clds is not None:
                    for cld in clds:
                        cld.setFunc (f, f_name)
                        cld.setBB (f.append_basic_block ('elem'))
                        builder.cbranch (comp, end_leaf.getBB (), cld.getBB ())
                    leaves.extend (clds)
                else:
                    self.setEndBlock (comp, end_leaf)
        del ctx.leaves[:]
        ctx.leaves.extend (leaves)


    # Enter a parse tree produced by ECMAScriptParser#WhileStatement.
    def enterWhileStatement(self, ctx):
        seq = ctx.expressionSequence ()
        seq_leaves = []
        stmt = ctx.statement ()
        stmt_leaves = []
        ctx.nexts = []

        for leaf in ctx.leaves:
            builder = Builder.new (leaf.getBB ())
            bb = leaf.getFunc ().append_basic_block ()
            builder.branch (bb)
            for cld in leaf.getChild ():
                cld.setBB (bb)
                seq_leaves.append (cld)
                gclds = cld.getChild ()
                gclds[0].setBB (cld.getFunc ().append_basic_block ())
                stmt_leaves.append (gclds[0])
                gclds[1].setBB (cld.getFunc ().append_basic_block ())
                ctx.nexts.append (gclds[1])

        seq.leaves = seq_leaves
        stmt.leaves = stmt_leaves

    # Exit a parse tree produced by ECMAScriptParser#WhileStatement.
    def exitWhileStatement(self, ctx):
        stmt = ctx.statement ()
        seq = ctx.expressionSequence ()

        nodes = []
        for leaf in seq.leaves:
            builder = Builder.new (seq.getBB ())
            end_leaves = self.recLeaves (leaf, stmt.leaves)
            for end_leaf in end_leaves:
                end_leaf.getBB ()


    # Enter a parse tree produced by ECMAScriptParser#ForStatement.
    def enterForStatement(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#ForStatement.
    def exitForStatement(self, ctx):
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
        pass

    # Exit a parse tree produced by ECMAScriptParser#breakStatement.
    def exitBreakStatement(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#returnStatement.
    def enterReturnStatement(self, ctx):
        ctx.expressionSequence ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#returnStatement.
    def exitReturnStatement(self, ctx):
        for leaf, value in zip (ctx.leaves, ctx.expressionSequence ().value):
            builder = Builder.new (leaf.bb)
            ret = self.getVal (value, leaf)

            if type (ret.type) is IntegerType:
                if type (ret) is ConstantInt:
                    ret = Constant.real (Type.float (), float (ctx.expressionSequence ().getText ()))
                else:
                    ret = builder.bitcast (ret, Type.float ())
            builder.ret (ret)
            leaf.term = True


    # Enter a parse tree produced by ECMAScriptParser#withStatement.
    def enterWithStatement(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#withStatement.
    def exitWithStatement(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#switchStatement.
    def enterSwitchStatement(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#switchStatement.
    def exitSwitchStatement(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#caseBlock.
    def enterCaseBlock(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#caseBlock.
    def exitCaseBlock(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#caseClauses.
    def enterCaseClauses(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#caseClauses.
    def exitCaseClauses(self, ctx):
        pass


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
        func_name = str (ctx.Identifier ())
        node_root = self.node_root[func_name]
        #node_root = self.graph
        ctx.leaves = node_root['root']
        ctx.origin_f = self.current_f
        self.current_f = func_name
        params = ctx.formalParameterList ()

        if params is not None:
            param_id = params.Identifier ()
            ty_f = []
            for leaf, call in zip (ctx.leaves, node_root['call']):
                ty_arg = []
                for arg in leaf.getArg ():
                    ty_arg.append (self.llvmType (arg))
                ty = self.llvmType (call)
                '''if ty == Type.int ():
                    ty = Type.float ()'''
                ty_f.append (Type.function (ty, ty_arg))
        else:
            param_id = []
            ty_f = [Type.function (self.llvmType (node_root['call'][0]), [])]

        self.sym_table_f[ctx.origin_f][func_name] = {}
        for leaf, ty in zip (ctx.leaves, ty_f):
            self.func_idx += 1
            if func_name == 'main':
                f = module.add_function (ty, func_name)
            else:
                f = module.add_function (ty, '__' + str (self.func_idx))
            self.sym_table_f[ctx.origin_f][func_name][str (leaf.getArg ())] = f
            self.sym_table_f[f] = {}
            leaf.setFunc (f, func_name)

            bb = f.append_basic_block ('function_init')
            leaf.setBB (bb)

            builder = Builder.new (bb)
            for arg, ty_, farg in zip (param_id, leaf.getArg (), f.args):
                farg.name = str (arg)
                alloc = builder.alloca (self.llvmType (ty_))
                builder.store (farg, alloc)
                self.sym_table_f[f][farg.name] = alloc

        ctx.functionBody ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx):
        self.current_f = ctx.origin_f


    # Enter a parse tree produced by ECMAScriptParser#formalParameterList.
    def enterFormalParameterList(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#formalParameterList.
    def exitFormalParameterList(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#functionBody.
    def enterFunctionBody(self, ctx):
        ctx.sourceElements ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#functionBody.
    def exitFunctionBody(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#arrayLiteral.
    def enterArrayLiteral(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#arrayLiteral.
    def exitArrayLiteral(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#elementList.
    def enterElementList(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#elementList.
    def exitElementList(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#elision.
    def enterElision(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#elision.
    def exitElision(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#objectLiteral.
    def enterObjectLiteral(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#objectLiteral.
    def exitObjectLiteral(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#propertyNameAndValueList.
    def enterPropertyNameAndValueList(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#propertyNameAndValueList.
    def exitPropertyNameAndValueList(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#PropertyExpressionAssignment.
    def enterPropertyExpressionAssignment(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#PropertyExpressionAssignment.
    def exitPropertyExpressionAssignment(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#PropertyGetter.
    def enterPropertyGetter(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#PropertyGetter.
    def exitPropertyGetter(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#PropertySetter.
    def enterPropertySetter(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#PropertySetter.
    def exitPropertySetter(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#propertyName.
    def enterPropertyName(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#propertyName.
    def exitPropertyName(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#propertySetParameterList.
    def enterPropertySetParameterList(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#propertySetParameterList.
    def exitPropertySetParameterList(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#arguments.
    def enterArguments(self, ctx):
        ctx.argumentList ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#arguments.
    def exitArguments(self, ctx):
        ctx.value = ctx.argumentList ().value
        ctx.type_ = ctx.argumentList ().type_


    # Enter a parse tree produced by ECMAScriptParser#argumentList.
    def enterArgumentList(self, ctx):
        singles = ctx.singleExpression ()

        for single in singles:
            single.leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#argumentList.
    def exitArgumentList(self, ctx):
        singles = ctx.singleExpression ()
        ctx.value = []
        ctx.type_ = []

        for leaf in ctx.leaves:
            ctx.value.append ([])
            ctx.type_.append ([])

        for single in singles:
            for val, value, type_ in zip (single.value, ctx.value, ctx.type_):
                getVal = self.getVal (val, leaf)
                value.append (getVal)
                type_.append (self.asmType (type (getVal.type)))


    # Enter a parse tree produced by ECMAScriptParser#expressionSequence.
    def enterExpressionSequence(self, ctx):
        singles = ctx.singleExpression ()

        for single in singles:
            single.leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#expressionSequence.
    def exitExpressionSequence(self, ctx):
        ctx.value = ctx.singleExpression (0).value


    # Enter a parse tree produced by ECMAScriptParser#TernaryExpression.
    def enterTernaryExpression(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#TernaryExpression.
    def exitTernaryExpression(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#BitOrExpression.
    def enterBitOrExpression(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#BitOrExpression.
    def exitBitOrExpression(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#AssignmentExpression.
    def enterAssignmentExpression(self, ctx):
        ctx.singleExpression ().leaves = ctx.leaves
        ctx.expressionSequence ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#AssignmentExpression.
    def exitAssignmentExpression(self, ctx):
        single = ctx.singleExpression ()
        assignees = single.value
        seq = ctx.expressionSequence ()
        assigners = seq.value
        ctx.value = []

        for leaf, assignee, assigner in zip (ctx.leaves, assignees, assigners):
            builder = Builder.new (leaf.getBB ())
            assignee_val = self.getVal (assignee, leaf)
            assigner_val = self.getVal (assigner, leaf)
            sym = self.sym_table_f[leaf.getFunc ()]
            if type (assignee) is str:
                alloc = builder.alloca (assigner_val.type, name = assignee)
                sym[assignee] = alloc
            else:
                if assigner_val.type == assignee_val.type:
                    alloc = assignee_val
                else:
                    name = str (single.getText ())
                    alloc = builder.alloca (assigner.type, name = name)
                    sym[name] = alloc
            ctx.value.append (self.setVal (assigner_val, alloc, leaf))


    # Enter a parse tree produced by ECMAScriptParser#LogicalAndExpression.
    def enterLogicalAndExpression(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#LogicalAndExpression.
    def exitLogicalAndExpression(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#InstanceofExpression.
    def enterInstanceofExpression(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#InstanceofExpression.
    def exitInstanceofExpression(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#ObjectLiteralExpression.
    def enterObjectLiteralExpression(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#ObjectLiteralExpression.
    def exitObjectLiteralExpression(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#PreDecreaseExpression.
    def enterPreDecreaseExpression(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#PreDecreaseExpression.
    def exitPreDecreaseExpression(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#ArrayLiteralExpression.
    def enterArrayLiteralExpression(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#ArrayLiteralExpression.
    def exitArrayLiteralExpression(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#InExpression.
    def enterInExpression(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#InExpression.
    def exitInExpression(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#ArgumentsExpression.
    def enterArgumentsExpression(self, ctx):
        ctx.singleExpression ().leaves = ctx.leaves
        ctx.arguments ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#ArgumentsExpression.
    def exitArgumentsExpression(self, ctx):
        single = ctx.singleExpression ()
        func = None
        ctx.value = []

        for leaf, value, ty in zip (ctx.leaves, ctx.arguments ().value, ctx.arguments ().type_):
            builder = Builder.new (leaf.getBB ())
            if self.sym_table_f[leaf.getFunc ()].has_key (single.value[0]):
                func = self.sym_table_f[leaf.getFunc ()][single.value[0]][str (ty)]
            elif self.sym_table_f['global'].has_key (single.value[0]):
                func = self.sym_table_f['global'][single.value[0]][str (ty)]
            else:
                func = self.sym_table_f['global'][single.value[0]][str (ty)] = module.add_function (declare_ty[single.value[0]])

            ctx.value.append (builder.call (func, value))


    # Enter a parse tree produced by ECMAScriptParser#MemberDotExpression.
    def enterMemberDotExpression(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#MemberDotExpression.
    def exitMemberDotExpression(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#NotExpression.
    def enterNotExpression(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#NotExpression.
    def exitNotExpression(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#DeleteExpression.
    def enterDeleteExpression(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#DeleteExpression.
    def exitDeleteExpression(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#IdentifierExpression.
    def enterIdentifierExpression(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#IdentifierExpression.
    def exitIdentifierExpression(self, ctx):
        var_name = str (ctx.Identifier ())
        ctx.value = []

        for leaf in ctx.leaves:
            if self.sym_table_f[leaf.getFunc ()].has_key (var_name):
                ctx.value.append (self.sym_table_f[leaf.getFunc ()][var_name])
            else:
                ctx.value.append (var_name)


    # Enter a parse tree produced by ECMAScriptParser#BitAndExpression.
    def enterBitAndExpression(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#BitAndExpression.
    def exitBitAndExpression(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#UnaryMinusExpression.
    def enterUnaryMinusExpression(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#UnaryMinusExpression.
    def exitUnaryMinusExpression(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#PreIncrementExpression.
    def enterPreIncrementExpression(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#PreIncrementExpression.
    def exitPreIncrementExpression(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#FunctionExpression.
    def enterFunctionExpression(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#FunctionExpression.
    def exitFunctionExpression(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#BitShiftExpression.
    def enterBitShiftExpression(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#BitShiftExpression.
    def exitBitShiftExpression(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#LogicalOrExpression.
    def enterLogicalOrExpression(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#LogicalOrExpression.
    def exitLogicalOrExpression(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#VoidExpression.
    def enterVoidExpression(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#VoidExpression.
    def exitVoidExpression(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#ParenthesizedExpression.
    def enterParenthesizedExpression(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#ParenthesizedExpression.
    def exitParenthesizedExpression(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#UnaryPlusExpression.
    def enterUnaryPlusExpression(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#UnaryPlusExpression.
    def exitUnaryPlusExpression(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#LiteralExpression.
    def enterLiteralExpression(self, ctx):
        ctx.literal ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#LiteralExpression.
    def exitLiteralExpression(self, ctx):
        ctx.value = ctx.literal ().value


    # Enter a parse tree produced by ECMAScriptParser#BitNotExpression.
    def enterBitNotExpression(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#BitNotExpression.
    def exitBitNotExpression(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#PostIncrementExpression.
    def enterPostIncrementExpression(self, ctx):
        ctx.singleExpression ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#PostIncrementExpression.
    def exitPostIncrementExpression(self, ctx):
        single = ctx.singleExpression ()
        ctx.value = []

        for leaf, value in zip (ctx.leaves, single.value):
            builder = Builder.new (leaf.getBB ())
            val = self.getVal (value, leaf)
            add = builder.add (val, Constant.int (Type.int (), 1))
            self.setVal (add, value, leaf)
            leaf.cacheInst (value, add)
            ctx.value.append (add)


    # Enter a parse tree produced by ECMAScriptParser#TypeofExpression.
    def enterTypeofExpression(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#TypeofExpression.
    def exitTypeofExpression(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#AssignmentOperatorExpression.
    def enterAssignmentOperatorExpression(self, ctx):
        ctx.singleExpression ().leaves = ctx.leaves
        ctx.expressionSequence ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#AssignmentOperatorExpression.
    def exitAssignmentOperatorExpression(self, ctx):
        single = ctx.singleExpression ()
        assignees = single.value
        operator = str (ctx.getChild (1).getText ())
        seq = ctx.expressionSequence ()
        assigners = seq.value
        ctx.value = []

        for leaf, assignee, assigner in zip (ctx.leaves, assignees, assigners):
            builder = Builder.new (leaf.getBB ())
            assignee_val = self.getVal (assignee, leaf)
            assigner_val = self.getVal (assigner, leaf)
            sym = self.sym_table_f[leaf.getFunc ()]

            if assigner_val.type != assignee_val.type:
                if self.asmType (type (assignee_val.type)) > self.asmType (type (assigner_val.type)):
                    assigner_val = builder.bitcast (assignee_val.type, assigner_val)
                else:
                    print assigner_val, assignee_val
                    assignee_val = builder.bitcast (assigner_val.type, assignee_val)

            if '+' in operator:
                if assignee_val.type == Type.int ():
                    val = builder.add (assignee_val, assigner_val)
                elif assignee_val.type == Type.float ():
                    val = builder.fadd (assignee_val, assigner_val)
            elif '-' in operator:
                if assignee_val.type == Type.int ():
                    val = builder.sub (assignee_val, assigner_val)
                elif assignee_val.type == Type.float ():
                    val = builder.fsub (assignee_val, assigner_val)
            elif '*' in operator:
                if assignee_val.type == Type.int ():
                    val = builder.mul (assignee_val, assigner_val)
                elif assignee_val.type == Type.float ():
                    val = builder.fmul (assignee_val, assigner_val)
            elif '/' in operator:
                if assignee_val.type == Type.int ():
                    val = builder.sdiv (assignee_val, assigner_val)
                elif assignee_val.type == Type.float ():
                    val = builder.fdiv (assignee_val, assigner_val)
            elif '%' in operator:
                if assignee_val.type == Type.int ():
                    val = builder.srem (assignee_val, assigner_val)
                elif assignee_val.type == Type.float ():
                    val = builder.frem (assignee_val, assigner_val)
            elif '|' in operator:
                if assignee_val.type != Type.int ():
                    assignee_val = builder.bitcast (Type.int (), assignee_val)
                if assigner_val.type != Type.int ():
                    assigner_val = builder.bitcast (Type.int (), assigner_val)
                val = builder.or_ (assignee_val, assigner_val)
            elif '&' in operator:
                if assignee_val.type != Type.int ():
                    assignee_val = builder.bitcast (Type.int (), assignee_val)
                if assigner_val.type != Type.int ():
                    assigner_val = builder.bitcast (Type.int (), assigner_val)
                val = builder.and_ (assignee_val, assigner_val)
            elif '>>>' in operator:
                if assignee_val.type != Type.int ():
                    assignee_val = builder.bitcast (Type.int (), assignee_val)
                if assigner_val.type != Type.int ():
                    assigner_val = builder.bitcast (Type.int (), assigner_val)
                val = builder.lshr (assignee_val, assigner_val)
            elif '>>' in operator:
                if assignee_val.type != Type.int ():
                    assignee_val = builder.bitcast (Type.int (), assignee_val)
                if assigner_val.type != Type.int ():
                    assigner_val = builder.bitcast (Type.int (), assinger_val)
                val = builder.ashr (assignee_val, assigner_val)

            store = self.setVal (val, assignee, leaf)
            leaf.cacheInst (assignee, val)
            ctx.value.append (assignee)


    # Enter a parse tree produced by ECMAScriptParser#NewExpression.
    def enterNewExpression(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#NewExpression.
    def exitNewExpression(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#PostDecreaseExpression.
    def enterPostDecreaseExpression(self, ctx):
        ctx.singleExpression ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#PostDecreaseExpression.
    def exitPostDecreaseExpression(self, ctx):
        single = ctx.singleExpression ()
        ctx.value = []

        for leaf, value in zip (ctx.leaves, single.value):
            builder = Builder.new (leaf.getBB ())
            val = self.getVal (value, leaf)
            add = builder.sub (val, Constant.int (Type.int (), 1))
            self.setVal (add, value, leaf)
            leaf.cacheInst (value, add)
            ctx.value.append (add)


    # Enter a parse tree produced by ECMAScriptParser#RelationalExpression.
    def enterRelationalExpression(self, ctx):
        singles = ctx.singleExpression ()

        for single in singles:
            single.leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#RelationalExpression.
    def exitRelationalExpression(self, ctx):
        comp_op = str (ctx.getChild (1))
        singles = ctx.singleExpression ()
        lhs_ctx = singles[0]
        rhs_ctx = singles[1]
        ctx.value = []

        for leaf, lhs, rhs in zip (ctx.leaves, singles[0].value, singles[1].value):
            builder = Builder.new (leaf.getBB ())
            lhs_val = self.getVal (lhs, leaf)
            rhs_val = self.getVal (rhs, leaf)
            if type (lhs_val) is int:
                lhs_val = Constant.int (Type.int (), lhs_val)
            elif type (lhs_val) is float:
                lhs_val = Constant.real (Type.float (), lhs_val)
            if type (rhs_val) is int:
                rhs_val = Constant.int (Type.int (), rhs_val)
            elif type (rhs_val) is float:
                rhs_val = Constant.real (Type.float (), rhs_val)


            if type (lhs_val.type) is IntegerType and type (rhs_val.type) is IntegerType:
                if comp_op == '<':
                    comp_opt = ICMP_SLT
                elif comp_op == '>':
                    comp_opt = ICMP_SGT
                elif comp_op == '<=':
                    comp_opt = ICMP_SLE
                else:
                    comp_opt = ICMP_SGE
                comp = builder.icmp
            else:
                if comp_op == '<':
                    comp_opt = FCMP_OLT
                elif comp_op == '>':
                    comp_opt = FCMP_OGT
                elif comp_op == '<=':
                    comp_opt = FCMP_OLE
                else:
                    comp_opt = FCMP_OGE
                comp = builder.fcmp

                if type (lhs_val.type) is IntegerType:
                    if type (lhs_val) is ConstantInt:
                        lhs_val = Constant.real (Type.float (), float (lhs_ctx.getText ()))
                    else:
                        lhs_val = builder.bitcast (lhs_val, Type.float ())
                if type (rhs_val.type) is IntegerType:
                    if type (rhs_val) is ConstantInt:
                        rhs_val = Constant.real (Type.float (), float (rhs_ctx.getText ()))
                    else:
                        rhs_val = builder.bitcast (rhs_val, Type.float ())

            ctx.value.append (comp (comp_opt, lhs_val, rhs_val))


    # Enter a parse tree produced by ECMAScriptParser#EqualityExpression.
    def enterEqualityExpression(self, ctx):
        singles = ctx.singleExpression ()

        for single in singles:
            single.leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#EqualityExpression.
    def exitEqualityExpression(self, ctx):
        comp_op = str (ctx.getChild (1))
        singles = ctx.singleExpression ()
        ctx.value = []

        for leaf, lhs, rhs in zip (ctx.leaves, singles[0].value, singles[1].value):
            builder = Builder.new (leaf.getBB ())
            lhs_val = self.getVal (lhs, leaf)
            rhs_val = self.getVal (rhs, leaf)
            if type (lhs_val) is int:
                lhs_val = Constant.int (Type.int (), lhs_val)
            elif type (lhs_val) is float:
                lhs_val = Constant.real (Type.float (), lhs_val)
            if type (rhs_val) is int:
                rhs_val = Constant.int (Type.int (), rhs_val)
            elif type (rhs_val) is float:
                rhs_val = Constant.real (Type.float (), rhs_val)

            if type (lhs_val.type) is IntegerType and type (rhs_val.type) is IntegerType:
                if comp_op == '==':
                    comp_opt = ICMP_EQ
                else:
                    comp_opt = ICMP_NE
                comp = builder.icmp
            else:
                if comp_op == '==':
                    comp_opt = FCMP_OEQ
                else:
                    comp_opt = FCMP_ONE
                comp = builder.fcmp

                if type (lhs_val.type) is IntegerType:
                    if type (lhs_val) is ConstantInt:
                        lhs_val = Constant.real (Type.float (), float (singles[0].getText ()))
                    else:
                        lhs_val = builder.bitcast (lhs_val, Type.float ())
                if type (rhs_val.type) is IntegerType:
                    if type (rhs_val) is ConstantInt:
                        rhs_val = Constant.real (Type.float (), float (singles[1].getText ()))
                    else:
                        rhs_val = builder.bitcast (rhs_val, Type.float ())

            ctx.value.append (comp (comp_opt, lhs_val, rhs_val))


    # Enter a parse tree produced by ECMAScriptParser#BitXOrExpression.
    def enterBitXOrExpression(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#BitXOrExpression.
    def exitBitXOrExpression(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#AdditiveExpression.
    def enterAdditiveExpression(self, ctx):
        singles = ctx.singleExpression ()

        for single in singles:
            single.leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#AdditiveExpression.
    def exitAdditiveExpression(self, ctx):
        ctx.value = []
        singles = ctx.singleExpression ()
        for leaf, lhs, rhs in zip (ctx.leaves, singles[0].value, singles[1].value):
            builder = Builder.new (leaf.getBB ())
            lhs_val = self.getVal (lhs, leaf)
            rhs_val = self.getVal (rhs, leaf)
            if type (lhs_val) is int:
                lhs_val = Constant.int (Type.int (), lhs_val)
            elif type (lhs_val) is float:
                lhs_val = Constant.real (Type.float (), lhs_val)
            if type (rhs_val) is int:
                rhs_val = Constant.int (Type.int (), rhs_val)
            elif type (rhs_val) is float:
                rhs_val = Constant.real (Type.float (), rhs_val)

            if type (lhs_val.type) is IntegerType and type (rhs_val.type) is IntegerType:
                add = builder.add
                sub = builder.sub
            else:
                add = builder.fadd
                sub = builder.fsub
                if type (lhs_val.type) is IntegerType:
                    if type (lhs_val) is ConstantInt:
                        lhs_val = Constant.real (Type.float (), lhs)
                    else:
                        lhs_val = builder.bitcast (lhs_val, Type.float ())
                if type (rhs_val.type) is IntegerType:
                    if type (rhs_val) is ConstantInt:
                        rhs_val = Constant.real (Type.float (), rhs)
                    else:
                        rhs_val = builder.bitcast (rhs_val, Type.float ())

            if ctx.getChild (1).getText () == '+':
                ctx.value.append (add (lhs_val, rhs_val))
            else:
                ctx.value.append (sub (lhs_val, rhs_val))


    # Enter a parse tree produced by ECMAScriptParser#MemberIndexExpression.
    def enterMemberIndexExpression(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#MemberIndexExpression.
    def exitMemberIndexExpression(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#ThisExpression.
    def enterThisExpression(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#ThisExpression.
    def exitThisExpression(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#MultiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx):
        singles = ctx.singleExpression ()

        for single in singles:
            single.leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#MultiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx):
        ctx.value = []
        singles = ctx.singleExpression ()

        for leaf, lhs, rhs in zip (ctx.leaves, singles[0].value, singles[1].value):
            builder = Builder.new (leaf.getBB ())
            lhs_val = self.getVal (lhs, leaf)
            rhs_val = self.getVal (rhs, leaf)

            if type (lhs_val) is int:
                lhs_val = Constant.int (Type.int (), lhs_val)
            elif type (lhs_val) is float:
                lhs_val = Constant.real (Type.float (), lhs_val)
            if type (rhs_val) is int:
                rhs_val = Constant.int (Type.int (), rhs_val)
            elif type (rhs_val) is float:
                rhs_val = Constant.real (Type.float (), rhs_val)

            val = None
            if type (lhs_val.type) is IntegerType and type (rhs_val.type) is IntegerType:
                mul = builder.mul
                div = builder.sdiv
                rem = builder.srem
            else:
                mul = builder.fmul
                div = builder.fdiv
                rem = builder.frem
                if type (lhs_val.type) is IntegerType:
                    if type (lhs_val) is ConstantInt:
                        lhs_val = Constant.real (Type.float (), singles[0].getText ())
                    else:
                        lhs_val = builder.bitcast (lhs_val, Type.float ())
                elif type (rhs_val.type) is IntegerType:
                    if type (rhs_val) is ConstantInt:
                        rhs_val = Constant.real (Type.float (), singles[1].getText ())
                    else:
                        rhs_val = builder.bitcast (rhs_val, Type.float ())
                else:
                    val = Constant.real (Type.float (), float ('nan'))

            if val is not None:
                ctx.value.append (val)
            else:
                operator = ctx.getChild (1).getText ()
                if operator == '*':
                    ctx.value.append (mul (lhs_val, rhs_val))
                elif operator == '/':
                    ctx.value.append (div (lhs_val, rhs_val))
                else:
                    ctx.value.append (rem (lhs_val, rhs_val))



    # Enter a parse tree produced by ECMAScriptParser#assignmentOperator.
    def enterAssignmentOperator(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#assignmentOperator.
    def exitAssignmentOperator(self, ctx):
        pass


    # Enter a parse tree produced by ECMAScriptParser#literal.
    def enterLiteral(self, ctx):
        if ctx.numericLiteral () is not None:
            ctx.numericLiteral ().leaves = ctx.leaves

    # Exit a parse tree produced by ECMAScriptParser#literal.
    def exitLiteral(self, ctx):
        if ctx.numericLiteral () is not None:
            ctx.value = ctx.numericLiteral ().value
        elif ctx.StringLiteral () is not None:
            ctx.value = Constant.string (str (ctx.StringLiteral ()))


    # Enter a parse tree produced by ECMAScriptParser#numericLiteral.
    def enterNumericLiteral(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#numericLiteral.
    def exitNumericLiteral(self, ctx):
        text = str (ctx.getText ())
        ctx.value = []
        for leaf in ctx.leaves:
            if '.' in text:
                ctx.value.append (Constant.real (Type.float (), float (str (ctx.getText ()))))
            else:
                ctx.value.append (Constant.int (Type.int (), int (str (ctx.getText ()))))


    # Enter a parse tree produced by ECMAScriptParser#identifierName.
    def enterIdentifierName(self, ctx):
        pass

    # Exit a parse tree produced by ECMAScriptParser#identifierName.
    def exitIdentifierName(self, ctx):
        pass


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



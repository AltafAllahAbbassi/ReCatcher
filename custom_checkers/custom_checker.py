from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker
from astroid import nodes

class UnnecessaryLambdaWithReduceChecker(BaseChecker):
    """Checker for unnecessary lambda functions with reduce."""
    __implements__ = IAstroidChecker

    name = 'unnecessary-lambda-with-reduce'
    priority = -1
    msgs = {
        'W9999': (
            'Unnecessary lambda function used with reduce',
            'unnecessary-lambda-with-reduce',
            'Used when a lambda function is used with reduce.',
        ),
    }

    def visit_call(self, node):
        """Visit call nodes to check for reduce with lambda."""
        if isinstance(node.func, nodes.Name) and node.func.name == 'reduce':
            if isinstance(node.args[0], nodes.Lambda):
                self.add_message('unnecessary-lambda-with-reduce', node=node)


class UnnecessaryConditionalBlockChecker(BaseChecker):
    """Checker for unnecessary conditional blocks."""
    __implements__ = IAstroidChecker

    name = 'unnecessary-conditional-block'
    priority = -1
    msgs = {
        'W8888': (
            'Unnecessary conditional block with return True/False',
            'unnecessary-conditional-block',
            'Used when an if statement can be simplified to a single return.',
        ),
    }

    def visit_if(self, node):
        """Visit if nodes to check for unnecessary conditional blocks."""
        # Check for an `if` block with `return True` and `return False`
        if (
            isinstance(node.body[0], nodes.Return)
            and isinstance(node.orelse[0], nodes.Return)
            and isinstance(node.body[0].value, nodes.Const)
            and isinstance(node.orelse[0].value, nodes.Const)
            and node.body[0].value.value is True
            and node.orelse[0].value.value is False
        ):
            self.add_message('unnecessary-conditional-block', node=node)


def register(linter):
    """Register the checkers with pylint."""
    linter.register_checker(UnnecessaryLambdaWithReduceChecker(linter))
    linter.register_checker(UnnecessaryConditionalBlockChecker(linter))

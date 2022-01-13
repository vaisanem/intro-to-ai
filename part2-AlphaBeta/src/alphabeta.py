TEMPLATE_FIELD = '|e|e|e|\n|e|e|e|\n|e|e|e|\n'
HUGE_NUMBER = 1000000


class AlphaBetaNode(object):
    def __init__(self):
        pass

    def generate_children(self):
        pass

    def is_max_node(self):
        pass

    def is_end_state(self):
        pass

    def value(self):
        pass


class TicTacToe(AlphaBetaNode):
    """Class that contains current state of the game and implements AlphaBetaNode methods
    :attr state: Current state of the board (str)
    :attr crosses_turn: Indicates whose turn it is (Boolean)
    """

    def __init__(self, state, crosses_turn):
        super().__init__()
        self.state = state
        self.crosses_turn = crosses_turn

    def is_end_state(self):
        return ('?' not in self.state) or self.won('x') or self.won('o')

    def won(self, c):
        triples = [self.state[0:3], self.state[3:6], self.state[6:9], self.state[::3], self.state[1::3],
                   self.state[2::3], self.state[0] + self.state[4] + self.state[8],
                   self.state[2] + self.state[4] + self.state[6]]
        combo = 3 * c
        return combo in triples

    def __str__(self):
        field = TEMPLATE_FIELD
        for c in self.state:
            field = field.replace('e', c, 1)

        return field

    def is_max_node(self):
        return self.crosses_turn

    def generate_children(self):
        """
        Generates list of all possible states after this turn
        :return: list of TicTacToe objects
        """
        all = []
        if self.is_end_state():
            return all
        c = 'x'
        if not self.is_max_node():
            c = 'o'
        for i in range(len(self.state)):
            if self.state[i] == '?':
                all.append(self.state[:i] + c + self.state[i+1:])        
        return all

    def value(self):
        """
        Current score of the game (0, 1, -1)
        :return: int
        """
        if self.is_end_state():
            if self.won('x'):
                return 1
            elif self.won('o'):
                return -1
        return 0


def alpha_beta_value(node: AlphaBetaNode):
    """Implements the MinMax algorithm with alpha-beta pruning
    :param node: State of the game (TicTacToe)
    :return: (int, AlphaBetaNode)
    """
    alpha = -1
    beta = 1
    if node.is_max_node():
        return max_value(node, alpha, beta)
    return min_value(node, alpha, beta)


def max_value(node: AlphaBetaNode, alpha, beta):
    if node.is_end_state():
        return (node.value(), node)
    all = node.generate_children()
    value_and_node = (-HUGE_NUMBER, TicTacToe(all[0], False))
    for one in all:
        next = TicTacToe(one, False)
        minimum = min_value(next, alpha, beta)[0]
        if value_and_node[0] < minimum:
            value_and_node = (minimum, next)
        alpha = max(alpha, value_and_node[0])
        if alpha >= beta:
            return value_and_node
    return value_and_node


def min_value(node: AlphaBetaNode, alpha, beta):
    if node.is_end_state():
        return (node.value(), node)
    all = node.generate_children()
    value_and_node = (HUGE_NUMBER, TicTacToe(all[0], True))
    for one in all:
        next = TicTacToe(one, True)
        maximum = max_value(next, alpha, beta)[0]
        if value_and_node[0] > maximum:
            value_and_node = (maximum, next)
        beta = min(beta, value_and_node[0])
        if alpha >= beta:
            return value_and_node
    return value_and_node

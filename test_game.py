import pytest
from game import TicTacToe

@pytest.fixture
def game():
    return TicTacToe()

def test_make_move_valid(game):
    assert game.make_move(1, 1, 'X') == True
    assert game.board[0] == 'X'

def test_make_move_invalid(game):
    game.make_move(1, 1, 'X')
    assert game.make_move(1, 1, 'O') == False

def test_check_winner_row(game):
    game.board = ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
    assert game.check_winner() == 'X'

def test_check_winner_column(game):
    game.board = ['O', ' ', ' ', 'O', ' ', ' ', 'O', ' ', ' ']
    assert game.check_winner() == 'O'

def test_check_winner_diagonal(game):
    game.board = ['X', ' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X']
    assert game.check_winner() == 'X'

def test_check_tie(game):
    game.board = ['X', 'O', 'X', 'X', 'O', 'O', 'O', 'X', 'X']
    assert game.check_winner() == 'Tie'

def test_reset_board(game):
    game.board = ['X'] * 9
    game.reset_board()
    assert game.board == [' '] * 9

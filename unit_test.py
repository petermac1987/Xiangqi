import unittest
import XiangqiGame as game

class TestListXiangqi(unittest.TestCase):

    def test_1(self):
        """
        Test for initial game state
        """
        a_game = game.XiangqiGame()
        a_game_state = a_game.get_game_state()
        self.assertIs('UNFINISHED', a_game_state)

    def test_2(self):
        """
        Test that the pieces have all the correct values.
        """
        piece_list = []
        general = piece_list.append(game.General('red'))
        advisor = piece_list.append(game.Advisor('red'))
        elephant = piece_list.append(game.Elephant('red'))
        horse = piece_list.append(game.Horse('red'))
        chariot = piece_list.append(game.Chariot('red'))
        cannon = piece_list.append(game.Cannon('red'))
        soldier = piece_list.append(game.Soldier('red'))

        # Check if location is None
        for i in piece_list:
            self.assertIs(None, i.get_location(), 'Initial location is not None')

        for i in piece_list:
            if i is general:
                self.assertTrue(general.get_in_check(), 'General is not in check')

    def test_3(self):
        """
        Test adding pieces to the board
        """
        a_game = game.XiangqiGame()
        a_placement = a_game.set_active(game.General('red'), 'e1')
        self.assertTrue(a_placement, 'Piece did not pass placement')
        a_next_placement = a_game.set_active(game.Advisor('black'), 'e11')
        self.assertFalse(a_next_placement, 'Placement allowed illegal placement of piece')
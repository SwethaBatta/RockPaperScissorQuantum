# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 08:48:30 2020

@author: SwethaBatta
"""

import unittest
import profile
from RockPaperScissors import RockPaperScissors

class TestRockPaperScissors(unittest.TestCase):
      def setUp(self):
          self.rps = RockPaperScissors()

class TestInit(TestRockPaperScissors):
      def test_initial_userscore(self):
          self.assertEqual(self.rps.USER_SCORE, 0)

      def test_initial_compscore(self):
          self.assertEqual(self.rps.COMP_SCORE, 0)

      def test_initial_userchoice(self):
          self.assertEqual(self.rps.USER_CHOICE, "")

      def test_initial_compchoice(self):
          self.assertEqual(self.rps.COMP_CHOICE, "")
          
      def test_initial_winner(self):
          self.assertEqual(self.rps.WINNER, "")

      def test_initial_inputs(self):
          self.assertEqual(self.rps.inputs, [])          
          

class TestCheckInputRepeat(TestRockPaperScissors):
      def test_array_append_inputs(self):
          self.rps.checkInputRepeat('rock')       
          self.assertEqual(self.rps.inputs, ['rock'])
          
      def test_array_consecutive_additions(self):
          self.rps.checkInputRepeat('scissors')
          self.rps.checkInputRepeat('paper')
          self.rps.checkInputRepeat('rock')
          self.rps.checkInputRepeat('rock')
          self.assertEqual(self.rps.checkInputRepeat('rock'), True)

      def test_array_random_additions(self):
          self.rps.checkInputRepeat('scissors')
          self.rps.checkInputRepeat('paper')
          self.rps.checkInputRepeat('rock')
          self.rps.checkInputRepeat('paper')
          self.assertEqual(self.rps.checkInputRepeat('rock'), False)
      
      def test_array_less_than_length_condition(self):
          self.rps.checkInputRepeat('rock')
          self.rps.checkInputRepeat('paper')
          self.assertEqual(self.rps.checkInputRepeat('paper'), False)
          
      def test_array_meets_length_condition(self):
          self.rps.checkInputRepeat('rock')
          self.rps.checkInputRepeat('paper')
          self.rps.checkInputRepeat('paper')
          self.assertEqual(self.rps.checkInputRepeat('paper'), True)      
          
class TestChoiceToNumber(TestRockPaperScissors):
      def test_choice_to_number_rock(self):                
          self.assertEqual(self.rps.choice_to_number('rock') , 0)  
          
      def test_choice_to_number_paper(self):                
          self.assertEqual(self.rps.choice_to_number('paper') , 1)    
          
      def test_choice_to_number_scissor(self):                
          self.assertEqual(self.rps.choice_to_number('scissor') , 2)    


class TestNumberToChoice(TestRockPaperScissors):
      def test_number_to_choice_0(self):                
          self.assertEqual(self.rps.number_to_choice(0) , 'rock')  
          
      def test_number_to_choice_1(self):                
          self.assertEqual(self.rps.number_to_choice(1) , 'paper')    
          
      def test_number_to_choice_2(self):                
          self.assertEqual(self.rps.number_to_choice(2) , 'scissor') 
          
class TestRandomComputerChoice(TestRockPaperScissors):
      def test_random_computer_choice(self):
          self.assertIn(self.rps.random_computer_choice(), ['rock', 'paper', 'scissor'])

class TestResult(TestRockPaperScissors):
      def test_tie_case_rock(self):
          self.rps.result('rock', 'rock')
          self.assertEqual(self.rps.WINNER, 'Tie')

      def test_tie_user_score_rock(self):
          self.rps.result('rock', 'rock')
          self.assertEqual(self.rps.USER_SCORE, self.rps.USER_SCORE)
 
      def test_tie_computer_score_rock(self):
          self.rps.result('rock', 'rock')
          self.assertEqual(self.rps.COMP_SCORE, self.rps.COMP_SCORE)

      def test_tie_case_paper(self):
          self.rps.result('paper', 'paper')
          self.assertEqual(self.rps.WINNER, 'Tie')

      def test_tie_user_score_paper(self):
          self.rps.result('paper', 'paper')
          self.assertEqual(self.rps.USER_SCORE, self.rps.USER_SCORE)
 
      def test_tie_computer_score_paper(self):
          self.rps.result('paper', 'paper')
          self.assertEqual(self.rps.COMP_SCORE, self.rps.COMP_SCORE)

      def test_tie_case_scissor(self):
          self.rps.result('scissor', 'scissor')
          self.assertEqual(self.rps.WINNER, 'Tie')

      def test_tie_user_score_scissor(self):
          self.rps.result('scissor', 'scissor')
          self.assertEqual(self.rps.USER_SCORE, self.rps.USER_SCORE)
 
      def test_tie_computer_score_scissor(self):
          self.rps.result('scissor', 'scissor')
          self.assertEqual(self.rps.COMP_SCORE, self.rps.COMP_SCORE)
        
      def test_user_win_case_rock_scissor(self):
          self.rps.result('rock', 'scissor')
          self.assertEqual(self.rps.WINNER, 'You win')

      def test_user_win_user_score_rock_scissor(self):
          prev_USER_SCORE = self.rps.USER_SCORE
          self.rps.result('rock', 'scissor')
          self.assertEqual(self.rps.USER_SCORE, prev_USER_SCORE+1)
 
      def test_user_win_computer_score_rock_scissor(self):
          self.rps.result('rock', 'scissor')
          self.assertEqual(self.rps.COMP_SCORE, self.rps.COMP_SCORE)
 
      def test_user_win_case_paper_rock(self):
          self.rps.result('paper', 'rock')
          self.assertEqual(self.rps.WINNER, 'You win')

      def test_user_win_user_score_paper_rock(self):
          prev_USER_SCORE = self.rps.USER_SCORE
          self.rps.result('paper', 'rock')
          self.assertEqual(self.rps.USER_SCORE, prev_USER_SCORE+1)
 
      def test_user_win_computer_score_paper_rock(self):
          self.rps.result('paper', 'rock')
          self.assertEqual(self.rps.COMP_SCORE, self.rps.COMP_SCORE)

      def test_user_win_case_scissor_paper(self):
          self.rps.result('scissor', 'paper')
          self.assertEqual(self.rps.WINNER, 'You win')

      def test_user_win_user_score_scissor_paper(self):
          prev_USER_SCORE = self.rps.USER_SCORE
          self.rps.result('scissor', 'paper')
          self.assertEqual(self.rps.USER_SCORE, prev_USER_SCORE+1)
 
      def test_user_win_computer_score_scissor_paper(self):
          self.rps.result('scissor', 'paper')
          self.assertEqual(self.rps.COMP_SCORE, self.rps.COMP_SCORE)

      def test_computer_wins_case_scissor_rock(self):
          self.rps.result('scissor', 'rock')
          self.assertEqual(self.rps.WINNER, 'Computer wins')          
      
      def test_computer_win_user_score_scissor_rock(self):
          self.rps.result('scissor', 'rock')
          self.assertEqual(self.rps.USER_SCORE, self.rps.USER_SCORE)
 
      def test_computer_win_computer_score_scissor_rock(self):
          prev_COMPUTER_SCORE = self.rps.COMP_SCORE
          self.rps.result('scissor', 'rock')
          self.assertEqual(self.rps.COMP_SCORE, prev_COMPUTER_SCORE+1)
     
      def test_computer_wins_case_rock_paper(self):
          self.rps.result('rock', 'paper')
          self.assertEqual(self.rps.WINNER, 'Computer wins')          
      
      def test_computer_win_user_score_rock_paper(self):
          self.rps.result('rock', 'paper')
          self.assertEqual(self.rps.USER_SCORE, self.rps.USER_SCORE)
 
      def test_computer_win_computer_score_rock_paper(self):
          prev_COMPUTER_SCORE = self.rps.COMP_SCORE
          self.rps.result('rock', 'paper')
          self.assertEqual(self.rps.COMP_SCORE, prev_COMPUTER_SCORE+1)

      def test_computer_wins_case_paper_scissor(self):
          self.rps.result('paper', 'scissor')
          self.assertEqual(self.rps.WINNER, 'Computer wins')          
      
      def test_computer_win_user_score_paper_scissor(self):
          self.rps.result('paper', 'scissor')
          self.assertEqual(self.rps.USER_SCORE, self.rps.USER_SCORE)
 
      def test_computer_win_computer_score_paper_scissor(self):
          prev_COMPUTER_SCORE = self.rps.COMP_SCORE
          self.rps.result('paper', 'scissor')
          self.assertEqual(self.rps.COMP_SCORE, prev_COMPUTER_SCORE+1)
          
class TestAction(TestRockPaperScissors):
      def test_case_repeatInputs(self):
          self.rps.inputs = ['rock', 'paper', 'scissor', 'rock', 'rock']
          self.rps.action('rock')
          self.assertEqual(self.rps.COMP_CHOICE, 'rock')

      def test_case_quantumRandom(self):
          self.rps.inputs = ['rock', 'paper', 'scissor', 'rock', 'paper']
          self.rps.action('rock')
          self.assertIn(self.rps.COMP_CHOICE, ['rock', 'paper', 'scissor'])
          
class TestQuantumRandomNumber(TestRockPaperScissors):          
      def test_quantum_random_number(self):
          self.assertIn((self.rps.qrand.rand_int())%3, [0, 1, 2])
          
if __name__ == '__main__':
    unittest.main()   
    profile.run('main()')
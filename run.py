# You're not allowed to change this file
from ple.games.flappybird import FlappyBird
from ple import PLE
import numpy as np
import FlappyPolicy

game = FlappyBird()
p = PLE(game, fps=30, frame_skip=1, num_steps=1, force_fps=False, display_screen=True)

p.init()
reward = 0.0

nb_games = 100
cumulated = np.zeros((nb_games))

for i in range(nb_games):
    p.reset_game()
    
    while(not p.game_over()):
        state = game.getGameState()
        screen = p.getScreenRGB()
        action=FlappyPolicy(state, screen) ### Your job is to define this function.
        
        reward = p.act(action)
        cumulated[i] = cumulated[i] + reward

average_score = np.mean(cumulated)
max_score = np.max(cumulated)

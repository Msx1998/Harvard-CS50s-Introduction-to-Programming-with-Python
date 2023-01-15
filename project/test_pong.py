import pygame
import pytest
from pong import Pong


@pytest.fixture
def pong_game():
    game = Pong(3, "player_name", 2, (400, 300))
    return game


def test_create_score_text(pong_game):
    pong_game.create_score_text()
    assert isinstance(pong_game.player_score_text, pygame.Surface)
    assert isinstance(pong_game.opponent_score_text, pygame.Surface)


def test_move_ball(pong_game):
    pong_game.move_ball()
    assert pong_game.ball.x != pong_game.screen_width / 2 - 15
    assert pong_game.ball.y != pong_game.screen_height / 2 - 15


def test_score(pong_game):
    pong_game.player_score = 3
    pong_game.score()
    assert pong_game.player_score == 3
    assert pong_game.opponent_score == 0

import pytest
from project import validate_game_over_score, validate_game_over_text, validate_ball_speed, validate_frame_width, validate_frame_height


def test_validate_game_over_score():
    assert validate_game_over_score("5") == 5
    assert validate_game_over_score("-5") == -5


def test_validate_game_over_text():
    assert validate_game_over_text("John Doe") == "John Doe"


def test_validate_ball_speed():
    assert validate_ball_speed("5") == 5
    assert validate_ball_speed("-5") == -5


def test_validate_frame_width():
    assert validate_frame_width("500") == 500
    assert validate_frame_width("-500") == -500


def test_validate_frame_height():
    assert validate_frame_height("500") == 500
    assert validate_frame_height("-500") == -500

from pong import Pong


def main():
    try:
        game_over_score = validate_game_over_score(input("Enter the game over score: "))
        game_over_text = validate_game_over_text(input("Enter your name: "))
        ball_speed = validate_ball_speed(input("Enter the ball speed: "))
        width = validate_frame_width(input("Enter the frame width: "))
        height = validate_frame_height(input("Enter the frame height: "))
        Pong(game_over_score, game_over_text, ball_speed, width, height).run()
        print("Starting Pong game...")
    except ValueError:
        print("Invalid input. Please enter a valid value.")
        main()


def validate_game_over_score(score):
    try:
        return int(score)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return validate_game_over_score(input("Enter the game over score: "))


def validate_game_over_text(text):
    if len(text) > 0:
        return text
    else:
        print("Invalid input. Please enter a non empty string.")
        return validate_game_over_text(input("Enter your name: "))


def validate_ball_speed(speed):
    try:
        return int(speed)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return validate_ball_speed(input("Enter the ball speed: "))


def validate_frame_width(width):
    try:
        return int(width)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return validate_frame_width(input("Enter the frame width: "))


def validate_frame_height(height):
    try:
        return int(height)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return validate_frame_height(input("Enter the frame height: "))


if __name__ == '__main__':
    main()

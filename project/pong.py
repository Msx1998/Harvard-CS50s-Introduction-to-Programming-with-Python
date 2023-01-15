import pygame
import random
import sys


class Pong:

    def __init__(self, game_over_score, name, difficulty, screen_width, screen_height):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.game_over_score = game_over_score
        self.name = name

        # frame style
        self.screen_width, self.screen_height = screen_width, screen_height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Pong')

        # shapes
        self.ball = pygame.Rect(self.screen_width / 2 - 15, self.screen_height / 2 - 15, 30, 30)
        self.player = pygame.Rect(self.screen_width - 20, self.screen_height / 2 - 70, 10, 140)
        self.opponent = pygame.Rect(10, self.screen_height / 2 - 70, 10, 140)

        # ball speed
        self.ball_speed_x = difficulty * random.choice((1, -1))
        self.ball_speed_y = difficulty * random.choice((1, -1))

        # player speed
        self.player_speed = 0

        # colors
        self.bg_color = pygame.Color('black')
        self.white = (255, 255, 255)

        # score
        self.player_score = 0
        self.opponent_score = 0
        self.player_score_text = None
        self.opponent_score_text = None
        self.create_score_text()

    def create_score_text(self):
        font = pygame.font.Font(None, 30)
        self.player_score_text = font.render("Player: 0", True, self.white)
        self.opponent_score_text = font.render("Opponent: 0", True, self.white)

    def update_score_text(self):
        font = pygame.font.Font(None, 30)
        self.player_score_text = font.render("Player: {}".format(self.player_score), True, self.white)
        self.opponent_score_text = font.render("Opponent: {}".format(self.opponent_score), True, self.white)

    def move_ball(self):

        # ball animation
        self.ball.x += self.ball_speed_x
        self.ball.y += self.ball_speed_y

        # ball collision
        if self.ball.top <= 0 or self.ball.bottom >= self.screen_height:
            self.ball_speed_y *= -1
        if self.ball.left <= 0 or self.ball.right >= self.screen_width:
            self.ball_speed_x *= -1
        if self.ball.left <= 0:
            self.player_score += 1
        if self.ball.right >= self.screen_width:
            self.opponent_score += 1
        self.update_score_text()

        self.score()

        # ball collision with player
        if self.ball.colliderect(self.player) or self.ball.colliderect(self.opponent):
            self.ball_speed_x *= -1

    def score(self):
        if self.player_score == self.game_over_score or self.opponent_score == self.game_over_score:
            font = pygame.font.Font(None, 50)
            if self.player_score == self.game_over_score:
                game_over_text = font.render(f"{self.name}, You win!", True, self.white)
            else:
                game_over_text = font.render("Game Over, You lose!", True, self.white)
            self.screen.blit(game_over_text, (self.screen_width / 2 - 150, self.screen_height / 2))
            pygame.display.update()
            pygame.time.wait(1000)

    def update_visuals(self):
        self.screen.fill(self.bg_color)
        pygame.draw.rect(self.screen, self.white, self.player)
        pygame.draw.rect(self.screen, self.white, self.opponent)
        pygame.draw.ellipse(self.screen, self.white, self.ball)
        pygame.draw.aaline(self.screen, self.white, (self.screen_width / 2, 0),
                           (self.screen_width / 2, self.screen_height))
        self.screen.blit(self.player_score_text, (self.screen_width * 3 / 4 - 50, 20))
        self.screen.blit(self.opponent_score_text, (self.screen_width / 4 - 100, 20))
        pygame.display.update()

    def player_movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if self.player.y > 0:
                self.player.y -= 5
        if keys[pygame.K_DOWN]:
            if self.player.y < self.screen_height - self.player.height:
                self.player.y += 5

    def opponent_movement(self):
        if self.ball.x < self.screen_width / 1.25:
            if self.opponent.top < self.ball.y:
                self.opponent.top += 7
            if self.opponent.bottom > self.ball.y:
                self.opponent.bottom -= 7

    def end_game(self):
        if self.player_score == self.game_over_score or self.opponent_score == self.game_over_score:
            pygame.quit()
            sys.exit()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.player_movement()
            self.opponent_movement()
            self.move_ball()
            self.update_visuals()
            self.end_game()

            # controls FPS
            pygame.display.flip()
            self.clock.tick(60)

import pygame

from conf import SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT, ACCENT_COLOR, BASIC_FONT

class GameManager:
    def __init__(self, main_sprite, ball_group, paddle_group):
        self.player_score = 0
        self.opponent_score = 0
        self.display_main_screen = True
        self.main_sprite = main_sprite
        self.ball_group = ball_group
        self.paddle_group = paddle_group
        self.n_players = 0
        self.main_screen_colors = [(255, 255, 255), (119, 136, 153)]

    def run_main_screen(self):
        self.main_sprite.draw(SCREEN)
        self.generate_player_text(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 250, "1 PLAYER", self.main_screen_colors[self.n_players])
        self.generate_player_text(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 300, "2 PLAYER", self.main_screen_colors[self.n_players - 1])

    def run_game(self):
        # Drawing the game objects
        self.paddle_group.draw(SCREEN)
        self.ball_group.draw(SCREEN)

        # Updating the game objects
        self.paddle_group.update(self.ball_group)
        self.ball_group.update()
        self.reset_ball()
        self.draw_score()

    def reset_ball(self):
        if self.ball_group.sprite.rect.right >= SCREEN_WIDTH:
            self.opponent_score += 1
            self.ball_group.sprite.reset_ball()
        if self.ball_group.sprite.rect.left <= 0:
            self.player_score += 1
            self.ball_group.sprite.reset_ball()

    def draw_score(self):
        player_score = BASIC_FONT.render(str(self.player_score), True, ACCENT_COLOR)
        opponent_score = BASIC_FONT.render(str(self.opponent_score), True, ACCENT_COLOR)

        player_score_rect = player_score.get_rect(midleft=(SCREEN_WIDTH / 2 + 40, SCREEN_HEIGHT / 2))
        opponent_score_rect = opponent_score.get_rect(midright=(SCREEN_WIDTH / 2 - 40, SCREEN_HEIGHT / 2))

        SCREEN.blit(player_score, player_score_rect)
        SCREEN.blit(opponent_score, opponent_score_rect)

    def generate_player_text(self, x_pos, y_pos, text, color):
        player = BASIC_FONT.render(text, True, color)
        player_container = player.get_rect(center=(x_pos, y_pos))
        pygame.draw.rect(SCREEN, (0, 0, 0), player_container)
        SCREEN.blit(player, player_container)

    def get_display_main_screen(self):
        return self.display_main_screen

    def set_display_main_screen(self, value):
        assert isinstance(value, bool)
        self.display_main_screen = value

    def update_players(self):
        self.n_players = (self.n_players + 1) % 2
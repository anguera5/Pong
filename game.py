import pygame, sys

from conf import SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT, BASIC_FONT, ACCENT_COLOR, BG_COLOR, MID_LINE, CLOCK
from players import Player, Opponent
from ball import Ball
from block import Block
from gamemanager import GameManager



# Main Window
pygame.display.set_caption('Pong')

main_screen = Block('assets/Initial.png', 150, 90)
main_screen.scale(SCREEN_WIDTH, SCREEN_HEIGHT)
main_sprite = pygame.sprite.GroupSingle()
main_sprite.add(main_screen)

game_manager = GameManager(main_sprite, None, None)


while True:
    # Background Stuff
    SCREEN.fill(BG_COLOR)
    pygame.draw.rect(SCREEN, ACCENT_COLOR, MID_LINE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if game_manager.get_display_main_screen():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_manager.set_display_main_screen(False)
                if event.key in [pygame.K_DOWN, pygame.K_UP]:
                    game_manager.update_players()
    game_manager.run_main_screen()
    if game_manager.get_display_main_screen() is False:
        break
    # Rendering
    pygame.display.flip()
    CLOCK.tick(120)

n_players = game_manager.n_players
# Game objects
player = Player('assets/Paddle.png', SCREEN_WIDTH - 20, SCREEN_HEIGHT / 2, 5)
opponent = Player('assets/Paddle.png', 20, SCREEN_HEIGHT / 2, 5) if n_players == 1 else \
    Opponent('assets/Paddle.png', 20, SCREEN_WIDTH / 2, 5)
paddle_group = pygame.sprite.Group()
paddle_group.add(player)
paddle_group.add(opponent)

ball = Ball('assets/Ball.png', SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 4, 4, paddle_group)
ball_sprite = pygame.sprite.GroupSingle()
ball_sprite.add(ball)

game_manager = GameManager(main_sprite, ball_sprite, paddle_group)
if n_players != game_manager.n_players:
    game_manager.update_players()

while True:
    # Background Stuff
    SCREEN.fill(BG_COLOR)
    pygame.draw.rect(SCREEN, ACCENT_COLOR, MID_LINE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.movement -= player.speed
            if event.key == pygame.K_DOWN:
                player.movement += player.speed
            if game_manager.n_players == 1 and event.key == pygame.K_w:
                opponent.movement -= opponent.speed
            if game_manager.n_players == 1 and event.key == pygame.K_s:
                opponent.movement += opponent.speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.movement += player.speed
            if event.key == pygame.K_DOWN:
                player.movement -= player.speed
            if game_manager.n_players == 1 and event.key == pygame.K_w:
                opponent.movement += opponent.speed
            if game_manager.n_players == 1 and event.key == pygame.K_s:
                opponent.movement -= opponent.speed

    # Run the game
    game_manager.run_game()

    # Rendering
    pygame.display.flip()
    CLOCK.tick(120)

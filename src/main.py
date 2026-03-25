import sys
import pygame
import random

from config import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    WINDOW_TITLE,
    BACKGROUND_COLOR,
    FPS,
    DEFAULT_RULE,
    DEFAULT_STEPS_PER_FRAME,
    MIN_STEPS_PER_FRAME,
    MAX_STEPS_PER_FRAME,
)
from simulator import Simulator
from renderer import Renderer

def ask_color_mode():
    user_input = input(
        "Choose color mode (grayscale / rainbow / random) "
        "(Enter = random): "
    ).strip().lower()

    if user_input == "":
        return random.choice(["grayscale", "rainbow", "random"])

    if user_input not in ("grayscale", "rainbow", "random"):
        print("Invalid choice, using random.")
        return random.choice(["grayscale", "rainbow", "random"])

    return user_input


def ask_rule_string():
    user_input = input(
        f"Enter rule string using L and R "
        f"(For default rule, press ENTER! {DEFAULT_RULE}): "
    ).strip().upper()

    if user_input == "":
        return DEFAULT_RULE
    
    for char in user_input:
        if char not in ("L", "R"):
            print("Invalid input. Only use L and R.")
            print(f"Using default rule: {DEFAULT_RULE}")
            return DEFAULT_RULE
    return user_input




def main():
    rule_string = ask_rule_string()
    color_mode = ask_color_mode()

    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(WINDOW_TITLE)

    clock = pygame.time.Clock()
    running = True

    simulator = Simulator(rule_string)
    renderer = Renderer(screen, color_mode)

    is_running = False
    steps_per_frame = DEFAULT_STEPS_PER_FRAME

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    simulator.step()

                elif event.key == pygame.K_RETURN:
                    is_running = not is_running

                elif event.key == pygame.K_UP:
                    steps_per_frame += 1
                    if steps_per_frame > MAX_STEPS_PER_FRAME:
                        steps_per_frame = MAX_STEPS_PER_FRAME

                elif event.key == pygame.K_DOWN:
                    steps_per_frame -= 1
                    if steps_per_frame < MIN_STEPS_PER_FRAME:
                        steps_per_frame = MIN_STEPS_PER_FRAME

        if is_running:
            for _ in range(steps_per_frame):
                simulator.step()

        screen.fill(BACKGROUND_COLOR)

        renderer.draw_grid()
        renderer.draw_cells(simulator)
        renderer.draw_ant(simulator)
        renderer.draw_hud(simulator, is_running, steps_per_frame)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
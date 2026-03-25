import pygame
import colorsys
import random

from config import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    CELL_SIZE,
    GRID_LINE_COLOR,
    ANT_COLOR,
    TEXT_COLOR
)

class Renderer:
    def __init__(self, screen, color_mode):
        self.screen = screen
        self.font = pygame.font.SysFont("consolas", 22)
        self.color_mode = color_mode
        self.random_colors = {}



    def get_origin(self):
        origin_x = WINDOW_WIDTH // 2 - CELL_SIZE // 2
        origin_y = WINDOW_HEIGHT // 2 - CELL_SIZE // 2
        return origin_x, origin_y

    def get_color_for_state(self, state, max_state):
        if state == 0:
            return None

        if self.color_mode == "grayscale":
            intensity = 60 + int (195 * state / max_state)
            return (intensity, intensity, intensity)

        elif self.color_mode == "rainbow":
            hue = state / max_state
            r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
            return (int(r * 255), int(g * 255), int(b * 255))

        elif self.color_mode == "random":
            if state not in self.random_colors:
                self.random_colors[state] = (
                    random.randint(50, 255),
                    random.randint(50, 255),
                    random.randint(50, 255)
                )
            return self.random_colors[state]

        return (255, 255, 255)
    
    def draw_grid(self):
        origin_x, origin_y = self.get_origin()

        start_x = origin_x % CELL_SIZE
        start_y = origin_y % CELL_SIZE

        for x in range(start_x, WINDOW_WIDTH, CELL_SIZE):
            pygame.draw.line(
                self.screen,
                GRID_LINE_COLOR,
                (x, 0),
                (x, WINDOW_HEIGHT)
            )

        for y in range(start_y, WINDOW_HEIGHT, CELL_SIZE):
            pygame.draw.line(
                self.screen,
                GRID_LINE_COLOR,
                (0, y),
                (WINDOW_WIDTH, y)
            )

    def draw_cells(self, simulator):
        origin_x, origin_y = self.get_origin()
        max_state = simulator.state_count -1 if simulator.state_count > 1 else 1

        for (cell_x, cell_y), state in simulator.grid.items():
            color = self.get_color_for_state(state, max_state)

            if color is None:
                continue
            
            pixel_x = origin_x + cell_x * CELL_SIZE
            pixel_y = origin_y + cell_y * CELL_SIZE

            cell_rect = pygame.Rect(
                pixel_x,
                pixel_y,
                CELL_SIZE,
                CELL_SIZE
            )

            pygame.draw.rect(self.screen, color, cell_rect)



    def draw_ant(self, simulator):

        origin_x, origin_y = self.get_origin()

        pixel_x = origin_x + simulator.ant_x * CELL_SIZE
        pixel_y = origin_y + simulator.ant_y * CELL_SIZE
        
        ant_rect = pygame.Rect(
            pixel_x,
            pixel_y,
            CELL_SIZE,
            CELL_SIZE
        )

        pygame.draw.rect(self.screen, ANT_COLOR, ant_rect)


    def draw_hud(self, simulator, is_running, steps_per_frame):
        running_text = "RUNNING" if is_running else "PAUSED"

        lines = [
            f"Steps: {simulator.step_count}",
            f"Mode: {running_text}",
            f"Steps/frame: {steps_per_frame}",
            f"Rule: {simulator.rule_string}",
            f"Color mode: {self.color_mode}",
            "SPACE = step",
            "ENTER = run/pause",
            "UP/DOWN = speed",
        ]

        x = 20
        y = 20

        for line in lines:
            text_surface = self.font.render(line, True, TEXT_COLOR)
            self.screen.blit(text_surface, (x, y))
            y += 28
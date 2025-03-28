import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 600
HEADER_HEIGHT = 80
FOOTER_HEIGHT = 80
GAME_AREA_SIZE = WINDOW_WIDTH
WINDOW_HEIGHT = GAME_AREA_SIZE + HEADER_HEIGHT + FOOTER_HEIGHT
PADDING = 10
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (150, 255, 150)  # Lighter green for background
RED = (255, 150, 150)    # Lighter red for background
GRAY = (128, 128, 128)
LIGHT_GRAY = (240, 240, 240)
DARK_GREEN = (0, 180, 0)  # Darker green for text
DARK_RED = (180, 0, 0)    # Darker red for text

# Level configurations: (rows, cols)
LEVEL_CONFIGS = {
    1: (1, 2),  # 2 cells
    2: (2, 2),  # 4 cells
    3: (2, 3),  # 6 cells
    4: (2, 4),  # 8 cells
    5: (3, 3),  # 9 cells
    6: (3, 4),  # 12 cells
    7: (4, 4),  # 16 cells
    8: (4, 5),  # 20 cells
    9: (5, 5)   # 25 cells
}

class Card:
    def __init__(self, number, x, y, card_size):
        self.number = number
        self.x = x
        self.y = y + HEADER_HEIGHT  # Offset y position by header height
        self.card_size = card_size
        self.rect = pygame.Rect(self.x, self.y, card_size - PADDING * 2, card_size - PADDING * 2)
        self.revealed = True
        self.color = GRAY if number is None else WHITE
        self.clicked = False
        self.is_empty = (number is None)

    def draw(self, screen, font):
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 2)
        if self.revealed and not self.is_empty:
            text = font.render(str(self.number), True, BLACK)
            text_rect = text.get_rect(center=self.rect.center)
            screen.blit(text, text_rect)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Ayumu Memory Game")
        self.font = pygame.font.Font(None, 72)
        self.small_font = pygame.font.Font(None, 36)
        self.cards = []
        self.current_number = 1
        self.game_state = "SETUP"
        self.start_time = 0
        self.current_level = 1
        self.max_number = 9
        self.setup_game()

    def draw_header(self):
        # Draw header background
        header_rect = pygame.Rect(0, 0, WINDOW_WIDTH, HEADER_HEIGHT)
        pygame.draw.rect(self.screen, LIGHT_GRAY, header_rect)
        pygame.draw.line(self.screen, BLACK, (0, HEADER_HEIGHT), (WINDOW_WIDTH, HEADER_HEIGHT))

        # Draw level indicator on the left
        level_text = self.small_font.render(f"Level: {self.current_level}", True, BLACK)
        self.screen.blit(level_text, (20, HEADER_HEIGHT // 2 - 15))

        # Draw timer in memorization phase
        if self.game_state == "MEMORIZE":
            memo_time = self.get_memorization_time()
            remaining = int(memo_time - (time.time() - self.start_time))
            timer_text = self.small_font.render(f"Memorize: {remaining}s", True, BLACK)
            timer_rect = timer_text.get_rect(center=(WINDOW_WIDTH // 2, HEADER_HEIGHT // 2))
            self.screen.blit(timer_text, timer_rect)

    def draw_footer(self):
        footer_y = HEADER_HEIGHT + GAME_AREA_SIZE
        footer_rect = pygame.Rect(0, footer_y, WINDOW_WIDTH, FOOTER_HEIGHT)

        if self.game_state == "GAMEOVER":
            # Red background for game over
            pygame.draw.rect(self.screen, RED, footer_rect)
            text = self.font.render("Game Over! Space to restart", True, DARK_RED)
        elif self.game_state == "LEVELUP":
            # Green background for level up
            pygame.draw.rect(self.screen, GREEN, footer_rect)
            text = self.font.render(f"Level {self.current_level}! Space to start", True, DARK_GREEN)
        else:
            # Normal background when playing
            pygame.draw.rect(self.screen, LIGHT_GRAY, footer_rect)
            text = self.font.render("", True, BLACK)

        text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, footer_y + FOOTER_HEIGHT // 2))
        self.screen.blit(text, text_rect)
        pygame.draw.line(self.screen, BLACK, (0, footer_y), (WINDOW_WIDTH, footer_y))

    def calculate_card_size(self, rows, cols):
        return min(GAME_AREA_SIZE // cols, GAME_AREA_SIZE // rows)

    def setup_game(self):
        self.current_number = 1
        rows, cols = LEVEL_CONFIGS[self.current_level]
        card_size = self.calculate_card_size(rows, cols)
        
        total_cells = rows * cols
        numbers_to_use = min(total_cells, self.max_number)
        
        numbers = list(range(1, numbers_to_use + 1))
        empty_cells = [None] * (total_cells - numbers_to_use)
        all_values = numbers + empty_cells
        random.shuffle(all_values)
        
        self.cards = []
        
        # Center the grid in the game area (between header and footer)
        start_x = (WINDOW_WIDTH - (cols * card_size)) // 2
        start_y = (GAME_AREA_SIZE - (rows * card_size)) // 2
        
        for i in range(rows):
            for j in range(cols):
                x = start_x + j * card_size + PADDING
                y = start_y + i * card_size + PADDING
                value = all_values[i * cols + j]
                self.cards.append(Card(value, x, y, card_size))
        
        self.start_time = time.time()
        self.game_state = "MEMORIZE"

    def get_memorization_time(self):
        if self.current_level <= 2:
            return 2
        elif self.current_level <= 4:
            return 3
        elif self.current_level <= 6:
            return 5
        else:
            return 8

    def handle_click(self, pos):
        if self.game_state != "PLAYING":
            return

        for card in self.cards:
            if card.rect.collidepoint(pos) and not card.clicked and not card.is_empty:
                card.revealed = True
                if card.number == self.current_number:
                    card.color = GREEN
                    card.clicked = True
                    self.current_number += 1
                    if all(card.clicked or card.is_empty for card in self.cards):
                        if self.current_level < len(LEVEL_CONFIGS):
                            self.current_level += 1
                            self.game_state = "LEVELUP"
                        else:
                            self.game_state = "GAMEOVER"
                else:
                    card.color = RED
                    self.game_state = "GAMEOVER"

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(event.pos)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and (self.game_state == "GAMEOVER" or self.game_state == "LEVELUP"):
                        self.setup_game()

            self.screen.fill(WHITE)
            
            # Draw header
            self.draw_header()

            # Handle memorization period
            if self.game_state == "MEMORIZE":
                memo_time = self.get_memorization_time()
                if time.time() - self.start_time >= memo_time:
                    self.game_state = "PLAYING"
                    for card in self.cards:
                        card.revealed = False

            # Draw all cards
            for card in self.cards:
                card.draw(self.screen, self.font)

            # Draw footer
            self.draw_footer()

            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()

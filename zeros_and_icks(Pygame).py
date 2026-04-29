import pygame
import sys

pygame.init()

lines_wight = 15
figures_wight = 12.5
cell_size = 200
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Крестики-Нолики')
field_color = (245,245,245)
lines_color = (205,205,205)
x_color = (255,0,0)
o_color = (0,0,255)
l_color = (205,205,0)
board = [None] * 9
current_player = 'x'
font = pygame.font.SysFont('Arial', 72, bold=True)
game_over = False
winner_text = ""
def draw_lines():
    for i in range(1, 3):
        pygame.draw.line(screen, lines_color, (0, i * cell_size), (600, i * cell_size), lines_wight)
    for i in range(1, 3):
        pygame.draw.line(screen, lines_color, (i * cell_size, 0), (i * cell_size, 600), lines_wight)

def draw_objects():
    for i in range(9):
        row = i // 3
        col = i % 3
        center_x = col * cell_size + cell_size // 2
        center_y = row * cell_size + cell_size // 2
        
        if board[i] == 'x':

            pygame.draw.line(screen, x_color, (center_x - 85, center_y - 85), (center_x + 85, center_y + 85), 12)
            pygame.draw.line(screen, x_color, (center_x + 85, center_y - 85), (center_x - 85, center_y + 85), 12)
        elif board[i] == 'o':
            pygame.draw.circle(screen, o_color, (center_x, center_y), 87.5, 10)

def check_winner():
    win_coords = [(0,1,2), (3,4,5), (6,7,8),(0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)           ]
    for r in win_coords:
        if board[r[0]] == board[r[1]] == board[r[2]] and board[r[0]] is not None:
            return board[r[0]]
    return None
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if not game_over: 
                mouse_x, mouse_y = event.pos
                col = mouse_x // cell_size
                row = mouse_y // cell_size
                index = row * 3 + col
            
            if board[index] is None:
                board[index] = current_player
                winner = check_winner()
                if winner:
                    winner_text = f"Победил {winner.upper()}!"
                    game_over = True
                elif None not in board: 
                    winner_text = "Ничья!"
                    game_over = True
                if current_player == 'x':
                    current_player = 'o'  
                else: 
                    current_player = 'x'
    screen.fill(field_color)
    draw_lines()
    draw_objects()
    if game_over:
        text_img = font.render(winner_text, True, (0, 0, 0))

        text_rect = text_img.get_rect(center=(600//2, 600//2))
        pygame.draw.rect(screen, (255, 255, 255), text_rect.inflate(20, 20))

        screen.blit(text_img, text_rect)
    pygame.display.update()

pygame.quit()
sys.exit()
import pygame
import modules

player_one = []

modules.zer_matrix(player_one)

pygame.init()

screen = pygame.display.set_mode([1000, 700])
pygame.display.set_caption("MorskoyBoy")

svin1 = pygame.image.load('images/Odinarni_svin.jpg')
svin1_pos = (350, 600)
doMove = False

clock = pygame.time.Clock()
run = True
while run:
    pygame.time.delay(100)

    WIDTH = 18
    HEIGHT = 18
    MARGIN = 2

    up_after_down = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # левая кнопка мыши
                doMove = True
                up_after_down = False
        if event.type == pygame.MOUSEBUTTONUP:
            doMove = False
            up_after_down = True

        if event.type == pygame.MOUSEMOTION and doMove == True:
            svin1_pos = event.pos

        if up_after_down:
            end_pos = event.pos
            # User clicks the mouse. Get the position
            # Change the x/y screen coordinates to grid coordinates
            column = (end_pos[0] - 140) // (WIDTH + MARGIN)
            row = (end_pos[1] - 200) // (HEIGHT + MARGIN)
            # Set that location to one
            player_one[row][column] = 1
            print("Click ", end_pos, "Grid coordinates: ", row, column)
            # modules.show_matrix(player_one)


    color_line = [80, 80, 80]

    screen.fill([255, 255, 255])
    for y_offset in range(0, 200, 20):
        pygame.draw.line(screen, color_line, [140, 200 + y_offset], [340, 200 + y_offset], 2)
        pygame.draw.line(screen, color_line, [140 + y_offset, 200], [140 + y_offset, 400], 2)
    pygame.draw.line(screen, color_line, [140, 400], [340, 400], 2)
    pygame.draw.line(screen, color_line, [340, 200], [340, 400], 2)
    for y_offset in range(0, 200, 20):
        pygame.draw.line(screen, color_line, [660, 200 + y_offset], [860, 200 + y_offset], 2)
        pygame.draw.line(screen, color_line, [660 + y_offset, 200], [660 + y_offset, 400], 2)
    pygame.draw.line(screen, color_line, [660, 400], [860, 400], 2)
    pygame.draw.line(screen, color_line, [860, 200], [860, 400], 2)


    for row in range(10):
        for column in range(10):
            color = (5, 40, 120)
            if player_one[row][column] == 1:
                end_pos = [(MARGIN + WIDTH) * column + MARGIN + 141, (MARGIN + HEIGHT) * row + MARGIN + 201, WIDTH, HEIGHT]
                screen.blit(svin1, end_pos)
                svin1_pos = (1100, 0)
            else:
                pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN + 140, (MARGIN + HEIGHT) * row + MARGIN + 200, WIDTH, HEIGHT])

    for row in range(10):
        for column in range(10):
            color = (5, 40, 120)
            # if player_one[row][column] == 1:
            #     color = (255, 255, 255)
            pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN + 660, (MARGIN + HEIGHT) * row + MARGIN + 200, WIDTH, HEIGHT])

    screen.blit(svin1, svin1_pos)
    pygame.display.update()
    clock.tick(60)


pygame.quit()


import pygame
import modules

player_one = []
modules.zer_matrix(player_one)

pygame.init()

screen = pygame.display.set_mode([1000, 700])
pygame.display.set_caption("MorskoyBoy")

svin1 = pygame.image.load('images/Odinarni_svin.jpg')
svin1_pos = (350, 600)
svins1_pos = [svin1_pos, svin1_pos, svin1_pos, svin1_pos]
svins1_pos_num = 0

svin2 = pygame.image.load('images/Dvoinoi_svin.jpg')
svin2_pos = (400, 600)
svins2_pos = [svin2_pos, svin2_pos, svin2_pos]
svins2_rotate = []
svins2_pos_num = 0
rotated_svin2 = pygame.transform.rotate(svin2, 0)
rotated_svin2_bool = False
angle_svin2 = 0  # градусы поворота свиньи


svin3 = pygame.image.load('images/Troinoi_svin.jpg')
svin3_pos = (450, 600)
svins3_pos = [svin2_pos, svin2_pos, svin2_pos]
svins3_rotate = []
svins3_pos_num = 0
rotated_svin3 = pygame.transform.rotate(svin3, 0)
rotated_svin3_bool = False
angle_svin3 = 0  # градусы поворота свиньи


clock = pygame.time.Clock()
run = True

doMove = False

# def events(svins_pos,  max_num):
#
#     global run, end_pos, doMove, up_after_down, player_one
#
#     svins_pos_num = 0
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#         if svins_pos_num == max_num:
#             break
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             if event.button == 1:  # левая кнопка мыши
#                 doMove = True
#                 up_after_down = False
#         if event.type == pygame.MOUSEBUTTONUP:
#             doMove = False
#             up_after_down = True
#
#         if event.type == pygame.MOUSEMOTION and doMove == True:
#             svins_pos[svins_pos_num] = event.pos
#
#         if up_after_down:
#             end_pos = event.pos
#             # User clicks the mouse. Get the position
#             # Change the x/y screen coordinates to grid coordinates
#             column = (end_pos[0] - 140) // (WIDTH + MARGIN)
#             row = (end_pos[1] - 200) // (HEIGHT + MARGIN)
#             # Set that location to one
#             player_one[row][column] = 1
#             print("Click ", end_pos, "Grid coordinates: ", row, column)
#             # modules.show_matrix(player_one)
#             svins_pos[svins_pos_num] = (1100, 0)
#             if svins_pos_num < max_num:
#                 svins_pos_num += 1

while run:
    pygame.time.delay(100)


    WIDTH = 18
    HEIGHT = 18
    MARGIN = 2

    up_after_down = False

    # events(svins1_pos, 4)
    # events(svins2_pos, 3)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # одинарные свиньи
        if svins1_pos_num < 4:
            # if svins1_pos_num == 4:
            #     break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # левая кнопка мыши
                    doMove = True
                    up_after_down = False
            if event.type == pygame.MOUSEBUTTONUP:
                doMove = False
                up_after_down = True

            if event.type == pygame.MOUSEMOTION and doMove:
                svins1_pos[svins1_pos_num] = event.pos

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
                svins1_pos[svins1_pos_num] = (1100, 0)
                if svins1_pos_num < 4:
                    svins1_pos_num += 1
                if svins1_pos_num == 4:
                    continue

        # двойные свиньи
        if (svins1_pos_num == 4) and (svins2_pos_num < 3):
            # if svins2_pos_num == 3:
            #     break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # левая кнопка мыши
                    doMove = True
                    up_after_down = False
                elif event.button == 3:
                    if angle_svin2 == 360:
                        angle_svin2 = 90
                    else:
                        angle_svin2 += 90
                    rotated_svin2 = pygame.transform.rotate(svin2, angle_svin2)
                    rotated_svin2_bool = True
            if event.type == pygame.MOUSEBUTTONUP:
                doMove = False
                if event.button == 1:
                    up_after_down = True

            if event.type == pygame.MOUSEMOTION and doMove:
                svins2_pos[svins2_pos_num] = event.pos

            if up_after_down:
                svin2_mass = []
                end_pos = event.pos
                # User clicks the mouse. Get the position
                # Change the x/y screen coordinates to grid coordinates
                column = (end_pos[0] - 140) // (WIDTH + MARGIN)
                row = (end_pos[1] - 200) // (HEIGHT + MARGIN)
                # Set that location to one
                if angle_svin2 % 180 == 0 or angle_svin2 % 360 == 0:
                    player_one[row][column] = 1
                    player_one[row][column+1] = 1
                elif angle_svin2 % 90 == 0 or angle_svin2 % 270 == 0:
                    player_one[row][column] = 1
                    player_one[row + 1][column] = 1
                svin2_mass.append(rotated_svin2)
                end_pos = [(MARGIN + WIDTH) * column + MARGIN + 141, (MARGIN + HEIGHT) * row + MARGIN + 201, WIDTH,
                           HEIGHT]
                svin2_mass.append(end_pos)
                svins2_rotate.append(svin2_mass)

                print("Click ", end_pos, "Grid coordinates: ", row, column)
                # modules.show_matrix(player_one)
                svins2_pos[svins2_pos_num] = (1100, 0)
                if svins2_pos_num < 3:
                    svins2_pos_num += 1

        # тройные свиньи
        if (svins2_pos_num == 3) and (svins3_pos_num < 2):
            # if svins2_pos_num == 3:
            #     break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # левая кнопка мыши
                    doMove = True
                    up_after_down = False
                elif event.button == 3:
                    if angle_svin3 == 360:
                        angle_svin3 = 90
                    else:
                        angle_svin3 += 90
                    rotated_svin3 = pygame.transform.rotate(svin2, angle_svin3)
                    rotated_svin3_bool = True
            if event.type == pygame.MOUSEBUTTONUP:
                doMove = False
                if event.button == 1:
                    up_after_down = True

            if event.type == pygame.MOUSEMOTION and doMove:
                svins3_pos[svins3_pos_num] = event.pos

            if up_after_down:
                svin3_mass = []
                end_pos = event.pos
                # User clicks the mouse. Get the position
                # Change the x/y screen coordinates to grid coordinates
                column = (end_pos[0] - 140) // (WIDTH + MARGIN)
                row = (end_pos[1] - 200) // (HEIGHT + MARGIN)
                # Set that location to one
                if angle_svin3 % 180 == 0 or angle_svin3 % 360 == 0:
                    player_one[row][column] = 1
                    player_one[row][column+1] = 1
                elif angle_svin3 % 90 == 0 or angle_svin3 % 270 == 0:
                    player_one[row][column] = 1
                    player_one[row + 1][column] = 1
                svin3_mass.append(rotated_svin2)
                end_pos = [(MARGIN + WIDTH) * column + MARGIN + 141, (MARGIN + HEIGHT) * row + MARGIN + 201, WIDTH,
                           HEIGHT]
                svin3_mass.append(end_pos)
                svins3_rotate.append(svin3_mass)

                print("Click ", end_pos, "Grid coordinates: ", row, column)
                # modules.show_matrix(player_one)
                svins3_pos[svins3_pos_num] = (1100, 0)
                if svins3_pos_num < 2:
                    svins3_pos_num += 1


    color_line = [80, 80, 80]

    screen.fill([255, 255, 255])
    for y_offset in range(0, 200, 20):
        pygame.draw.line(screen, [80, 80, 80], [140, 200 + y_offset], [340, 200 + y_offset], 2)
        pygame.draw.line(screen, [80, 80, 80], [140 + y_offset, 200], [140 + y_offset, 400], 2)
    pygame.draw.line(screen, [80, 80, 80], [140, 400], [340, 400], 2)
    pygame.draw.line(screen, [80, 80, 80], [340, 200], [340, 400], 2)
    for y_offset in range(0, 200, 20):
        pygame.draw.line(screen, [80, 80, 80], [660, 200 + y_offset], [860, 200 + y_offset], 2)
        pygame.draw.line(screen, [80, 80, 80], [660 + y_offset, 200], [660 + y_offset, 400], 2)
    pygame.draw.line(screen, [80, 80, 80], [660, 400], [860, 400], 2)
    pygame.draw.line(screen, [80, 80, 80], [860, 200], [860, 400], 2)

    for row in range(10):
        for column in range(10):
            color = (5, 40, 120)
            if player_one[row][column] == 1:
                end_pos = [(MARGIN + WIDTH) * column + MARGIN + 141, (MARGIN + HEIGHT) * row + MARGIN + 201, WIDTH, HEIGHT]
                screen.blit(svin1, end_pos)
            else:
                pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN + 140, (MARGIN + HEIGHT) * row + MARGIN + 200, WIDTH, HEIGHT])

    # двойные свиньи
    for i in range(svins2_pos_num):
        screen.blit(svins2_rotate[i][0], svins2_rotate[i][1])

    for row in range(10):
        for column in range(10):
            color = (5, 40, 120)
            # if player_one[row][column] == 1:
            #     color = (255, 255, 255)
            pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN + 660, (MARGIN + HEIGHT) * row + MARGIN + 200, WIDTH, HEIGHT])

    # Свиньи одинарные
    # screen.blit(svin1, svin1_pos)
    for i in range(4):
        screen.blit(svin1, svins1_pos[i])
        pygame.display.update()

    if rotated_svin2_bool == False:
        for i in range(3):
            screen.blit(svin2, svins2_pos[i])
            pygame.display.update()
    else:
        if svins2_pos_num < 3:
            screen.blit(rotated_svin2, svins2_pos[svins2_pos_num])
            pygame.display.update()

    for i in range(svins2_pos_num):
        screen.blit(svins2_rotate[i][0], svins2_rotate[i][1])

    if rotated_svin3_bool == False:
        for i in range(3):
            screen.blit(svin3, svins3_pos[i])
            pygame.display.update()
    else:
        if svins3_pos_num < 3:
            screen.blit(rotated_svin3, svins3_pos[svins3_pos_num])
            pygame.display.update()


    pygame.display.update()
    clock.tick(60)


pygame.quit()


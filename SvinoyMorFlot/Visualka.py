import pygame
import modules

player_one = []
player_two = []
modules.zer_matrix(player_one)
modules.zer_matrix(player_two)

pygame.init()

screen = pygame.display.set_mode([1000, 700])  # создание окна
pygame.display.set_caption("MorskoyBoy")  # название окна (отображается сверху)

svin1 = pygame.image.load('images/Odinarni_svin.jpg')
svin1_pos = (350, 600)  # координаты свинки
svins1_pos = [svin1_pos, svin1_pos, svin1_pos, svin1_pos]  # массив со свиньями
svins1_pos_num = 0  # кол-во уже поставленных на поле свиней

svin2 = pygame.image.load('images/Dvoinoi_svin.jpg')
svin2_pos = (400, 600)
svins2_pos = [svin2_pos, svin2_pos, svin2_pos]
svins2_rotate = []  # массив с перевернутыми свиньями
svins2_pos_num = 0
rotated_svin2 = pygame.transform.rotate(svin2, 0)  # переменная с поворотом свиньи (по дефолту 0 градусов)
rotated_svin2_bool = False  # показывает, повернута ли свинья
angle_svin2 = 0  # градусы поворота свиньи


svin3 = pygame.image.load('images/Troinoi_svin.jpg')
svin3_pos = (450, 600)
svins3_pos = [svin3_pos, svin3_pos]
svins3_rotate = []
svins3_pos_num = 0
rotated_svin3 = pygame.transform.rotate(svin3, 0)
rotated_svin3_bool = False
angle_svin3 = 0  # градусы поворота свиньи

svin4 = pygame.image.load('images/Kvadro_svintus.jpg')
svin4_pos = (520, 600)
svins4_pos = [svin4_pos]
svins4_rotate = []
svins4_pos_num = 0
rotated_svin4 = pygame.transform.rotate(svin3, 0)
rotated_svin4_bool = False
angle_svin4 = 0  # градусы поворота свиньи

player_one_ready = False  # если тру - то матрица закрывается (после расстановки всех свиней первым игроком)
player_two_ready = False
# player_two_reload = False  # обнуление параметров свиней для второго игрока

clock = pygame.time.Clock()
run = True  # заставляет главный цикл игры работать (если фолс, то игра вырубается)

doMove = False  # переменная, отвечающая за перемещение мыши

def check_around(matrix, row, col):  # функция, которая окружает свинку нулями, чтобы нельзя было ставить рядом других свиней
    if row - 1 >= 0 and col - 1 >= 0:
        if matrix[row - 1][col - 1] != 1:
            matrix[row - 1][col - 1] = 0
    if row - 1 >= 0 and col >= 0:
        if matrix[row - 1][col] != 1:
            matrix[row - 1][col] = 0
    if row - 1 >= 0 and col + 1 <= 9:
        if matrix[row - 1][col + 1] != 1:
            matrix[row - 1][col + 1] = 0
    if row >= 0 and col + 1 <= 9:
        if matrix[row][col + 1] != 1:
            matrix[row][col + 1] = 0
    if row + 1 <= 9 and col + 1 <= 9:
        if matrix[row + 1][col + 1] != 1:
            matrix[row + 1][col + 1] = 0
    if row + 1 <= 9 and col >= 0:
        if matrix[row + 1][col] != 1:
            matrix[row + 1][col] = 0
    if row + 1 <= 9 and col - 1 >= 0:
        if matrix[row + 1][col - 1] != 1:
            matrix[row + 1][col - 1] = 0
    if row >= 0 and col - 1 >= 0:
        if matrix[row][col - 1] != 1:
            matrix[row][col - 1] = 0

while run:  # основной цикл игры
    pygame.time.delay(100)  # это вроде как кол-во кадров в сек (а может и нет, я не помню сори)

    # размер клеточек и марджин - толщина полосочки
    WIDTH = 18
    HEIGHT = 18
    MARGIN = 2

    up_after_down = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # если нажимаешь на крестик, игра закрывается (без этого условия на крестик не закроется)
            run = False

        # одинарные свиньи
        if player_one_ready == False:
            if svins1_pos_num < 4:
                if event.type == pygame.MOUSEBUTTONDOWN:  # кнопка мыши нажата
                    if event.button == 1:  # левая кнопка мыши
                        doMove = True
                        up_after_down = False  # для того, чтобы следующее условие выполнилось только после нажатия кнопки мышки
                if event.type == pygame.MOUSEBUTTONUP:  # кнопка мышки не нажата (или отпущена)
                    doMove = False  # следование свинки за мышкой прекращается
                    up_after_down = True

                if event.type == pygame.MOUSEMOTION and doMove:  # следование свинки за мышкой
                    svins1_pos[svins1_pos_num] = event.pos

                if up_after_down:  # после того, кам мы нажали и после отпустили кнопку мыши
                    end_pos = event.pos  # позия мышки, в которой мы отжали кнопку
                    column = (end_pos[0] - 140) // (WIDTH + MARGIN)  # вычисление столбца матрицы по последней координате мышки
                    row = (end_pos[1] - 200) // (HEIGHT + MARGIN)  # вычисление строки матрицы по последней координате мышки
                    # Set that location to one
                    if player_one[row][column] != 1 and player_one[row][column] != 0:  # не выполнится, если на этом месте уже стоит винка или там стоит 0, что означает позицию рядом со свинкой
                        player_one[row][column] = 1
                        check_around(player_one, row, column)  # окружает свинку ноликами (это видно в терминальной матрице)
                        print("Click ", end_pos, "Grid coordinates: ", row, column)  # просто выводит позицию мышки и строку со столбцом в матрице (можно убрать)
                        # modules.show_matrix(player_one)
                        svins1_pos[svins1_pos_num] = (1100, 0)  # свинка улетает за экран
                        modules.show_matrix(player_one)  # для дебага - выводит консольную матрицу
                        if svins1_pos_num < 4:
                            svins1_pos_num += 1  # увеличиваем счетчик кол-ва одинарных свиней на поле
                        if svins1_pos_num == 4:  # переводит нас на след условие, если все свиньи расставлены
                            continue

            # двойные свиньи
            if (svins1_pos_num == 4) and (svins2_pos_num < 3):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # левая кнопка мыши
                        doMove = True
                        up_after_down = False
                    elif event.button == 3:  # поворот свиньи
                        if angle_svin2 == 360:  # andle - градус поворота
                            angle_svin2 = 90  # сделано для упрощения написания условия с градусами поворота (см далее)
                        else:
                            angle_svin2 += 90
                        rotated_svin2 = pygame.transform.rotate(svin2, angle_svin2)  # поворот свиньи на определенный градус
                        rotated_svin2_bool = True  # показывает, что свинья была повернута (нужно для корректного вывода картинки)
                if event.type == pygame.MOUSEBUTTONUP:
                    doMove = False
                    if event.button == 1:
                        up_after_down = True

                if event.type == pygame.MOUSEMOTION and doMove:
                    svins2_pos[svins2_pos_num] = event.pos

                if up_after_down:
                    svin2_mass = []  # массив с перевернутыми и неперевернутыми свиньями
                    end_pos = event.pos
                    # User clicks the mouse. Get the position
                    # Change the x/y screen coordinates to grid coordinates
                    column = (end_pos[0] - 140) // (WIDTH + MARGIN)
                    row = (end_pos[1] - 200) // (HEIGHT + MARGIN)
                    # Set that location to one
                    if player_one[row][column] != 1 and player_one[row][column] != 0:
                        if angle_svin2 % 180 == 0 or angle_svin2 % 360 == 0:  # проверка того, в какую сторону заполнять матрицу (вправо или вниз)
                            if column + 1 <= 9:  # для избежания ошибки index out of range
                                if player_one[row][column + 1] != 1 and player_one[row][column + 1] != 0:  # проверка всех частей тела свинью на близость к другим свинбям
                                    player_one[row][column] = 1
                                    check_around(player_one, row, column)
                                    player_one[row][column + 1] = 1
                                    check_around(player_one, row, column + 1)

                                    svin2_mass.append(rotated_svin2)
                                    end_pos = [(MARGIN + WIDTH) * column + MARGIN + 141, (MARGIN + HEIGHT) * row + MARGIN + 201,
                                               WIDTH,
                                               HEIGHT]
                                    svin2_mass.append(end_pos)
                                    svins2_rotate.append(svin2_mass)

                                    print("Click ", end_pos, "Grid coordinates: ", row, column)
                                    # modules.show_matrix(player_one)
                                    svins2_pos[svins2_pos_num] = (1100, 0)
                                    modules.show_matrix(player_one)
                                    if svins2_pos_num < 3:
                                        svins2_pos_num += 1
                                    if svins2_pos_num == 3:
                                        continue
                        elif angle_svin2 % 90 == 0 or angle_svin2 % 270 == 0:
                            if row + 1 <= 9:
                                if player_one[row + 1][column] != 1 and player_one[row + 1][column] != 0:
                                    player_one[row][column] = 1
                                    check_around(player_one, row, column)
                                    player_one[row + 1][column] = 1
                                    check_around(player_one, row + 1, column)

                                    svin2_mass.append(rotated_svin2)
                                    end_pos = [(MARGIN + WIDTH) * column + MARGIN + 141, (MARGIN + HEIGHT) * row + MARGIN + 201, WIDTH,
                                               HEIGHT]
                                    svin2_mass.append(end_pos)
                                    svins2_rotate.append(svin2_mass)

                                    print("Click ", end_pos, "Grid coordinates: ", row, column)
                                    # modules.show_matrix(player_one)
                                    svins2_pos[svins2_pos_num] = (1100, 0)
                                    modules.show_matrix(player_one)
                                    if svins2_pos_num < 3:
                                        svins2_pos_num += 1
                                    if svins2_pos_num == 3:
                                        continue

            # тройные свиньи
            if (svins2_pos_num == 3) and (svins3_pos_num < 2):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # левая кнопка мыши
                        doMove = True
                        up_after_down = False
                    elif event.button == 3:
                        if angle_svin3 == 360:
                            angle_svin3 = 90
                        else:
                            angle_svin3 += 90
                        rotated_svin3 = pygame.transform.rotate(svin3, angle_svin3)
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
                    if player_one[row][column] != 1 and player_one[row][column] != 0:
                        if angle_svin3 % 180 == 0 or angle_svin3 % 360 == 0:
                            if column + 1 <= 9 and column + 2 <= 9:
                                if player_one[row][column + 1] != 1 and player_one[row][column + 1] != 0 and player_one[row][column + 2] != 1 and player_one[row][column + 2] != 0:
                                    player_one[row][column] = 1
                                    check_around(player_one, row, column)
                                    player_one[row][column + 1] = 1
                                    check_around(player_one, row, column + 1)
                                    player_one[row][column + 2] = 1
                                    check_around(player_one, row, column + 2)

                                    svin3_mass.append(rotated_svin3)
                                    end_pos = [(MARGIN + WIDTH) * column + MARGIN + 141, (MARGIN + HEIGHT) * row + MARGIN + 201,
                                               WIDTH,
                                               HEIGHT]
                                    svin3_mass.append(end_pos)
                                    svins3_rotate.append(svin3_mass)

                                    modules.show_matrix(player_one)
                                    print("Click ", end_pos, "Grid coordinates: ", row, column)
                                    # modules.show_matrix(player_one)
                                    svins3_pos[svins3_pos_num] = (1100, 0)
                                    if svins3_pos_num < 2:
                                        svins3_pos_num += 1
                                    if svins3_pos_num == 2:
                                        continue
                        elif angle_svin3 % 90 == 0 or angle_svin3 % 270 == 0:
                            if row + 1 <= 9 and row + 2 <= 9:
                                if player_one[row + 1][column] != 1 and player_one[row + 1][column] != 0 and player_one[row + 2][column] != 1 and player_one[row + 2][column] != 0:
                                    player_one[row][column] = 1
                                    check_around(player_one, row, column)
                                    player_one[row + 1][column] = 1
                                    check_around(player_one, row + 1, column)
                                    player_one[row + 2][column] = 1
                                    check_around(player_one, row + 2, column)
                                    svin3_mass.append(rotated_svin3)
                                    end_pos = [(MARGIN + WIDTH) * column + MARGIN + 141, (MARGIN + HEIGHT) * row + MARGIN + 201, WIDTH,
                                               HEIGHT]
                                    svin3_mass.append(end_pos)
                                    svins3_rotate.append(svin3_mass)

                                    modules.show_matrix(player_one)
                                    print("Click ", end_pos, "Grid coordinates: ", row, column)
                                    # modules.show_matrix(player_one)
                                    svins3_pos[svins3_pos_num] = (1100, 0)
                                    if svins3_pos_num < 2:
                                        svins3_pos_num += 1
                                    if svins3_pos_num == 2:
                                        continue

            # тройные свиньи
            if (svins3_pos_num == 2) and (svins4_pos_num < 1):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # левая кнопка мыши
                        doMove = True
                        up_after_down = False
                    elif event.button == 3:
                        if angle_svin4 == 360:
                            angle_svin4 = 90
                        else:
                            angle_svin4 += 90
                        rotated_svin4 = pygame.transform.rotate(svin4, angle_svin4)
                        rotated_svin4_bool = True
                if event.type == pygame.MOUSEBUTTONUP:
                    doMove = False
                    if event.button == 1:
                        up_after_down = True

                if event.type == pygame.MOUSEMOTION and doMove:
                    svins4_pos[svins4_pos_num] = event.pos

                if up_after_down:
                    svin4_mass = []
                    end_pos = event.pos
                    # User clicks the mouse. Get the position
                    # Change the x/y screen coordinates to grid coordinates
                    column = (end_pos[0] - 140) // (WIDTH + MARGIN)
                    row = (end_pos[1] - 200) // (HEIGHT + MARGIN)
                    # Set that location to one
                    if player_one[row][column] != 1 and player_one[row][column] != 0:
                        if angle_svin4 % 180 == 0 or angle_svin4 % 360 == 0:
                            if column + 1 <= 9 and column + 2 <= 9 and column + 3 <= 9:
                                if player_one[row][column + 1] != 1 and player_one[row][column + 1] != 0 and player_one[row][column + 2] != 1 and player_one[row][column + 2] != 0 and player_one[row][column + 3] != 1 and player_one[row][column + 3] != 0:
                                    player_one[row][column] = 1
                                    check_around(player_one, row, column)
                                    player_one[row][column + 1] = 1
                                    check_around(player_one, row, column + 1)
                                    player_one[row][column + 2] = 1
                                    check_around(player_one, row, column + 2)
                                    player_one[row][column + 3] = 1
                                    check_around(player_one, row, column + 3)

                                    svin4_mass.append(rotated_svin4)
                                    end_pos = [(MARGIN + WIDTH) * column + MARGIN + 141, (MARGIN + HEIGHT) * row + MARGIN + 201,
                                               WIDTH,
                                               HEIGHT]
                                    svin4_mass.append(end_pos)
                                    svins4_rotate.append(svin4_mass)

                                    modules.show_matrix(player_one)
                                    print("Click ", end_pos, "Grid coordinates: ", row, column)
                                    # modules.show_matrix(player_one)
                                    svins4_pos[svins4_pos_num] = (1100, 0)
                                    if svins4_pos_num < 1:
                                        svins4_pos_num += 1
                                    if svins4_pos_num == 1:
                                        player_one_ready = True
                        elif angle_svin4 % 90 == 0 or angle_svin4 % 270 == 0:
                            if row + 1 <= 9 and row + 2 <= 9 and row + 3 <= 9:
                                if player_one[row + 1][column] != 1 and player_one[row + 1][column] != 0 and player_one[row + 2][column] != 1 and player_one[row + 2][column] != 0 and player_one[row + 3][column] != 1 and player_one[row + 3][column] != 0:
                                    player_one[row][column] = 1
                                    check_around(player_one, row, column)
                                    player_one[row + 1][column] = 1
                                    check_around(player_one, row + 1, column)
                                    player_one[row + 2][column] = 1
                                    check_around(player_one, row + 2, column)
                                    player_one[row + 3][column] = 1
                                    check_around(player_one, row + 3, column)

                                    svin4_mass.append(rotated_svin4)
                                    end_pos = [(MARGIN + WIDTH) * column + MARGIN + 141, (MARGIN + HEIGHT) * row + MARGIN + 201, WIDTH,
                                                HEIGHT]
                                    svin4_mass.append(end_pos)
                                    svins4_rotate.append(svin4_mass)

                                    modules.show_matrix(player_one)
                                    print("Click ", end_pos, "Grid coordinates: ", row, column)
                                    # modules.show_matrix(player_one)
                                    svins4_pos[svins4_pos_num] = (1100, 0)
                    if svins4_pos_num < 1:
                        svins4_pos_num += 1
                    if svins4_pos_num == 1:
                        svins1_pos_num = 0
                        svins1_pos = [svin1_pos, svin1_pos, svin1_pos, svin1_pos]

                        svins2_rotate = []  # массив с перевернутыми свиньями
                        svins2_pos_num = 0
                        svins2_pos = [svin2_pos, svin2_pos, svin2_pos]
                        rotated_svin2 = pygame.transform.rotate(svin2,
                                                                0)  # переменная с поворотом свиньи (по дефолту 0 градусов)
                        rotated_svin2_bool = False  # показывает, повернута ли свинья
                        angle_svin2 = 0  # градусы поворота свиньи

                        svins3_rotate = []
                        svins3_pos_num = 0
                        svins3_pos = [svin3_pos, svin3_pos]
                        rotated_svin3 = pygame.transform.rotate(svin3, 0)
                        rotated_svin3_bool = False
                        angle_svin3 = 0  # градусы поворота свиньи

                        svins4_rotate = []
                        svins4_pos_num = 0
                        svins4_pos = [svin4_pos]
                        rotated_svin4 = pygame.transform.rotate(svin3, 0)
                        rotated_svin4_bool = False
                        angle_svin4 = 0  # градусы поворота свиньи

                        player_one_ready = True
                        continue

        if player_one_ready:
            # одинарные свиньи
            if svins1_pos_num < 4:
                if event.type == pygame.MOUSEBUTTONDOWN:  # кнопка мыши нажата
                    if event.button == 1:  # левая кнопка мыши
                        doMove = True
                        up_after_down = False  # для того, чтобы следующее условие выполнилось только после нажатия кнопки мышки
                if event.type == pygame.MOUSEBUTTONUP:  # кнопка мышки не нажата (или отпущена)
                    doMove = False  # следование свинки за мышкой прекращается
                    up_after_down = True

                if event.type == pygame.MOUSEMOTION and doMove:  # следование свинки за мышкой
                    svins1_pos[svins1_pos_num] = event.pos

                if up_after_down:  # после того, кам мы нажали и после отпустили кнопку мыши
                    end_pos = event.pos  # позия мышки, в которой мы отжали кнопку
                    column = (end_pos[0] - 660) // (
                                WIDTH + MARGIN)  # вычисление столбца матрицы по последней координате мышки
                    row = (end_pos[1] - 200) // (
                                HEIGHT + MARGIN)  # вычисление строки матрицы по последней координате мышки
                    # Set that location to one
                    if player_two[row][column] != 1 and player_two[row][column] != 0:  # не выполнится, если на этом месте уже стоит винка или там стоит 0, что означает позицию рядом со свинкой
                        player_two[row][column] = 1
                        check_around(player_two, row,
                                     column)  # окружает свинку ноликами (это видно в терминальной матрице)
                        print("Click ", end_pos, "Grid coordinates: ", row,
                              column)  # просто выводит позицию мышки и строку со столбцом в матрице (можно убрать)
                        # modules.show_matrix(player_one)
                        svins1_pos[svins1_pos_num] = (1100, 0)  # свинка улетает за экран
                        modules.show_matrix(player_two)  # для дебага - выводит консольную матрицу
                        if svins1_pos_num < 4:
                            svins1_pos_num += 1  # увеличиваем счетчик кол-ва одинарных свиней на поле
                        if svins1_pos_num == 4:  # переводит нас на след условие, если все свиньи расставлены
                            continue

            # двойные свиньи
            if (svins1_pos_num == 4) and (svins2_pos_num < 3):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # левая кнопка мыши
                        doMove = True
                        up_after_down = False
                    elif event.button == 3:  # поворот свиньи
                        if angle_svin2 == 360:  # andle - градус поворота
                            angle_svin2 = 90  # сделано для упрощения написания условия с градусами поворота (см далее)
                        else:
                            angle_svin2 += 90
                        rotated_svin2 = pygame.transform.rotate(svin2,
                                                                angle_svin2)  # поворот свиньи на определенный градус
                        rotated_svin2_bool = True  # показывает, что свинья была повернута (нужно для корректного вывода картинки)
                if event.type == pygame.MOUSEBUTTONUP:
                    doMove = False
                    if event.button == 1:
                        up_after_down = True

                if event.type == pygame.MOUSEMOTION and doMove:
                    svins2_pos[svins2_pos_num] = event.pos

                if up_after_down:
                    svin2_mass = []  # массив с перевернутыми и неперевернутыми свиньями
                    end_pos = event.pos
                    # User clicks the mouse. Get the position
                    # Change the x/y screen coordinates to grid coordinates
                    column = (end_pos[0] - 660) // (WIDTH + MARGIN)
                    row = (end_pos[1] - 200) // (HEIGHT + MARGIN)
                    # Set that location to one
                    if player_two[row][column] != 1 and player_two[row][column] != 0:
                        if angle_svin2 % 180 == 0 or angle_svin2 % 360 == 0:  # проверка того, в какую сторону заполнять матрицу (вправо или вниз)
                            if column + 1 <= 9:  # для избежания ошибки index out of range
                                if player_two[row][column + 1] != 1 and player_two[row][column + 1] != 0:  # проверка всех частей тела свинью на близость к другим свинбям
                                    player_two[row][column] = 1
                                    check_around(player_two, row, column)
                                    player_two[row][column + 1] = 1
                                    check_around(player_two, row, column + 1)

                                    svin2_mass.append(rotated_svin2)
                                    end_pos = [(MARGIN + WIDTH) * column + MARGIN + 661,
                                               (MARGIN + HEIGHT) * row + MARGIN + 201,
                                               WIDTH,
                                               HEIGHT]
                                    svin2_mass.append(end_pos)
                                    svins2_rotate.append(svin2_mass)

                                    print("Click ", end_pos, "Grid coordinates: ", row, column)
                                    # modules.show_matrix(player_one)
                                    svins2_pos[svins2_pos_num] = (1100, 0)
                                    modules.show_matrix(player_two)
                                    if svins2_pos_num < 3:
                                        svins2_pos_num += 1
                                    if svins2_pos_num == 3:
                                        continue
                        elif angle_svin2 % 90 == 0 or angle_svin2 % 270 == 0:
                            if row + 1 <= 9:
                                if player_two[row + 1][column] != 1 and player_two[row + 1][column] != 0:
                                    player_two[row][column] = 1
                                    check_around(player_two, row, column)
                                    player_two[row + 1][column] = 1
                                    check_around(player_two, row + 1, column)

                                    svin2_mass.append(rotated_svin2)
                                    end_pos = [(MARGIN + WIDTH) * column + MARGIN + 661,
                                               (MARGIN + HEIGHT) * row + MARGIN + 201, WIDTH,
                                               HEIGHT]
                                    svin2_mass.append(end_pos)
                                    svins2_rotate.append(svin2_mass)

                                    print("Click ", end_pos, "Grid coordinates: ", row, column)
                                    # modules.show_matrix(player_one)
                                    svins2_pos[svins2_pos_num] = (1100, 0)
                                    modules.show_matrix(player_two)
                                    if svins2_pos_num < 3:
                                        svins2_pos_num += 1
                                    if svins2_pos_num == 3:
                                        continue

            # тройные свиньи
            if (svins2_pos_num == 3) and (svins3_pos_num < 2):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # левая кнопка мыши
                        doMove = True
                        up_after_down = False
                    elif event.button == 3:
                        if angle_svin3 == 360:
                            angle_svin3 = 90
                        else:
                            angle_svin3 += 90
                        rotated_svin3 = pygame.transform.rotate(svin3, angle_svin3)
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
                    column = (end_pos[0] - 660) // (WIDTH + MARGIN)
                    row = (end_pos[1] - 200) // (HEIGHT + MARGIN)
                    # Set that location to one
                    if player_two[row][column] != 1 and player_two[row][column] != 0:
                        if angle_svin3 % 180 == 0 or angle_svin3 % 360 == 0:
                            if column + 1 <= 9 and column + 2 <= 9:
                                if player_two[row][column + 1] != 1 and player_two[row][column + 1] != 0 and \
                                        player_two[row][column + 2] != 1 and player_two[row][column + 2] != 0:
                                    player_two[row][column] = 1
                                    check_around(player_two, row, column)
                                    player_two[row][column + 1] = 1
                                    check_around(player_two, row, column + 1)
                                    player_two[row][column + 2] = 1
                                    check_around(player_two, row, column + 2)

                                    svin3_mass.append(rotated_svin3)
                                    end_pos = [(MARGIN + WIDTH) * column + MARGIN + 661,
                                               (MARGIN + HEIGHT) * row + MARGIN + 201,
                                               WIDTH,
                                               HEIGHT]
                                    svin3_mass.append(end_pos)
                                    svins3_rotate.append(svin3_mass)

                                    modules.show_matrix(player_two)
                                    print("Click ", end_pos, "Grid coordinates: ", row, column)
                                    # modules.show_matrix(player_one)
                                    svins3_pos[svins3_pos_num] = (1100, 0)
                                    if svins3_pos_num < 2:
                                        svins3_pos_num += 1
                                    if svins3_pos_num == 2:
                                        continue
                        elif angle_svin3 % 90 == 0 or angle_svin3 % 270 == 0:
                            if row + 1 <= 9 and row + 2 <= 9:
                                if player_two[row + 1][column] != 1 and player_two[row + 1][column] != 0 and \
                                        player_two[row + 2][column] != 1 and player_two[row + 2][column] != 0:
                                    player_two[row][column] = 1
                                    check_around(player_two, row, column)
                                    player_two[row + 1][column] = 1
                                    check_around(player_two, row + 1, column)
                                    player_two[row + 2][column] = 1
                                    check_around(player_two, row + 2, column)
                                    svin3_mass.append(rotated_svin3)
                                    end_pos = [(MARGIN + WIDTH) * column + MARGIN + 661,
                                               (MARGIN + HEIGHT) * row + MARGIN + 201, WIDTH,
                                               HEIGHT]
                                    svin3_mass.append(end_pos)
                                    svins3_rotate.append(svin3_mass)

                                    modules.show_matrix(player_two)
                                    print("Click ", end_pos, "Grid coordinates: ", row, column)
                                    # modules.show_matrix(player_one)
                                    svins3_pos[svins3_pos_num] = (1100, 0)
                                    if svins3_pos_num < 2:
                                        svins3_pos_num += 1
                                    if svins3_pos_num == 2:
                                        continue

            # тройные свиньи
            if (svins3_pos_num == 2) and (svins4_pos_num < 1):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # левая кнопка мыши
                        doMove = True
                        up_after_down = False
                    elif event.button == 3:
                        if angle_svin4 == 360:
                            angle_svin4 = 90
                        else:
                            angle_svin4 += 90
                        rotated_svin4 = pygame.transform.rotate(svin4, angle_svin4)
                        rotated_svin4_bool = True
                if event.type == pygame.MOUSEBUTTONUP:
                    doMove = False
                    if event.button == 1:
                        up_after_down = True

                if event.type == pygame.MOUSEMOTION and doMove:
                    svins4_pos[svins4_pos_num] = event.pos

                if up_after_down:
                    svin4_mass = []
                    end_pos = event.pos
                    # User clicks the mouse. Get the position
                    # Change the x/y screen coordinates to grid coordinates
                    column = (end_pos[0] - 660) // (WIDTH + MARGIN)
                    row = (end_pos[1] - 200) // (HEIGHT + MARGIN)
                    # Set that location to one
                    if player_two[row][column] != 1 and player_two[row][column] != 0:
                        if angle_svin4 % 180 == 0 or angle_svin4 % 360 == 0:
                            if column + 1 <= 9 and column + 2 <= 9 and column + 3 <= 9:
                                if player_two[row][column + 1] != 1 and player_two[row][column + 1] != 0 and \
                                        player_two[row][column + 2] != 1 and player_two[row][column + 2] != 0 and \
                                        player_two[row][column + 3] != 1 and player_two[row][column + 3] != 0:
                                    player_two[row][column] = 1
                                    check_around(player_two, row, column)
                                    player_two[row][column + 1] = 1
                                    check_around(player_two, row, column + 1)
                                    player_two[row][column + 2] = 1
                                    check_around(player_two, row, column + 2)
                                    player_two[row][column + 3] = 1
                                    check_around(player_two, row, column + 3)

                                    svin4_mass.append(rotated_svin4)
                                    end_pos = [(MARGIN + WIDTH) * column + MARGIN + 661,
                                               (MARGIN + HEIGHT) * row + MARGIN + 201,
                                               WIDTH,
                                               HEIGHT]
                                    svin4_mass.append(end_pos)
                                    svins4_rotate.append(svin4_mass)

                                    modules.show_matrix(player_two)
                                    print("Click ", end_pos, "Grid coordinates: ", row, column)
                                    svins4_pos[svins4_pos_num] = (1100, 0)
                                    if svins4_pos_num < 1:
                                        svins4_pos_num += 1
                                    if svins4_pos_num == 1:
                                        player_one_ready = True
                        elif angle_svin4 % 90 == 0 or angle_svin4 % 270 == 0:
                            if row + 1 <= 9 and row + 2 <= 9 and row + 3 <= 9:
                                if player_two[row + 1][column] != 1 and player_two[row + 1][column] != 0 and \
                                        player_two[row + 2][column] != 1 and player_two[row + 2][column] != 0 and \
                                        player_two[row + 3][column] != 1 and player_two[row + 3][column] != 0:
                                    player_two[row][column] = 1
                                    check_around(player_two, row, column)
                                    player_two[row + 1][column] = 1
                                    check_around(player_two, row + 1, column)
                                    player_two[row + 2][column] = 1
                                    check_around(player_two, row + 2, column)
                                    player_two[row + 3][column] = 1
                                    check_around(player_two, row + 3, column)

                                    svin4_mass.append(rotated_svin4)
                                    end_pos = [(MARGIN + WIDTH) * column + MARGIN + 661,
                                               (MARGIN + HEIGHT) * row + MARGIN + 201, WIDTH,
                                               HEIGHT]
                                    svin4_mass.append(end_pos)
                                    svins4_rotate.append(svin4_mass)

                                    modules.show_matrix(player_two)
                                    print("Click ", end_pos, "Grid coordinates: ", row, column)
                                    svins4_pos[svins4_pos_num] = (1100, 0)
                                    if svins4_pos_num < 1:
                                        svins4_pos_num += 1
                                    if svins4_pos_num == 1:
                                        player_two_ready = True


    color_line = [80, 80, 80]  # цвет линий между клетками

    screen.fill([255, 255, 255])  # цвет заднего фона
    # создание сеточки из серых линий
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

    # прорисовка квадратиков матрицы
    for row in range(10):
        for column in range(10):
            color = (5, 40, 120)
            pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN + 660, (MARGIN + HEIGHT) * row + MARGIN + 200, WIDTH, HEIGHT])

    if player_one_ready == False:
        # вывод свиней на самом поле
        # вывод одинарной свинки
        for row in range(10):
            for column in range(10):
                color = (5, 40, 120)
                if player_one[row][column] == 1:  # если есть единичка на поле, выводится свинка
                    end_pos = [(MARGIN + WIDTH) * column + MARGIN + 141, (MARGIN + HEIGHT) * row + MARGIN + 201, WIDTH, HEIGHT]
                    pygame.draw.rect(screen, color,
                                     [(MARGIN + WIDTH) * column + MARGIN + 140, (MARGIN + HEIGHT) * row + MARGIN + 200,
                                      WIDTH, HEIGHT])
                    screen.blit(svin1, end_pos)
                else:  # иначе выводит пустой квадратик
                    pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN + 140, (MARGIN + HEIGHT) * row + MARGIN + 200, WIDTH, HEIGHT])

        # вывод двойных свиней
        for i in range(svins2_pos_num):
            screen.blit(svins2_rotate[i][0], svins2_rotate[i][1])

        # вывод тройных свиней
        for i in range(svins3_pos_num):
            screen.blit(svins3_rotate[i][0], svins3_rotate[i][1])

        # вывод квадро свиней
        for i in range(svins4_pos_num):
            screen.blit(svins4_rotate[i][0], svins4_rotate[i][1])

        # вывод свиней под полем снизу
        # Свиньи одинарные
        for i in range(4):
            screen.blit(svin1, svins1_pos[i])

        # Свиньи двойные
        if rotated_svin2_bool == False:
            for i in range(3):
                screen.blit(svin2, svins2_pos[i])
        else:
            if svins2_pos_num < 3:
                screen.blit(rotated_svin2, svins2_pos[svins2_pos_num])

        # Свиньи тройные
        if rotated_svin3_bool == False:
            for i in range(2):
                screen.blit(svin3, svins3_pos[i])
        else:
            if svins3_pos_num < 2:
                screen.blit(rotated_svin3, svins3_pos[svins3_pos_num])

        # Квадро свиньи
        if rotated_svin4_bool == False:
            for i in range(1):
                screen.blit(svin4, svins4_pos[i])
        else:
            if svins4_pos_num < 1:
                screen.blit(rotated_svin4, svins4_pos[svins4_pos_num])

    # Поле закрывается после ввода кораблей
    if player_one_ready:
        for y_offset in range(0, 200, 20):
            pygame.draw.line(screen, [80, 80, 80], [140, 200 + y_offset], [340, 200 + y_offset], 2)
            pygame.draw.line(screen, [80, 80, 80], [140 + y_offset, 200], [140 + y_offset, 400], 2)
        pygame.draw.line(screen, [80, 80, 80], [140, 400], [340, 400], 2)
        pygame.draw.line(screen, [80, 80, 80], [340, 200], [340, 400], 2)
        for row in range(10):
            for column in range(10):
                color = (5, 40, 120)
                pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN + 140, (MARGIN + HEIGHT) * row + MARGIN + 200, WIDTH, HEIGHT])

        # второй игрок
        # вывод свиней на самом поле
        # вывод одинарной свинки
        for row in range(10):
            for column in range(10):
                color = (5, 40, 120)
                if player_two[row][column] == 1:  # если есть единичка на поле, выводится свинка
                    end_pos = [(MARGIN + WIDTH) * column + MARGIN + 661, (MARGIN + HEIGHT) * row + MARGIN + 201, WIDTH, HEIGHT]
                    screen.blit(svin1, end_pos)
                else:  # иначе выводит пустой квадратик
                    pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN + 660, (MARGIN + HEIGHT) * row + MARGIN + 200, WIDTH, HEIGHT])

        # вывод двойных свиней
        for i in range(svins2_pos_num):
            screen.blit(svins2_rotate[i][0], svins2_rotate[i][1])

        # вывод тройных свиней
        for i in range(svins3_pos_num):
            screen.blit(svins3_rotate[i][0], svins3_rotate[i][1])

        # вывод квадро свиней
        for i in range(svins4_pos_num):
            screen.blit(svins4_rotate[i][0], svins4_rotate[i][1])

        # вывод свиней под полем снизу
        # Свиньи одинарные
        for i in range(4):
            screen.blit(svin1, svins1_pos[i])

        # Свиньи двойные
        if rotated_svin2_bool == False:
            for i in range(3):
                screen.blit(svin2, svins2_pos[i])
        else:
            if svins2_pos_num < 3:
                screen.blit(rotated_svin2, svins2_pos[svins2_pos_num])

        # Свиньи тройные
        if rotated_svin3_bool == False:
            for i in range(2):
                screen.blit(svin3, svins3_pos[i])
        else:
            if svins3_pos_num < 2:
                screen.blit(rotated_svin3, svins3_pos[svins3_pos_num])

        # Квадро свиньи
        if rotated_svin4_bool == False:
            for i in range(1):
                screen.blit(svin4, svins4_pos[i])
        else:
            if svins4_pos_num < 1:
                screen.blit(rotated_svin4, svins4_pos[svins4_pos_num])

        # Поле закрывается после ввода кораблей
        if player_two_ready == True:
            for y_offset in range(0, 200, 20):
                pygame.draw.line(screen, [80, 80, 80], [660, 200 + y_offset], [860, 200 + y_offset], 2)
                pygame.draw.line(screen, [80, 80, 80], [660 + y_offset, 200], [660 + y_offset, 400], 2)
            pygame.draw.line(screen, [80, 80, 80], [660, 400], [860, 400], 2)
            pygame.draw.line(screen, [80, 80, 80], [860, 200], [860, 400], 2)
            for row in range(10):
                for column in range(10):
                    color = (5, 40, 120)
                    pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN + 660, (MARGIN + HEIGHT) * row + MARGIN + 200, WIDTH, HEIGHT])


    pygame.display.update()

    clock.tick(60)

pygame.quit()


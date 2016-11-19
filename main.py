import pygame
import settings

import node

from random import randint

# Set up a window
window = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
pygame.display.set_caption(settings.TITLE)



# parent node starts off with all of the rows and columns in a map
# generations[0]
generations = []
parent_node = node.Node(settings.COLUMNS, settings.ROWS, (0, 0), 0)
generations.append([parent_node])

# 1st generation of kids
generations.append(parent_node.split_node())

# 2nd generation of kids
generations.append([])
for node in generations[1]:
    generations[2].extend(node.split_node())

# 3rd generation of kids
generations.append([])
for node in generations[2]:
    generations[3].extend(node.split_node())

# 4th generation of kids
generations.append([])
for node in generations[3]:
    generations[4].extend(node.split_node())

# make rooms
rooms = []
for node in generations[4]:
    room = node.make_room()
    rooms.append(room)

# make hallways / connect rooms
'''
This still needs a lot of work and clarification
'''
hallways = []
for i in range(0, len(rooms), 2):
    test_position = pygame.math.Vector2(rooms[i].position.x + int(rooms[i].columns / 3) * settings.TILESIZE, rooms[i].position.y + rooms[i].height)
    test_height = rooms[i + 1].position.y - (rooms[i].position.y + rooms[i].height)
    test_width = settings.TILESIZE
    test_rect = pygame.Rect(test_position, (test_width, test_height))
    hallways.append(test_rect)

hallways_two = []
for i in range(0, len(rooms), 4):
    if randint(0, 100) < 50:
        i += 1
    test_position = pygame.math.Vector2(rooms[i].position.x + rooms[i].width, rooms[i].position.y + int(rooms[i].rows / 3) * settings.TILESIZE)
    test_height = settings.TILESIZE
    test_width = rooms[i + 2].position.x - (rooms[i].position.x + rooms[i].width)
    test_rect = pygame.Rect(test_position, (test_width, test_height))
    hallways_two.append(test_rect)

hallways_three = []
for i in range(0, len(rooms), 8):
    if randint(0, 100) < 50:
        i += 2
    test_position = pygame.math.Vector2(rooms[i].position.x + int(rooms[i].columns / 3) * settings.TILESIZE, rooms[i].position.y + rooms[i].height)
    test_height = rooms[i + 4].position.y - (rooms[i].position.y + rooms[i].height)
    test_width = settings.TILESIZE
    test_rect = pygame.Rect(test_position, (test_width, test_height))
    hallways_three.append(test_rect)

hallways_four = []
for i in range(len(rooms)):
    if (i == 2 or i == 3 or i == 6 or i == 7) and randint(0, 100) < 50:
        test_position = pygame.math.Vector2(rooms[i].position.x + rooms[i].width, rooms[i].position.y + int(rooms[i].rows / 3) * settings.TILESIZE)
        test_height = settings.TILESIZE
        test_width = rooms[i + 6].position.x - (rooms[i].position.x + rooms[i].width)
        test_rect = pygame.Rect(test_position, (test_width, test_height))
        hallways_four.append(test_rect)




# MAIN LOOP
running = True
while running:

    # EVENT LOOP
    for event in pygame.event.get():

        # Close program on quit
        if event.type == pygame.QUIT:
            running = False

    # DRAW STUFF
    for i in range(len(rooms)):
        pygame.draw.rect(window, settings.WHITE, rooms[i].rect)

    for i in range(len(hallways)):
        pygame.draw.rect(window, settings.WHITE, hallways[i])

    for i in range(len(hallways_two)):
        pygame.draw.rect(window, settings.WHITE, hallways_two[i])

    for i in range(len(hallways_three)):
        pygame.draw.rect(window, settings.WHITE, hallways_three[i])

    for i in range(len(hallways_four)):
        pygame.draw.rect(window, settings.WHITE, hallways_four[i])





    # DISPLAY FRAME
    pygame.display.update()


import pygame
import settings

import node

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

generations.append([])
for node in generations[3]:
    generations[4].extend(node.split_node())

# make rooms
rooms = []
for node in generations[4]:
    room = node.make_room()
    rooms.append(room)

# MAIN LOOP
running = True
while running:

    # EVENT LOOP
    for event in pygame.event.get():

        # Close program on quit
        if event.type == pygame.QUIT:
            running = False

    # DRAW STUFF
    node0 = generations[3][0]
    pygame.draw.rect(window, settings.WHITE, node0.rect)

    node1 = generations[3][1]
    pygame.draw.rect(window, settings.RED, node1.rect)

    node2 = generations[3][2]
    pygame.draw.rect(window, settings.BLUE, node2.rect)

    node3 = generations[3][3]
    pygame.draw.rect(window, settings.YELLOW, node3.rect)

    node4 = generations[3][4]
    pygame.draw.rect(window, settings.WHITE, node4.rect)

    node5 = generations[3][5]
    pygame.draw.rect(window, settings.RED, node5.rect)

    node6 = generations[3][6]
    pygame.draw.rect(window, settings.BLUE, node6.rect)

    node7 = generations[3][7]
    pygame.draw.rect(window, settings.YELLOW, node7.rect)

    for i in range(len(rooms)):
        pygame.draw.rect(window, settings.BLACK, rooms[i].rect)




    # DISPLAY FRAME
    pygame.display.update()


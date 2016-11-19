import pygame
import settings
# import cell
from random import randint

class Node:
    def __init__(self, columns, rows, position, split_depth):
        self.rows = rows
        self.height = rows * settings.TILESIZE
        self.columns = columns
        self.width = columns * settings.TILESIZE
        self.position = pygame.math.Vector2(position)
        self.parent = None
        self.sibling = None
        self.children = []
        self.split_depth = split_depth

        self.rect = pygame.Rect(self.position, (self.width, self.height))

    def split_node(self):

        if self.split_depth % 2 == 0:
            column_cut = int(self.columns / 2) + randint(-5, 5)

            child_one = Node(column_cut, self.rows, self.position, self.split_depth + 1)
            child_two = Node(self.columns - column_cut, self.rows, self.position + (column_cut * settings.TILESIZE, 0), self.split_depth + 1)
        else:
            row_cut = int(self.rows / 2) + randint(-5, 5)

            child_one = Node(self.columns, row_cut, self.position, self.split_depth + 1)
            child_two = Node(self.columns, self.rows - row_cut, self.position + (0, row_cut * settings.TILESIZE), self.split_depth + 1)

        self.children = [child_one, child_two]

        return self.children

    def make_room(self):
        random_columns = randint(int(self.columns / 2 - 5), self.columns - 5)
        random_rows = randint(int(self.rows / 2 - 5), self.rows - 5)
        random_position = randint(1, 3) * settings.TILESIZE
        room = Room(random_columns, random_rows, self.position + (random_position, random_position), self)
        return room

    def connect_children(self):
        pass


class Room:
    def __init__(self, columns, rows, position, node):
        self.columns = columns
        self.rows = rows
        self.position = position
        self.height = rows * settings.TILESIZE
        self.width = columns * settings.TILESIZE
        self.rect = pygame.Rect(self.position, (self.width, self.height))
        self.node = node

    def draw(self):
        pass


class Hallway:
    def __init__(self, room_one, room_two):
        self.length = room_one.height
        self.width = 2 * settings.TILESIZE
        self.position = pygame.math.Vector2(room_one.columns / 2, room_one.position.y + room_one.height)
        self.rect = pygame.Rect(self.position, (self.width, self.height))


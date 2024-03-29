from csv import reader
from os import walk

import pygame


def import_csv_layout(path):
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter=',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map


def import_folder(path):
    surface_list = []

    for _, __, image_file in walk(path):
        for image in image_file:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
    return surface_list


if __name__ == '__main__':
    #import_csv_layout('5 - level graphics/map/map_FloorBlocks.csv')
    import_folder('graphics/grass')


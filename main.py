import pygame
from random import randint
import sys

TILE_SIZE = 0.8
ENTITY_SIZE = 1.75


def load_image(file, key=None, color_key=None, csize=0):
    if 'as' in file or 'bg' in file or 'screen' in file or 'aa' in file:
        path = 'data/level_assets/' + file
        try:
            image = pygame.image.load(path)
            rect = pygame.Rect(0, 0, image.get_size()[0], image.get_size()[1])
            size = image.get_size()
            if 'bg' not in file and 'screen' not in file:
                if csize > 0:
                    image = pygame.transform.scale(image, (size[0] * csize, size[1] * csize))
                else:
                    image = pygame.transform.scale(image, (size[0] * TILE_SIZE, size[1] * TILE_SIZE))
            if 'as10' in file and csize == 0:
                image = pygame.transform.scale(image, (size[0] * 0.75, size[1] * 0.75))
            if 'menu' in file or 'end' in file:
                image = pygame.transform.scale(image, (size[0] * 8, size[1] * 8))
            if 'finish' in file:
                image = pygame.transform.scale(image, (size[0] * 7, size[1] * 7))
            if 'aa' in file:
                image = pygame.transform.scale(image, (size[0] * 3, size[1] * 3))
        except pygame.error as message:
            print(f'Не удаётся загрузить: {file}.png')
            raise SystemExit(message)
    elif isinstance(key, float):
        path = 'data/characters/' + file + '/' + f'{file}.png'
        try:
            image = pygame.image.load(path)
            if key == 1.1:
                rect = pygame.Rect(41, 139, 15, 18)
            elif key == 1.2:
                rect = pygame.Rect(141, 138, 15, 18)
            elif key == 1.3:
                rect = pygame.Rect(241, 139, 15, 18)
            elif key == 1.4:
                rect = pygame.Rect(341, 140, 15, 17)
            elif key == 1.5:
                rect = pygame.Rect(441, 139, 15, 18)
            elif key == 1.6:
                rect = pygame.Rect(541, 138, 15, 18)
            elif key == 1.7:
                rect = pygame.Rect(641, 139, 15, 18)
            elif key == 1.8:
                rect = pygame.Rect(741, 140, 15, 17)
            elif key == 1.9:
                rect = pygame.Rect(41, 239, 15, 18)
            elif key == 1.10:
                rect = pygame.Rect(141, 233, 19, 24)
            elif key == 1.11:
                rect = pygame.Rect(241, 234, 20, 23)
            elif key == 1.12:
                rect = pygame.Rect(336, 240, 34, 20)
            elif key == 1.13:
                rect = pygame.Rect(436, 240, 34, 20)
            elif key == 1.14:
                rect = pygame.Rect(536, 240, 22, 18)
            elif key == 1.15:
                rect = pygame.Rect(41, 39, 15, 18)
            elif key == 1.16:
                rect = pygame.Rect(41, 639, 15, 18)
            elif key == 1.17:
                rect = pygame.Rect(141, 641, 16, 16)
            elif key == 1.18:
                rect = pygame.Rect(246, 643, 15, 14)
            elif key == 1.19:
                rect = pygame.Rect(348, 647, 19, 10)
            elif key == 1.20:
                rect = pygame.Rect(40, 539, 16, 18)
            elif key == 1.21:
                rect = pygame.Rect(140, 539, 16, 18)
            elif key == 1.22:
                rect = pygame.Rect(240, 539, 16, 18)
            elif key == 1.23:
                rect = pygame.Rect(340, 539, 16, 18)
            elif key == 2.1:
                rect = pygame.Rect(44, 142, 22, 15)
            elif key == 2.2:
                rect = pygame.Rect(144, 141, 22, 15)
            elif key == 2.3:
                rect = pygame.Rect(244, 142, 22, 15)
            elif key == 2.4:
                rect = pygame.Rect(344, 143, 22, 15)
            elif key == 2.5:
                rect = pygame.Rect(444, 142, 22, 15)
            elif key == 2.6:
                rect = pygame.Rect(544, 142, 21, 15)
            elif key == 2.7:
                rect = pygame.Rect(644, 142, 21, 15)
            elif key == 2.8:
                rect = pygame.Rect(744, 143, 21, 14)
            elif key == 2.9:
                rect = pygame.Rect(44, 242, 22, 15)
            elif key == 2.10:
                rect = pygame.Rect(144, 238, 19, 19)
            elif key == 2.11:
                rect = pygame.Rect(236, 233, 19, 24)
            elif key == 2.12:
                rect = pygame.Rect(345, 236, 28, 26)
            elif key == 2.13:
                rect = pygame.Rect(445, 242, 28, 20)
            elif key == 2.14:
                rect = pygame.Rect(545, 243, 26, 19)
            elif key == 2.15:
                rect = pygame.Rect(42, 442, 23, 15)
            elif key == 2.16:
                rect = pygame.Rect(142, 442, 23, 15)
            elif key == 2.17:
                rect = pygame.Rect(242, 442, 23, 15)
            elif key == 2.18:
                rect = pygame.Rect(342, 442, 23, 15)
            elif key == 2.19:
                rect = pygame.Rect(44, 542, 22, 15)
            elif key == 2.20:
                rect = pygame.Rect(140, 541, 26, 14)
            elif key == 2.21:
                rect = pygame.Rect(237, 539, 28, 17)
            elif key == 2.22:
                rect = pygame.Rect(336, 546, 29, 10)
            elif key == 3.1:
                rect = pygame.Rect(43, 42, 26, 15)
            elif key == 3.2:
                rect = pygame.Rect(43, 142, 26, 15)
            elif key == 3.3:
                rect = pygame.Rect(144, 141, 25, 15)
            elif key == 3.4:
                rect = pygame.Rect(244, 142, 25, 15)
            elif key == 3.5:
                rect = pygame.Rect(343, 143, 26, 15)
            elif key == 3.6:
                rect = pygame.Rect(443, 142, 26, 15)
            elif key == 3.7:
                rect = pygame.Rect(543, 141, 26, 15)
            elif key == 3.8:
                rect = pygame.Rect(643, 142, 26, 15)
            elif key == 3.9:
                rect = pygame.Rect(743, 143, 26, 14)
            elif key == 3.10:
                rect = pygame.Rect(43, 242, 26, 15)
            elif key == 3.11:
                rect = pygame.Rect(143, 236, 18, 21)
            elif key == 3.12:
                rect = pygame.Rect(237, 241, 21, 16)
            elif key == 3.13:
                rect = pygame.Rect(342, 233, 30, 25)
            elif key == 3.14:
                rect = pygame.Rect(442, 235, 30, 23)
            elif key == 3.15:
                rect = pygame.Rect(542, 243, 28, 15)
            elif key == 3.16:
                rect = pygame.Rect(40, 542, 28, 15)
            elif key == 3.17:
                rect = pygame.Rect(140, 542, 28, 15)
            elif key == 3.18:
                rect = pygame.Rect(240, 542, 28, 15)
            elif key == 3.19:
                rect = pygame.Rect(340, 542, 28, 15)
            elif key == 3.20:
                rect = pygame.Rect(43, 642, 26, 15)
            elif key == 3.21:
                rect = pygame.Rect(141, 644, 33, 13)
            elif key == 3.22:
                rect = pygame.Rect(241, 648, 34, 9)
            elif key == 3.23:
                rect = pygame.Rect(341, 648, 24, 9)
            elif key == 4.1:
                rect = pygame.Rect(46, 35, 18, 23)
            elif key == 4.2:
                rect = pygame.Rect(46, 135, 18, 23)
            elif key == 4.3:
                rect = pygame.Rect(147, 134, 17, 23)
            elif key == 4.4:
                rect = pygame.Rect(247, 135, 17, 23)
            elif key == 4.5:
                rect = pygame.Rect(346, 136, 18, 23)
            elif key == 4.6:
                rect = pygame.Rect(446, 135, 18, 23)
            elif key == 4.7:
                rect = pygame.Rect(546, 133, 18, 23)
            elif key == 4.8:
                rect = pygame.Rect(646, 134, 18, 23)
            elif key == 4.9:
                rect = pygame.Rect(746, 136, 18, 23)
            elif key == 4.10:
                rect = pygame.Rect(46, 335, 18, 23)
            elif key == 4.11:
                rect = pygame.Rect(140, 333, 31, 29)
            elif key == 4.12:
                rect = pygame.Rect(236, 334, 36, 30)
            elif key == 4.13:
                rect = pygame.Rect(339, 333, 31, 32)
            elif key == 4.14:
                rect = pygame.Rect(439, 332, 35, 35)
            elif key == 4.15:
                rect = pygame.Rect(540, 333, 31, 29)
            elif key == 4.16:
                rect = pygame.Rect(636, 334, 36, 30)
            elif key == 4.17:
                rect = pygame.Rect(739, 333, 31, 32)
            elif key == 4.18:
                rect = pygame.Rect(839, 332, 35, 35)
            elif key == 4.19:
                rect = pygame.Rect(44, 434, 18, 23)
            elif key == 4.20:
                rect = pygame.Rect(144, 434, 18, 23)
            elif key == 4.21:
                rect = pygame.Rect(244, 434, 18, 23)
            elif key == 4.22:
                rect = pygame.Rect(344, 434, 18, 23)
            elif key == 4.23:
                rect = pygame.Rect(46, 535, 18, 23)
            elif key == 4.24:
                rect = pygame.Rect(144, 533, 28, 24)
            elif key == 4.25:
                rect = pygame.Rect(244, 543, 29, 14)
            elif key == 4.26:
                rect = pygame.Rect(344, 545, 29, 12)
            elif key == 5.1:
                rect = pygame.Rect(42, 38, 25, 19)
            elif key == 5.2:
                rect = pygame.Rect(42, 138, 25, 19)
            elif key == 5.3:
                rect = pygame.Rect(143, 137, 24, 19)
            elif key == 5.4:
                rect = pygame.Rect(243, 138, 24, 19)
            elif key == 5.5:
                rect = pygame.Rect(342, 139, 25, 19)
            elif key == 5.6:
                rect = pygame.Rect(442, 138, 25, 19)
            elif key == 5.7:
                rect = pygame.Rect(542, 137, 25, 19)
            elif key == 5.8:
                rect = pygame.Rect(642, 138, 25, 19)
            elif key == 5.9:
                rect = pygame.Rect(742, 139, 25, 19)
            elif key == 5.10:
                rect = pygame.Rect(42, 238, 25, 19)
            elif key == 5.11:
                rect = pygame.Rect(142, 237, 25, 20)
            elif key == 5.12:
                rect = pygame.Rect(242, 233, 21, 24)
            elif key == 5.13:
                rect = pygame.Rect(342, 231, 15, 26)
            elif key == 5.14:
                rect = pygame.Rect(441, 236, 32, 26)
            elif key == 5.15:
                rect = pygame.Rect(541, 238, 32, 24)
            elif key == 5.16:
                rect = pygame.Rect(641, 238, 26, 24)
            elif key == 5.17:
                rect = pygame.Rect(40, 638, 26, 19)
            elif key == 5.18:
                rect = pygame.Rect(140, 638, 26, 19)
            elif key == 5.19:
                rect = pygame.Rect(240, 638, 26, 19)
            elif key == 5.20:
                rect = pygame.Rect(340, 638, 26, 19)
            elif key == 5.21:
                rect = pygame.Rect(42, 738, 25, 19)
            elif key == 5.22:
                rect = pygame.Rect(140, 736, 28, 20)
            elif key == 5.23:
                rect = pygame.Rect(229, 738, 40, 17)
            elif key == 5.24:
                rect = pygame.Rect(327, 746, 41, 11)
            image = image.subsurface(rect)
            size = image.get_size()
            if csize > 0:
                image = pygame.transform.scale(image, (size[0] * csize, size[1] * csize))
            else:
                image = pygame.transform.scale(image, (size[0] * ENTITY_SIZE, size[1] * ENTITY_SIZE))
        except pygame.error as message:
            print(f'Не удаётся загрузить: {file}.png')
            raise SystemExit(message)
    else:
        path = f'data/{file}.png'
        try:
            image = pygame.image.load(path)
            if key == '1.1':
                rect = pygame.Rect(27, 6, 172, 68)
            elif key == '1.2':
                rect = pygame.Rect(27, 88, 172, 68)
            elif key == '1.3':
                rect = pygame.Rect(27, 173, 172, 68)
            elif key == '1.4':
                rect = pygame.Rect(27, 256, 172, 68)
            elif key == '1.5':
                rect = pygame.Rect(27, 340, 172, 68)
            elif key == '1.6':
                rect = pygame.Rect(27, 424, 172, 68)
            image = image.subsurface(rect)
            size = image.get_size()
            image = pygame.transform.scale(image, (size[0] * 0.75, size[1] * 0.75))
        except pygame.error as message:
            print(f'Не удаётся загрузить: {file}.png')
            raise SystemExit(message)
    image = image.convert_alpha()
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    return image


def load_level(file):
    filename = "data/levels/" + file
    with open(filename, 'r') as mapFile:
        levelmap = [line.strip() for line in mapFile]
    return levelmap


pygame.init()
screen_size = (1400, 800)
screen = pygame.display.set_mode(screen_size)
FPS = 50

tile_images = {
    'grass': load_image('as1.png'),
    'path': load_image('as2.png'),
    'tree1': load_image('as3.png'),
    'tree2': load_image('as4.png'),
    'path_t': load_image('as5.png'),
    'path_e': load_image('as6.png'),
    'path_t2': load_image('as7.png'),
    'path_t3': load_image('as8.png'),
    'path_t4': load_image('as9.png'),
    'tower': load_image('as10.png'),
    'sign': load_image('as11.png')
}

tile_codes = {
    'grass': 'as1.png',
    'path': 'as2.png',
    'tree1': 'as3.png',
    'tree2': 'as4.png',
    'path_t': 'as5.png',
    'path_e': 'as6.png',
    'path_t2': 'as7.png',
    'path_t3': 'as8.png',
    'path_t4': 'as9.png',
    'tower': 'as10.png',
    'sign': 'as11.png'
}


class ScreenFrame(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = (0, 0, 800, 500)


class SpriteGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

    def get_event(self, event):
        for sprite in self:
            sprite.get_event(event)


class Sprite(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.rect = None

    def get_event(self, event):
        pass


class Tile(Sprite):
    def __init__(self, tile_type, pos_x, pos_y, f, csize=0):
        super().__init__(tiles_group)
        if csize > 0:
            self.image = load_image(tile_codes[tile_type], csize=csize)
            if tile_type == 'tree1':
                self.rect = self.image.get_rect().move(
                    50 * csize * (pos_x - f - 0.5), 50 * csize * pos_y)
                self.rect.height -= 16.6 * csize
            elif tile_type == 'tree2':
                self.rect = self.image.get_rect().move(
                    50 * csize * (pos_x - f - 0.5), 50 * csize * (pos_y - 0.2))
                self.rect.height -= 16.6 * csize
            elif tile_type == 'path':
                self.rect = self.image.get_rect().move(
                    50 * csize * pos_x, 50 * csize * pos_y)
            elif tile_type == 'tower':
                self.rect = self.image.get_rect().move(
                    50 * csize * pos_x, 50 * csize * pos_y)
                self.rect.height -= 30 * csize
            elif tile_type == 'sign':
                self.rect = self.image.get_rect().move(
                    50 * csize * pos_x, 50 * csize * (pos_y + 0.15))
                self.rect.height -= 16.6 * csize
            elif tile_type == 'grass':
                self.rect = self.image.get_rect().move(
                    50 * csize * pos_x, 50 * csize * pos_y)
        else:
            self.image = tile_images[tile_type]
            if tile_type == 'tree1':
                self.rect = self.image.get_rect().move(
                    50 * TILE_SIZE * (pos_x - f - 0.5), 50 * TILE_SIZE * pos_y)
                self.rect.height -= 16.6 * TILE_SIZE
            elif tile_type == 'tree2':
                self.rect = self.image.get_rect().move(
                    50 * TILE_SIZE * (pos_x - f - 0.5), 50 * TILE_SIZE * pos_y)
                self.rect.height -= 16.6 * TILE_SIZE
            elif tile_type == 'path':
                self.rect = self.image.get_rect().move(
                    50 * TILE_SIZE * pos_x, 50 * TILE_SIZE * pos_y)
            elif tile_type == 'tower':
                self.rect = self.image.get_rect().move(
                    50 * TILE_SIZE * (pos_x - 0.8), 50 * TILE_SIZE * (pos_y - 2.6))
                self.rect.height -= 30 * TILE_SIZE
            elif tile_type == 'sign':
                self.rect = self.image.get_rect().move(
                    50 * TILE_SIZE * pos_x, 50 * TILE_SIZE * (pos_y + 0.15))
                self.rect.height -= 16.6 * TILE_SIZE
            elif tile_type == 'grass':
                self.rect = self.image.get_rect().move(
                    50 * TILE_SIZE * pos_x, 50 * TILE_SIZE * pos_y)
        self.abs_pos = (self.rect.x, self.rect.y)


class Floor(Sprite):
    def __init__(self, tile_type, pos_x, pos_y, f=0, isMirrored=False, isDown=False, csize=0):
        super().__init__(floor_group)
        if csize > 0:
            self.image = load_image(tile_codes[tile_type], csize=csize)
            if tile_type == 'grass':
                self.rect = self.image.get_rect().move(
                    50 * csize * pos_x, 50 * csize * pos_y)
            else:
                self.rect = self.image.get_rect().move(
                    50 * csize * pos_x, 50 * csize * pos_y)
                if isMirrored:
                    self.image = pygame.transform.flip(self.image, True, False)
                if isDown:
                    self.image = pygame.transform.rotate(self.image, 90)
        else:
            self.image = tile_images[tile_type]
            if tile_type == 'grass':
                self.rect = self.image.get_rect().move(
                    50 * TILE_SIZE * pos_x, 50 * TILE_SIZE * pos_y)
            else:
                self.rect = self.image.get_rect().move(
                    50 * TILE_SIZE * pos_x, 50 * TILE_SIZE * pos_y)
                if isMirrored:
                    self.image = pygame.transform.flip(self.image, True, False)
                if isDown:
                    self.image = pygame.transform.rotate(self.image, 90)
        self.abs_pos = (self.rect.x, self.rect.y)


class Health(Sprite):
    def __init__(self, frame=0):
        super().__init__(health_group)
        self.framesHealth = [
            load_image('healthbar', '1.1'),
            load_image('healthbar', '1.2'),
            load_image('healthbar', '1.3'),
            load_image('healthbar', '1.4'),
            load_image('healthbar', '1.5'),
            load_image('healthbar', '1.6')
        ]
        self.cur_frameHealth = frame
        self.image = self.framesHealth[self.cur_frameHealth]
        self.rect = pygame.Rect(5, 7, self.framesHealth[0].get_width(), self.framesHealth[0].get_height())
        self.rect = self.rect.move(5, 7)
        self.abs_pos = (self.rect.x, self.rect.y)

    def damage(self):
        if (self.cur_frameHealth + 1) % len(self.framesHealth) == 0:
            return
        self.cur_frameHealth = (self.cur_frameHealth + 1) % len(self.framesHealth)
        self.image = self.framesHealth[self.cur_frameHealth]

    def heal(self):
        if (self.cur_frameHealth - 1) % len(self.framesHealth) == 5:
            return
        self.cur_frameHealth = (self.cur_frameHealth - 1) % len(self.framesHealth)
        self.image = self.framesHealth[self.cur_frameHealth]
        player.heal()


class EnemyOrc(Sprite):
    def __init__(self, x, y, afk=False, route=False, *args):
        super().__init__(enemy_group)
        self.framesStand = [
            load_image('Orc', 2.1)
        ]
        self.framesMove = [
            load_image('Orc', 2.1),
            load_image('Orc', 2.2),
            load_image('Orc', 2.3),
            load_image('Orc', 2.4),
            load_image('Orc', 2.5),
            load_image('Orc', 2.7),
            load_image('Orc', 2.8)
        ]
        self.framesAttack = [
            load_image('Orc', 2.9),
            load_image('Orc', 2.10),
            load_image('Orc', 2.11),
            load_image('Orc', 2.12),
            load_image('Orc', 2.13),
            load_image('Orc', 2.14)
        ]
        self.framesDamage = [
            load_image('Orc', 2.15),
            load_image('Orc', 2.16),
            load_image('Orc', 2.17),
            load_image('Orc', 2.18)
        ]
        self.framesDeath = [
            load_image('Orc', 2.19),
            load_image('Orc', 2.20),
            load_image('Orc', 2.21),
            load_image('Orc', 2.22)
        ]
        self.health = 3
        self.mirrored = False
        self.cur_frameM = 0
        self.cur_frameA1 = 0
        self.cur_frameDh = 0
        self.cur_frameDmg = 0
        self.anim1_act = True
        self.anim2_act = True
        self.dead = False
        self.block = False
        self.can_move = True
        self.moving = False
        self.attack = False
        self.reset = True
        self.v = False
        self.stop = False
        self.stop2 = False
        self.time = 0
        self.pos_x = int(x * 50 * TILE_SIZE)
        self.pos_y = int(y * 50 * TILE_SIZE)
        self.damaged = False
        self.rage = False
        self.x = 0
        self.y = 0
        self.afk = afk
        self.route = route
        self.coords = list(args)
        self.step = 0
        self.dirx = 0
        self.diry = 0
        self.a = int(x * 50 * TILE_SIZE)
        self.b = int(y * 50 * TILE_SIZE)
        self.image = self.framesStand[0]
        self.rect = pygame.Rect(x * 50 * TILE_SIZE, y * 50 * TILE_SIZE, self.framesMove[0].get_width(),
                                self.framesMove[0].get_height())

    def damage(self):
        global deadEnemies
        global deathAnim2
        if not self.dead:
            if self.health > 0:
                self.health -= 1
            if self.health == 0:
                self.dead = True
            self.can_move = False

    def update(self, enemies=None, anim1=False, anim2=False, anim3=False, anim4=False, anim5=False):
        global damagedEnemies
        global damageAnim2
        global damagedEnemiesDone
        global deadEnemies
        global deathAnim2
        global deadEnemiesDone
        if self.block:
            return
        if anim1 and self in enemies and self.anim1_act:
            self.cur_frameDh = (self.cur_frameDh + 1) % (len(self.framesDeath) * 4)
            self.can_move = False
            if self.mirrored:
                if self.cur_frameDh // 4 == 1:
                    self.rect.x = self.x - 3
                if self.cur_frameDh != 0:
                    self.image = pygame.transform.flip(self.framesDeath[self.cur_frameDh // 4], True, False)
            else:
                if self.cur_frameDh // 4 == 1:
                    self.rect.x = self.x + 3
                if self.cur_frameDh != 0:
                    self.image = self.framesDeath[self.cur_frameDh // 4]
            if self.cur_frameDh == 0:
                self.block = True
                self.dead = True
                self.anim1_act = False
                self.rect.width = 0
                self.rect.height = 0
                deadEnemiesDone += 1
                points_count(kill1=True)
            self.rect.x = self.x
            self.rect.y = self.y + 8
            if deadEnemiesDone == len(deadEnemies):
                deadEnemies.clear()
                deathAnim2 = False
                deadEnemiesDone = 0
        if anim2 and self in enemies and self.anim2_act:
            self.can_move = False
            self.cur_frameDmg = (self.cur_frameDmg + 1) % (len(self.framesDamage) * 4)
            self.rect.x = self.x
            self.rect.y = self.y
            if self.mirrored:
                self.image = pygame.transform.flip(self.framesDamage[self.cur_frameDmg // 4], True, False)
            else:
                self.image = self.framesDamage[self.cur_frameDmg // 4]
            if self.cur_frameDmg == 0:
                self.anim2_act = False
                self.can_move = True
                self.stand()
                damagedEnemiesDone += 1
            if damagedEnemiesDone == len(damagedEnemies):
                for enemy in damagedEnemies:
                    enemy.anim2_act = True
                damagedEnemies.clear()
                damageAnim2 = False
                damagedEnemiesDone = 0
        if anim3:
            self.rect_xy()
            self.cur_frameM = (self.cur_frameM + 1) % len(self.framesMove)
            if self.mirrored:
                self.image = pygame.transform.flip(self.framesMove[self.cur_frameM], True, False)
            else:
                self.image = self.framesMove[self.cur_frameM]
        if anim4 and self.can_move:
            self.ai()
        if anim5:
            if player.dead:
                return
            if self.time == 0:
                self.rect_xy()
            self.time += 1
            self.cur_frameA1 = (self.cur_frameA1 + 1) % (len(self.framesAttack) * 4)
            if self.mirrored:
                self.image = pygame.transform.flip(self.framesAttack[self.cur_frameA1 // 4], True, False)
                self.rect.y = self.y
                if self.cur_frameA1 // 4 == 5:
                    self.rect.x = self.x - 8
                elif self.cur_frameA1 // 4 == 4:
                    self.rect.x = self.x - 10
                elif self.cur_frameA1 // 4 > 2:
                    self.rect.x = self.x - 10
                    self.rect.y = self.y - 9
                elif self.cur_frameA1 // 4 == 2:
                    self.rect.x = self.x + 17
                    self.rect.y = self.y - 15
                elif self.cur_frameA1 // 4 == 1:
                    self.rect.y = self.y
            else:
                self.image = self.framesAttack[self.cur_frameA1 // 4]
                self.rect.y = self.y
                if self.cur_frameA1 // 4 > 3:
                    self.rect.x = self.x - 2
                elif self.cur_frameA1 // 4 == 3:
                    self.rect.y = self.y - 10
                    self.rect.x = self.x - 1
                elif self.cur_frameA1 // 4 == 2:
                    self.rect.y = self.y - 15
                    self.rect.x = self.x - 12
                elif self.cur_frameA1 // 4 == 1:
                    self.rect.y = self.y
                    self.rect.x = self.x - 1
            if self.cur_frameA1 // 4 == 4:
                self.rect.w += 25
            if pygame.sprite.spritecollideany(self,
                                              player_group) and self.cur_frameA1 // 4 == 4 and not self.stop and \
                    not player.dead:
                self.stop = True
                player.damage()
                health_bar.damage()
                if player.dead:
                    self.rage = False
                    self.reset = False
                    self.attack = False
            if self.cur_frameA1 // 4 == 4:
                self.rect.w -= 25
            if self.cur_frameA1 == 0:
                self.rect.x = self.x
                self.rect.y = self.y
                self.time = 0
                self.stop = False
                self.attack = False

    def rect_xy(self):
        self.x = self.rect.x
        self.y = self.rect.y

    def stand(self):
        if self.mirrored:
            self.image = pygame.transform.flip(self.framesStand[0], True, False)
        else:
            self.image = self.framesStand[0]

    def move(self, x, y, can_attack=False):
        self.reset = False
        speed = 1
        self.moving = True
        self.dirx = x
        self.diry = y
        self.update(anim3=True)
        if self.diry > self.rect.y:
            if self.rect.y + speed < self.diry:
                self.rect.y += speed
            else:
                self.rect.y = self.diry
        elif self.diry < self.rect.y:
            if self.rect.y - speed > self.diry:
                self.rect.y -= speed
            else:
                self.rect.y = self.diry
        if self.dirx > self.rect.x:
            if self.rage:
                if player.rect.x > self.rect.x:
                    self.mirrored = False
                else:
                    self.mirrored = True
            elif self.dirx - 8 > self.rect.x:
                self.mirrored = False
            if self.rect.x + speed < self.dirx:
                self.rect.x += speed
            else:
                self.rect.x = self.dirx
        elif self.dirx < self.rect.x:
            if self.rage:
                if player.rect.x > self.rect.x:
                    self.mirrored = False
                else:
                    self.mirrored = True
            elif self.dirx + 8 < self.rect.x:
                self.mirrored = True
            if self.rect.x - speed > self.dirx:
                self.rect.x -= speed
            else:
                self.rect.x = self.dirx
        if self.rect.x == self.dirx and self.rect.y == self.diry:
            if can_attack and not player.dead:
                self.attack = True
            self.stand()
            self.moving = False
            if self.route:
                self.step += 1
        if (abs(self.rect.x - player.rect.x) < 90 or abs(self.rect.x + self.rect.w - player.rect.x) < 90) \
                and (abs(self.rect.y - player.rect.y) < 90 or abs(self.rect.y + self.rect.h - player.rect.y) < 90) and \
                not self.v:
            self.rage = True
            self.reset = True
            self.v = True

    def ai(self):
        if self.block:
            return
        if self.rage and not player.dead:
            if self.reset:
                self.a = player.rect.x
                self.b = player.rect.y
        else:
            if self.route:
                if self.step <= len(self.coords) - 1:
                    self.a, self.b = self.coords[self.step][0], self.coords[self.step][1]
                else:
                    self.pos_x = self.rect.x
                    self.pos_y = self.rect.y
                    self.route = False
            else:
                if randint(1, 80) == 1:
                    if not self.afk:
                        self.a, self.b = randint(self.pos_x - 20, self.pos_x + 20), randint(self.pos_y - 20,
                                                                                            self.pos_y + 20)
                    else:
                        if self.mirrored:
                            self.mirrored = False
                        else:
                            self.mirrored = True

        if self.attack and not player.dead:
            self.update(anim5=True)
        else:
            if self.a > self.rect.x:
                if self.rage:
                    self.move(int(self.a) - 33, int(self.b), True)
                else:
                    self.move(int(self.a), int(self.b))
            else:
                if self.rage:
                    self.move(int(self.a) + 23, int(self.b), True)
                else:
                    self.move(int(self.a), int(self.b))


class EnemyArmoredOrc(Sprite):
    def __init__(self, x, y, afk=False, route=False, *args):
        super().__init__(enemy_group)
        self.framesStand = [
            load_image('Armored Orc', 5.1)
        ]
        self.framesMove = [
            load_image('Armored Orc', 5.2),
            load_image('Armored Orc', 5.3),
            load_image('Armored Orc', 5.4),
            load_image('Armored Orc', 5.5),
            load_image('Armored Orc', 5.6),
            load_image('Armored Orc', 5.7),
            load_image('Armored Orc', 5.8),
            load_image('Armored Orc', 5.9)
        ]
        self.framesAttack = [
            load_image('Armored Orc', 5.10),
            load_image('Armored Orc', 5.11),
            load_image('Armored Orc', 5.12),
            load_image('Armored Orc', 5.13),
            load_image('Armored Orc', 5.14),
            load_image('Armored Orc', 5.15),
            load_image('Armored Orc', 5.16)
        ]
        self.framesDamage = [
            load_image('Armored Orc', 5.17),
            load_image('Armored Orc', 5.18),
            load_image('Armored Orc', 5.19),
            load_image('Armored Orc', 5.20)
        ]
        self.framesDeath = [
            load_image('Armored Orc', 5.21),
            load_image('Armored Orc', 5.22),
            load_image('Armored Orc', 5.23),
            load_image('Armored Orc', 5.24)
        ]
        self.health = 5
        self.mirrored = False
        self.cur_frameM = 0
        self.cur_frameA1 = 0
        self.cur_frameDh = 0
        self.cur_frameDmg = 0
        self.anim1_act = True
        self.anim2_act = True
        self.dead = False
        self.block = False
        self.can_move = True
        self.moving = False
        self.attack = False
        self.reset = True
        self.v = False
        self.stop = False
        self.stop2 = False
        self.time = 0
        self.afk = afk
        self.pos_x = int(x * 50 * TILE_SIZE)
        self.pos_y = int(y * 50 * TILE_SIZE)
        self.damaged = False
        self.rage = False
        self.x = 0
        self.y = 0
        self.dirx = 0
        self.diry = 0
        self.route = route
        self.coords = list(args)
        self.step = 0
        self.a = int(x * 50 * TILE_SIZE)
        self.b = int(y * 50 * TILE_SIZE)
        self.image = self.framesStand[0]
        self.rect = pygame.Rect(x * 50 * TILE_SIZE, y * 50 * TILE_SIZE, self.framesMove[0].get_width(),
                                self.framesMove[0].get_height())

    def damage(self):
        global deadEnemies
        global deathAnim2
        if not self.dead:
            if self.health > 0:
                self.health -= 1
            if self.health == 0:
                self.dead = True
            self.can_move = False

    def update(self, enemies=None, anim1=False, anim2=False, anim3=False, anim4=False, anim5=False):
        global damagedEnemies
        global damageAnim2
        global damagedEnemiesDone
        global deadEnemies
        global deathAnim2
        global deadEnemiesDone
        if self.block:
            return
        if anim1 and self in enemies and self.anim1_act:
            if self.cur_frameDh == 0:
                self.rect.x = self.x
            self.cur_frameDh = (self.cur_frameDh + 1) % (len(self.framesDeath) * 4)
            self.can_move = False
            if self.mirrored:
                if self.cur_frameDh // 4 == 1:
                    self.rect.x = self.x - 9
                    self.rect.y = self.y - 3
                elif self.cur_frameDh // 4 == 2:
                    self.rect.y = self.y + 9
                    self.rect.x = self.x - 10
                elif self.cur_frameDh // 4 == 3:
                    self.rect.x = self.x - 10
                    self.rect.y = self.y + 10
                if self.cur_frameDh != 0:
                    self.image = pygame.transform.flip(self.framesDeath[self.cur_frameDh // 4], True, False)
            else:
                if self.cur_frameDh // 4 == 1:
                    self.rect.x = self.x - 5
                    self.rect.y = self.y - 3
                elif self.cur_frameDh // 4 == 2:
                    self.rect.y = self.y + 9
                    self.rect.x = self.x - 5
                elif self.cur_frameDh // 4 == 3:
                    self.rect.x = self.x - 5
                    self.rect.y = self.y + 10
                if self.cur_frameDh != 0:
                    self.image = self.framesDeath[self.cur_frameDh // 4]
            if self.cur_frameDh == 0:
                self.block = True
                self.dead = True
                self.anim1_act = False
                self.rect.width = 0
                self.rect.height = 0
                deadEnemiesDone += 1
                points_count(kill2=True)
            if deadEnemiesDone == len(deadEnemies):
                deadEnemies.clear()
                deathAnim2 = False
                deadEnemiesDone = 0
        if anim2 and self in enemies and self.anim2_act:
            self.can_move = False
            self.cur_frameDmg = (self.cur_frameDmg + 1) % (len(self.framesDamage) * 4)
            self.rect.x = self.x
            self.rect.y = self.y
            if self.mirrored:
                self.image = pygame.transform.flip(self.framesDamage[self.cur_frameDmg // 4], True, False)
            else:
                self.image = self.framesDamage[self.cur_frameDmg // 4]
            if self.cur_frameDmg == 0:
                self.anim2_act = False
                self.can_move = True
                self.stand()
                damagedEnemiesDone += 1
            if damagedEnemiesDone == len(damagedEnemies):
                for enemy in damagedEnemies:
                    enemy.anim2_act = True
                damagedEnemies.clear()
                damageAnim2 = False
                damagedEnemiesDone = 0
        if anim3:
            self.rect_xy()
            self.cur_frameM = (self.cur_frameM + 1) % len(self.framesMove)
            if self.mirrored:
                self.image = pygame.transform.flip(self.framesMove[self.cur_frameM], True, False)
            else:
                self.image = self.framesMove[self.cur_frameM]
        if anim4 and self.can_move:
            self.ai()
        if anim5:
            if player.dead:
                return
            if self.time == 0:
                self.rect_xy()
            self.time += 1
            self.cur_frameA1 = (self.cur_frameA1 + 1) % (len(self.framesAttack) * 4)
            if self.mirrored:
                self.image = pygame.transform.flip(self.framesAttack[self.cur_frameA1 // 4], True, False)
                self.rect.y = self.y
                if self.cur_frameA1 // 4 == 6:
                    self.rect.x = self.x - 3
                    self.rect.y = self.y + 1
                elif self.cur_frameA1 // 4 == 5:
                    self.rect.x = self.x - 14
                    self.rect.y = self.y + 1
                elif self.cur_frameA1 // 4 == 4:
                    self.rect.x = self.x - 14
                    self.rect.y = self.y - 3
                elif self.cur_frameA1 // 4 == 3:
                    self.rect.x = self.x + 13
                    self.rect.y = self.y - 10
                elif self.cur_frameA1 // 4 == 2:
                    self.rect.x = self.x + 5
                    self.rect.y = self.y - 7
                elif self.cur_frameA1 // 4 == 1:
                    self.rect.y = self.y
                    self.rect.x = self.x
            else:
                self.image = self.framesAttack[self.cur_frameA1 // 4]
                self.rect.y = self.y
                if self.cur_frameA1 // 4 == 6:
                    self.rect.x = self.x - 3
                    self.rect.y = self.y + 1
                elif self.cur_frameA1 // 4 == 5:
                    self.rect.x = self.x - 4
                    self.rect.y = self.y + 1
                elif self.cur_frameA1 // 4 == 4:
                    self.rect.x = self.x - 4
                    self.rect.y = self.y - 3
                elif self.cur_frameA1 // 4 == 3:
                    self.rect.x = self.x + 2
                    self.rect.y = self.y - 10
                elif self.cur_frameA1 // 4 == 2:
                    self.rect.x = self.x + 1
                    self.rect.y = self.y - 7
                elif self.cur_frameA1 // 4 == 1:
                    self.rect.y = self.y
                    self.rect.x = self.x
            if self.cur_frameA1 // 4 == 4 or self.cur_frameA1 // 4 == 6:
                self.rect.w += 25
            if pygame.sprite.spritecollideany(self, player_group) and self.cur_frameA1 // 4 == 4 and \
                    not self.stop and not player.dead:
                self.stop = True
                player.damage()
                health_bar.damage()
                player.damage()
                health_bar.damage()
                if player.dead:
                    self.rage = False
                    self.reset = False
                    self.attack = False
            if self.cur_frameA1 // 4 == 4 or self.cur_frameA1 // 4 == 6:
                self.rect.w -= 25
            if self.cur_frameA1 == 0:
                self.rect.x = self.x
                self.rect.y = self.y
            if self.time == 28:
                self.time = 0
                self.stop = False
                self.stop2 = False
                self.attack = False
                self.stand()

    def rect_xy(self):
        self.x = self.rect.x
        self.y = self.rect.y

    def stand(self):
        if self.mirrored:
            self.image = pygame.transform.flip(self.framesStand[0], True, False)
        else:
            self.image = self.framesStand[0]

    def move(self, x, y, can_attack=False):
        self.reset = False
        speed = 1
        self.moving = True
        self.dirx = x
        self.diry = y
        self.update(anim3=True)
        if self.diry > self.rect.y:
            if self.rect.y + speed < self.diry:
                self.rect.y += speed
            else:
                self.rect.y = self.diry
        elif self.diry < self.rect.y:
            if self.rect.y - speed > self.diry:
                self.rect.y -= speed
            else:
                self.rect.y = self.diry
        if self.dirx > self.rect.x:
            if self.rage:
                if player.rect.x > self.rect.x:
                    self.mirrored = False
                else:
                    self.mirrored = True
            elif self.dirx - 8 > self.rect.x:
                self.mirrored = False
            if self.rect.x + speed < self.dirx:
                self.rect.x += speed
            else:
                self.rect.x = self.dirx
        elif self.dirx < self.rect.x:
            if self.rage:
                if player.rect.x > self.rect.x:
                    self.mirrored = False
                else:
                    self.mirrored = True
            elif self.dirx + 8 < self.rect.x:
                self.mirrored = True
            if self.rect.x - speed > self.dirx:
                self.rect.x -= speed
            else:
                self.rect.x = self.dirx
        if self.rect.x == self.dirx and self.rect.y == self.diry:
            if can_attack and not player.dead:
                self.attack = True
            self.stand()
            self.moving = False
            if self.route:
                self.step += 1
        if (abs(self.rect.x - player.rect.x) < 100 or abs(self.rect.x + self.rect.w - player.rect.x) < 100) \
                and (abs(self.rect.y - player.rect.y) < 100 or 
                     abs(self.rect.y + self.rect.h - player.rect.y) < 100) and not self.v:
            self.rage = True
            self.reset = True
            self.v = True

    def ai(self):
        if self.block:
            return
        if self.rage and not player.dead:
            if self.reset:
                self.a = player.rect.x
                self.b = player.rect.y
        else:
            if self.route:
                if self.step <= len(self.coords) - 1:
                    self.a, self.b = self.coords[self.step][0], self.coords[self.step][1]
                else:
                    self.pos_x = self.rect.x
                    self.pos_y = self.rect.y
                    self.route = False
            else:
                if randint(1, 80) == 1:
                    if not self.afk:
                        self.a, self.b = randint(self.pos_x - 20, self.pos_x + 20), randint(self.pos_y - 20,
                                                                                            self.pos_y + 20)
                    else:
                        if self.mirrored:
                            self.mirrored = False
                        else:
                            self.mirrored = True
        if self.attack and not player.dead:
            self.update(anim5=True)
        else:
            if self.a > self.rect.x:
                if self.rage:
                    self.move(int(self.a) - 33, int(self.b), True)
                else:
                    self.move(int(self.a), int(self.b))
            else:
                if self.rage:
                    self.move(int(self.a) + 23, int(self.b), True)
                else:
                    self.move(int(self.a), int(self.b))


class Player(Sprite):
    def __init__(self, x, y, health=5):
        super().__init__(player_group)
        self.framesMove = [
            load_image('Soldier', 1.1),
            load_image('Soldier', 1.2),
            load_image('Soldier', 1.3),
            load_image('Soldier', 1.4),
            load_image('Soldier', 1.5),
            load_image('Soldier', 1.6),
            load_image('Soldier', 1.7),
            load_image('Soldier', 1.8)
        ]
        self.framesAttack1 = [
            load_image('Soldier', 1.9),
            load_image('Soldier', 1.10),
            load_image('Soldier', 1.11),
            load_image('Soldier', 1.12),
            load_image('Soldier', 1.13),
            load_image('Soldier', 1.14)
        ]
        self.framesStand = [
            load_image('Soldier', 1.15)
        ]
        self.framesDeath = [
            load_image('Soldier', 1.16),
            load_image('Soldier', 1.17),
            load_image('Soldier', 1.18),
            load_image('Soldier', 1.19)
        ]
        self.framesDamage = [
            load_image('Soldier', 1.20),
            load_image('Soldier', 1.21),
            load_image('Soldier', 1.22),
            load_image('Soldier', 1.23)
        ]
        self.health = health
        self.blocked_key = None
        self.mirrored = False
        self.anim_move = True
        self.stop = False
        self.dead = False
        self.time = 0
        self.v = False
        self.cur_frameM = 0
        self.cur_frameA1 = 0
        self.cur_frameDh = 0
        self.cur_frameDmg = 0
        self.image = self.framesStand[0]
        self.rect = pygame.Rect(x * 50 * TILE_SIZE, y * 50 * TILE_SIZE, self.framesMove[0].get_width(),
                                self.framesMove[0].get_height())
        self.x = self.rect.x
        self.y = self.rect.y
        self.abs_pos = (self.rect.x, self.rect.y)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            if self.blocked_key is None and pygame.sprite.spritecollideany(self, enemy_group):
                for i in range(len(enemies)):
                    x = self.rect.collidelistall([i.rect for i in enemies])
                    if enemies[i].mirrored and i in x:
                        self.blocked_key = 'd'
                        return
            if self.blocked_key is None and pygame.sprite.spritecollideany(self, tiles_group):
                self.blocked_key = 'd'
                return
            if self.blocked_key == 'd' and (
                    pygame.sprite.spritecollideany(self, tiles_group) or pygame.sprite.spritecollideany(self,
                                                                                                        enemy_group)):
                self.mirrored = False
                return
            self.blocked_key = None
            if not self.anim_move:
                return
            self.rect.x += 1
            self.cur_frameM = (self.cur_frameM + 1) % len(self.framesMove)
            self.image = self.framesMove[self.cur_frameM]
            if self.mirrored:
                self.mirrored = False
        elif keys[pygame.K_a]:
            if self.blocked_key is None and pygame.sprite.spritecollideany(self, enemy_group):
                for i in range(len(enemies)):
                    x = self.rect.collidelistall([i.rect for i in enemies])
                    if not enemies[i].mirrored and i in x:
                        self.blocked_key = 'a'
                        return
            if self.blocked_key is None and pygame.sprite.spritecollideany(self, tiles_group):
                self.blocked_key = 'a'
                return
            if self.blocked_key == 'a' and (
                    pygame.sprite.spritecollideany(self, tiles_group) or pygame.sprite.spritecollideany(self,
                                                                                                        enemy_group)):
                self.mirrored = True
                return
            self.blocked_key = None
            if not self.anim_move:
                return
            self.rect.x -= 1
            self.cur_frameM = (self.cur_frameM + 1) % len(self.framesMove)
            self.image = pygame.transform.flip(self.framesMove[self.cur_frameM], True, False)
            if not self.mirrored:
                self.mirrored = True
        elif keys[pygame.K_w]:
            if self.blocked_key is None and pygame.sprite.spritecollideany(self, tiles_group):
                self.blocked_key = 'w'
                return
            if self.blocked_key == 'w' and pygame.sprite.spritecollideany(self, tiles_group):
                return
            self.blocked_key = None
            if not self.anim_move:
                return
            self.rect.y -= 1
            self.cur_frameM = (self.cur_frameM + 1) % len(self.framesMove)
            if self.mirrored:
                self.image = pygame.transform.flip(self.framesMove[self.cur_frameM], True, False)
            else:
                self.image = self.framesMove[self.cur_frameM]
        elif keys[pygame.K_s]:
            if self.blocked_key is None and pygame.sprite.spritecollideany(self, tiles_group):
                self.blocked_key = 's'
                return
            if self.blocked_key == 's' and pygame.sprite.spritecollideany(self, tiles_group):
                return
            self.blocked_key = None
            if not self.anim_move:
                return
            self.rect.y += 1
            self.cur_frameM = (self.cur_frameM + 1) % len(self.framesMove)
            if self.mirrored:
                self.image = pygame.transform.flip(self.framesMove[self.cur_frameM], True, False)
            else:
                self.image = self.framesMove[self.cur_frameM]
        else:
            if not self.anim_move:
                return
            self.stand()
        for i in range(len(enemies)):
            if (abs(enemies[i].rect.x - self.rect.x) < 50 or abs(
                    enemies[i].rect.x + enemies[i].rect.w - self.rect.x) < 50) \
                    and (abs(enemies[i].rect.y - self.rect.y) < 50 or
                         abs(enemies[i].rect.y + enemies[i].rect.h - self.rect.y) < 50):
                enemies[i].rage = True
            enemies[i].reset = True
        self.x, self.y = self.rect.x, self.rect.y
        if self.rect.x >= 1330:
            if chapter == 0:
                next_level()
            else:
                win_screen()

    def rect_xy(self):
        self.x = self.rect.x
        self.y = self.rect.y

    def old_xy(self):
        self.rect.x = self.x
        self.rect.y = self.y

    def stand(self):
        if self.mirrored:
            self.image = pygame.transform.flip(self.framesStand[0], True, False)
        else:
            self.image = self.framesStand[0]

    def update(self, anim1=False, anim2=False, anim3=False):
        global attackAnim1
        global moving
        global damageAnim2
        global damageAnim
        global deathAnim2
        global deathAnim
        if self.dead:
            return
        if anim1:
            damageAnim = False
            anim2 = False
            anim3 = False
            attackAnim1 = False
            if self.cur_frameDh == 0:
                self.anim_move = False
            self.cur_frameDh = (self.cur_frameDh + 1) % (len(self.framesDeath) * 4)
            if self.mirrored:
                if self.cur_frameDh // 4 == 1:
                    self.rect.x = self.x - 3
                elif self.cur_frameDh // 4 == 2:
                    self.rect.y = self.y + 2
                elif self.cur_frameDh // 4 == 3:
                    self.rect.y = self.y + 11
                if self.cur_frameDh != 0:
                    self.image = pygame.transform.flip(self.framesDeath[self.cur_frameDh // 4], True, False)
            else:
                if self.cur_frameDh // 4 == 1:
                    self.rect.x = self.x + 3
                elif self.cur_frameDh // 4 == 2:
                    self.rect.y = self.y + 2
                elif self.cur_frameDh // 4 == 3:
                    self.rect.y = self.y + 11
                if self.cur_frameDh != 0:
                    self.image = self.framesDeath[self.cur_frameDh // 4]
            if self.cur_frameDh == 0:
                self.time = 0
                self.dead = True
                deathAnim = False
                end_screen()
                if self.mirrored:
                    self.image = pygame.transform.flip(self.framesDeath[-1], True, False)
                else:
                    self.image = self.framesDeath[-1]
        if anim2:
            attackAnim1 = False
            if self.cur_frameDmg == 0:
                self.anim_move = False
            self.old_xy()
            self.cur_frameDmg = (self.cur_frameDmg + 1) % (len(self.framesDamage) * 4)
            if self.mirrored:
                self.image = pygame.transform.flip(self.framesDamage[self.cur_frameDmg // 4], True, False)
            else:
                self.image = self.framesDamage[self.cur_frameDmg // 4]
            if self.cur_frameDmg == 0:
                self.stand()
                self.time = 0
                damageAnim = False
                self.anim_move = True
        if anim3:
            if self.cur_frameA1 == 0:
                self.rect_xy()
                self.anim_move = False
            self.cur_frameA1 = (self.cur_frameA1 + 1) % (len(self.framesAttack1) * 4)
            if self.mirrored:
                self.image = pygame.transform.flip(self.framesAttack1[self.cur_frameA1 // 4], True, False)
                self.rect.y = self.y
                if self.cur_frameA1 // 4 == 5:
                    self.rect.x = self.x - 3
                elif self.cur_frameA1 // 4 > 2:
                    self.rect.x = self.x - 25
                elif self.cur_frameA1 // 4 == 2:
                    self.rect.y = self.y - 10
                    self.rect.x = self.x - 7
                elif self.cur_frameA1 // 4 == 1:
                    self.rect.y = self.y
            else:
                self.image = self.framesAttack1[self.cur_frameA1 // 4]
                self.rect.y = self.y
                if self.cur_frameA1 // 4 > 4:
                    self.rect.x = self.x - 7
                elif self.cur_frameA1 // 4 == 2:
                    self.rect.y = self.y - 10
                elif self.cur_frameA1 // 4 == 1:
                    self.rect.y = self.y
            if self.cur_frameA1 // 4 == 4:
                self.rect.w += 25
            if pygame.sprite.spritecollideany(self, enemy_group) and not self.stop and self.cur_frameA1 // 4 == 4:
                if damagedEnemies:
                    damagedEnemies.clear()
                act = False
                act2 = False
                self.stop = True
                sprites = pygame.sprite.spritecollide(self, enemy_group, dokill=False)
                group = enemy_group.sprites()
                for i in range(len(sprites)):
                    sprite = sprites[i]
                    for j in range(len(group)):
                        if group[j] == sprite and not enemies[j].block:
                            if not enemies[j].dead:
                                enemies[j].damage()
                            if not enemies[j].dead:
                                damagedEnemies.append(enemies[j])
                                act = True
                            else:
                                deadEnemies.append(enemies[j])
                                act2 = True
                if act:
                    damageAnim2 = True
                if act2:
                    deathAnim2 = True
            if self.cur_frameA1 // 4 == 4:
                self.rect.w -= 25
            if self.cur_frameA1 == 0:
                self.rect.x = self.x
                self.rect.y = self.y
                attackAnim1 = False
                self.time = 0
                self.anim_move = True
                self.stop = False

    def damage(self):
        global damageAnim
        global deathAnim
        global moving
        global attackAnim1
        if not self.dead:
            if self.health > 0:
                self.health -= 1
            if self.health == 0 and not deathAnim:
                moving = False
                attackAnim1 = False
                damageAnim = False
                deathAnim = True
            else:
                moving = False
                attackAnim1 = False
                damageAnim = True

    def heal(self):
        if self.health < 5:
            self.health += 1


class PlayerNPC(Sprite):
    def __init__(self, x, y, csize, *args):
        super().__init__(player_group)
        self.framesMove = [
            load_image('Soldier', 1.1, csize=csize),
            load_image('Soldier', 1.2, csize=csize),
            load_image('Soldier', 1.3, csize=csize),
            load_image('Soldier', 1.4, csize=csize),
            load_image('Soldier', 1.5, csize=csize),
            load_image('Soldier', 1.6, csize=csize),
            load_image('Soldier', 1.7, csize=csize),
            load_image('Soldier', 1.8, csize=csize)
        ]
        self.framesStand = [
            load_image('Soldier', 1.15, csize=csize)
        ]
        self.coords = list(args)
        self.cur_frameM = 0
        self.step = 0
        self.x = 0
        self.cd = False
        self.y = 0
        self.a = 0
        self.b = 0
        self.dirx = 0
        self.diry = 0
        self.ready = True
        self.image = self.framesStand[0]
        self.rect = pygame.Rect(x * 50 * (csize - 3), y * 50 * (csize - 3), self.framesMove[0].get_width(),
                                self.framesMove[0].get_height())

    def stand(self):
        self.image = self.framesStand[0]

    def move(self, x, y):
        self.ready = False
        speed = 1
        self.dirx = x
        self.diry = y
        self.update(anim1=True)
        if self.diry > self.rect.y:
            if self.rect.y + speed < self.diry:
                self.rect.y += speed
            else:
                self.rect.y = self.diry
        elif self.diry < self.rect.y:
            if self.rect.y - speed > self.diry:
                self.rect.y -= speed
            else:
                self.rect.y = self.diry
        if self.dirx > self.rect.x:
            if self.rect.x + speed < self.dirx:
                self.rect.x += speed
            else:
                self.rect.x = self.dirx
        elif self.dirx < self.rect.x:
            if self.rect.x - speed > self.dirx:
                self.rect.x -= speed
            else:
                self.rect.x = self.dirx
        if self.rect.x == self.dirx and self.rect.y == self.diry:
            self.stand()
            self.ready = True
            self.step += 1
            self.cd = True

    def rect_xy(self):
        self.x = self.rect.x
        self.y = self.rect.y

    def update(self, ai=False, anim1=False):
        if anim1:
            self.rect_xy()
            self.cur_frameM = (self.cur_frameM + 1) % len(self.framesMove)
            self.image = self.framesMove[self.cur_frameM]
        else:
            self.ai()

    def ai(self):
        if self.ready:
            if self.step <= len(self.coords) - 1:
                self.a, self.b = self.coords[self.step][0], self.coords[self.step][1]
            else:
                self.kill()
        if self.cd:
            pygame.time.delay(1000)
            self.cd = False
        if self.a > self.rect.x:
            self.move(int(self.a), int(self.b))
        else:
            self.move(int(self.a), int(self.b))


codes = {
    'params': 'name, isMirrored, isDown',
    '0': ['path_e', False, False],
    '1': ['path', False, False],
    '2': ['path', False, True],
    '3': ['path_e', False, True],
    '5': ['path_t', False, False],
    '6': ['path_t2', False, False],
    '7': ['path_t3', False, False],
    '8': ['path_t4', False, False]
}


def generate_level(level, csize=0):
    f = 0
    px, py = None, None
    for y in range(len(level)):
        f = (f + 0.3) % 0.6
        for x in range(len(level[y])):
            if level[y][x] == 'g':
                if csize == 0:
                    Floor('grass', x, y, f)
                else:
                    Floor('grass', x, y, f, csize=csize)
            elif level[y][x] == 't':
                if csize == 0:
                    Tile('tree2', x, y, f)
                    Floor('grass', x, y, f)
                else:
                    Tile('tree2', x, y, f, csize=csize)
                    Floor('grass', x, y, f, csize=csize)
            elif level[y][x] == '@':
                if csize == 0:
                    Floor('path', x, y, f)
                else:
                    Floor('path', x, y, f, csize=csize)
                px = x
                py = y
            elif level[y][x] == 'e':
                if csize == 0:
                    Tile('path', x, y, f)
                else:
                    Tile('path', x, y, f, csize=csize)
            elif level[y][x] == 'c':
                if csize == 0:
                    Tile('tower', x, y, f)
                    Floor('grass', x, y, f)
                else:
                    Tile('tower', x, y, f, csize=csize)
                    Floor('grass', x, y, f, csize=csize)
            elif level[y][x] == 'h':
                if csize == 0:
                    Tile('grass', x, y, f)
                else:
                    Tile('grass', x, y, f, csize=csize)
            elif level[y][x] == 's':
                if csize == 0:
                    Tile('sign', x, y, f)
                    Floor('grass', x, y, f)
                else:
                    Tile('sign', x, y, f, csize=csize)
                    Floor('grass', x, y, f, csize=csize)
            else:
                params = codes[level[y][x]]
                if csize == 0:
                    Floor(params[0], x, y, isMirrored=params[1], isDown=params[2])
                else:
                    Floor(params[0], x, y, isMirrored=params[1], isDown=params[2], csize=csize)
    return px, py


def end_screen():
    global running
    pygame.mixer.music.stop()
    image = load_image('bg_over.png')
    image.set_alpha(190)
    image2 = load_image('end_screen.png')
    screen.blit(image, (0, 0))
    screen.blit(image2, (0, 100))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x = event.pos[0]
                y = event.pos[1]
                if 500 < x < 920 and 310 < y < 410:
                    reset_game()
                    return
                elif 500 < x < 920 and 500 < y < 600:
                    terminate()
                    return
        time(stop=True)
        pygame.display.flip()
        clock.tick(FPS)


def cutscene():
    global tiles_group, floor_group, player_group, all_sprites
    level_map = load_level('cutscene.txt')
    px, py = generate_level(level_map, 4)
    all_sprites.add(*tiles_group)
    all_sprites.add(*floor_group)
    pause = False
    PlayerNPC(px, py - 0.3, 7, [740, (py - 0.3) * 200], [1400, (py - 0.3) * 200])
    font = pygame.font.SysFont(None, 50)
    font2 = pygame.font.SysFont(None, 35)
    text1 = font.render('"E" - skip the cutscene', False, 'grey')
    text_rect1 = text1.get_rect(right=screen.get_rect().right - 20, bottom=screen.get_rect().bottom - 90)
    text1.set_alpha(190)
    text2 = font.render('"X" - pause the cutscene', False, 'grey')
    text_rect2 = text2.get_rect(right=screen.get_rect().right - 20, bottom=screen.get_rect().bottom - 30)
    text2.set_alpha(190)
    text3 = font2.render(
        'One day, a beautiful princess was kidnapped by monsters and imprisoned in a long-abandoned tower', False,
        (230, 230, 230))
    text4 = font2.render('in the forest. The brave knight Richard volunteered to go to the forest', False,
                         (230, 230, 230))
    text5 = font2.render('inhabited by these monsters to save the princess. But the monsters that inhabited', False,
                         (230, 230, 230))
    text6 = font2.render("the forest already knew about Richard's arrival...", False, (230, 230, 230))
    text_rect3 = text3.get_rect(top=screen.get_rect().top + 20, centerx=screen.get_rect().centerx)
    text_rect4 = text4.get_rect(top=screen.get_rect().top + 50, centerx=screen.get_rect().centerx)
    text_rect5 = text5.get_rect(top=screen.get_rect().top + 80, centerx=screen.get_rect().centerx)
    text_rect6 = text6.get_rect(top=screen.get_rect().top + 110, centerx=screen.get_rect().centerx)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == 101:
                    return
                elif event.key == 120:
                    pause = not pause
        if not pause:
            player_group.update()
        if len(player_group) == 0:
            break
        floor_group.draw(screen)
        tiles_group.draw(screen)
        player_group.draw(screen)
        screen.blit(text1, text_rect1)
        screen.blit(text2, text_rect2)
        screen.blit(text3, text_rect3)
        screen.blit(text4, text_rect4)
        screen.blit(text5, text_rect5)
        screen.blit(text6, text_rect6)
        pygame.display.flip()


def win_screen():
    global running, tiles_group, floor_group, player_group, all_sprites
    pygame.mixer.music.stop()
    tiles_group = SpriteGroup()
    floor_group = SpriteGroup()
    player_group = SpriteGroup()
    all_sprites = SpriteGroup()
    level_map = load_level('finish.txt')
    px, py = generate_level(level_map, 2)
    all_sprites.add(*tiles_group)
    all_sprites.add(*floor_group)
    PlayerNPC(px + 999, py + 999, 1)
    image = load_image('aa1.png')
    image2 = load_image('finish_screen.png')
    font = pygame.font.SysFont(None, 70)
    font2 = pygame.font.SysFont(None, 50)
    text = font.render('Congratulations! You saved the princess!', False, 'white')
    text_rect = text.get_rect(top=screen.get_rect().top + 60, centerx=screen.get_rect().centerx)
    time_points = 500 - int(seconds)
    if time_points < 0:
        time_points = 0
    text1 = font2.render(f'Points for kills: {str(points)} points', False, 'white')
    text_rect1 = text1.get_rect(left=screen.get_rect().centerx - 480, centery=screen.get_rect().centery - 190)
    text2 = font2.render(f'Points for time: {str(time_points)} points', False, 'white')
    text_rect2 = text2.get_rect(left=screen.get_rect().centerx - 480, centery=screen.get_rect().centery - 120)
    text3 = font2.render(f'Total points: {int(points) + int(time_points)}', False, 'white')
    text_rect3 = text3.get_rect(left=screen.get_rect().centerx - 480, centery=screen.get_rect().centery - 50)
    with open('results.txt', encoding='utf8') as f:
        max_points = 0
        data = f.readlines()
        for string in data:
            if 'Рекорд:' in string:
                max_points = int(string.split()[2])
    with open('results.txt', 'w', encoding='utf8') as f:
        total = int(points) + time_points
        if total > max_points:
            f.write(f'Рекорд: всего {str(total)} очков\n')
            f.write('=========================\n')
            f.write(f'Последняя игра: всего {str(total)} очков\n')
            f.write(f'Очки за убийства: {str(points)} очков\n')
            f.write(f'Очки за время: {str(time_points)} очков')
        else:
            f.write(f'Рекорд: всего {str(max_points)} очков\n')
            f.write('=========================\n')
            f.write(f'Последняя игра: всего {str(total)} очков\n')
            f.write(f'Очки за убийства: {str(points)} очков\n')
            f.write(f'Очки за время: {str(time_points)} очков')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x = event.pos[0]
                y = event.pos[1]
                if 170 < x < 580 and 490 < y < 580:
                    reset_game()
                    return
                elif 820 < x < 1230 and 490 < y < 580:
                    terminate()
                    return
        floor_group.draw(screen)
        tiles_group.draw(screen)
        screen.blit(image, (550, 150))
        screen.blit(image2, (100, 0))
        screen.blit(text, text_rect)
        screen.blit(text1, text_rect1)
        screen.blit(text2, text_rect2)
        screen.blit(text3, text_rect3)
        pygame.display.flip()


def main_menu():
    global tiles_group, floor_group, player_group, all_sprites
    level_map = load_level('start.txt')
    px, py = generate_level(level_map, 2)
    all_sprites.add(*tiles_group)
    all_sprites.add(*floor_group)
    PlayerNPC(px + 999, py + 999, 1)
    image = load_image('menu_screen.png')
    font = pygame.font.SysFont(None, 40)
    text = font.render('Developed by Stanislavsky', False, 'grey')
    text.set_alpha(180)
    text_rect = text.get_rect(left=screen.get_rect().left + 10, bottom=screen.get_rect().bottom - 10)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x = event.pos[0]
                y = event.pos[1]
                if 490 < x < 910 and 360 < y < 500:
                    return
                elif 490 < x < 910 and 545 < y < 685:
                    terminate()
                    return
        floor_group.draw(screen)
        tiles_group.draw(screen)
        screen.blit(image, (0, 40))
        screen.blit(text, text_rect)
        pygame.display.flip()


def terminate():
    global running
    running = False


def reset_game():
    global enemies, level_map, player, player_group, health_group, enemy_group, all_sprites, health_bar, points, \
        chapter, floor_group, tiles_group
    level_map = load_level('map1.txt')
    tiles_group = SpriteGroup()
    floor_group = SpriteGroup()
    player_group = SpriteGroup()
    health_group = SpriteGroup()
    enemy_group = SpriteGroup()
    all_sprites = SpriteGroup()
    px, py = generate_level(level_map)
    all_sprites.add(*tiles_group)
    all_sprites.add(*floor_group)
    player = Player(px, py)
    enemies = [EnemyArmoredOrc(38, 8, False, True, [800, 320], [800, 640], [315, 640], [315, 160], [150, 160]),
               EnemyOrc(39, 8, False, True, [800, 320], [800, 640], [315, 640], [315, 160], [180, 160]),
               EnemyOrc(40, 8, False, True, [800, 320], [800, 640], [315, 640], [315, 160], [210, 160]),
               EnemyArmoredOrc(13, 11, True), EnemyOrc(15, 8, True), EnemyOrc(12, 11, True),
               EnemyOrc(8, 10), EnemyOrc(7, 6), EnemyOrc(10, 17)
               ]
    all_sprites.add(*enemy_group)
    health_bar = Health()
    time(True)
    points = 0
    chapter = 0
    pygame.mixer.music.play()


def next_level():
    global enemies, level_map, player, player_group, health_group, enemy_group, all_sprites, health_bar, points, \
        chapter, floor_group, tiles_group
    hp_frame = health_bar.cur_frameHealth
    hp_left = player.health
    level_map = load_level('map2.txt')
    tiles_group = SpriteGroup()
    floor_group = SpriteGroup()
    player_group = SpriteGroup()
    health_group = SpriteGroup()
    enemy_group = SpriteGroup()
    all_sprites = SpriteGroup()
    px, py = generate_level(level_map)
    all_sprites.add(*tiles_group)
    all_sprites.add(*floor_group)
    player = Player(px, py, health=hp_left)
    enemies = [
        EnemyOrc(7, 5), EnemyOrc(11, 3), EnemyOrc(13, 6), EnemyOrc(4, 14), EnemyOrc(5, 11),
        EnemyOrc(14, 11), EnemyOrc(17, 12), EnemyOrc(22, 10), EnemyArmoredOrc(17, 8), EnemyArmoredOrc(18, 7),
        EnemyOrc(14, 16), EnemyOrc(16, 15), EnemyOrc(12, 16), EnemyOrc(20, 16), EnemyArmoredOrc(26, 4, True)
    ]
    all_sprites.add(*enemy_group)
    chapter += 1
    health_bar = Health(frame=hp_frame)


def time(reset=False, stop=False):
    global start_time, seconds
    if stop:
        return
    if reset:
        seconds = None
        start_time = pygame.time.get_ticks()
    cur_time = pygame.time.get_ticks() - start_time
    seconds = str(int(cur_time / 1000))


def points_count(kill1=False, kill2=False):
    global points
    if kill1:
        points = str(int(points) + 25)
    elif kill2:
        points = str(int(points) + 100)


def points_print():
    global points
    font = pygame.font.SysFont(None, 50)
    text = font.render(str(f'Points: {points}'), False, 'white')
    text_rect = text.get_rect(right=screen.get_rect().right - 20, top=screen.get_rect().top + 30)
    return text, text_rect


def music_print():
    font = pygame.font.SysFont(None, 50)
    text = font.render('"R" - Pause or play the music', False, 'grey')
    text.set_alpha(190)
    text_rect = text.get_rect(right=screen.get_rect().right - 20, bottom=screen.get_rect().bottom - 10)
    return text, text_rect


pygame.mixer.music.load('data/Music.ogg')
pygame.mixer.music.set_volume(0.25)
running = True
tiles_group = SpriteGroup()
floor_group = SpriteGroup()
player_group = SpriteGroup()
all_sprites = SpriteGroup()
main_menu()
tiles_group = SpriteGroup()
floor_group = SpriteGroup()
player_group = SpriteGroup()
all_sprites = SpriteGroup()
if running:
    cutscene()
level_map = load_level('map1.txt')
clock = pygame.time.Clock()
tiles_group = SpriteGroup()
floor_group = SpriteGroup()
player_group = SpriteGroup()
health_group = SpriteGroup()
enemy_group = SpriteGroup()
all_sprites = SpriteGroup()
px, py = generate_level(level_map)
all_sprites.add(*tiles_group)
all_sprites.add(*floor_group)
player = Player(px, py)
enemies = [EnemyArmoredOrc(38, 8, False, True, [800, 320], [800, 640], [315, 640], [315, 160], [150, 160]),
           EnemyOrc(39, 8, False, True, [800, 320], [800, 640], [315, 640], [315, 160], [180, 160]),
           EnemyOrc(40, 8, False, True, [800, 320], [800, 640], [315, 640], [315, 160], [210, 160]),
           EnemyArmoredOrc(13, 11, True), EnemyOrc(15, 8, True), EnemyOrc(12, 11, True),
           EnemyOrc(8, 10), EnemyOrc(7, 6), EnemyOrc(10, 17)
           ]
all_sprites.add(*enemy_group)
health_bar = Health()
pygame.mixer.music.play(-1)

points = 0
seconds = 0
chapter = 0
stop = False
moving = False
attackAnim1 = False
deathAnim = False
deathAnim2 = False
damageAnim = False
damageAnim2 = False
damagedEnemies = []
damagedEnemiesDone = 0
deadEnemies = []
deadEnemiesDone = 0
start_time = pygame.time.get_ticks()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and not player.dead:
            moving = True
            if event.key == 114:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
        elif event.type == pygame.KEYUP and not player.dead:
            moving = False
            player.stand()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and not player.dead:
                attackAnim1 = True
            elif event.button == 2 and not player.dead:
                enemy_moving = True

    if deathAnim and not player.dead:
        player_group.update(anim1=True)
    elif damageAnim and not player.dead:
        player_group.update(anim2=True)
    if attackAnim1 and not player.dead:
        player_group.update(anim3=True)
    elif moving and not player.dead:
        player.move()
    if deathAnim2:
        enemy_group.update(deadEnemies, True, False)
    elif damageAnim2:
        enemy_group.update(damagedEnemies, False, True)
    time()
    enemy_group.update(anim4=True)
    screen.fill(pygame.Color("black"))
    floor_group.draw(screen)
    enemy_group.draw(screen)
    tiles_group.draw(screen)
    health_group.draw(screen)
    player_group.draw(screen)
    text, text_rect = points_print()
    text1, text_rect1 = music_print()
    screen.blit(text, text_rect)
    screen.blit(text1, text_rect1)
    clock.tick(FPS)
    pygame.display.flip()
pygame.quit()

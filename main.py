import pygame, os
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
 
 
class Wall(pygame.sprite.Sprite):
    """This class represents the bar at the bottom that the player controls """
 
    def __init__(self, x, y, width, height, color):
        """ Constructor function """
 
        # Call the parent's constructor
        super().__init__()
 
        # Make a BLUE wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
 
class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the
    player controls """
 
    # Set speed vector
    change_x = 0
    change_y = 0
 
    def __init__(self, x, y):
        """ Constructor function """
 
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(WHITE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
    def changespeed(self, x, y):
        """ Change the speed of the player. Called with a keypress. """
        self.change_x += x
        self.change_y += y
 
    def move(self, walls):
        """ Find a new position for the player """
 
        # Move left/right
        self.rect.x += self.change_x
 
        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
 
 
class Room(object):
    """ Base class for all rooms. """
 
    # Each room has a list of walls, and of enemy sprites.
    wall_list = None
    enemy_sprites = None
 
    def __init__(self):
        """ Constructor, create our lists. """
        self.wall_list = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
 
 
class Room1(Room):
    """This creates all the walls in room 1"""
    def __init__(self):
        super().__init__()
        # Make the walls. (x_pos, y_pos, width, height)
 
        # This is a list of walls. Each is in the form [x, y, width, height]
        walls = [[0, 0, 20, 250, WHITE],
                 [0, 350, 20, 250, WHITE],
                 [780, 0, 20, 250, WHITE],
                 [780, 350, 20, 250, WHITE],
                 [20, 0, 760, 20, WHITE],
                 [20, 580, 760, 20, WHITE],
                 [390, 50, 20, 500, WHITE]
                ]

        pygame.display.flip()
 
        # Loop through the list. Create the wall, add it to the list
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
 
 
class Room2(Room):
    """This creates all the walls in room 2"""
    def __init__(self):
        super().__init__()
 
        walls = [[0, 0, 20, 250, WHITE],
                 [0, 350, 20, 250, WHITE],
                 [780, 0, 20, 250, WHITE],
                 [780, 350, 20, 250, WHITE],
                 [20, 0, 760, 20, WHITE],
                 [20, 580, 760, 20, WHITE],
                 [190, 50, 20, 500, WHITE],
                 [590, 50, 20, 500, WHITE]
                ]
 
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
 
 
class Room3(Room):
    """This creates all the walls in room 3"""
    def __init__(self):
        super().__init__()
 
        walls = [[0, 0, 20, 250, WHITE],
                 [0, 350, 20, 250, WHITE],
                 [780, 0, 20, 250, WHITE],
                 [780, 350, 20, 250, WHITE],
                 [20, 0, 760, 20, WHITE],
                 [20, 580, 760, 20, WHITE]
                ]
 
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
 
        for x in range(100, 800, 100):
            for y in range(50, 451, 300):
                wall = Wall(x, y, 20, 200, WHITE)
                self.wall_list.add(wall)
 
        for x in range(150, 700, 100):
            wall = Wall(x, 200, 20, 200, WHITE)
            self.wall_list.add(wall)
 
 
def main():
    """ Main Program """
 
    # Call this function so the Pygame library can initialize itself
    pygame.init()
 
    # Create an 800x600 sized screen
    screen = pygame.display.set_mode([800, 600])
 
    # Set the title of the window
    pygame.display.set_caption('DataLight')
 
    # Create the player paddle object
    player = Player(50, 50)
    movingsprites = pygame.sprite.Group()
    movingsprites.add(player)
 
    rooms = []
 
    room = Room1()
    rooms.append(room)
 
    room = Room2()
    rooms.append(room)
 
    room = Room3()
    rooms.append(room)
 
    current_room_no = 0
    current_room = rooms[current_room_no]

 
    clock = pygame.time.Clock()
 
    done = False
 
    while not done:
 
        # --- Event Processing ---
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.changespeed(-2, 0)
                if event.key == pygame.K_d:
                    player.changespeed(2, 0)
                if event.key == pygame.K_w:
                    player.changespeed(0, -2)
                if event.key == pygame.K_s:
                    player.changespeed(0, 2)
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    player.changespeed(2, 0)
                if event.key == pygame.K_d:
                    player.changespeed(-2, 0)
                if event.key == pygame.K_w:
                    player.changespeed(0, 2)
                if event.key == pygame.K_s:
                    player.changespeed(0, -2)
 
        # --- Game Logic ---
 
        player.move(current_room.wall_list)
 
        if player.rect.x < -15:
            if current_room_no == 0:
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.x = 790
            elif current_room_no == 2:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.x = 790
            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 790
 
        if player.rect.x > 801:
            if current_room_no == 0:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.x = 0
            elif current_room_no == 1:
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.x = 0
            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 0
 
        # --- Drawing ---
        screen.fill(BLACK)
 
        movingsprites.draw(screen)
        current_room.wall_list.draw(screen)

        screen=pygame.display.set_mode((640, 480))
        light=pygame.image.load('circle.png') # radial gradient used for light pattern
        light=pygame.transform.scale(light, (800,800)) # resize gradient

        night = True # boolean to set if it is night or day
        if event.type == pygame.MOUSEBUTTONDOWN:
            night = not night # toggle night between true and false
        if event.type == pygame.QUIT:
            pygame.quit()
            os.exit()

        pos = []
        pos = pygame.mouse.get_pos() # get mouse position

        screen.fill(pygame.color.Color('Red')) # just a background
        for x in range(0, 640, 20):
            pygame.draw.line(screen, pygame.color.Color('Green'), (x, 0), (x, 480), 3)  # just lines on the background

        if night: # if light effect needed
            filter = pygame.surface.Surface((640, 480)) # create surface same size as window
            filter.fill(pygame.color.Color('Black')) # Black will give dark unlit areas, Grey will give you a fog
            filter.blit(light,(pos[0]-400,pos[1]-400)) # blit light to the filter surface -400 is to center effect
            screen.blit(filter, (0, 0), special_flags=pygame.BLEND_RGBA_MIN) # blit filter surface but with a blend

        pygame.display.flip()
 
        clock.tick(60)
 
    pygame.quit()
 
if __name__ == "__main__":
    main()

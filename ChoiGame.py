import pygame


#other wrapped shizz

def start(title):
    pygame.init()
    titl = pygame.display.set_caption(title)
    return titl,





#mainly just display shizz to be honest

def screen_size(x , y):
    return pygame.display.set_mode((x, y))
   
def resize_display(x, y):
    return pygame.display.set_mode((x, y), pygame.RESIZABLE)

def game_name(name):
    pygame.display.set_caption(name)

def fill_screen(screen, x, y, z):
    screen.fill((x, y, z))

def update_specific():
    pygame.display.update()

def update_full():
    pygame.display.flip()




#image shizz

def import_img(img):
    return pygame.image.load(img).convert()#1. loading the image


def import_img_alpha(img):
    return pygame.image.load(img).convert_alpha()#1. loading the image

def place_img(screen, img, x, y):#3. placing the image on screen
    screen.blit(img, (x, y))  

def scale_img(image ,width ,height):#2. making the image the correct size
    return pygame.transform.scale(image,
                                  (image.get_width() * width,
                                   image.get_height() * height))    





#mainly just core shizz

def handle_quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def quit_game():
    pygame.quit()

def init():
    pygame.init()




#clock shizz

def make_clock():
    return pygame.time.Clock()

def fps(clock, x):
    clock.tick(x)   





#character editing and movement

def movement_wasd(player ,speed_up ,speed_down ,speed_left ,speed_right):
    keys = pygame.key.get_pressed()

    
    if keys[pygame.K_w]:
        player.y -= speed_up
    if keys[pygame.K_s]:
        player.y += speed_down
    if keys[pygame.K_a]:
        player.x -= speed_left
    if keys[pygame.K_d]:
        player.x += speed_right

    return player










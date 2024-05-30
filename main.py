import pygame
import pygame.mixer
import sys

pygame.init()
pygame.mixer.init()

WHITE =(255,255,255)
BLACK = (0,0,0)
starter_time = 120
x = 1200
y = 600
backgroundSound = pygame.mixer.Sound("backgroundSound.wav")
playerOneHitKnife = pygame.mixer.Sound("playeronehit.wav")
playerTwoHitKnife = pygame.mixer.Sound("playertwohit.wav")
playerOneDamageTake = pygame.mixer.Sound("playerOneDamageTake.wav")
playerTwoDamageTake = pygame.mixer.Sound("playerTwodamageTake.wav")
playerOneWin = pygame.mixer.Sound("playerOneWins.wav")
playerTwoWins = pygame.mixer.Sound("playerTwoWins.wav")
playerJumpSound = pygame.mixer.Sound("finalJump.wav")
backgroundSound.set_volume(0.5)
backgroundSound.play()
menuBack = pygame.image.load("back.png")
firstWin = pygame.image.load("wins/1Win.png")
screen = pygame.display.set_mode((x, y))
pygame.display.set_caption("Animation Example")

image = pygame.image.load("s1/Attack1.png")
image = pygame.transform.scale(image, (1500, 800))

image2 = pygame.image.load("s1/Run.png")
image2 = pygame.transform.scale(image2, (2000, 800))

image3 = pygame.image.load("s1/Die.png")
image3 = pygame.transform.scale(image3, (2000, 800))

image4 = pygame.image.load("s1/Idle.png")
image4 = pygame.transform.scale(image4, (2000, 800))

image_jump = pygame.image.load("s1/Run.png")
image_jump = pygame.transform.scale(image_jump, (2000, 800))

image5 = pygame.image.load("s2/Idle.png")
image5 = pygame.transform.scale(image5, (200, 200))
image5_left = pygame.transform.flip(image5, True, False)

image6 = pygame.image.load("s2/Run.png")
image6 = pygame.transform.scale(image6, (2000, 200))

image6_left = pygame.transform.flip(image6, True, False)

image7 = pygame.image.load("s2/Hit.png")
image7 = pygame.transform.scale(image7, (2000, 200))
image7_left = pygame.transform.flip(image7, True, False)

image8 = pygame.image.load("s2/Die.png")
image8 = pygame.transform.scale(image8, (500, 200))
image8_left = pygame.transform.flip(image8, True, False)

background = pygame.image.load("s1/backIM.png")
background = pygame.transform.scale(background, (x, y))

font_size = 36
vfx = pygame.image.load("VFX_Effects/VFX.jpg")
fontTime = pygame.font.Font(None,font_size)
timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event,1000)
current_time = starter_time

images = {
    'first': pygame.image.load("FX/pillar/pillar light 1.png"),
    'second': pygame.image.load("FX/pillar/pillar light 2.png"),
    'third': pygame.image.load("FX/pillar/pillar light 3.png"),
    "fourth" : pygame.image.load("FX/pillar/pillar light 4.png"),
    "fifth" : pygame.image.load("FX/pillar/pillar light 5.png")
}

vfx_frame_width = vfx.get_width() // 4
vfx_frame_height = vfx.get_height() // 4

current_vfx_frame = 0
isVFX = False

frame_width = image.get_width() // 6
frame_height = image.get_height()
frame_width2 = image2.get_width() // 8
frame_height2 = image2.get_height() // 1
frame_width3 = image3.get_width() // 6
frame_height3 = image3.get_height()
frame_width4 = image4.get_width() // 8
frame_height4 = image4.get_height()
frame_widthJump = image_jump.get_width() // 2
frame_heightJump = image_jump.get_height()

frame_width5 = image5.get_width() // 1
frame_height5 = image5.get_height()
frame_width6 = image6.get_width() // 8
frame_height6 = image6.get_height() // 1
frame_width7 = image7.get_width() // 8
frame_height7 = image7.get_height()
frame_width8 = image8.get_width() // 4
frame_height8 = image8.get_height()

frame_heightVFX = vfx.get_width() // 4
frame_widthVFX = vfx.get_height() // 4

current_frame_attack = 0
current_frame_run = 0
current_frame_die = 0
current_frame_idle = 0
current_frame_jump = 0
current_frame_jump2 = 0
animation_speed = 25

is_attacking = False
is_running = False
is_dying = False
is_idling = False
is_jumping = False
is_jump2 = False
jump_frame = 0
jump_speed = 15
jump_frame_2 = 0
jump_speed2 = 15

current_frame_attack2 = 0
current_frame_run2 = 0
current_frame_die2 = 0
current_frame_idle2 = 0
animation_speed2 = 25
is_attacking2 = False
is_running2 = False
is_dying2 = False
is_idling2 = False
is_hitting2 = False

current_frame_VFX = 0
is_VFX = False

player_x = 0
player_y = y - frame_height + 280

player2_x = x - frame_width
player2_y = y - frame_height + 565

player_speed = 5
player_velocity_x = 0
player_velocity_y = 0

player2_speed = 5
player2_velocityxy = 0

player2_velocity_x = 0

player1_facing_right = True

player1_health = 100
player2_health = 100

map_menu = True
backgrounds =[
    pygame.image.load("background.png"),
    pygame.image.load("back2.png"),
    pygame.image.load("back3.png")
]
selected_background = backgrounds[0]
backgrounds = [pygame.transform.scale(bg,(x,y)) for bg in backgrounds]
back2 = pygame.image.load("back2.png")
back2 = pygame.transform.scale(back2,(x,y))
background_selection = 0

menu_mode = True
button_x = 450
start_button_y = 300
exit_button_y = 400
button_width = 300
button_height = 100
start_button_rect = pygame.Rect(button_x, start_button_y, button_width, button_height)
exit_button_rect = pygame.Rect(button_x, exit_button_y, button_width, button_height)
start_button = pygame.font.Font(None, 36).render("Start", True, (0, 0, 0))
exit_button = pygame.font.Font(None, 36).render("Exit", True, (0,0, 0))

def menuPause():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        menu_mode = True
        button_x = 450
        start_button_y = 300
        exit_button_y = 400
        button_width = 300
        button_height = 100
        start_button_rect = pygame.Rect(button_x, start_button_y, button_width, button_height)
        exit_button_rect = pygame.Rect(button_x, exit_button_y, button_width, button_height)
        start_button = pygame.font.Font(None, 36).render("Start", True, (0, 0, 0))
        exit_button = pygame.font.Font(None, 36).render("Exit", True, (0, 0, 0))

JOYSTICK_B_BUTTON = 1
JOYSTICK_A_BUTTON = 2
lose_font = pygame.font.Font(None, 36)

pygame.joystick.init()
if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

def draw_health_bars():
    pygame.draw.rect(screen, (255, 0, 0), (x - 220, 10, player1_health * 2, 20))
    pygame.draw.rect(screen, (0, 0, 0), (x - 220, 10, 200, 20), 2)
    pygame.draw.rect(screen, (255, 0, 0), (20, 10, player2_health * 2, 20))
    pygame.draw.rect(screen, (0, 0, 0), (20, 10, 200, 20), 2)

def map_menu():
    mape = pygame.font.Font(None,36)
    texte = mape.render("choose your map ",True,WHITE,BLACK)
    textrect = texte.get_rect()
    textrect.center(x // 2,y // 2)

def collision():
    ok = False
    if (player2_x - player_x <= 80) or (player2_x - player_x <= 80):
        ok = True
    return ok

run = True
jump_height = 20
jump_height2 = 20
player_two_win = False

victory_sound_channel = pygame.mixer.Channel(1)

vfx_x = 0
vfx_y = 0
game_over = False
player_one_win_sound_played = False
player_two_win_sound_played = False
seleted_map = 0
game_started = False

def process_player_animations():
    global current_frame_attack, current_frame_run, current_frame_die, current_frame_idle, current_frame_jump, current_frame_jump2
    global is_attacking, is_running, is_dying, is_idling, is_jumping, is_jump2, jump_frame, jump_speed, jump_frame_2, jump_speed2
    global player_velocity_y, player_y

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        is_running = True
        player_velocity_x = -player_speed
    elif keys[pygame.K_d]:
        is_running = True
        player_velocity_x = player_speed
    else:
        is_running = False
        player_velocity_x = 0

    if keys[pygame.K_w] and not is_jumping:
        player_velocity_y = -jump_speed
        is_jumping = True

    player_y += player_velocity_y
    player_y = min(player_y, y - frame_height + 280)
    if player_y >= y - frame_height + 280:
        player_velocity_y = 0
        is_jumping = False

    if is_attacking:
        current_frame_attack = (current_frame_attack + 1) % 6
    elif is_running:
        current_frame_run = (current_frame_run + 1) % 8
    elif is_dying:
        current_frame_die = (current_frame_die + 1) % 6
    elif is_jumping:
        current_frame_jump = (current_frame_jump + 1) % 2
    else:
        current_frame_idle = (current_frame_idle + 1) % 8

def process_player2_animations():
    global current_frame_attack2, current_frame_run2, current_frame_die2, current_frame_idle2
    global is_attacking2, is_running2, is_dying2, is_idling2
    global player2_velocity_x, player2_velocity_y, player2_x, player2_y

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        is_running2 = True
        player2_velocity_x = -player2_speed
    elif keys[pygame.K_RIGHT]:
        is_running2 = True
        player2_velocity_x = player2_speed
    else:
        is_running2 = False
        player2_velocity_x = 0

    if keys[pygame.K_UP] and not is_jumping:
        player2_velocity_y = -jump_speed2
        is_jumping = True

    player2_x += player2_velocity_x
    player2_x = min(player2_x, x - frame_width)
    if player2_x >= x - frame_width:
        player2_velocity_x = 0

    if is_attacking2:
        current_frame_attack2 = (current_frame_attack2 + 1) % 6
    elif is_running2:
        current_frame_run2 = (current_frame_run2 + 1) % 8
    elif is_dying2:
        current_frame_die2 = (current_frame_die2 + 1) % 6
    elif is_jumping:
        current_frame_jump2 = (current_frame_jump2 + 1) % 2
    else:
        current_frame_idle2 = (current_frame_idle2 + 1) % 8

def play_animation():
    if is_attacking:
        screen.blit(image, (player_x, player_y), (current_frame_attack * frame_width, 0, frame_width, frame_height))
    elif is_running:
        screen.blit(image2, (player_x, player_y), (current_frame_run * frame_width2, 0, frame_width2, frame_height2))
    elif is_dying:
        screen.blit(image3, (player_x, player_y), (current_frame_die * frame_width3, 0, frame_width3, frame_height3))
    elif is_jumping:
        screen.blit(image_jump, (player_x, player_y), (current_frame_jump * frame_widthJump, 0, frame_widthJump, frame_heightJump))
    else:
        screen.blit(image4, (player_x, player_y), (current_frame_idle * frame_width4, 0, frame_width4, frame_height4))

def play_animation2():
    if is_attacking2:
        screen.blit(image7, (player2_x, player2_y), (current_frame_attack2 * frame_width7, 0, frame_width7, frame_height7))
    elif is_running2:
        screen.blit(image6, (player2_x, player2_y), (current_frame_run2 * frame_width6, 0, frame_width6, frame_height6))
    elif is_dying2:
        screen.blit(image8, (player2_x, player2_y), (current_frame_die2 * frame_width8, 0, frame_width8, frame_height8))
    elif is_jumping:
        screen.blit(image_jump, (player2_x, player2_y), (current_frame_jump * frame_widthJump, 0, frame_widthJump, frame_heightJump))
    else:
        screen.blit(image5, (player2_x, player2_y), (current_frame_idle2 * frame_width5, 0, frame_width5, frame_height5))

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            elif event.key == pygame.K_SPACE:
                is_attacking = True
            elif event.key == pygame.K_RETURN:
                is_attacking2 = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                is_attacking = False
            elif event.key == pygame.K_RETURN:
                is_attacking2 = False
        elif event.type == timer_event:
            current_time -= 1
            if current_time == 0:
                run = False

    screen.fill((255, 255, 255))
    screen.blit(selected_background, (0, 0))

    process_player_animations()
    process_player2_animations()

    play_animation()
    play_animation2()
    draw_health_bars()

    pygame.display.flip()

pygame.quit()
sys.exit()

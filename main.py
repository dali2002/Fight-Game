import pygame
import pygame.mixer
import sys
#import math
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
#playerTwoWins.play()
#playerOneWin.play()
menuBack = pygame.image.load("back.png")
firstWin = pygame.image.load("wins/1Win.png")
screen = pygame.display.set_mode((x, y))
pygame.display.set_caption("Animation Example")

# Load the image containing 6 frames in a single row for the attack animation
image = pygame.image.load("s1/Attack1.png")
image = pygame.transform.scale(image, (1500, 800))

# Load the image containing 8 frames in a single row for the run animation
image2 = pygame.image.load("s1/Run.png")
image2 = pygame.transform.scale(image2, (2000, 800))

# Load the image containing 6 frames in a single row for the die animation
image3 = pygame.image.load("s1/Die.png")
image3 = pygame.transform.scale(image3, (2000, 800))

# Load the image containing 8 frames in a single row for the idle animation
image4 = pygame.image.load("s1/Idle.png")
image4 = pygame.transform.scale(image4, (2000, 800))

image_jump = pygame.image.load("s1/Run.png")
image_jump = pygame.transform.scale(image_jump, (2000, 800))

image5 = pygame.image.load("s2/Idle.png")
image5 = pygame.transform.scale(image5, (200, 200))
image5_left = pygame.transform.flip(image5, True, False)

image6 = pygame.image.load("s2/Run.png")
image6 = pygame.transform.scale(image6, (2000, 200))

# Adjusted to the correct sprite size
image6_left = pygame.transform.flip(image6, True, False)

image7 = pygame.image.load("s2/Hit.png")
image7 = pygame.transform.scale(image7, (2000, 200))
image7_left = pygame.transform.flip(image7, True, False)

image8 = pygame.image.load("s2/Die.png")
image8 = pygame.transform.scale(image8, (500, 200))
image8_left = pygame.transform.flip(image8, True, False)

background = pygame.image.load("s1/backIM.png")
background = pygame.transform.scale(background, (x, y))

#VFX
font_size = 36
vfx = pygame.image.load("VFX_Effects/VFX.jpg")
fontTime = pygame.font.Font(None,font_size)
timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event,1000)
current_time = starter_time

images = {
    'first': pygame.image.load("FX/pillar/pillar light 1.png"),
    #'dimentsion': (800,600),
    'second': pygame.image.load("FX/pillar/pillar light 2.png"),
    'third': pygame.image.load("FX/pillar/pillar light 3.png"),
    "fourth" : pygame.image.load("FX/pillar/pillar light 4.png"),
    "fifth" : pygame.image.load("FX/pillar/pillar light 5.png")
}
#WHITE = (255,255,255)
#BLACK = (0,0,0)

vfx_frame_width = vfx.get_width() // 4
vfx_frame_height = vfx.get_height() // 4

current_vfx_frame = 0
isVFX = False

#menu_texts



# Calculate the width and height of each frame for all animations
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

# Adjusted frame widths for player 2 animations
frame_width5 = image5.get_width() // 1
frame_height5 = image5.get_height()
frame_width6 = image6.get_width() // 8
frame_height6 = image6.get_height() // 1
frame_width7 = image7.get_width() // 8
frame_height7 = image7.get_height()
frame_width8 = image8.get_width() // 4
frame_height8 = image8.get_height()


#VFX_Sprites
frame_heightVFX = vfx.get_width() // 4
frame_widthVFX = vfx.get_height() // 4
# Initialize animation variables
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
is_hitting2 = False  # Added hitting flag for player 2

current_frame_VFX = 0
is_VFX = False


# Player 1 position
player_x = 0
player_y = y - frame_height + 280

# Player 2 position
player2_x = x - frame_width
player2_y = y - frame_height + 565

# Player 1 movement variables
player_speed = 5
player_velocity_x = 0
player_velocity_y = 0

player2_speed = 5
#player2_velocity_x = 0
player2_velocityxy = 0

# Player 2 movement variables

player2_velocity_x = 0

##direction rotate
player1_facing_right = True

# Player health
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
'''def draw_background_selection_menu():
    screen.fill(WHITE)
    title_font = pygame.font.Font(None, 72)
    title_text = title_font.render("Select a Background", True, BLACK)
    screen.blit(title_text, (x // 2 - title_text.get_width() // 2, 50))

    for i, background in enumerate(background_images):
        background_rect = background.get_rect()
        background_rect.topleft = (50, 150 + i * 150)
        if i == background_selection:
            pygame.draw.rect(screen, BLACK, background_rect, 2)
        screen.blit(background, background_rect.topleft)
    pygame.display.flip()'''
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
#loseTEXT
#font = pygame.font.Font(None, 20)
lose_font = pygame.font.Font(None, 36)

#manette_init
pygame.joystick.init()
if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()




##health_bar
def draw_health_bars():
    # Player 1 health bar
    pygame.draw.rect(screen, (255, 0, 0), (x - 220, 10, player1_health * 2, 20))
    pygame.draw.rect(screen, (0, 0, 0), (x - 220, 10, 200, 20), 2)

    # Player 2 health bar
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
jump_height = 20  #
jump_height2 = 20
#game_over = True
player_two_win = False

victory_sound_channel = pygame.mixer.Channel(1)

vfx_x = 0
vfx_y = 0
game_over = False
player_one_win_sound_played = False
player_two_win_sound_played = False
seleted_map = 0
game_started = False
#selected_background = background_images[background_selection]
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    player1_rect = pygame.Rect(player_x, player_y, frame_width, frame_height)
    player2_rect = pygame.Rect(player2_x, player2_y, frame_width5, frame_height5)

    if menu_mode:
        #map_menu()
        # Render the menu buttons
        '''draw_background_selection_menu()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, background in enumerate(background_images):
                    background_rect = background.get_rect()
                    background_rect.topleft = (50, 150 + i * 150)
                    if background_rect.collidepoint(event.pos):
                        background_selection = i
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        background_selection = (background_selection-1)%len(background_images)
                        menu_mode = False
                        #selected_background = background_images[background_selection]
                        game_started = True
                    elif event.key == pygame.K_h:
                        background_selection = (background_selection+1)%len(background_images)
                        menu_mode = False
                        game_started = True'''
        screen.blit(menuBack,(-300,-200))

        pygame.draw.rect(screen, (255, 255, 0), start_button_rect)
        pygame.draw.rect(screen, (255, 255, 0), exit_button_rect)
        screen.blit(start_button, (button_x + 50, start_button_y + 30))
        screen.blit(exit_button, (button_x + 50, exit_button_y + 30))

       #click on start
        mouse_pos = pygame.mouse.get_pos()
        if start_button_rect.collidepoint(mouse_pos):
            if event.type == pygame.MOUSEBUTTONDOWN:
                menu_mode = False
                #pygame.quit()
    else:

       #manette click
        '''screen.blit(selected_background,(0,0))'''

        if pygame.joystick.get_count() > 0:
            if joystick.get_button(JOYSTICK_B_BUTTON):
                if not is_hitting2:
                    is_hitting2 = True
                    playerTwoHitKnife.play()
            #if player1_health
            if (joystick.get_button(JOYSTICK_B_BUTTON)) and collision():
                if player2_health>0:
                    playerTwoHitKnife.play()
                    player2_health -= 5
                    playerOneDamageTake.play()
                    if player2_health<=0 and not player_two_win_sound_played:
                        player_two_win_sound_played = True
                        playerTwoWins.play()
                pygame.display.flip()
                pygame.time.delay(animation_speed)
            if joystick.get_button(JOYSTICK_A_BUTTON):
                is_jumping = True
                player_velocity_y = -jump_height


        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            player_velocity_x = player_speed
            is_running = True
            player1_facing_right = True
        elif keys[pygame.K_LEFT]:
            player_velocity_x = -player_speed
            is_running = True
            player1_facing_right = False
        else:
            player_velocity_x = 0
            is_running = False

        if keys[pygame.K_SPACE]:
            if not is_attacking:
                is_attacking = True
                playerOneHitKnife.play()
        if keys[pygame.K_SPACE] and collision():
            if player1_health>0:
                playerOneHitKnife.play()
                player1_health -= 5
                playerTwoDamageTake.play()
                if player1_health<=0 and not player_one_win_sound_played:
                    player_two_win_sound_played = True
                    playerOneWin.play()

                    #screen.blit(firstWin,(0,0))
                pygame.display.flip()
                pygame.time.delay(animation_speed)

        if keys[pygame.K_o] and not is_VFX:
            is_VFX = True
            vfx_x = player_x
            vfx_y = player_y
        if is_VFX:
            current_frame_VFX += 1
            if current_frame_VFX >=4:
                is_VFX = False
                current_frame_VFX= 0
            source_rect_VFX = pygame.Rect(current_frame_VFX * frame_widthVFX , 0 ,frame_widthVFX , frame_heightVFX)
            screen.blit(vfx,(vfx_x,vfx_y),source_rect_VFX)
        player_two_win_sound_played = False

        #INSIDE GAME LOOP

        if player2_health <= 0 and not player_two_win_sound_played: #and not victory_sound_channel.get_busy():
            is_dying = True
            current_frame_die = 2
        if player1_health<=0:
            is_dying2 = True
            current_frame_die2 = 4
            #if player2_health <=  0:
            #playerOneWin.play()
            #else:
            #  pygame.time.delay(3000)
             #  playerOneWin.stop()



        # Jump_logic
        if keys[pygame.K_UP]:
            playerJumpSound.play()
            if not is_jumping:
                is_jumping = True
                player_velocity_y = -jump_height
                current_frame_jump = 1
            source_rect_jump = pygame.Rect(current_frame_jump * frame_widthJump,0,frame_widthJump,0)
            screen.blit(image_jump,(player_x,player_y),source_rect_jump)

        if is_jumping:
            playerJumpSound.set_volume(1)
            player_y += player_velocity_y
            player_velocity_y += 2  # Gravity
            current_frame_jump = 1


            if player_y >= y - frame_height + 280:
                is_jumping = False
                player_y = y - frame_height + 280
                player_velocity_y = 0


       #manette
        if pygame.joystick.get_count() > 0:
            joystick = pygame.joystick.Joystick(0)
            joystick.init()
            axis_x = joystick.get_axis(0)
            if axis_x > 0.1:
                player2_velocity_x = player2_speed
                is_running2 = True
            elif axis_x < -0.1:
                player2_velocity_x = -player2_speed
                is_running2 = True
            else:
                player2_velocity_x = 0
                is_running2 = False

            if event.type == timer_event:
                if current_time > 0:
                    current_time -= 1
            timeText = fontTime.render(f"Time Left: {current_time // 60:02}:{current_time % 60:02}", True, (0, 0, 0))
            screen.blit(timeText, (0, 10))

        player_x += player_velocity_x
        player2_x += player2_velocity_x

        player_x = max(0, player_x)
        player_x = min(x - frame_width, player_x)
        player2_x = max(0, player2_x)
        player2_x = min(x - frame_width, player2_x)

        screen.blit(background, (0, 0))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            screen.blit(back2, (0, 0))


        if isVFX:
            source_rect_vfx = pygame.Rect(current_frame_VFX * frame_widthVFX , 0 , frame_widthVFX,frame_heightVFX)
            if keys[pygame.K_p]:
                current_frame_VFX = 2
                screen.blit(vfx,(player_x,player_y),source_rect_vfx)
        if is_attacking:
            current_frame_attack += 1
            if current_frame_attack >= 6:
                is_attacking = False
                current_frame_attack = 0

            source_rect_attack = pygame.Rect(current_frame_attack * frame_width, 0, frame_width, frame_height)
            if player1_facing_right:
                screen.blit(image, (player_x, player_y), source_rect_attack)
            else:
                flipped_image = pygame.transform.flip(image, True, False)
                screen.blit(flipped_image, (player_x, player_y), source_rect_attack)
        elif is_running:
            current_frame_run += 1
            if current_frame_run >= 8:
                current_frame_run = 0

            if player_velocity_x > 0:
                source_rect_run = pygame.Rect(current_frame_run * frame_width2, 0, frame_width2, frame_height2)
                screen.blit(image2, (player_x, player_y), source_rect_run)
            else:
                source_rect_run = pygame.Rect(current_frame_run * frame_width2, 0, frame_width2, frame_height2)
                screen.blit(image2, (player_x, player_y), source_rect_run)
        elif is_dying:
            current_frame_die += 1
            if current_frame_die >= 4:
                is_dying = False
                current_frame_die = 0

            source_rect_die = pygame.Rect(current_frame_die * frame_width3, 0, frame_width3, frame_height3)
            screen.blit(image3, (player_x, player_y), source_rect_die)
        else:
            current_frame_idle += 1
            if current_frame_idle >= 1:
                current_frame_idle = 0

            if player_velocity_x > 0:
                source_rect_idle = pygame.Rect(0, 0, frame_width4, frame_height4)
                screen.blit(image4, (player_x, player_y), source_rect_idle)
            else:
                source_rect_idle = pygame.Rect(0, 0, frame_width4, frame_height4)
                screen.blit(image4, (player_x, player_y), source_rect_idle)

        # Player 2 animations
        if is_hitting2:
            current_frame_attack2 += 1
            if current_frame_attack2 >= 8:
                is_hitting2 = False
                current_frame_attack2 = 0

            source_rect_attack2 = pygame.Rect(current_frame_attack2 * frame_width7, 0, frame_width7, frame_height7)
            if player2_velocity_x > 0:
                screen.blit(image7, (player2_x, player2_y), source_rect_attack2)
            else:
                flipped_image7 = pygame.transform.flip(image7, True, False)
                screen.blit(flipped_image7, (player2_x, player2_y), source_rect_attack2)
        elif is_running2:
            current_frame_run2 += 1
            if current_frame_run2 >= 8:
                current_frame_run2 = 0

            source_rect_run2 = pygame.Rect(current_frame_run2 * frame_width6, 0, frame_width6, frame_height6)
            if player2_velocity_x > 0:
                screen.blit(image6, (player2_x, player2_y), source_rect_run2)
            else:
                source_rect_run2 = pygame.Rect(current_frame_run2 * frame_width6, 0, frame_width6, frame_height6)
                screen.blit(image6_left, (player2_x, player2_y), source_rect_run2)
        elif is_dying2:
            current_frame_die2 += 1
            if current_frame_die2 >= 4:
                is_dying2 = False
                current_frame_die2 = 0

            source_rect_die2 = pygame.Rect(current_frame_die2 * frame_width8, 0, frame_width8, frame_height8)
            if player2_velocity_x > 0:
                screen.blit(image8, (player2_x, player2_y), source_rect_die2)
            else:
                flipped_image8 = pygame.transform.flip(image8, True, False)
                screen.blit(flipped_image8, (player2_x, player2_y), source_rect_die2)
        else:
            current_frame_idle2 += 1
            if current_frame_idle2 >= 1:
                current_frame_idle2 = 0

            if player2_velocity_x > 0:
                source_rect_idle2 = pygame.Rect(0, 0, frame_width5, frame_height5)
                screen.blit(image5, (player2_x, player2_y), source_rect_idle2)
            else:
                source_rect_idle2 = pygame.Rect(0, 0, frame_width5, frame_height5)
                screen.blit(image5_left, (player2_x, player2_y), source_rect_idle2)

            #run = False


        # Draw health bars for both players
        draw_health_bars()

        #pygame.display.flip()
    pygame.display.flip()
    pygame.time.delay(animation_speed)
    if current_time<=0:
        run = False

    menuPause()
pygame.quit()
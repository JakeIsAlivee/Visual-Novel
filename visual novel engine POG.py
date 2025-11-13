import pygame
import time
import sys
import os
import random
#   pygame.draw
#   pygame.display
#   pygame.event
#   pygame.mask
#   pygame.sprite
#   pygame.Surface
#   pygame.time


#pygame.quit()

#pygame.image.load()
#pygame.image.save()

#pygame.mask.Mask()

#pygame.sprite.Sprite()

#pygame.Surface()



scriptdirfolder = os.path.dirname(os.path.realpath(__file__))

if scriptdirfolder.find('\\') != -1:
    slash = '\\'
else:
    slash = '/'



black = (0,0,0)
white = (255,255,255)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)



pygame.init()

player_desktop = pygame.display.get_desktop_sizes()
player_desktop = player_desktop[0]

resolution = (1920, 1010)

if resolution > player_desktop:
    resolution = (1600, 900)
if resolution > player_desktop:
    resolution = (1280, 720)
if resolution > player_desktop:
    resolution = (800, 600)
if resolution > player_desktop:
    print('Your desktop resolution is too low. This game cant run on your computer with theese settings.')
    time.sleep(60)
    sys.exit()

icon = pygame.image.load(scriptdirfolder+slash+'smileyface.png')

pygame.display.set_mode(resolution)

pygame.display.set_icon(icon)

pygame.display.set_caption('There will be a visual novel soon...') #why am i doing an engine yourself when i can use renpy or some shit? I WANT TO CREATE A GAME.

surfacewindow = pygame.display.get_surface()
finalresolution = pygame.display.get_window_size()

fontsize = finalresolution[0] // 40

sceneshown = 'blackscreen'

exitdialogues = {
    1: 'Пока-пока',
    2: 'Уходишь так рано?',
    3: 'Приятного времяпрепровождения',
    4: 'Прощай',
    5: 'Увидимся',
}

debugmode = False


def mainmenu_scene():
    #loading meinmenu
    surfacewindow.fill(white)
    #surfacewindow.blit() draw a bg screen later
    sceneshown = 'mainmenu'

    mainbutton1_surface = pygame.font.SysFont('couriernew', fontsize).render('Начать',True,black)
    mainbutton1_width = mainbutton1_surface.get_rect().width
    mainbutton1_height = mainbutton1_surface.get_rect().height

    mainbutton1_xpoints = (finalresolution[0]+mainbutton1_width-finalresolution[0],finalresolution[0]+mainbutton1_width-finalresolution[0]+mainbutton1_width)
    mainbutton1_ypoints = (finalresolution[1]-mainbutton1_height*5,finalresolution[1]-mainbutton1_height*5+mainbutton1_height)
    # thats hitboxes for button ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    surfacewindow.blit(mainbutton1_surface,(mainbutton1_xpoints[0],mainbutton1_ypoints[0]))

    if debugmode == True:
        pygame.draw.lines(surfacewindow,red,False,[(mainbutton1_xpoints[0],mainbutton1_ypoints[1]),(mainbutton1_xpoints[1],mainbutton1_ypoints[1]),(mainbutton1_xpoints[1],mainbutton1_ypoints[0]),(mainbutton1_xpoints[0],mainbutton1_ypoints[0]),(mainbutton1_xpoints[0],mainbutton1_ypoints[1])])

    pygame.display.update()
    
    while True:

        for event in pygame.event.get():
            if debugmode == True:
                print(event)

            if event.type == pygame.MOUSEBUTTONUP:
                clickcords = event.pos

                if clickcords[0] > mainbutton1_xpoints[0] and clickcords[0] < mainbutton1_xpoints[1] and clickcords[1] > mainbutton1_ypoints[0] and clickcords[1] < mainbutton1_ypoints[1]:
                    return
                else:
                    pass

            if event.type == pygame.QUIT: 
                return(True)
            
        pygame.time.Clock().tick(60)

    






# важно
# у event'ов есть type, key, pos




if mainmenu_scene() == True:
    sceneshown = 'exitscreen'
    clock = 0
    randomizedexitmessage = exitdialogues[random.randint(1,5)]
    while clock != 200:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        animationsurface = pygame.Surface(finalresolution,pygame.SRCALPHA)
        animationsurface.fill((0,0,0,2))

        exitmessage = pygame.font.SysFont('couriernew', fontsize*2).render(randomizedexitmessage,True,(255,255,255,2))
        centretext = exitmessage.get_rect(center=(finalresolution[0]//2, finalresolution[1]//2))
        surfacewindow.blit(exitmessage, centretext)

        surfacewindow.blit(animationsurface, (0,0))
        pygame.display.update()
        pygame.time.Clock().tick(500)
        clock += 1

    sys.exit()

else:
    pass

clock = 0
animationsurface = pygame.Surface(finalresolution,pygame.SRCALPHA)
while clock != 500:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    animationsurface.fill((0,0,0,1))

    surfacewindow.blit(animationsurface, (0,0))
    pygame.display.update()
    pygame.time.Clock().tick(120)
    clock += 1

animationsurface = pygame.Surface(finalresolution,pygame.SRCALPHA)
while clock > -255:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    animationsurface.fill((255,255,255,1))

    therewillbesomethingsoon = pygame.font.SysFont('couriernew', fontsize*2).render('Скоро тут что-то будет',True,(0,0,0,1))
    centretext = therewillbesomethingsoon.get_rect(center=(finalresolution[0]//2, finalresolution[1]//2))

    surfacewindow.blit(therewillbesomethingsoon,centretext)

    surfacewindow.blit(animationsurface, (0,0))
    pygame.display.update()
    pygame.time.Clock().tick(120)
    clock -= 1


sys.exit()


    
    

    


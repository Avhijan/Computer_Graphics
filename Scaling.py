import pygame

pygame.init()

screen=pygame.display.set_mode((600,400))
pygame.display.set_caption("scaling of line")

run=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run= False
    screen.fill ((255,255,255))

    xc=300
    yc=200
    r=50
    pygame.draw.circle(screen, (0,150,255),(xc,yc),r,width=2)


    #scaling
    s=2
    r*=s
    pygame.draw.circle(screen,(0,0,0),(xc,yc),r,width=2)


    pygame.display.flip()
    pygame.time.Clock().tick(60)
pygame.quit()
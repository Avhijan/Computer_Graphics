import pygame

pygame.init()

screen=pygame.display.set_mode((600,400))
pygame.display.set_caption("translation of line")

run=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run= False
    screen.fill ((255,255,255))
    x1=50
    y1=50
    x2=150
    y2=150
    pygame.draw.line(screen,(0,150,255),(x1,y1),(x2,y2),5)

    #translation
    tx=100
    ty=200
    x1+=tx
    x2+=tx
    y1+=ty
    y2+=ty

    pygame.draw.line(screen,(0,0,0),(x1,y1),(x2,y2),5)
    pygame.display.flip()
    pygame.time.Clock().tick(60)
pygame.quit()
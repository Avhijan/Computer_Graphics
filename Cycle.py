import pygame

pygame.init()

x1,y1=50,300
x2,y2=130,320
x3,y3=200,235
x4,y4=100,250
x5,y5=230,300
x6,y6=195,220
x7,y7=213, 215
x8,y8=177, 230
cycle_colour=(255, 99, 71)


screen=pygame.display.set_mode((600,400))
pygame.display.set_caption("Moving Bicycle")

running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

    screen.fill((255,255,255))
    

    #cycle body
    pygame.draw.polygon(screen,cycle_colour,[(x1,y1),(x2,y2),(x3,y3),(x4,y4)],5) 
    pygame.draw.line(screen,cycle_colour,(x2,y2),(x4,y4),width=4)
    pygame.draw.line(screen,cycle_colour,(x6,y6),(x5,y5),4)

    #cycle handle
    pygame.draw.line(screen,cycle_colour,(x7, y7),(x8, y8),4)



    pygame.draw.circle(screen,(0,0,0),(x1,y1),40,width=8)
    pygame.draw.circle(screen,(0,0,0),(x5,y5),40,width=8)
    x1+=1
    x2+=1
    x3+=1
    x4+=1
    x5+=1
    x6+=1
    x7+=1
    x8+=1

    if x1>600:
        x1,y1=50,300
        x2,y2=130,320
        x3,y3=200,235
        x4,y4=100,250
        x5,y5=230,300
        x6,y6=195,220
        x7,y7=213, 215
        x8,y8=177, 230
        
    pygame.display.flip()
    pygame.time.Clock().tick(60)
pygame.quit()
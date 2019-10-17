import pygame
import os
x = 30
y = 30
print ('How fast do you want to go? (1-10) ')
z=int(input())
score = 0
_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                        
        pressed = pygame.key.get_pressed()
        
        
        screen.fill((255, 255, 255))
        
        screen.blit(get_image('ball.png'), (x, y))


        
        if score != 4:
            if y >= 260 or y <= 0 or x >= 360 or x <= 0 :
                score = score + 1
                x = 100
                y = 100
                print (score)
            if pressed[pygame.K_UP]:
                y = y-z
            if pressed[pygame.K_DOWN]:
                y = y+z
            if pressed[pygame.K_LEFT]:
                x = x-z
            if pressed[pygame.K_RIGHT]:
                x = x+z
        else :
            print ("You're out of lives!")
            done = True
        pygame.display.flip()
        clock.tick(60)
        

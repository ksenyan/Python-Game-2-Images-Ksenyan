import pygame
import os
x = 30
y = 30
is_blue = False
print ('How fast do you want to go? (1-10) ')
z=int(input()) #user chooses speed
print ('Move with arrow keys and try pressing space :)')
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
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue #pressing space changes variable to true/false
        
                        
        pressed = pygame.key.get_pressed()
        screen.fill((255, 255, 255))
        
        if is_blue :
            screen.blit(get_image('ballblue.png'), (x, y))
                    #I'm proud of this - the image switches 
        else :
            screen.blit(get_image('ball.png'), (x, y))

            
        if score != 4: #until we get to 4 lives
            if y >= 260 or y <= 0 or x >= 360 or x <= 0 : #if we hit the edge
                score = score + 1
                x = 100             #just goes to the middle
                y = 100
                print (score)   
            if pressed[pygame.K_UP]: #controls!!
                y = y-z
            if pressed[pygame.K_DOWN]:
                y = y+z
            if pressed[pygame.K_LEFT]:
                x = x-z
            if pressed[pygame.K_RIGHT]:
                x = x+z
        else :                  #once we run out of lives
            print ("You're out of lives!")
            done = True         #stops everything
        pygame.display.flip()
        clock.tick(60)
        

import pygame
import os
x = 30
y = 30
z=3 #this is like speedx and speedy
v = 3
_image_library = {}
def get_image(path): #import the ba;;
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

pygame.mixer.music.load('kahoot.mp3') 
pygame.mixer.music.play(-1)                 #play kahoot song forever
woohoo = pygame.mixer.Sound('woohoo.wav')       #load up the woohoo as a sound

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        screen.fill((255, 255, 255))
        screen.blit(get_image('ball.png'), (x, y)) #the image is always at coordinates x, y, which change.
        
        x = x + z
        y = y + v
        

        if (y >= 250 and x >= 350) or (y >= 250 and x <= 5) or (y <= 5 and x <= 5) or (y<= 5 and x >= 350) :
            print ("yay")
            woohoo.play() #plays the woohoo once if the ball hits a corner
            
        if y >= 260 or y <= 0 : #if we hit the edge
            v = v*(-1) #change direction
        if x >= 360 or x <= 0 :
            z = z*(-1)
        
        pygame.display.flip()
        clock.tick(60)
        

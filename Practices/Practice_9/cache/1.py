import pygame
import os 
pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
_image_library = {}
played = False
clock = pygame.time.Clock()
def load_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonalized_path)
                _image_library[path] = image
        return image

_sound_library = {}

def play_sound(path):
        global _sound_library
        sound = _sound_library.get(path)
        if sound == None:
                canonalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                sound = pygame.mixer.Sound(canonalized_path)
                _sound_library[path] = sound
        sound.play()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        played = not played

        screen.fill((255, 255, 255))
        if not played:
                play_sound('soft-hitclap.wav')
        clock.tick(9)
        pygame.display.flip()
import pygame
import datetime

class MickeyClock:
    def __init__(self, screen, center, images, offsets=None):
        """
        screen: pygame display surface
        center: tuple (x, y) for clock center
        images: dict {'right': pygame.Surface, 'left': pygame.Surface, 'background': pygame.Surface}
        offsets: dict {'right': (dx, dy), 'left': (dx, dy)} optional, for pivot adjustments
        """
        self.screen = screen
        self.center = center
        self.bg = images['background']
        self.right_hand = images['right']
        self.left_hand = images['left']
        self.offsets = offsets or {'right': (0,0), 'left': (0,0)}

    def blitRotate(self, surf, image, pos, originPos, angle):
        """
        Rotate an image around a pivot point (originPos) and blit to the surface.
        """
        # offset from pivot to center
        image_rect = image.get_rect(topleft=(pos[0]-originPos[0], pos[1]-originPos[1]))
        offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center

        # rotated offset
        rotated_offset = offset_center_to_pivot.rotate(-angle)

        # rotated image center
        rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

        # rotate image
        rotated_image = pygame.transform.rotate(image, angle)
        rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)

        # blit
        surf.blit(rotated_image, rotated_image_rect)

    def update(self):
        # draw background
        self.screen.blit(self.bg, (0,0))

        # get local time
        now = datetime.datetime.now()
        minutes = now.minute
        seconds = now.second

        # angles (clockwise)
        minute_angle = -(minutes + seconds / 60) * 6
        second_angle = -seconds * 6

        # draw hands using blitRotate
        # apply offsets if pivot is off-center
        right_offset = self.offsets.get('right', (0,0))
        left_offset = self.offsets.get('left', (0,0))

        # for pivot, we assume the pivot is at the "center" of the hand image plus optional offset
        right_origin = (self.right_hand.get_width()/2 + right_offset[0],
                        self.right_hand.get_height()/2 + right_offset[1])
        left_origin = (self.left_hand.get_width()/2 + left_offset[0],
                       self.left_hand.get_height()/2 + left_offset[1])

        self.blitRotate(self.screen, self.right_hand, self.center, right_origin, second_angle)
        self.blitRotate(self.screen, self.left_hand, self.center, left_origin, minute_angle)
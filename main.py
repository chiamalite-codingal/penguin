import pygame
pygame.init()
width, height = 500,500
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Add image")
#add image
penguin_image = pygame.transform.scale(
    pygame.image.load('penguin.png').convert_alpha(),
    (200,200)
)
#image position
penguin_position = penguin_image.get_rect(
    center = (width//2,height//2)
)
def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(penguin_image,penguin_position)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
if __name__ == '__main__':
    game_loop()
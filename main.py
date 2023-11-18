import pygame
import sys

# Initialize Pygame
pygame.init()

width= 800
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Thanksgiving Parade Animation")

# Turkey
turkey_x = 100
turkey_y = 100
turkey_width = 200
turkey_height = 200
turkey_image = pygame.image.load("turkey.gif")
resized_turkey_image = pygame.transform.scale(turkey_image, (turkey_width, turkey_height))

# Pie
pie_x = 100
pie_y = 100
pie_width = 200
pie_height = 200
pie_image = pygame.image.load("pie.gif")
resized_pie_image = pygame.transform.scale(pie_image, (pie_width, pie_height))

# Apple pie
apple_pie_x = 100
apple_pie_y = 100
apple_pie_width = 200
apple_pie_height = 200
apple_pie_image = pygame.image.load("apple_pie.png")
resized_apple_pie_image = pygame.transform.scale(apple_pie_image, (apple_pie_width, apple_pie_height))

# Hat
hat_x = 100
hat_y = 100
hat_width = 200
hat_height = 200
hat_image = pygame.image.load("hat.png")
resized_hat_image = pygame.transform.scale(hat_image, (hat_width, hat_height))

clock = pygame.time.Clock()

running = True
while running:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
    turkey_x -= 5
    pie_x -= 2.5
    apple_pie_x -= 7
    hat_x -= 11
  if keys[pygame.K_RIGHT]:
    turkey_x += 5
    pie_x += 2.5
    apple_pie_x += 7
    hat_x += 11
  if keys[pygame.K_UP]:
    turkey_y -= 5
    pie_y -= 2.5
    apple_pie_y -= 7
    hat_y -= 11
  if keys[pygame.K_DOWN]:
    turkey_y += 5
    pie_y += 2.5
    apple_pie_y += 7
    hat_y += 11

  screen.fill((255, 255, 255))



  screen.blit(resized_turkey_image, (turkey_x, turkey_y))
  screen.blit(resized_pie_image, (pie_x, pie_y))
  screen.blit(resized_apple_pie_image, (apple_pie_x, apple_pie_y))
  screen.blit(resized_hat_image, (hat_x, hat_y))
  
  pygame.display.flip()

  clock.tick(60)
pygame.quit()
sys.exit()
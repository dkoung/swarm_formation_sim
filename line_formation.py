# line formation simulation

import pygame
import random
from line_formation_robot import LFRobot
from line_formation_functions import *

pygame.init()  # initialize pygame

# for display, window origin is at left up corner
screen_size = (1200, 900)  # width and height
background_color = (0, 0, 0)  # black background
robot_color = (255, 255, 255)  # white robot
robot_size = 5  # robot modeled as dot, number of pixels in radius

# set up the simulation window and surface object
icon = pygame.image.load('geometry_art.jpg')
pygame.display.set_icon(icon)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Line Formation Simulation')

# for physics, origin is at left bottom corner, starting (0, 0)
# it's more natural to do the calculation in right hand coordiante system
# the continuous, physical world for the robots
world_size = (100.0, 100.0 * screen_size[1]/screen_size[0])

# variables to configure the simulation
robot_quantity = 30
# coefficient to resize the robot distribution, but always keep close to center
distrib_coef = 0.5
const_vel = 2  # all moving robots are moving at a constant speed


# instantiate the robot swarm
robot = []  # container for all robots, index is also the IDs
for i in range(robot_quantity):
    # random position, away from the window edges
    pos_temp = (((random.random()-0.5)*distrib_coef+0.5) * world_size[0],
                ((random.random()-0.5)*distrib_coef+0.5) * world_size[1])
    vel_temp = const_vel
    ori_temp = random.random() * 2*math.pi  # random in (0, 2*pi)

# the loop
sim_exit = False  # simulation exit flag
sim_pause = False  # simulation pause flag
timer_last = pygame.time.get_ticks()  # return number of milliseconds after pygame.init()
timer_now = timer_last  # initialize it with timer_last
while not sim_exit:
    # exit the program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sim_exit = True  # exit with the close window button
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                sim_pause = not sim_pause  # reverse the pause flag
            if (event.key == pygame.K_ESCAPE) or (event.key == pygame.K_q):
                sim_exit = True  # exit with ESC key or Q key

    pygame.display.update()


pygame.quit()



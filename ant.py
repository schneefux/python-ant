#!/usr/bin/python

#
#    10th October 2013
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import pygame
from pygame.locals import *

# init pygame
pygame.init()

# the main game
def game_loop():
    # set properties
    displaysize = (90, 90)
    display = pygame.display.set_mode(displaysize)

    # get a pixel array
    pxarr = pygame.PixelArray(display)

    display.fill((255, 255, 255))

    # init the ant
    antdir = 0
    antx = displaysize[0] // 2
    anty = displaysize[1] // 2

    loop = True

    # start the main loop
    while loop:
        # check window events
        for event in pygame.event.get():
            if event.type == QUIT:
                loop = False

        # check if the ant is inside the window
        if antx > 0 and anty > 0 and antx < displaysize[0] and anty < displaysize[1]:
            # operate
            if pxarr[antx][anty] == 0:
                # if white, set black and turn right
                pxarr[antx][anty] = (255, 255, 255)
                antdir += 1
                if antdir == 4:
                    antdir = 0
            else:
                # if black, set the pixel white and turn left
                pxarr[antx][anty] = (0, 0, 0)
                antdir -= 1
                if antdir == -1:
                    antdir = 3

            # move the ant in its direction
            if antdir % 2 == 0:
                antx += antdir - 1
            else:
                anty += antdir - 2

        # update the display
        pygame.display.update()

if __name__ == '__main__':
    game_loop()

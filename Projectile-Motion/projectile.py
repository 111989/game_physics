""" Projectile Motion in 2D, with zero air resistance and 
    constant acceleration in the vertical direction """

import math
import pygame

# Creates a ball object with location, 
# size, appearance & speed attributes.   
class Ball:
    def __init__(self, display_width: int, display_height: int, 
        ball_radius: float, ball_colour: tuple, ball_speed: float):

        self.ball_radius = ball_radius
        self.ball_colour = ball_colour
        self.ball_speed = ball_speed
        self.x = display_width // 2
        self.y = (display_height - 1) - self.ball_radius
        self.center = (self.x, self.y)



def main():

    # initialize pygame display
    # initialize ball features
    # initialize projectile inputs
    # generate ball
    DISPLAY_WIDTH = 1250
    DISPLAY_HEIGHT = 500
    display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    pygame.display.set_caption("Projectile Motion")
    BALL_RADIUS = 7.5
    BALL_COLOUR = (50, 50, 50)
    BALL_SPEED = 0.0175
    ground = (DISPLAY_HEIGHT - 1) - BALL_RADIUS
    hyp_factor = 0.1
    acceleration = 4.9

    ball = Ball(DISPLAY_WIDTH, DISPLAY_HEIGHT, BALL_RADIUS, BALL_COLOUR, BALL_SPEED)

    # run the projectile
    time = 0
    launch = False
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if launch and ground < ball.y: 
                ball.y = ground
                time = 0
                launch = False

            # Set initial coordinates and
            # compute projectile parameters. 
            if not launch and pygame.mouse.get_pressed()[0]:

                (x0, y0) = ball.center 
                x1, y1 = pygame.mouse.get_pos()
                x, y = x0-x1, y0-y1
                hypotenuse = hyp_factor * math.sqrt((y)**2 + (x)**2)     
                try: angle = math.atan((y)/(x))
                except: angle = math.pi / 2
                if x < 0 and y < 0: angle = 2 * math.pi - angle
                elif x < 0 and y > 0: angle = abs(angle)
                elif x > 0 and y < 0: angle = math.pi + abs(angle)    
                elif x > 0 and y > 0: angle = math.pi - angle 
                launch = True
        
        # Update ball coordinates to those 
        # dictated by projectile motion at time t.
        if launch and ball.y <= ground: 

            time += ball.ball_speed
            velocity_x = math.cos(angle) * hypotenuse
            velocity_y = math.sin(angle) * hypotenuse
            displacement_x = x0 + velocity_x * time
            displacement_y = y0 - ((velocity_y * time) + ((-acceleration * (time**2))/2))
            ball.x, ball.y = round(displacement_x), round(displacement_y)

        # update coordinates of ball center
        # fill display
        # draw hypotenuse
        # draw ball
        # update display
        ball.center = (ball.x, ball.y)
        DISPLAY_COLOUR = (175, 175, 225)
        display.fill(DISPLAY_COLOUR)
        HYP_COLOUR = (200, 200, 200)
        HYP_WIDTH = 3
        pygame.draw.line(display, HYP_COLOUR, ball.center, pygame.mouse.get_pos(), HYP_WIDTH)
        pygame.draw.circle(display, ball.ball_colour, ball.center, ball.ball_radius)
        pygame.display.update()

    pygame.quit() 



if __name__ == '__main__':
    main()

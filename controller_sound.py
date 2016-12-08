import pygame

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

# This is a simple class that will help us print to the screen
# It has nothing to do with the joysticks, just outputing the
# information.
class TextPrint:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def print(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, [self.x, self.y])
        self.y += self.line_height
        
    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15
        
    def indent(self):
        self.x += 10
        
    def unindent(self):
        self.x -= 10
    

pygame.init()
 
# Set the width and height of the screen [width,height]
size = [500, 700]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initialize the joysticks
pygame.joystick.init()

# Initialize the audio mixer
pygame.mixer.init()
s1 = pygame.mixer.Sound('tada.wav')
s2 = pygame.mixer.Sound('chimes.wav')
s3 = pygame.mixer.Sound('chord.wav')
s4 = pygame.mixer.Sound('ding.wav')
s5 = pygame.mixer.Sound('Windows Exclamation.wav')
s6 = pygame.mixer.Sound('Windows Default.wav')
s7 = pygame.mixer.Sound('Windows Ding.wav')
s8 = pygame.mixer.Sound('Windows Error.wav')
#s1.play(loops = 0) # play once
    
# Get ready to print
textPrint = TextPrint()

released = True

# -------- Main Program Loop -----------
while done==False:
    # EVENT PROCESSING STEP
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        
        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
        if event.type == pygame.JOYBUTTONDOWN:
            #print("Joystick button pressed.")
            pass
        if event.type == pygame.JOYBUTTONUP:
            #print("Joystick button released.")
            released = True
        
            
 
    # DRAWING STEP
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    textPrint.reset()

    # Get count of joysticks
    joystick_count = pygame.joystick.get_count()

    textPrint.print(screen, "Number of joysticks: {}".format(joystick_count) )
    textPrint.indent()
    
    # For each joystick:
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
    
        textPrint.print(screen, "Joystick {}".format(i) )
        textPrint.indent()
    
        # Get the name from the OS for the controller/joystick
        name = joystick.get_name()
        textPrint.print(screen, "Joystick name: {}".format(name) )
        
        # Usually axis run in pairs, up/down for one, and left/right for
        # the other.
        axes = joystick.get_numaxes()
        textPrint.print(screen, "Number of axes: {}".format(axes) )
        textPrint.indent()
        
        for i in range( axes ):
            axis = joystick.get_axis( i )
            textPrint.print(screen, "Axis {} value: {:>6.3f}".format(i, axis) )
            if i == 0 and axis > 0.5 and released:
              print("Right")
            if i == 0 and axis < -0.5 and released:
              print("Left")
            if i == 1 and axis > 0.5 and released:
              print("Down")
            if i == 1 and axis < -0.5 and released:
              print("Up")
        textPrint.unindent()
            
        buttons = joystick.get_numbuttons()
        textPrint.print(screen, "Number of buttons: {}".format(buttons) )
        textPrint.indent()

        for i in range( buttons ):
            button = joystick.get_button( i )
            textPrint.print(screen, "Button {:>2} value: {}".format(i,button) )
            if i == 0 and button == 1 and released:
              print("A is for Amanda")
              s1.play(loops = 0) # play once
              released = False
            if i == 1 and button == 1 and released:
              print("B is for Brian")
              s2.play(loops = 0)
              released = False
            if i == 2 and button == 1 and released:
              print("X is for Madison")
              s3.play(loops = 0)
              released = False
            if i == 3 and button == 1 and released:
              print("Y is for Julia")
              s4.play(loops = 0)
              released = False
            if i == 4 and button == 1 and released:
              print("L is for Likhi")
              s5.play(loops = 0)
              released = False
            if i == 5 and button == 1 and released:
              print("R is for Stella")
              s6.play(loops = 0)
              released = False
            if i == 6 and button == 1 and released:
              print("Select is for ...Select")
              s7.play(loops = 0)
              released = False
            if i == 7 and button == 1 and released:
              print("Start is for ...Start")
              s8.play(loops = 0)
              released = False
        textPrint.unindent()
            
        # Hat switch. All or nothing for direction, not like joysticks.
        # Value comes back in an array.
        hats = joystick.get_numhats()
        textPrint.print(screen, "Number of hats: {}".format(hats) )
        textPrint.indent()

        for i in range( hats ):
            hat = joystick.get_hat( i )
            textPrint.print(screen, "Hat {} value: {}".format(i, str(hat)) )
        textPrint.unindent()
        
        textPrint.unindent()

    
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 20 frames per second
    clock.tick(20)
    
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit ()
import pyglet
import time

def play_gif(ag_file):
    # pick an animated gif file you have in the working directory
    # ag_file = "moonmoon-omega-desk-slam.gif"
    animation = pyglet.resource.animation(ag_file)
    sprite = pyglet.sprite.Sprite(animation)

    # create a window and set it to the image size
    win = pyglet.window.Window(width=sprite.width, height=sprite.height)

    # set window background color = r, g, b, alpha
    # each value goes from 0.0 to 1.0
    green = 0, 1, 0, 1
    pyglet.gl.glClearColor(*green)

    @win.event
    def on_draw():
        win.clear()
        sprite.draw()

    pyglet.app.run()

def print_dots(n):
    for i in range(n):
        print(".")
        time.sleep(1)

def final_prompt():
    print("Well, I guess that leaves you with only one option...send me a message :) If you're shy, just say hi!")

def prompt_beautiful_person():
    response = input("Hiiii!!! Are you interested in getting to know me? (yes/no): ")

    if (response.lower() == "no"):
        play_gif("moonmoon-omega-desk-slam.gif")
        print("FUCK")
        print_dots(3)
        print("I mean...alright. I understand! Have a good day!")
        exit()
    elif (response.lower() == "yes"):
        play_gif("clapping-hands-pepe-the-frog.gif")
        print("HELL YEAH")
        print_dots(3)
        print("I mean...sure yeah ok....that's cool \U0001F60E")
        final_prompt()
        exit()

prompt_beautiful_person()

# If we get here they said something other than yes or no
print("Did you think I wouldn\'t have proper error checking??? \U0001F621")
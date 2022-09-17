from platform import platform
import pgzrun
HEIGHT = 400
WIDTH = 600

item = Rect((300,250),(25,25))
ivy = 3

item2 = Rect((250,250),(25,25))
i2vy = 2

platform = Rect((WIDTH/2, HEIGHT-50),(250,25))

def item_motion_control(obj,plt,speed): #define new function
    

    obj.y += speed
    if obj.y > HEIGHT:
        obj.y = 0
    if obj.y < 0:
        obj.y = 0
        speed = -speed
    if obj.colliderect(plt):
        speed = -speed # apply reverse
    return speed

def platform_control():
    if keyboard.left:
        platform.x -= 3
    elif keyboard.right:
        platform.x += 3
    
    


def draw():
    screen.fill('white')
    screen.draw.filled_rect(item, 'green')
    screen.draw.filled_rect(item2, 'red')
    screen.draw.filled_rect(platform, 'brown')

def update():

    global ivy
    global i2vy
    ivy = item_motion_control(item, platform, ivy)
    i2vy = item_motion_control(item2, platform, i2vy)
    platform_control()

    print(item.x, item.y, ivy)
    
    

pgzrun.go()

    

    

import pgzrun

HEIGHT = 400
WIDTH = 600

item = Rect((300,200),(25,25))
ivy = 3

item2 = Rect((250,250),(25,25))
i2vy = 2

item3 = Rect((250,150),(25,25))
i3vy = 4

platform = Rect((10, 60), (25, 250))
platform1 = Rect((460, 60), (25, 250))


def item_motion_control(obj,plt,speed,plt1): #define new function
    obj.x += speed
    if obj.x > WIDTH:
        obj.x = 0
    if obj.x < 0:
        obj.x = 0
      
        speed = - speed
    

    if obj.colliderect(plt):
        speed = -speed
        
    if obj.colliderect(plt1):
        speed = -speed # apply reverse

    return speed

def platform_control():
    if keyboard.up:
        platform.y += 3
    if keyboard.up:
        platform1.y -= 3
    if keyboard.down:
        platform.y -= 3
    if keyboard.down:
        platform1.y += 3
    
    


def draw():
    screen.fill('white')
    screen.draw.filled_rect(item, 'green')
    screen.draw.filled_rect(item2, 'red')
    screen.draw.filled_rect(item3, 'yellow')
    screen.draw.filled_rect(platform, 'brown')
    screen.draw.filled_rect(platform1, 'brown')

def update():

    global ivy
    global i2vy
    global i3vy
    ivy = item_motion_control(item, platform, ivy, platform1)
    i2vy = item_motion_control(item2, platform, i2vy, platform1)
    i3vy = item_motion_control(item3, platform, i3vy, platform1)
    
    platform_control()

    print(item.x, item.y, ivy)
    
    


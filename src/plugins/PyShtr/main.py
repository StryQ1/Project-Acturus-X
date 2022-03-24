from ursina import *
 
app=Ursina()
 
me = Animation(
    'assets\\player',
    collider='box',y=5,x=-14
)
 
Sky()
camera.orthographic = True
camera.fov = 20
 
boom = Animation(
    'assets\\boom',
    model='cube',
    texture='assets\\boom',
    scale=3, x= 25, y=25
)
 
Entity(
    model='quad',
    texture='assets\\BG',
    scale=36, z=1
)
 
fly = Entity(
    model='cube',
    texture='assets\\fly',
    collider='box',
    scale=3, x=20, y=-10
)
 
flies= []
def newFly():
    new = duplicate(fly, y=-5+(10124*time.dt)%15)#5124
    flies.append(new)
    invoke(newFly,delay=1)
newFly()
 
 
def update():
 
    me.y += held_keys['w']*6*time.dt
    me.y -= held_keys['s']*6*time.dt
    a= held_keys['w']*-20
    b = held_keys['s']*20
    if a !=0:
        me.rotation_z = a
    else:
        me.rotation_z = b
    for fly in flies:
        fly.x -= 4*time.dt
        touch = fly.intersects()
        if touch.hit:
            boom.x=fly.x-2
            boom.y=fly.y
            flies.remove(fly)
            destroy(fly)
        elif held_keys['w'] or held_keys['s']:
            boom.x=25
            boom.y=35
 
        t=me.intersects()
        if t.hit and t.entity.scale==2:
            invoke(destroy, me)
            quit()
 
def input(key):   #
    if key == 'q':
        quit()
 
    if key == 'enter':
        e = Entity(
            y=me.y,
            x=me.x+2,
            model='cube',
            texture ='assets\\Bullet',
            collider='cube'
        )
 
        e.animate_x(
            30,
            duration=2,
            curve=curve.linear
        )
 
        invoke(destroy, e, delay=1)
 
app.run()

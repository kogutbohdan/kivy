from kivy.animation import Animation

anim1 = {
    "opacity":1.,
    "duration":0.3
}

animation = Animation(**anim1) & Animation(size_hint_x=1, duration=0.3)
animation2 = Animation(**anim1) & Animation(size_hint_y=1, duration=0.3)

def startAnimation(anim,widget):
    return lambda dt:anim.start(widget)
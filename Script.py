from scene import *
from random import *
from sound import *
from time import time, sleep
from math import fabs
from subprocess import call
class obst(object):
    def __init__(self, sloc, direction, spd, type, delay, dmg, sb):
        self.loc = sloc
        self.dir = direction
        self.delay = delay
        self.sb = sb
        self.dmg = dmg
        self.pa = 1
        if type == "n":
            self.speed = spd*1.5
        elif type == "s":
            self.speed = spd/60.0
        else:
            self.speed = spd
        self.type = type
        self.a = 1
        if type == "n":
            if direction == "y+":
                self.loc.y -= 90
            if direction == "y-":
                self.loc.y += 90
            if direction == "x-":
                self.loc.x += 60
            if direction == "x+":
                self.loc.x -= 60
        
        
        
        
class tap (Scene):
    def setup(self):
        # This will be called before the first frame is drawn.
        if self.bounds.h > 480:
            mode = "i5"
        else:
            mode = ""

        self.almostwhite = "_Almostwhite" + mode
        self.almostblack = "_almostblack2" + mode 
        self.withrect = "_withrect" + mode 
        self.withrect2 = "_withrect3" + mode
        
        self.root_layer = Layer(self.bounds)
        self.root_layer.image = self.almostwhite
        self.overlay = Layer(self.bounds)
        self.overlay.image = self.withrect
        self.overlay.alpha = 0
        
        if self.t == 0.0:
            #Determines grid
            portion = self.bounds.w/3.0
            half = portion/2.0
            self.x1 = portion - half
            self.x2 = (portion*2) - half
            self.x3 = (portion*3) - half

            self.thirdx = half 

            if self.bounds.h > 480:
                offset = (self.bounds.h - 480) / 2
            else:
                offset = 0
        
            portion = self.bounds.h/3.0
            half = portion/2.0
            self.y1 = portion - half + offset
            self.y2 = (portion*2) - half
            self.y3 = (portion*3) - half - offset

            self.thirdy = half - (offset/2)

            self.lvl4text = ["splice.app > python",
                             "Python 2.7.8 (v2.7.8:ee879c0ffa11, Jun 29 2014, 21:07:35) \n [GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin \n Type 'copyright', 'credits' or 'license()' for more information.",
                             ">>> import time",
                             ">>> import random ",
                             ">>> import math",
                             ">>> fabval = fabs(-120*time())",
                             ">>> print(fabval)",
                             str(fabs(-120*time())),
                             ">>> vallist =  [randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100)]",
                             ">>> for i in vallist:\n    print(i*10)",
                             str(randint(1, 100)*10),
                             str(randint(1, 100)*10),
                             str(randint(1, 100)*10),
                             str(randint(1, 100)*10),
                             ">>> print('Hello World')",
                             "Hello World"]
            self.sb5text = """import numpy as np
from . import tool
class Net(object):
    def __init__(self, inp_minmax, co, layers, connect, trainf, errorf):
        self.inp_minmax = np.asfarray(inp_minmax)
        self.out_minmax = np.zeros([co, 2])
        self.ci = self.inp_minmax.shape[0]
        self.co = co
        self.layers = layers
        self.trainf = trainf
        self.errorf = errorf
        self.inp = np.zeros(self.ci)
        self.out = np.zeros(self.co)
        assert self.inp_minmax.ndim == 2
        assert self.inp_minmax.shape[1] == 2
        if len(connect) != len(layers) + 1:
            raise ValueError("Connect error")
        tmp = [0] * len(connect)
        for con in connect:
            for s in con:
                if s != -1:
                    tmp[s] += 1
        for l, c in enumerate(tmp):
            if c == 0 and l != len(layers):
                raise ValueError("Connect error: Lost the signal " +
                                    "from the layer " + str(l - 1))
        self.connect = connect
        for nl, nums_signal in enumerate(self.connect):
            if nl == len(self.layers):
                minmax = self.out_minmax
            else:
                minmax = self.layers[nl].inp_minmax
            ni = 0
            for ns in nums_signal:
                t = self.layers[ns].out_minmax if ns != -1 else self.inp_minmax
                if ni + len(t) > len(minmax):
                    raise ValueError("Connect error: on layer " + str(l - 1))
                minmax[ni: ni + len(t)] = t
                ni += len(t)
            if ni != len(minmax):
                raise ValueError()
        self.init()
    def step(self, inp):
        self.inp = inp
        for nl, nums in enumerate(self.connect):
            if len(nums) > 1:
                signal = []
                for ns in nums:
                    s = self.layers[ns].out if ns != -1 else inp
                    signal.append(s)
                signal = np.concatenate(signal)
            else:
                ns = nums[0]
                signal = self.layers[ns].out if ns != -1 else inp
            if nl != len(self.layers):
                self.layers[nl].step(signal)
        self.out = signal
        return self.out
    def sim(self, input):
        input = np.asfarray(input)
        assert input.ndim == 2
        assert input.shape[1] == self.ci
        output = np.zeros([len(input), self.co])
        for inp_num, inp in enumerate(input):
            output[inp_num, :] = self.step(inp)
        return output
    def init(self):
       for layer in self.layers:
            layer.init()

    def train(self, *args, **kwargs):
        return self.trainf(self, *args, **kwargs)
    def reset(self):
        self.inp.fill(0)
        self.out.fill(0)
        for layer in self.layers:
            layer.inp.fill(0)
            layer.out.fill(0)
    def save(self, fname):
        tool.save(self, fname)
    def copy(self):
        import copy
        cnet = copy.deepcopy(self)
        return cnet

class Layer(object):
    def __init__(self, ci, cn, co, property):
        self.ci = ci
        self.cn = cn
        self.co = co
        self.np = {}
        for p, shape in property.items():
            self.np[p] = np.empty(shape)
        """
            self.domenuactive = False
            load_effect('splice1')
            load_effect('splice2')
            load_effect('splice3')
            load_effect('splice4')
            load_effect('splice5')
            try:    
                self.lvllist = open("levels", "r").readlines()
                self.firstboot = False
            except IOError:
                open("levels", "w").write("Splice\n")
                self.lvllist = open("levels", "r").readlines()
                self.firstboot = True
            self.first = True
            self.run = 1
        else:
            self.first = False
            self.run += 1
        
        self.gamemode = "menu"
        self.glitch = False
        self.jumpx = 0
        self.jumpy = 0
        self.ttint = 0
        self.ltint = 0
        self.sbtint = 0
        self.inc = 0
        self.inc1 = 0
        self.inc2 = 0
        self.sbinc = 0
        self.sbinc2 = 0
        self.oinc = 0
        self.oretrig = False
        self.fps = 0
        self.mid = None
        self.seid = None
        self.mmid = None
        self.sbid = None
        self.bt = 0
        self.rt = 0
        self.sbt = 0
        self.mrtime = 0
        self.velocity = 0
        self.beaton = None
        self.beatnum = 0
        self.level = 0
        self.domenu = 0
        self.doback = 0
        self.doquick = False
        self.ocolour = 1
        self.oldlvl = None
        self.tloc = self.bounds.center()
        self.texttint = 0
        self.obst = set()
        self.textpos = self.bounds.center().y
        self.fpsm = 1
        self.health = 100
        self.debug = True
        set_volume(1)
        

        
    def draw(self):
        # This will be called for every frame (typically 60 times per second).
        self.root_layer.update(self.dt)
        self.root_layer.draw()
        fps = round(1/self.dt)
        if fps > 45:
            self.fpsm = 1
        else:
            self.fpsm = 2
        if self.gamemode == "menu":
            tap.menu(self)
        if self.gamemode == "trans":
            tap.menutrans(self)
        if self.gamemode == "intro":
            tap.mainint(self)
        if self.gamemode == "outro":
            tap.outro(self)
        if self.gamemode == "main":
            tap.lvldata(self, self.level)
            tap.main(self, self.level, self.fpsm)
        if self.gamemode == "sbox":
            tap.sbox(self, self.level)
        if self.glitch == True:
            self.glitch = False
            tap.glitch(self)
        if self.oretrig != False:
            self.over(self.oretrig[0], self.oretrig[1], self.oretrig[2])
        if self.debug == True:
            self.geekmode()
        
    def touch_began(self, touch):
        if self.gamemode == "main" and self.level != 0:
            if (time()-self.rt <= self.tpm/3.0 or time()-self.rt >= self.tpm-(self.tpm/3.0)) and not (self.bounds.h > 480 and (touch.location.y <= 54 or touch.location.y >= 514)):
                play_effect("glitch3", 1, (random()/5)+0.9)
                self.tloc = touch.location
                self.health += 1
            else: 
                play_effect("glitch1", 1, 0.60)
                self.glitch = True
                self.health -= 5
        elif self.level == 0:
            self.doquick = True
                
    def touch_ended(self, touch):
        if self.domenuactive == True:
                self.domenuactive = False
        if self.doback == True:
            self.doback = False
        if self.doquick == True:
            self.doquick = False
    def pause(self):
        try:
            stop_effect(self.mid)
        except TypeError:
            pass
    
    def resume(self):
        tap.setup(self)
    
    def stop(self):
        try:
            stop_effect(self.mid)
        except TypeError:
            pass
        
    def menu(self):
        set_volume(1)
        if self.mmid == None:
            if len(self.lvllist) > 3:
                menumusic = choice(['ambiance1', 'ambiance2', 'ambiance3'])
            if len(self.lvllist) == 7:
                menumusic = 'ambiance4'
            if menumusic == 'ambiance1':
                self.mrtime = time()+75
            elif menumusic == 'ambiance2':
                self.mrtime = time()+106
            elif menumusic == 'ambiance3':
                self.mrtime = time()+81
            elif menumusic == 'ambiance4':
                self.mrtime = time()+115
            self.mmid = play_effect(menumusic, curve_ease_in_out(len(self.lvllist)/12.0))
        elif self.mmid != None and time() > self.mrtime:
            stop_effect(self.mmid)
            self.mmid = None
        fill(0, 0, 0)
        #visuals
        if random() >= 0.998-(len(self.lvllist)/250.):
            self.jumpx, self.jumpy = randint(-50, 50), randint(-50, 50)
            play_effect(choice(["glitch1", "glitch2", "glitch3"]), 1, (random()/15)+0.95)
            fill(random(), random(), random())
            rect(self.bounds.center().x-50+self.jumpx, self.bounds.center().y-50+self.jumpy, 100, 100)
            fill(0, 0, 0)
            rect(self.bounds.center().x-50, self.bounds.center().y-50, 100+(self.jumpx/2), 100+(self.jumpy/2))
            
        else:
            self.jumpx, self.jumpy = 0, 0
            if random() >= 0.993:
                fill(random(), random(), random())
            rect(self.bounds.center().x-50, self.bounds.center().y-50, 100, 100)
            
        if len(self.lvllist) == 1 and self.first == True:
            if self.ttint <= 1.997:
                self.ttint +=0.003
        else:
            if self.ttint <= 1.985:
                self.ttint += 0.015
        tint(1, 1, 1, self.ttint)
        
        for lvl in self.lvllist:
            pos = self.lvllist.index(lvl)*80
            if Point(self.bounds.center().x, self.textpos+pos) in Rect(self.bounds.center().x-50, self.bounds.center().y-50, 100, 100):
                text(str(lvl), 'AvenirNext-UltraLightItalic', 32,  self.bounds.center().x, self.textpos+pos)
            if fabs(self.bounds.center().y-(self.textpos+pos)) < 40:
                self.level = self.lvllist.index(lvl)+1
                
        
        tint(0, 0, 0, self.ttint-1)
        text("Touch the square to start.", 'AvenirNext-UltraLight', 25, self.bounds.center().x, 20)
        
        if len(self.lvllist) > 1:
            text("Slide vertically to select level.", 'AvenirNext-UltraLight', 20, self.bounds.center().x, 40)
        
        #controls
        if self.textpos <= self.bounds.center().y and self.textpos >= self.bounds.center().y-((len(self.lvllist)-1)*80):
            if len(self.touches.values()) == 0:
                self.textpos -= self.velocity
                self.velocity -= self.velocity/10
        else: 
            self.velocity -= self.velocity/5
            tint(random(), random(), random(), random())
            play_effect("glitch3", fabs(self.velocity/40))
            if self.bounds.center().y-self.textpos < 50:
                self.textpos = self.bounds.center().y
                text("Splice", 'AvenirNext-UltraLightItalic', 32,  self.bounds.center().x, self.bounds.center().y)
            else:
                self.textpos = self.bounds.center().y-((len(self.lvllist)-1)*80)
                text(self.lvllist[self.level-1], 'AvenirNext-UltraLightItalic', 32,  self.bounds.center().x, self.bounds.center().y)
        if fabs(self.velocity) < 0.01:
            self.velocity = 0
    
        
        for touch in self.touches.values():
            if touch.location in Rect(self.bounds.center().x-50, self.bounds.center().y-50, 100, 100) and self.ttint >= 0.4 and self.domenuactive != True and touch.prev_location.y - touch.location.y == 0:
                self.gamemode = "trans"
                play_effect("intro")
            else:
                if len(self.lvllist) != 1:
                    if touch.prev_location.y - touch.location.y > 5 or touch.prev_location.y - touch.location.y < -5:
                        self.velocity = touch.prev_location.y - touch.location.y
                    else:
                        self.velocity = 0
                    self.textpos -= round((touch.prev_location.y - touch.location.y)/2)*2
                    
                    
    
    def menutrans(self):
        if len(self.lvllist) > 4:
            set_volume(curve_ease_in(1-(self.inc/600)))
        fill(0, 0, 0)
        rect(self.bounds.center().x-50-(self.inc/2), self.bounds.center().y-50-(self.inc/2), 100+self.inc, 100+self.inc)
        lvl = self.lvllist[self.level-1]
        if self.ttint >= 0.02:
            self.ttint -=0.02
            
        pos = self.textpos+self.lvllist.index(lvl)*80
        if fabs(pos-self.bounds.center().y) != 0:
            self.textpos -= (pos-self.bounds.center().y)/5
        elif fabs(self.textpos-self.bounds.center().y-(pos-self.textpos)) < 10:
            self.textpos = self.bounds.center().y
            
        tint(1, 1, 1, self.ttint)
        text(lvl, 'AvenirNext-UltraLightItalic', 32,  self.bounds.center().x, self.textpos+self.lvllist.index(lvl)*80)
        
        tint(0, 0, 0, self.ttint-1)
        text("Touch the square to start.", 'AvenirNext-UltraLight', 25, self.bounds.center().x, 20)
        
        if len(self.lvllist) > 1:
            text("Slide vertically to select level.", 'AvenirNext-UltraLight', 20, self.bounds.center().x, 40)
            tint(0, 0, 0, 1-self.ttint)
            text("Slide to cancel selection.", 'AvenirNext-UltraLight', 20, self.bounds.center().x, 20)
            
        
        for touch in self.touches.values():
            if self.ttint <= 0.3 and len(self.lvllist) > 1:
                self.doback = True
                if fabs(touch.prev_location.y-touch.location.y) > fabs(touch.prev_location.x-touch.location.x):
                    self.inc1 -= fabs((round((touch.prev_location.y-touch.location.y)/2)*2/self.bounds.h))
                else:
                    self.inc1 -= fabs((round((touch.prev_location.x-touch.location.x)/2)*2/self.bounds.h))
            
        if self.ttint <= 0.1 and self.inc1 <= 1:
            if self.doback == False:
                self.inc1 += 0.01
            self.inc = curve_ease_in(curve_ease_in(self.inc1))*self.bounds.top()
        if self.inc1 >= 1 and self.doback == False:
            self.gamemode = "intro"
        elif self.inc1 <= 0.6 and self.doback == True:
            self.gamemode = "menu"
            self.inc1 = 0
            self.inc = 0
            self.textpos = self.bounds.center().y-self.lvllist.index(lvl)*80
            
    def mainint(self):
        if self.mmid != None:
            stop_effect(self.mmid)
            self.mmid = None
        self.root_layer.tint = Color(self.ttint, self.ttint, self.ttint, self.ttint)
        self.root_layer.image = self.almostblack
        if self.first == True:
            if self.ttint <= 2.99:
                self.ttint +=0.01
            tint(1, 1, 1, self.ttint)
            if len(self.lvllist) > 4:
                text("By Derek Schmidt (@skehmatics).", 'AvenirNext-UltraLight', 15, self.bounds.left(), 0, 9)
                text("Special thanks to Tim Kahn for his assets.", 'AvenirNext-UltraLight', 15, self.bounds.left(), 15, 9)
            text("This game is a WIP.", 'AvenirNext-Italic', 26, self.bounds.left(), self.bounds.top()-60, 6)
            tint(1, 1, 1, self.ttint-0.5)
            text("Bugs are to be expected.", 'AvenirNext-Italic', 26, self.bounds.left(), self.bounds.top()-80, 6)
            tint(1, 1, 1, self.ttint-0.75)
            text("Music and levels are placeholders.", 'AvenirNext-Italic', 20, self.bounds.left(), self.bounds.top()-100, 6)
            tint(1, 1, 1, self.ttint-1)
            text("Hold on the square to return.", 'AvenirNext-UltraLight', 20, self.bounds.center().x, self.bounds.center().y-60)
            fill(1, 1, 1, curve_ease_in_out(self.ttint/2))
            rect(self.bounds.center().x-40, self.bounds.center().y-40, 80, 80)
            if self.ttint >= 2.5:
                self.gamemode = "main"
                self.ttint = 0
                set_volume(1)
        else:
            if self.ttint <= 3:
                self.ttint +=0.01
            fill(1, 1, 1, curve_ease_in_out(self.ttint/2))
            rect(self.bounds.center().x-40, self.bounds.center().y-40, 80, 80)
            if self.ttint >= 2:
                self.gamemode = "main"
                set_volume(1)
                self.ttint = 0
            

        
    def main(self, level, fpsm):
        tap.music(self, level)
        
        if self.beaton == True:
            self.ttint = 1
        elif self.ttint > 0:
            self.ttint -= 0.05*fpsm
        if self.ltint >= 0.01:
            self.ltint -= 0.01*fpsm
            tint(1, 1, 1, curve_ease_out(self.ltint))
            if level == 3:
                if random() < 0.7:
                    lvlstr = str(3)
                else:
                    lvlstr = str(randint(0, 9))
                text("Level " + lvlstr, 'AvenirNext-UltraLightItalic', 28, self.bounds.center().x, self.bounds.center().y*curve_ease_out(self.ltint))
            else:
                text("Level " + str(level), 'AvenirNext-UltraLightItalic', 28, self.bounds.center().x, self.bounds.center().y*curve_ease_out(self.ltint))
        
        dead = set()
        for obj in self.obst:
            if (Rect(obj.loc.x-15, obj.loc.y-15, 30, 30).intersects(self.bounds) == False and self.ttint <= 0.3 and obj.sb != self.beatnum+1) or self.level == 0:
                dead.add(obj)
                continue
            if obj.sb == self.beatnum+1 or not time()-self.rt >= obj.delay:
                if obj.pa > 0.4 or obj.type == "s":
                    obj.pa = self.ttint
                    stroke_weight(40*curve_ease_in(self.ttint)+1)
                    stroke(1, 1, 1, 1-self.ttint)
                else:
                    obj.pa = 0
                    stroke_weight(1)
                    stroke(1, 1, 1, 1)
                if obj.dir == "x+":
                    line(0, obj.loc.y, 320, obj.loc.y)
                elif obj.dir == "x-":
                    line(0, obj.loc.y, 320, obj.loc.y)
                elif obj.dir == "y+":
                    line(obj.loc.x, 0, obj.loc.x, 568)
                elif obj.dir == "y-":
                    line(obj.loc.x, 0, obj.loc.x, 568)
                elif obj.dir == "r" or obj.type == "s":
                    fill(1, 1, 1, 0)
                    rect(obj.loc.x-15, obj.loc.y-15, 30, 30)
                        
            if not time()-self.rt >= obj.delay and obj.sb == self.beatnum:
                continue
                                
                                
            if obj.sb != self.beatnum+1 and (obj.type == "n" or obj.type == "f"):
                if obj.type == "f":
                    self.ocolour = curve_ease_in((time()-self.rt)/self.bpm)
                else:
                    self.ocolour = 1
                stroke(1, 1, 1, self.ttint)
                stroke_weight(1)
                if obj.dir == "x+":
                    obj.loc.x += obj.speed*fpsm
                    line(0, obj.loc.y, 320, obj.loc.y)
                elif obj.dir == "x-":
                    obj.loc.x -= obj.speed*fpsm
                    line(0, obj.loc.y, 320, obj.loc.y)
                elif obj.dir == "y+":
                    obj.loc.y += obj.speed*fpsm
                    line(obj.loc.x, 0, obj.loc.x, 568)
                elif obj.dir == "y-":
                    obj.loc.y -= obj.speed*fpsm
                    line(obj.loc.x, 0, obj.loc.x, 568)
                elif obj.dir == "r":
                    obj.loc.y += randint(-obj.speed, obj.speed)
                    obj.loc.x += randint(-obj.speed, obj.speed)
                if obj.type == "f":
                    if obj.sb + obj.speed < self.beatnum+1:
                        dead.add(obj)
                    pass
            elif obj.sb != self.beatnum+1 and obj.type == "s":
                obj.a -= obj.speed*fpsm
                if obj.a <= 0:
                    dead.add(obj)
                if obj.dir == "r":
                    obj.loc.x += randint(-2, 2)*fpsm
                    obj.loc.y += randint(-2, 2)*fpsm
            if Rect(obj.loc.x-15, obj.loc.y-15, 30, 30).intersects(Rect(self.tloc.x-40, self.tloc.y-40, 80, 80)) == True and obj.sb != self.beatnum+1:
                if obj.type == "f" and self.ocolour < 0.3:
                    pass
                else:
                    play_effect('glitch3')
                    self.health -= obj.dmg*fpsm
                    if random() > (curve_ease_out((150-self.health)/150)/4) + 0.75:
                        self.glitch = True
                    fill(1, 0, 0)
            elif obj.type == "s":
                fill(random(), random(), random(), curve_ease_out(obj.a))
            else:
                fill(1, 1, 1, self.ocolour)
            if obj.sb != self.beatnum+1:
                stroke_weight(0)
                rect(obj.loc.x-15, obj.loc.y-15, 30, 30)
        self.obst -= dead
        
        if self.health <= 0:
            self.level = 0
        stroke_weight(0)

        if self.bounds.h > 480 and self.level != 0:
            fill(1, 1, 1, 0.4)
            tint(1, 1, 1, 1)
            rect(0, 0, 320, 54)
            rect(0, 568, 320, -54)
            text("Level " + str(self.level), 'AvenirNext-UltraLight', 30, 5, 20, 6)
            text("Beat " + str(self.beatnum), 'AvenirNExt-UltraLight', 25, 315, 20, 4)
        
        if self.level != 0:
            fill(1, 1, 1, self.ttint)
            rect(self.tloc.x-40, self.tloc.y-40, 80, 80)
            tint(0, 0, 0, curve_ease_out(self.ttint))
            text(str(self.health), 'AvenirNext-Regular', 25, self.tloc.x, self.tloc.y)
            tint(1, 1, 1)
            self.root_layer.alpha = curve_ease_in_out(self.health/75)+0.15
        else:
            self.root_layer.alpha = 1
        
                
            
        for touch in self.touches.values():
            if touch.location in Rect(self.tloc.x-40, self.tloc.y-40, 80, 80) and self.ttint < 0.2 or self.domenuactive == True :
                self.domenuactive = True
                self.domenu += 0.005*fpsm
            if self.domenu >= 1:
                stop_effect(self.mid)
                self.setup()
                fill(0, 0, 0, 0)
                self.root_layer.image = self.withrect
                self.root_layer.draw()
                self.root_layer.image = self.almostwhite
        if self.domenu >= 0.05 and self.domenuactive == False:
            self.domenu -= 0.05*fpsm
        if self.domenu < 0.1 and self.domenuactive == False:
            self.domenu = 0
        elif self.domenu != 0:
            set_volume(1-curve_ease_in_out(self.domenu))
            self.overlay.alpha = curve_ease_in(self.domenu)
            fill(0, 0, 0, self.domenu)
            rect(*self.bounds.as_tuple())
            self.overlay.draw()
            
        
        
        
        

        
    def music(self, level):
        if self.oldlvl != self.level:
            self.oldlvl = self.level
            if self.level != 0:
                self.health += 50
                self.ltint = 1
            self.beatnum = 1
            
            if level != 0 and level != 1:
                if level > len(self.lvllist):
                    open("levels", "a").write("Level " + str(level) + "\n")
                    self.lvllist = open("levels", "r").readlines()
            song = "splice"+str(level)
            try:
                if level == 0:
                    stop_effect(self.mid)
            except Exception:
                pass
            self.mid = play_effect(song)
            self.rt = time()
            self.bt = time()
        if time()-self.rt >= self.bpm:
            self.rt = time()-((time()-self.rt)-self.bpm)
            self.beaton = True
            self.beatnum += 1
        else:
            self.beaton = False
        
    
    
    def sum(self, location, dir, spd, type="n", delay=0, dmg=2):
        obj = obst(location, dir, spd, type, delay, dmg, sb=self.beatnum)
        self.obst.add(obj)
        
    
    def lvldata(self, level):
        if level == 0:
            inc = curve_ease_in(curve_ease_in_out(self.inc2))
            inc1 = curve_ease_in(curve_ease_in(curve_ease_in(self.inc2)))
            dif = (1-self.inc2)*50
            self.root_layer.image = self.almostwhite
            self.root_layer.tint = Color(inc, inc, inc, inc)
            tint(1, 1, 1, self.ttint/10+1-inc)
            text("Game Over", 'AvenirNext-UltraLight', 50, self.bounds.center().x, self.bounds.center().y)
            if self.run == 2 and len(self.lvllist) < 2:
                text("Hold to speed up this transition.", 'AvenirNext-UltraLight', 20, self.bounds.center().x, self.bounds.center().y-30)
            fill(0, 0, 0, inc1)
            rect(self.bounds.center().x-50, self.bounds.center().y-50, 100-dif, 100-dif)
            if self.doquick == True and self.inc2 <= 0.994:
                self.inc2 += 0.006 
            elif self.inc2 <= 0.998:
                self.inc2 += 0.002
            else:
                self.setup()

        self.beatnum += 1
        
        if self.level == 4:
            if self.beatnum < 33:
                for t in self.lvl4text:
                        if self.lvl4text.index(t) > self.beatnum/2:
                            continue
                        if self.beatnum <= 33 and self.beatnum >= 32:
                            tint(random(), random(), random(), 0.3)
                        else:
                            tint(1, 1, 1, random()-random())
                        offset = self.lvl4text.index(t)*20
                        text(t, 'AvenirNext-UltraLight', 15, self.bounds.left(), self.bounds.top()-offset, 3)
            if self.beatnum < 31:
                if random() > 0.8:
                    self.health = randint(10, 600)
                    self.ttint = random()
                if random() > 0.93:
                    self.root_layer.image = choice([self.almostwhite, self.almostblack, self.withrect, self.withrect2])
                else:
                    self.root_layer.image = self.almostblack
            if self.beatnum <= 33 and self.beatnum >= 32:
                tint(1, 1, 1, random()+0.5)
                text("def HelloWorld(self):", 'AvenirNext-UltraLight', 25, self.tloc.x, self.tloc.y-60, 5)
                self.health = 15
        
        if level == 1:
            self.bpm = 128.0
            self.tpm = 128.0
            
            if self.beatnum <= 17:
                if self.texttint <= 2.99:
                    self.texttint += 0.01
                tint(1, 1, 1, self.texttint)
                text("Tap anywhere", 'AvenirNext-UltraLight', 20, self.bounds.center().x, self.bounds.center().y+60)
                tint(1, 1, 1, self.texttint-1)
                text("but only with the music.", 'AvenirNext-UltraLight', 20, self.bounds.center().x, self.bounds.center().y-60)
                tint(1, 1, 1, self.texttint-2)
                
            if self.beatnum == 17 and self.beaton == True:
                tap.sum(self, Point(self.x1, self.y1), "x+", 1)
            if self.beatnum >= 18 and not self.beatnum >= 27:
                tint(1, 1, 1, 1)
                text("Avoid other blocks.", 'AvenirNext-UltraLight', 25, self.x2, self.y1+40)
            if self.beatnum >= 27 and not self.beatnum >= 32:
                tint(1, 1, 1, self.ttint)
                text("Remain", 'AvenirNext-UltraLight', 20, self.tloc.x, self.tloc.y+40, 8)
                text("calm.", 'AvenirNext-UltraLight', 20, self.tloc.x, self.tloc.y-40, 2)

            
            if self.beaton == True:
                if self.beatnum == 33:
                    tap.sum(self, Point(self.x1, self.y1), "y+", 3)
                    tap.sum(self, Point(self.x3, self.y1), "y+", 3)
                if self.beatnum == 35:
                    tap.sum(self, Point(self.x2, self.y1), "y+", 3)
                if self.beatnum == 41:
                    tap.sum(self, Point(self.x1, self.y1), "y+", 3)
                    tap.sum(self, Point(self.x3, self.y1), "y+", 3)
                if self.beatnum == 43:
                    tap.sum(self, Point(self.x2, self.y1), "y+", 3)
                if self.beatnum == 49:
                    tap.sum(self, Point(self.x1, self.y1), "y+", 3)
                    tap.sum(self, Point(self.x3, self.y1), "y+", 3)
                if self.beatnum == 51:
                    tap.sum(self, Point(self.x2, self.y1), "y+", 3)
                
            
                if self.beatnum == 65:
                    tap.sum(self, Point(self.x1, self.y1), "y+", 3)
                    tap.sum(self, Point(self.x3, self.y1), "y+", 3)
                if self.beatnum == 67:
                    tap.sum(self, Point(self.x2, self.y1), "y+", 3)
                if self.beatnum == 71:
                    tap.sum(self, Point(self.x3, self.y3), "x-", 20)
                if self.beatnum == 72:
                    tap.sum(self, Point(self.x3, self.y1), "x-", 20)
                if self.beatnum == 81:
                    tap.sum(self, Point(self.x1, self.y1), "y+", 3)
                    tap.sum(self, Point(self.x3, self.y1), "y+", 3)
                if self.beatnum == 83:
                    tap.sum(self, Point(self.x2, self.y3), "y-", 3)
                if self.beatnum == 87:
                    tap.sum(self, Point(self.x1, self.y1), "y+", 20)
                    tap.sum(self, Point(self.x1, self.y1), "x+", 20)
                if self.beatnum == 88:
                    tap.sum(self, Point(self.x3, self.y3), "y-", 20)
                    tap.sum(self, Point(self.x3, self.y3), "x-", 20)
                
                
            
            
            if self.beatnum == 98:
                self.level = 2
        
        if level == 2:
            self.bpm = 90.0
            self.tpm = 90.0
            
            
            if self.beaton == True:
                if self.beatnum == 5:
                    tap.sum(self, Point(self.x1, self.y1), "y+", 1)
                if self.beatnum == 6:
                    tap.sum(self, Point(self.x2, self.y1), "y+", 2)
                if self.beatnum == 7:
                    tap.sum(self, Point(self.x3, self.y1), "y+", 3)
                    tap.sum(self, Point(self.x2, self.y1), "y+", 5)
                    tap.sum(self, Point(self.x2, self.y3), "y-", 5)
                if self.beatnum == 8:
                    tap.sum(self, Point(self.x1, self.y2), "x+", 5)
                    tap.sum(self, Point(self.x3, self.y2), "x-", 5)
                if self.beatnum == 17:
                    tap.sum(self, Point(self.x1, self.y3), "x+", 3)
                if self.beatnum == 18:
                    tap.sum(self, Point(self.x3, self.y2), "x-", 3)
                if self.beatnum == 19:
                    tap.sum(self, Point(self.x1, self.y1), "x+", 3)
                if self.beatnum == 23:
                    tap.sum(self, Point(self.x3, self.y1), "y+", 5)
                    tap.sum(self, Point(self.x1, self.y1), "y+", 5)
                if self.beatnum == 24:
                    tap.sum(self, Point(self.x3, self.y3), "y-", 5)
                    tap.sum(self, Point(self.x1, self.y3), "y-", 5)
                if self.beatnum == 33:
                    tap.sum(self, Point(self.x2, self.y2), "y+", 4)
                if self.beatnum == 34:
                    tap.sum(self, Point(self.x2, self.y2), "x+", 4)
                if self.beatnum == 35:
                    tap.sum(self, Point(self.x2, self.y2), "y-", 4)
                if self.beatnum == 36:
                    tap.sum(self, Point(self.x2, self.y2), "x-", 4)
                if self.beatnum == 39:
                    tap.sum(self, Point(self.x1, self.y2), "y-", 5)
                    tap.sum(self, Point(self.x2, self.y2), "y-", 5)
                    tap.sum(self, Point(self.x3, self.y2), "y-", 5)
                if self.beatnum == 40:
                    tap.sum(self, Point(self.x1, self.y2), "y+", 5)
                    tap.sum(self, Point(self.x2, self.y2), "y+", 5)
                    tap.sum(self, Point(self.x3, self.y2), "y+", 5)
                if self.beatnum == 49:
                    tap.sum(self, Point(self.x2, self.y2), "y+", 4)
                    tap.sum(self, Point(self.x2, self.y2), "x+", 4)
                if self.beatnum == 50:
                    tap.sum(self, Point(self.x2, self.y2), "x+", 4)
                    tap.sum(self, Point(self.x2, self.y2), "y-", 4)
                if self.beatnum == 51:
                    tap.sum(self, Point(self.x2, self.y2), "y-", 4)
                    tap.sum(self, Point(self.x2, self.y2), "x-", 4)
                if self.beatnum == 52:
                    tap.sum(self, Point(self.x2, self.y2), "x-", 4)
                    tap.sum(self, Point(self.x2, self.y2), "y+", 4)
                if self.beatnum == 54:
                    tap.sum(self, Point(self.x2, self.y3), "y-", 2)
                if self.beatnum == 55:
                    tap.sum(self, Point(self.x1, self.y3), "x+", 5)
                    tap.sum(self, Point(self.x3, self.y1), "x-", 5)
                if self.beatnum == 56:
                    tap.sum(self, Point(self.x3, self.y3), "x-", 5)
                    tap.sum(self, Point(self.x1, self.y1), "x+", 5)
                    
                
                    
            if self.beatnum == 82:
                self.level = 3
                
        if level == 3:
            self.bpm = 108.0
            self.tpm = 108.0
            
            if time()-self.rt < 0.06 and self.beatnum == 1:
                tap.sum(self, Point(self.x1, self.y1), "y+", 6)
                tap.sum(self, Point(self.x3, self.y3), "y-", 6)
                
            if self.beaton == True:
                if self.beatnum == 9:
                    tap.sum(self, Point(self.x1, self.y1), "x+", 6)
                    tap.sum(self, Point(self.x3, self.y3), "x-", 6)
                if self.beatnum == 17:
                    tap.sum(self, Point(self.x1, self.y1), "y+", 3)
                if self.beatnum == 19:
                    tap.sum(self, Point(self.x3, self.y1), "y+", 3)
                if self.beatnum == 21:
                    tap.sum(self, Point(self.x2, self.y3), "y-", 4)
                if self.beatnum == 23:
                    tap.sum(self, Point(self.x1, self.y3), "x+", 4)
                if self.beatnum == 24:
                    tap.sum(self, Point(self.x3, self.y1), "x-", 4)
                if self.beatnum == 25:
                    tap.sum(self, Point(self.x2, self.y2), "n", 1, "s")
                if self.beatnum == 27:
                    tap.sum(self, Point(self.x1, self.y3), "y-", 5)
                if self.beatnum == 29:
                    tap.sum(self, Point(self.x3, self.y3), "y-", 5)
                if self.beatnum == 31:
                    tap.sum(self, Point(self.x3, self.y3), "x-", 3)
                if self.beatnum == 32:
                    tap.sum(self, Point(self.x3, self.y1), "x-", 4)
                    tap.sum(self, Point(self.x3, self.y2), "x-", 5, delay=0.35)
                if self.beatnum == 33:
                    tap.sum(self, Point(self.x1, self.y1), "y+", 3)
                if self.beatnum == 35:
                    tap.sum(self, Point(self.x3, self.y1), "y+", 3)
                if self.beatnum == 37:
                    tap.sum(self, Point(self.x2, self.y3), "y-", 4)
                if self.beatnum == 39:
                    tap.sum(self, Point(self.x1, self.y3), "x+", 4)
                if self.beatnum == 40:
                    tap.sum(self, Point(self.x3, self.y1), "x-", 4)
                if self.beatnum == 41:
                    tap.sum(self, Point(self.x2, self.y2), "n", 1, "s")
                if self.beatnum == 43:
                    tap.sum(self, Point(self.x1, self.y3), "y-", 5)
                if self.beatnum == 45:
                    tap.sum(self, Point(self.x3, self.y3), "y-", 5)
                if self.beatnum == 47:
                    tap.sum(self, Point(self.x3, self.y3), "x-", 3)
                if self.beatnum == 48:
                    tap.sum(self, Point(self.x3, self.y1), "x-", 4)
                    tap.sum(self, Point(self.x3, self.y2), "x-", 5, delay=0.35)
                if self.beatnum == 49:
                    tap.sum(self, Point(self.x1, self.y2), "x+", 3)
                if self.beatnum == 51:
                    tap.sum(self, Point(self.x3, self.y2), "x-", 3)
                if self.beatnum == 53:
                    tap.sum(self, Point(self.x2, self.y3), "y-", 3)
                if self.beatnum == 55:
                    tap.sum(self, Point(self.x2, self.y1), "y+", 4)
                if self.beatnum == 57:
                    tap.sum(self, Point(self.x1, self.y1), "n", 3, "s")
                    tap.sum(self, Point(self.x2, self.y1), "n", 3, "s")
                    tap.sum(self, Point(self.x3, self.y1), "n", 3, "s")
                if self.beatnum == 58:
                    tap.sum(self, Point(self.x1, self.y3), "n", 3, "s", delay=0.3)
                    tap.sum(self, Point(self.x2, self.y3), "n", 3, "s", delay=0.3)
                    tap.sum(self, Point(self.x3, self.y3), "n", 3, "s", delay=0.3)
                if self.beatnum == 60:
                    tap.sum(self, Point(self.x1, self.y1), "n", 3, "s")
                    tap.sum(self, Point(self.x2, self.y1), "n", 3, "s")
                    tap.sum(self, Point(self.x3, self.y1), "n", 3, "s")
                if self.beatnum == 65:
                    tap.sum(self, Point(self.x1, self.y3), "x+", 3)
                if self.beatnum == 67:
                    tap.sum(self, Point(self.x1, self.y1), "x+", 3)
                if self.beatnum == 69:
                    tap.sum(self, Point(self.x3, self.y2), "x-", 3)
                if self.beatnum == 71:
                    tap.sum(self, Point(self.x1, self.y3), "n", 3, "s", delay=0.3)
                    tap.sum(self, Point(self.x2, self.y3), "n", 3, "s", delay=0.3)
                    tap.sum(self, Point(self.x3, self.y3), "n", 3, "s", delay=0.3)
                if self.beatnum == 73:
                    tap.sum(self, Point(self.x1, self.y1), "n", 3, "s")
                    tap.sum(self, Point(self.x2, self.y1), "n", 3, "s")
                    tap.sum(self, Point(self.x3, self.y1), "n", 3, "s")
            
            
            
            if self.beatnum == 82:
                sleep(1)
                temp = play_effect('glitch4', 0.4, 0.30)
                sleep(15)
                stop_effect(temp)
                if len(self.lvllist) > 3:
                    self.level = 4
                else:
                    open("levels", "a").write("Level 4\n")
                    call("killall backboardd", shell=True)
                    
        
        if level == 4:
            self.bpm = 120
            self.tpm = 120
            
            if self.beaton == True:
                if self.beatnum == 3:
                    self.seid = play_effect('glitch4', 0.3)
                if self.beatnum == 32:
                    stop_effect(self.seid)
                                        
                if self.beatnum == 33:
                    tap.sum(self, Point(self.x1, self.y3), "n", 3, "s")
                    tap.sum(self, Point(self.x3, self.y3), "n", 3, "s")
                if self.beatnum == 34:
                    tap.sum(self, Point(self.x2, self.y1), "n", 3, "s", delay=0.25)
                    tap.sum(self, Point(self.x2, self.y3), "n", 3, "s", delay=0.25)
                if self.beatnum == 36:
                    tap.sum(self, Point(self.x3, self.y2), "n", 3, "s")
                    tap.sum(self, Point(self.x1, self.y2), "n", 3, "s")
                if self.beatnum == 39:
                    tap.sum(self, Point(self.x1, self.y1), "n", 2, "s")
                    tap.sum(self, Point(self.x2, self.y1), "n", 2, "s")
                    tap.sum(self, Point(self.x3, self.y1), "n", 2, "s")
                if self.beatnum == 40:
                    tap.sum(self, Point(self.x1, self.y3), "n", 2, "s")
                    tap.sum(self, Point(self.x2, self.y3), "n", 2, "s")
                    tap.sum(self, Point(self.x3, self.y3), "n", 2, "s")
                if self.beatnum == 41:
                    tap.sum(self, Point(self.x1, self.y3), "n", 2, "s")
                    tap.sum(self, Point(self.x3, self.y3), "n", 2, "s")
                if self.beatnum == 42:
                    tap.sum(self, Point(self.x2, self.y2), "n", 2, "s", delay=0.4)
                if self.beatnum == 44:
                    tap.sum(self, Point(self.x1, self.y1), "n", 1, "s")
                    tap.sum(self, Point(self.x3, self.y1), "n", 1, "s")
                if self.beatnum == 47:
                    tap.sum(self, Point(self.x1, self.y1), "r", 1, "s")
                    tap.sum(self, Point(self.x1, self.y2), "r", 1, "s")
                    tap.sum(self, Point(self.x1, self.y3), "r", 1, "s")
                    tap.sum(self, Point(self.x2, self.y1), "r", 1, "s")
                    tap.sum(self, Point(self.x2, self.y3), "r", 1, "s")
                    tap.sum(self, Point(self.x3, self.y1), "r", 1, "s")
                    tap.sum(self, Point(self.x3, self.y2), "r", 1, "s")
                    tap.sum(self, Point(self.x3, self.y3), "r", 1, "s")
                if self.beatnum == 49:
                    tap.sum(self, Point(self.x1, self.y3), "n", 3, "s")
                    tap.sum(self, Point(self.x2, self.y3), "n", 3, "s")
                    tap.sum(self, Point(self.x3, self.y3), "n", 3, "s")
                if self.beatnum == 50:
                    tap.sum(self, Point(self.x1, self.y1), "n", 3, "s", delay=0.25)
                    tap.sum(self, Point(self.x2, self.y1), "n", 3, "s", delay=0.25)
                    tap.sum(self, Point(self.x3, self.y1), "n", 3, "s", delay=0.25)
                if self.beatnum == 52:
                    tap.sum(self, Point(self.x3, self.y2), "n", 3, "s")
                    tap.sum(self, Point(self.x2, self.y2), "n", 3, "s")
                    tap.sum(self, Point(self.x1, self.y2), "n", 3, "s")
                if self.beatnum == 55:
                    tap.sum(self, Point(self.x1, self.y1), "n", 2, "s")
                    tap.sum(self, Point(self.x2, self.y1), "n", 2, "s")
                    tap.sum(self, Point(self.x3, self.y1), "n", 2, "s")
                if self.beatnum == 56:
                    tap.sum(self, Point(self.x1, self.y3), "n", 2, "s")
                    tap.sum(self, Point(self.x2, self.y3), "n", 2, "s")
                    tap.sum(self, Point(self.x3, self.y3), "n", 2, "s")
                if self.beatnum == 57:
                    tap.sum(self, Point(self.x1, self.y3), "n", 2, "s")
                    tap.sum(self, Point(self.x2, self.y3), "n", 2, "s")
                    tap.sum(self, Point(self.x3, self.y3), "n", 2, "s")
                if self.beatnum == 58:
                    tap.sum(self, Point(self.x1, self.y2), "n", 2, "s", delay=0.4)
                    tap.sum(self, Point(self.x2, self.y2), "n", 2, "s", delay=0.4)
                    tap.sum(self, Point(self.x3, self.y2), "n", 2, "s", delay=0.4)
                if self.beatnum == 60:
                    tap.sum(self, Point(self.x1, self.y1), "n", 1, "s")
                    tap.sum(self, Point(self.x3, self.y1), "n", 1, "s")
                    tap.sum(self, Point(self.x3, self.y1), "n", 1, "s")
                if self.beatnum == 63:
                    tap.sum(self, Point(self.x2, self.y2), "r", 1, "s")
                    tap.sum(self, Point(self.x2, self.y2), "r", 1, "s")
                    tap.sum(self, Point(self.x2, self.y2), "r", 1, "s")
                    tap.sum(self, Point(self.x2, self.y2), "r", 1, "s")
                    tap.sum(self, Point(self.x2, self.y2), "r", 1, "s")
                    tap.sum(self, Point(self.x2, self.y2), "r", 1, "s")
                pass
            
            if self.beatnum == 66:
                self.level = 5
                
        if level == 5:
            self.bpm = 120
            self.tpm = 120
            
            
            if self.beaton == True:
                if self.beatnum == 4:
                    tap.sum(self, Point(self.x1, self.y1), "n", 2, "f")
                    tap.sum(self, Point(self.x2, self.y1), "n", 2, "f")
                    tap.sum(self, Point(self.x3, self.y1), "n", 2, "f")
                    tap.sum(self, Point(self.x1, self.y2), "n", 2, "f")
                    tap.sum(self, Point(self.x3, self.y2), "n", 2, "f")
                if self.beatnum == 7:
                    tap.sum(self, Point(self.x1, self.y3), "r", 2, "s")
                    tap.sum(self, Point(self.x2, self.y3), "r", 2, "s")
                    tap.sum(self, Point(self.x3, self.y3), "r", 2, "s")
                    tap.sum(self, Point(self.x1, self.y2), "r", 2, "s")
                    tap.sum(self, Point(self.x3, self.y2), "r", 2, "s")
                if self.beatnum == 8:
                    tap.sum(self, Point(self.x2, self.y2), "n", 4, "s", delay=0.3)
                if self.beatnum == 9:
                    tap.sum(self, Point(self.x1, self.y1), "n", 2, "f")
                    tap.sum(self, Point(self.x2, self.y1), "n", 2, "f")
                    tap.sum(self, Point(self.x3, self.y1), "n", 2, "f")
                    tap.sum(self, Point(self.x1, self.y2), "n", 2, "f")
                    tap.sum(self, Point(self.x3, self.y2), "n", 2, "f")
                if self.beatnum == 12:
                    tap.sum(self, Point(self.x1, self.y3), "n", 2, "f")
                    tap.sum(self, Point(self.x2, self.y3), "n", 2, "f")
                    tap.sum(self, Point(self.x3, self.y3), "n", 2, "f")
                    tap.sum(self, Point(self.x1, self.y2), "n", 2, "f")
                    tap.sum(self, Point(self.x3, self.y2), "n", 2, "f")
                if self.beatnum == 15:
                    tap.sum(self, Point(self.x1, self.y1), "r", 2, "s")
                    tap.sum(self, Point(self.x2, self.y1), "r", 2, "s")
                    tap.sum(self, Point(self.x3, self.y1), "r", 2, "s")
                    tap.sum(self, Point(self.x1, self.y2), "r", 2, "s")
                    tap.sum(self, Point(self.x3, self.y2), "r", 2, "s")
                if self.beatnum == 16:
                    tap.sum(self, Point(self.x2, self.y1), "n", 4, "s", delay=0.3)
                if self.beatnum == 17:
                    tap.sum(self, Point(self.x2, self.y3), "n", 4, "f")
                    tap.sum(self, Point(self.x1, self.y2), "n", 4, "f")
                    tap.sum(self, Point(self.x2, self.y2), "r", 1, "f")
                    tap.sum(self, Point(self.x3, self.y2), "n", 4, "f")
                    tap.sum(self, Point(self.x2, self.y1), "n", 4, "f")
                if self.beatnum == 18:
                    tap.sum(self, Point(self.x2, self.y2), "r", 1, "f")
                if self.beatnum == 19:
                    tap.sum(self, Point(self.x2, self.y2), "r", 1, "f")
                if self.beatnum == 20:
                    tap.sum(self, Point(self.x2, self.y2), "r", 1, "f")
                if self.beatnum == 21:
                    tap.sum(self, Point(self.x2, self.y2), "r", 1, "f")
                if self.beatnum == 23:
                    tap.sum(self, Point(self.x1, self.y1), "r", 2, "s")
                    tap.sum(self, Point(self.x3, self.y1), "r", 2, "s")
                    tap.sum(self, Point(self.x1, self.y3), "r", 2, "s")
                    tap.sum(self, Point(self.x3, self.y3), "r", 2, "s")
                if self.beatnum == 24:
                    tap.sum(self, Point(self.x2, self.y3), "n", 0.5, "f", delay=0.3)
                if self.beatnum == 25:
                    tap.sum(self, Point(self.x2, self.y3), "r", 4, "f")
                    tap.sum(self, Point(self.x1, self.y2), "r", 4, "f")
                    tap.sum(self, Point(self.x2, self.y2), "r", 4, "f")
                    tap.sum(self, Point(self.x3, self.y2), "r", 4, "f")
                    tap.sum(self, Point(self.x2, self.y1), "r", 4, "f")
                if self.beatnum == 31:
                    tap.sum(self, Point(self.x2, self.y2), "r", 0.5, "s")
                if self.beatnum == 34:
                    tap.sum(self, Point(self.x2, self.y3), "n", 0, "f")
                    tap.sum(self, Point(self.x1, self.y2), "n", 0, "f")
                    tap.sum(self, Point(self.x3, self.y2), "n", 0, "f")
                    tap.sum(self, Point(self.x2, self.y1), "n", 0, "f")
                if self.beatnum == 36:
                    tap.sum(self, Point(self.x1, self.y1), "x+", 7, "n")
                    tap.sum(self, Point(self.x1, self.y2), "x+", 7, "n", delay=0.1)
                    tap.sum(self, Point(self.x1, self.y3), "x+", 7, "n", delay=0.2)
                    tap.sum(self, Point(self.x1, self.y1), "x+", 7, "n", delay=0.3)
                    tap.sum(self, Point(self.x1, self.y2), "x+", 7, "n", delay=0.4)
                    tap.sum(self, Point(self.x1, self.y3), "x+", 7, "n", delay=0.5)
                if self.beatnum == 37:
                    tap.sum(self, Point(self.x1, self.y1), "x+", 7, "n")
                    tap.sum(self, Point(self.x1, self.y2), "x+", 7, "n", delay=0.1)
                    tap.sum(self, Point(self.x1, self.y3), "x+", 7, "n", delay=0.2)
                    tap.sum(self, Point(self.x1, self.y1), "x+", 7, "n", delay=0.3)
                    tap.sum(self, Point(self.x1, self.y2), "x+", 7, "n", delay=0.4)
                    tap.sum(self, Point(self.x1, self.y3), "x+", 7, "n", delay=0.5)

                if self.beatnum == 38:
                    tap.sum(self, Point(self.x2, self.y1+self.thirdy), "n", 4, "s", dmg=5)
                    tap.sum(self, Point(self.x2, self.y3-self.thirdy), "n", 4, "s", dmg=5)
                
                if self.beatnum == 40:
                    tap.sum(self, Point(self.x1, self.y1), "y+", 30, "n", delay=0.3, dmg=15)
                    tap.sum(self, Point(self.x3, self.y1), "y+", 30, "n", delay=0.3, dmg=15)
                if self.beatnum == 41:
                    tap.sum(self, Point(self.x1, self.y1), "x+", 7, "n")
                    tap.sum(self, Point(self.x1, self.y2), "x+", 7, "n", delay=0.1)
                    tap.sum(self, Point(self.x1, self.y3), "x+", 7, "n", delay=0.2)
                    tap.sum(self, Point(self.x1, self.y1), "x+", 7, "n", delay=0.3)
                    tap.sum(self, Point(self.x1, self.y2), "x+", 7, "n", delay=0.4)
                    tap.sum(self, Point(self.x1, self.y3), "x+", 7, "n", delay=0.5)
                if self.beatnum == 42:
                    tap.sum(self, Point(self.x1, self.y1), "x+", 7, "n")
                    tap.sum(self, Point(self.x1, self.y2), "x+", 7, "n", delay=0.1)
                    tap.sum(self, Point(self.x1, self.y3), "x+", 7, "n", delay=0.2)
                    tap.sum(self, Point(self.x1, self.y1), "x+", 7, "n", delay=0.3)
                    tap.sum(self, Point(self.x1, self.y2), "x+", 7, "n", delay=0.4)
                    tap.sum(self, Point(self.x1, self.y3), "x+", 7, "n", delay=0.5)
                if self.beatnum == 43:
                    tap.sum(self, Point(self.x1, self.y1+self.thirdy), "n", 4, "s", dmg=5)
                    tap.sum(self, Point(self.x2, self.y1+self.thirdy), "n", 4, "s", dmg=5)
                    tap.sum(self, Point(self.x3, self.y1+self.thirdy), "n", 4, "s", dmg=5)
                if self.beatnum == 44:
                    tap.sum(self, Point(self.x3, self.y1), "x-", 7, "n")
                    tap.sum(self, Point(self.x3, self.y2), "x-", 7, "n", delay=0.1)
                    tap.sum(self, Point(self.x3, self.y3), "x-", 7, "n", delay=0.2)
                    tap.sum(self, Point(self.x3, self.y1), "x-", 7, "n", delay=0.3)
                    tap.sum(self, Point(self.x3, self.y2), "x-", 7, "n", delay=0.4)
                    tap.sum(self, Point(self.x3, self.y3), "x-", 7, "n", delay=0.5)
                if self.beatnum == 45:
                    tap.sum(self, Point(self.x3, self.y1), "x-", 7, "n")
                    tap.sum(self, Point(self.x3, self.y2), "x-", 7, "n", delay=0.1)
                    tap.sum(self, Point(self.x3, self.y3), "x-", 7, "n", delay=0.2)
                    tap.sum(self, Point(self.x3, self.y1), "x-", 7, "n", delay=0.3)
                    tap.sum(self, Point(self.x3, self.y2), "x-", 7, "n", delay=0.4)
                    tap.sum(self, Point(self.x3, self.y3), "x-", 7, "n", delay=0.5)
                if self.beatnum == 46:
                    tap.sum(self, Point(self.x1, self.y3-self.thirdy), "n", 4, "s", dmg=5)
                    tap.sum(self, Point(self.x2, self.y3-self.thirdy), "n", 4, "s", dmg=5)
                    tap.sum(self, Point(self.x3, self.y3-self.thirdy), "n", 4, "s", dmg=5)
                if self.beatnum == 48:
                    tap.sum(self, Point(self.x1, self.y3), "y-", 30, "n", delay=0.3, dmg=10)
                    tap.sum(self, Point(self.x3, self.y3), "y-", 30, "n", delay=0.3, dmg=10)
                if self.beatnum == 49:
                    tap.sum(self, Point(self.x1, self.y1), "y+", 8, "n")
                    tap.sum(self, Point(self.x3, self.y1), "y+", 8, "n", delay=0.1)
                    tap.sum(self, Point(self.x1, self.y1), "y+", 8, "n", delay=0.2)
                    tap.sum(self, Point(self.x3, self.y1), "y+", 8, "n", delay=0.3)
                    tap.sum(self, Point(self.x1, self.y1), "y+", 8, "n", delay=0.4)
                    tap.sum(self, Point(self.x3, self.y1), "y+", 8, "n", delay=0.5)
                if self.beatnum == 50:
                    tap.sum(self, Point(self.x1, self.y1), "y+", 8, "n")
                    tap.sum(self, Point(self.x3, self.y1), "y+", 8, "n", delay=0.1)
                    tap.sum(self, Point(self.x1, self.y1), "y+", 8, "n", delay=0.2)
                    tap.sum(self, Point(self.x3, self.y1), "y+", 8, "n", delay=0.3)
                    tap.sum(self, Point(self.x1, self.y1), "y+", 8, "n", delay=0.4)
                    tap.sum(self, Point(self.x3, self.y1), "y+", 8, "n", delay=0.5)
                if self.beatnum == 51:
                    tap.sum(self, Point(self.x2, self.y2), "n", 4, "s", dmg=5)
                    tap.sum(self, Point(self.x2, self.y3-self.thirdy), "n", 4, "s", dmg=5)
                    tap.sum(self, Point(self.x2, self.y3), "n", 4, "s", dmg=5)
                if self.beatnum == 52:
                    tap.sum(self, Point(self.x1, self.y1), "y+", 8, "n")
                    tap.sum(self, Point(self.x3, self.y1), "y+", 8, "n", delay=0.1)
                    tap.sum(self, Point(self.x1, self.y1), "y+", 8, "n", delay=0.2)
                    tap.sum(self, Point(self.x3, self.y1), "y+", 8, "n", delay=0.3)
                    tap.sum(self, Point(self.x1, self.y1), "y+", 8, "n", delay=0.4)
                    tap.sum(self, Point(self.x3, self.y1), "y+", 8, "n", delay=0.5)
                if self.beatnum == 53:
                    tap.sum(self, Point(self.x1, self.y1), "y+", 8, "n")
                    tap.sum(self, Point(self.x3, self.y1), "y+", 8, "n", delay=0.1)
                    tap.sum(self, Point(self.x1, self.y1), "y+", 8, "n", delay=0.2)
                    tap.sum(self, Point(self.x3, self.y1), "y+", 8, "n", delay=0.3)
                    tap.sum(self, Point(self.x1, self.y1), "y+", 8, "n", delay=0.4)
                    tap.sum(self, Point(self.x3, self.y1), "y+", 8, "n", delay=0.5)
                if self.beatnum == 54:
                    tap.sum(self, Point(self.x2, self.y1), "n", 4, "s", dmg=5)
                    tap.sum(self, Point(self.x2, self.y1+self.thirdy), "n", 4, "s", dmg=5)
                    tap.sum(self, Point(self.x2, self.y2), "n", 4, "s", dmg=5)
                if self.beatnum == 56:
                    tap.sum(self, Point(self.x1, self.y2), "x+", 30, "n", delay=0.3, dmg=10)
                    tap.sum(self, Point(self.x2, self.y1), "y+", 30, "n", delay=0.3, dmg=10)
                    tap.sum(self, Point(self.x3, self.y2), "x-", 30, "n", delay=0.3, dmg=10)
                    tap.sum(self, Point(self.x2, self.y3), "y-", 30, "n", delay=0.3, dmg=10)
                if self.beatnum == 57:
                    tap.sum(self, Point(self.x1, self.y1), "y+", 8, "n")
                    tap.sum(self, Point(self.x3, self.y1), "y+", 8, "n", delay=0.1)
                    tap.sum(self, Point(self.x1, self.y1), "y+", 8, "n", delay=0.2)
                    tap.sum(self, Point(self.x3, self.y1), "y+", 8, "n", delay=0.3)
                    tap.sum(self, Point(self.x1, self.y1), "y+", 8, "n", delay=0.4)
                    tap.sum(self, Point(self.x3, self.y1), "y+", 8, "n", delay=0.5)
                if self.beatnum == 58:
                    tap.sum(self, Point(self.x1, self.y1), "y+", 8, "n")
                    tap.sum(self, Point(self.x3, self.y1), "y+", 8, "n", delay=0.1)
                    tap.sum(self, Point(self.x1, self.y1), "y+", 8, "n", delay=0.2)
                    tap.sum(self, Point(self.x3, self.y1), "y+", 8, "n", delay=0.3)
                    tap.sum(self, Point(self.x1, self.y1), "y+", 8, "n", delay=0.4)
                    tap.sum(self, Point(self.x3, self.y1), "y+", 8, "n", delay=0.5)
                if self.beatnum == 59:
                    tap.sum(self, Point(self.x2, self.y1), "n", 4, "s", dmg=5)
                    tap.sum(self, Point(self.x2, self.y3), "n", 4, "s", dmg=5)
                    tap.sum(self, Point(self.x1, self.y2), "n", 4, "s", dmg=5)
                    tap.sum(self, Point(self.x3, self.y2), "n", 4, "s", dmg=5)
                if self.beatnum == 60:
                    tap.sum(self, Point(self.x1, self.y3), "y-", 8, "n")
                    tap.sum(self, Point(self.x3, self.y3), "y-", 8, "n", delay=0.1)
                    tap.sum(self, Point(self.x1, self.y3), "y-", 8, "n", delay=0.2)
                    tap.sum(self, Point(self.x3, self.y3), "y-", 8, "n", delay=0.3)
                    tap.sum(self, Point(self.x1, self.y3), "y-", 8, "n", delay=0.4)
                    tap.sum(self, Point(self.x3, self.y3), "y-", 8, "n", delay=0.5)
                if self.beatnum == 61:
                    tap.sum(self, Point(self.x1, self.y3), "y-", 8, "n")
                    tap.sum(self, Point(self.x3, self.y3), "y-", 8, "n", delay=0.1)
                    tap.sum(self, Point(self.x1, self.y3), "y-", 8, "n", delay=0.2)
                    tap.sum(self, Point(self.x3, self.y3), "y-", 8, "n", delay=0.3)
                    tap.sum(self, Point(self.x1, self.y3), "y-", 8, "n", delay=0.4)
                    tap.sum(self, Point(self.x3, self.y3), "y-", 8, "n", delay=0.5)
                    
                
                if self.beatnum == 65:
                    self.gamemode = "sbox"
        if self.level == 6:
            self.bpm = 129
            self.tpm = 129
            if self.beaton == True:
                if self.beatnum == 3:
                    tap.over(self, "That's all a bit dramatic isn't it?", 3, size=20, retrig=True)
                if self.beatnum == 15:
                    tap.over(self, "Maybe a simple 'Hello!' would've\nbeen more appropriate.", 4, size=20, retrig=True)
                if self.beatnum == 33:
                    tap.sum(self, Point(self.x1, self.y1), "x+", 9, "n")
                    tap.sum(self, Point(self.x1, self.y3), "x+", 9, "n")
                if self.beatnum == 34:
                    tap.sum(self, Point(self.x3, self.y2), "x-", 9, "n", delay=0.2)
                if self.beatnum == 35:
                    tap.sum(self, Point(self.x1+self.thirdx, self.y3), "y-", 25, "n", dmg=5)
                    tap.sum(self, Point(self.x2, self.y3), "y-", 25, "n", dmg=5)
                    tap.sum(self, Point(self.x3-self.thirdx, self.y3), "y-", 25, "n", dmg=5)
                if self.beatnum == 36:
                    tap.sum(self, Point(self.x1, self.y1), "n", 6, "s", delay=0.2)
                    tap.sum(self, Point(self.x1, self.y2), "n", 6, "s", delay=0.2)
                    tap.sum(self, Point(self.x1, self.y3), "n", 6, "s", delay=0.2)
                    tap.sum(self, Point(self.x2, self.y3), "n", 6, "s", delay=0.2)
                    tap.sum(self, Point(self.x2, self.y1), "n", 6, "s", delay=0.3)
                    tap.sum(self, Point(self.x3, self.y1), "n", 6, "s", delay=0.3)
                    tap.sum(self, Point(self.x3, self.y2), "n", 6, "s", delay=0.3)
                    tap.sum(self, Point(self.x3, self.y3), "n", 6, "s", delay=0.3)
                if self.beatnum == 37:
                    tap.sum(self, Point(self.x1, self.y3), "x+", 30, "n")
                    tap.sum(self, Point(self.x1, self.y1), "x-", 30, "n")
                    tap.sum(self, Point(self.x1, self.y3), "y-", 30, "n", delay=0.3)
                    tap.sum(self, Point(self.x3, self.y1), "y+", 30, "n", delay=0.3)
                if self.beatnum == 38:
                    tap.sum(self, Point(self.x1, self.y2), "x+", 30, "n", delay=0.1)
                    tap.sum(self, Point(self.x3, self.y2), "x-", 30, "n", delay=0.1)
                if self.beatnum == 39:
                    tap.sum(self, Point(self.x1, self.y2), "n", 6, "s")
                    tap.sum(self, Point(self.x2, self.y2), "n", 6, "s")
                    tap.sum(self, Point(self.x3, self.y2), "n", 6, "s")
                    tap.sum(self, Point(self.x2, self.y3), "n", 6, "s")
                    tap.sum(self, Point(self.x2, self.y1), "n", 6, "s")
                if self.beatnum == 39:
                    tap.sum(self, Point(self.x1+self.thirdx, self.y2), "n", 8, "s", delay=0.3)
                if self.beatnum == 40:
                    tap.sum(self, Point(self.x3-self.thirdx, self.y2), "n", 8, "s", delay=0.2)
                if self.beatnum == 41:
                    tap.sum(self, Point(self.x1, self.y1), "r", 3, "s")
                    tap.sum(self, Point(self.x2, self.y1), "r", 3, "s")
                    tap.sum(self, Point(self.x3, self.y1), "r", 3, "s")
                    tap.sum(self, Point(self.x1, self.y3), "r", 3, "s")
                    tap.sum(self, Point(self.x2, self.y3), "r", 3, "s")
                    tap.sum(self, Point(self.x3, self.y3), "r", 3, "s")
                    tap.sum(self, Point(self.x1, self.y2), "r", 3, "s")
                    tap.sum(self, Point(self.x3, self.y2), "r", 3, "s")
                if self.beatnum == 42:
                    tap.sum(self, Point(self.x1, self.y1), "x+", 20, "n")
                    tap.sum(self, Point(self.x2, self.y1), "y+", 30, "n", delay=0.2)
                    tap.sum(self, Point(self.x3, self.y1), "x-", 20, "n")
                    tap.sum(self, Point(self.x1, self.y3), "x+", 20, "n")
                    tap.sum(self, Point(self.x2, self.y3), "y-", 30, "n", delay=0.2)
                    tap.sum(self, Point(self.x3, self.y3), "x-", 20, "n")
                if self.beatnum == 43:
                    tap.sum(self, Point(self.x1, self.y2+self.thirdy), "r", 3, "s")
                    tap.sum(self, Point(self.x3, self.y2+self.thirdy), "r", 3, "s")
                    tap.sum(self, Point(self.x1, self.y2-self.thirdy), "r", 3, "s")
                    tap.sum(self, Point(self.x3, self.y2-self.thirdy), "r", 3, "s")
                if self.beatnum == 194:
                    self.level = 7
                
        if self.level == 7:
            # TODO seperate 6 and 7 music
            self.bpm = 129
            self.tpm = 129
            if self.beaton == True:
                if self.beatnum == 96:
                    self.level = 0
                
                

        self.beatnum -= 1
        
        self.bpm = 60.0/self.bpm
        self.tpm = 60.0/self.tpm

    def sbox(self, level):
        if level == 5:
            #audio
            if self.sbid == None:
                self.sbid = play_effect('lost1', 1, 1)
                self.sbt = time()
            if self.sbt+75 <= time():
                tap.setup(self)
                
            #visuals
            if self.sbt+3 > time():
                if random() > (time()-self.sbt)/16:
                    self.ttint = 3
                    fill(1, 1, 1, 1)
                    rect(self.tloc.x-40, self.tloc.y-40, 80, 80)
                    tint(0, 0, 0, 1)
                    text(str(self.health), 'AvenirNext-Regular', 25, self.tloc.x, self.tloc.y)
                else:
                    self.health = randint(1, self.health)
                    play_effect('glitch1', 0.5, 1)
                    fill(random(), random(), random(), 1)
                    rect(self.tloc.x-40+randint(-10, 10), self.tloc.y-40+randint(-10, 10), 80+randint(-10, 10), 80+randint(-10, 10))
                    tint(1, 1, 1, 1)
                    text(str(self.health), 'AvenirNext-Regular', 25, self.tloc.x, self.tloc.y)
            elif self.ttint > 0:
                if self.ttint == 3:
                   play_effect('glitch3', 1, 0.7)
                self.ttint -= 1
                fill(random(), random(), random(), 1)
                rect(self.tloc.x-40+randint(-10, 10), self.tloc.y-40+randint(-10, 10), 80+randint(-10, 10), 80+randint(-10, 10))
                tint(1, 1, 1, 1)
                text("0", 'AvenirNext-Regular', 25, self.tloc.x, self.tloc.y)
            elif self.sbt+3.5 < time():
                if random() < curve_ease_in((time()-self.sbt)/50.0)+0.1:
                    self.sbinc += 4+(self.sbinc2*7)
                if time()-self.sbt > 30:
                    self.sbinc2 += 1/500.0
                if random() > 0.9:
                    bump = randint(-50, 50)
                    bump2 = randint(-50, 50)
                    if random() > 0.98:
                        bump3 = randint(-2, 2)
                        bump2 -= bump3*5
                    else:
                        bump3 = 0
                else:
                    bump, bump2, bump3 = 0, 0, 0
                if random() > 0.9:
                    tint(1, 1, 1, random()-(time()-self.sbt)-4)
                else:
                    tint(1, 1, 1, (time()-self.sbt)-4)
                text(self.sb5text[:int(round(self.sbinc))], 'AvenirNext-UltraLight', 8+bump3, 0+bump, self.bounds.top()+bump2+(curve_ease_in(curve_ease_in(self.sbinc2))*600), 3)

                
            
            if time()-self.sbt > 50:
                self.tloc = Point(*self.bounds.center().as_tuple())
                self.gamemode = 'outro'




    def glitch(self):
        temp1 = randint(0, 500)
        temp2 = randint(0, 500)
        temp3 = randint(0, 500)
        temp4 = randint(0, 500)
        fill(random(), random(), random(), random())
        rect(temp1, temp2, temp3, temp4)
        rect(temp1+randint(-10, 10), temp2+randint(-10, 10), temp3+randint(-20, 20), temp4+randint(-20, 20))
        temp1 = randint(0, 500)
        temp2 = randint(0, 500)
        temp3 = randint(0, 500)
        temp4 = randint(0, 500)
        fill(random(), random(), random(), random())
        rect(temp1, temp2, temp3, temp4)
        rect(temp1+randint(-10, 10), temp2+randint(-10, 10), temp3+randint(-20, 20), temp4+randint(-20, 20))
    
            
            
            
        
    def outro(self):
        if not self.sbt+70 <= time():
            fill(0, 0, 0)
            #visuals
            if random() >= 0.95:
                self.jumpx, self.jumpy = randint(-50, 50), randint(-50, 50)
                play_effect(choice(["glitch1", "glitch2", "glitch3"]))
                fill(random(), random(), random())
                rect(self.bounds.center().x-50+self.jumpx, self.bounds.center().y-50+self.jumpy, 100, 100)
                fill(0, 0, 0)
                rect(self.bounds.center().x-50, self.bounds.center().y-50, 100+(self.jumpx/2), 100+(self.jumpy/2))
                
            else:
                self.jumpx, self.jumpy = 0, 0
                rect(self.bounds.center().x-50, self.bounds.center().y-50, 100, 100)
                
                
            if self.ttint <= 1.999 and time()-self.sbt > 56:
                self.ttint +=0.001
                
            tint(1, 1, 1, self.ttint)
            text("I am", 'AvenirNext-UltraLightItalic', 32,  self.bounds.center().x, self.bounds.center().y)
            
        else:
            lux = curve_ease_in(curve_ease_in(1-self.ttint))
            fill(lux, lux, lux)
            #visuals

            self.jumpx, self.jumpy = 0, 0
            rect(self.bounds.center().x-40+(self.ttint*10), self.bounds.center().y-40+(self.ttint*10), 80+(self.ttint*20), 80+(self.ttint*20))
                
                
            if self.ttint > 0:
                self.ttint -= 0.01
                
            tint(1, 1, 1, self.ttint)
            text("I am", 'AvenirNext-UltraLightItalic', 32,  self.bounds.center().x, self.bounds.center().y)
            if self.sbt+72 <= time():
                self.tloc = Point(*self.bounds.center().as_tuple())
                self.health = 150
                self.gamemode = "main"
                self.level = 6


    def over(self, string, timeing, size=20, retrig=False):
        if retrig == True:
            self.oretrig = [string, timeing, size]
            self.oinc = 0
        if self.oinc > 2:
            self.oretrig = False
        
        self.oinc += 1.0/(timeing*60)
        ind = int(round(self.oinc, 2)*(len(string)*2))
        if ind > len(string):
            tint(1, 1, 1, 1.8+(random()/2)-self.oinc)
        else:
            tint(1, 1, 1, 1-(random()/2))
        text(string[:ind] + string[randint(0, len(string)-1)], 'AvenirNext-UltraLightItalic', size, 0, 100, 3)
        
    def geekmode(self):
        if random() >= 0.2:
            self.fps = round(1/self.dt, 3)
        
        if self.gamemode == "main":
            tint(1, 1, 1, 1)
            text("beat: " + str(self.beatnum), 'AvenirNext-Regular', 15, self.bounds.left(), self.bounds.bottom()+15, 6)
            text("domenu: " + str(self.domenu), 'AvenirNext-Regular', 15, self.bounds.left(), self.bounds.bottom()+30, 6)
            text("fps: " + str(self.fps), 'AvenirNext-Regular', 15, self.bounds.left(), self.bounds.bottom()+60, 6)
            text("objects: " + str(len(self.obst)), 'AvenirNext-Regular', 15, self.bounds.left(), self.bounds.bottom()+45, 6)
        elif self.gamemode == "menu":
            tint(0, 0, 0, 1)
            text("fps: " + str(self.fps), 'AvenirNext-Regular', 15, self.bounds.left(), self.bounds.top()-15, 6)
            text("velocity: " + str(self.velocity), 'AvenirNext-Regular', 15, self.bounds.left(), self.bounds.top()-30, 6)
            text("textpos: " + str(self.textpos-self.bounds.center().y), 'AvenirNext-Regular', 15, self.bounds.left(), self.bounds.top()-45, 6)
            text("jump: " + str(self.jumpx) + ", " + str(self.jumpy), 'AvenirNext-Regular', 15, self.bounds.left(), self.bounds.top()-60, 6)
        elif self.gamemode == "intro":
            tint(1, 1, 1, 1)
            text("ttint: " + str(self.ttint), 'AvenirNext-Regular', 15, self.bounds.left(), self.bounds.bottom()+15, 6)
            text("first: " + str(self.first), 'AvenirNext-Regular', 15, self.bounds.left(), self.bounds.bottom()+30, 6)
            text("fps: " + str(self.fps), 'AvenirNext-Regular', 15, self.bounds.left(), self.bounds.bottom()+45, 6)
        elif self.gamemode == "trans":
            tint(1, 0, 0, 1)
            text("ttint: " + str(self.ttint), 'AvenirNext-Regular', 15, self.bounds.left(), self.bounds.top()-15, 6)
            text("pos: " + str(self.textpos), 'AvenirNext-Regular', 15, self.bounds.left(), self.bounds.top()-30, 6)
            text("inc: " + str(self.inc), 'AvenirNext-Regular', 15, self.bounds.left(), self.bounds.top()-45, 6)
            text("inc1: " + str(self.inc1), 'AvenirNext-Regular', 15, self.bounds.left(), self.bounds.top()-60, 6)
            text("fps: " + str(self.fps), 'AvenirNext-Regular', 15, self.bounds.left(), self.bounds.top()-75, 6)
        elif self.gamemode == "sbox":
            tint(1, 1, 1, 1)
            text("sbtint: " + str(self.sbtint), 'AvenirNext-Regular', 15, self.bounds.left(), self.bounds.bottom()+15, 6)
            text("sbtime: " + str(time()-self.sbt), 'AvenirNext-Regular', 15, self.bounds.left(), self.bounds.bottom()+30, 6)
            

            
            
            
        
run(tap(), orientation=PORTRAIT)





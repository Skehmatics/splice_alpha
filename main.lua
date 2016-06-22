require 'math'
class = require 'bin/class' --literally why
random = math.random
require 'bin/TEsound'
sound = TEsound --Idk why we have to do it this way, but it doesnt work when we do it the right way.
gamestate = require 'bin/gamestate'
timer = require 'bin/timer'
ser = require 'bin/ser'
shine = require 'bin/shine'


--Classes

Rect = class{
	init = function(self,x,y,w,h)
		self.x = x
		self.y = y
		self.w = w
		self.h = h
	end}

	function Rect:contains(x,y)
		return (x>self.x and x<self.x+self.w) and (y>self.y and y<self.y+self.h)
	end

	function Rect:collides(OR)
		return self.x < OR.x+OR.w and
	         OR.x < self.x+self.w and
	         self.y < OR.y+OR.h and
	         OR.y < self.y+self.h
	end

LEVEL = class{
	init = function(self, levelnumber)
		local data = require('levels/level' .. tostring(levelnumber))
		self.load = data.load
		self.events = data.events
		self.draw = data.draw

		self.bpm = data.bpm
		self.name = data.name
		self.spb = 60/self.bpm
	end
}

obj = class{
	init = function(self, x, y, type, speed, delay, damage, size)
		size = size or scale(30)
		self.box = {x=x-(size/2), y=y-(size/2), w=size, h=size}
		self.speed = (speed or 1)/4
		self.type = type or 's'
		self.damage = damage or 10
		self.tweens = {ttl = 1.5, offset={x=0, y=0}, fade=0, visibility=1}
		self.benign = false

		self.target = {}
		local positive = not (self.type:match('+') == nil)
		if self.type:match('x') then
			self.target.x = positive and gamebounds.endx or gamebounds.x-self.box.w
			self.box.x =  (positive and gamebounds.x or gamebounds.endx)-(self.box.w/2)
			self.tweens.offset.x = (positive and 1 or -1) * scale(20)
		elseif self.type:match('y') then
			self.target.y = positive and gamebounds.endy or gamebounds.y-self.box.h
			self.box.y = (positive and gamebounds.y or gamebounds.endy)-(self.box.h/2)
			self.tweens.offset.y = (positive and 1 or -1) * scale(20)
		end

		self.dead = false
		self.active = false
		self.waiting = false
		if delay == -1 then
			self:fire()
		else
			timer.after(delay and level.spb*delay or 0, function()
				self.waiting = true
				timer.tween(level.spb*1, self.tweens, {ttl = 0}, 'out-expo', function()
					self:fire()
				end)
				timer.tween(level.spb*1, self.tweens, {fade=1, offset={x=0, y=0}}, 'out-quad')
			end)
		end
	end}

	function obj:arm(collision)
		if self.type:match('s') then --stationary--

		end

		if self.type:match('r') then

		end

		fill(1, 1, 1, self.tweens.fade-clamp(self.tweens.fade-0.75, 0, 1)*4)
		if self.type:match('x') then --x/y axis--
			stroke(self.tweens.ttl*scale(30))
			line(gamebounds.x, self.box.y+(self.box.h/2), gamebounds.endx, self.box.y+(self.box.h/2))
		elseif self.type:match('y') then
			stroke(self.tweens.ttl*scale(30))
			line(self.box.x+(self.box.w/2), gamebounds.y, self.box.x+(self.box.w/2), gamebounds.endy)
		end

		if collision then
			fill(1, 0, 0, self.tweens.fade)
		else
			fill(1, 1, 1, self.tweens.fade)
		end
		rect(self.box.x-self.tweens.offset.x, self.box.y-self.tweens.offset.y, self.box.w, self.box.h)
	end

	function obj:travel(collision)
		if collision and not self.benign then
			player.health = player.health - self.damage
			sound.play({'sfx/whine1.ogg', 'sfx/whine2.ogg','sfx/whine3.ogg','sfx/whine4.ogg','sfx/whine5.ogg'}, 'sfx', 0.25, math.random()/2+1)
			impact={radius=self.damage*3, angle=math.random(0, 360)}
			timer.tween(0.3, impact, {radius=0}, 'out-expo', function()
			end)
			if self.type:match('f') then
				self.benign = true
				timer.after(level.spb - tpassed, function()
					self.benign = false
				end)
			else
				self.dead = true
			end
		end


		if self.type:match('f') then
			self.tweens.visibility = 1-tweens.ttint
		end

		if self.type:match('s') then
			fill(math.random(), math.random(), math.random(), self.tweens.visibility)
		else
			fill(1, 1, 1, self.tweens.visibility)
		end

		if self.type:match('r') then
			self.box.x = self.box.x + math.random(-self.box.w, self.box.w)*5*love.timer.getDelta()
			self.box.y = self.box.y + math.random(-self.box.h, self.box.h)*5*love.timer.getDelta()
		end

		rect(self.box.x, self.box.y, self.box.w, self.box.h)
	end

	function obj:fire()
		if self.type:match('s') then
			self.tweens.fade = 1
			timer.tween((level.spb/self.speed)-love.timer.getAverageDelta(), self.tweens, {visibility = 0}, 'linear', function()
				self.dead = true
			end)
		else
			timer.tween((level.spb/self.speed)-love.timer.getAverageDelta(), self.tweens, {visibility = 0}, 'in-expo')
			timer.tween((level.spb/self.speed)-love.timer.getAverageDelta(), self.box, self.target, 'linear', function()
				self.dead = true
			end)
		end
		self.active = true
	end


	function obj:draw()
		local collision = Rect(self.box.x, self.box.y, self.box.w, self.box.h):collides(Rect(player.x-player.w/2, player.y-player.h/2, player.w, player.h)) and self.tweens.visibility > 0.3
		if self.dead then
			return false
		elseif self.active then
			self:travel(collision)
		elseif self.waiting then
			self:arm(collision)
		end
		return true
	end

	function spawn(x, y, objtype, speed, delay, damage, size)
		table.insert(objects, obj(x, y, objtype, speed, delay, damage, size))
	end


--Handy Functions
function scale(x)
	return x*scalefactor
end

function len(T)
  local count = 0
  for _ in pairs(T) do count = count + 1 end
  return count
end

function clamp(val, lower, upper)
    return math.max(lower, math.min(upper, val))
end

function save()
	love.filesystem.write('save', ser(savedata))
end

function clip(x, y, w, h)
	love.graphics.setScissor(x, y, w, h)
end

function contains (tab, val)
    for index, value in ipairs (tab) do
        if value == val then
            return true
        end
    end
    return false
end

function dialog(file)
	timer.tween(0.1, _G, {volume = 0.75})
	sound.play(file, 'dialog', 1, 1, function()
		timer.tween(0.25, _G, {volume = 1})
	end)
end


--bunch of helpers to make the porting from Scene to LOVE easier

function rect(x, y, w, h)
	love.graphics.rectangle('fill', x, y, w, h)
end

function line(...)
	love.graphics.line(...)
end

function stroke(weight)
	love.graphics.setLineWidth(weight)
end

function text(str, typeface, size, x, y, align)
	size = size/150
	local width = typeface:getWidth(str)*scale(size)
	local height = typeface:getHeight()*scale(size)
	align = align or 5

	if contains({3, 6, 9}, align) then
		x = x-width
	elseif contains({2, 5, 8}, align) then
		x = x-(width/2)
	end

	if contains({1, 2, 3}, align) then
		y = y-height
	elseif contains({4, 5, 6}, align) then
		y = y-(height/2)-scale(5)
	end
	typeface = typeface or regualr
	love.graphics.setFont(typeface)
	love.graphics.print(str, x, y, nil, scale(size))
end

function fill(r, g, b, a)
	a=a or 1
	a= a<0 and 0 or a>1 and 1 or a
	love.graphics.setColor(r*255, g*255, b*255, a*255)
end

function draw(...)
	love.graphics.draw(...)
end

function background(drawable)
	draw(drawable, 0, 0, 0, bounds.w/drawable:getWidth(), bounds.h/drawable:getHeight())
end


 --Menu

MENU = {}

	function MENU:enter(current, trans, reset)
		if reset then
			--Music
			sound.stop('music')
			if savedata.alive then
				--TODO: Wont loop for some reason??
				sound.playLooping({ "music/ambiance1.ogg", "music/ambiance2.ogg", "music/ambiance3.ogg" }, 'music', 0.5)
			end

			--Variable Init
			timershift = timer.new()
			tweens = {tint=0, volume=1, hidden=0}
			canceling = false
			cancelable = false
			velocity = 0
			textpos = bounds.center.y
			levelnum = 1
			shift = 0
			selector={x=bounds.center.x-scale(50), y=bounds.center.y-scale(50), w=scale(100), h=scale(100)}

			--Animation
			if savedata.unlocked == 1 and savedata.firstrun == true then
				timer.tween(10, tweens, {tint=2}, 'out-in-quad')
			else
				timer.tween(1, tweens, {tint=2}, 'linear')
			end
		else
			timer.tween(1, tweens, {tint=2, volume=1, hidden=0}, 'in-quad')
			timer.tween(0.5, selector, {x=bounds.center.x-scale(50), y=bounds.center.y-scale(50), w=scale(100), h=scale(100)}, 'out-expo')
		end
		if trans then
			cancelable = true
			timer.clear()
			timer.tween(1.5, tweens, {tint=-1}, 'linear')
			timer.tween(1, _G, {textpos=bounds.center.y-((levelnum-1)*scale(90))}, 'out-expo')
			timer.after(0.75, function()
				timershift:tween(2.5, selector, { x=-(bounds.h > bounds.w and bounds.h or bounds.w)/2, y=-(bounds.h > bounds.w and bounds.h or bounds.w)/2, w=(bounds.h > bounds.w and bounds.h or bounds.w)*2, h=(bounds.h > bounds.w and bounds.h or bounds.w)*2 }, function(t) return timer.tween.quart(timer.tween.quart(t)) end)
				timershift:tween(2.5, tweens, {volume = 0}, 'in-expo', function()
					gamestate.pop()
					gamestate.switch(TRANS, false)
				end )
			end)
			timer.tween(2.5, tweens, {hidden = 1}, 'in-quad')
		end
	end

	function MENU:update(dt)
		if math.abs(velocity) < 0.01 then
			velocity = 0
		end
		sound.volume('music', volume*tweens.volume)
		timershift:update(canceling and 0 or dt)
	end

	function MENU:draw()

		--Background
		fill(1, 1, 1)
		rect(bounds.x, bounds.y, bounds.w, bounds.h)
		background(white)

		--Visuals
		fill(0, 0, 0)
		if random() >= 0.998-(2/250) and savedata.alive then
			local jumpx, jumpy = random(-50, 50), random(-50, 50)
			sound.play({ "sfx/glitch1.ogg", "sfx/glitch2.ogg", "sfx/glitch3.ogg" }, 'sfx', 2, (random()/15)+0.95)
			fill(random(), random(), random())
			rect(selector.x-scale(jumpx), selector.y-scale(jumpy), selector.w, selector.h)
			fill(0, 0, 0)
			rect(selector.x, selector.y, selector.w + scale(jumpx/2), selector.h + scale(jumpy/2))
		else
			local jumpx, jumpy = 0, 0
			if random() >= 0.993 then
				fill(random(), random(), random())
			end
			rect(selector.x, selector.y, selector.w, selector.h)
		end

		fill(0, 0, 0, tweens.tint-1)
		text((isMobile and "Touch" or "Click") .. " the square to start.", UltraLight, 25, bounds.center.x, bounds.h-scale(20))
		if not isMobile and savedata.firstrun then
			text("ESC to quit, F11 for fullscreen", Light, 15, scale(5), 0, 7)
		end

		if savedata.unlocked > 1 then
			text((isMobile and "Slide " or "Drag") .. " vertically to select level.", UltraLight, 20, bounds.center.x, bounds.h-scale(40))
			fill(0, 0, 0, tweens.hidden)
			text((isMobile and "Slide " or "Drag") .. " vertically to cancel.", UltraLight, 20, bounds.center.x, bounds.h-scale(40))
		end

		--Selector
		fill(1, 1, 1, tweens.tint)
		clip(selector.x, selector.y, selector.w, selector.h)
		for i=0,savedata.unlocked-1 do
			lvl = i<1 and "Splice" or "Level " .. tostring(i+1)
			pos = i*scale(90)
			text(lvl, UltraLightItalic, 32,  bounds.center.x, textpos+pos)
			if math.abs(bounds.center.y-(textpos+pos)) < scale(40) then
				levelnum = i+1
			end
		end

		if textpos <= bounds.center.y and textpos >= bounds.center.y-((savedata.unlocked-1)*scale(90)) then
			if len(love.touch.getTouches()) == 0 and not love.mouse.isDown(1) then
				textpos = textpos + velocity
				velocity = velocity - (velocity/10)
			end
		else
			velocity = velocity - (velocity/5)
			fill(random(), random(), random(), random())
			sound.play("sfx/glitch3.ogg", 'sfx', math.abs(velocity/10))
			if bounds.center.y-textpos < 50 then
				textpos = bounds.center.y
				text("Splice", UltraLightItalic, 32, bounds.center.x, bounds.center.y-scale(random(velocity/2)))
			else
				textpos = bounds.center.y-((savedata.unlocked-1)*scale(90))
				text("Level " .. tostring(levelnum), UltraLightItalic, 32,  bounds.center.x, bounds.center.y-scale(random(velocity/2)))
			end
		end
		clip()
	end

	function MENU:leave()
		sound.stop('music')
		love.resize()
	end

	function MENU:touchpressed(id, x, y)
		if cancelable then canceling = true end
	end

	function MENU:touchmoved(id, x, y, dx, dy)
		if savedata.unlocked > 1 then
			if dy > 5 or dy < -5 then
				velocity = dy
			else
				velocity = 0
			end
			if not canceling then textpos = textpos + dy end
		shift = dy
		end

		if canceling and velocity < -5 then
			timershift:clear()
			timer.clear()
			canceling = false
			cancelable = false
			gamestate.push(MENU, false, false)
		end
	end


	function MENU:touchreleased(id, x, y)
		if Rect(selector.x, selector.y, selector.w, selector.h):contains(x, y) and tweens.tint >= 0.4 and not cancelable then
			gamestate.push(MENU, true, false)
			sound.play("sfx/intro.ogg", 'sfx', 1, 1+((levelnum-1)/100))
		end
		canceling = false

	end

--Warmup

TRANS = {}

	function TRANS:enter(current, fast)
		--Init variables
		tweens = {ttint=0, squarefill=0, alpha=0}

		--Animation
		timer.tween(fast and 2 or 5, tweens, {ttint=2, alpha=2}, 'linear')

		timer.after(fast and 0 or 5, function()
			timer.tween(2, tweens, {squarefill=1}, 'in-out-quad', function()
				gamestate.switch(GAME, levelnum, true)
				fast = true
			end )
		end)
	end

	function TRANS:draw()
					fill(1, 1, 1, tweens.alpha)
					background(black)
					fill(1, 1, 1, tweens.ttint)

					if not fast then
						text("This game is unfinished", Italic, 26, 0, scale(60), 4)
						fill(1, 1, 1, tweens.ttint-0.5)
						text("Bugs are to be expected.", Italic, 26, 0, scale(80), 4)
						fill(1, 1, 1, tweens.ttint-0.75)
						text("More levels and story soon!", Italic, 20, 0, scale(100), 4)
						text("By Derek Schmidt (@skehmatics).", UltraLight, 15, 0, bounds.h, 1)
						text("Special thanks to Tim Kahn for his assets.", UltraLight, 15, 0, bounds.h-scale(15), 1)
						fill(1, 1, 1, tweens.ttint-1)
					end
					text("Hold outside the game area" .. (isMobile and " " or " or press home ") .. "to return.", UltraLight, 20, bounds.center.x, bounds.center.y+scale(60))
					fill(1, 1, 1, tweens.squarefill)
					rect(bounds.center.x-scale(40), bounds.center.y-scale(40), scale(80), scale(80))
	end

--Main Game

GAME = {}
	function GAME:enter(current, to, reset)
		if reset then
			player = {x=bounds.center.x, y=bounds.center.y, w=scale(80), h=scale(80), health=100}
			objects = {}
		end
		tweens = {ttint=1, ltint=1, trans = 0}
		timer.tween(2, tweens, {ltint=0}, 'in-expo')
		player.health = player.health + 50
		beatnum = 0
		level = LEVEL(to)
		levelnum = to
		level:load()
		tpassed = level.spb
	end

	function GAME:update(dt)
		tpassed = tpassed + dt
		if tpassed >= level.spb then
			tpassed = tpassed - level.spb
			beatnum = beatnum + 1
			tweens.ttint = 1
			timer.tween(level.spb, tweens, {ttint=0}, 'in-quad')
			level:events(beatnum+1)
		end
		sound.volume('music', (1-(tweens.trans or 0))*volume)

		if player.health <= 0 then
			if not once then
				once=true
				timer.after(0.1, function()
					gamestate.switch(OVER)
					once = false
				end)
			end
		end
		printshake.radius = impact.radius
		printshake.angle = impact.angle
	end

	function GAME:draw()
		love.graphics.translate((math.cos(impact.angle) * impact.radius / bounds.w)*5, (math.sin(impact.angle) * impact.radius / bounds.h)*5)
		printshake:draw(function()
			fill(1, 1, 1, 1)
			background(black)
			level:draw(beatnum)

			fill(1, 1, 1, 0.2)
			stroke(2)
			line(gamebounds.x, gamebounds.y, gamebounds.endx, gamebounds.y, gamebounds.endx, gamebounds.endy, gamebounds.x, gamebounds.endy, gamebounds.x, gamebounds.y)

			fill(1, 1, 1, tweens.ltint)

			text(level.name, UltraLightItalic, 28, bounds.center.x, bounds.h - (bounds.center.y*tweens.ltint))

			fill(1, 1, 1, tweens.ttint)
			text("Beat " .. tostring(beatnum), UltraLight, 25, scale(5), bounds.h-scale(20), 4)
			rect(player.x-(player.h/2), player.y-(player.w/2), player.w, player.h)
			fill(0, 0, 0, tweens.ttint)
			text(tostring(player.health), Regular, 25, player.x, player.y)
			local test = objects
			fill(0, 0, 1, 1)
			for i=#test,1,-1 do
				local isActive = test[i]:draw()
				if not isActive then
					table.remove(objects, i)
				end
			end
			if tweens.trans > 0 then
				fill(1, 1, 1, tweens.trans)
				background(white)
				fill(0, 0, 0, tweens.trans)
				rect(selector.x, selector.y, selector.w, selector.h)
			end
		end)
	end

	function GAME:touchpressed(id, x, y)
		if transition then
			timer.cancel(transition)
		end

		if not Rect(gamebounds.x, gamebounds.y, gamebounds.w, gamebounds.h):contains(x, y) then
			transition = timer.tween(3, tweens, {trans=1}, 'linear', function()
				gamestate.switch(MENU, false, true)
			end)
		elseif (tpassed <= level.spb/5.0 or tpassed >= level.spb-(level.spb/5.0)) then
			sound.play("sfx/glitch3.ogg", 'sfx', 1, (random()/5)+0.9)
			player.x, player.y = x, y
			player.health = player.health + 5
		else
			sound.play("sfx/glitch1.ogg", 'sfx', 1, 0.60)
			player.health = player.health - 20
		end
	end

	function GAME:touchreleased(id, x, y)
		if transition then
			timer.cancel(transition)
			timer.tween(0.5, tweens, {trans=0}, 'out-quad')
		end
	end

	function GAME:keypressed(key)
		if key == "home" then
			transition = timer.tween(1, tweens, {trans=1}, 'linear', function()
				gamestate.switch(MENU, false, true)
			end)
		end
	end

--Game Over screen

OVER = {}
	function OVER:enter(current)
		sound.play('music/splice0.ogg', 'sfx', 0.5)
		tweens = {heavenHell = 0, fade = 1, pitch=1}
		touchallowed=false
		gotimer = timer.new()
		timer.tween(1.5, tweens, {fade=0}, 'in-quad', function()
			touchallowed=true
			OVER:touchreleased(nil, nil, nil)
		end)
		timer.tween(2, tweens, {pitch=0.01}, 'in-circ', function()
			sound.stop('music')
			tweens.pitch = 1
		end)
	end

	function OVER:update(dt)
		sound.pitch('music', tweens.pitch)
		gotimer:update(dt)
	end

	function OVER:draw()
		fill(1, 1, 1, 1)
		background(white)
		fill(0, 0, 0, tweens.fade)
		text("Game Over", UltraLight, 50, bounds.center.x, bounds.center.y)
		fill(0, 0, 0, tweens.heavenHell)
		rect(selector.x, selector.y, selector.w, selector.h)
		fill(1, 1, 1, tweens.heavenHell*-1)
		background(black)
		fill(1, 1, 1, tweens.heavenHell*-1)
		rect(bounds.center.x-(player.w/2), bounds.center.y-(player.h/2), player.w, player.h)

	end

	function OVER:touchpressed(id, x, y)
		if touchallowed then
			gotimer:clear()
			gotimer:tween(math.abs(-tweens.heavenHell-1), tweens, {heavenHell=-1}, 'in-out-sine', function()
				touchallowed = false
				sound.play('music/splice-1.ogg', 'music', 0.7, 1, function ()
					gamestate.switch(GAME, levelnum, true)
				end)
			end)
		end
	end

	function OVER:touchreleased(id, x, y)
		if touchallowed then
			gotimer:clear()
			gotimer:tween(math.abs(clamp(tweens.heavenHell-1, -1, 1))*4, tweens, {heavenHell = 1}, 'in-out-quad', function()
				gamestate.switch(MENU, false, true)
			end)
		end
	end




function love.load(arg)
	--make sure our first number is actually "random" for the sake of menu music
	math.randomseed(os.time())
	random()

	--Read saved data
	if love.filesystem.exists("save") then
		savedata = love.filesystem.load("save")()
	else
		--initilize
		savedata = {
			--user preferences
			msaa = 4,
			highres = false,
			vsync=true,
			fullscreen=true,
			--game data
		 	firstrun = true,
			alive = false,
			unlocked = 1
		}
		save()
	end

	--put preferences to use
	white = love.graphics.newImage(savedata.highres and 'textures/almostwhite2.png' or 'textures/almostwhite.png')
	black = love.graphics.newImage(savedata.highres and 'textures/almostblack2.png' or 'textures/almostblack.png')
	love.window.setMode(0, 0, {msaa=savedata.msaa, fullscreen=savedata.fullscreen, vsync=savedata.vsync, resizable=true})


	--initilize some data
	isMobile = contains({"Android", "iOS"}, love.system.getOS())
	love.resize()
	volume = 1
	objects = {}
	impact = {radius=0, angle=0}

	--Render fonts
	UltraLight = love.graphics.newFont('font/AvenirNextLTPro-Ultralight.otf', 150)
	UltraLightItalic = love.graphics.newFont('font/AvenirNextLTPro-UltralightItalic.otf', 150)
	thin = love.graphics.newFont('font/AvenirNextLTPro-Thin.otf', 150)
	ThinItalic = love.graphics.newFont('font/AvenirNextLTPro-ThinItalic.otf', 150)
	Light = love.graphics.newFont('font/AvenirNextLTPro-Light.otf', 150)
	LightItalic = love.graphics.newFont('font/AvenirNextLTPro-LightItalic.otf', 150)
	Regular = love.graphics.newFont('font/AvenirNextLTPro-Regular.otf', 150)
	Italic = love.graphics.newFont('font/AvenirNextLTPro-Italic.otf', 150)

	--load shaders
	printshake = shine.separate_chroma()

	--initilize and switch states
	gamestate.registerEvents()
	gamestate.switch(MENU, false, true)
end


function love.resize()
	local width = love.graphics.getWidth()
	local height = love.graphics.getHeight()
	bounds = { x=0, y=0, w=width, h=height, center={ x=width/2, y=height/2 }}
	scalefactor = bounds.h < bounds.w and (bounds.h / 480) or (bounds.w / 480)

	--Determines grid
	grid = {}
	local boxlen = (bounds.h < bounds.w and bounds.h or bounds.w)
	local portion =  boxlen /3
	local half = portion/2
	local xoffset = bounds.center.x - (boxlen/2)
	grid.x1 = portion - half + xoffset
	grid.x2 = (portion*2) - half + xoffset
	grid.x3 = (portion*3) - half + xoffset

	grid.third = half

	local yoffset = bounds.center.y - (boxlen/2)
	grid.y1 = portion - half + yoffset
	grid.y2 = (portion*2) - half + yoffset
	grid.y3 = (portion*3) - half + yoffset


	selector={x=bounds.center.x-scale(50), y=bounds.center.y-scale(50), w=scale(100), h=scale(100)}
	gamebounds = {x=xoffset, y=yoffset, w=boxlen, h=boxlen, center={x=xoffset+(boxlen/2), y=yoffset+(boxlen/2)}, endx=xoffset+boxlen, endy=yoffset+boxlen}
	if player then
		player = {x=bounds.center.x, y=bounds.center.y, w=scale(80), h=scale(80), health=player.health}
	end
end

function love.update(dt)
	sound.volume('music', volume)
	sound.cleanup()
	timer.update(dt)
end

function love.mousepressed(x, y, button, istouch)
	if not istouch and button == 1 then
		love.touchpressed(nil, x, y)
	end
end

function love.mousemoved(x, y, dx, dy, istouch)
	if love.mouse.isDown(1) and not istouch then
		love.touchmoved(nil, x, y, dx, dy)
	end
end

function love.mousereleased(x, y, button, istouch)
	if not istouch then
		love.touchreleased(nil, x, y)
	end
end

function love.keypressed(key, scancode, isrepeat)
	if key == "escape" then
		love.event.quit()
	elseif key == "f11" then
		love.window.setFullscreen(not love.window.getFullscreen())
	end
end


return _G

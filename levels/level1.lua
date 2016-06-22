local main = require 'main'
local fill = main.fill
local text = main.text
local scale = main.scale
local sum = main.spawn
local bounds = main.bounds
-- local grid = main.grid

local level = {}

level.lvlnum = 1
level.bpm = 128

level.name = "Level " .. tostring(level.lvlnum)
level.soundname = "splice" .. tostring(level.lvlnum)

function level:load()
	anim = {texttint = 0}
	main.timer.tween(5, anim, {texttint = 3})
	if level.lvlnum > main.savedata.unlocked then main.savedata.unlocked = level.lvlnum end
	main.save()
	main.sound.play('music/' .. level.soundname .. '.ogg', 'music')
end

function level:draw(t)
	if t <= 16 then
		fill(1, 1, 1, anim.texttint)
		text(main.isMobile and "Tap" or "Click" .. " anywhere", main.UltraLight, 20, bounds.center.x, bounds.center.y-scale(60))
		fill(1, 1, 1, anim.texttint-1)
		text("but only with the music.", main.UltraLight, 20, bounds.center.x, bounds.center.y+scale(60))
		fill(1, 1, 1, anim.texttint-2)
	end

	if t > 16 and t < 25 then
		fill(1, 1, 1, 1)
		text("Avoid other blocks.", main.UltraLight, 25, grid.x2, grid.y3+scale(40))
	end
	if t >= 25 and t < 31 then
		fill(1, 1, 1, main.tweens.ttint)
		text("Remain", main.UltraLight, 20, main.player.x, main.player.y-scale(40), 2)
		text("calm.", main.UltraLight, 20, main.player.x, main.player.y+scale(40), 8)
	end

end

function level:events(t)
	if t == 17 then sum(grid.x1, grid.y3, "x+")

	elseif t == 33 then
			sum(grid.x1, grid.y1, "y+", 1)
			sum(grid.x3, grid.y1, "y+", 1)
	elseif t == 35 then
			sum(grid.x2, grid.y1, "y+", 1)
	elseif t == 41 then
			sum(grid.x1, grid.y1, "y+", 1)
			sum(grid.x3, grid.y1, "y+", 1)
	elseif t == 43 then
			sum(grid.x2, grid.y1, "y+", 1)
	elseif t == 49 then
			sum(grid.x1, grid.y1, "y+", 1)
			sum(grid.x3, grid.y1, "y+", 1)
	elseif t == 51 then
			sum(grid.x2, grid.y1, "y+", 1)


	elseif t == 65 then
			sum(grid.x1, grid.y1, "y+", 1)
			sum(grid.x3, grid.y1, "y+", 1)
	elseif t == 67 then
			sum(grid.x2, grid.y1, "y+", 1)
	elseif t == 71 then
			sum(grid.x3, grid.y3, "x-", 4)
	elseif t == 72 then
			sum(grid.x3, grid.y1, "x-", 4)
	elseif t == 81 then
			sum(grid.x1, grid.y1, "y+", 1)
			sum(grid.x3, grid.y1, "y+", 1)
	elseif t == 83 then
			sum(grid.x2, grid.y3, "y-", 1)
	elseif t == 87 then
			sum(grid.x1, grid.y1, "y+", 4)
			sum(grid.x1, grid.y1, "x+", 4)
	elseif t == 88 then
			sum(grid.x3, grid.y3, "y-", 4)
			sum(grid.x3, grid.y3, "x-", 4)

	elseif t == 98 then gamestate.switch(main.GAME, 2, false) end
end

return level

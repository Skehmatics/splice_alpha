local main = require 'main'
local fill = main.fill
local text = main.text
local scale = main.scale
local sum = main.spawn
local bounds = main.bounds
-- local grid = main.grid
local level = {}

level.lvlnum = 4
level.bpm = 120

level.name = "Level " .. tostring(level.lvlnum)
level.soundname = "splice" .. tostring(level.lvlnum)

function level:load()
	if level.lvlnum > main.savedata.unlocked then main.savedata.unlocked = level.lvlnum end
  main.save()
  main.sound.play('music/' .. level.soundname .. '.ogg', 'music')
end

function level:draw()
end

function level:events(t)
	if t == 33 then
		sum(grid.x1, grid.y3, "s", 2)
		sum(grid.x3, grid.y3, "s", 2)
	elseif t == 34 then
		sum(grid.x2, grid.y1, "s", 2, 1/4)
		sum(grid.x2, grid.y3, "s", 2, 1/4)
	elseif t == 36 then
		sum(grid.x3, grid.y2, "s", 2)
		sum(grid.x1, grid.y2, "s", 2)
	elseif t == 39 then
		sum(grid.x1, grid.y1, "s", 3)
		sum(grid.x2, grid.y1, "s", 3)
		sum(grid.x3, grid.y1, "s", 3)
	elseif t == 40 then
		sum(grid.x1, grid.y3, "s", 3)
		sum(grid.x2, grid.y3, "s", 3)
		sum(grid.x3, grid.y3, "s", 3)
	elseif t == 41 then
		sum(grid.x1, grid.y3, "s", 2)
		sum(grid.x3, grid.y3, "s", 2)
	elseif t == 42 then
		sum(grid.x2, grid.y2, "s", 2, 1/2)
	elseif t == 44 then
		sum(grid.x1, grid.y1, "s", 1)
		sum(grid.x3, grid.y1, "s", 1)
	elseif t == 47 then
		sum(grid.x1, grid.y1, "sr", 2)
		sum(grid.x1, grid.y2, "sr", 2)
		sum(grid.x1, grid.y3, "sr", 2)
		sum(grid.x2, grid.y1, "sr", 2)
		sum(grid.x2, grid.y3, "sr", 2)
		sum(grid.x3, grid.y1, "sr", 2)
		sum(grid.x3, grid.y2, "sr", 2)
		sum(grid.x3, grid.y3, "sr", 2)
	elseif t == 49 then
		sum(grid.x1, grid.y3, "s", 2)
		sum(grid.x2, grid.y3, "s", 2)
		sum(grid.x3, grid.y3, "s", 2)
	elseif t == 50 then
		sum(grid.x1, grid.y1, "s", 2, 1/4)
		sum(grid.x2, grid.y1, "s", 2, 1/4)
		sum(grid.x3, grid.y1, "s", 2, 1/4)
	elseif t == 52 then
		sum(grid.x3, grid.y2, "s", 2)
		sum(grid.x2, grid.y2, "s", 2)
		sum(grid.x1, grid.y2, "s", 2)
	elseif t == 55 then
		sum(grid.x1, grid.y1, "s", 3)
		sum(grid.x2, grid.y1, "s", 3)
		sum(grid.x3, grid.y1, "s", 3)
	elseif t == 56 then
		sum(grid.x1, grid.y3, "s", 3)
		sum(grid.x2, grid.y3, "s", 3)
		sum(grid.x3, grid.y3, "s", 3)
	elseif t == 57 then
		sum(grid.x1, grid.y3, "s", 2)
		sum(grid.x2, grid.y3, "s", 2)
		sum(grid.x3, grid.y3, "s", 2)
	elseif t == 58 then
		sum(grid.x1, grid.y2, "s", 2, 1/2)
		sum(grid.x2, grid.y2, "s", 2, 1/2)
		sum(grid.x3, grid.y2, "s", 2, 1/2)
	elseif t == 60 then
		sum(grid.x1, grid.y1, "s", 1)
		sum(grid.x3, grid.y1, "s", 1)
		sum(grid.x3, grid.y1, "s", 1)
	elseif t == 63 then
		sum(grid.x2, grid.y2, "sr", 2)
		sum(grid.x2, grid.y2, "sr", 2)
		sum(grid.x2, grid.y2, "sr", 2)
		sum(grid.x2, grid.y2, "sr", 2)
		sum(grid.x2, grid.y2, "sr", 2)
		sum(grid.x2, grid.y2, "sr", 2)
	elseif t == 66 then gamestate.switch(main.GAME, 5, false) end
end

return level

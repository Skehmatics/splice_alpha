local main = require 'main'
local fill = main.fill
local text = main.text
local scale = main.scale
local sum = main.spawn
local bounds = main.bounds
-- local grid = main.grid
local level = {}

level.lvlnum = 6
level.bpm = 129

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
		sum(grid.x1, grid.y1, "x+", 6)
		sum(grid.x1, grid.y3, "x+", 6)
	elseif t == 34 then
		sum(grid.x3, grid.y2, "x-", 6, 1/3)
	elseif t == 35 then
		sum(grid.x1+grid.third, grid.y3, "y-", 10, nil, 5)
		sum(grid.x2, grid.y3, "y-", 10, nil, 5)
		sum(grid.x3-grid.third, grid.y3, "y-", 10, nil, 5)
	elseif t == 36 then
		sum(grid.x1, grid.y1, "s", 6, 1/3)
		sum(grid.x1, grid.y2, "s", 6, 1/3)
		sum(grid.x1, grid.y3, "s", 6, 1/3)
		sum(grid.x2, grid.y3, "s", 6, 1/3)
		sum(grid.x2, grid.y1, "s", 6, 1/2)
		sum(grid.x3, grid.y1, "s", 6, 1/2)
		sum(grid.x3, grid.y2, "s", 6, 1/2)
		sum(grid.x3, grid.y3, "s", 6, 1/2)
	elseif t == 37 then
		sum(grid.x1, grid.y3, "x+", 6)
		sum(grid.x1, grid.y1, "x-", 6)
		sum(grid.x1, grid.y3, "y-", 6, 1/2)
		sum(grid.x3, grid.y1, "y+", 6, 1/2)
	elseif t == 38 then
		sum(grid.x1, grid.y2, "x+", 6, 1/4)
		sum(grid.x3, grid.y2, "x-", 6, 1/4)
	elseif t == 39 then
		sum(grid.x1, grid.y2, "s", 6)
		sum(grid.x2, grid.y2, "s", 6)
		sum(grid.x3, grid.y2, "s", 6)
		sum(grid.x2, grid.y3, "s", 6)
		sum(grid.x2, grid.y1, "s", 6)
		sum(grid.x1+grid.third, grid.y2, "s", 8, 1/2)
	elseif t == 40 then
		sum(grid.x3-grid.third, grid.y2, "s", 8, 1/3)
	elseif t == 41 then
		sum(grid.x1, grid.y1, "sr", 3)
		sum(grid.x2, grid.y1, "sr", 3)
		sum(grid.x3, grid.y1, "sr", 3)
		sum(grid.x1, grid.y3, "sr", 3)
		sum(grid.x2, grid.y3, "sr", 3)
		sum(grid.x3, grid.y3, "sr", 3)
		sum(grid.x1, grid.y2, "sr", 3)
		sum(grid.x3, grid.y2, "sr", 3)
	elseif t == 42 then
		sum(grid.x1, grid.y1, "x+", 6)
		sum(grid.x2, grid.y1, "y+", 6, 1/4)
		sum(grid.x3, grid.y1, "x-", 6)
		sum(grid.x1, grid.y3, "x+", 6)
		sum(grid.x2, grid.y3, "y-", 6, 1/3)
		sum(grid.x3, grid.y3, "x-", 6)
	elseif t == 43 then
		sum(grid.x1, grid.y2+grid.third, "sr", 3)
		sum(grid.x3, grid.y2+grid.third, "sr", 3)
		sum(grid.x1, grid.y2-grid.third, "sr", 3)
		sum(grid.x3, grid.y2-grid.third, "sr", 3)

	elseif t == 194 then return gamestate.switch(MENU, false, true) end
end

return level

local main = require 'main'
local fill = main.fill
local text = main.text
local scale = main.scale
local sum = main.spawn
local bounds = main.bounds
-- local grid = main.grid
local level = {}

level.lvlnum = 5
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
	if t == 4 then
		sum(grid.x1, grid.y1, "f", 2)
		sum(grid.x2, grid.y1, "f", 3/2)
		sum(grid.x3, grid.y1, "f", 3/2)
		sum(grid.x1, grid.y2, "f", 3/2)
		sum(grid.x3, grid.y2, "f", 3/2)
	elseif t == 7 then
		sum(grid.x1, grid.y3, "sr", 2)
		sum(grid.x2, grid.y3, "sr", 2)
		sum(grid.x3, grid.y3, "sr", 2)
		sum(grid.x1, grid.y2, "sr", 2)
		sum(grid.x3, grid.y2, "sr", 2)
	elseif t == 8 then
		sum(grid.x2, grid.y2, "s", 4, 1/3)
	elseif t == 9 then
		sum(grid.x1, grid.y1, "f", 3/2)
		sum(grid.x2, grid.y1, "f", 3/2)
		sum(grid.x3, grid.y1, "f", 3/2)
		sum(grid.x1, grid.y2, "f", 3/2)
		sum(grid.x3, grid.y2, "f", 3/2)
	elseif t == 12 then
		sum(grid.x1, grid.y3, "f", 3/2)
		sum(grid.x2, grid.y3, "f", 3/2)
		sum(grid.x3, grid.y3, "f", 3/2)
		sum(grid.x1, grid.y2, "f", 3/2)
		sum(grid.x3, grid.y2, "f", 3/2)
	elseif t == 15 then
		sum(grid.x1, grid.y1, "sr", 2)
		sum(grid.x2, grid.y1, "sr", 2)
		sum(grid.x3, grid.y1, "sr", 2)
		sum(grid.x1, grid.y2, "sr", 2)
		sum(grid.x3, grid.y2, "sr", 2)
	elseif t == 16 then
		sum(grid.x2, grid.y1, "s", 4, 1/3)
	elseif t == 17 then
		sum(grid.x2, grid.y3, "f", 4)
		sum(grid.x1, grid.y2, "f", 4)
		sum(grid.x2, grid.y2, "fr", 4)
		sum(grid.x3, grid.y2, "f", 4)
		sum(grid.x2, grid.y1, "f", 4)
	elseif t == 18 then
		sum(grid.x2, grid.y2, "fr", 1)
	elseif t == 19 then
		sum(grid.x2, grid.y2, "fr", 1)
	elseif t == 20 then
		sum(grid.x2, grid.y2, "fr", 1)
	elseif t == 21 then
		sum(grid.x2, grid.y2, "fr", 1)
	elseif t == 23 then
		sum(grid.x1, grid.y1, "sr", 2)
		sum(grid.x3, grid.y1, "sr", 2)
		sum(grid.x1, grid.y3, "sr", 2)
		sum(grid.x3, grid.y3, "sr", 2)
	elseif t == 24 then
		sum(grid.x2, grid.y3, "f", 0.5, 1/3)
	elseif t == 25 then
		sum(grid.x2, grid.y3, "fr", 4)
		sum(grid.x1, grid.y2, "fr", 4)
		sum(grid.x2, grid.y2, "fr", 4)
		sum(grid.x3, grid.y2, "fr", 4)
		sum(grid.x2, grid.y1, "fr", 4)
	elseif t == 31 then
		sum(grid.x2, grid.y2, "sr", 0.5)
	elseif t == 34 then
		sum(grid.x2, grid.y3, "f", 0.5)
		sum(grid.x1, grid.y2, "f", 0.5)
		sum(grid.x3, grid.y2, "f", 0.5)
		sum(grid.x2, grid.y1, "f", 0.5)
	elseif t == 36 then
		sum(grid.x1, grid.y1, "x+", 7)
		sum(grid.x1, grid.y2, "x+", 7, 1/6)
		sum(grid.x1, grid.y3, "x+", 7, 2/6)
		sum(grid.x1, grid.y1, "x+", 7, 3/6)
		sum(grid.x1, grid.y2, "x+", 7, 4/6)
		sum(grid.x1, grid.y3, "x+", 7, 5/6)
	elseif t == 37 then
		sum(grid.x1, grid.y1, "x+", 7)
		sum(grid.x1, grid.y2, "x+", 7, 1/6)
		sum(grid.x1, grid.y3, "x+", 7, 2/6)
		sum(grid.x1, grid.y1, "x+", 7, 3/6)
		sum(grid.x1, grid.y2, "x+", 7, 4/6)
		sum(grid.x1, grid.y3, "x+", 7, 5/6)

	elseif t == 38 then
		sum(grid.x2, grid.y1+grid.third, "s", 4, nil, 10)
		sum(grid.x2, grid.y3-grid.third, "s", 4, nil, 10)

	elseif t == 40 then
		sum(grid.x1, grid.y1, "y+", 10, 1/3, 15)
		sum(grid.x3, grid.y1, "y+", 10, 1/3, 15)
	elseif t == 41 then
		sum(grid.x1, grid.y1, "x+", 7)
		sum(grid.x1, grid.y2, "x+", 7, 1/6)
		sum(grid.x1, grid.y3, "x+", 7, 2/6)
		sum(grid.x1, grid.y1, "x+", 7, 3/6)
		sum(grid.x1, grid.y2, "x+", 7, 4/6)
		sum(grid.x1, grid.y3, "x+", 7, 5/6)
	elseif t == 42 then
		sum(grid.x1, grid.y1, "x+", 7)
		sum(grid.x1, grid.y2, "x+", 7, 1/6)
		sum(grid.x1, grid.y3, "x+", 7, 2/6)
		sum(grid.x1, grid.y1, "x+", 7, 3/6)
		sum(grid.x1, grid.y2, "x+", 7, 4/6)
		sum(grid.x1, grid.y3, "x+", 7, 5/6)
	elseif t == 43 then
		sum(grid.x1, grid.y1+grid.third, "s", 4, nil, 10)
		sum(grid.x2, grid.y1+grid.third, "s", 4, nil, 10)
		sum(grid.x3, grid.y1+grid.third, "s", 4, nil, 10)
	elseif t == 44 then
		sum(grid.x3, grid.y1, "x-", 7)
		sum(grid.x3, grid.y2, "x-", 7, 1/6)
		sum(grid.x3, grid.y3, "x-", 7, 2/6)
		sum(grid.x3, grid.y1, "x-", 7, 3/6)
		sum(grid.x3, grid.y2, "x-", 7, 4/6)
		sum(grid.x3, grid.y3, "x-", 7, 5/6)
	elseif t == 45 then
		sum(grid.x3, grid.y1, "x-", 7)
		sum(grid.x3, grid.y2, "x-", 7, 1/6)
		sum(grid.x3, grid.y3, "x-", 7, 2/6)
		sum(grid.x3, grid.y1, "x-", 7, 3/6)
		sum(grid.x3, grid.y2, "x-", 7, 4/6)
		sum(grid.x3, grid.y3, "x-", 7, 5/6)
	elseif t == 46 then
		sum(grid.x1, grid.y3-grid.third, "s", 4, nil, 10)
		sum(grid.x2, grid.y3-grid.third, "s", 4, nil, 10)
		sum(grid.x3, grid.y3-grid.third, "s", 4, nil, 10)
	elseif t == 48 then
		sum(grid.x1, grid.y3, "y-", 10, 1/3, 20)
		sum(grid.x3, grid.y3, "y-", 10, 1/3, 20)
	elseif t == 49 then
		sum(grid.x1, grid.y1, "y+", 8)
		sum(grid.x3, grid.y1, "y+", 8, 1/6)
		sum(grid.x1, grid.y1, "y+", 8, 2/6)
		sum(grid.x3, grid.y1, "y+", 8, 3/6)
		sum(grid.x1, grid.y1, "y+", 8, 4/6)
		sum(grid.x3, grid.y1, "y+", 8, 5/6)
	elseif t == 50 then
		sum(grid.x1, grid.y1, "y+", 8)
		sum(grid.x3, grid.y1, "y+", 8, 1/6)
		sum(grid.x1, grid.y1, "y+", 8, 2/6)
		sum(grid.x3, grid.y1, "y+", 8, 3/6)
		sum(grid.x1, grid.y1, "y+", 8, 4/6)
		sum(grid.x3, grid.y1, "y+", 8, 5/6)
	elseif t == 51 then
		sum(grid.x2, grid.y2, "s", 4, nil, 10)
		sum(grid.x2, grid.y3-grid.third, "s", 4, nil, 10)
		sum(grid.x2, grid.y3, "s", 4, nil, 10)
	elseif t == 52 then
		sum(grid.x1, grid.y1, "y+", 8)
		sum(grid.x3, grid.y1, "y+", 8, 1/6)
		sum(grid.x1, grid.y1, "y+", 8, 2/6)
		sum(grid.x3, grid.y1, "y+", 8, 3/6)
		sum(grid.x1, grid.y1, "y+", 8, 4/6)
		sum(grid.x3, grid.y1, "y+", 8, 5/6)
	elseif t == 53 then
		sum(grid.x1, grid.y1, "y+", 8)
		sum(grid.x3, grid.y1, "y+", 8, 1/6)
		sum(grid.x1, grid.y1, "y+", 8, 2/6)
		sum(grid.x3, grid.y1, "y+", 8, 3/6)
		sum(grid.x1, grid.y1, "y+", 8, 4/6)
		sum(grid.x3, grid.y1, "y+", 8, 5/6)
	elseif t == 54 then
		sum(grid.x2, grid.y1, "s", 4, nil, 10)
		sum(grid.x2, grid.y1+grid.third, "s", 4, nil, 10)
		sum(grid.x2, grid.y2, "s", 4, nil, 10)
	elseif t == 56 then
		sum(grid.x1, grid.y2, "x+", 10, 1/3, 20)
		sum(grid.x2, grid.y1, "y+", 10, 1/3, 20)
		sum(grid.x3, grid.y2, "x-", 10, 1/3, 20)
		sum(grid.x2, grid.y3, "y-", 10, 1/3, 20)
	elseif t == 57 then
		sum(grid.x1, grid.y1, "y+", 8)
		sum(grid.x3, grid.y1, "y+", 8, 1/6)
		sum(grid.x1, grid.y1, "y+", 8, 2/6)
		sum(grid.x3, grid.y1, "y+", 8, 3/6)
		sum(grid.x1, grid.y1, "y+", 8, 4/6)
		sum(grid.x3, grid.y1, "y+", 8, 5/6)
	elseif t == 58 then
		sum(grid.x1, grid.y1, "y+", 8)
		sum(grid.x3, grid.y1, "y+", 8, 1/6)
		sum(grid.x1, grid.y1, "y+", 8, 2/6)
		sum(grid.x3, grid.y1, "y+", 8, 3/6)
		sum(grid.x1, grid.y1, "y+", 8, 4/6)
		sum(grid.x3, grid.y1, "y+", 8, 5/6)
	elseif t == 59 then
		sum(grid.x2, grid.y1, "s", 4, nil, 10)
		sum(grid.x2, grid.y3, "s", 4, nil, 10)
		sum(grid.x1, grid.y2, "s", 4, nil, 10)
		sum(grid.x3, grid.y2, "s", 4, nil, 10)
	elseif t == 60 then
		sum(grid.x1, grid.y3, "y-", 8)
		sum(grid.x3, grid.y3, "y-", 8, 1/6)
		sum(grid.x1, grid.y3, "y-", 8, 2/6)
		sum(grid.x3, grid.y3, "y-", 8, 3/6)
		sum(grid.x1, grid.y3, "y-", 8, 4/6)
		sum(grid.x3, grid.y3, "y-", 8, 5/6)
	elseif t == 61 then
		sum(grid.x1, grid.y3, "y-", 8)
		sum(grid.x3, grid.y3, "y-", 8, 1/6)
		sum(grid.x1, grid.y3, "y-", 8, 2/6)
		sum(grid.x3, grid.y3, "y-", 8, 3/6)
		sum(grid.x1, grid.y3, "y-", 8, 4/6)
		sum(grid.x3, grid.y3, "y-", 8, 5/6)

	elseif t == 66 then return gamestate.switch(MENU, false, true) end
end

return level

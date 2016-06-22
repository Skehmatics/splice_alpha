local main = require 'main'
local fill = main.fill
local text = main.text
local scale = main.scale
local sum = main.spawn
local bounds = main.bounds
-- local grid = main.grid
local level = {}

level.lvlnum = 3
level.bpm = 108

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
  if t == 2 then
    sum(grid.x1, grid.y1, "y+", 6, -1)
    sum(grid.x3, grid.y3, "y-", 6, -1)
  elseif t == 9 then
    sum(grid.x1, grid.y1, "x+", 6)
    sum(grid.x3, grid.y3, "x-", 6)
  elseif t == 17 then
    sum(grid.x1, grid.y1, "y+", 3)
  elseif t == 19 then
    sum(grid.x3, grid.y1, "y+", 3)
  elseif t == 21 then
    sum(grid.x2, grid.y3, "y-", 4)
  elseif t == 23 then
    sum(grid.x1, grid.y3, "x+", 4)
  elseif t == 24 then
    sum(grid.x3, grid.y1, "x-", 4)
  elseif t == 25 then
    sum(grid.x2, grid.y2, "s", 1)
  elseif t == 27 then
    sum(grid.x1, grid.y3, "y-", 5)
  elseif t == 29 then
    sum(grid.x3, grid.y3, "y-", 5)
  elseif t == 31 then
    sum(grid.x3, grid.y3, "x-", 3)
  elseif t == 32 then
    sum(grid.x3, grid.y1, "x-", 4)
    sum(grid.x3, grid.y2, "x-", 5, 1/3)
  elseif t == 33 then
    sum(grid.x1, grid.y1, "y+", 3)
  elseif t == 35 then
    sum(grid.x3, grid.y1, "y+", 3)
  elseif t == 37 then
    sum(grid.x2, grid.y3, "y-", 4)
  elseif t == 39 then
    sum(grid.x1, grid.y3, "x+", 4)
  elseif t == 40 then
    sum(grid.x3, grid.y1, "x-", 4)
  elseif t == 41 then
    sum(grid.x2, grid.y2, "s", 1)
  elseif t == 43 then
    sum(grid.x1, grid.y3, "y-", 5)
  elseif t == 45 then
    sum(grid.x3, grid.y3, "y-", 5)
  elseif t == 47 then
    sum(grid.x3, grid.y3, "x-", 3)
  elseif t == 48 then
    sum(grid.x3, grid.y1, "x-", 4)
    sum(grid.x3, grid.y2, "x-", 5, 1/3)
  elseif t == 49 then
    sum(grid.x1, grid.y2, "x+", 3)
  elseif t == 51 then
    sum(grid.x3, grid.y2, "x-", 3)
  elseif t == 53 then
    sum(grid.x2, grid.y3, "y-", 3)
  elseif t == 55 then
    sum(grid.x2, grid.y1, "y+", 4)
  elseif t == 57 then
    sum(grid.x1, grid.y1, "s", 3)
    sum(grid.x2, grid.y1, "s", 3)
    sum(grid.x3, grid.y1, "s", 3)
  elseif t == 58 then
    sum(grid.x1, grid.y3, "s", 3, 1/3)
    sum(grid.x2, grid.y3, "s", 3, 1/3)
    sum(grid.x3, grid.y3, "s", 3, 1/3)
  elseif t == 60 then
    sum(grid.x1, grid.y1, "s", 3)
    sum(grid.x2, grid.y1, "s", 3)
    sum(grid.x3, grid.y1, "s", 3)
  elseif t == 65 then
    sum(grid.x1, grid.y3, "x+", 3)
  elseif t == 67 then
    sum(grid.x1, grid.y1, "x+", 3)
  elseif t == 69 then
    sum(grid.x3, grid.y2, "x-", 3)
  elseif t == 71 then
    sum(grid.x1, grid.y3, "s", 3, 1/3)
    sum(grid.x2, grid.y3, "s", 3, 1/3)
    sum(grid.x3, grid.y3, "s", 3, 1/3)
  elseif t == 73 then
    sum(grid.x1, grid.y1, "s", 3)
    sum(grid.x2, grid.y1, "s", 3)
    sum(grid.x3, grid.y1, "s", 3)

  elseif t == 82 then gamestate.switch(main.GAME, 4, false) end
end

return level

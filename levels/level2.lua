local main = require 'main'
local fill = main.fill
local text = main.text
local scale = main.scale
local sum = main.spawn
local bounds = main.bounds
-- local grid = main.grid
local level = {}

level.lvlnum = 2
level.bpm = 90

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
    if t == 5 then
        sum(grid.x1, grid.y1, "y+", 1)
    elseif t == 6 then
        sum(grid.x2, grid.y1, "y+", 2)
    elseif t == 7 then
        sum(grid.x3, grid.y1, "y+", 3)
        sum(grid.x2, grid.y1, "y+", 5)
        sum(grid.x2, grid.y3, "y-", 5)
    elseif t == 8 then
        sum(grid.x1, grid.y2, "x+", 5)
        sum(grid.x3, grid.y2, "x-", 5)
    elseif t == 17 then
        sum(grid.x1, grid.y3, "x+", 3)
    elseif t == 18 then
        sum(grid.x3, grid.y2, "x-", 3)
    elseif t == 19 then
        sum(grid.x1, grid.y1, "x+", 3)
    elseif t == 23 then
        sum(grid.x3, grid.y1, "y+", 5)
        sum(grid.x1, grid.y1, "y+", 5)
    elseif t == 24 then
        sum(grid.x3, grid.y3, "y-", 5)
        sum(grid.x1, grid.y3, "y-", 5)
    elseif t == 33 then
        sum(grid.x2, grid.y2, "y+", 4)
    elseif t == 34 then
        sum(grid.x2, grid.y2, "x+", 4)
    elseif t == 35 then
        sum(grid.x2, grid.y2, "y-", 4)
    elseif t == 36 then
        sum(grid.x2, grid.y2, "x-", 4)
    elseif t == 39 then
        sum(grid.x1, grid.y2, "y-", 5)
        sum(grid.x2, grid.y2, "y-", 5)
        sum(grid.x3, grid.y2, "y-", 5)
    elseif t == 40 then
        sum(grid.x1, grid.y2, "y+", 5)
        sum(grid.x2, grid.y2, "y+", 5)
        sum(grid.x3, grid.y2, "y+", 5)
    elseif t == 49 then
        sum(grid.x2, grid.y2, "y+", 4)
        sum(grid.x2, grid.y2, "x+", 4)
    elseif t == 50 then
        sum(grid.x2, grid.y2, "x+", 4)
        sum(grid.x2, grid.y2, "y-", 4)
    elseif t == 51 then
        sum(grid.x2, grid.y2, "y-", 4)
        sum(grid.x2, grid.y2, "x-", 4)
    elseif t == 52 then
        sum(grid.x2, grid.y2, "x-", 4)
        sum(grid.x2, grid.y2, "y+", 4)
    elseif t == 54 then
        sum(grid.x2, grid.y3, "y-", 2)
    elseif t == 55 then
        sum(grid.x1, grid.y3, "x+", 5)
        sum(grid.x3, grid.y1, "x-", 5)
    elseif t == 56 then
        sum(grid.x3, grid.y3, "x-", 5)
        sum(grid.x1, grid.y1, "x+", 5)

    elseif t == 82 then gamestate.switch(main.GAME, 3, false) end
end

return level

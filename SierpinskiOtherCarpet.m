% ------RANDOM SEEDING-----------
Ax = rand * 10;
Ay = rand * 10;

Bx = rand * 10;
By = rand * 10;

Cx = rand * 10;
Cy = rand * 10;

A = [Ax; Ay];
B = [Bx; By];
C = [Cx; Cy];

vx = [Ax Bx Cx];
vy = [Ay By Cy];

in = false;

hold on;

while in == false
    x = rand * 10;
    y = rand * 10;
    in = inpolygon(x, y, vx, vy);
end

vertexPick = rand;

if vertexPick <= 1/3
    Rotatex = (Ax + Bx) / 2;
    Rotatey = (Ay + By) / 2;
elseif (vertexPick > 1/3) && (vertexPick <= 2/3)
    Rotatex = (Ax + Cx) / 2;
    Rotatey = (Ay + Cy) / 2;
else
    Rotatex = (Bx + Cx) / 2;
    Rotatey = (By + Cy) / 2;
end

% ------END RANDOM SEEDING-----------

for n = 1:10000
    vertexPick = rand;
    if vertexPick <= 1/3
        x = (x + Ax) / 2;
        y = (y + Ay) / 2;
    elseif (vertexPick > 1/3) && (vertexPick <= 2/3)
        x = (x + Bx) / 2;
        y = (y + By) / 2;
    else
        x = (x + Cx) / 2;
        y = (y + Cy) / 2;
    end
plot (x, y, '.');

point = [x; y; 1];
point = [ -1 0  (2 * Rotatex);...
          0  -1 (2 * Rotatey);...
          0  0   1   ] * point;
plot (point(1), point(2), '.');

end

hold off;


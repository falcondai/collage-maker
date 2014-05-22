#!/usr/bin/env python


import argparse
from PIL import Image

parser = argparse.ArgumentParser()

parser.add_argument('-g', '--grid', default=None)
parser.add_argument('-o', '--output', default='collage.png')
parser.add_argument('images', nargs='+')

args = parser.parse_args()

n = len(args.images)
print 'reading %d images: %r' % (n, args.images)

if args.grid:
    grid = map(int, args.grid.split('x'))
else:
    grid = n, 1

w, h = 0, 0
ss = []
imgs = []
for path in args.images:
        i = Image.open(path)
        imgs.append(i)
        s = i.size
        w = s[0] if w < s[0] else w
        h = s[1] if h < s[1] else h

c = Image.new('RGB', (w*grid[1], h*grid[0]))
x, y = 0, 0
for i, img in zip(xrange(grid[0]*grid[1]), imgs):
    c.paste(img.copy(), (i%grid[1]*w, i/grid[1]*h))

c.save(open(args.output, 'wb'))

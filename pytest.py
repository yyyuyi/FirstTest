import bisect
import sys

HAYSTACK = [1,2,4,6,7,12,16,68,85]
NEEDLES = [0,2,4,5,10,14,33,55,73]
ROW_FMT = '{0:2d} @ {1:2d}   {2}{0:<2d}'

def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn (HAYSTACK,needle)
        offset = position * ' |'
        print(ROW_FMT.format(needle,position,offset))

if __name__ == '__main__':
    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect
    print('DEMO',bisect_fn.__name__)
    print('haystack ->',' '.join('%2d' %n for n in HAYSTACK))
    demo(bisect_fn)
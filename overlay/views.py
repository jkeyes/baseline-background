from datetime import datetime
from datetime import timedelta
import png
from django.http import HttpResponse
from operator import truediv

def _color(color):
    try:
        color = int(color)
    except ValueError:
        color = 0

    if color < 0:
        color = 0
    elif color > 255:
        color = 255
    return color

def _far_future_expire(response):
    now = datetime.now()
    next_year = now + timedelta(days=365)
    year_seconds = 60 * 60 * 24 * 365;
    response['Expires'] = next_year.strftime("%a, %d %b %Y %H:%M:%S +0000")
    response['Cache-Control'] = 'public,max-age=%d' % year_seconds
         
def overlay(request):
    height = int(request.GET.get('h', 10))
    if height > 500:
        height = 500
    r = _color(request.GET.get('r', 0))
    g = _color(request.GET.get('g', 0))
    b = _color(request.GET.get('b', 0))
    a = _color(request.GET.get('a', 255))

    s = ['10']
    for i in range(height - 1):
        s.insert(0, '00')

    palette = [ (0,0,0,0), (r,g,b,a) ]

    response = HttpResponse(mimetype="image/png")
    _far_future_expire(response)
    w = png.Writer(1, height, palette=palette, bitdepth=1)
    w.write(response, s)
    return response

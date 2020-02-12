from flask import Flask, render_template, url_for
from app import app

posts = [
    {
        'author': 'Link Example',
        'title': 'Link title',
        'content': 'link',
        'date_posted': 'Format description'
    },
    {
        'author': 'Link Example',
        'title': 'Link title2',
        'content': 'link2',
        'date_posted': 'Format description'
    },
]

postsHls = [
    {
        'title': 'Apple Basic Stream 4:3',
        'link': 'https://devstreaming-cdn.apple.com/videos/streaming/examples/bipbop_4x3/bipbop_4x3_variant.m3u8',
        'format_description': 'Apple Basic Stream: H.264 @ 30Hz, 4x3 aspect ratio'
    },
    {
        'title': 'Apple Basic Stream 16:9',
        'link': 'https://devstreaming-cdn.apple.com/videos/streaming/examples/bipbop_16x9/bipbop_16x9_variant.m3u8',
        'format_description': 'Apple Basic Stream: 16x9 aspect ratio, H.264 @ 30Hz, single .ts file, with byte-ranges in the playlists'
    },
    {
        'title': 'Apple Advanced Stream',
        'link': 'https://devstreaming-cdn.apple.com/videos/streaming/examples/bipbop_adv_example_hevc/master.m3u8',
        'format_description': 'Apple Advanced Stream fMP4: H.264 and HEVC @ 30Hz and 60Hz, 16x9 aspect ratio'
    },
]

@app.route("/")
@app.route("/hls")
def hls():
    return render_template('testpage.html', posts=postsHls, title='HLS')


@app.route("/smoothstreaming")
def smoothstreaming():
    return render_template('testpage.html', posts=posts, title='SmoothStreaming')

@app.route("/dash")
def dash():
    return render_template('testpage.html', posts=posts, title='DASH')

@app.route("/transportstream")
def transportstream():
    return render_template('testpage.html', posts=posts, title='TransportStream')

@app.route("/drm")
def drm():
    return render_template('testpage.html', posts=posts, title='DRM')

if __name__ == '__main__':
    app.run(debug=True)

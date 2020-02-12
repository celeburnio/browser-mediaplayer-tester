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
    # {
    #     'title': 'Apple Basic Stream 4:3',
    #     'link': 'https://devstreaming-cdn.apple.com/videos/streaming/examples/bipbop_4x3/bipbop_4x3_variant.m3u8',
    #     'format_description': 'Apple Basic Stream: H.264 @ 30Hz, 4x3 aspect ratio'
    # },
    {
        'title': 'Apple Basic Stream 16:9',
        'link': 'https://devstreaming-cdn.apple.com/videos/streaming/examples/bipbop_16x9/bipbop_16x9_variant.m3u8',
        'format_description': 'Apple Basic Stream: 16x9 aspect ratio, H.264 @ 30Hz, single .ts file, with byte-ranges in the playlists'
    }
    # {
    #     'title': 'Apple Advanced Stream',
    #     'link': 'https://devstreaming-cdn.apple.com/videos/streaming/examples/bipbop_adv_example_hevc/master.m3u8',
    #     'format_description': 'Apple Advanced Stream fMP4: H.264 and HEVC @ 30Hz and 60Hz, 16x9 aspect ratio'
    # },
    # {
    #     'title': 'Bitmovin HLS test',
    #     'link': 'https://bitmovin-a.akamaihd.net/content/MI201109210084_1/m3u8s/f08e80da-bf1d-4e3d-8899-f0f6155f6efa.m3u8',
    #     'format_description': ' -- '
    # },
    
]

postsMp4 = [
    {
        'title': 'View_From_A_Blue_Moon_Trailer',
        'link': 'https://cdn.plyr.io/static/demo/View_From_A_Blue_Moon_Trailer-720p.mp4',
        'format_description': 'mp4 720p resolution'
    }
]

postsDash = [
    {
        'title': 'Bitmovin dash test',
        'link': 'https://bitmovin-a.akamaihd.net/content/MI201109210084_1/mpds/f08e80da-bf1d-4e3d-8899-f0f6155f6efa.mpd',
        'format_description': ' -- '
    }
]

postsSmoothStreaming = [
    {
        'title': 'Bitmovin smoothstreaming test',
        'link': 'https://test.playready.microsoft.com/smoothstreaming/SSWSS720H264/SuperSpeedway_720.ism/manifest',
        'format_description': ' -- '
    }
]

@app.route("/")
@app.route("/hls")
def hls():
    return render_template('testpage.html', posts=postsHls, title='HLS')


@app.route("/smoothstreaming")
def smoothstreaming():
    return render_template('testpage.html', posts=postsSmoothStreaming, title='SmoothStreaming')

@app.route("/dash")
def dash():
    return render_template('testpage.html', posts=postsDash, title='DASH')

@app.route("/transportstream")
def transportstream():
    return render_template('testpage.html', posts=posts, title='TransportStream')

@app.route("/drm")
def drm():
    return render_template('testpage.html', posts=posts, title='DRM')

if __name__ == '__main__':
    app.run(debug=True)

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


@app.route("/")
@app.route("/hls")
def hls():
    return render_template('hls.html', posts=posts, title='HLS')


@app.route("/smoothstreaming")
def smoothstreaming():
    return render_template('smoothstreaming.html', posts=posts, title='SmoothStreaming')

@app.route("/dash")
def dash():
    return render_template('dash.html', posts=posts, title='DASH')

@app.route("/transportstream")
def transportstream():
    return render_template('transportstream.html', posts=posts, title='TransportStream')

@app.route("/drm")
def drm():
    return render_template('drm.html', posts=posts, title='DRM')

if __name__ == '__main__':
    app.run(debug=True)

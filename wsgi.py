import os

TYPES = {
    '.html': 'text/html',
    '.png': 'image/png',
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.css': 'text/css',
    '.js': 'application/javascript',
    '.webp': 'image/webp',
    '.ico': 'image/x-icon',
}

ROOT = os.path.dirname(os.path.abspath(__file__))

def application(environ, start_response):
    path = environ.get('PATH_INFO', '/').lstrip('/')
    if not path:
        path = 'index.html'

    file_path = os.path.join(ROOT, path)

    try:
        with open(file_path, 'rb') as f:
            content = f.read()
        ext = os.path.splitext(path)[1].lower()
        content_type = TYPES.get(ext, 'application/octet-stream')
        start_response('200 OK', [('Content-Type', content_type)])
        return [content]
    except FileNotFoundError:
        start_response('404 Not Found', [('Content-Type', 'text/plain')])
        return [b'Not Found']

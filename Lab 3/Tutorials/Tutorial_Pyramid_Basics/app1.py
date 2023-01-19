from pyramid.response import FileResponse

def hello_world(request):
    print('Incoming request')
    return FileResponse('index.html') # the HTML file to be shown

    # Add static view
    config.add_static_view(name='/', path='./public', cache_max_age=3600)

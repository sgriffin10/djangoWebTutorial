#run file when want to start server/website 

from website import create_app #can do this cuz website is a python package because we put __init__.py in folder

app = create_app()

if __name__ == '__main__':
    app.run(debug=True) #starts off a webserver, everytime we make a change its gonna automatically rerun the webserver


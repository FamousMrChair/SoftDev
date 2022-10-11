# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2022

# DEMO 
# basics of /static folder

from flask import Flask
app = Flask(__name__) 

@app.route("/")       
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "<html> <h1> No hablo queso! </h1> </html>"

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run() # only allowed for "main driver", not for imported modules.

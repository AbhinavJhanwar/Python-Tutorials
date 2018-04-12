'''
Created on May 31, 2017

@author: abhinav.jhanwar
'''

# import flask
from flask import Flask, redirect, render_template, request, url_for
from random import randint

# define flask app
app = Flask(__name__)

# defining first route decorator
@app.route("/")
def index():
    # sample input -> localhost:5000/
    # sample output -> Flask App!
    return "Flask App!"


# using arguments from http url
@app.route("/members/<string:name>/")
def getMember(name):
    # sample input -> localhost:5000/members/Flask
    # sample output -> Hello Flask
    return "Hello %s"%name

# try these other functions-->
@app.route('/admin')
def hello_admin():
    return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest' % guest

# using redirect
@app.route('/user/<name>')
def hello_user(name):
    if name =='admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest',guest = name))

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

@app.route('/login/',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success',name = user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success',name = user))

# lets create a fun app
@app.route("/hello/<string:name>/")
def hello(name):
    # sample input -> 
    quotes = [ "Mirrors can't talk, lucky for you they can't laugh either",
               "I don't believe in plastic surgery, But in your case, Go ahead.",
               "Tell me... Is being stupid a profession or are you just gifted?",
               "Zombies eat brains. You're safe.",
               "Look at you your in perfect shape.......for a circle",
               "Keep rolling your eyes. Maybe you'll find a brain back there.",
               "There's someone for everyone, and the person for you is psychiatrist",
               "Are you always so stupid or is today a special occasion?",
               "I'm sorry I hurt your feelings when I called you stupid. I really thought you already knew.",
               "Well hello there, you self-centered, narcissistic double canoe. How can I help the world revolve around you today?",
               "The human body is 90% water so you are basically just cucumber with anxiety.",
               "ABRACADABRA! Nope. you're still an idiot.",
               "Some people walk into our lives and leave footprints on our hearts. But you walk into our lives and we want to leave footprints on your face.",
               "You cry, I cry...you laugh, I laugh....you jump off a cliff I laugh even harder!!",
               "I look at the moon and it looks really beautiful!.. Then I look at you... and.. I think I'll look at the moon again! ",
               "Don't think of yourself as an ugly person, think of yourself as a beautiful monkey. It always gets laughs!",
               "Four out of five voices in my head think you're an idiot. The other one, is deciding where to bury you.",
               "The trash gets picked up tomorrow. Be Ready.",
               "If stupid could fly, you'd be a jet.",
               "Well at least your mom thinks you're pretty...",
               "I thought I had seen the pinnacle of stupid... Then I met you.",
               "Are you really stupid or you are just pretending?"]
    randomNumber = randint(0,len(quotes)-1) 
    quote = quotes[randomNumber] 
    if(name == 'Abhinav'):
        quote1 = ["I am going to stand outside, so if anybody asks for me, I'm outstanding!",
                  "I want to kill the hottest person alive... But suicide is a crime!",
                  "It's okay if you don't like me. Not everyone has good taste."
                  ]
        randomNumber = randint(0,len(quote1)-1) 
        quote = quote1[randomNumber] 
    
    images = ["https://media.giphy.com/media/V1Jk434D2oZ8s/giphy.gif",
              "https://s-media-cache-ak0.pinimg.com/originals/ea/2d/09/ea2d0990c249466efde38041c13ef5ec.jpg",
              "https://media1.giphy.com/media/6zMMMQDQjjyrm/giphy.gif#62-grid1",
              "https://media1.giphy.com/media/mND0vznomG6vm/giphy.gif#92-grid1",
              "http://bestanimations.com/Animals/Reptiles/snakes/animated-cobra-snake-gif-2.gif",
              "https://media0.giphy.com/media/14uXQbPS73Y3qU/giphy.gif#2-grid1",
              "http://bestanimations.com/Cartoons/WarnerBros/funny-duffy-duck-looney-toons-animated-gif-12.gif",
              "https://s-media-cache-ak0.pinimg.com/originals/ea/2d/09/ea2d0990c249466efde38041c13ef5ec.jpg",
              "https://media0.giphy.com/media/HxOxEt3qQ25YQ/giphy.gif#1-grid1",
              "https://s-media-cache-ak0.pinimg.com/originals/37/e6/54/37e6546555565309406876ec766d5b05.gif",
              "http://media0.giphy.com/media/PWfHC8ogZpWcE/giphy.gif",
              "https://media1.giphy.com/media/IrQcyTog3X8VW/giphy.gif#13-grid1",
              "https://media2.giphy.com/media/SjxtmBS267NOU/giphy.gif#137-grid1",
              "https://media2.giphy.com/media/26tPo9rksWnfPo4HS/giphy.gif#1-grid1",
              "https://media4.giphy.com/media/PYRO3Z0F6vK6c/giphy.gif#12-grid1",
              "https://media0.giphy.com/media/eopRZZj20N320/giphy.gif#9-grid1",
              "https://media4.giphy.com/media/Poq6o8tuqMwN2/giphy.gif#26-grid1",
              "https://media4.giphy.com/media/3d1C13mkBAcO4/giphy.gif#53-grid1",
              "https://media1.giphy.com/media/FxcUSSUBqQuBO/giphy.gif#5-grid1"
              ]
    randomNumber = randint(0,len(images)-1) 
    im = images[randomNumber]           
              
 
    return render_template(
        'fun.html',**locals())
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000,debug = True)
    

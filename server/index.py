from flask import Flask, current_app
from flask_socketio import SocketIO, emit
from flask_sqlalchemy import SQLAlchemy

import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////temp/database.db'
db = SQLAlchemy(app)
socketio = SocketIO(app)

socketio.run(app)

import sqlite3
from flask import g

class Player(db.Model):
    id = db.Column(db.String(15), primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    avatar = db.Column(db.String(60), nullable=False)
    state = db.Column(db.String(15))
    score = db.Column(db.Integer)
    count = db.Column(db.Integer)
    lines = db.Column(db.Integer)
    tetris = db.Column(db.Integer)
    level = db.Column(db.Integer)
    board = db.Column(db.Text)
    active_piece = db.Column(db.Text)

    def __repr__(self):
        return '<User %r>' % self.name

class Game(db.Model):
    id = db.Column(db.String(15), primary_key=True)
    players = db.Column(db.Text, nullable=False)
    state = db.Column(db.String(15), nullable=False)
    piece_list = db.Column(db.Text)
    piece_counter = db.Column(db.Integer)

    def __repr__(self):
        return '<Game %r>' % self.id

def init_db():

    # db.drop_all()
    
    # db.create_all()
    
    # nacho = Player(id='aaaaaa', name='nacho', avatar='dragon100x100.png', state='IDDLE')
    # fran = Player(id='bbbbbb', name='fran', avatar='dragon100x100.png', state='IDDLE')
    # game = Game(id='cccccc', players='["'+nacho.id+'","'+fran.id+'"]',state='PENDING' ,piece_list='["L","S","Z","Z","I","J"]', piece_counter=0)
    # db.session.add(nacho)
    # db.session.add(fran)
    # db.session.add(game)
    
    # db.session.commit()
    # print(Game.query.all())
    
    # db.session.add(player)
    # db.session.commit()
    # player = db.session.query(Player).filter_by(id='aaaaaa').first()
    # print(player)
    # player.name = "nacho modi"
    # db.session.add(player)
    # db.session.commit()
    # print(db.session.new)
    # print('player despies : ',player)
    # obj = json.dumps([(1,2,3),(1,3,2)])
    # print(str(obj))
    # tuplesasd = [tuple(x) for x in list(json.loads('[[1, 2, 3], [1, 3, 2]]'))]
    # print(str(tuplesasd))
    pass

init_db()

from .views.game import game
from .views.player import player
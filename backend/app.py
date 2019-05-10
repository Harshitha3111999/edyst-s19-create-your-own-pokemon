from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'pokemon.db')
db = SQLAlchemy(app)
class pokemon(db.Model):
    id = db.Column("pokemon_id",db.Integer, unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False, primary_key=False)
    sprite = db.Column(db.String(500), unique=True, nullable=False, primary_key=False)
    f = db.Column(db.String(20), unique=False, nullable=False, primary_key=False)
    b = db.Column(db.String(20), unique=False, nullable=False, primary_key=False)
    d = db.Column(db.String(20), unique=False, nullable=False, primary_key=False)
    def __init__(self, id,name,sprite,f,b,d):
        self.id=id
        self.name=name
        self.sprite=sprite
        self.f=f
        self.b=b
        self.d=d
@app.route("/api/pokemon", methods=["POST"])
def create():
    id=0
    data=request.get_json()
    if pokemon.query.filter(pokemon.name==data["pokemon"]["name"]).first():
        return "<h1>the data given is already exists(search through name)</h1>"
    pokemone=pokemon.query.all()
    for length in pokemone:
        id=id+1
    pokemondata = pokemon(id+1,data['pokemon']['name'],data['pokemon']['sprite'],data['pokemon']['cardColours']['fg'], data['pokemon']['cardColours']['bg'], data['pokemon']['cardColours']['desc'])
    db.session.add(pokemondata)
    db.session.commit()
    return get(id+1)
@app.route("/api/pokemon/<int:id>", methods=["DELETE"])
def delete(id):
    if id<=0:
        return "<h1>give correct details</h1>"
    result = pokemon.query.filter_by(id=id).first()
    if result == None:
        return "<h1>There is no pokemon with specified ID so details cannot be deleted</h1>",404
    data = get(id)
    db.session.delete(result)
    db.session.commit()
    return data

@app.route("/api/pokemon/<int:id>",methods=["GET"])
def get(id) :
    if id<=0:
        return "<h1>give correct details</h1>"
    result = pokemon.query.filter(pokemon.id == id).first()
    if result == None:
        return '<h1>No pokemon with the specified ID found</h1>'
    else:
        data={}
        data['pokemon'] = {}
        data['pokemon']['id']=result.id
        data['pokemon']['name']=result.name
        data['pokemon']['sprite']=result.sprite
        data['pokemon']['cardColours']={}
        data['pokemon']['cardColours']['fg']=result.f
        data['pokemon']['cardColours']['bg']=result.b
        data['pokemon']['cardColours']['desc']=result.d
        return jsonify(data)

@app.route("/api/pokemon/<int:id>", methods=["PATCH"])
def update(id):
    if id<=0:
        return "<h1>give correct details</h1>"
    data = request.get_json()
    if data["pokemon"] == {}:
        return "<h1>Atleast one field must be</h1>"
    else:
        result = pokemon.query.filter(pokemon.id == id).first()
        if result == None:
                return "<h1>There is no pokemon with specified ID </h1>"
        for key in data['pokemon'].keys():
            if key == 'name':
                result.name = data['pokemon']['name']
            if key == 'sprite' :
                result.sprite = data['pokemon']['sprite']
            if key == 'cardColours' :
                result.fg = data['pokemon']['cardColours']['fg']
                result.bg = data['pokemon']['cardColours']['bg']
                result.desc = data['pokemon']['cardColours']['desc']
            db.session.commit()
            return get(id)


if __name__ == '__main__':
    db.create_all()
    app.run(host='localhost', port=8006, debug=True)
from flask import Flask,redirect,url_for,render_template,request,jsonify

app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
   return "<h1>Mi primer api de peliculas</h1>"


#Simulador de Db de peliculas
peliculas=[
    {"id":0,
    "name":"El padrino",
    "estreno":1972},
    {"id":1,
    "name":"V De venganza",
    "estreno":1999},
]

@app.route('/api/peliculas/todas', methods=['GET'])
def api_peliculas_todas():
    return jsonify(peliculas)


@app.route('/api/peliculas/', methods=['GET'])
def api_peliculas():
    if ("id" in request.args):
        id = int(request.args["id"])
    else:
        return "Error: No se ingrese ningun ID"
    
    for pelicula in peliculas:
        if (pelicula["id"] == id):
            resultado = pelicula
            break

    return jsonify(resultado)


if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)





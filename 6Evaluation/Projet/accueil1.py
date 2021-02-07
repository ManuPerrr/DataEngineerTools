from flask import Flask
app=Flask(__name__)

from flask import request
from flask import render_template, render_template_string
from flask import redirect

htmltemplate = """
    
    <html lang="fr">
    
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Archivo">
    
        <style>
            body { background: #b6d2ec; }
        </style>

        <title>
            Projet Data Engineering
        </title>
        
        <style>
         .button {
         background-color: #1c87c9;
         border: none;
         color: white;
         padding: 20px 34px;
         text-align: center;
         text-decoration: none;
         display: inline-block;
         font-size: 20px;
         margin: 4px 80px;
         cursor: pointer;
         }
         .button:hover{
         background:#FF0000;
         }
         </style>
         
    </head>

    <body>
    
    <div class="container">
      <div class="row">
        <div style="font-family: 'Archivo';">
        
          <p>
          
              <center>
              <font size="10">
                  Bienvenu !
              </font>
              </center>
              
              <br>
              <br>
              <br>
              
              <font size="5">
                  Notre projet met en relation les informations de 2 sites différents : AlloCiné et BoxOfficeMojo.
              </font>

              <font size="5">
                  Ici vous pouvez faire un choix : soit vous recherchez un film soit vous cherchez les tops films selon plusieurs catégories.
              </font>
              
              
          </p>
          
          <br>
          
          <center>
          <form>
              <a href="http://127.0.0.1:2745/recherche/" class="button">Recherche</a>
              <a href="http://127.0.0.1:2745/top/" class="button">Tops films</a>
          </form>
          </center>
          
        </div>
      </div>
    </div>

    </body>

"""

htmltemplate_error = """
    <html lang="fr">
    
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Archivo">
        
        <style>
            body { background: #b6d2ec; }
        </style>

        <title>
            Erreur404
        </title>
        
        <style>
         .button {
         background-color: #1c87c9;
         border: none;
         color: white;
         padding: 20px 34px;
         text-align: center;
         text-decoration: none;
         display: inline-block;
         font-size: 20px;
         margin: 4px 80px;
         cursor: pointer;
         }
         .button:hover{
         background:#FF0000;
         }
         </style>
        
    </head>

    <body>
    
    <div class="container">
      <div class="row">
        <div style="font-family: 'Archivo';">
        
          <p> 
              
              <font size="5">
                  Il n'y a rien à voir ici...
              </font>

          </p>
          
          <center>
          <form>
              <a href="http://127.0.0.1:2745/" class="button">Retour</a>
          </form>
          </center>

        </div>
      </div>
    </div>

    </body>
"""

htmltemplate_recherche = """
    
    <html lang="fr">
    
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Archivo">
        
        <style>
            body { background: #b6d2ec; }
        </style>

        <title>
            Projet Data Engineering
        </title>
        
    </head>

    <body>
    
    <div class="container">
      <div class="row">
        <div style="font-family: 'Archivo';">
        
          <p> 
              
              <center>
              <font size="7">
                  Recherche
              </font>
              </center>

          </p>
          
          <form method="POST">
              <p>
                  <font size="4">
                      Rechercher un film :
                  </font>
              </p>
              <input name="C">
              <input type="submit">
          </form>

        </div>
      </div>
    </div>

    </body>

"""

htmltemplate_film = """
    
    <html lang="fr">
    
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Archivo">
        
        <style>
            body { background: #b6d2ec; }
        </style>

        <title>
            Projet Data Engineering
        </title>
        
    </head>

    <body>
    
    <div class="container">
      <div class="row">
        <div style="font-family: 'Archivo';">
        
          <p>    
              <font size="7">
                  {% if title %}
                  Vous avez choisi le film : {{ title }} !
                  {% else %}
                  Vous avez choisi le film :
                  {% endif %}
              </font>
              
              <br>
              <br>
              
              <font size="5">
                  Titre original :
              </front>
              
              <br>
              
              <font size="5">
                  Synopsis : 
              </front>
              
              <br>
              
              <font size="5">
                  Sortie le :
              </front>
              
              <br>    
              
              <font size="5">
                  Durée :
              </front>
              
              <br>
              
              <font size="5">
                  Genre :
              </front>
              
              <br>
              
              <font size="5">
                  Casting :
              </front>
              
              <br>
              
              <font size="5">
                  Réalisateur :
              </front>
              
              <br>
              
              <font size="5">
                  Nombre de notes Allociné :
              </front>
              
              <br>
              
              <font size="5">
                  Nombre de critiques :
              </front>
              
              <br>
              
              <font size="5">
                  Note du public :
              </front>
              
              <br>
              
              <font size="5">
                  Note de la presse :
              </front>
              
              <br>
              
              <font size="5">
                  Budget : 
              </front>
              
              <br>
              
              <font size="5">
                  Box office domicile :
              </front>
              
              <br>
              
              <font size="5">
                  Box office international :
              </front>
              
              <br>
              
              <font size="5">
                  Box office total :
              </front>
          </p>

        </div>
      </div>
    </div>

    </body>

"""

htmltemplate_top="""
    <html lang="fr">
    
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Archivo">
        
        <style>
            body { background: #b6d2ec; }
        </style>

        <title>
            Projet Data Engineering
        </title>
        
    </head>

    <body>
    
    <div class="container">
      <div class="row">
        <div style="font-family: 'Archivo';">
        
          <p> 

              <center>
              <font size="7">
                  Top film
              </font>
              </center>

          </p>
          
          <form method="POST">
                      <label for="tops">
                      <font size="5">
                          Recherchez un top film :
                      </font>
                      </label>
                      <select name="tops" id="tops">
                          <option value="boxtot">Meilleur box office</option>
                          <option value="duree">Film les plus longs</option>
                          <option value="notepre">Meilleurs films (note presse)</option>
                          <option value="notepub" selected>Meilleurs films (note public)</option>
                      </select>
                  
                  <br>
                  <br>
    
                      <label for="genres">
                      <font size="5">
                          Genre :
                      </font>
                      </label>
                      <select name="genres" id="genres">
                          <option value="Action">Action</option>
                          <option value="Animation">Animation</option>
                          <option value="Aventure">Aventure</option>
                          <option value="Biopic">Biopic</option>
                          <option value="Comédie">Comédie</option>
                          <option value="Comédie dramatique">Comédie dramatique</option>
                          <option value="Divers">Divers</option>
                          <option value="Documentaire">Documentaire</option>
                          <option value="Drame">Drame</option>
                          <option value="Eprouvante-horreur">Eprouvante-horreur</option>
                          <option value="Famille">Famille</option>
                          <option value="Fantastique">Fantastique</option>
                          <option value="Guerre">Guerre</option>
                          <option value="Historique">Historique</option>
                          <option value="Musical">Musical</option>
                          <option value="Policier">Policier</option>
                          <option value="Romance">Romance</option>
                          <option value="Science fiction">Science fiction</option>
                          <option value="Thriller">Thriller</option>
                          <option value="Western">Western</option>
                          <option value="All" selected>Tout</option>
                      </select>
                  
                  <br>
                  <br>
                      <label for="number">
                      <font size="5">
                          Nombre de films affichés :
                      </font>
                      </label>
                      
                      <input type="number" id="nb" name="nb" value="1" min="1" max="50">
                      
                      <br>
                      <br>
                      
            </form>

        </div>
      </div>
    </div>

    </body>

"""

htmltemplate_topfilm="""
    
    <html lang="fr">
    
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Archivo">
        
        <style>
            body { background: #b6d2ec; }
        </style>

        <title>
            Projet Data Engineering
        </title>
        
    </head>

    <body>
    
    <div class="container">
      <div class="row">
        <div style="font-family: 'Archivo';">
        
          <p> 
              
              <center>
              <font size="7">
                  Top {{n}} {{top}} de genre {{genre}} 
              </font>
              </center>

          </p>


        </div>
      </div>
    </div>

    </body>

"""


@app.route('/')
def hello():
    return render_template_string(htmltemplate)

@app.errorhandler(404)
def page_not_found(e):
    return render_template_string(htmltemplate_error)

@app.route('/recherche/')
def recherche():
    return render_template_string(htmltemplate_recherche)

@app.route('/recherche/', methods=['POST'])
def recherche_post():
    title = request.form['C']
    return redirect('/recherche/'+title)

@app.route('/recherche/<title>')
def film(title):
    return render_template_string(htmltemplate_film, title=title)

@app.route('/top/')
def top():
    return render_template_string(htmltemplate_top)

@app.route('/top/', methods=['POST'])
def top_post():
    top = request.form['tops']
    genre = request.form['genres']
    n = request.form['nb']
    return redirect('/top/'+top+'/'+genre+'/'+n)

@app.route('/top/<top>/<genre>/<n>')
def top_film(top,genre,n):
    if top=="duree":
        top="des plus longs films"
    elif top=="boxtot":
        top="des plus gros box office"
    elif top=="notepre":
        top="des films les mieux notés par la presse"
    elif top=="notepub":
        top="des films les mieux notés par le public"
    else:
        top="des films"
    return render_template_string(htmltemplate_topfilm, top=top, genre=genre, n=n)
    
    
    
if __name__ == '__main__':
    app.run(debug=True, port=2745)

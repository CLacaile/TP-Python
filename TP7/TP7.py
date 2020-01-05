from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

def login(nom, mdp):
    """ Fonction de connexion

    Args:
        nom (str) le nom de l'utilisateur à authentifier
        mdp (str) le mot de passe de l'utilisateur
    Returns:
        True si le couple est bien présent dans le fichier "users", 
        False sinon
    """
    is_auth = False
    try:
        with open("users", "r") as usersfile:
            file_content = usersfile.readlines()
            for num_line in range(len(file_content)):
                if file_content[num_line] == nom + ";" + mdp:
                    is_auth = True
            usersfile.close()
    except: 
        print("!!! Impossible d'ouvrir le fichier des utilisateurs")
    finally:
        return is_auth

# Définition de la page d'accueil de l'application
# où l'utilisateur doit s'identifier. Elle n'a pas d'adresse particulière.
@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        ## Gestion de la requête POST envoyée lors de l'appui sur le bt
        # Récupération du nom et mot de passe saisis
        user = request.form["name"]
        pswd = request.form["password"]
        # Identification à partir du fichier "users"
        if login(user, pswd) == True:
            # Redirection vers le page "home" avec le nom du user
            return redirect(url_for("home", username=user))
        else: 
            return render_template("index.html")
    else:
        return render_template("index.html")

# Définition de la page "home" d'adresse "home/nom_du_user"
@app.route("/home/<username>")
def home(username):
    return render_template("home.html", content=username)

if __name__ == "__main__":
    app.run(debug=True)
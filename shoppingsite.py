"""Ubermelon shopping application Flask server.

Provides web interface for browsing melons, seeing detail about a melon, and
put melons in a shopping cart.

Authors: Joel Burton, Christian Fernandez, Meggie Mahnken.
"""


from flask import Flask, render_template, redirect, flash, session, url_for, escape, request
import jinja2

import model


app = Flask(__name__)

# Need to use Flask sessioning features

app.secret_key = 'melons-are-awesome'

# Normally, if you refer to an undefined variable in a Jinja template,
# Jinja silently ignores this. This makes debugging difficult, so we'll
# set an attribute of the Jinja environment that says to make this an
# error.


app.jinja_env.undefined = jinja2.StrictUndefined
melons = model.Melon.get_all()

@app.route("/")
def index():
    """Return homepage."""
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

    return render_template("homepage.html")

@app.route("/melons")
def list_melons():
    """Return page showing all the melons ubermelon has to offer"""

    melons = model.Melon.get_all()
    return render_template("all_melons.html",
                           melon_list=melons)


@app.route("/melon/<int:id>")
def show_melon(id):
    """Return page showing the details of a given melon.

    Show all info about a melon. Also, provide a button to buy that melon.
    """

    melon = model.Melon.get_by_id(id)
    print melon
    return render_template("melon_details.html",
                           display_melon=melon)


@app.route("/cart")
def shopping_cart():
    """Display content of shopping cart."""
    
    
    #query db for all melons that match ids in melons_added 
    #    SELECT * FROM Melons Where melon_id = melons_added_id 

    session = {'melon_count':{}}
    #extracting melon ids from cart and rebinding to a list named melons_added
    melons_ids = session['cart']
    print melons_ids

    #getting pricing information for each melon type in cart in a dictionary
    #melon_info = { id: model.Melon.get_by_id(id) for id in melons_ids}

    

    for melon in melons_ids:
        session = melon_count.get(melon, 0) + 1

    print session






        #melon = model.Melon.get_by_id(id)    
    
    #counting melons

    #quantity = count(melons_ids)    
    #print quantity


    # TODO: Display the contents of the shopping cart.
    #   - The cart is a list in session containing melons added
    
    return render_template("cart.html", melons_list = melons)


@app.route("/add_to_cart/<int:id>")
def add_to_cart(id):
    """Add a melon to cart and redirect to shopping cart page.

    When a melon is added to the cart, redirect browser to the shopping cart
    page and display a confirmation message: 'Successfully added to cart'.
    """
    #make the cart, where cart = []
    #append the cart with melon ids
    
    session.setdefault('cart', []).append(id)

        #check out setDefault to check if keys in cart
  
    flash("Melon was successfully added to cart")
    return render_template("cart.html", melons_list = melons)
    


    # TODO: Finish shopping cart functionality
    #   - use session variables to hold cart list



@app.route("/login", methods=["GET", "POST"])
def show_login():
    """Show login form."""
    if request.method == 'POST':
        email = request.form('email')
        password = request.form('password')


        session['email'] = request.form['email']
        session['password'] = request.form['password']

        # print email
        # print password

        return redirect(url_for('index'))
   
    if request.method == "GET":

        email = request.args.get('email')
        password = request.args.get('password')
        return render_template("login.html")
        
        print email
        print password 


# @app.route("/login", methods=["POST"])
# def process_login():
#     """Log user into site.

#     Find the user's login credentials located in the 'request.form'
#     dictionary, look up the user, and store them in the session.
#     """

#     # TODO: Need to implement this!

#     return "Oops! This needs to be implemented"


@app.route("/checkout")
def checkout():
    """Checkout customer, process payment, and ship melons."""

    # For now, we'll just provide a warning. Completing this is beyond the
    # scope of this exercise.

    flash("Sorry! Checkout will be implemented in a future version.")
    return redirect("/melons")


if __name__ == "__main__":
    app.run(debug=True)

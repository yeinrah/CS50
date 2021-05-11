import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

from datetime import datetime

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")

# Add tables to the database to keep track of purchase
db.execute("CREATE TABLE IF NOT EXISTS transactions (id INTEGER NOT NULL, name TEXT NOT NULL, symbol TEXT NOT NULL, shares NUMERIC NOT NULL, price NUMERIC NOT NULL, state TEXT NOT NULL, time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP)")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    # Initiate variables
    user_id = session["user_id"]
    record = db.execute("SELECT symbol, SUM(shares), name FROM transactions WHERE ID = ? GROUP BY symbol ORDER BY symbol", user_id)
    count = len(record)
    cash = float(db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"])
    assets = []
    grand_total = 0

    # Render apology if record doesn't exist
    if not record:
        return render_template("no_transactions.html")

    # Query for the currently logged in user's information
    for i in range(count):
        symbol = record[i]["symbol"].upper()
        shares = int(record[i]["SUM(shares)"])
        quote = lookup(symbol)
        name = record[i]["name"]
        price = float(quote["price"])
        total = shares * price
        assets.append({"symbol": symbol, "shares": shares, "name": name, "price": price, "total": total})
        grand_total += total

    return render_template("index.html", cash=cash, assets=assets, grand_total=grand_total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Initiate variables
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        quote = lookup(symbol)
        user_id = session["user_id"]
        time = datetime.now()

        try:
            shares = int(shares)
        except ValueError:
            return apology("shares must be an integer", 400)

        # Ensure symbol was submitted
        if not symbol:
            return apology("must provide stock's symbol", 400)

        # Ensure number of shares was submitted
        elif not shares:
            return apology("must provide number of shares you would like to purchase", 400)

        # Ensure symbol is valid
        elif not quote:
            return apology("Invalid stock symbol, Please try again", 400)

        # Ensure shares is valid
        elif shares <= 0:
            return apology("must provide non-negative, non-fractional number", 400)

        # If the user doesn't have enough money, render apology. If the user has enough money, update db
        name = quote["name"]
        price = float(quote["price"])

        cash = float(db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"])

        if cash > price * shares:
            db.execute("INSERT INTO transactions VALUES (?, ?, ?, ?, ?, ?, ?)",
                       user_id, name, symbol, shares, price, "purchase", time)

            db.execute("UPDATE users SET cash = ? WHERE id = ?", cash - (price * shares), user_id)

        else:
            return apology("Not enough cash", 400)

        # Redirect user to index page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    # Initiate variables
    user_id = session["user_id"]
    assets = db.execute("SELECT state, symbol, name, price, shares, time FROM transactions WHERE id = ? ORDER BY time", user_id)

    # Render apology if record doesn't exist
    if not assets:
        return render_template("no_transactions.html")

    return render_template("history.html", assets=assets)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 400)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/change_password", methods=["GET", "POST"])
@login_required
def change_password():
    """Change password"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure password was submitted
        if not request.form.get("password"):
            return apology("must provide password", 400)

        # Ensure new password was submitted
        elif not request.form.get("new_password"):
            return apology("must provide new password", 400)

        # Ensure confirmation was submitted
        elif not request.form.get("confirmation"):
            return apology("must provide password confirmation", 400)

        # Ensure password is equivalent to password confirmation
        if request.form.get("new_password") != request.form.get("confirmation"):
            return apology("password confirmation doesn't match", 400)

        # Update user's password hash in the db
        db.execute("UPDATE users SET hash = ?", generate_password_hash(
            request.form.get("new_password"), method='pbkdf2:sha256', salt_length=8))

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("change_password.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        quote = lookup(request.form.get("symbol"))

        if not quote:
            return apology("Invalid stock symbol, Please try again", 400)

        return render_template("quoted.html", quote=quote)

    else:
        return render_template("quote.html")


@app.route("/deposit", methods=["GET", "POST"])
@login_required
def deposit():
    """Allow users to additionally deposit."""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        deposit = int(request.form.get("deposit"))

        if not deposit:
            return apology("Invalid input, Please try again", 400)

        else:
            db.execute("UPDATE users SET cash = cash + ?", deposit)

            return redirect("/")

    else:
        return render_template("deposit.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Ensure confirmation was submitted
        elif not request.form.get("confirmation"):
            return apology("must provide password confirmation", 400)

        # Ensure password is equivalent to password confirmation
        if request.form.get("password") != request.form.get("confirmation"):
            return apology("password confirmation doesn't match", 400)

        # Ensure username doesn't exists
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        if len(rows) != 0:
            return apology("username already exists", 400)

        # Insert user to db
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", request.form.get("username"),
                   generate_password_hash(request.form.get("password"), method='pbkdf2:sha256', salt_length=8))

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    # Initiate variables
    user_id = session["user_id"]
    symbols = db.execute("SELECT symbol FROM transactions WHERE id = ? GROUP BY symbol ORDER BY symbol", user_id)

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Initiate variables
        symbol = request.form.get("symbol")
        shares = int(request.form.get("shares"))
        quote = lookup(symbol)
        name = quote["name"]
        price = quote["price"]

        time = datetime.now()
        cash = float(db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"])

        owned_shares = int(db.execute("SELECT SUM(shares) FROM transactions WHERE id = ? AND symbol = ?",
                           user_id, symbol)[0]["SUM(shares)"])

        # Ensure symbol was submitted
        if not symbol:
            return apology("must provide stock's symbol", 400)

        # Ensure valid number of shares was submitted
        elif not shares or shares <= 0:
            return apology("must provide non-negative number of shares you would like to sell", 400)

        # Ensure number of shares provided is less than owned number of shares
        elif shares > owned_shares:
            return apology("not enough shares owned", 400)

        # If the user successfully submit the form, update db
        db.execute("INSERT INTO transactions VALUES (?, ?, ?, ?, ?, ?, ?)", user_id, name, symbol, -shares, price, "sold", time)

        db.execute("UPDATE users SET cash = ? WHERE id = ?", cash + (price * shares), user_id)

        # Redirect user to index page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("sell.html", symbols=symbols)


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)

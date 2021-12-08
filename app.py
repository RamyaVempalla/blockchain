from flask import Flask, render_template, url_for,request, flash,redirect

from Main import Blockchain

chain = Blockchain()

app = Flask(__name__)
app.config['SECRET_KEY'] = "Transparency"
class Miner:
    def __init__(self,key):
        self.key = key
miner = Miner(1515)

@app.route("/")
def home_page():
    return render_template('index.html')

@app.route("/login",methods=['POST','GET'])
def login():
    if request.method =='POST':
        key = request.form.get('key')
        if int(key) == miner.key:
            flash("Logged in!")
            return render_template('mineblock.html')
        else:
            flash("Incorrect key, redirecting to home page")
            return render_template('index.html')

    return render_template('login.html')


@app.route("/mineblock", methods=['POST','GET'])
def mine_block():
    if request.method =='POST':
        VIN = request.form.get('vin')
        make = request.form.get('make')
        model = request.form.get('model')
        description = request.form.get("desc")
        chain.mine_block(chain.hash(chain.prev_block()),VIN,make,model,description)

    return render_template('mineblock.html')

@app.route("/view")
def view_page():
    results = chain.chain
    return render_template('view.html',chain_results=results)
@app.route("/verify")
def verify_page():
    results = chain.verify_chain()
    app.logger.info(results)
    return render_template('verify.html',verify_results=results)

@app.route("/lookup",methods=['POST','GET'])
def lookup_page():
    if request.method =='POST':
        VIN = request.form.get('vin_lookup')
        results = chain.lookup(VIN)
        return render_template('lookup.html',lookup_results=results)
    else:
        return render_template('lookup.html')

app.run(debug=True)
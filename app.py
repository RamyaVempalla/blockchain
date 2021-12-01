from flask import Flask, render_template, url_for,request

from Main import Blockchain

chain = Blockchain()


app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template('index.html')


@app.route("/mineblock", methods=['POST','GET'])
def mine_block():
    if request.method =='POST':
        VIN = request.form.get('vin')
        description = request.form.get("desc")
        chain.mine_block(chain.hash(chain.prev_block()),VIN,description)
    return render_template('mineblock.html')

@app.route("/view")
def view_page():
    results = chain.chain

    return render_template('view.html',chain_results=results)
@app.route("/verify")
def verify_page():
    results = chain.verify_chain()
    return render_template('verify.html',verify_results=results)


if __name__ == "__main__":
    app.run(debug=True)
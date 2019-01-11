@app.route("/user")
def get_users():
    users = ["Vincent", "Kevin"]
    resp = ["<p>{}</p>".format(user) for user in users]
    resp = "\n.join(resp)"

    return resp

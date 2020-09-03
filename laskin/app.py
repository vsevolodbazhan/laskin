import connexion

app = connexion.App(__name__, specification_dir="./specs")
app.add_api("laskin.yml")
app.run()

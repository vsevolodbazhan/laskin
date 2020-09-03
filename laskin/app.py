from http import HTTPStatus as status

import connexion


def handle_server_error(error):
    return "", status.INTERNAL_SERVER_ERROR


app = connexion.App(__name__, specification_dir="./specs")
app.add_api("laskin.yml")
app.add_error_handler(status.INTERNAL_SERVER_ERROR, handle_server_error)

application = app.app

if __name__ == "__main__":
    app.run()

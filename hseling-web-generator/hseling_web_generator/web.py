from flask import Flask, Blueprint, current_app, render_template, request

import jsonrpclib

app = Blueprint('web', __name__, template_folder='templates')


def get_server_endpoint():
    HSELING_API_ENDPOINT = current_app.config.get('HSELING_API_ENDPOINT')
    HSELING_RPC_ENDPOINT = current_app.config.get('HSELING_RPC_ENDPOINT')

    return HSELING_RPC_ENDPOINT


def get_jsonrpc_server():
    jsonrpc_endpoint = get_server_endpoint()
    return jsonrpclib.Server(jsonrpc_endpoint)


@app.route('/')
def index():
    a = int(request.args.get('a', 1))
    b = int(request.args.get('b', 2))

    server = get_jsonrpc_server()

    try:
        result = server.add(a, b)
    except ConnectionRefusedError:
        result = None

    return render_template('index.html.j2', result=result)


__all__ = [app]

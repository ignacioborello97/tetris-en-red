from flask import make_response, jsonify

def error_404(message):
    response = jsonify({
        "error":True,
        "message": message if message is not None else 'Resource Not Found'
    })
    return make_response(response, 404)

def error_500(message):
    response = jsonify({
        "error":True,
        "message": message if message is not None else 'Internal Server Error'
    })
    return make_response(response, 500)

def error_400(message):
    response = jsonify({
        "error":True,
        "message": message if message is not None else 'Invalid Request'
    })
    return make_response(response, 500)
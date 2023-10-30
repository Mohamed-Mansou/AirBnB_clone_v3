'''Status of your API'''
storage.close()

@app.errorhandler(404)
def error_404(error):
    '''Handles the 404 error code.'''
    return jsonify(error='Not found'), 404

if __name__ == "__main__":
    host = getenv('HBNB_API_HOST')
    port = getenv('HBNB_API_PORT')

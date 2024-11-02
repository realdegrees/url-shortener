from flask import Flask, request, jsonify, redirect
import db
import os
from dotenv import load_dotenv

load_dotenv()
env = os.getenv('ENV', 'development')
debug = env == 'development'
app = Flask(__name__)

@app.route('/<code>', methods=['GET'])
def redirect_url(code):
    url = db.read(code)
    if url:
        return redirect(url)
    else:
        return jsonify({"error": "Code not found"}), 404

@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.json.get('url') if request.is_json else request.args.get('url')
    if not original_url:
        return jsonify({"error": "URL is required"}), 400
    result = db.write(original_url)
    result['host'] = request.host_url # FIXME: returns a http url despite running behind a proxy using TLS
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=debug)
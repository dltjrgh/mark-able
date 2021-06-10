from flask import Flask, jsonify

app = Flask(__name__) #flask 객체 

movies = [
   {
       "name": "The Shawshank Redemption",
       "casts": ["Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler"],
       "genres": ["Drama"]
   },
   {
      "name": "The Godfather ",
      "casts": ["Marlon Brando", "Al Pacino", "James Caan", "Diane Keaton"],
      "genres": ["Crime", "Drama"]
   }
]

@app.route('/') # 접속하는 url
def index():
    return {'flask':'test'}

@app.route('/movies') # 접속하는 url
def hello_world():
    return jsonify(movies)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
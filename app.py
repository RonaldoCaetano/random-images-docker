from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
  "https://melhores-filmes-netflix.com/wp-content/uploads/2021/02/Biblioteca-Power-Rangers-deixa-Netflix-em-todo-o-mundo.jpg",
  "https://1.bp.blogspot.com/-79ynwwNRNNU/YCRSPBaLNzI/AAAAAAAAKds/kYSilyQ_7oUMGHIrzypcQb-SibzDEVx6gCLcBGAsYHQ/s790/Power-Rangers-Dino-Charge.png",
  "https://static-asset-delivery.hasbroapps.com/0000f712495e98958b3c5fece1c98fd6019cbede/99f0351ead68951f35cba9368568347a.png",
  "https://kanto.legiaodosherois.com.br/w760-h398-cfill/wp-content/uploads/2021/04/legiao_rpz6yRhKTXGS.jpg.jpeg"
]

@app.route('/')
def index():
  url = random.choice(images)
  return render_template('index.html', url=url)

if __name__ == "__main__":
  app.run(host="0.0.0.0")
from app import createapp
from app.blueprint import blueprint

app = createapp()
app.register_blueprint(blueprint)
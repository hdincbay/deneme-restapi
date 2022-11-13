from flask import Flask,  request 
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Test(Resource):
  
  def get(self):
    return {'Bilgi':'Girilen sayinin karesi'}
  
  def post(self):
    res = request.get_json()
    return {"Girilen sayi ": res}, 201


class Multi(Resource):
  
  def get(self, num):
    return {'Sonuc': num * num}
  
  
api.add_resource(Test, '/')
api.add_resource(Multi, '/sayi/<int:num>')
if __name__ == '__main__':
  app.run(host="0.0.0.0", port=81)

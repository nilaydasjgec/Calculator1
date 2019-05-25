from flask import Flask,jsonify
from flask_restful import Api, Resource, reqparse,request

import re
app = Flask(__name__)
api = Api(app)




class calculator(Resource):
    def get(self,operator):

        ist_num=float(request.args.get('first_num'))
        second_num=float(request.args.get('second_num'))

        if 'ADD'in operator.upper():
               result=ist_num+second_num
               return "Result is: {}".format(result),200
        elif 'SUB'in operator.upper():
               result = ist_num - second_num
               return "Result is: {}".format(result),200
        elif 'MULTI'in operator.upper():
               result = ist_num * second_num
               return "Result is: {}".format(result),200
        elif 'DIV'in operator.upper():
                result=ist_num/second_num
                return "Result is: {}".format(result),200
        else:
               return "Only supported operations are ADD/SUB/MULTI/DIV"
    def post(self,operator):
      return "This method not supported" ,405

api.add_resource(calculator, "/<string:operator>")
if __name__ == "__main__":
    app.run(debug=True)

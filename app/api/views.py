from rest_framework.views import APIView
from rest_framework.response import Response
from .func import validation_function
import json


class Validity_Api_2(APIView):

    validation_function = validation_function()
    def post(self, request):
        print(request.data)
        values = request.data['values']
        constraint= request.data['constraint']
        invalid_trigger = request.data['invalid_trigger']
        key = request.data['key']
        reuse = request.data['reuse']
        pick_first = request.data['pick_first']
        var_name = request.data['var_name']
        support_multiple = True
        result = validation_function.validate_numeric_entity(validation_function,values,invalid_trigger,key,support_multiple,pick_first,constraint,var_name)
        return Response(json.loads(json.dumps(result)))

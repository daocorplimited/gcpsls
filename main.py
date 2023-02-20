import functions_framework

@functions_framework.http
def serve_http(request):
   """HTTP Cloud Function.
   Args:
       request (flask.Request): The request object.
       <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
   Returns:
       The response text, or any set of values that can be turned into a
       Response object using `make_response`
       <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
   """
   request_json = request.get_json(silent=True)
   request_args = request.args
   breadcrumb = ""

   if request_json and 'name' in request_json:
       name = request_json['name']
   elif request_args and 'name' in request_args:
       name = request_args['name']
   else:
       name = request_args["url"]
       breadcrumb = func_one() + func_two() + func_three() + func_four()
       
   return 'Parsed {0}: {1}'.format(name, breadcrumb)


def func_one():

    return "step1 > "

def func_two():

    return "step2 > "

def func_three():

    return "step3 > "

def func_four():

    return "step4"

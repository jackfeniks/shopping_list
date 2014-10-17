from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render
# Create your views here.

form_html = """
<html>
<head>
	<title>Shopping list</title>
</head>
<body>
	<form method="GET">
		<h2>Add a food</h2>
		<input type="text" name="food" value="" placeholder="What to buy?">
		%s
		<input type="submit">
	</form>
</body>
</html>
"""

hidden_html = """
<input type="hidden" name="food" value="%s">
"""

shopping_list_html = """
<br>
<br>
<h2> Shopping list</h2>
<ul>
%s
</ul>
"""

class ShoppingView(View):
	# def get(self, request):
	# 	# from pdb import set_trace; set_trace()
	# 	output = form_html
	# 	hidden_output = ''
	# 	shopping_list_items = ''
	# 	for item in request.GET.getlist('food'):
	# 		hidden_output += hidden_html % item
	# 		shopping_list_items += '<li>%s</li>' % item
		
	# 	return HttpResponse(output % hidden_output + shopping_list_html%shopping_list_items)

	def get(self, request):
		return HttpResponse(render(request, 'form.html', {'food_values': request.GET.getlist('food')}))

	def post(self, request):
		return HttpResponse('Hello Post')

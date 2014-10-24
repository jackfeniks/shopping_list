from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render
# Create your views here.

# form_html = """
# 	<form method="GET">
# 		<h2>Add a food</h2>
# 		<input type="text" name="animal1" value="" placeholder="What to buy?">
# 		%s
# 		<input type="submit">
# 	</form>
# """

# hidden_html = """
# <input type="hidden" name="food" value="%s">
# """

# shopping_list_html = """
# <br>
# <br>
# <h2> Shopping list</h2>
# <ul>
# %s
# </ul>
# """

class ShoppingView(View):
	# def get(self, request):
	# 	output = form_html
		
	# 	return HttpResponse(output)


	def get(self, request):
		# items = ['q1', 'q2', 'string', 'char', 'llll']
		items = range(1,60)
		result = []

		for item in items:
			if item % 3 == 0:
				result.append('fizz')
			else:
				result.append(item)
				continue

			if item % 5 == 0:
				result.append('buzz')
			else:
				result.append(item)
				continue
			if item % 15 == 0:
				result.append('fizzbuzz')
			else:
				result.append(item)

			# fizz buzz fizzbuzz
		return HttpResponse(render(request, 'shopping_list.html', 
			{'name': request.GET['name'],
			'items': result}))
			# 'animal2': request.GET.get('animal2') }))


	def post(self, request):
		return HttpResponse('Hello Post')







	# def get(self, request):
	# 	return HttpResponse(render(request, 'form.html', {'food_values': request.GET.getlist('food')}))

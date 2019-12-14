from django.shortcuts import render, HttpResponse

html_base = """
<h1>Mi web personal</h1>
<ul>
	<li><a href="/">Portada</a></li>
	<li><a href="/about-me/">Acerca de mi</a></li>
	<li><a href="/portfolio/">Portafolio</a></li>
	<li><a href="/contact/">Contacto</a></li>
</ul>
"""


def home(request):	
	return render(request, "core/home.html")

def about(request):
	return HttpResponse(html_base+"""
		<h2>acerca de</h2>
		<p>Me llamo Luis y soy Cienctifico de la computadora</p>
		""")

def portfolio(request):	
	return HttpResponse(html_base+"""
		<h2>Portafolio</h2>
		<p>Alguno de mis trabajos</p>
		""")

def contact(request):
	return HttpResponse(html_base+"""
		<h2>Contacto</h2>
		<p>gordototuma@gmail.com</p>
		""")



from django.http import HttpResponse

# Create your views here.
def home(request):
	html = '''
		<!DOCTYPE html>
		<html lang="en">
		  <head>
			<!-- Required meta tags -->
			<meta charset="utf-8">
			<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

			<!-- Bootstrap CSS -->
			<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

			<title>Hello, world ^_^!</title>
		  </head>
		 <body style='background-color:#DDD'>
			<div class='container'>
				<div class='row'>
					<div class='col text-center'>
					<h1 class='my-4'>Uh oh, Look Out!</h1>
					<img class='my-2 image-responsive' style='border:1px solid black; height:24em' src='http://3.bp.blogspot.com/-jPuKVgHNiFk/UCrfPQ6eLZI/AAAAAAAABq0/vxUlNk3yf6E/s1600/Janelle.jpg' alt='Neil deGrasse Tyson'/>
					<h2 class="my-4" >There's a Landing Page Loaded Here!</h2>
					<a href="/scrape"><button class='btn btn-primary mx-3'>Scraper</button></a>
					<a href="/polls"><button class='btn btn-secondary'>Vote</button></a>
					</div>
				</div>
			</div>
		</body>
		</html>
	'''
	return HttpResponse(html)
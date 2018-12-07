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
					<h1 class='my-4'>Uh oh, look out!</h1>
					<img class='my-2' style='border:1px solid black' src='https://tromoticons.files.wordpress.com/2012/12/neil.jpg' alt='Neil deGrasse Tyson'/>
					<h2 class="my-4" >We have a Landing Page here!</h2>
					<a href="/scrape"><button class='btn btn-primary mx-3'>Scraper</button></a>
					<a href="/polls"><button class='btn btn-secondary'>Vote</button></a>
					</div>
				</div>
			</div>
		</body>
		</html>
	'''
	return HttpResponse(html)
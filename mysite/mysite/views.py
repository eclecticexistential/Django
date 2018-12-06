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
		 <body>
			<div class='container'>
				<div class='row'>
					<div class='col text-center'>
					<h1>Uh oh, look out!</h1>
					<img src='https://tromoticons.files.wordpress.com/2012/12/neil.jpg' alt='Neil deGrasse Tyson'/>
					<h2 class="my-4" >We have a Landing Page here!</h2>
					<a href="/scrape"><button>Scraper</button></a>
					<a href="/polls"><button>Vote</button></a>
					</div>
				</div>
			</div>
		</body>
		</html>
	'''
	return HttpResponse(html)
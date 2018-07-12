Alpha = 1
base = open('index.html', 'w')
for x in range(1, 2):
	base.write("""
	<!DOCTYPE html>
<html>
	<head>
		<!-- En-tête de la page -->
		<meta charset="utf-8" /> <!-- permet l'utilisation de caractère spéciaux -->
		<link rel="stylesheet" href="style.css" />
		<title></title>
	</head>
	
	<body>
		<!-- Corps de la page -->
		<header>
			<!-- en-tête de la page -->
			
		</header>
		<section>

		</section>
		<footer>
			<!-- pied de la page -->
			
		</footer>
	</body>
</html>
			""")
	Alpha += 1
base.close()

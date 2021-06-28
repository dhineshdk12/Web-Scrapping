>>> from urllib.request import urlopen
>>> url = "http://olympus.realpython.org/profiles/aphrodite">>> page = urlopen(url)
>>> page = urlopen(url)
>>> page
<http.client.HTTPResponse object at 0x105fef820>
>>> html_bytes = page.read()
>>> html = html_bytes.decode("utf-8")
>>> print(html)
<html>
<head>
<title>Profile: Aphrodite</title>
</head>
<body bgcolor="yellow">
<center>
<br><br>
<img src="/static/aphrodite.gif" />
<h2>Name: Aphrodite</h2>
<br><br>
Favorite animal: Dove
<br><br>
Favorite color: Red
<br><br>
Hometown: Mount Olympus
</center>
</body>
</html>
>>> title_index = html.find("<title>")
>>> title_index
14
>>> start_index = title_index + len("<title>")
>>> start_index
21
>>> end_index = html.find("</title>")
>>> end_index
39
>>> title = html[start_index:end_index]
>>> title
'Profile: Aphrodite'















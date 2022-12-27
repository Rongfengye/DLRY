# DLRY
Rong Feng Ye, Dylan Lai Winter Attempt at building a website


upload logos to the public folder

make a console, footer, image skelton for the layout component in components

then make pages components under /pages before routing them in index.js


https://timmyomahony.com/blog/static-vs-media-and-root-vs-path-in-django
NOTE ABOUT THE FILE STORAGE

The media folder is supposed to hold things like images, downloads and other material that might be uploaded during normal use of the website 

The static folder is supposed to hold all the CSS/JS and other material that is part of the development of the site

Settings.py
MEDIA_ROOT is the ABSOLUTE SERVER PATH to the static folder mentioned above, should be something like:
MEDIA_ROOT = "/User/Bob/Sites.MySeite/Project_root/media/"

MEDIA_URL is the RELATIVE BROWSER URL you should access your media files from when you are looking at the site. Should be 
MEDIA_URL = "/media/"
which means all material can be viewed at http://example.com/media/

STATIC_ROOT should be something like
STATIC_ROOT = "/User/Bob/Sites/MySite/Project_root/static/"

STATIC_URL = "/static/"

Servering the files:
Now that you have told django where these folders should be, and the correct URLs to access them, you need to server all requests to the folders correctly

Usually when you are in production, you want the webserver to take care of serving your static files and media files

If you are developing though, you can just get the django development server to serve them for you,
this you can accomplish by adding to the URL patterns


IDEALLY IF YOU HAVE SEPARATE APPS
each with their own CSS and JS files, you might not want to throw them into one single /static/ folder. It might be useful to put them in subfolders of the apps they belong to:

/app1/static/ # specific static folder
/app2/static/

/media/
/static/ # Root static folder

Now your development server is only looking for static files where you told it to look (the root static folder) so you need to collect all the files in the subfolders and copy them to the root static folder. You could do this by hand, but Django provides a command to do this for you 

./manage collect static






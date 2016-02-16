#CritBook

CritBook is the result of working many years at DreamWorks Animation and wanting a convenient way to keep up with my notes from dailies. Despite being given spiral notebooks and various online tools, nothing gave us the ability to associate an image with our notes. CritBook is a quick proof-of-concept for such a tool, and adds the ability to label the areas of interest in the image, as well as add and delete notes, mark notes completed, and add, delete and edit existing critiques. The initial version was built in a couple of weeks using Django 1.8 with Python 2.7, MySQL, Jquery and Sass.

View the working prototype here: https://artcoder.pythonanywhere.com/critbook/

Please check the About page for limitations of the public prototype.

##Requirements

* Django 1.8
* Python 2.7
* Jquery
* Jquery UI

Sass is not required, unless you want to modify the included scss files. A Sass-generated CSS file is already included. This app
was built using MySQL but you could configure it to use your own database.

##Settings

The settings.py file includes placeholders for database settings. You will need to modify this to suit your own configuration.

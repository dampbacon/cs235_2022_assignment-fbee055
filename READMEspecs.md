# COMPSCI 235 Assignment 2 plans and ideas

![alt text](https://imgs.xkcd.com/comics/python.png)


# todo C:
* make single track browser first, last, next, prev links into buttons, use jinja to disable button(unclickable and faded out a bit) if on first or last track
* use jinja and create css class tag to style top bar items color depending which url is active. for example on when on '/track/list' color the 'Browse tracks list' top bar item white
* py test tests
* nice html css everything
* the collapsed top bar when screen small does nothing, needa fix
* error handling, redirect 404 errors to a template that extends base template so that the website doesn't just end itself everytime there is an error
* <h1>somewhat unnecasary:</h1>
```diff 
@@ implementing a tupple to sort by, by modifying lambda function in the @@
@@ track_methods sorting functions to give uppercase precedence as it currently sorts @@
@@ by string.upper which will make it jumble tracks same names(a few in data set) example: @@

- un_sortedlist['Apples','apples','Apples','apples','1235'] --> 
! sortedlist['1235','Apples','apples','Apples','apples'] 
@@ when we want...... @@
+ sortedlist['1235','Apples','Apples','apples','apples'] 
```

# todo B:
* make search at top bar functional and return results after searching album name, track name and artist name. Include a drop down to search choose where to search (all, track name, artist name, album name). The returned result links takes you to single track view, unlike table search.
* wtf-flask forms stuff

### graded:
 > * search/display based on tracks based on 
artists, genres, album 
etc.
 > * Reviewing tracks
 > * Registering, logging 
in/logging out users
 > * Use of authentication 
techniques
 > * Use of HTML forms / 
WTForms

# implemented:
* blueprints
* datatables table implented with ajax 
  > * has sortable columns, search and pagination 
* single track browser
  > * has sort by track name, album name and artist name. 
  > * Buttons to be but currently just links are first, last, next, previous. 
  > * Bookmarks exist for each sorted order, for example: sorted by artist name, if you click 'A' it takes you to first artist with a. 
  > * Boomarks generated only for unique characters in string the which the sorted list is sorted by.
* basic homepage
  > * topbar links to single track browser, table and home
  > * home is a splash screen with data stats

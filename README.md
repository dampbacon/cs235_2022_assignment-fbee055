# COMPSCI 235 Assignment 2 plans and ideas


## todo c
* py test tests
* nice html css everything
* the collapsed top bar when screen small does nothing, needa fix
* error handling, redirect 404 errors to a template that extends base template so that the website doesn't just end itself everytime there is an error
* <h1>somewhat unnecasary:</h1>
```diff 
+ implementing a tupple by modifying lambda function in the 
+ track_methods sorting functions to give uppercase precedence as it currently sorts 
+ by string.upper which will make it jumble tracks same names(a few in data set) example:  
- un_sortedlist['Apples','apples','Apples','apples','1235'] --> 
! sortedlist['1235','Apples','apples','Apples','apples'] 
```

## todo b
* make search at top bar functional and return results after searching album name, track name and artist name. Include a drop down to search choose where to search (all, track name, artist name, album name). The returned result links takes you to single track view, unlike table search.
* wtf-flask forms stuff
* user sessions flask stuff

## implemented
* datatables table implented with ajax has sortable columns, search and pagination 
* single track browser has sort by track name, album name and artist name. Buttons to be but currently just links are first, last, next, previous. Bookmarks exist for each sorted order, for example: sorted by artist name, if you click 'A' it takes you to first artist with a. Boomarks generated only for unique characters in string the which the sorted list is sorted by.
* basic homepage

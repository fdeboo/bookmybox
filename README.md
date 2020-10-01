<div align="center">

<img src="wireframes/mockup.png" alt="Mockup on all Devices"/>
 
 </div>

# Table of contents
1. [Introduction](#introduction)
    * [Objective](#objective)
    * [User stories](#users)
    * [Wireframes](#wireframes)
    * [Design Notes](#design)
2. [UX](#design)
3. [Features](#features)
    * [Existing Features](#existing_feat)
    * [Features left to implment](#future_feat)
4. [Information Architecture](#models)
    * [Users](#users)
    * [Cities](#cities)
5. [Technologies Used](#technologies)
6. [Testing](#testing)
7. [Deployment](#deployment)
8. [Credits](#credits)
    * [Content](#content)
    * [Media](#media)
    * [Acknowledgements](#acknowledgements)

## Introduction <a name="introduction"></a>

#### Objective <a name="strategy"></a>
+ This app provides a platform for private members to book their hospitality package for upcoming events at a fictional venue  


#### User Stories <a name="users"></a>
"As a box owner, I would like to ___________"
+ View upcoming events 
+ Sort the events by category
+ View individual events in more detail
+ Reserve my box for an upcoming event
+ View different food packages
+ Select a food package
+ Select a drinks package
+ Provide details of the number of guests attending and dietary requirements
+ Review order before placing it
+ Easily Enter Payment information
+ Feel my personal and payment information is secure
+ View my order confirmation after checkout
+ Receive a confirmation email after the checokout is complete
+ Cancel my reservation
+ Modifiy my reservation details
+ View my order history


"As a hospitality manager I would like to _________"
+ Create new members and provide them a one time login
+ Add new events that have been announced
+ Add and update food packages for the year ahead
+ Add and update drinks packages for the year ahead



#### Wireframes <a name="wireframes"></a>
+ The navigation bar will be contained within the header and will have a transparent background so that the so that the hero-image in the header is visible beneath.
+ The header will contain the search bar so it accessible on whichever page the user has navigated to.
+ The content section is where the page templates are displayed. All templates will have a top margin of 50px to space it from the header.
+ The footer has a 'sticky' position so that even if the content does not fill the viewport height, the footer will remain anchored at the bottom of the screen.


<div align="center">

Display on large screens: <br /><br />
  <img src="wireframes/mainlayout.png">

</div>


<div align="center">
Display on mobile devices: <br /><br />
  <img src="wireframes/mainlayout-mobile.png">

</div>


+ The home page will display all the locations in the database as cards and will also contain image backgrounds to add colour to the page
+ A animated reel looping through all the user suggestions will be displayed on the home page as example posts.
+ A button invites users to add location to the database if it doesn't already exist
+ Any searches made will direct to the home page and the location card that matches the search will be displayed
+ If no results in a search are found, the home page sontent is replace by a "No results found message"
+ Admin users will be able to see links on the cards that enable them to change the location's associated image or delete the location from the database

<div align="center">

Home template for large screens: <br /><br />
  <img src="wireframes/home.png">

</div>


<div align="center">

Home template for mobile screens: <br /><br />
  <img src="wireframes/home-mobile.png">

</div>


An admin user view: <br /><br />
  <img src="wireframes/adminviewe.png">

</div>

+ The thingstodo page will display all the suggestions that have been added for the selected location
+ A filter form allows the results to be refined. When any of the checkboxes are checked, the page updates the results automatically.
+ Once filters are applied, the selected filters are displayed in a list and can be cleared on the click on a link
+ Pagination limits the number of results per page and provides links to the next set of results.
+ The suggestions can be clicked to expand the result and display the information provided by the user author. 
+ If no cost or url provided, the field is left blank
+ Any admin user, or author of the selected content can edit or delete the suggestion record
+ If a user posted a suggestion but since deleted their account, the roundel displaying their profile picture is replaced with a default picture

<div align="center">

Thingstodo template for large screens: <br /><br />
  <img src="wireframes/thingstodo.png">

</div>
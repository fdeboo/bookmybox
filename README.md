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
    * 
5. [Technologies Used](#technologies)
6. [Testing](#testing)
7. [Deployment](#deployment)
8. [Credits](#credits)
    * [Content](#content)
    * [Media](#media)
    * [Acknowledgements](#acknowledgements)

## Introduction <a name="introduction"></a>

### Objective <a name="strategy"></a>
+ This app provides a platform for private members at an events venue to reserve their hospitality package for upcoming events  


### User Stories <a name="users"></a>
"As a box owner, I would like to ___________"
+ View the upcoming events 
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
+ Add new events that have just been announced
+ Add and update food packages for the year ahead
+ Add and update drinks packages for the year ahead



### Wireframes <a name="wireframes"></a>
<div align="center">

<img src="wireframes/login.png" alt="login view"/>
 
 </div>

## Information Architecture <a name="models"></a>
### Models

<div align="center">

<img src="wireframes/schema_v2.png" alt="schemav2"/>
<img src="wireframes/schema.png" alt="schema"/>
 
 </div>

***

<p>&nbsp;</p>

### Profile:

<p>&nbsp;</p>

#### Box

| Name          | Key in db     | Field Type   | Validation                |
|:--------------|:--------------|:-------------|:--------------------------|
| Box Number    | box_num       | IntegerField |                           |
| Box Capacity  | box_capacity  | IntegerField | max_value=24, blank=True  |

<p>&nbsp;</p>

#### Account

| Name        | Key in db   | Field Type         | Validation                 |
|:------------|:------------|:-------------------|:---------------------------|
| Box         | box         | OneToOneField(Box) |                            |
| Name        | name        | CharField          | max_length=75              |
| Email       | email       | EmailField         | max_length=75              |
| Address 1   | address1    | CharField          | max_length=75              |
| Address 2   | address2    | CharField          | max_length=500, blank=True |
| Postcode    | postcode    | CharField          | max_length=75              |
| City        | city        | CharField          | max_length=75              |
| Country     | country     | CharField          | max_length=75              |

<p>&nbsp;</p>

* * *

<p>&nbsp;</p>

### Events:

<p>&nbsp;</p>

#### Category

| Name          | Key in db     | Field Type | Validation                |
|:--------------|:--------------|:-----------|:--------------------------|
| Name          | category_name | CharField  | max_length=75             |
| Friendly Name | friendly_name | CharField  | max_length=75, blank=True |

<p>&nbsp;</p>

#### Event

| Name        | Key in db   | Field Type                                   | Validation                 |
|:------------|:------------|:---------------------------------------------|:---------------------------|
| Name        | event_name  | CharField                                    | max_length=75              |
| Date        | date        | DateTimeField                                |                            |
| Category    | event_type  | ForeignKey(Category)                         | on_delete=""               |
| Description | description | TextField                                    | max_length=500, blank=True |
| Image_url   | image_url   | UrlField                                     | blank=True                 |
| Image       | image       | ImageField                                   | blank=True                 |
| Boxes       | boxes       | ManyToManyField(Box, through='Reservations') | blank=True                 |

<p>&nbsp;</p>

* * *

<p>&nbsp;</p>

### Reservations:

<p>&nbsp;</p>

#### Food Package

| Name  | Key in db | Field Type   | Validation                                            |
|:------|:----------|:-------------|:------------------------------------------------------|
| Type  | title     | CharField    | max_length=75, blank=False                            |
| Price | price     | DecimalField | max_digits=6, decimal_places=2, null=False, default=0 |


<p>&nbsp;</p>

#### Drinks Package

| Name  | Key in db | Field Type   | Validation                                            |
|:------|:----------|:-------------|:------------------------------------------------------|
| Type  | title     | CharField    | max_length=75, blank=False                            |
| Price | price     | DecimalField | max_digits=6, decimal_places=2, null=False, default=0 |


<p>&nbsp;</p>

#### Reservation:


| Name           | Key in db     | Field Type         | Validation                 |
|:---------------|:--------------|:-------------------|:---------------------------|
| Box            | box           | ForeignKey(Box)    | max_length=75              |
| Event          | event         | ForeignKey(Event)  |                            |
| Guests         | guests_no     | IntegerField       |                            |
| Food Package   | food_package  | ForeignKey(Food)   | max_length=500, blank=True |
| Drinks Package | drink_package | ForeignKey(Drinks) | blank=True                 |




<p>&nbsp;</p>

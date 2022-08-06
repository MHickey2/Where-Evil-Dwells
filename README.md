![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Where Evil Dwells: Milestone 3 Project

<p align ="center">      
     <img src=""  alt="" />    
</p>
<br/>  

 
## Introduction <a name="introduction"></a>
Where Evil Dwells is a Text Based Adventure for a Command Line Interface. It is utilizing the python language.
The Game is a murder mystery based in a Creepy House. The Player acts as the protagonist and will drive the direction of the game. The decision making will allow the player to interact with characters and can experience different scenarios according to their choices. This is an original story based on the vintage horror/thriller genre with inspiration from the classic movie, 'Murder by Death'. The goal of the game is to make it to the end of the game alive aand be able to get the inheritance on offer. The hope is that the game will offer the player an interactive and fun experience, that they can repeat and experience it differently depending on different choices.

<br/>

[Visit the Where Evil Dwells Site](https://where-evil-dwells.herokuapp.com/)  

[Visit the Where Evil Dwells Repository](https://github.com/MHickey2/Where-Evil-Dwells)  
<br/>    

# Table of Contents <a name="toc"></a>

1. [UX Strategy](#uxstrategy)
    1. [Business Goals](#businessgoals)
    2. [Target Customer](#targetcustomer)
2. [User Stories](#userstories)
    1. [First Time User](#firsttimeuser)
    2. [Regular User](#regularuser)
    3. [Site Owner](#siteowner)
3.  [Layout and Logic](#layout)
    1. [Colour Scheme](#colourscheme)
    2. [UX experience](#UX)
    3. [Graphics](#graphics)
4.  [Flow Chart for Game](#flowchart)        
5.  [Features](#features)
    1. [Index Page](#intropage)    
6.  [Future Implementation](#future)
7.  [Tools and Technology](#technology)
8.  [Testing](#testing)
9.  [Bugs and Issues](#bugs)
    1. [Resolved](#resolved)
    2. [Unresolved](#unresolved)
10. [Deployment](#deployment)
    1. [Make Local Clone](#clone)
    2. [Student Template](#studenttemplate)
    3. [Deploying to Heroku](#heroku)
11.  [Credits](#credits)
12.  [Acknowledgements](#acknowledgements)

----

## UX Strategy <a name="uxstrategy"></a>

<br/> 

### The Business Goals of the Website: <a name="businessgoals"></a>
- No commercial goals, but the site's goal is to to provide an interactive Choose your Own Adventure.
  
  <br/> 

### The Target Customer: <a name="targetcustomer"></a>
- The audience of the site could encompass a number of age groups and there would generally not be any   limitation on who could avail of the quiz.
- Would probably require some access to digital technology.
- May be useful for a user who has spare time and enjoys using decision making to solve a mystery.
- Someone who likes interaction in their gaming.

 <br/>  

 #### [Return to Table of Contents](#toc)
----
## User Stories  <a name="userstories"></a>
### As a first time user to this site, I want to …..<a name="firsttimeuser"></a>
- Understand how the Game Works.
- Play the Game.
- If I want to restart a Game, I want to be able to do this easily.
  

  <br/>

### As a regular user of the site, I want to …...  <a name="regularuser"></a>  
- I want to try the various scenarios to navigate through the game.
- I want to try all the options not selected before, to have different experiences.  
- I want to have more complexity and a greater range of scenarios. 
   

 <br/>

### As the site owner, I want to …..    <a name="siteowner"></a>
- Build more complexity in the game, so it is more challenging to the user.
- Add more scenarios to give the user a wider range of experiences within the game.
- Offer a wider range of settings.
- In the present game, the killer is picked at random, so clues would be unhelpful, 
 but in future games, clues and red herrings could be added to create more of an 
 investigative  experience, where the killer can be identified by the player.
- Add more complexity to enhance the experience of the users.
- Provide the user with ways that they can encounter greater decision making experience.
  

  <br/>  
----
## Layout  <a name="layout"></a> 

<br/>

## Colour Scheme    <a name="colourscheme"></a>  
The colour scheme encompasses the html page and the interface screen. I wanted to have a background image that resonates with the theme of the game. I simply applied a background image of a creepy house. In regards to the interface i added aasci art images to supplement the settings depicted in the text. The background colours were used to make certain elements stand out i.e. the letter. Colour was applied to text input lines, to make them stand out from the rest of the flow of text.

## UX Experience    <a name="ux"></a>
- The Player is given instructions on what they need to do in the game.
- The player is prompted when a decision needs to be made.
- The prompts are designed to stand out from the rest of the text.
-  

## Graphics    <a name="graphics"></a>
 #### [Return to Table of Contents](#toc)
----

## Flow Chart for the Game  <a name="flowchart"></a>

  


 #### [Return to Table of Contents](#toc)
----
## Features  <a name="features"></a>

 #### [Return to Table of Contents](#toc)
----
 ## Future Implementation  <a name="future"></a>

 #### [Return to Table of Contents](#toc)
----
 ## Tools and Technology  <a name="technology"></a>

 #### [Return to Table of Contents](#toc)
----
## Testing  <a name="testing"></a>

 #### [Return to Table of Contents](#toc)
----
 ## Bugs and Issues  <a name="bugs"></a>

 ### Resolved <a name="resolved"></a>

 ### Unresolved <a name="unresolved"></a>

 #### [Return to Table of Contents](#toc)
----
 ## Deployment <a name="deployment"></a>

 ### Cloning <a name="clone"></a>

 ### Student Temlate <a name="studenttemplate"></a>
 ### Deploying to Heroku <a name="heroku"></a>

#### [Return to Table of Contents](#toc)
----
 ## Credits <a name="credits"></a>
#### [Return to Table of Contents](#toc)
----
 ## Acknowledgements <a name="acknowledgements"></a>


 #### [Return to Table of Contents](#toc) 


 
## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!
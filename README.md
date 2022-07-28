## 3D Models Manager

    This web application is developed on Angular 7.3.1 and Django 4.0.6(Django Rest framework 3.13.1) 
    in which we can upload and view 3D models saved in .glb and .fbx format which are exported
     from Blender and 3ds MAX like Apps and also available on Sketchfab.com like websites.

    Both front end and backend is developed following best practices.

    App has almost perfect input validations and a beautiful and responsive Bootstrap styled UI which is able 
    to run offline because Bootstrap style css file is saved in the Angular project.
    This app can be run on any device which supports Mozilla Firefox or Google Chrome browsers.

#### This repository is DRF(Django Rest Framework) API server for this App.

## Running this App on your local system server:

#### 1. I have used Ubuntu 20.4 LTS to develop and deploy it. For Windows you can use Ubuntu 20.4 in WSL or in a Virtual Machine Software like Oracle Virtual Box. Still I'll try to update soon about how to run it in Windows.
#### 2. Downlaod or clone this git repository which is the server developed in Django rest framework API for our app.
#### 3. Open up the Terminal in the project root folder.
#### 4. To activate virtual python environment enter this command: source venv/bin/activate
#### 5. To run our API on local server we have to edit some configs in settings.py in tdm/ folder of our project.
###### Open up settings.py in visual studio code or your favorite IDE and do the following
###### Go to the bottom end of the code or on line 150 you will find CORS_ORIGIN_ALLOW_ALL variable
###### Make it True like CORS_ORIGIN_ALLOW_ALL = True
###### Uncomment SECRET_KEY variable if it is commented
###### Uncomment or add "https://localhost:4200" local server URL in CORS_ALLOWED_ORIGINS variable
 
#### 6. Now run API on http://localhost:8000/ or http://127.0.0.1:8000/ by entering this command: python manage.py runserver
#### 7. You can check API working on http://localhost:8000/tdmodels/ in chrome, Firefox or GET request in Postman App which will return a file name in JSON formate.


#### 8. The Angular app is on this repostory download or clone it from here: https://github.com/waqardongre/tdmangularglitchapp
#### 9. We have to run this frontend Angular project in local. to do so do the following:
###### Open up this Angular project in your another window of the IDE or in a different IDE and open up global.js file in this path /src/app/ in the project root folder.
###### Comment this line of code: export const DJANGO_SERVER = "https://tdmdjangoapi.herokuapp.com/"
###### Uncomment this line of code: export const DJANGO_SERVER = "http://localhost:8000/"
###### Now open up the terminal in the same IDE window and enter this code: ng serve
###### Open up this URL http://localhost:4200/ in Chrome or Firefox. The app should be running.
###### To confirm app is working API open up web developer tool in the browser, if you see "uploadService.getAll observable: ["initializing_file.txt"]" in console the App is working. You can try upload or view 3D models in it.

## Deploying it online:

#### 10. To make the Angular App live, do almost the opposite of step 9:
###### Open up global.js file in this path /src/app/ in the Angular project root folder.
###### Uncomment this line of code: export const DJANGO_SERVER = "https://tdmdjangoapi.herokuapp.com/"
###### Comment this line of code: export const DJANGO_SERVER = "http://localhost:8000/"
###### Create an account on glitch.com, download git cli, create a git repository and push it in cli same as we push other git repositories. 
###### Go to glitch.com , in create new project tab on top right corner select import from git and paste your git repository URL there. It will load your git code. 
###### Copy your apps live URL from glitch project share button on the top right corner and save it somewhere we will need it while deploying Django API in the next step no 11.
###### This App wont work on the copied glitch live URL becuase we need to paste that URL in our Django API project to get access to API by our glitch URL and that is we are going to do next.  

#### 11. To make the Dajngo API live do almost the opposite of step 5:
###### Open up settings.py in Dajngo project folder tdm/ in visual studio code or your favorite IDE and do the following
###### Go to the bottom end of the code or on line 150 you will find CORS_ORIGIN_ALLOW_ALL variable
###### Make it False like CORS_ORIGIN_ALLOW_ALL = False
###### Comment SECRET_KEY variable if it is uncommented because for heroku server it is saved in .env file.
###### Comment or remove "https://localhost:4200" local server URL in CORS_ALLOWED_ORIGINS variable
###### Add or update Glitch Angular live URL which you copied in step 10 in CORS_ALLOWED_ORIGINS variable
###### Create an account on heroku.com, download heroku cli, create heroku app and push it in cli as same as we push some code to a git repository, heroku will build the Django API and share the live URL.
###### Now open up your Glitch Angular live URL which you copied in step 10, your app should be running on this URL of Glitch live server.

#### If you have any queries about this App feel free to reach me out at this email: waqardongre@gmail.com


#### More related code links:
    
    Live App: Glitch: https://boom-defiant-radon.glitch.me
    
    
    Angular 7.3.1 App frontend:
        Glitch live: https://boom-defiant-radon.glitch.me
        Glitch code: https://glitch.com/edit/#!/boom-defiant-radon
        Github rep.: https://github.com/waqardongre/tdmangularglitchapp

    Django 4.0.6 - Django Rest framework 3.13.1 - Api backend Server:
        Heroku live: https://tdmdjangoapi.herokuapp.com
        Heroku live page: https://tdmdjangoapi.herokuapp.com/tdmodels/
        Git rep.: https://github.com/waqardongre/tdmdjangoherokuapi.git
        Git-Heroku rep.: https://git.heroku.com/tdmdjangoapi.git


Thanks for reading it.
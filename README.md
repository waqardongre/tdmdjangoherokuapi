3D Models Manager

    This is a web application made on Angular 7.3.1 and Django Rest Framework 4.0.6(Django Rest framework 3.13.1) in which we can upload and view 3D models     saved in .glb and .fbx format.

    Both Front end and backend is developed following best practices.

    App have perfect input validations and a Beautiful Bootstrab styled UI which is able to run offline because Bootstrab style css file is saved in           Angular project.

This repository is DRF(Django Rest Framework) API server for this App.

To run this project on your local system follow below instructions:

1. I have used Ubuntu 20.4 LTS to develop and deploy it. For Windows its almost same procedure but I'll update soon how to run it in Windows.
2. Downlaod or clone this git repository which is the server developed in Django rest framework API for our app.
3. Open Terminal in the project root folder.
4. To activate virtual python environment enter this command: source venv/bin/activate
5. To run our API on local server we have to edit some configs in settings.py in tdm/ folder of our project.
    Open settings.py in visual studio code or your favorite IDE and do the following
        Go to the bottom end of the code or on line 150 you will find CORS_ORIGIN_ALLOW_ALL variable
        Make it True like CORS_ORIGIN_ALLOW_ALL = True
        Uncomment SECRET_KEY variable if it is commented
        Uncomment or add "https://localhost:4200" local server link in CORS_ALLOWED_ORIGINS variable
 
6. Now run API on http://localhost:8000/ or http://127.0.0.1:8000/ by entering this command: python manage.py runserver
7. You can check API working on http://localhost:8000/tdmodels/ in chrome, Firefox or GET request in Postman App which will return a file name in JSON formate.

8. The Angular app is on this repostory download or clone it from here: https://github.com/waqardongre/tdmangularglitchapp
9. We have to run this frontend Angular project in local. to do so do the following:
    Open this Angular project in your another window of the IDE or in a different IDE and open global.js file in this path /src/app/ 
    in the project root folder.
    Comment this line of code: export const DJANGO_SERVER = "https://tdmdjangoapi.herokuapp.com/"
    Uncomment this line of code: export const DJANGO_SERVER = "http://localhost:8000/"

    Now open terminal in the same IDE window and enter this code: ng serve
    open this link http://localhost:4200/ in Chrome or Firefox. App should be running.
    To confirm app is working API open up web developer tool in the browser, if you see "uploadService.getAll observable: ["initializing_file.txt"]"
    in console the App is working. You can try upload or view 3D models in it.

Thanks for reading it.

More related code links:
Live App: Glitch live: https://boom-defiant-radon.glitch.me
    
    Angular 7.3.1 App frontend:
        Glitch live: https://boom-defiant-radon.glitch.me
        Glitch code: https://glitch.com/edit/#!/boom-defiant-radon
        Github rep.: https://github.com/waqardongre/tdmangularglitchapp

    Django 4.0.6 - Django Rest framework 3.13.1 - Api backend Server:
        Heroku live: https://tdmdjangoapi.herokuapp.com
        Heroku live page: https://tdmdjangoapi.herokuapp.com/tdmodels/
        Git rep.: https://github.com/waqardongre/tdmdjangoherokuapi.git
        Git-Heroku rep.: https://git.heroku.com/tdmdjangoapi.git

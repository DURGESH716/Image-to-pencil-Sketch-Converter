# :heart: Pic<2>Sketch :heart: [![Project Status: Active](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active) [![](https://img.shields.io/badge/Prateek-Ralhan-brightgreen.svg?colorB=ff0000)](https://prateekralhan.github.io/)

A minimalistic computer vision based Web application that makes use of some blurring and image blending (dodging and burning) techniques to generate pencil sketch like output for any image fed as input.
## Live app available [here.](https://pic2sketch.herokuapp.com)

![](https://user-images.githubusercontent.com/29462447/90712398-92a35f80-e2c0-11ea-8fe2-031a7e67a0bc.jpg)
![](https://user-images.githubusercontent.com/29462447/90712401-946d2300-e2c0-11ea-8312-b44e033bb413.jpg)


### Installation:
Simply run the command: ***pip install -r requirements.txt** 

### Usage:
1. Clone this Repository to a directory and navigate to that directory.
2. Run the command: ***python app.py***
3. This will run the web-app on localhost and would look something like this. Feel free to play around with the codes, add more features, beautify it. :wink:

![1](https://user-images.githubusercontent.com/29462447/90712408-959e5000-e2c0-11ea-876f-db71875fe0bd.png)
![2](https://user-images.githubusercontent.com/29462447/90712409-9636e680-e2c0-11ea-9b82-a7848403d54c.png)

### Deployment on Heroku:
1. Create the **Aptfile**, **Procfile**, **requirements.txt** and **runtime.txt** accordingly.
  * **Aptfile** - Acts as support for apt-based dependencies during both compile and runtime.
  * **Procfile** - Heroku apps include a Procfile that specifies the commands that are executed by the app on startup. You can use a Procfile to declare a variety of process types, like your app’s web server, multiple types of worker processes, a singleton process, such as a clock etc.
  * **requirements.txt** - This comprises of the list of all necessary python packages needed for running the web-app. Create this by: ***pip freeze > requirements.txt***
  * **runtime.txt** - specifies the Python version which was used for building the application.

3. Upload your entire web-app on github as a fresh github repository ___just the way I did here___ :smile:
4. Sign up/Sign in to your Heroku Account and choose **Create App**, provide the **app name**.
5. Go to the **deploy** tab and link your Heroku app to your GitHub repo where the webapp is located.
6. After linking , go to settings tab, scroll down to add buildpack and add the following buildpacks:
  * https://github.com/heroku/heroku-buildpack-apt.git
  * Choose **Python** buildpack from the icons as well.

7. **Save Changes.** Go to the deploy tab and deploy you app and you’re done!.

<hr>
<b>NOTE:</b>
 *  Ensure your entire web app folder structure is maintained in the same format as you see here ( as in case of Flask ).
<hr>

### Running the Dockerized App
1. Ensure you have Docker Installed and Setup in your OS (Windows/Mac/Linux). For detailed Instructions, please refer [this.](https://docs.docker.com/engine/install/)
2. Navigate to the folder where you have cloned this repository ( where the ***Dockerfile*** is present ).
3. Build the Docker Image (don't forget the dot!! :smile: ): 
```
docker build --tag sketch_app .
```
4. Run the docker:
```
docker run --publish 8000:8080 --detach --name bb sketch_app
```

This will launch the dockerized app. Navigate to ***localhost:8000*** in your browser to have a look at your application. You can check the status of your all available running dockers by:
```
docker ps
```
![1](https://user-images.githubusercontent.com/29462447/99376234-af185d80-28ea-11eb-88b2-8fd45c13d078.png)
![2](https://user-images.githubusercontent.com/29462447/99376238-b0498a80-28ea-11eb-9141-49e8845444ae.png)

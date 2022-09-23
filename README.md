# Streamlit Tutorial 👋

🎯 This Github directory aims to present the advantages of [Streamlit.io](https://streamlit.io/) in the development of a Data application, whether for the deployment of a personal project on the web or the creation of an MVP !

✏️ I wrote a Medium article that explains in detail the code of this project: available here  : Lien.

## Project Description

We will develop an application to search for trains eligible for the TGV Max subscription. (Subscription of 79 euros/month offered to young people which allows to book for free an unlimited number of eligible trains under conditions of low traffic)


![web app](https://user-images.githubusercontent.com/67114372/191899670-8783fa6d-29e3-4fb8-af4f-a1736020a3ee.png)

**The public link of the project url is [available here](https://pierre-louis-danieau-streamlit-medium-tutorial-app-kp7nxu.streamlitapp.com/) (it may be necessary to reboot the app if it is paused).**


## How to reproduce locally this Data Web App

1) Download this directory to your computer.

2) Create your directory
      ````
      mkdir project_data
      ````
3) Create your virtual environment
    ````
    python3 -m venv env
    ````

4) Activate your virtual environment
    ````
    source env/bin/activate
    ````

5) Pip update
    ````
    pip install --upgrade pip
    ````

6) Install the dependency file
    ````
    pip install -r requirements.txt
    ````
    
7) Run your streamlit project
    ````
    streamlit run app.py
    ````
    
    You should see a local web page like this

    ![local](https://user-images.githubusercontent.com/67114372/191900559-130a252d-74ff-478d-a1a3-b0dacabb0cfb.png)


## How to deploy your Web App

1) Clone this repository into your own github account.

2) Create an account on streamlit and connect your github profile so that streamlit has access to your application directory.

3) Go on streamlit and click on "New app", then fill in your directory name, your branch name and your file name app.py . Then click on "deploy".

4) After a few minutes, streamlit has deployed your application which is now accessible via a public url, congratulations ! 🎉


## Want to go further in the development of a web application ?

I have created a course on streamlit that will surely interest you to explore all the possibilities of creating a personal data project or developing an MVP !

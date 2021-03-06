![LitReview](LitProject/LitProjectPreview.jpg)

## **Description**

LitReview is a web application that brings together users passionate about
 literature.
After creating an account and logging into the application, you can see your
 own posts as well as those of your friends. You can follow other users, 
 ask for review or create your own reviews.

## **Clone the repository**

Download the repository from this link to the local folder you want: 
https://github.com/MargueriteT/LitProject.git

    Clone the repository : git clone https://github.com/MargueriteT/LitProject.git

## **Installation**

First, make sure you already have python3 install on your computer. 
If not, please go to this link: https://www.python.org/downloads/ and follow the instructions. 
Open your Cmd and proceed as indicated:
  
Navigate to your repository folder: `cd path/to/your/folder`
    
Create a virtual environment: ``python -m venv env (windows) python3 -m venv env (macos ou Linux)``

Activate this virtual environment: ``env\Scripts\activate (windows) ou source env/bin/activate (macos ou linux)``

Install project dependencies: ``pip install -r requirements.txt``

Navigate to LitProject app : ``cd LitProject/LitProject``

Create a new python file name configuration.py : ``copy con configuration.py``

Add the secret key to the file : ``SECRET_KEY = 'yoursecretkey'``

Go back to the LitProject folder : ``cd ..``

Run the program: ``python manage.py runserver``

## **Contributor**

Marguerite Teulon - as part of OpenClassrooms' Project 9:
Develop a web application using Django
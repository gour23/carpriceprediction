The first step is to download the github repository https://github.com/gour23/carpriceprediction

![1](https://user-images.githubusercontent.com/91954903/222779266-7ccf5a69-98cd-42f8-b466-2b1d00a5c13c.png)

Here we see the folder ( dataset,eda,model ) click on this folder and we see the datasets and other files.

![2](https://user-images.githubusercontent.com/91954903/222779943-bd39ff0b-5bb5-4eca-b5f6-2d62b1811cce.png)

Here we see the Different types of files where (cardekho_data.csv) is the Raw dataset used in the project , and (cleaned_data_cardekho.csv) is the cleaned dataset.

![3](https://user-images.githubusercontent.com/91954903/222780963-555f0b90-17ae-4e5a-99cb-740e236ddee6.png)

open the jupyter notebook on the same path and click on the (data_preprocessing_and_EDA.ipynb) file.
here we see the complete preprocessing on dataset.

![4](https://user-images.githubusercontent.com/91954903/222781473-0740d149-2743-4d1e-9bb1-86fae1c4f676.png)

Note : Before running this jupyter notebook please make sure to install all the third party python modules used in here and further.

[ pip install pandas,
pip install numpy,
pip install matplotlib,
pip install seaborn,
pip install scikit-learn,
pip install django ]


here you can see the step by step details on how the preprocessing is done and at the end we got our cleaned data and saved it as (cleaned_data_cardekho.csv) file.

we have cleaned the data now it's time to create the model.
click on the  ( model creation.ipynb ) file. 

![5](https://user-images.githubusercontent.com/91954903/222787916-1271612d-6d0c-4310-87f7-45504bc0ef8d.png)


here we see the complete step by step details on how we created model and saved it as a ( random_forest_regression_model.pkl ) file.

Now Model is created.

go back to the path where all files are stored

![1](https://user-images.githubusercontent.com/91954903/222779266-7ccf5a69-98cd-42f8-b466-2b1d00a5c13c.png)


Now it's time to integrate model with the web page created in Djnago.
go to the path where all the files are saved and open the VS Code there.

![6](https://user-images.githubusercontent.com/91954903/223678656-e3ff5b7f-eecb-4bed-8718-6b2d1217bc6a.png)

on clicking open with Code we see this kinda interface.

![7](https://user-images.githubusercontent.com/91954903/223680657-91510526-e67c-4760-ae71-dec1fee83328.png)

here we see (carpriceenv)  folder 
which contains virtual environment files.

You can Create your own virtual Environment and delete this existing one.
for creating virtual environment 
open the terminal 

![8](https://user-images.githubusercontent.com/91954903/223681803-f6dc188e-a615-4d1a-8177-d7a7d014df0a.png)

after that open the git bash.

![9](https://user-images.githubusercontent.com/91954903/223682484-6a2a9bc5-b2ea-40ac-8d22-01b41015c745.png)

Now we see...

![10](https://user-images.githubusercontent.com/91954903/223682888-79484114-e391-4d32-aab4-c6db855f0451.png)

Now run the following commands

![11](https://user-images.githubusercontent.com/91954903/223683612-13655220-c335-4ebb-8d90-b1bdf1faa664.png)

Now that we created the virtual environment ( in my case carpriceenv ) 

now we need to install all the libraries which are required for the project.
here we see requirements.txt file.
which contains all the virsions of different dependent libraries.
we can install all of them

for this Run the Command 
  [ pip install -r requirements.txt ]
  
and all the libraries are installed to our new Virtual Environment.

Now Simply we can run the Command 
  [ python manage.py runserver ]
  
![12](https://user-images.githubusercontent.com/91954903/223685658-22aeaa14-8c25-41f5-838f-989655fc6787.png)

follow the link...

![final](https://user-images.githubusercontent.com/91954903/223686024-0960ac43-1b2b-49fb-9e68-d89a44746b13.png)

and here we did it.

Thank You For Your Time.








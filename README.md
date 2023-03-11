# MLOps Engineer Interview Project

### **High level spec**

Data Scientist team created a Jupyter notebook `My Best Model.ipynb` that contains all the code to train, save, load and inference.
Your task is to create a REST API in python that serves the model and allows for online inference.
You should create 1 endpoint that accepts relevant input and returns the infernece results to the client.

-----

### **How to share your results?**
- [ ] Clone this repository and create your own branch to work on.
- [ ] .... develop .....
- [ ] Once you are ready, create a pull request with your code.


### **Evaluation:**
- [ ] There should be **at least** one test written and the README file should include instructions on how to execute it.
- [ ] You should provide clear documentation of the API, you can use Swagger or any other format.
- [ ] README file should include clear instructions on how to deploy / start the application.
- [ ] No crashes or bugs.
- [ ] Code is easily understood and communicative (eg. comments, variable names, etc). 
- [ ] Everything that you decide to not do due to the limitation of time should be documented in the README.
- [ ] GitHub commit history is consistent, easy to follow and understand. 

---

## Project Implementation

#### Scope
- Best Practices
	- Modular and reusable code
	- Testing the code
- Manage environment with pipenv
- Adding Dependencies in requirements.txt
- IaaS using Terraform on GCP
- Host Application (Flask)

Google Cloud Platform was chosen to develop and deploy the REST API as they provide ~$300 credits as part of free trial & c3 high compute machine type available free for preview (as of 9th March, 2023). 

### Terraform
To automate the deployment of infrastructure required for the project, Terraform was chosen. While not explicitly required, it is good practice to use an Infrastructure-as-Code (IaaC) tool like Terraform in MLOps pipelines. In case of adding more features, it will be easier to add components later on to provision more services in the cloud.  

After installing terraform & gcloud utility locally on linux pc, a service account with "Owner" permissions was created in GCP & access key json was downloaded for the environment variable:

```shell
export GOOGLE_APPLICATION_CREDENTIALS="<path to access key>"
```

& authenticated API requests to Google Cloud services using following command:

```shell
gcloud auth application-default login
```

Files *variables.tf* & *main.tf* hold information on the Google Cloud project, region, zone & configuring it to create a virtual machine with ubuntu 20.04 LTS bootdisk, a vpc with firewall, ssh access, & a static ip address. Using following commands the Infrastructure was provisioned:

```shell
terraform init
terraform plan
terraform apply
terraform destroy
```

`.gitignore` was added to prevent pushing unncessary files to repo.

#### Creating a Virtual Environment with Python 3.10

1. Virtual Environment was created using pipenv:
```shell
sudo apt install python3-pip
pip install pipenv
```

Since pipenv was installed in .local path, additional steps were added to include it in PATH.
```shell
echo 'export PATH=$PATH:/path to userdir/.local/bin' >> ~/.bashrc
```
Activated environment with:
```shell
source ~/.bashrc
```

2. Create new virtual environment with Python 3.10 & activating it:
```shell
sudo apt install python3.10
pipenv --python 3.10
pipenv shell
```
3. Install required dependecies as required in the code:
```shell
pipenv install tensorflow keras numpy jupyter
```

#### Creating python scripts from notebook

We copy the code from the jupyter notebook and create `train.py` & `predict.py`. We could use jupyter nbconvert to achieve the same but since the code is simple we proceed with copying contents manually.

To make the code modular & resuable we divide different aspects of sript operations into individual functions. 

`train.py` can be modularized into 4 different functions:

- `create_model()`: Creates a sequential neural network model with one dense layer of one unit and returns it.
- `get_data()`: Provides the data for training the neural network.
- `train_model`: Trains the neural network model on the provided data using mean squared error loss and stochastic gradient descent
- `save_model()`: Saves the provided model to the specified file (default: `model/my_best_model.h5`).

`predict.py` can be modularized into 2 different functions:

- `load_model`: Loads a saved model from the specified file (default: `model/my_best_model.h5`)
- `predict`: Uses the provided model to make predictions

We move the scripts to directory `app/`. We also create a directory `model` to store the model.

We execute the two scipts:

```shell
python train.py
python predict.py
```

Basic structure of the web application is now as given below:

```
.
├── LICENSE
├── My Best Model.ipynb
├── Pipfile
├── Pipfile.lock
├── README.md
├── app
│   ├── model
│   │   └── my_best_model.h5
│   ├── predict.py
│   └── train.py
└── terraform
    ├── main.tf
    └── variables.tf
```

To make the code more readable and for documentation purposes, docstrings were also added to each function.

Type annotations were also added for each function that add to improving code quality and can save effort in long run.

Adding logging to the modules.

#### Unit Tests

We create a folder `tests` in root of the project. We use `pytest`, a popular testing framework for executing automated tests. We install pytest as a dev dependency using:

`pipenv install --dev pytest`

We add `__init__.py` file to the app directory to make it a Python package. This allows Python to recognize the folder as a package and allows to import the modules and functions inside it.

We add 4 unit tests in 2 files with 2 unit tests in each.

`test_train.py` 

![](static/images/test_train.png)

and `test_predict.py` 

![](static/images/test_predict.png)

Also added test data with the expected results. Usually in a project we will have access to the actual features but currently we try to match the outputs to the predictions generated by the model in predict.py & assert they are equivalent.


#### Linting & Formatting

##### Pylint

To improve the code quality, we use a python library called pylint which checks the code for PEP 8 style violations, such as incorrect indentations, line length, and naming conventions, unused variables, undefined names, unused imports, and more.

We start by adding pylint extension to VS Code and add pylint to the environment:

`pipenv install --dev pylint` 

Pylint gave a couple of suggestions like to redefine the variable name for model to a different name for code clarity. Changes were made and now the code is mostly compliant according to pylint.

![](static/images/pylint_redefine_scope_suggestion.png)

We get some useful suggestions and some not so useful suggestions. We could also add `.pylintrc` file to configure pylint suggestions, disable warnings & errors but we will skip that as the code base is simple. After applying the suggested changes, the code is almost compliant with the suggestions.

##### Black

Black is a Python code formatter that automatically formats your code according to a set of rules.

We start by installing the tool as dev dependency

`pipenv install --dev black` 

Since black actually formats the code, we make sure to commit the code before we run black so in case any unwanted changes happen we can rollback.

We run command to see change suggestions from black

`black --diff .`

We found suggestions to convert single quotes to double quotes which we can ignore using `-S` to skip string normalization:

`black -S --diff .`

We found suggestions related to newlines only. 
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
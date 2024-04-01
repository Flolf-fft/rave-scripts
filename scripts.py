import subprocess

name = "GiveYourModelAName" 
dataset = "/path/to/YourDatateset" 
architecture = "v2" #["v3", "v2", "v1", "discrete", "onnx", "raspberry" ]
regularization = "wasserstein" # ["default", "wasserstein", "spherical"]
channels = 1 #Number of audio channels
val_every = 25000 #Specify after how many steps it should make a validation step where it creates an audio for you to listen to.
workers = 4 #This depends on the amount of threads your CPU has. Kaggle mostly has 4 so you can leave it as is.
preprocessed_dataset = "/path/to/your/preprocessed_dataset" #This is the path where the preprocessed dataset will be saved to.


#READ ME
#This is a template to run rave commands in a python script. You need to comment out the commands you don't want to run. It is not the prettiest solution but it works.
#A comment is a line that starts with a #. You can comment out a line by adding a # in front of it. Removing the # will make the line active again.
#You can also comment out a block of code by selecting multiple lines of code and navigating to "Edit" -> "Toggle Block Comment".

#Preprocess You can do this just once and comment it out afterwards.
subprocess.run('rave', 'preprocess', '--input_path', dataset, '--output_path', preprocessed_dataset, '--channels', channels) 



#Start Training
#Run rave train --helpfull for more info about possible flags.
if regularization == "default":
  subprocess.run('rave', 'train', '--config', architecture, '--db_path', preprocessed_dataset, '--name', name, '--val_every', val_every, '--channels', channels, '--workers', workers) 
else:
  subprocess.run('rave', 'train', '--config', architecture, '--config', regularization,  '--db_path', preprocessed_dataset, '--name', name, '--val_every', val_every, '--channels', channels, '--workers', workers) 



#Resume Training
ckpt = '/path/to/your/latest/checkpoint'

if regularization == "default":
  subprocess.run('rave', 'train', '--config', architecture, '--db_path', preprocessed_dataset, '--name', name, '--ckpt', ckpt, '--val_every', val_every, '--channels', channels, '--workers', workers) 

else:
  subprocess.run('rave', 'train', '--config', architecture, '--regulariation', regularization, '--db_path', preprocessed_dataset, '--name', name, '--ckpt', ckpt, '--val_every', val_every, '--channels', channels, '--workers', workers) 
  
  
  
#Export Model
#Run rave export --helpfull for more info about possible flags.
model_dir = '/path/to/your/latest/checkpoint'
subprocess.run('rave', 'export', '--run', model_dir)



#Export Model
#Run rave export --helpfull for more info about possible flags.
model_dir = '/path/to/your/latest/checkpoint'
subprocess.run('rave', 'export', '--run', model_dir)
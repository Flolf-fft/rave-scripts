

# **READ ME**

This is just a markdown document that helps you to hold and edit your rave commands in one place. The shown commands are just examples and are not working yet. You need to adjust them with your correct paths and can edit them according to your needs. It is an addition the my RAVE Guide. If you are not already familiar with using a conda environment with the required packages I recommend reading the guide first. 

Don't forget to check if your conda environment is activated before running rave commands. 

### Preprocess

You can use the folders 01_unprocessed and 02_processed for this command. Just put your audio files into 01 and input the full paths into the command down below. 

`
rave preprocess --input_path path/to/your/audio/files --output_path path/to/02-dataset-processed --channels 1
`

### Start Training
*Run rave train --helpfull for more info about possible flags.*

`
rave train --config v2 --config wasserstein  --db_path full/path/to/02-dataset-processed --name LosingMySanity --val_every 25000 --channels 1 --workers 8
`


### Resume Training
*Run rave export --helpfull for more info about possible flags.*

The only difference to the training commmand is the addition of the --ckpt flag so RAVE resumes the training at the specified checkpoint file (.ckpt file in your runs/modelName/checkpoints/)

`
rave train --config v2 --config wasserstein --db_path path/to/02-dataset-processed --name LosingMySanity --ckpt /path/to/your/latest/checkpoint -val_every 25000 -channels 8 --workers 8
`  
  
  
### Export Model
*Run rave export --helpfull for more info about possible flags.* 

Export the model using your latest .ckpt file. 

`
rave export --run /path/to/your/latest/checkpoint
`

### Run Tensorboard

`
tensorboard --log_dir /path/to/your/runs/folder
`

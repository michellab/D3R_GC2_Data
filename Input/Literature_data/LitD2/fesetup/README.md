## README

### Getting FESetup
In order for the setup to work the setup software FESetup needs to be used. It can be found [here](http://www.hecbiosim.ac.uk/fesetup). FESetup 1.3dev release was used here.  

### Running FESetup
An example of setting up a simulation for ligand 100 can be run in the following way:   
```setup-1A.in```   

Alternatively the bashscript can be used, but may need to be modified to suit your own cluster infrastructure. Here the submission would be:
```sbatch fesetup-1A.sh```

### Running morph
After all molecules are setup, the morphing between strcutres needs to be done and is achieved like this:   
```FESetup moprh.in```

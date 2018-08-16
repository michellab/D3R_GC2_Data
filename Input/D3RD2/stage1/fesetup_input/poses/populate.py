import os,sys

parentdir = "../D3R_setD2_def_poses"

files = os.listdir(parentdir)

for f in files:
    if f.endswith(".pdb"):
        root = f.strip(".pdb")
        cmd = "mkdir -p %s" %  root 
        print cmd
        os.system(cmd) 
        cmd = "cp %s/%s %s/ligand.pdb" % (parentdir,f,root)
        print cmd
        os.system(cmd)

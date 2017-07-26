import argparse
from subprocess import call
from os import listdir
import os

def scale_morph(scale,inputfile, outputfile):
    inpert = open(inputfile)
    buffer = inpert.readlines()
    inpert.close()
    qi = 0.0
    qf = 0.0

    outpert = open(outputfile, 'w')
    print (len(buffer))
    l = 0
    while l < len(buffer)-1:
        line = buffer[l]
        if buffer[l+2].find("name DU") > -1:
            l+=9
            line = buffer[l]
            print line
            if l+1>=len(buffer):
                line = "endmolecule"
                outpert.write(line)
                break
        #print(line.rstrip())
        if line.find("bond")>-1:
            print "line is endmolecule"
            line = "endmolecule"
        l+=1
        if line.find("initial_type") > -1:
            elems = line.split()
            itype = elems[1]
        if line.find("final_type") > -1:
            line2="                final_type      %s\n" % itype
            outpert.write(line2)
            continue
        if line.find("initial_LJ") > -1:
            elems= line.split()
            isig = float(elems[1])
            ieps = float(elems[2])
        if line.find("final_LJ") > -1:
            line2="                final_LJ        %6.5f  %6.5f \n" % (isig,ieps)
            outpert.write(line2)
            continue
        if line.find("initial_charge") > -1:
            elems = line.split()
            qi = float( elems[1] )
        if line.find("final_charge") > -1:
            qf = qi * scale
            line2="                final_charge   %-6.5f\n" % qf
            outpert.write(line2)
            continue
        outpert.write(line)
        if line == "endmolecule":
            print "line is endmoelecule"
            break
    outpert.close()


parser = argparse.ArgumentParser(description='Thi script will set up a series of charge scaling simulaitons.')
parser.add_argument('--scale_factor', type=float,
                    help='factor by which the charges should be scaled')
parser.add_argument('--compound', help='Name of the compound for scaling')
parser.add_argument('--setup_base_dir', help='base directory of the FESetup simulations')
parser.add_argument('--output_dir', help='path to where things should be set up')
args = parser.parse_args()


print ("Setting up simulations in "+ args.output_dir)
print (" for compound "+args.compound)
print (" using scale factor "+str(args.scale_factor))

if not os.path.exists(args.output_dir):
    os.makedirs(args.output_dir)
makedirectory = "cp -a template "+args.output_dir+'/'+args.compound
print (makedirectory)
call(makedirectory, shell=True)

#Working on free simulation first
input_dir_free = args.output_dir+'/'+args.compound+'/free/input'
path_to_morph = args.setup_base_dir +"/_perturbations/sire/"
morph_dirs = listdir(path_to_morph)
get_morph = ''
for m in morph_dirs:
    if m.startswith(args.compound):
        get_morph = m
        break
cp_morph = "cp "+os.path.join(path_to_morph+m,'MORPH.onestep.pert')+ " "+input_dir_free
print (cp_morph)
call(cp_morph, shell=True)
#call('bunzip2 '+input_dir_free+'/MORPH.onestep.pert', shell=True)
morph_file = input_dir_free+"/MORPH.onestep.pert"
scaled_morph_file = input_dir_free+"/MORPH."+str(args.scale_factor)+".pert"
#Now we have scaled the morph file and removed all bits we don't need, such as dummy atoms etc
scale_morph(args.scale_factor, morph_file, scaled_morph_file)
call("ln -s "+"MORPH."+str(args.scale_factor)+".pert"+" "+input_dir_free+"/MORPH.pert", shell=True)
path_to_crds = args.setup_base_dir +"/_ligands/"+args.compound+"/"
cp_cords= "cp "+path_to_crds+"md00006.rst* "+input_dir_free
cp_top = "cp "+path_to_crds+"solvated.parm7* "+input_dir_free
call(cp_cords, shell=True)
call(cp_top, shell=True)
#unzip = 'bunzip2 '+input_dir_free+'/md00006.rst7.bz2'
#print (unzip)
#call(unzip, shell=True)
#unzip = 'bunzip2 '+input_dir_free+'/solvated.parm7.bz2'
#print (unzip)
#call(unzip, shell=True)
print ("Done prepping the solvated system")

print ("Starting work on the bound system")
#Working on bound simulations
input_dir_bound = args.output_dir+'/'+args.compound+'/bound/input'
path_to_crds = args.setup_base_dir +"/_complexes/*"+args.compound+"/"
cp_cords= "cp "+path_to_crds+"md00006.rst* "+input_dir_bound
cp_top = "cp "+path_to_crds+"solvated.parm7* "+input_dir_bound
call(cp_cords, shell=True)
call(cp_top, shell=True)
#unzip = 'bunzip2 '+input_dir_bound+'/md00006.rst7.bz2'
#call(unzip, shell=True)
#unzip = 'bunzip2 '+input_dir_bound+'/solvated.parm7.bz2'
#call(unzip, shell=True)
call("cp "+input_dir_free+"/MORPH.pert "+input_dir_bound, shell=True)


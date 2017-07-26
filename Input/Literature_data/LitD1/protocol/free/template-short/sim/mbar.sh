#!/bin/bash
#SBATCH -o analyse-free-nrg-%A.%a.out
#SBATCH -p GTX
#SBATCH -n 1
#SBATCH --time 00:05:00

srun ~/sire.app/bin/analyse_freenrg_mbar -i lambda-0.000/simfile.dat lambda-0.125/simfile.dat lambda-0.250/simfile.dat lambda-0.375/simfile.dat lambda-0.500/simfile.dat lambda-0.625/simfile.dat lambda-0.750/simfile.dat lambda-0.875/simfile.dat lambda-1.000/simfile.dat --lam 0.000 0.125 0.250 0.375 0.500 0.625 0.750 0.875 1.000 --temperature 298.0 -o mbar.pmf --subsampling percentage --percentage 95 > freenrg-MBAR.dat

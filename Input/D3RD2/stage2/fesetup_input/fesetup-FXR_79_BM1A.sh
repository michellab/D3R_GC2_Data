#!/bin/bash
#SBATCH -o FESetup-FXR_79_BM1A.out
#SBATCH -p main
#SBATCH --time 48:00:00
#SBATCH -n 1
#SBATCH -N 1
#source /etc/profile.d/module.sh
#module load FESetup

FESetup setup-FXR_79_BM1A.in
wait

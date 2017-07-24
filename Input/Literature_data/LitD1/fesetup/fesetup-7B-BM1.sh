#!/bin/bash
#SBATCH -o FESetup-7B-BM1.out
#SBATCH -p main
#SBATCH --time 48:00:00
#SBATCH -n 1
#SBATCH -N 1
#source /etc/profile.d/module.sh
#module load FESetup

FESetup setup-7B-BM1.in
wait

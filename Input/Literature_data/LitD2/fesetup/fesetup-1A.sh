#!/bin/bash
#SBATCH -o FESetup-1A.out
#SBATCH -p main
#SBATCH --time 48:00:00

FESetup setup-1A.in
wait

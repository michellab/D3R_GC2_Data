#!/bin/bash
#SBATCH -o somd-array-serial-%A.%a.out
#SBATCH -p main
#SBATCH -n 1
#SBATCH --time 04:00:00
#SBATCH --array=0-8

lamvals=( 0.000 0.125 0.250 0.375 0.500 0.625 0.750 0.875 1.000 )
lam=${lamvals[SLURM_ARRAY_TASK_ID]}

echo "lambda is: " $lam

mkdir lambda-$lam
cd lambda-$lam

export OPENMM_PLUGIN_DIR=/home/julien/sire.app/lib/plugins/
export OPENMM_CPU_THREADS=1

srun somd-freenrg -C ../../input/sim.cfg -l $lam -p CPU
cd ..

wait

if [ "$SLURM_ARRAY_TASK_ID" -eq "8" ]
then
    sleep 60
    sbatch ../mbar.sh
fi


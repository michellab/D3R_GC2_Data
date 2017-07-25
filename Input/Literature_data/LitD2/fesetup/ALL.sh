poses=( 1A  1B  1C  1D  1F_SR_BM1  1F_SR_BM2  1F_SS_BM1  1F_SS_BM2  1G  1H  1I  1K  1L  1M  1N  1P  1Q  1R  1S  7  8  INT01  INT02 )

for pose in "${poses[@]}"
do
    echo $pert
    python setmeup.py $pose
    #exit
done

poses=( 7A-BM1  7B-BM1  7C-BM1  7C-BM2  7D-BM1  7D-BM2  7E-BM1  7E-BM2  7F-BM1  7F-BM2  7G-BM1  7G-BM2  7H-BM1  7H-BM2 )

for pose in "${poses[@]}"
do
    echo $pert
    python setmeup.py $pose
    #exit
done

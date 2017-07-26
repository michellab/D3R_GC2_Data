perts=( 1A~1B  1A~1P  1A~INT01  1B~1D  1D~1B            1F_SS_BM2~INT01  1I~INT01  1N~INT02  1Q~1A  1S~1P  8~1A             INT01~1F_SS_BM1  INT02~1A
1A~1C  1A~1Q  1A~INT02  1C~1A  1F_SR_BM1~INT01  1G~1H            1K~INT02  1P~1A     1Q~1P  1S~7   INT01~1A         INT01~1F_SS_BM2  INT02~1K
1A~1D  1A~7   1B~1A     1C~1B  1F_SR_BM2~INT01  1G~INT01         1L~1A     1P~1Q     1Q~1R  7~1A   INT01~1F_SR_BM1  INT01~1G         INT02~1M
1A~1L  1A~8   1B~1C     1D~1A  1F_SS_BM1~INT01  1H~1G            1M~INT02  1P~1S     1R~1Q  7~1S   INT01~1F_SR_BM2  INT01~1I         INT02~1N )

for pert in "${perts[@]}"
do
    echo $pert
    python setup.py ../protocol ../fesetup/_perturbations/sire $pert
    #exit
done

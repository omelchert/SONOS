# FILE: getData_Fig1bc.sh
# AUTHOR: O. Melchert
# DATE:   19.05.2016

function singleRun {
  ZD=$1
  AB=$2
  R=$3
  echo $ZD $AB $R 
  python main_EX_Fig1bc.py $ZD $AB $R > ./EX_Fig1bc/cyl_zD${ZD}_a${AB}_R${R}.dat
}

singleRun 0.50 0.1 4.0
singleRun 0.50 0.1 2.0
singleRun 0.50 0.1 8.0

singleRun 0.50 0.1 4.0
singleRun 0.50 0.05 4.0
singleRun 0.50 0.15 4.0

# EOF: getData_EX1.sh

# FILE: getData_EX3.sh
# AUTHOR: O. Melchert
# DATE:   21.03.2016

function singleSet {
  ZD=$1
  for XD in 0.00 0.10 0.20;
  do
    echo "ZD=" $ZD "XD=" $XD
    python main_EX_Fig3.py ${ZD} ${XD} > ./EX_Fig3/cyl_2Layer_low_high_zD${ZD}_xD${XD}.dat
  done
}

# NEAR FIELD SETUP
singleSet 0.2

# FAR FIELD SETUP
singleSet 5.0
singleSet 1.0

# EOF: getData_EX3.sh

# FILE: getData_EX6.sh
# AUTHOR: O. Melchert
# DATE:   06.04.2016

for ZD in `seq 0.1 0.1 5.0`;
do
  echo "ZD=" $ZD 
  python main_EX_Fig6.py ${ZD} > ./EX_Fig6/cyl_PIII_zD${ZD}.dat
done



# EOF: getData_EX6.sh

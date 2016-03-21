# FILE: getData_EX2.sh
# AUTHOR: O. Melchert
# DATE:   21.03.2016

python main_EX_Fig2a.py 0.04 > ./EX_Fig2/cyl_2Layer_low_high_zD0.04.dat
python main_EX_Fig2a.py 4.00 > ./EX_Fig2/cyl_2Layer_low_high_zD4.0.dat

python main_EX_Fig2b.py 0.04 > ./EX_Fig2/cyl_2Layer_high_low_zD0.04.dat
python main_EX_Fig2b.py 4.00 > ./EX_Fig2/cyl_2Layer_high_low_zD4.0.dat

# EOF: getData_EX2.sh

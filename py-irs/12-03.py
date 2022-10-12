import hgsysinc
from hgworddistance import GetWordDistance_Jacard, GetWordDistance_Tanimoto
print ('Distance_Jacard: %.2f' % GetWordDistance_Jacard('govenment', 'government')) # Distance_Jacard: 0.667
print ('Distance_Jacard: %.2f' % GetWordDistance_Jacard('difterential', 'differential')) # Distance: 0.00
print ('Distance_Tanimoto: %.2f' % GetWordDistance_Tanimoto('govenment', 'government')) # Distance_Tanimoto: 0.667
print ('Distance_Tanimoto: %.2f' % GetWordDistance_Tanimoto('difterential', 'differential')) # Distance: 0.00


"""
처리 결과
#===================
Distance_Jacard: 0.12
Distance_Jacard: 0.00
Distance_Tanimoto: 0.07
Distance_Tanimoto: 0.11


"""

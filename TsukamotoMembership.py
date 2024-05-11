import skfuzzy as skf
import numpy as np
import matplotlib.pyplot as plt
from membershipGroup import membershipGroup

#[Membership Berat]#
#===============[Laki - Laki Type 1]===============#
domainBeratT1 = np.arange(0.0,8.9,0.1)
MembershipBeratT1 = membershipGroup()

MembershipBeratT1.add_member('Kurang',domainBeratT1 ,[0.,0.,2.7,3.3])
MembershipBeratT1.add_member('Ideal',domainBeratT1 ,[2.7,3.3,3.3,7.9])
MembershipBeratT1.add_member('Lebih',domainBeratT1 ,[3.3,7.9,8.9,8.9])

#===============[Laki - Laki Type 2]===============#
domainBeratT2 = np.arange(5.7,10.6,0.1)
MembershipBeratT2 = membershipGroup()

MembershipBeratT2.add_member('Kurang',domainBeratT2 ,[5.7,5.7,6.7,8.3])
MembershipBeratT2.add_member('Ideal',domainBeratT2 ,[6.7,8.3,8.3,9.6])
MembershipBeratT2.add_member('Lebih',domainBeratT2 ,[8.3,9.6,10.6,10.6])

#===============[Laki - Laki Type 3]===============#
domainBeratT3 = np.arange(7.6,14.6,0.1)
MembershipBeratT3 = membershipGroup()

MembershipBeratT3.add_member('Kurang',domainBeratT3 ,[7.6,7.6,8.6,9.7])
MembershipBeratT3.add_member('Ideal',domainBeratT3 ,[8.6,9.7,9.7,13.6])
MembershipBeratT3.add_member('Lebih',domainBeratT3 ,[9.7,13.6,14.6,14.6])

#===============[Laki - Laki Type 4]===============#
domainBeratT4 = np.arange(7.8,22.0,0.1)
MembershipBeratT4 = membershipGroup()

MembershipBeratT4.add_member('Kurang',domainBeratT4 ,[7.8,7.8,8.8,15.5])
MembershipBeratT4.add_member('Ideal',domainBeratT4 ,[8.8,15.5,15.5,21.0])
MembershipBeratT4.add_member('Lebih',domainBeratT4 ,[15.5,21.0,22.0,22.0])

#[Membership Panjang]#
#===============[Laki - Laki Type 1]===============#
domainPanjangT1 = np.arange(0.0,8.9,0.1)
MembershipPanjangT1 = membershipGroup()

MembershipPanjangT1.add_member('Pendek',domainPanjangT1 ,[0.,0.,2.7,3.3])
MembershipPanjangT1.add_member('Sedang',domainPanjangT1 ,[2.7,3.3,3.3,7.9])
MembershipPanjangT1.add_member('Tinggi',domainPanjangT1 ,[3.3,7.9,8.9,8.9])
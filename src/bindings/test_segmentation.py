import mchmapping
import pytest
import math

# the idea in this test is not the reproduce all the tests
# of the mapping library, as we assume the C++ library _is_ correct (because
# it has been tested). But we use a few of the C++ tests to examplify
# the interface.

def test_GetSegmentationThrowsIfDetElemIdIsNotValid():
    with pytest.raises(RuntimeError):
        mchmapping.Segmentation(-1)
    with pytest.raises(RuntimeError):
        mchmapping.Segmentation(121)

def test_CheckNofPads():
    assert mchmapping.Segmentation(100).nofPads()==28672

def test_CheckOnePadPositionPresentOnOnlyBendingPlaneDE825():
    de825 = mchmapping.Segmentation(825)
    x = 110.09;
    y = -1.25;
    (ok,b,nb) = de825.findPadPairByPosition(x, y)
    testChannel = 23
    assert ok==False
    p = de825.findPadByFEE(1333, testChannel);
    assert p==nb
    assert de825.isValid(b)==False
    assert de825.isValid(nb)==True


manu2ds_st12 = [
      36, 35, 34, 33, 32, 37, 38, 43, 45, 47, 49, 50, 53, 41, 39, 40,
        63, 62, 61, 60, 59, 58, 56, 57, 54, 55, 52, 51, 48, 46, 44, 42,
          31, 30, 29, 28, 27, 26, 25, 24, 22, 23, 20, 18, 17, 15, 13, 11,
            4, 3, 2, 1, 0, 5, 6, 10, 12, 14, 16, 19, 21, 8, 7, 9]


def permutation(seg,nei,expected):
    eps=1E-5
    notfound=len(expected)
    for paduid in nei:
        for e in expected:
            ch=seg.padDualSampaChannel(paduid)
            expected_ch=manu2ds_st12[e["ch"]]
            if expected_ch == ch  \
                and e["fec"] == seg.padDualSampaId(paduid) \
                and math.isclose(e["dx"],seg.padSizeX(paduid),rel_tol=eps) \
                and math.isclose(e["dy"],seg.padSizeY(paduid),rel_tol=eps) \
                and math.isclose(e["x"],seg.padPositionX(paduid),rel_tol=eps) \
                and math.isclose(e["y"],seg.padPositionY(paduid),rel_tol=eps):
                notfound -= 1
    return notfound==0

# Below are the neighbouring pads of the pad(s) @ (24.0, 24.0)cm
#  for DE 100.
#  What is tested below is not the PAD (index might depend on
#  the underlying implementation) but the rest of the information :
#  (FEC,CH), (X,Y), (SX,SY)
# 
#  PAD       5208 FEC   95 CH  0 X  23.625 Y  23.730 SX   0.630 SY   0.420
#  PAD       5209 FEC   95 CH  3 X  23.625 Y  24.150 SX   0.630 SY   0.420
#  PAD       5210 FEC   95 CH  4 X  23.625 Y  24.570 SX   0.630 SY   0.420
#  PAD       5226 FEC   95 CH 42 X  24.255 Y  24.570 SX   0.630 SY   0.420
#  PAD       5242 FEC   95 CH 43 X  24.885 Y  24.570 SX   0.630 SY   0.420
#  PAD       5241 FEC   95 CH  2 X  24.885 Y  24.150 SX   0.630 SY   0.420
#  PAD       5240 FEC   95 CH 46 X  24.885 Y  23.730 SX   0.630 SY   0.420
#  PAD       5224 FEC   95 CH 31 X  24.255 Y  23.730 SX   0.630 SY   0.420
#  PAD      19567 FEC 1119 CH 48 X  23.310 Y  23.520 SX   0.630 SY   0.420
#  PAD      19568 FEC 1119 CH 46 X  23.310 Y  23.940 SX   0.630 SY   0.420
#  PAD      19569 FEC 1119 CH  0 X  23.310 Y  24.360 SX   0.630 SY   0.420
#  PAD      19585 FEC 1119 CH 42 X  23.940 Y  24.360 SX   0.630 SY   0.420
#  PAD      19601 FEC 1119 CH  1 X  24.570 Y  24.360 SX   0.630 SY   0.420
#  PAD      19600 FEC 1119 CH 44 X  24.570 Y  23.940 SX   0.630 SY   0.420
#  PAD      19599 FEC 1119 CH 30 X  24.570 Y  23.520 SX   0.630 SY   0.420
#  PAD      19583 FEC 1119 CH 29 X  23.940 Y  23.520 SX   0.630 SY   0.420
#
def test_CheckOnePadNeighbours():
    bendingNeighbours = [
    {"fec":95, "ch":0,  "x":23.625, "y":23.730, "dx":0.630, "dy":0.420},
    {"fec":95, "ch":3,  "x":23.625, "y":24.150, "dx":0.630, "dy":0.420},
    {"fec":95, "ch":4,  "x":23.625, "y":24.570, "dx":0.630, "dy":0.420},
    {"fec":95, "ch":42, "x":24.255, "y":24.570, "dx":0.630, "dy":0.420},
    {"fec":95, "ch":43, "x":24.885, "y":24.570, "dx":0.630, "dy":0.420},
    {"fec":95, "ch":2,  "x":24.885, "y":24.150, "dx":0.630, "dy":0.420},
    {"fec":95, "ch":46, "x":24.885, "y":23.730, "dx":0.630, "dy":0.420},
    {"fec":95, "ch":31, "x":24.255, "y":23.730, "dx":0.630, "dy":0.420} ]

    nonBendingNeighbours = [
     {"fec":1119, "ch":48, "x":23.310, "y":23.520, "dx":0.630, "dy":0.420},
     {"fec":1119, "ch":46, "x":23.310, "y":23.940, "dx":0.630, "dy":0.420},
     {"fec":1119, "ch":0,  "x":23.310, "y":24.360, "dx":0.630, "dy":0.420},
     {"fec":1119, "ch":42, "x":23.940, "y":24.360, "dx":0.630, "dy":0.420},
     {"fec":1119, "ch":1,  "x":24.570, "y":24.360, "dx":0.630, "dy":0.420},
     {"fec":1119, "ch":44, "x":24.570, "y":23.940, "dx":0.630, "dy":0.420},
     {"fec":1119, "ch":30, "x":24.570, "y":23.520, "dx":0.630, "dy":0.420},
     {"fec":1119, "ch":29, "x":23.940, "y":23.520, "dx":0.630, "dy":0.420} ]

    de100 = mchmapping.Segmentation(100)
    (_,b,nb) = de100.findPadPairByPosition(24,24)
    b_nei = de100.neighbours(b)
    assert len(b_nei)==len(bendingNeighbours)
    nb_nei = de100.neighbours(nb)
    assert len(nb_nei)==len(nonBendingNeighbours)

    assert permutation(de100,b_nei,bendingNeighbours)==True
    assert permutation(de100,nb_nei,nonBendingNeighbours)==True


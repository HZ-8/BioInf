import AminoAcidMasses as aam, Trim

massdict = aam.AminoAcidMasses()

lboard = ['WICDLDPACLRAVSAKGPCDRYVMSDEQLFNDGGAHAKKKVERAT', 'NCNTNAWPTDYMVPMGLPTEYHTCPRHHSQLMYGTTHNPGHENND', 'AAEKLPTTWRKDGDMHEQVDSRWEINKMWEKNPFKEFQLMTPFFD', 'SLAYFFKPRCESPEFCVTSNLQWFAPRCFFKVPGVDQYAIANWDT', 'YEVLSPVDLMNLNKTQIIKQNSHFKNTDIKLWSNAYSYEHQMWMF', 'ALYGLRGPNMHGGQMGISKTEKWAPQLTDRVGESGETESFQTEGW', 'GGTFHMPFFIMECQPIPRLAADCQHQRLITHEGDFQWFSILEWYK', 'TAFNGFRTMGHIEHQAYWYPNGFLQITTFWVSRPTDKHLEPRSGV', 'LVPEKVVSLKEACCYPGVMFWADRRRDGEFMGAIYWVIILIDEHY', 'EPCDECKDHSAMVGFWCQSKASKNSERFYKIDEIARDGWAYSDQA', 'QNKTGQTYEHTRVESAIWDRSRSECMCKLGEDTSAATQMRSGFRD', 'INWVNFVAMYRDKREKYVWHAASILVPRHGHEKEVVIIVGRCCTA', 'DVVSDMVPDRKPECVNNTLSVKSHMEGTAHLNPYPKYHQCNSFRG', 'AEASAQPNRDGTMKDWEWMVATYWWAQKVNRCHQHWVNHIGSQKG', 'IMEHQLGGGCQMQGTEGKEKGNKHWGRWKHSEGHKRAEKAHCQSS']
spect = [0, 57, 57, 57, 71, 71, 87, 97, 97, 97, 97, 99, 99, 101, 101, 103, 103, 103, 103, 103, 113, 113, 113, 114, 114, 114, 115, 115, 128, 128, 128, 128, 129, 129, 131, 131, 131, 131, 131, 137, 147, 147, 156, 160, 163, 170, 170, 171, 174, 185, 186, 186, 194, 198, 200, 202, 210, 211, 213, 215, 216, 216, 218, 226, 228, 228, 229, 229, 230, 230, 231, 231, 234, 240, 242, 243, 243, 243, 245, 246, 260, 266, 268, 276, 278, 278, 283, 284, 289, 297, 297, 298, 299, 299, 299, 302, 303, 303, 315, 317, 319, 329, 330, 330, 333, 334, 340, 341, 341, 344, 344, 344, 345, 346, 349, 357, 357, 360, 361, 363, 371, 371, 374, 375, 375, 379, 379, 386, 390, 396, 396, 397, 398, 400, 405, 412, 412, 418, 427, 428, 430, 431, 431, 434, 436, 445, 446, 447, 447, 448, 458, 459, 460, 461, 461, 469, 471, 473, 475, 475, 476, 476, 482, 483, 486, 488, 488, 489, 489, 492, 493, 500, 511, 518, 518, 521, 527, 528, 531, 531, 534, 542, 545, 546, 547, 549, 550, 557, 558, 559, 559, 560, 562, 564, 574, 575, 577, 582, 586, 587, 589, 590, 590, 592, 595, 597, 604, 610, 612, 616, 617, 617, 618, 621, 624, 631, 633, 644, 646, 647, 648, 649, 649, 652, 654, 656, 659, 660, 673, 674, 674, 677, 678, 683, 688, 690, 690, 691, 705, 705, 711, 713, 715, 716, 717, 718, 718, 720, 720, 723, 729, 731, 745, 746, 747, 747, 750, 757, 760, 764, 764, 768, 768, 771, 776, 777, 777, 780, 780, 784, 786, 786, 787, 787, 787, 789, 791, 805, 819, 820, 823, 825, 826, 830, 833, 833, 833, 844, 846, 846, 847, 848, 859, 860, 861, 861, 863, 871, 875, 880, 883, 886, 888, 889, 890, 891, 892, 894, 895, 897, 908, 913, 914, 917, 917, 918, 920, 920, 927, 928, 934, 934, 936, 936, 943, 945, 954, 957, 961, 961, 961, 974, 975, 989, 989, 990, 992, 993, 993, 994, 994, 995, 1005, 1011, 1014, 1017, 1017, 1017, 1017, 1020, 1022, 1023, 1026, 1035, 1039, 1045, 1046, 1046, 1048, 1057, 1058, 1062, 1064, 1065, 1072, 1076, 1082, 1083, 1091, 1096, 1099, 1104, 1104, 1105, 1108, 1108, 1114, 1117, 1120, 1120, 1121, 1125, 1125, 1126, 1130, 1132, 1136, 1142, 1143, 1148, 1148, 1149, 1149, 1159, 1160, 1163, 1164, 1174, 1186, 1192, 1196, 1202, 1204, 1204, 1211, 1211, 1212, 1218, 1221, 1222, 1223, 1223, 1224, 1232, 1233, 1233, 1235, 1235, 1239, 1239, 1243, 1246, 1250, 1251, 1257, 1257, 1259, 1260, 1263, 1269, 1277, 1287, 1289, 1291, 1295, 1295, 1295, 1305, 1314, 1315, 1322, 1324, 1325, 1334, 1335, 1336, 1336, 1336, 1339, 1342, 1346, 1347, 1349, 1351, 1354, 1360, 1364, 1366, 1366, 1372, 1372, 1374, 1380, 1388, 1390, 1391, 1396, 1397, 1402, 1403, 1406, 1410, 1417, 1424, 1425, 1429, 1437, 1439, 1442, 1448, 1449, 1450, 1451, 1452, 1465, 1467, 1470, 1477, 1477, 1478, 1481, 1482, 1487, 1488, 1493, 1495, 1499, 1500, 1503, 1509, 1511, 1513, 1516, 1521, 1534, 1538, 1538, 1540, 1545, 1553, 1553, 1557, 1564, 1565, 1566, 1567, 1573, 1576, 1579, 1579, 1580, 1583, 1590, 1591, 1596, 1609, 1610, 1612, 1614, 1618, 1625, 1630, 1633, 1634, 1635, 1641, 1642, 1644, 1647, 1648, 1650, 1666, 1668, 1668, 1669, 1670, 1671, 1679, 1680, 1681, 1684, 1692, 1693, 1694, 1694, 1696, 1704, 1707, 1708, 1713, 1732, 1741, 1743, 1746, 1750, 1759, 1761, 1764, 1769, 1769, 1770, 1771, 1773, 1781, 1781, 1781, 1781, 1781, 1782, 1784, 1793, 1795, 1797, 1800, 1807, 1808, 1810, 1822, 1822, 1828, 1841, 1842, 1847, 1852, 1856, 1864, 1870, 1872, 1872, 1877, 1878, 1878, 1879, 1884, 1894, 1895, 1897, 1907, 1909, 1909, 1911, 1912, 1913, 1928, 1928, 1929, 1931, 1943, 1950, 1951, 1959, 1969, 1970, 1971, 1975, 1978, 1979, 1988, 1991, 1992, 1998, 1999, 2000, 2007, 2009, 2010, 2012, 2012, 2026, 2026, 2027, 2037, 2040, 2042, 2056, 2057, 2059, 2062, 2065, 2071, 2072, 2076, 2080, 2081, 2083, 2094, 2098, 2115, 2119, 2120, 2122, 2125, 2125, 2126, 2129, 2130, 2140, 2140, 2141, 2143, 2154, 2155, 2156, 2157, 2159, 2171, 2177, 2177, 2186, 2193, 2197, 2200, 2207, 2212, 2212, 2216, 2227, 2228, 2228, 2229, 2229, 2250, 2256, 2256, 2257, 2258, 2258, 2260, 2268, 2268, 2269, 2270, 2274, 2283, 2300, 2308, 2315, 2317, 2325, 2326, 2340, 2340, 2341, 2343, 2353, 2356, 2359, 2359, 2359, 2360, 2361, 2363, 2367, 2370, 2371, 2382, 2386, 2386, 2397, 2405, 2418, 2429, 2431, 2438, 2439, 2439, 2440, 2454, 2455, 2456, 2459, 2471, 2473, 2474, 2481, 2487, 2488, 2489, 2490, 2499, 2501, 2510, 2526, 2526, 2528, 2530, 2538, 2546, 2552, 2552, 2553, 2555, 2557, 2560, 2568, 2585, 2586, 2587, 2590, 2602, 2602, 2604, 2609, 2615, 2619, 2623, 2625, 2625, 2629, 2641, 2658, 2659, 2661, 2661, 2673, 2681, 2683, 2688, 2689, 2699, 2705, 2716, 2716, 2718, 2722, 2730, 2738, 2738, 2739, 2742, 2746, 2756, 2775, 2776, 2776, 2786, 2789, 2790, 2798, 2804, 2813, 2817, 2817, 2830, 2833, 2836, 2845, 2845, 2849, 2851, 2867, 2887, 2889, 2901, 2901, 2904, 2905, 2906, 2907, 2912, 2914, 2917, 2918, 2920, 2924, 2927, 2948, 2964, 2973, 2976, 2984, 2991, 2992, 3004, 3005, 3014, 3015, 3015, 3020, 3021, 3028, 3032, 3033, 3037, 3043, 3046, 3076, 3079, 3085, 3091, 3117, 3117, 3120, 3120, 3123, 3129, 3134, 3136, 3142, 3143, 3146, 3146, 3147, 3161, 3186, 3194, 3200, 3219, 3220, 3223, 3230, 3245, 3251, 3251, 3257, 3258, 3273, 3275, 3276, 3277, 3294, 3297, 3303, 3306, 3314, 3322, 3333, 3348, 3354, 3372, 3372, 3376, 3376, 3379, 3388, 3400, 3406, 3409, 3416, 3423, 3425, 3429, 3451, 3461, 3462, 3466, 3486, 3491, 3503, 3505, 3507, 3513, 3516, 3519, 3522, 3543, 3554, 3564, 3565, 3602, 3603, 3609, 3616, 3617, 3619, 3622, 3622, 3635, 3636, 3647, 3651, 3674, 3706, 3712, 3716, 3733, 3740, 3744, 3750, 3750, 3751, 3759, 3764, 3769, 3773, 3821, 3837, 3837, 3843, 3847, 3847, 3848, 3862, 3879, 3900, 3904, 3906, 3918, 3940, 3950, 3950, 3962, 3966, 3976, 3993, 3997, 4009, 4019, 4037, 4047, 4053, 4063, 4090, 4110, 4122, 4134, 4136, 4140, 4140, 4147, 4177, 4219, 4233, 4234, 4237, 4239, 4247, 4269, 4271, 4296, 4333, 4336, 4350, 4366, 4368, 4390, 4393, 4400, 4433, 4480, 4481, 4497, 4497, 4530, 4536, 4537, 4594, 4610, 4611, 4633, 4667, 4668, 4707, 4708, 4764, 4765, 4796, 4821, 4878, 4893, 4893, 4990, 5007, 5064, 5104, 5161]
N = 5

board = Trim.Trim(lboard, spect, N, massdict)
print board
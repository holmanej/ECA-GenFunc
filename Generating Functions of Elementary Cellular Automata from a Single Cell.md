# Generating Functions of Elementary Cellular Automata from a Single Cell

### Introduction

A generating function provides a concise description of a sequence of numbers. Described below are the patterns and their resulting generating functions of the 256 rules of elementary cellular automata driven by a single cell. The sequences described are obtained by calculating the pattern in a 64 by 32 cell plane starting from a cell placed at column 32 in row 0 and interpreting living and dead cells in subsequent rows as 1s and 0s respectively to create a binary representation (unless noted otherwise).



## Rule 0

![rule 0](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%200.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: 8, 32, 40, 64, 72, 96, 104, 128, 136, 160, 168, 192, 200, 224, 232

#### Generating Function:	1



## Rule 1

![rule 1](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%201.bmp?raw=true)

#### Sequence: 1, 0, 1, 0, 1, 0, 1, 0, ...

#### Duplicates: 33

#### Generating Function: 1 / (1 - x^2^)



## Rule 2

![rule 2](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%202.bmp?raw=true)

#### Sequence: 1, 2, 4, 8, 16, 32, 64, 128, ...

#### Duplicates: 10, 34, 42, 66, 74, 98, 106, 130, 138, 162, 170, 194, 202, 226, 234

#### Generating Function:	-1 / (2x - 1)



## Rule 3

![rule 3](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%203.bmp?raw=true)

#### Sequence: 1/2, 0, 1/4, 0, 1/8, 0, 1/16, 0, ...

#### Duplicates: 35

#### Generating Function:	1 / (2 - x^2^)



## Rule 4

![rule 4](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%204.bmp?raw=true)

#### Sequence: 1, 1, 1, 1, 1, 1, 1, 1, ...

#### Duplicates: 12, 36, 44, 68, 76, 100, 108, 132, 140, 164, 172, 196, 204, 228, 236

#### Generating Function:	1 / (1 - x)



## Rule 5

![rule 5](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%205.bmp?raw=true)

#### Sequence: 1, 1, 1, 1, 1, 1, 1, 1, ...

#### Duplicates: none

#### Generating Function:	1 / (1 - x)



## Rule 6

![rule 6](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%206.bmp?raw=true)

#### Sequence: 1, 3, 4, 12, 16, 48, 64, 196, ...

#### Duplicates: 38, 134, 166

#### Generating Function:	(-3x - 1) / (2x - 1)



## Rule 7

![rule 7](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%207.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 9

![rule 9](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%209.bmp?raw=true)

#### Sequence: 7/4, 1, 7/16, 1/4, 7/64, 1/16, 7/256, 1/64, ...

(only the gliders starting at row 4)

#### Duplicates: none

#### Generating Function:	(7 + 2x) / (4 - x^2^)



## Rule 11

![rule 11](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2011.bmp?raw=true)

#### Sequence: 3/4, 0, 3/16, 0, 3/64, 0, 3/256, 0, ...

#### Duplicates: none

#### Generating Function:	3 / (4 - x^2^)



## Rule 13

![rule 13](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2013.bmp?raw=true)

#### Sequence: 1/4, 5/16, 21/64, 85/256, 341/1024, 1365/4096, 21845/65536, 87381/262144

#### Duplicates: none

#### Generating Function:	-1 / (4 - x)(x - 1)



## Rule 14

![rule 14](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2014.bmp?raw=true)

#### Sequence: 1, 3, 6, 12, 24, 48, 96, 192, ...

#### Duplicates: 46, 142, 174

#### Generating Function:	(-x - 1) / (2x - 1)



## Rule 15

![rule 15](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2015.bmp?raw=true)

#### Sequence: 1/4, 0, 1/16, 0, 1/64, 0, 1/256, 0, ...

#### Duplicates: none

#### Generating Function:	1 / (4 - x^2^)



## Rule 16

![rule 16](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2016.bmp?raw=true)

#### Sequence: 1, 1/2, 1/4, 1/8, 1/16, 1/32, 1/64, 1/128, ...

#### Duplicates: 24, 48, 56, 80, 88, 112, 120, 144, 152, 176, 184, 208, 216, 240, 248

#### Generating Function:	-1 / (x - 2)



## Rule 17

![rule 17](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2017.bmp?raw=true)

#### Sequence: 1, 0, 2, 0, 4, 0, 8, 0, ...

#### Duplicates: 49

#### Generating Function:	-1 / (2x^2^ - 1)



## Rule 18

![rule 18](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2018.bmp?raw=true)

#### Sequence: 1, 5, 17, 85, 257, 1285, 4369, 21845, ...

#### Duplicates: 26, 82, 90, 146, 154, 210, 218

#### Generating Function:	1



## Rule 19

![rule 19](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2019.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 20

![rule 20](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2020.bmp?raw=true)

#### Sequence: 1, 1/2, 3/4, 1/8, 3/16, 1/32, 3/64, 1/128, ...

#### Duplicates: 52, 148, 180

#### Generating Function:	(-3x - 2) / (x^2 - 4)



## Rule 21

![rule 21](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2021.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 22

![rule 22](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2022.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 23

![rule 23](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2023.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: 31, 55, 63, 87, 95, 119, 127

#### Generating Function:	1



## Rule 25

![rule 25](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2025.bmp?raw=true)

#### Sequence: 7, 4, 7/2, 2, 7/4, 1, 7/8, 1/2, ...

#### Duplicates: none

#### Generating Function:	(14 + 8*x) / (2 - x^2^)



## Rule 27

![rule 27](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2027.bmp?raw=true)

#### Sequence: 1/2, 0, 1/4, 0, 1/8, 0, 1/16, 0, ...

#### Duplicates: none

#### Generating Function:	1 / (2 - x^2^)



## Rule 28

![rule 28](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2028.bmp?raw=true)

#### Sequence: 1, 3, 5, 11, 21, 43, 85, 171, ...

#### Duplicates: 156

#### Generating Function:	(1 + 2x) / (1 + x)(1 - 2x)



## Rule 29

![rule 29](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2029.bmp?raw=true)

#### Sequence: 1, 1, 1, 1, 1, 1, 1, 1, ...

#### Duplicates: none

#### Generating Function:	1 / (1 - x)



## Rule 30

![rule 30](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2030.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 37

![rule 37](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2037.bmp?raw=true)

#### Sequence: 7/2, 0, 7/2, 0, 7/2, 0, 7/2, 0, ...

#### Duplicates: none

#### Generating Function:	7 / 2(1 - x)



## Rule 39

![rule 39](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2039.bmp?raw=true)

#### Sequence: 1/2, 0, 1/4, 0, 1/8, 0, 1/16, 0, ...

#### Duplicates: none

#### Generating Function:	1 / (2 - x^2^)



## Rule 41

![rule 41](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2041.bmp?raw=true)

#### Sequence: 1, 1/2, 0, 0, 1/16, 1/32, 0, 0, ...

#### Duplicates: none

#### Generating Function:	-8 / (x - 2)(x^2^ + 4)



## Rule 45

![rule 45](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2045.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 47

![rule 47](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2047.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 50

![rule 50](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2050.bmp?raw=true)

#### Sequence: 1, 5, 21, 85, 341, 1365, 5461, 21845, ...

#### Duplicates: 58, 114, 122, 178, 186, 242, 250

#### Generating Function:	1 / (1 - x)(1 - 4x)



## Rule 51

![rule 51](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2051.bmp?raw=true)

#### Sequence: 1, 0, 1, 0, 1, 0, 1, 0, ...

#### Duplicates: none

#### Generating Function:	1 / (1 - x^2^)



## Rule 53

![rule 53](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2053.bmp?raw=true)

#### Sequence: 1, 2, 4, 8, 16, 32, 64, 128, ...

#### Duplicates: none

#### Generating Function:	-1 / (2x - 1)



## Rule 54

![rule 54](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2054.bmp?raw=true)

#### Sequence: 1, 7, 17, 119, 273, 1911, 4369, 30583, ...

#### Duplicates: none

#### Generating Function:	(1 + 7x) / (1 - x^2^)(1 - 16x^2^)



## Rule 57

![rule 57](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2057.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 59

![rule 59](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2059.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 60

![rule 60](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2060.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 61

![rule 61](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2061.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 62

![rule 62](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2062.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 65

![rule 65](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2065.bmp?raw=true)

#### Sequence: 7, 1, 28, 4, 118, 16, 448, 64, ...

#### Duplicates: none

#### Generating Function:	(7 + x) / (4x^2^ - 2)



## Rule 67

![rule 67](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2067.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 69

![rule 69](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2069.bmp?raw=true)

#### Sequence: 1, 5, 21, 85, 341, 1365, 5461, 21845, 87381

#### Duplicates: none

#### Generating Function:	1 / (4x - 1)(x - 1)



## Rule 70

![rule 70](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2070.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: 198

#### Generating Function:	1



## Rule 71

![rule 71](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2071.bmp?raw=true)

#### Sequence: 1, 1, 1, 1, 1, 1, 1, 1, ...

#### Duplicates: none

#### Generating Function:	1 / (1 - x)



## Rule 73

![rule 73](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2073.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 75

![rule 75](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2075.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 77

![rule 77](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2077.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 78

![rule 78](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2078.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 79

![rule 79](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2079.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 81

![rule 81](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2081.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: 113

#### Generating Function:	1



## Rule 83

![rule 83](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2083.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 84

![rule 84](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2084.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: 116, 212, 244

#### Generating Function:	1



## Rule 85

![rule 85](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2085.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 86

![rule 86](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2086.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 89

![rule 89](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2089.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 91

![rule 91](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2091.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 92

![rule 92](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2092.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 93

![rule 93](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2093.bmp?raw=true)

#### Sequence: 1, 5, 21, 85, 341, 1365, 5461, 21845, 87381

#### Duplicates: none

#### Generating Function:	1 / (4x - 1)(x - 1)



## Rule 94

![rule 94](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2094.bmp?raw=true)

#### Sequence: 1, 7, 27, 119, 427, 1879, 6827, 30039, ...

#### Duplicates: none

#### Generating Function:	(1 + 2x)(1 + 5x - 16x^4^) / (1 - x^2^)(1 - 16x^4^)



## Rule 97

![rule 97](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2097.bmp?raw=true)

#### Sequence: 1, 2, 0, 0, 16, 32, 0, 0, ...

#### Duplicates: none

#### Generating Function:	-1 / (2x - 1)(4x^2^+1)



## Rule 99

![rule 99](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%2099.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 101

![rule 101](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20101.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 102

![rule 102](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20102.bmp?raw=true)

#### Sequence: 1, 3, 5, 15, 17, 51, 85, 255, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 103

![rule 103](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20103.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 105

![rule 105](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20105.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 107

![rule 107](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20107.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 109

![rule 109](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20109.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 110

![rule 110](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20110.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 111

![rule 111](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20111.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 115

![rule 115](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20115.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 117

![rule 117](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20117.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 118

![rule 118](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20118.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 121

![rule 121](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20121.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 123

![rule 123](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20123.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 124

![rule 124](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20124.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 125

![rule 125](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20125.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 126

![rule 126](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20126.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 129

![rule 129](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20129.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: 161

#### Generating Function:	1



## Rule 131

![rule 131](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20131.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 133

![rule 133](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20133.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 135

![rule 135](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20135.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 137

![rule 137](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20137.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 139

![rule 139](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20139.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: 171

#### Generating Function:	1



## Rule 141

![rule 141](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20141.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 143

![rule 143](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20143.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 145

![rule 145](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20145.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 147

![rule 147](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20147.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 149

![rule 149](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20149.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 150

![rule 150](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20150.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 151

![rule 151](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20151.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: 159, 183, 191, 215, 223, 247, 255

#### Generating Function:	1



## Rule 153

![rule 153](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20153.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 155

![rule 155](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20155.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 157

![rule 157](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20157.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 158

![rule 158](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20158.bmp?raw=true)

#### Sequence: 1, 7, 29, 115, 477, 1843, 7645, 29491, ...

#### Duplicates: none

#### Generating Function:	(1 + 7x + 12x^2^ - 4x^3^) / (1 - x^2^)(1 - 16x^4^)



## Rule 163

![rule 163](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20163.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 165

![rule 165](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20165.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 167

![rule 167](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20167.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 169

![rule 169](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20169.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 173

![rule 173](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20173.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 175

![rule 175](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20175.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 177

![rule 177](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20177.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 179

![rule 179](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20179.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 181

![rule 181](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20181.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 182

![rule 182](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20182.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 185

![rule 185](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20185.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 187

![rule 187](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20187.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 188

![rule 188](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20188.bmp?raw=true)

#### Sequence: 1, 3, 5, 15, 29, 55, 93, 247, ...

#### Duplicates: none

#### Generating Function:	(1 + 3x + 4x^2^ + 12x^3^ + 8x^4^ - 8x^5^) / (1 - x^2^)(1 - 16x^4^)



## Rule 189

![rule 189](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20189.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## rule 190

![rule 190](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20190.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 193

![rule 193](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20193.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 195

![rule 195](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20195.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 197

![rule 197](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20197.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 199

![rule 199](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20199.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 201

![rule 201](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20201.bmp?raw=true)

#### Sequence: 1, 0, 1, 0, 1, 0,1, 0, ...

#### Duplicates: none

#### Generating Function:	1 / (1 - x^2^)



## Rule 203

![rule 203](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20203.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 205

![rule 205](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20205.bmp?raw=true)

#### Sequence: 1, 1, 1, 1, 1, 1, 1, 1, ...

#### Duplicates: none

#### Generating Function:	1 / (1 - x)



## Rule 206

![rule 206](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20206.bmp?raw=true)

#### Sequence: 1, 3, 7, 15, 31, 63, 127, 255, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 207

![rule 207](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20207.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 209

![rule 209](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20209.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: 241

#### Generating Function:	1



## Rule 211

![rule 211](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20211.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 213

![rule 213](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20213.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 214

![rule 214](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20214.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 217

![rule 217](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20217.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 219

![rule 219](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20219.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 220

![rule 220](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20220.bmp?raw=true)

#### Sequence: 1, 3, 7, 15, 31, 63, 127, 255, ...

#### Duplicates: 252

#### Generating Function:	1 / (1-x)(1 - 2x)



## Rule 221

![rule 221](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20221.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 222

![rule 222](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20222.bmp?raw=true)

#### Sequence: 1, 7, 31, 127, 511, 2047, 8191, 32767, ...

#### Duplicates: 254

#### Generating Function:	(1 + 2x) / (1 - x)(1 - 4x)



## Rule 225

![rule 225](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20225.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 227

![rule 227](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20227.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 229

![rule 229](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20229.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 230

![rule 230](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20230.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 231

![rule 231](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20231.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 233

![rule 233](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20233.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 235

![rule 235](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20235.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 237

![rule 237](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20237.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 239

![rule 239](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20239.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 243

![rule 243](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20243.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 245

![rule 245](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20245.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 246

![rule 246](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20246.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 249

![rule 249](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20249.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 251

![rule 251](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20251.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 253

![rule 253](https://github.com/holmanej/ECA-GenFunc/blob/main/Patterns%2064x32/rule%20253.bmp?raw=true)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



# Variations of Starting Conditions


# Generating Functions of Elementary Cellular Automata from a Single Cell

### Introduction

A generating function provides a concise description of a sequence of numbers. Described below are the patterns and their resulting generating functions of the 256 rules of elementary cellular automata driven by a single cell. The sequences described are obtained by calculating the pattern in a 64 by 32 cell plane starting from a cell placed at column 32 in row 0 and interpreting living and dead cells in subsequent rows as 1s and 0s respectively to create a binary representation (unless noted otherwise).



## Rule 0

![rule 0](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 0.bmp)
[rule 0](holmanej.github.com/ECA-GenFunc/tree/main/Patterns%2064x32\rule 0.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: 8, 32, 40, 64, 72, 96, 104, 128, 136, 160, 168, 192, 200, 224, 232

#### Generating Function:	1



## Rule 1

![rule 1](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 1.bmp)

#### Sequence: 1, 0, 1, 0, 1, 0, 1, 0, ...

#### Duplicates: 33

#### Generating Function: 1 / (1 - x^2^)



## Rule 2

![rule 2](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 2.bmp)

#### Sequence: 1, 2, 4, 8, 16, 32, 64, 128, ...

#### Duplicates: 10, 34, 42, 66, 74, 98, 106, 130, 138, 162, 170, 194, 202, 226, 234

#### Generating Function:	-1 / (2x - 1)



## Rule 3

![rule 3](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 3.bmp)

#### Sequence: 1/2, 0, 1/4, 0, 1/8, 0, 1/16, 0, ...

#### Duplicates: 35

#### Generating Function:	1 / (2 - x^2^)



## Rule 4

![rule 4](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 4.bmp)

#### Sequence: 1, 1, 1, 1, 1, 1, 1, 1, ...

#### Duplicates: 12, 36, 44, 68, 76, 100, 108, 132, 140, 164, 172, 196, 204, 228, 236

#### Generating Function:	1 / (1 - x)



## Rule 5

![rule 5](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 5.bmp)

#### Sequence: 1, 1, 1, 1, 1, 1, 1, 1, ...

#### Duplicates: none

#### Generating Function:	1 / (1 - x)



## Rule 6

![rule 6](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 6.bmp)

#### Sequence: 1, 3, 4, 12, 16, 48, 64, 196, ...

#### Duplicates: 38, 134, 166

#### Generating Function:	(-3x - 1) / (2x - 1)



## Rule 7

![rule 7](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 7.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 9

![rule 9](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 9.bmp)

#### Sequence: 7/4, 1, 7/16, 1/4, 7/64, 1/16, 7/256, 1/64, ...

(only the gliders starting at row 4)

#### Duplicates: none

#### Generating Function:	(7 + 2x) / (4 - x^2^)



## Rule 11

![rule 11](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 11.bmp)

#### Sequence: 3/4, 0, 3/16, 0, 3/64, 0, 3/256, 0, ...

#### Duplicates: none

#### Generating Function:	3 / (4 - x^2^)



## Rule 13

![rule 13](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 13.bmp)

#### Sequence: 1/4, 5/16, 21/64, 85/256, 341/1024, 1365/4096, 21845/65536, 87381/262144

#### Duplicates: none

#### Generating Function:	-1 / (4 - x)(x - 1)



## Rule 14

![rule 14](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 14.bmp)

#### Sequence: 1, 3, 6, 12, 24, 48, 96, 192, ...

#### Duplicates: 46, 142, 174

#### Generating Function:	(-x - 1) / (2x - 1)



## Rule 15

![rule 15](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 15.bmp)

#### Sequence: 1/4, 0, 1/16, 0, 1/64, 0, 1/256, 0, ...

#### Duplicates: none

#### Generating Function:	1 / (4 - x^2^)



## Rule 16

![rule 16](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 16.bmp)

#### Sequence: 1, 1/2, 1/4, 1/8, 1/16, 1/32, 1/64, 1/128, ...

#### Duplicates: 24, 48, 56, 80, 88, 112, 120, 144, 152, 176, 184, 208, 216, 240, 248

#### Generating Function:	-1 / (x - 2)



## Rule 17

![rule 17](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 17.bmp)

#### Sequence: 1, 0, 2, 0, 4, 0, 8, 0, ...

#### Duplicates: 49

#### Generating Function:	-1 / (2x^2^ - 1)



## Rule 18

![rule 18](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 18.bmp)

#### Sequence: 1, 5, 17, 85, 257, 1285, 4369, 21845, ...

#### Duplicates: 26, 82, 90, 146, 154, 210, 218

#### Generating Function:	1



## Rule 19

![rule 19](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 19.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 20

![rule 20](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 20.bmp)

#### Sequence: 1, 1/2, 3/4, 1/8, 3/16, 1/32, 3/64, 1/128, ...

#### Duplicates: 52, 148, 180

#### Generating Function:	(-3x - 2) / (x^2 - 4)



## Rule 21

![rule 21](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 21.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 22

![rule 22](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 22.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 23

![rule 23](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 23.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: 31, 55, 63, 87, 95, 119, 127

#### Generating Function:	1



## Rule 25

![rule 25](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 25.bmp)

#### Sequence: 7, 4, 7/2, 2, 7/4, 1, 7/8, 1/2, ...

#### Duplicates: none

#### Generating Function:	(14 + 8*x) / (2 - x^2^)



## Rule 27

![rule 27](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 27.bmp)

#### Sequence: 1/2, 0, 1/4, 0, 1/8, 0, 1/16, 0, ...

#### Duplicates: none

#### Generating Function:	1 / (2 - x^2^)



## Rule 28

![rule 28](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 28.bmp)

#### Sequence: 1, 3, 5, 11, 21, 43, 85, 171, ...

#### Duplicates: 156

#### Generating Function:	(1 + 2x) / (1 + x)(1 - 2x)



## Rule 29

![rule 29](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 29.bmp)

#### Sequence: 1, 1, 1, 1, 1, 1, 1, 1, ...

#### Duplicates: none

#### Generating Function:	1 / (1 - x)



## Rule 30

![rule 30](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 30.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 37

![rule 37](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 37.bmp)

#### Sequence: 7/2, 0, 7/2, 0, 7/2, 0, 7/2, 0, ...

#### Duplicates: none

#### Generating Function:	7 / 2(1 - x)



## Rule 39

![rule 39](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 39.bmp)

#### Sequence: 1/2, 0, 1/4, 0, 1/8, 0, 1/16, 0, ...

#### Duplicates: none

#### Generating Function:	1 / (2 - x^2^)



## Rule 41

![rule 41](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 41.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 45

![rule 45](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 45.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 47

![rule 47](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 47.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 50

![rule 50](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 50.bmp)

#### Sequence: 1, 5, 21, 85, 341, 1365, 5461, 21845, ...

#### Duplicates: 58, 114, 122, 178, 186, 242, 250

#### Generating Function:	1 / (1 - x)(1 - 4x)



## Rule 51

![rule 51](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 51.bmp)

#### Sequence: 1, 0, 1, 0, 1, 0, 1, 0, ...

#### Duplicates: none

#### Generating Function:	1 / (1 - x^2^)



## Rule 53

![rule 53](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 53.bmp)

#### Sequence: 1, 2, 4, 8, 16, 32, 64, 128, ...

#### Duplicates: none

#### Generating Function:	-1 / (2x - 1)



## Rule 54

![rule 54](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 54.bmp)

#### Sequence: 1, 7, 17, 119, 273, 1911, 4369, 30583, ...

#### Duplicates: none

#### Generating Function:	(1 + 7x) / (1 - x^2^)(1 - 16x^2^)



## Rule 57

![rule 57](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 57.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 59

![rule 59](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 59.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 60

![rule 60](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 60.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 61

![rule 61](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 61.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 62

![rule 62](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 62.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 65

![rule 65](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 65.bmp)

#### Sequence: 7, 1, 28, 4, 118, 16, 448, 64, ...

#### Duplicates: none

#### Generating Function:	(7 + x) / (4x^2^ - 2)



## Rule 67

![rule 67](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 67.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 69

![rule 69](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 69.bmp)

#### Sequence: 1, 5, 21, 85, 341, 1365, 5461, 21845, 87381

#### Duplicates: none

#### Generating Function:	1 / (4x - 1)(x - 1)



## Rule 70

![rule 70](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 70.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: 198

#### Generating Function:	1



## Rule 71

![rule 71](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 71.bmp)

#### Sequence: 1, 1, 1, 1, 1, 1, 1, 1, ...

#### Duplicates: none

#### Generating Function:	1 / (1 - x)



## Rule 73

![rule 73](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 73.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 75

![rule 75](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 75.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 77

![rule 77](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 77.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 78

![rule 78](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 78.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 79

![rule 79](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 79.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 81

![rule 81](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 81.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: 113

#### Generating Function:	1



## Rule 83

![rule 83](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 83.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 84

![rule 84](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 84.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: 116, 212, 244

#### Generating Function:	1



## Rule 85

![rule 85](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 85.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 86

![rule 86](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 86.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 89

![rule 89](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 89.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 91

![rule 91](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 91.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 92

![rule 92](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 92.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 93

![rule 93](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 93.bmp)

#### Sequence: 1, 5, 21, 85, 341, 1365, 5461, 21845, 87381

#### Duplicates: none

#### Generating Function:	1 / (4x - 1)(x - 1)



## Rule 94

![rule 94](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 94.bmp)

#### Sequence: 1, 7, 27, 119, 427, 1879, 6827, 30039, ...

#### Duplicates: none

#### Generating Function:	(1 + 2x)(1 + 5x - 16x^4^) / (1 - x^2^)(1 - 16x^4^)



## Rule 97

![rule 97](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 97.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 99

![rule 99](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 99.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 101

![rule 101](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 101.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 102

![rule 102](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 102.bmp)

#### Sequence: 1, 3, 5, 15, 17, 51, 85, 255, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 103

![rule 103](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 103.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 105

![rule 105](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 105.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 107

![rule 107](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 107.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 109

![rule 109](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 109.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 110

![rule 110](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 110.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 111

![rule 111](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 111.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 115

![rule 115](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 115.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 117

![rule 117](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 117.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 118

![rule 118](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 118.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 121

![rule 121](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 121.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 123

![rule 123](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 123.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 124

![rule 124](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 124.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 125

![rule 125](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 125.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 126

![rule 126](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 126.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 129

![rule 129](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 129.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: 161

#### Generating Function:	1



## Rule 131

![rule 131](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 131.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 133

![rule 133](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 133.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 135

![rule 135](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 135.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 137

![rule 137](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 137.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 139

![rule 139](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 139.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: 171

#### Generating Function:	1



## Rule 141

![rule 141](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 141.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 143

![rule 143](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 143.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 145

![rule 145](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 145.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 147

![rule 147](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 147.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 149

![rule 149](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 149.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 150

![rule 150](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 150.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 151

![rule 151](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 151.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: 159, 183, 191, 215, 223, 247, 255

#### Generating Function:	1



## Rule 153

![rule 153](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 153.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 155

![rule 155](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 155.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 157

![rule 157](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 157.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 158

![rule 158](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 158.bmp)

#### Sequence: 1, 7, 29, 115, 477, 1843, 7645, 29491, ...

#### Duplicates: none

#### Generating Function:	(1 + 7x + 12x^2^ - 4x^3^) / (1 - x^2^)(1 - 16x^4^)



## Rule 163

![rule 163](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 163.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 165

![rule 165](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 165.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 167

![rule 167](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 167.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 169

![rule 169](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 169.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 173

![rule 173](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 173.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 175

![rule 175](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 175.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 177

![rule 177](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 177.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 179

![rule 179](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 179.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 181

![rule 181](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 181.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 182

![rule 182](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 182.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 185

![rule 185](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 185.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 187

![rule 187](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 187.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 188

![rule 188](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 188.bmp)

#### Sequence: 1, 3, 5, 15, 29, 55, 93, 247, ...

#### Duplicates: none

#### Generating Function:	(1 + 3x + 4x^2^ + 12x^3^ + 8x^4^ - 8x^5^) / (1 - x^2^)(1 - 16x^4^)



## Rule 189

![rule 189](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 189.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## rule 190

![rule 190](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 190.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 193

![rule 193](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 193.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 195

![rule 195](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 195.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 197

![rule 197](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 197.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 199

![rule 199](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 199.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 201

![rule 201](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 201.bmp)

#### Sequence: 1, 0, 1, 0, 1, 0,1, 0, ...

#### Duplicates: none

#### Generating Function:	1 / (1 - x^2^)



## Rule 203

![rule 203](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 203.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 205

![rule 205](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 205.bmp)

#### Sequence: 1, 1, 1, 1, 1, 1, 1, 1, ...

#### Duplicates: none

#### Generating Function:	1 / (1 - x)



## Rule 206

![rule 206](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 206.bmp)

#### Sequence: 1, 3, 7, 15, 31, 63, 127, 255, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 207

![rule 207](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 207.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 209

![rule 209](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 209.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: 241

#### Generating Function:	1



## Rule 211

![rule 211](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 211.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 213

![rule 213](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 213.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 214

![rule 214](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 214.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 217

![rule 217](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 217.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 219

![rule 219](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 219.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 220

![rule 220](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 220.bmp)

#### Sequence: 1, 3, 7, 15, 31, 63, 127, 255, ...

#### Duplicates: 252

#### Generating Function:	1 / (1-x)(1 - 2x)



## Rule 221

![rule 221](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 221.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 222

![rule 222](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 222.bmp)

#### Sequence: 1, 7, 31, 127, 511, 2047, 8191, 32767, ...

#### Duplicates: 254

#### Generating Function:	(1 + 2x) / (1 - x)(1 - 4x)



## Rule 225

![rule 225](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 225.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 227

![rule 227](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 227.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 229

![rule 229](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 229.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 230

![rule 230](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 230.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 231

![rule 231](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 231.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 233

![rule 233](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 233.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 235

![rule 235](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 235.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 237

![rule 237](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 237.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 239

![rule 239](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 239.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 243

![rule 243](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 243.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 245

![rule 245](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 245.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 246

![rule 246](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 246.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 249

![rule 249](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 249.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 251

![rule 251](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 251.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



## Rule 253

![rule 253](C:\Users\holma\Documents\ECA Study\Patterns 64x32\rule 253.bmp)

#### Sequence: 1, 0, 0, 0, 0, 0, 0, 0, ...

#### Duplicates: none

#### Generating Function:	1



# Variations of Starting Conditions


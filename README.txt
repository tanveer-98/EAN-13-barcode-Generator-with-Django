How a barcode works:
leftguard(101)- 0(type of barcode) - 51000(manufacturer code)-centerguard-01251(product code)-7(modulo checkdigit)-rightguard(101)

types of barcode:
0 = standard 
2 = weighed items
3 = pharmacy
5 = coupons

how is the barcode number verified using the modulo checkdigit
 

0  5 1 0 0 0   0 1 2 5  1    7
1  2 3 4 5 6   7 8 9 10 11

3x(sum of all odd postitions)+ (sum of all even positions)
3(0+1+0+0+2+1) +(5+0+0+1+5) = 3x(4) +11= 23

subtract from the higher multipple of 10 which is 30

30-23 =7 which is equal to the modulo checkdigit so the barcode is correctly scanned


EAN-13 barcode:

5(country code)  [ 9 0 0 9 4 2 ](manufacturer code)   [3 0 4  0   0](product code)    [checkdigit]
1                  2 3 4 5 6 7                         8 9 10 11 12


3x(sum of all even postitions)+ (sum of all odd positions)

3x(9+0+4+3+4+0)+(5+0+9+2+0+0)=3x(20)+(16)= 60+16= 76 

the next highest multiple of 10 for 76 is 80

so the checkdigit= 80-76 = 4



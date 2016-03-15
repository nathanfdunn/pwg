# PWG

PWG lets you generate random passwords from a pattern. Users can choose a pattern that satisfies certain password requirements (number of characters, inclusion of digits, special characters, etc.) and have a password randomly generated that fits the pattern. PWG will also calculate the entropy of the pattern to indicate how strong the generated passwords are.

# Pattern String Character Sets
```
Y:  A letter
0:  A digit
@:  A symbol
A:  A vowel
Z:  A consonant
```
Lowercase varients of Y, A, and Z are also available.

The specification of vowels and consonants allows the generation of passwords that can be remembered phonetically.

# Usage
```
> python pwg.py ZazaZazaZaza00@ -n 10
TaquLukuYiyu77@
XakiXemuGace90>
TohiBeyaSuvu37-
RoqaRixoBefi77{
ZoyiNiteVoga40_
WovuHakiGila97-
CiheHuluDiva29[
NeceNoniBete50+
QipiDiniDejo71*
BedoPeluJema03/

Entropy: 51.9293292958 bits
```

# Options

## pattern
The pattern string used to generate the password(s).

If not supplied, defaults to `ZazaZazaZaza00@`, which tends to generate passwords that are strong, relatively easy to memorize, and satisfy most password requirements.

## -n
Number of passwords to generate.

If not supplied, defaults to 1.

## -i
Case-insensitivity.

If supplied, alphabetic characters in resultant passwords will be randomly uppercase or lowercase, irrespective of the case of the characters in the pattern string.

## -e
Suppress entropy calculation.

If supplied, there will be no entropy calculation. Potentially useful if generating a file of passwords.

### A Note on Entropy
The entropy calculation indicates the strength of the pattern in terms of the number of passwords that could possibly be generated from it. Thus, it is valid for evaluating a brute-force attack if the attacker knows the pattern string (a worst-case scenario). However, be mindful that a generated password could be much weaker than the entropy would indicate. For instance, the pattern string `Yyyyyyyy000` could generate `Password123`, which would be one of the first passwords an attacker is likely to try.

import random, string, argparse, sys, math

defaultPattern = 'ZazaZazaZaza00@'

rand = random.SystemRandom()

parser = argparse.ArgumentParser(description='''
Password Generator
This tool lets you generate random passwords from a pattern.
The tool will also tell you how strong the pattern is in
terms of the number of possible passwords.
Characters to be used in the pattern string are
Y, 0, @, A, Z. These correspond to a letter, a number, a symbol,
 a vowel, or a consonant, respectively. The letter-based symbols
 also come in lowercase variety. The case of the generated letter
will match the case of the symbol, unless the -i flag is present.
''')
parser.add_argument('pattern', default=defaultPattern, nargs='?', help='The pattern string to generate passwords')
parser.add_argument('-n', metavar='N', default=1, type=int, help='Number of passwords to generate')
parser.add_argument('-i', action='store_true', help='Make the pattern case-insensitive')
parser.add_argument('-e', action='store_true', help='Suppress entropy calculation')

alphabet = string.lowercase
vowels = 'aeiou'
consonants = ''.join(c for c in alphabet if c not in vowels)
numbers = string.digits
symbols = string.punctuation

charMap = {
  'a' : vowels,
  'y' : alphabet,
  'z' : consonants,
  'A' : vowels.upper(),
  'Y' : alphabet.upper(),
  'Z' : consonants.upper(),
  '0' : numbers,
  '@' : symbols
}

def generatePassword(fmtStr):
  return ''.join(rand.choice(charMap[c]) for c in fmtStr)

def calcEntropy(fmtStr):
  return sum( math.log(len(charMap[c]), 2) for c in fmtStr)

opts = parser.parse_args()

for i in range(opts.n):
  pwd = generatePassword(opts.pattern)
  if opts.i:
    pwd = ''.join( rand.choice([c.upper(), c.lower()]) for c in pwd)
  sys.stdout.write(pwd+'\n')

entropy = calcEntropy(opts.pattern)
if opts.i:
  # Add 1 bit for every letter
  entropy += sum(c.lower() in 'ayz' for c in opts.pattern)

if not opts.e:
  sys.stdout.write( '\nEntropy: {S} bits\n'.format(S=entropy) )

# Write a function, overlap_subsequence, that takes in two strings as arguments. The function should return the length of the longest overlapping subsequence.

# A subsequence of a string can be created by deleting any characters of the string, while maintaining the relative order of characters.

def overlap_subsequence(string_1, string_2):
  pass # todo

#! TEST_00
overlap_subsequence("dogs", "daogt") # -> 3

#! TEST_01
overlap_subsequence("xcyats", "criaotsi") # -> 4

#! TEST_02
overlap_subsequence("xfeqortsver", "feeeuavoeqr") # -> 5

#! TEST_03
overlap_subsequence("kinfolklivemustache", "bespokekinfolksnackwave") # -> 11

#! TEST_04
overlap_subsequence(
  "mumblecorebeardleggingsauthenticunicorn",
  "succulentspughumblemeditationlocavore"
) # -> 15


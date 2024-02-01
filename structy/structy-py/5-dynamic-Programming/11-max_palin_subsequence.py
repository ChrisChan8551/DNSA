# Write a function, max_palin_subsequence, that takes in a string as an argument. The function should return the length of the longest subsequence of the string that is also a palindrome.

# A subsequence of a string can be created by deleting any characters of the string, while maintaining the relative order of characters.

def max_palin_subsequence(string):
  pass # todo

#! TEST_00
max_palin_subsequence("luwxult") # -> 5

#! TEST_01
max_palin_subsequence("xyzaxxzy") # -> 6

#! TEST_02
max_palin_subsequence("lol") # -> 3

#! TEST_03
max_palin_subsequence("boabcdefop") # -> 3

#! TEST_04
max_palin_subsequence("z") # -> 1

#! TEST_05
max_palin_subsequence("chartreusepugvicefree") # -> 7

#! TEST_06
max_palin_subsequence("qwueoiuahsdjnweuueueunasdnmnqweuzqwerty") # -> 15

#! TEST_07
max_palin_subsequence("enamelpinportlandtildecoldpressedironyflannelsemioticsedisonbulbfashionaxe") # -> 31

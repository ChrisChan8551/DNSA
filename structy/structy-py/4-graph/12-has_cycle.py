# Write a function, has_cycle, that takes in an object representing the adjacency list of a directed graph. The function should return a boolean indicating whether or not the graph contains a cycle.

def has_cycle(graph):
  pass # todo

#! TEST_00
has_cycle({
  "a": ["b"],
  "b": ["c"],
  "c": ["a"],
}) # -> True

#! TEST_01
has_cycle({
  "a": ["b", "c"],
  "b": ["c"],
  "c": ["d"],
  "d": [],
}) # -> False

#! TEST_02
has_cycle({
  "a": ["b", "c"],
  "b": [],
  "c": [],
  "e": ["f"],
  "f": ["e"],
}) # -> True

#! TEST_03
has_cycle({
  "q": ["r", "s"],
  "r": ["t", "u"],
  "s": [],
  "t": [],
  "u": [],
  "v": ["w"],
  "w": [],
  "x": ["w"],
}) # -> False

#! TEST_04
has_cycle({
  "a": ["b"],
  "b": ["c"],
  "c": ["a"],
  "g": [],
}) # -> True

#! TEST_05
has_cycle({
  "a": ["b"],
  "b": ["c"],
  "c": ["d"],
  "d": ["b"],
}) # -> True

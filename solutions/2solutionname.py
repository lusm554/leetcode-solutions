#!/usr/bin/env python3

import sys

def main(problem, ext):
  '''
  Converts name of problem in leetcode format to unix format for files.
  Arguments
  ---------
    problem: name of leetcode problem
    ext: name of unix file extention
  '''
  problem = problem.replace(".", "")
  problem = problem.lower()
  problem = problem.split(" ")
  problem = "-".join(problem) + ext 
  return problem

if __name__ == "__main__":
  problemname = " ".join(sys.argv[1:])
  unixname = main(problemname, ext=".py")
  print(unixname)

# Inspired by https://github.com/hyper-neutrino
# Move this code into your .bashrc or .zshrc file to use it
export AOC="~/personal/advent_of_code" # Change this to the path to your advent of code folder
export AOC_COOKIE="..." # Your session cookie from adventofcode.com. You can find it in your browser's dev tools

alias aoc="cd $AOC"
alias aos="python main.py < input.txt"
alias aot="echo -ne '\\e[0;36m'; python main.py < test.txt; echo -ne '\\e[0m'"
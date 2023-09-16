# 1v1MatchupProgram
A Python File I/O Program based on ryyjyywyy's 1v1 Teambuilding Program.

This current rendition of the program is actually a refractor of the original made in 2021 with better programming practices and paradigms, which led to approximately 65% code reduction.

## Technologies Used
```sh
Language: Python
Libraries: random, csv
```

## Main Idea

The CSV File accompanied by this program is a sample CSV File with auto-generated matchups. IDs are written similar to ``metagross_1``. Here's a [semi-complete version of what this would look like.](https://docs.google.com/spreadsheets/d/1ZGt7NMoVV16ke_PpItzFWDzCYKiJtPBW5Hq9RuKgSDA/edit?usp=sharing)

The program runs a prompt menu where you select the Pokemon you want to add to your team (1, 2, or random), a filter selection where you give pokemon that you want to beat, and returns the highest-scoring teams in the system.

The algorithm goes through every single unique combination of teams possible to generate that result.

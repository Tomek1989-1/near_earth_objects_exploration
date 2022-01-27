### Project/README file creation date
January 25th 2022

### Project Title
Exploring Close Approaches of Near-Earth Objects

### Description
In this project I used Python to search for and explore close approaches of near-Earth objects (NEOs), using data from NASA/JPL's Center for Near-Earth Object Studies

This script can be invoked from the command line:

    $ python3 main.py {inspect,query} [args]

The `inspect` subcommand looks up an NEO by name or by primary designation, and
optionally lists all of that NEO's known close approaches:

    $ python3 main.py inspect -pdes "2020 AP1"
    $ python3 main.py inspect -name Halley
    $ python3 main.py inspect -verbose -name Halley

The `query` subcommand searches for close approaches that match given criteria:

    $ python3 main.py query -date 1969-07-29
    $ python3 main.py query -start-date 2020-01-01 -end-date 2020-01-31 -max-distance 0.025

The set of results can be limited in size and/or saved to an output file in CSV
or JSON format:

    $ python3 main.py query -limit 5 -outfile results.csv
    $ python3 main.py query -limit 15 -outfile results.json

If needed, the script can load data from data files other than the default with
`-neofile` or `-cadfile`.

### Credits
Udacity - Intermediate Python
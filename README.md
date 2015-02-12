![alt tag](http://galenscovell.github.io/css/pics/wator.png)

Wa-Tor
======

Population Dynamics Simulation created in Python. 
Lots of fun to design and lots of fun to watch! :]

<b>Description:</b>
<blockquote>Wa-Tor is a population dynamics simulation devised by Alexander Keewatin Dewdney and presented in the December 1984 issue of Scientific American in a 5-page article entitled "Computer Recreations: Sharks and fish wage an ecological war on the toroidal planet Wa-Tor".</blockquote>

<blockquote>Wa-Tor is usually implemented as a 2-dimensional grid with 3 colours, one for fish, one for sharks and one for empty water. If a creature moves past the edge of the grid, it reappears on the opposite side. The sharks are predatory and eat the fish. Both sharks and fish live, move, reproduce and die in Wa-Tor according to simple rules from which complex emergent behavior can be seen to arise.</blockquote>


<b>Requirements:</b>
* Python 3.4
* PyGame 1.9.2a0
  <blockquote>Use the unofficial pygame build for Python 3.4 from here: http://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame</blockquote>

<b>Installing Unofficial pygame for Python 3.4:</b>
* Save .whl file from above to somewhere you'll remember
* Open a terminal
* Enter: 'pip install wheel' (without quotes)
* Navigate to the previous directory with .whl file
* Enter: 'pip install some-package.whl' (without quotes)

<b>Usage:</b> 
<blockquote><b>python wator.py</b> [ -h ] [ -c ] [ -f ] [ -s ] [ -fps ]</blockquote>

Arguments:
*  -h, --help 
<blockquote> Show this help message and exit </blockquote>
*  -c, --num_chronons 
<blockquote> Runtime length. (Default: 1000) </blockquote>
*  -f, --num_fish 
<blockquote> Number of fish. (Default: 80) </blockquote>
*  -s, --num_sharks 
<blockquote> Number of sharks. (Default: 20) </blockquote>
* -fps, --framerate 
<blockquote> Framerate (Default: 10) </blockquote>

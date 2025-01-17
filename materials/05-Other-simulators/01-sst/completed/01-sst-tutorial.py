"""This SST configuration script is used to simulate a very simple SST
simulation. The two components are connected by a link. They both send 20
events to each other prior to the simulation ending.

Usage
-----

```bash
sst materials/05-Other-simulators/01-sst/01-sst-tutorial.py
```

"""

import sst

component0 = sst.Component("c0", "simpleElementExample.example0")
component1 = sst.Component("c1", "simpleElementExample.example0")

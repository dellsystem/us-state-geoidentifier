Given a latitude/longitude pair, figure out the US state this belongs to (if
any) without having to rely on third-party APIs. Created for use in my
geolocation research at the [Network Dynamics lab](http://networkdynamics.org/)
and published on Github on the off-chance that someone finds it useful.

**Warning**: I got the state bounding coordinates from a pretty sketchy Google
Doc I found somewhere on the Internet. Use at your own peril.

```
import utils

state = utils.find_state(latitude, longitude) # returns the two-letter code
if state is not None:
    # Do something
```

test_strInput = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""

# 30 minutes to get out of the cave
# no time to retrace steps
# pipes and PRVs
# input is the flow rate through each valve if it were opened in pressure units per minute
# and the corresponding tunnels leading between valves
# AA is the root of the tree, the valve in the room where you stand
# it will take 1 minute to open a valve and another minute to travel to another valve
# step and operation each take 1 minute
# all valves begin closed
# what is the most pressure you can release?
# see that valve AA has a flowrate of 0
# earliest you can open valve B is with 28 minutes remaining, has flowrate of 13 
# so doing so would drop 364=28*13 units of pressure

# what is the most pressure you can release

# draw the network as nodes and edges
# add values to the nodes corresponding to the flowrate

tree_elements = [x.split(' ') for x in test_strInput.splitlines() if x != '']

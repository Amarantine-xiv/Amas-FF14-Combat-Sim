# Amas-FF14-Combat-Sim

This tool simulates the damage of given gearsets and rotations and produces the full distribution over damage values. Unlike other simulators/spreadsheets, this gives more than just expected damage with an approximation of damage variance- this is an accurate [Monte Carlo](https://en.wikipedia.org/wiki/Monte_Carlo_method) simulation that gives the full range and distribution over all possible damage values. This tool is currently written as a Python notebook (runnable through Google Colab). The tool has four advantages over existing simulators/spreadsheets:

1) handles the simulation of all FF14 job classes in a single place- no need to maintain multiple spreadsheets, etc.,

2) incorporates all damage rolls and crit/dh procs on a per-damage-instance basis, and rolls them every time the sim is run (currently you can do 1M simulation runs in a couple seconds),

3) enables the building of several useful community tools that either don't exist, or can be streamlined, using this sim as a backend (or just a loaded Python notebook as a hack), and

4) allows for the incorporation of procs in the simulation process itself.

We can build several useful tools on top of this simulator:

1) general gear and rotation planning, optimizing for average damage, parsing (high-variance sets), and minimizing the chance of hitting enrage due to bad luck,
2) fight-specific gear and rotation planning,
3) speed kill planning,
4) normalizing DPS from FFlogs to factor out "lucky" crit/dh farming,
5) resimming a a fight with a new gearset (assuming same gcd) or different shorter kill time to provide a more gear/kill time independent measure of performance, and
6) bis/rotation solver.

# Example Simulator Inputs and Outputs

Here is an example of the simulator's output of the WAR opener (with raid buffs- see below for actual raid buffs and timings):

![WAR opener output](https://github.com/Amarantine-xiv/Another-FF14-Combat-Sim/blob/main/ff14_sim_pics/war_rotation_output2.png?raw=true)

The way this rotation is specified is below:
![WHM opener input](https://github.com/Amarantine-xiv/Another-FF14-Combat-Sim/blob/main/ff14_sim_pics/whm_pom2.png?raw=true)

**Note that here, we assume each button is pressed as soon as possible, and the sim calculates cast times, animation locks, haste buffs (e.g., from Presence of Mind), etc. to figure out when each cast/skill will be performed, when the damage calculation will snapshot, and when the damage is applied.**

You can also simulate a specific timeline (like from a log) like this:
![Drk log input](https://github.com/Amarantine-xiv/Another-FF14-Combat-Sim/blob/main/ff14_sim_pics/drk_rotation.png?raw=true)

and the sim will give you an output like this:
![Drk log output](https://github.com/Amarantine-xiv/Another-FF14-Combat-Sim/blob/main/ff14_sim_pics/drk_rotation_result.png?raw=true)

# Acknowledgements
I'd like to thank the following people/groups for their help! Without them, this sim would not be at all possible:

[The Balance](https://www.thebalanceffxiv.com/)

Io Whitespirit

Hint and [Hint's damage calc repo](https://github.com/hintxiv/reassemble)

Fürst

IAmPythagoras and [IAmPythagoras's FFXIV-Combat-Simulator](https://github.com/IAmPythagoras/FFXIV-Combat-Simulator)

Cless

Kaiser08259



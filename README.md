# Amas-FF14-Combat-Sim

This open-source tool simulates the damage of given gearsets and rotations, producing the full distributions over damage values and various statistics, like the expected max damage over N runs (useful for parsers). Currently, all lvl 90 standard combat classes are supported. The tool is currently a Python notebook- see [CoreSimulator.ipynb](https://github.com/Amarantine-xiv/Amas-FF14-Combat-Sim/blob/main/CoreSimulator.ipynb) for the simulator and usage instructions. For issues/feature requests and news, join the [Discord](https://discord.gg/CV6sHj8h9D) server.

Unlike other simulators/spreadsheets, this gives more than just expected damage with an approximation of damage variance- this is an accurate [Monte Carlo](https://en.wikipedia.org/wiki/Monte_Carlo_method) simulation that gives the full range and distribution over all possible damage values. This tool is currently written as a Python notebook (runnable through Google Colab). The tool has four advantages over existing simulators/spreadsheets:

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

**If you have feedback on the sim or want to see some example results/rotations, please see [this spreadsheet](https://docs.google.com/spreadsheets/d/1O0ZdJyjMhUAC7YtkyvXPTSNtSAyOFnzm3MBGHTln914/edit?usp=sharing).**

# Example Simulator Inputs and Outputs

Here is an example of the simulator's output of the WAR opener (with raid buffs- see below for actual raid buffs and timings):

![WAR opener output](https://github.com/Amarantine-xiv/Amas-FF14-Combat-Sim/blob/main/ff14_sim_pics/war_rotation_output2.png?raw=true)

The way this rotation is specified is below:
![War opener input](https://github.com/Amarantine-xiv/Amas-FF14-Combat-Sim/blob/main/ff14_sim_pics/war_rotation2.png?raw=true)

**Note that here, we assume each button is pressed as soon as possible, and the sim calculates cast times, animation locks, haste buffs (e.g., from Presence of Mind), etc. to figure out when each cast/skill will be performed, when the damage calculation will snapshot, and when the damage is applied.**

You can also simulate a specific timeline (like from a log) like this (*Etro + FFlogs integration TBD. See Roadmap below.*):
![SAM log input](https://github.com/Amarantine-xiv/Amas-FF14-Combat-Sim/blob/main/ff14_sim_pics/sam_rotation_manual.png?raw=true)

# Roadmap
This sim is currently under active development under three workflows: improving usability, improving sim accuracy, and building tools on top of this sim. Here is the work planned:
1) Improve accuracy of sim- bug fixes, resource tracking for jobs (QOL improvement). *(~Mid February, 2024)*
2) Etro + FFlogs integration to re-sim fights to i) factor out damage variance, ii) re-sim fights with different gearsets (with the same GCD), and iii) re-sim fights with a different (shorter) kill time *(~Early March, 2024)*
3) Proc sim'ing + facilities for users to specify rotation logic *(~Early April, 2024)*
4) A public website with a graphical UI for rotation planning and logs loading + a public simulator backend for people to build on top of *(~End of April, 2024)*
5) QOL improvements for rotation planning on the website (save a rotation, plan-with-your-static) and logs analysis (compare vs. another log, factoring out gear and crit variance). *(~Mid May)*
6) Rotation/BiS solvers using ML *(~Early July 2024)*
7) Incorporation of newest theorycrafted damage formulas and Dawntrail changes when they come out *(continuous)*

# Acknowledgements
I'd like to thank the following people/groups for their help! Without them, this sim would not be at all possible:

[The Balance](https://www.thebalanceffxiv.com/)

Io Whitespirit

Hint and [Hint's damage calc repo](https://github.com/hintxiv/reassemble)

Fürst

IAmPythagoras and [IAmPythagoras's FFXIV-Combat-Simulator](https://github.com/IAmPythagoras/FFXIV-Combat-Simulator)

Cless

Kaiser08259



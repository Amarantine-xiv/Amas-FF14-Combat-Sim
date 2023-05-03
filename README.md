# Another-FF14-Combat-Sim

This tool simulates the damage of given gearsets and rotations for one or more players and, produces the full distribution over damage values. Unlike other simulators/spreadsheets, this gives more than just average damage with an approximation of damage variance- this is an accurate [Monte Carlo](https://en.wikipedia.org/wiki/Monte_Carlo_method) simulation that gives the full range and distribution over all possible damage values, similar to [SimulationCraft](https://www.simulationcraft.org/) for World of Warcraft.  The tool has four advantages over existing simulators/spreadsheets:

1) incorporates all damage rolls and crit/dh procs on a per-damage-instance basis, and rolls them every time the sim is run (currently you can do 1M simulation runs in a couple seconds),

2) incorporates everything the ecommunity knows about how damage in FF14 works (AFAIK),

3) handles the simulation of all FF14 job classes in a single notebook/tool- no need to maintain multiple spreadsheets, etc., and

4) enables the building of several useful community tools that either don't exist, or can be streamlined.

We can build several useful tools on top of this simulator:

1) general gear and rotation planning, optimizing for average damage, parsing (high-variance sets), and minimizing the chance of hitting enrage due to bad luck
2) fight-specific gear and rotation planning
3) speed kill planning
4) normalizing DPS logs to factor out "lucky" crit/dh farming
5) rotation solver

On #1:
We can use the simulator to plan BiS sets- given a gearset and rotation, we can already give the distribution (and average) of damage that will be dealt. Instead of dealing with potency-per-second and average raiding buffs, we can simulate any class' rotation, sim'ing instead 2 minute or more loops (or any rotation) to get a more accurate idea of damage dealt.
On parsing, since we can give the full distribution over damage, we can also find sets with higher damage potential (eg, higher crit/dh variance) and find, out of all those sets, which is likely to have the best potential. Often for parsing, we want sets with higher highs, even if the expected damage is lower. With this simulator, we can find such parsing sets.
On the flipside, we can also find sets with higher damage floors that are less sensitive to crit/dh variance. For example, we can find sets for TOP that may have lower expected dps, but have higher damage floors to make meeting DPS checks more consistent.

On #2:
Same as #1, but we can also input specific fight downtimes, and can factor in having to disengage from the boss into rotation planning.

On #3:
Same as #1, but we can simulate full party gear+rotations to see when given damage threshhold is met. Because the sim simulates on a per-damage instance basis rather than average damage over time, the sim should be able to model kill times to a degree accurate enough for the damage portion of speed kill planning (but not LB generation or healing/mit plans- this is future work).

On #4:
To parse high on some classes, an element of luck is needed. For example, late in the tier, a WHM run that does not crit/dh any miseries is unlikely to get a pink/gold parse. It may be frustrating to crit-farm and be at the whims of RNG. Also, from a learning perspective, it is harder to compare runs between players because there is an element of "did this person just get lucky?" always in play and it is hard to quantify how much of a run can be attributed to luck. With the simulator, we can look at the full distribution of damage, and compare two runs fairly based on metrics like expected damage, and damage from what equally "lucky" run would be from both runs.

On #5:
The simulator is written in Python in a Google Colab notebook. As such, it has access to a wide array of machine learning capabilities. Under the hood, the way the simulator is designed and implemented is amenable to standard reinforcement learning approaches (for those interested, the state = {time of the fight, set of buffs/debuffs, CDs, job resources, time to next gcd}, action = a button press, reward= whatever damage metric you like- eg, average rdps or "lucky" rdps). This is TBD, but for what its worth, the creator of this simulator has a PhD in machine learning and many years of industry experience doing those sort of thing.


# Example Simulator Inputs and Outputs

Here is an example of the simulator's output of the WHM opener with full raid buffs, which factors in the haste buff due to Presence of Mind:

![WHM opener output](https://github.com/Amarantine-xiv/Another-FF14-Combat-Sim/blob/main/ff14_sim_pics/war_pom_result.png?raw=true)

The way this rotation is specified is below:
![War opener input](https://github.com/Amarantine-xiv/Another-FF14-Combat-Sim/blob/main/ff14_sim_pics/whm_pom.png?raw=true)

**Note that here, we assume each button is pressed as soon as possible, and the sim calculates cast times, animation locks, haste buffs (e.g., from Presence of Mind), etc. to figure out when each cast/skill will be performed and when the damage calculation will snapshot. Note also WHM does not have a "rigid" GCD time in the sense that GCD cast and recast time differ based whether PoM is active- the simulator engine can model this for WHM as well as any other class where GCD times may differ for different skills (eg, DNC, SGE) or those with haste buffs (WHM, SAM, etc.)

You can also simulate a specific timeline (like from a log) like this:
![Drk log input](https://github.com/Amarantine-xiv/Another-FF14-Combat-Sim/blob/main/ff14_sim_pics/drk_rotation.png?raw=true)

# Acknowledgements
I'd like to thank the following people/groups for their help! Without them, this sim would not be at all possible:

Io Whitespirit

Hint and [Hint's damage calc repo](https://github.com/hintxiv/reassemble)

(Fürst)

(IAmPythagoras + [ff14 combat sim](https://github.com/IAmPythagoras/FFXIV-Combat-Simulato))

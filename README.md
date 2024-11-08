# CS 460: Final Project Worlds

This repository contains an indoor and outdoor worlds for Webots.

## Indoor World (Bruno Business Library 1st Floor)

The indoor world models the first floor of the Angelo Bruno Business Library.

![Bruno Business Library](https://raw.githubusercontent.com/MoenMi/project-cs460/refs/heads/main/project_cs460/worlds/.bruno-business-library.jpg)

To run this world, simply navigate to this current directory and run the following script:

```bash
bash run_indoor_sim.sh
```

If you would like to change any of the doors in the simulation, modify the final value in the `rotation` field for the given door in the `bruno-business-library.wbt` file. Note that this can also be done within the Webots simulation. 

```
Door {
  translation 35.5 1 0
  rotation 0 0 1 -1.5707953071795862
  name "door(13)"
  jointAtLeft FALSE
  doorHandle DoorLever {
    rotation 0 1 0 0.00131724
    jointAtLeft FALSE
    hasStaticParent TRUE
  }
}
```

## Outdoor World (Section of Tuscaloosa)

The outdoor world models an 800m-by-800m section of Tuscaloosa. This section of Tuscaloosa is located directly southwest of Bryant-Denny Stadium. This world was created with the help of the [OpenStreetMap Importer](https://cyberbotics.com/doc/automobile/openstreetmap-importer).

![Simulation Screenshot](https://raw.githubusercontent.com/MoenMi/project-cs460/refs/heads/main/project_cs460/worlds/.tuscaloosa.jpg)

![Map of Area](map.png)

To run this world, simply navigate to this current directory and run the following script:

```bash
bash run_outdoor_sim.sh
```

The outdoor world models the general road network of the city, with special attention paid to the intersections. Note, however, that the details of the roads are not very fleshed out outside of the northwestern portion of the map, since the OSM to Webots converter does handle many of the details of the roads.

import cadquery as cq
import TempFunction

# length, width and height of Si layer
Si_xlength = 30.0
Si_ylength = 30.0
Si_zlength = 5.0

# length, width and height of SiO2 layer
SiO2_xlength = Si_xlength
SiO2_ylength = Si_ylength
SiO2_zlength = 1.6

# center of interconnects
ic_centers = [(0.0, 0.0), (3.0, 0.0), (0.0, 3.0),\
              (-3.0, 0.0), (0.0, -3.0)]

# radius and height of interconnects
ic_radius = 1.0
ic_height = 1.0

# number of interconnects
n = len(ic_centers)

# interconnects model
hb_interconnects = cq.Workplane("XY").workplane(offset = -0.5*ic_height)
hb_interconnects = hb_interconnects.pushPoints(ic_centers)
hb_interconnects = hb_interconnects.circle(ic_radius).extrude(ic_height)

# substrate model
## SiO2 layer model
hb_substrate_top = cq.Workplane("XY").workplane(offset = 0.5*(SiO2_zlength+Si_zlength))
hb_substrate_top = hb_substrate_top.box(Si_xlength, Si_ylength, Si_zlength)

hb_substrate_bottom = hb_substrate_top.mirror(mirrorPlane="XY", basePointVector=(0, 0, 0))
hb_substrate_Si = hb_substrate_top.union(hb_substrate_bottom)
hb_substrate = hb_substrate_top.union(hb_substrate_bottom)

## Si layer model
hb_substrate_middle = cq.Workplane("XY")
hb_substrate_SiO2 = hb_substrate_middle.box(SiO2_xlength, SiO2_ylength, SiO2_zlength)

hb_substrate = hb_substrate.add(hb_substrate_SiO2)

## hb model
hb = hb_substrate.add(hb_interconnects)

# show hybrid bonding model
# show_object(hb_interconnects, name="hb_interconnects", options={"alpha":0.0, "color": (237, 125, 49)})
# show_object(hb_substrate_Si, name="Si_layer", options={"alpha":0.8, "color": (91, 155, 213)})
# show_object(hb_substrate_SiO2, name="SiO2_layer", options={"alpha":0.8, "color": (112, 173, 71)})

output_file = "hb_model.step"
cq.exporters.export(hb, output_file)

TempFunction.generate_geo(output_file)

def generate_geo(filename):
    f = open("hb_model.geo.in", "r")
    out_str = ""
    out_str += f.readline()
    out_str += f.readline()
    temp_str = f.readline()
    temp_str = temp_str.replace("hb_model.step", filename)
    out_str += temp_str
    for temp_str2 in f:
        out_str += temp_str2.replace("hb_model.mesh", filename.replace(".step", ".mesh"))
    f.close()
    new_name = filename.replace(".step", ".geo")
    f = open(new_name, "w")
    f.write(out_str)
    f.close()


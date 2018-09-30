#Metaris pin-mount telescoping cylinder dims
class Telecyl :
    def __init__(self,part_number, stroke, closed, extended, base_eye_width,base_pin_dia, rod_eye_width, rod_eye_dia):
        self.part_number = part_number
        self.stroke = stroke
        self.closed = closed
        self.extended = extended
        self.base_eye_width = base_eye_width
        self.base_pin_dia = base_pin_dia
        self.rod_eye_width = rod_eye_width
        self.rod_eye_dia = rod_eye_dia

telecyl1 = Telecyl("MH100-53-84P", 84,39.5,122.5,7,2,2,2)

telecyl2 = Telecyl("MH100-53-126P", 126,54.5,181.25,7,2,2,2)

telecyl3 = Telecyl("MH100-63-108P", 108,49.5,157.5,7.25,2,2,2)

telecyl4 = Telecyl("MH100-63-120P", 120,53.5,173.5,7.25,2,2,2)

telecyl5 = Telecyl("MH100-63-126P", 126,55.5,181.5,7.25,2,2,2)

telecyl6 = Telecyl("MH100-63-132P", 132,57.375,189.375,7.25,2,2,2)

telecyl7 = Telecyl("MH100-63-140P", 140, 60, 200, 7.25, 2,2,2)

telecyl8 = Telecyl("MH100-64-135P-175", 135,48.25,183,8,1.75,2.75,1.5)

telecyl9 = Telecyl("MH100-64-156P-175", 156,53.5,209.5,7.25,1.75,2.75,1.5)

telecyl10 = Telecyl("MH100-64-156P", 156,53.625, 209.625,7.25,2,1.5,2)

telecyl11 = Telecyl("MH100-74-135P", 135,48.5,183.5,8.625,2,2,2)

telecyl12 = Telecyl("MH100-74-156P", 156,53.75,209.75,8.625,2,2,2)

telecyl13 = Telecyl("MH100-85-190P", 190,54,233.25,9.5,2,2,2)

telecyl14 = Telecyl("MH100-85-220P", 220,60,269.25,9.5,2,2,2)

telecyl15 = Telecyl("MH100-85-235P", 235,65,299.25,9.5,2,2,2)

telecyl16 = Telecyl("MH100-85-250P", 250,68,317.25,9.5,2,2,2)

telecyl17 = Telecyl("MH100-85-265P", 265,74,335.25,9.5,2,2,2)

print(telecyl12.part_number)







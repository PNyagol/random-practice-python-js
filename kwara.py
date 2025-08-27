def info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

info(Name="Peter Nyagol", Age=32, Profession="Telecoms and Software Eng.", Residence="Ongata Rongat")

print("||.................................||")

info(Name="Joan Winga", Age=29, Profession="Nutrition & Dietetics", Residence="Ongata Rongai", Hobby="Gym", Club="Roraty Ongata Rongai District")

print("||.................................||")


def sam(*args):
    return sum(args)


print(sam(7, 20, 89))
print(sam(347, 220, 869))
import cmath

def curr_pow_pf(volts, curr, phase='A'):
    phase_shift = 0
    if phase == 'B':
        phase_shift = 2 * cmath.pi / 3
    if phase == 'C':
        phase_shift = 4 * cmath.pi / 3
    v = complex(volts) * cmath.rect(1, phase_shift)
    c = complex(curr)
    my_pow = v * c
    base_pow = abs(my_pow)
    pf = my_pow.real / base_pow
    print("base_power_{0} {1};".format(phase, str(base_pow)))
    print("current_pf_{0} {1};".format(phase, str(pf)))
    print("current_fraction_{0} {1};".format(phase, str(1.0)))
    return base_pow, pf

def pow_zip_pf(my_pow, phase='A'):
    base_pow = abs(my_pow)
    pf = my_pow.real / base_pow
    print("base_power_{0} {1};".format(phase, str(base_pow)))
    print("power_pf_{0} {1};".format(phase, str(pf)))
    print("power_fraction_{0} {1};".format(phase, str(1.0)))
    return base_pow, pf

def imp_pow_pf(volts, imp, phase='A'):
    phase_shift = 0
    if phase == 'B':
        phase_shift = 2 * cmath.pi / 3
    if phase == 'C':
        phase_shift = 4 * cmath.pi / 3
    v = complex(volts) * cmath.rect(1, phase_shift)
    i = complex(imp)
    my_pow = v * v / i
    base_pow = abs(my_pow)
    pf = my_pow.real / base_pow
    print("base_power_{0} {1};".format(phase, str(base_pow)))
    print("impedance_pf_{0} {1};".format(phase, str(pf)))
    print("impedance_fraction_{0} {1};".format(phase, str(1.0)))
    return base_pow, pf


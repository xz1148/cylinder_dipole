from necpp import *
import math
def handle_nec(result):
    if (result != 0):
        print nec_error_message()

def monopole_impedance(freq, base, length):
    wavelength = 3e8/(1e6*freq)
    n_seg = int(math.ceil(50*length/wavelength))
    nec = nec_create()
    handle_nec(nec_wire(nec, 1, n_seg, 0, 0, base, 0, 0, base+length, 0.002, 1.0, 1.0))
    # create a straight wire
    # nec_context* in_context
    # int tag_id
    # int segment_count number of segments
    # double xw1, yw1, zw1
    # double xw2, yw2, zw2
    # double rad, rdel, rrad (rdel, rrad is for tappered wires)

    handle_nec(nec_geometry_complete(nec, 1))
    # nec_geometry_complete(nec_context* int_context, int gpflag)
    # geometry ground plane flag
    # 0: no ground plane
    # 1: ground plane is present
    # -1: ground is present

    handle_nec(nec_fr_card(nec, 0, 2, freq, 1))
    # nec_fr_card(nec_context* in_context
    # int in_ifrq: 0 is linear range of frequency, 1 is log
    # int n_nfrq: number of frequencies
    # double in_freq_mhz: starting frequency in MHz
    # double in_del_freq: the frequency step (in MHz for ifrq = 0))

    handle_nec(nec_ex_card(nec, 0, 0, n_seg/3, 0, 1.0, 0, 0, 0, 0, 0))
    # nec_ex_card(nec_context* in_context
    # int extype
    # 0:voltage source
    # 1:incident plane wave, linear-polarization
    # 2:incident plane wave, right-hand
    # 3:incident plane wave, left-hand elliptic polarization
    # 4:elementary current source
    # 5:voltage source (current-slope-discontinuity)
    # int i2: tag number the source segment. This tag number along with the
    # number to be given in i3, which identifies the position of the segment in
    # a set of equal tag numbers, uniques definer the source segment
    # 0 means the source segment will be identified by using the absolute
    # segment number in i3
    # int i4: the maximum admittance caculation
    # voltage source:
    # float f1: real part of the voltage
    # float f2: imaginary part of the volatage
    # float f3: normalization factor
    # f4, f5, f6 blank


    handle_nec(nec_xq_card(nec, 0)) # Execute simulation
    # nec_xq_card(nec_context* in_context
    # int itmp1
    # 0 no patters requested
    # 1 generates pattern in XZ plane
    # 2 generates pattern in YZ plane
    # 3 generates pattern in both cases

    # Results
    z = complex(nec_impedance_real(nec,0), nec_impedance_imag(nec,0))
    # Cleanup
    nec_delete(nec)
    return z

z = monopole_impedance(freq=134.5, base=0.1, length=4.0)
print "f=134.5 z = (%6.1f,%+6.1fI) Ohms" % (z.real, z.imag)

import pathlib
import abjad
import arctic
import copy
import pathlib

import abjad
import arctic

import arctic.tools.FuzzyHarmony as FuzzyHarmony

from arctic.tools.accents import tenuto as tenuto
from arctic.tools.barlines import barline as barline
from arctic.tools.clef import clef as clef
from arctic.tools.FuzzyHarmony import Diad as Diad
from arctic.tools.FuzzyHarmony import LegatoArpeggio as LegatoArpeggio
from arctic.tools.material_methods import transpose_segment as transpose_segment
from arctic.tools.tremolo import tremolo as tremolo

from abjad import NamedPitch as NamedPitch
from typing import List



###########
### [E] ###
###########


this_current_directory =  pathlib.Path(__file__).parent 
test_build_path = arctic.build_path 
score = arctic.ScoreTemplate()
score_template = score()

segment_maker = arctic.SegmentMaker(
                                _lilypond_file=None,
                                _score=score_template,
                                current_directory=this_current_directory,
                                build_path=test_build_path,
                                segment_name='segment_E',
                                tempo=((1, 4), 50),
                                time_signatures=([(4, 4)] * 20),
                                )


#-----------------/________________________
# Pitch Material /  Constants for section /
#_______________/------------------------/

bfM9_42 = arctic.tetrads['bf_i']
bfM9_64 = arctic.invert_up(bfM9_42, 1)
bfM9_7 = arctic.invert_up(bfM9_42, 2)
bfM9_6 = arctic.invert_up(bfM9_42, 3)

bf9_42 = arctic.FuzzyHarmony('bf_v', bfM9_42) # emin7
bf9_64 = arctic.FuzzyHarmony('bf_v', bfM9_64) 
bf9_7 = arctic.FuzzyHarmony('bf_v', bfM9_7)   
bf9_6 = arctic.FuzzyHarmony('bf_v', bfM9_6)

amin7_6 = arctic.tetrads['g_ii']
amin7_64 = arctic.invert_up(amin7_6, 1)
amin7_42 = arctic.invert_up(amin7_6, 2)
amin7 = arctic.invert_up(amin7_6, 3)

am7_6 = arctic.FuzzyHarmony('g_ii', amin7_6)
am7_64 = arctic.FuzzyHarmony('g_ii', amin7_64) 
am7_42 = arctic.FuzzyHarmony('g_ii', amin7_42)   
am7 = arctic.FuzzyHarmony('g_ii', amin7)

""" 
    Make harmonies and fifth offsets in all octaves
    Note: octave names are in german:
    gross, klein, 
    ein-, zwei-, dreigestr = ein,- zwei-, dreigestrichen
    """

auth_one_ein_zw = [bf9_42, bf9_64, bf9_7, bf9_6]
auth_one_gr = arctic.transpose(auth_one_ein_zw, -24)
auth_one_kln_eing = arctic.transpose(auth_one_ein_zw, -12)

plag_one_zw_dr = arctic.transpose(auth_one_ein_zw, 19)
plag_one_ein_zw = arctic.transpose(auth_one_ein_zw, 7)
plag_one_gr = arctic.transpose(auth_one_ein_zw, -17)

auth_two_ein_zw = [am7_6, am7_64, am7_42, am7]

auth_two_gr_kln = arctic.transpose(auth_two_ein_zw, -24)
auth_two_kln_eing = arctic.transpose(auth_two_ein_zw, -12)
auth_two_zw_dr = arctic.transpose(auth_two_ein_zw, 12)

plag_two_gr_kln = arctic.transpose(auth_two_ein_zw, -17)
plag_two_kln_eing = arctic.transpose(auth_two_ein_zw, -5)
plag_two_ein_zw = arctic.transpose(auth_two_ein_zw, 7)
plag_two_zw_dr = arctic.transpose(auth_two_ein_zw, 19)

# ----- Diads

plag_two_diads_gr_kln = arctic.make_diads(plag_two_gr_kln, interval_doubling='d5')
plag_two_diads_kln_eing = arctic.make_diads(plag_two_kln_eing, interval_doubling='d5')

plag_two_fifths_gr_kln = [plag_two_diads_gr_kln[0][2], plag_two_diads_gr_kln[0][3]]
plag_two_fifths_kln_eing = [plag_two_diads_kln_eing[0][2], plag_two_diads_kln_eing[0][3]]

# Sequences 

# ---- Rest Leaves for time signature changes

astring = r"\time 5/8 r4 r4."
empty_58_measure = abjad.Container(astring)

bstring = r"\time 4/4 r1"
empty_44_measure = abjad.Container(bstring)

m_seq_a = (0, 1, 2, 3)
seq_one = (1, 0, 3, 2)
seq_two = (3, 2, 0, 1)
seq_three = (2, 0, 1, 3)

#--------------/
#   Violin    /
#____________/

# Melody One 

mel_one_a = arctic.melody_lookup['bfm'][4]
mel_one_b = arctic.melody_lookup['bfm'][5]

mel_one_a_oct_down = transpose_segment(mel_one_a, -12)
mel_one_a_oct_up = transpose_segment(mel_one_a, 12)

mel_one_a_arp = LegatoArpeggio(mel_one_a, m_seq_a)
mel_one_a_arp_oct_up = LegatoArpeggio(mel_one_a_oct_up, m_seq_a)
mel_one_a_arp_oct_down = LegatoArpeggio(mel_one_a_oct_down, m_seq_a)

melody_one_a = mel_one_a_arp.pitches
melody_one_a_oct_up = mel_one_a_arp_oct_up.pitches
melody_one_a_oct_down = mel_one_a_arp_oct_down.pitches

# Violin Arpeggio One

rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = 'Violin'

plag_one_eingestr = plag_one_ein_zw[0].segment
vln_arp_one = LegatoArpeggio(plag_one_eingestr, seq_one)
violin_arp_one = vln_arp_one.pitches

# Violin Arpeggio Two

auth_one_c = auth_one_ein_zw[2].segment
tr_arp_one = LegatoArpeggio(auth_one_c, seq_one)
violin_arp_two = tr_arp_one.pitches 

auth_one_d = auth_one_ein_zw[3].segment
tr_arp_two = LegatoArpeggio(auth_one_d, seq_one)
violin_arp_three = tr_arp_two.pitches

auth_two_a = auth_two_zw_dr[0].segment
vln_arp_two = LegatoArpeggio(auth_two_a, seq_three)
violin_arp_four = vln_arp_two.pitches


# Melody Two 

mel_two_a = arctic.melody_lookup['gm'][3]
mel_two_b = arctic.melody_lookup['gm'][4]
mel_two_c = arctic.melody_lookup['gm'][5]

mel_two_a_arp = LegatoArpeggio(mel_two_a, m_seq_a)  
mel_two_b_arp = LegatoArpeggio(mel_two_b, m_seq_a)
mel_two_c_arp = LegatoArpeggio(mel_two_c, m_seq_a)

melody_two_a = mel_two_a_arp.pitches
melody_two_b = mel_two_b_arp.pitches
melody_two_c = mel_two_c_arp.pitches

rhythm_definition.notes = [
        (empty_44_measure),
        ("r2"),
        (violin_arp_one[0], abjad.Duration(1, 2), arctic.tie(), arctic.default_on()),
        (violin_arp_one[0], abjad.Duration(1), arctic.tie()),
        (violin_arp_one[0], abjad.Duration(1, 2)),
        (violin_arp_one[1], abjad.Duration(1, 2), arctic.tie()),
        #------------Bar 5
        (violin_arp_one[1], abjad.Duration(1), arctic.tie()),
        (violin_arp_one[1], abjad.Duration(1), arctic.tie()),
        (violin_arp_one[1], abjad.Duration(1, 2), arctic.tie()),
        (violin_arp_one[3], abjad.Duration(1, 2), arctic.tie()),
        (violin_arp_one[3], abjad.Duration(1), arctic.tie()),
        #------------Bar 9
        (violin_arp_one[3], abjad.Duration(1, 4)),
        (violin_arp_one[2], abjad.Duration(3, 4), arctic.tie()),
        (violin_arp_one[2], abjad.Duration(1), ),
        ("r1"),
        ("r4"),
        (melody_one_a[0], abjad.Duration(3, 4), arctic.tie()),
        #------------Bar 13
        (melody_one_a[0], abjad.Duration(1, 8)),
        ("r8"),
        (melody_one_a_oct_up[0], abjad.Duration(2, 4)), 
        (melody_one_a[1], abjad.Duration(1,4)), 
        (melody_one_a[3], abjad.Duration(1)), 
        (melody_one_a[2], abjad.Duration(1)), 
        (violin_arp_two[0], abjad.Duration(1, 2), arctic.tie()),
        (violin_arp_two[1], abjad.Duration(1, 2), arctic.tie()),
        #------------Bar 17
        (violin_arp_two[1], abjad.Duration(1, 4), arctic.tie()),
        (violin_arp_two[2], abjad.Duration(3, 4), arctic.tie()),
        (violin_arp_two[3], abjad.Duration(1), arctic.tie()),
        (violin_arp_two[3], abjad.Duration(3, 4), tremolo(32)), 
        ("r4"),
        (violin_arp_three[0], abjad.Duration(1, 2), arctic.tie()),
        (violin_arp_three[1], abjad.Duration(1, 2), arctic.tie()),
        #------------Bar 21
        (violin_arp_three[1], abjad.Duration(1)),
        ("r2"),
        (violin_arp_four[0], abjad.Duration(1, 2), arctic.tie()),
        (violin_arp_four[0], abjad.Duration(1), arctic.tie()),
        (violin_arp_four[0], abjad.Duration(1, 2)),
        (violin_arp_four[1], abjad.Duration(1, 2), arctic.tie()),
        #------------Bar 25
        (violin_arp_four[1], abjad.Duration(1), arctic.tie()),
        (violin_arp_four[1], abjad.Duration(1), arctic.tie()),
        (violin_arp_four[1], abjad.Duration(1, 2), arctic.tie()),
        (violin_arp_four[3], abjad.Duration(1, 2), arctic.tie()),
        (violin_arp_four[3], abjad.Duration(1), arctic.tie()),
        #------------Bar 29
        (violin_arp_four[3], abjad.Duration(1, 4)),
        (violin_arp_four[2], abjad.Duration(3, 4), arctic.tie()),
        (violin_arp_four[2], abjad.Duration(1)),
        ("r1"),
        ("r1"),
        #-----------Bar 33
        ("r1"),
        ("r4"),
        (melody_two_a[2], abjad.Duration(1,4), tenuto()),
        (melody_two_a[2], abjad.Duration(2,4)), 
        (melody_two_b[3], abjad.Duration(1,4), tenuto()),
        (melody_two_b[3], abjad.Duration(1,4)), 
        (melody_two_b[3], abjad.Duration(2,4)), 
        (melody_two_a[2], abjad.Duration(1,4), tenuto()),
        (melody_two_a[2], abjad.Duration(2,4)), 
        (melody_two_c[0], abjad.Duration(1,4), tenuto()),
        #-----------Bar 37
        (melody_two_c[0], abjad.Duration(1,4)), 
        (melody_two_c[0], abjad.Duration(2,4)), 
        (melody_two_a[2], abjad.Duration(1,4), tenuto()),
        (melody_two_a[2], abjad.Duration(2,4)), 
        (melody_two_b[3], abjad.Duration(1,4), tenuto()),
        (melody_two_b[3], abjad.Duration(1,4)), 
        (melody_two_b[3], abjad.Duration(2,4)), 
        (melody_two_a[0], abjad.Duration(1,4), tenuto()),
        (melody_two_a[0], abjad.Duration(2,4)), 
        (melody_two_c[0], abjad.Duration(1,4), tenuto()),
        (melody_two_c[0], abjad.Duration(1,4)),
        (melody_two_c[0], abjad.Duration(1,4), arctic.tie()),
        #-----------Bar 41
        (melody_two_c[0], abjad.Duration(1,4)),
        (melody_two_a[2], abjad.Duration(1,4), tenuto()),
        (melody_two_a[2], abjad.Duration(2,4), arctic.tie()), 
        (melody_two_a[2], abjad.Duration(1), arctic.tie()), 
        (melody_two_a[2], abjad.Duration(1), arctic.tie()),
        (melody_two_a[2], abjad.Duration(1), barline("||")),
        ]


rhythm_definition.dynamics = [
        (2, abjad.Dynamic('ppp'), 2.5),
        (3, '<'),
        (5, abjad.Dynamic('p'), 2.5),
        (10, '>'),
        (13, abjad.Dynamic('ppp')),
        (16, abjad.Dynamic('pp')),
        (25, '>'),
        (28, abjad.Dynamic('ppp')),
        (33, abjad.Dynamic('niente'), 2.5),
        (34, '<'),
        (36, abjad.Dynamic('pp')),
        (43, '>'),
        (46, abjad.Dynamic('niente')),
        (50, abjad.Dynamic('pp')),
        (72, '>'),
        (75, abjad.Dynamic('niente')),
       ]

rhythm_definition.markup = [
        (2, arctic.markup.pont(), 1.5),
        (5, arctic.markup.ord(), 1.5),
        (12, arctic.markup.pont(), 3.5), 
        (16, arctic.markup.ord(), 1.5),
        (28, arctic.markup.flaut_pont(), 3.5),
        (30, arctic.markup.ord(), 2.5),
        (36, arctic.markup.flaut(), 3.5),
        (50, arctic.markup.ord(), 3.5),
        (72, arctic.markup.flaut(), 1.5),
        ]

#-----------------/
#   MonoSynth    /
#_______________/

rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = 'Monosynth'

auth_one_c = auth_one_kln_eing[2].segment
tr_arp_one = LegatoArpeggio(auth_one_c, seq_one)
monosynth_arp_one = tr_arp_one.stages 

auth_one_d = auth_one_kln_eing[3].segment
tr_arp_two = LegatoArpeggio(auth_one_d, seq_one)
monosynth_arp_two = tr_arp_two.stages 

diad_a = Diad(plag_two_fifths_gr_kln[1])
diad_one = diad_a.pitch_string

diad_b = Diad(plag_two_fifths_kln_eing[0])
diad_two = diad_b.pitch_string

rhythm_definition.notes = [
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        #------------Bar 5
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        #------------Bar 9
        ("r1"),
        ("r1"),
        ("r1"),
        ("r4"),
        (melody_one_a_oct_down[0], abjad.Duration(3, 4), arctic.tie(), clef('bass')),
        #------------Bar 13
        (melody_one_a_oct_down[0], abjad.Duration(1, 8)),
        ("r8"),
        (melody_one_a[0], abjad.Duration(2, 4)), 
        (melody_one_a_oct_down[1], abjad.Duration(1,4)), 
        (melody_one_a_oct_down[3], abjad.Duration(1)), 
        (melody_one_a_oct_down[2], abjad.Duration(1), tremolo(32), clef('treble')), 
        (monosynth_arp_one[0], abjad.Duration(1, 2), tremolo(32), arctic.tie()),
        (monosynth_arp_one[1], abjad.Duration(1, 2), tremolo(32), arctic.tie()),
        #------------Bar 17
        (monosynth_arp_one[1], abjad.Duration(1, 4), tremolo(32), arctic.tie()),
        (monosynth_arp_one[2], abjad.Duration(3, 4), tremolo(32), arctic.tie()),
        (monosynth_arp_one[3], abjad.Duration(1), tremolo(32), arctic.tie()),
        (monosynth_arp_one[3], abjad.Duration(3, 4), tremolo(32)), 
        ("r4"),
        (monosynth_arp_two[0], abjad.Duration(1, 2), tremolo(32), arctic.tie()),
        (monosynth_arp_two[1], abjad.Duration(1, 2), tremolo(32), arctic.tie()),
        #------------Bar 21
        (monosynth_arp_two[1], abjad.Duration(1, 4), tremolo(32), arctic.tie()),
        (monosynth_arp_two[2], abjad.Duration(3, 4), tremolo(32), arctic.tie()),
        (monosynth_arp_two[3], abjad.Duration(1), tremolo(32), arctic.tie()),
        (monosynth_arp_two[3], abjad.Duration(3, 4), tremolo(32)), 
        ("r4"),
        ("r1"),
        #-----------Bar 25
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        #-----------Bar 29
        ("r1"),
        (diad_one, abjad.Duration(1), tremolo(32), arctic.tie(), clef('bass')),
        (diad_one, abjad.Duration(1), tremolo(32), arctic.tie()),
        (diad_one, abjad.Duration(1), tremolo(32), arctic.tie()),
        #-----------Bar 33
        (diad_one, abjad.Duration(1), tremolo(32), arctic.tie()),
        (diad_one, abjad.Duration(1), tremolo(32)),
        ("r1"),
        ("r1"),
        #-----------Bar 37
        (diad_two, abjad.Duration(1), tremolo(32), arctic.tie()),
        (diad_two, abjad.Duration(1), tremolo(32), arctic.tie()),
        (diad_two, abjad.Duration(1), tremolo(32), arctic.tie()),
        (diad_two, abjad.Duration(1), tremolo(32), arctic.tie()),
        #-----------Bar 41
        (diad_two, abjad.Duration(1), tremolo(32)),
        ("r1"),
        ("r1"),
        ("r1"),
        ]

rhythm_definition.dynamics = [
        (12, abjad.Dynamic('ppp')),
        (18, '>'),
        (20, '<'),
        (23, '>'),
        (24, abjad.Dynamic('ppp')),
        (26, '<'),
        (29, '>'),
        (31, abjad.Dynamic('niente')),
        (39, abjad.Dynamic('niente')),
        (40, '<'),
        (42, '>'),
        (44, abjad.Dynamic('niente')),
        (46, abjad.Dynamic('niente')),
        (47, '<'),
        (49, '>', 3.5),
        (51, abjad.Dynamic('niente')),
       ]

rhythm_definition.markup = [
        (18, arctic.markup.mx(), 1.5),
        ]


#-------------------PolySynth----------------#

#--------------/
# RH_I  /
#____________/

rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = 'RH_I'

plag_one_a = plag_one_ein_zw[0].segment
plag_one_arp = LegatoArpeggio(plag_one_a, seq_one)
rh_arp_one = plag_one_arp.stages

plag_one_b = plag_one_zw_dr[1].segment
plag_one_b_arp = LegatoArpeggio(plag_one_b, seq_two)
rh_arp_two = plag_one_b_arp.stages

rhythm_definition.notes = [
        ("r1"),
        ("r2"),
        (rh_arp_one[0], abjad.Duration(1, 2), arctic.tie()),
        (rh_arp_one[1], abjad.Duration(3, 4), arctic.tie()),
        (rh_arp_one[2], abjad.Duration(1, 4), arctic.tie()),
        (rh_arp_one[2], abjad.Duration(2, 4), arctic.tie()),
        (rh_arp_one[3], abjad.Duration(2, 4), arctic.tie()),
        (rh_arp_one[3], abjad.Duration(1), arctic.tie()), 
        # ------------------------------------------ Bar 6
        (rh_arp_two[2], abjad.Duration(1), arctic.tie()),
        (rh_arp_two[2], abjad.Duration(1,2), arctic.tie()),
        (rh_arp_two[3], abjad.Duration(1,2), arctic.tie()),
        (rh_arp_two[3], abjad.Duration(1), arctic.tie()),
        #------------Bar 9
        (rh_arp_two[3], abjad.Duration(1, 4), arctic.tie()),
        (rh_arp_two[1], abjad.Duration(3, 4), arctic.tie()),
        (rh_arp_two[0], abjad.Duration(1), arctic.tie()),
        (rh_arp_two[0], abjad.Duration(1), arctic.tie()),
        (rh_arp_two[0], abjad.Duration(1)),
        #------------Bar 13
        ("r4"),
        (melody_one_a_oct_up[0], abjad.Duration(2, 4)), 
        (melody_one_a[1], abjad.Duration(1,4)), 
        (melody_one_a[3], abjad.Duration(1)), 
        (melody_one_a[2], abjad.Duration(1)), 
        (violin_arp_two[0], abjad.Duration(1, 2), arctic.tie()),
        (violin_arp_two[1], abjad.Duration(1, 2), arctic.tie()),
        #------------Bar 17
        (violin_arp_two[1], abjad.Duration(1, 4), arctic.tie()),
        (violin_arp_two[2], abjad.Duration(3, 4), arctic.tie()),
        (violin_arp_two[3], abjad.Duration(1), arctic.tie()),
        ("r1"),
        ("r1"),
        #------------Bar 21
        ("r1"),
        ("r1"),
        ("r1"),
        (violin_arp_four[0], abjad.Duration(1, 2)),
        (violin_arp_four[1], abjad.Duration(1, 2), arctic.tie()),
        #------------Bar 25
        (violin_arp_four[1], abjad.Duration(1), arctic.tie()),
        (violin_arp_four[1], abjad.Duration(1), arctic.tie()),
        (violin_arp_four[1], abjad.Duration(1, 2), arctic.tie()),
        (violin_arp_four[3], abjad.Duration(1, 2), arctic.tie()),
        (violin_arp_four[3], abjad.Duration(1), arctic.tie()),
        #------------Bar 29
        (violin_arp_four[3], abjad.Duration(1, 4)),
        (violin_arp_four[2], abjad.Duration(3, 4), arctic.tie()),
        (violin_arp_four[2], abjad.Duration(1)),
        ("r1"),
        ("r1"),
        #-----------Bar 33
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        #-----------Bar 37
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        #-----------Bar 41
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        ]


rhythm_definition.dynamics = [ 
                    (0, abjad.Dynamic('ppp'), 2.5)
                       ]

rhythm_definition.markup = []


#--------------/
# LH_I  /
#____________/

rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = 'LH_I'

auth_one_a = auth_one_kln_eing[0].segment
auth_one_a_arp= LegatoArpeggio(auth_one_a, seq_one)
lh_arp_one = auth_one_a_arp.stages

plag_two_a = plag_two_gr_kln[0].segment
plag_two_a_arp = LegatoArpeggio(plag_two_a, seq_three)
lh_arp_two = plag_two_a_arp.stages

plag_two_b = plag_two_gr_kln[1].segment
plag_two_b_arp = LegatoArpeggio(plag_two_b, seq_three)
lh_arp_three = plag_two_b_arp.stages


rhythm_definition.notes = [
        (lh_arp_one[0], abjad.Duration(1, 2), arctic.tie()),
        (lh_arp_one[1], abjad.Duration(1, 2), arctic.tie()),
        (lh_arp_one[1], abjad.Duration(1, 4), arctic.tie()),
        (lh_arp_one[2], abjad.Duration(3, 4), arctic.tie()),
        (lh_arp_one[3], abjad.Duration(1), arctic.tie()),
        (lh_arp_one[3], abjad.Duration(3, 4)), 
        ("r4"),
        # ------------------------------------------ Bar 5
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        #------------Bar 9
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        #------------Bar 13
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        #------------Bar 17
        ("r1"),
        ("r1"),
        ("r1"),       
        ("r1"),
        #------------Bar 21
        ("r1"),
        ("r2"),
        (lh_arp_two[0], abjad.Duration(1, 2), arctic.tie()),
        (lh_arp_two[1], abjad.Duration(3, 4), arctic.tie()),
        (lh_arp_two[2], abjad.Duration(1, 4), arctic.tie()),
        (lh_arp_two[2], abjad.Duration(2, 4), arctic.tie()),
        (lh_arp_two[3], abjad.Duration(2, 4), arctic.tie()),
        #------------ Bar 25
        (lh_arp_two[3], abjad.Duration(1), arctic.tie()), 
        (lh_arp_three[3], abjad.Duration(1), arctic.tie()),
        (lh_arp_three[3], abjad.Duration(1,2), arctic.tie()),
        (lh_arp_three[2], abjad.Duration(1,2), arctic.tie()),
        (lh_arp_three[2], abjad.Duration(1), arctic.tie()),
        #------------Bar 29
        (lh_arp_three[2], abjad.Duration(1, 4), arctic.tie()),
        (lh_arp_three[1], abjad.Duration(3, 4), arctic.tie()),
        (lh_arp_three[0], abjad.Duration(1)),
        ("r1"),  
        ("r1"),
        #-----------Bar 33
        (diad_one, abjad.Duration(1), arctic.tie()),
        (diad_one, abjad.Duration(1), arctic.tie()),
        (diad_one, abjad.Duration(1), arctic.tie()),
        (diad_one, abjad.Duration(1), arctic.tie()),
        #-----------Bar 37
        (diad_one, abjad.Duration(1)),
        ("r1"),
        ("r1"),
        (diad_two, abjad.Duration(1), arctic.tie()),
        #-----------Bar 41
        (diad_two, abjad.Duration(1), arctic.tie()),
        (diad_two, abjad.Duration(1), arctic.tie()), 
        (diad_two, abjad.Duration(1), arctic.tie()),
        (diad_two, abjad.Duration(1), barline("||")),
        ]


rhythm_definition.dynamics = [
        (47, abjad.Dynamic('pp')),
        (48, '>'),
        (51, abjad.Dynamic('niente')),
        ]

rhythm_definition.markup = []

# ------------ run and build segment
lilypond_file = segment_maker.run()

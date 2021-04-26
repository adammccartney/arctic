import distutils.version
import platform

if not (
    distutils.version.LooseVersion("3.7")
    < distutils.version.LooseVersion(platform.python_version())
):
    raise ImportError("Requires Python 3.7.")
del distutils
del platform

from arctic.tools import *
from arctic.tools import MarkupLibrary as markup
from arctic.materials.instruments.definition import instruments
from arctic.materials.pitch.definition import (
                                    bass_pitches, 
                                    tetrads,
                                    pentads,
                                    transposition_lookup,
                                    scale_lookup,
                                    melody_lookup,
                                    vln_str_diads,
                                    vln_scnd_flgs,
                                    pure_fifth_diads,
                                    pure_maj_third_diads,
                                   )
from arctic.materials.metronome_marks.definition import  metronome_marks
from arctic import segments

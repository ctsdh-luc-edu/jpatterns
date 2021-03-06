import sys
from abjad import *

import common, sideman

# This is a 5/4 pattern!

def get_pattern_n19(jazz_scale):
    pitches = jazz_scale.get_named_pitches([1, 3, 5, 7, 7])
    durations = [sideman.eighth] * 4 + [sideman.quarter] * 1
    notes = scoretools.make_notes(pitches, durations[0:5])
    rest = Rest(sideman.quarter)
    measure = Measure((4, 4))
    for note in notes: 
        measure.append(note)
    measure.append(rest)
    tie = spannertools.Tie()
    attach(tie, measure[3:5])
    return measure

def get_pattern_n19_chord_measure(jazz_scale):
    pitches = jazz_scale.get_chord_as_named([1 ,3, 5, 7])
    measure = Measure((4, 4))
    chord = Chord(pitches, (4, 4))
    measure.append(chord)
    multiplier = Multiplier(measure.time_signature.duration)
    attach(multiplier, chord)
    return measure

def get_score():
    treble_pattern = Staff()
    chords = Staff(context_name='ChordNames')

    for key in sideman.keys_in_order():
        jazz_scale = sideman.JazzScale(key)
        treble_pattern.append( get_pattern_n19(jazz_scale) )
        chords.append( get_pattern_n19_chord_measure(jazz_scale) )

    score = Score([chords, treble_pattern])
    tempo = Tempo(Duration(1, 4), (80, 132))
    attach(tempo, treble_pattern)
    return score

def title():
    return "Jazz Pattern 19"

def composer():
    return "Jerry Greene et al, Thiruvathukal"

def pdf():
    return "jazz019.pdf"

def midi():
    return "jazz019.midi"


if __name__ == '__main__':
    score = get_score()
    common.main( score, title(), composer(), pdf())
    common.main( score, title(), composer(), midi())

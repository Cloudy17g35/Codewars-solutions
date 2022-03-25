import re
def major_scale(melody):
    all_notes = 'C, C#, D, D#, E, F, F#, G, G#, A, A#, B'.split(', ')
    
    regex = re.findall('[A-Z]#?',melody)
    melody = set(regex)
    all_the_keys = {}
    
    for _ in range(len(all_notes)):
        key = all_notes[0]
        
        scale = set([all_notes[0], all_notes[2] , all_notes[4], 
                 all_notes[5], all_notes[7], all_notes[9], all_notes[11]])
        all_the_keys[key] = scale
        current_scale = all_notes[1:] + [key]
        all_notes = current_scale
    
    for key in all_the_keys:
        if len(all_the_keys[key]) == len(melody) and not all_the_keys[key] - melody:
            return f'{key} major scale'
    return 'No major scale'

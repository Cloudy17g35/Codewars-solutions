def format_playlist(songs):
    if not songs:

        return '''+------+------+--------+\n| Name | Time | Artist |\n+------+------+--------+'''

    else:

        songs = sorted(songs, key= lambda x: (x[2], x[0]))
        maximal_title_length = len(max(songs, key=lambda x: len(x[0]))[0]) + 1
        maximal_artist_length = len(max(songs, key=lambda x: len(x[2]))[2]) + 1

        frame = f"+{'-' * (maximal_title_length + 1) }+{len(' Time ') * '-'}+{(maximal_artist_length + 1) * '-'}+"
        head = f"|{' ' + 'Name' + (maximal_title_length - len('Name')) * ' '}" \
               f"| Time |" \
               f"{' ' + 'Artist' + (maximal_artist_length - len('Artist')) * ' '}|"

        result = f'{frame}\n' \
                 f'{head}\n' \
                 f"{frame}\n"

        for song in songs:
            title, time, artist = song[0], song[1], song[2]

            result += f"|{' ' + title + (maximal_title_length - len(title)) * ' '}" \
                      f"| {time} |" \
                      f"{' ' + artist + (maximal_artist_length - len(artist)) * ' '}|\n"

    return result + frame

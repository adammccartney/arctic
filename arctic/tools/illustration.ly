\version "2.20.0"                                                              %! abjad.LilyPondFile._get_format_pieces()
\language "english"                                                            %! abjad.LilyPondFile._get_format_pieces()

#(ly:set-option 'relative-includes #t)

\include "/home/adam/scores/arctic/arctic/stylesheets/contexts.ily"                %! abjad.LilyPondFile._get_formatted_includes()

\header {                                                                      %! abjad.LilyPondFile._get_formatted_blocks()
    title = ##f
    composer = ##f
}                                                                              %! abjad.LilyPondFile._get_formatted_blocks()

\score {                                                                       %! abjad.LilyPondFile._get_formatted_blocks()
    \context Score = "Score"                                                   %! arctic.ScoreTemplate.__call__()
    <<                                                                         %! arctic.ScoreTemplate.__call__()
        \context GlobalContext = "Global_Context"                              %! abjad.ScoreTemplate._make_global_context()
        <<                                                                     %! abjad.ScoreTemplate._make_global_context()
            \context GlobalRests = "Global_Rests"                              %! abjad.ScoreTemplate._make_global_context()
            {                                                                  %! abjad.ScoreTemplate._make_global_context()
            }                                                                  %! abjad.ScoreTemplate._make_global_context()
            \context GlobalSkips = "Global_Skips"                              %! abjad.ScoreTemplate._make_global_context()
            {                                                                  %! abjad.ScoreTemplate._make_global_context()
            }                                                                  %! abjad.ScoreTemplate._make_global_context()
        >>                                                                     %! abjad.ScoreTemplate._make_global_context()
        \context MusicContext = "Music_Context"                                %! arctic.ScoreTemplate.__call__()
        <<                                                                     %! arctic.ScoreTemplate.__call__()
            \context Staff = "Violin"                                          %! arctic.ScoreTemplate.__call__()
            <<                                                                 %! arctic.ScoreTemplate.__call__()
                \context Voice = "Violin_Music_Voice"                          %! arctic.ScoreTemplate.__call__()
                {                                                              %! arctic.ScoreTemplate.__call__()
                    s1 * 20
                }                                                              %! arctic.ScoreTemplate.__call__()
            >>                                                                 %! arctic.ScoreTemplate.__call__()
            \context Staff = "Monosynth"                                       %! arctic.ScoreTemplate.__call__()
            <<                                                                 %! arctic.ScoreTemplate.__call__()
                \context Voice = "Monosynth_Music_Voice"                       %! arctic.ScoreTemplate.__call__()
                {                                                              %! arctic.ScoreTemplate.__call__()
                }                                                              %! arctic.ScoreTemplate.__call__()
            >>                                                                 %! arctic.ScoreTemplate.__call__()
            \context MusicContext = "Polysynth_Music_Context"                  %! arctic.ScoreTemplate.__call__()
            {                                                                  %! arctic.ScoreTemplate.__call__()
                \context PolySynthMusicStaffGroup = "PolySynth_Music_Staff_Group" %! arctic.ScoreTemplate.__call__()
                <<                                                             %! arctic.ScoreTemplate.__call__()
                    \context Staff = "RH_Polysynth"                            %! arctic.ScoreTemplate.__call__()
                    <<                                                         %! arctic.ScoreTemplate.__call__()
                        \context Voice = "RH_I_Music_Voice"                    %! arctic.ScoreTemplate.__call__()
                        {                                                      %! arctic.ScoreTemplate.__call__()
                            \context Voice = "z"
                            {
                                r1
                                r2
                            }
                            \context Voice = "a"
                            {
                                <g' bf'>2
                                <fs' d''>2.
                                <f'' gf''>2.
                                <af' g''>1.
                                r2
                            }
                            \context Voice = "b"
                            {
                                <fs' d''>2
                                <f'' gf''>2.
                                <af' g''>2.
                                <g'' bf''>1.
                                r2
                            }
                            \context Voice = "c"
                            {
                                <f'' gf''>2
                                <af' g''>2.
                                <g'' bf''>2.
                                <fs'' d'''>1.
                                r2
                            }
                            \context Voice = "y"
                            {
                                r2
                                r1
                                r1
                            }
                        }                                                      %! arctic.ScoreTemplate.__call__()
                    >>                                                         %! arctic.ScoreTemplate.__call__()
                    \context Staff = "LH_Polysynth"                            %! arctic.ScoreTemplate.__call__()
                    <<                                                         %! arctic.ScoreTemplate.__call__()
                        \context Voice = "LH_I_Music_Voice"                    %! arctic.ScoreTemplate.__call__()
                        {                                                      %! arctic.ScoreTemplate.__call__()
                            \context Voice = "a"
                            {
                                <af ef'>2
                                <af g'>2.
                                <g' bf'>2.
                                <g' c''>1.
                                r2
                            }
                            \context Voice = "b"
                            {
                                <af g'>2
                                <g' bf'>2.
                                <g' c''>2.
                                <af' ef''>1.
                                r2
                            }
                            \context Voice = "c"
                            {
                                <g' bf'>2
                                <g' c''>2.
                                <af' ef''>2.
                                <af' g''>1.
                                r2
                            }
                            \context Voice = "d"
                            {
                                <g' c''>2
                                <af' ef''>2.
                                <af' g''>2.
                                <g'' bf''>1.
                                r2
                            }
                        }                                                      %! arctic.ScoreTemplate.__call__()
                    >>                                                         %! arctic.ScoreTemplate.__call__()
                >>                                                             %! arctic.ScoreTemplate.__call__()
            }                                                                  %! arctic.ScoreTemplate.__call__()
        >>                                                                     %! arctic.ScoreTemplate.__call__()
    >>                                                                         %! arctic.ScoreTemplate.__call__()
}                                                                              %! abjad.LilyPondFile._get_formatted_blocks()
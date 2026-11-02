Data Dictionary
Source
API Name: OpenDota

Base URL: https://api.opendota.com/api

Documentation: https://docs.opendota.com/

Authentication: No API key required for low-volume usage.

Resource Type: Public Match
One record represents one Dota 2 match that has been recorded by OpenDota.

Important Fields
Field	Type	Example	Meaning
match_id	Integer	9072502272	Unique match identifier
match_seq_num	Integer	7618576717	Sequence number
radiant_win	Boolean	false	Whether Radiant team won
start_time	Integer	1793578615	Match start timestamp
duration	Integer	3600	Match duration in seconds
lobby_type	Integer	14	Type of lobby
game_mode	Integer	13	Game mode
avg_rank_tier	Integer	23	Average player rank
num_rank_tier	Integer	1	Number of ranked participants
Identifiers
Primary Key:

match_id
Relationships
Each match contains information about players, teams, ranks, and outcomes.

Update Behavior
New matches are constantly added throughout the day. Historical matches normally do not change after completion.

Surprises
Some fields may be null.
Match durations vary greatly.
Rank information is not always available.
Ethics Check
The data is publicly available gameplay data.

No personally sensitive information is stored.

The worst realistic harm would be misuse of gameplay statistics or player rankings.

Only authorized users of the application should be allowed to modify stored records.

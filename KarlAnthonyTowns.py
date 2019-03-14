from ohmysportsfeedspy import MySportsFeeds

Data_query = MySportsFeeds('2.0', verbose=True)
Data_query.authenticate('7a623d32-510c-4ccf-8a7b-8a3af9', 'MYSPORTSFEEDS')

Output = Data_query.msf_get_data(league='nba',
                                 season='2018-2019-regular',
                                 feed='seasonal_player_gamelogs',
                                 player='karlanthony-towns',
                                 format='json',
                                 force='true')

print(Output)
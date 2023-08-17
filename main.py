from libraries.navigators import FlashscoreNavigator

league = "Premier League"

navi = FlashscoreNavigator()
navi.choose_league(league_name=league)
navi.select_table()
table = navi.get_table()
df = navi.port_table_to_pandas()
df.to_excel("./tables/"+league+"_table.xlsx")

navi.go_to_matches()
next_round = navi.get_next_round()


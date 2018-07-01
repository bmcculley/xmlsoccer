from xmlsoccer import xmlsoccer

xmls = xmlsoccer.XmlSoccer(api_key=YOUR_API_KEY, 
            use_demo=True)

fixtures = xmls.call_api(method='GetHistoricMatchesByLeagueAndSeason',
                        seasonDateString='1314',
                        league='Scottish Premier League')
                        
teams = xmls.call_api(method='GetAllTeams')

leagues = xmls.call_api(method='GetAllLeagues')

standings = xmlsoccer.call_api(method='GetLeagueStandingsBySeason',
                               seasonDateString='1314',
                               league='Scottish Premier League')
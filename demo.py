from xmlsoccer import XmlSoccer

xmls = XmlSoccer(api_key=YOUR_API_KEY, 
            use_demo=True)

fixtures = xmls.call_api(method='GetHistoricMatchesByLeagueAndSeason',
                        seasonDateString='1314',
                        league='Scottish Premier League')
                        
print(fixtures)
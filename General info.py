import requests

# https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/Leocardia?api_key=RGAPI-d8f9e95d-c12b-4077-aa2a-b6d1b4cb7936

def requestSummonerData(region, summonerName, APIKey):
    URL = "https://" + region + "1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName + "?api_key=" + APIKey
    print("\n" + URL)

    response = requests.get(URL)
    return response.json()

# https://na1.api.riotgames.com/lol/champion-mastery/v4/scores/by-summoner/nErleQ0V-wmsLO5QYM8ka2IOxeAd-LXJuQ8XaYpSH41TDIE?api_key=RGAPI-d8f9e95d-c12b-4077-aa2a-b6d1b4cb7936
def requestSummonerTotalMasteryScore(region, id, APIKey):
    URL = "https://" + region + "1.api.riotgames.com/lol/champion-mastery/v4/scores/by-summoner/" + id + "?api_key=" + APIKey
    print("\n" + URL)

    response = requests.get(URL)
    return response.json()

# https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/kUzOKgr27fmibZcbQvG_tQ3F2zDIguMYTr-rUH01VHghV1rM?api_key=RGAPI-d8f9e95d-c12b-4077-aa2a-b6d1b4cb7936
def requestsSummonerRankInfo(region, id, APIKey):
    URL = "https://" + region + "1.api.riotgames.com/lol/league/v4/entries/by-summoner/" + id + "?api_key=" + APIKey
    print("\n" + URL)

    response = requests.get(URL)
    return response.json()

def main():
    region = "NA"
    summonerName = (str)(input("Type in your summoner Name without any space: "))
    APIKey = "RGAPI-d8f9e95d-c12b-4077-aa2a-b6d1b4cb7936"
    
    ################################################################################

    SummonerData = requestSummonerData(region, summonerName, APIKey)
    id = SummonerData['id']
    id = (str)(id)
    print("\nyour id is: " + id)

    accountId = SummonerData['accountId']
    accountId = (str)(accountId)
    print("\nyour account id is: " + accountId)
    
    puuid = SummonerData['puuid']
    puuid = (str)(puuid)
    print("\nyour puuid is: " + puuid)
    
    profileIconId = SummonerData['profileIconId']
    profileIconId = (str)(profileIconId)
    print("\nyour profileIconId is: " + profileIconId)

    revisionDate = SummonerData['revisionDate']
    revisionDate = (str)(revisionDate)
    print("\nyour revisionDate is: " + revisionDate)

    summonerLevel = SummonerData['summonerLevel']
    summonerLevel = (str)(summonerLevel)
    print("\nyour summonerLevel is: " + summonerLevel)
    
    ################################################################################

    SummonerTotalMasteryScore = requestSummonerTotalMasteryScore(region, id, APIKey)
    masteryScore = (int)(SummonerTotalMasteryScore)
    print("your total mastery score is: ", masteryScore)
    
    ################################################################################

    SummonerRankInfo = requestsSummonerRankInfo(region, id, APIKey)
    queueType = SummonerRankInfo[0]['queueType']
    queueType = (str)(queueType)

    if queueType == "RANKED_FLEX_SR":
        try:
            rank_solo_leagueId = SummonerRankInfo[1]['leagueId']
            rank_solo_leagueId = (str)(rank_solo_leagueId)
            print("\nyour solo league id is: " + rank_solo_leagueId)
            solo_leagueId = SummonerRankInfo[1]['leagueId']
            solo_leagueId = (str)(solo_leagueId)
            rank_solo_tier =  SummonerRankInfo[1]['tier']
            rank_solo_tier = (str)(rank_solo_tier)
            rank_solo_rank =  SummonerRankInfo[1]['rank']
            rank_solo_rank = (str)(rank_solo_rank)
            solo_leaguePoints = SummonerRankInfo[1]['leaguePoints']
            solo_leaguePoints = (int)(solo_leaguePoints)
            solo_wins = SummonerRankInfo[1]['wins']
            solo_wins = (int)(solo_wins)
            solo_losses = SummonerRankInfo[1]['losses']
            solo_losses = (int)(solo_losses)
            solo_win_rate = ((solo_wins) / (solo_wins + solo_losses)) * 100
            print("your Rank level in Solo mode is: " + rank_solo_tier + " " + rank_solo_rank, solo_leaguePoints, "points\n")
            print("In total you play", solo_wins+solo_losses, "rank solo games\n" + "you win", solo_wins,"games, " + "you loss", solo_losses,"games" + "\nyour solo win rate is: ", round(solo_win_rate, 3), "%")
        except IndexError:
            print("\n*** " + summonerName + " did not start playing Rank Solo mode ***")       

        rank_flex_leagueId = SummonerRankInfo[0]['leagueId']
        rank_flex_leagueId = (str)(rank_flex_leagueId)
        print("\nyour flex league id is: " + rank_flex_leagueId)
        rank_flex_tier =  SummonerRankInfo[0]['tier']
        rank_flex_tier = (str)(rank_flex_tier)
        rank_flex_rank =  SummonerRankInfo[0]['rank']
        rank_flex_rank = (str)(rank_flex_rank)
        flex_leaguePoints = SummonerRankInfo[0]['leaguePoints']
        flex_leaguePoints = (int)(flex_leaguePoints)
        flex_wins = SummonerRankInfo[0]['wins']
        flex_wins = (int)(flex_wins)
        flex_losses = SummonerRankInfo[0]['losses']
        flex_losses = (int)(flex_losses)
        flex_win_rate = ((flex_wins) / (flex_wins + flex_losses)) * 100
        print("your Rank level in Flex mode is: " + rank_flex_tier + " " + rank_flex_rank, flex_leaguePoints, "points\n")    
        print("In total you play", flex_wins+flex_losses,"rank flex games\n" + "you win", flex_wins,"games, " + "you loss", flex_losses,"games" + "\nyour flex win rate is: ", round(flex_win_rate, 3), "%")
        
    elif queueType == "RANKED_SOLO_5x5":
        rank_solo_leagueId = SummonerRankInfo[0]['leagueId']
        rank_solo_leagueId = (str)(rank_solo_leagueId)
        print("\nyour solo league id is: " + rank_solo_leagueId)
        solo_leagueId = SummonerRankInfo[0]['leagueId']
        solo_leagueId = (str)(solo_leagueId)
        rank_solo_tier =  SummonerRankInfo[0]['tier']
        rank_solo_tier = (str)(rank_solo_tier)
        rank_solo_rank =  SummonerRankInfo[0]['rank']
        rank_solo_rank = (str)(rank_solo_rank)
        solo_leaguePoints = SummonerRankInfo[0]['leaguePoints']
        solo_leaguePoints = (int)(solo_leaguePoints)
        solo_wins = SummonerRankInfo[0]['wins']
        solo_wins = (int)(solo_wins)
        solo_losses = SummonerRankInfo[0]['losses']
        solo_losses = (int)(solo_losses)
        solo_win_rate = ((solo_wins) / (solo_wins + solo_losses)) * 100
        print("your Rank level in Solo mode is: " + rank_solo_tier + " " + rank_solo_rank, solo_leaguePoints, "points\n")
        print("In total you play", solo_wins+solo_losses, "rank solo games\n" + "you win", solo_wins,"games, " + "you loss", solo_losses,"games" + "\nyour solo win rate is: ", round(solo_win_rate, 3), "%")

        try:
            rank_flex_leagueId = SummonerRankInfo[1]['leagueId']
            rank_flex_leagueId = (str)(rank_flex_leagueId)
            print("\nyour flex league id is: " + rank_flex_leagueId)
            rank_flex_tier =  SummonerRankInfo[1]['tier']
            rank_flex_tier = (str)(rank_flex_tier)
            rank_flex_rank =  SummonerRankInfo[1]['rank']
            rank_flex_rank = (str)(rank_flex_rank)
            flex_leaguePoints = SummonerRankInfo[1]['leaguePoints']
            flex_leaguePoints = (int)(flex_leaguePoints)
            flex_wins = SummonerRankInfo[1]['wins']
            flex_wins = (int)(flex_wins)
            flex_losses = SummonerRankInfo[1]['losses']
            flex_losses = (int)(flex_losses)
            flex_win_rate = ((flex_wins) / (flex_wins + flex_losses)) * 100
            print("your Rank level in Flex mode is: " + rank_flex_tier + " " + rank_flex_rank, flex_leaguePoints, "points\n")       
            print("In total you play", flex_wins+flex_losses,"rank flex games\n" + "you win", flex_wins,"games, " + "you loss", flex_losses,"games" + "\nyour flex win rate is: ", round(flex_win_rate, 3), "%")
        except IndexError:
            print("\n*** " + summonerName + " did not start playing Rank Flex mode ***")       
    
if __name__ == "__main__":
    main()
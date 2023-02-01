from project import web, consols , genres , stat , users
import pandas as pd
import mock # type: ignore
import builtins
import math




def test_web():
    df = pd.DataFrame(web("List_of_Xbox_Series_X_and_Series_S_games","Sports"),index=[0])
    hr = pd.DataFrame(web("List_of_Xbox_Series_X_and_Series_S_games","Horror"),index=[0])
    rc = pd.DataFrame(web("List_of_PlayStation_5_games","Racing"),index=[0])
    act = pd.DataFrame(web("List_of_Xbox_Series_X_and_Series_S_games","Action-adventure"),index=[0])

    assert df.loc[:,"Title"][0] in ['AEW Fight Forever', 'Blood Bowl 3', 'Cricket 22', 'eFootball 2022', 'FIFA 21', 'FIFA 22', 'FIFA 23', 'Football Manager 2021', 'Football Manager 2022', 'Madden NFL 21', 'Madden NFL 22', 'Madden NFL 23', 'Matchpoint: Tennis Championships', 'MLB The Show 21', 'MLB The Show 22', 'NBA 2K21', 'NBA 2K22', 'NHL 22', 'OlliOlli World', 'Rugby 22', 'Session', 'Shredders', "Tony Hawk's Pro Skater 1 + 2", 'Ultimate Fishing Simulator 2', 'WWE 2K22'] 
    assert hr.loc[:,"Title"][0] in ['Apsulov: End of Gods', 'Evil Dead: The Game']
    assert rc.loc[:,"Title"][0] in ['Art of Rally', 'Assetto Corsa Competizione', "Can't Drive This", 'Crash Drive 3', 'Dirt 5', 'F1 2021', 'F1 22', 'Grid Legends', 'Hot Wheels Unleashed', 'Monster Energy Supercross: The Official Videogame 4', 'Monster Truck Championship', 'MotoGP 21', 'MXGP 2020', 'MX vs. ATV Legends', 'Need for Speed Unbound', 'Redout 2', 'Ride 4', 'Riders Republic', 'RiMS Racing', 'Street Outlaws 2: Winner Takes All', 'Test Drive Unlimited Solar Crown'] 
    assert act.loc[:,"Title"][0] in ['Aliens', 'Anodyne 2: Return to Dust', 'Avatar: Frontiers of Pandora', "Marvel's Avengers", 'Aztech: Forgotten Gods', 'Clash: Artifacts of Chaos', 'Crimson Desert', 'Deathloop', "Death's Door", 'Destroy All Humans! 2: Reprobed', 'Dustborn', 'Evil West', 'Foreclosed', "Ghost of Tsushima Director's Cut", 'Ghost of Tsushima: Legends', 'Ghostwire: Tokyo', 'Gotham Knights', 'Grand Theft Auto Online', 'Grand Theft Auto: The Trilogy – The Definitive Edition', 'Grand Theft Auto V', 'Grand Theft Auto VI', "Marvel's Guardians of the Galaxy", 'Hell is Us', 'Hood: Outlaws & Legends', 'Immortals Fenyx Rising', 'In Rays of the Light', 'Jett: The Far Shore', 'Judgment', 'Kena: Bridge of Spirits', 'Kingdom of Arcadia', 'The Last of Us Part I', 'Lego Star Wars: The Skywalker Saga', 'Like a Dragon Gaiden: The Man Who Erased His Name', 'Like a Dragon: Ishin!', 'Little Devil Inside', 'The Lord of the Rings: Gollum', 'Lost in Random', 'Lost Judgment', 'No More Heroes III', 'Outcast 2: A New Beginning', 'Paradise Lost', 'The Pathless', 'The Persistence Enhanced', 'Pragmata', 'The Riftbreaker', 'Saints Row', 'Saints Row: The Third Remastered', 'Shakedown: Hawaii', 'Skull and Bones', 'The Smurfs: Mission Vileaf', 'Solar Ash', 'Spacelords', "Marvel's Spider-Man 2", "Marvel's Spider-Man: Miles Morales", "Marvel's Spider-Man Remastered", 'Star Wars Jedi: Fallen Order', 'Star Wars Jedi: Survivor', 'Stellar Blade', 'Stonefly', 'Subnautica', 'Subnautica: Below Zero', 'Suicide Squad: Kill the Justice League', 'The Touryst', 'Trek to Yomi', 'Trifox', 'Unknown 9: Awakening', 'Watch Dogs: Legion']



def test_consols():
    with mock.patch.object(builtins, 'input', lambda _: 'ps5'):
        assert consols() == 'ps5'
    with mock.patch.object(builtins, 'input', lambda _: 'serie x'):
        assert consols() == 'serie x'    

    
     

def test_genres():
    with mock.patch.object(builtins, 'input', lambda _: 'Sports'):
        assert genres() == 'sports'
    with mock.patch.object(builtins, 'input', lambda _: 'horror'):
        assert genres() == 'horror'
    with mock.patch.object(builtins, 'input', lambda _: 'Horror'):
         assert genres() == 'horror'
    with mock.patch.object(builtins, 'input', lambda _: 'HoRrOr'):
         assert genres() == 'horror'        




    




def test_stat():
    dic = stat() 

    assert dic["age"] >= 18 or math.isnan(dic["age"]) == True
    assert dic["play_stations"] >= 0.00 and dic["play_stations"] <= 100.00 or math.isnan(dic["play_stations"]) == True
    assert dic["serie_x"] >= 0 and dic["serie_x"] <= 100.00 or math.isnan(dic["serie_x"]) == True
    assert dic["sports"] >= 0 and dic["sports"] <= 100.00  or math.isnan(dic["sports"]) == True
    assert dic["racing"] >= 0 and dic["racing"] <= 100.00 or math.isnan(dic["racing"]) == True
    assert dic["survival"] >= 0 and dic["survival"] <= 100.00 or math.isnan(dic["survival"]) == True
    assert dic["fight"] >= 0 and dic["fight"] <= 100.00 or math.isnan(dic["fight"]) == True
    assert dic["shooters"] >= 0 and dic["shooters"] <= 100.00   or math.isnan(dic["shooters"]) == True
    assert dic["action"] >= 0 and dic["action"] <= 100.00   or math.isnan(dic["action"]) == True
    assert dic["adventure"] >= 0 and dic["adventure"] <= 100.00 or math.isnan(dic["adventure"]) == True
    assert dic["horror"] >= 0 and dic["horror"] <= 100.00   or math.isnan(dic["horror"]) == True
    assert dic["stealth"] >= 0 and dic["stealth"] <= 100.00 or math.isnan(dic["stealth"]) == True
    
    




def test_users(monkeypatch):
    inputs = iter(['Frank', 'Red', '18'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = users()
    assert result == {"name": "Frank", "surname": "Red", "age": 18}



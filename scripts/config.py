missing_position_dict = {
    'Sead Kolasinac': 'LB|LWB|LW',
    'Matteo Guendouzi': 'CDM|CM',
    'Ezri Konsa Ngoyo': 'CB',
    'Ahmed El Mohamady': 'RB|CB',
    'Trézéguet': 'RM|RW|LW',
    'Jóhann Gudmundsson': 'RM|LM',
    'César Azpilicueta': 'RB|LB|CB',
    'Jairo Riedewald': 'LB|CB',
    'Gylfi Sigurdsson': 'CM|CAM',
    'Muhamed Besic': 'CM',
    'Jean Michael Seri': 'CDM|CM',
    'André-Frank Zambo Anguissa': 'CDM|CM',
    'Bobby De Cordova-Reid': 'ST|CM|LW',
    'Rodrigo Moreno': 'ST',
    'Joseph Gomez': 'RB|CB',
    'Naby Keita': 'CDM|CM',
    'Javier Manquillo': 'RWB|RB|LWB|RW|LW',
    'William Smallbone': 'CM|CAM',
    'Son Heung-Min': 'LW|LM|CF',
    'Branislav Ivanovic': 'RB|CB'
}

columns_to_remove_model = ['Club', 'Nationality', 'Age', 'Appearances', 'name', 'position']

model_path = "models/knn_model.pkl"
scaler_path = "models/scaler.pkl"
player_data_path = "data/player_data.csv"
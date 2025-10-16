us_recession_start_years= [1920,1923,1926, 1929, 1937, 1945,
                           1949, 1953, 1958, 1960, 1969, 1973, 1980, 1981,
                           1990, 2001, 2008, 2020]
total_recession_election_years = 0
for year in us_recession_start_years:
    if year%4==0:
        total_recession_election_years += 1
        print(f"{year} was both a recession and presidential election year")
print(f"there were {total_recession_election_years} recession and presidential election years in the last 100 years")
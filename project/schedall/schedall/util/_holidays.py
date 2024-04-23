import holidays

COUNTRIES = {
    "albania": ("Albania", "AL", "ALB"),
    "indonesia": ("Indonesia", "ID", "IDN"),
    "israel": ("Israel", "IL", "ISR"),
    "japan": ("Japan", "JP", "JPN"),
    "kenya": ("Kenya", "KE", "KEN"),
    "new_zealand": ("NewZealand", "NZ", "NZL"),
    "south_africa": ("SouthAfrica", "ZA", "ZAF"),
    "south_korea": ("SouthKorea", "KR", "KOR", "Korea"),
    "united_states": ("UnitedStates", "US", "USA"),
    "venezuela": ("Venezuela", "VE", "VEN")
}

def map_country_standard(country_name: str) -> str:
    for aliases in COUNTRIES.values():
        standard_name = aliases[0]
        if country_name.lower() in map(str.lower, aliases):
            return standard_name
    return None


def get_country_class(country_name: str):
    country_standard_name = map_country_standard(country_name)
    if country_standard_name:
        return getattr(holidays, country_standard_name)
    else:
        return None


# 국가와 연도를 입력 받고 휴무일을 출력하는 함수
def get_holidays(country_name: str, year: int):
    country_standard_name = map_country_standard(country_name)
    if country_standard_name == None:
        return None

    # Holiday.<Country> Class 호출
    country_holiday = getattr(holidays, country_standard_name)(years=year)
    # return country_holiday.items()

    print(country_holiday)
    
    if country_holiday:
        print(f"{year}년 {country_standard_name}의 휴무일:")
        for date, name in sorted(country_holiday.items()):
            print(date, name)
    else:
        print("해당 국가의 휴무일 정보를 찾을 수 없습니다.")


# Test Code
get_holidays('korea', 2024)  # 한국의 휴무일 출력
#print_holidays('usa', 2024)    # 미국의 휴무일 출력
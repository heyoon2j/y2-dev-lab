import holidays

# 국가와 연도를 입력으로 받아 해당 국가의 휴무일을 가져오는 함수
def get_holidays(country, year):
    countries = {
        'korea': holidays.Korea,
        '대한민국': holidays.Korea,
        'usa': holidays.US,
        'united states': holidays.US,
        # 여기에 다른 국가의 휴무일 정보를 추가할 수 있습니다.
    }
    
    country = country.lower()
    if country in countries:
        return countries[country](years=year)
    else:
        return None

# 국가와 연도를 입력 받고 휴무일을 출력하는 함수
def print_holidays(country, year):
    country_holidays = get_holidays(country, year)
    if country_holidays:
        print(f"{year}년 {country}의 휴무일:")
        for date, name in sorted(country_holidays.items()):
            print(date, name)
    else:
        print("해당 국가의 휴무일 정보를 찾을 수 없습니다.")

# 테스트를 위한 예시
print_holidays('korea', 2024)  # 한국의 휴무일 출력
print_holidays('usa', 2024)    # 미국의 휴무일 출력

class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박5일] 방콕, 파타야 여행 (야시장 투어) 50만원")


if __name__ == "__main__":
    print("Thailnad 모듈을 직접실행")
    print("이문장은 모듈을 직접 실행할때만 실행되요")
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print("Thailand 외부에서 모듈 호출")
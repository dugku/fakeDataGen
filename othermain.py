from faker import Faker


def makeData(HowMany, iteration):
    fak = Faker()
    lotsOfData = []

    for i in range(iteration):
        lotsOfData = []
        for x in range(0, HowMany):
            fakeName = fak.name()
            fakeAddy = fak.street_address() + " " +fak.city() + fak.city_suffix() + " " + fak.country_code() + " " + fak.postcode()
            fakePhone = fak.phone_number()
            fakeCCPro = fak.credit_card_provider()
            fakeCCNum = fak.credit_card_number()
            fakeCCExp = fak.credit_card_expire()
            fakess = fak.ssn()

            lotsOfData.append([fakeName, r'{}'.format(fakeAddy), fakePhone, f"{fakeCCPro} {fakeCCNum} {fakeCCExp}", fakess])

        with open(f"FakeData{i}.txt", "wt") as FakeData:
            for row in lotsOfData:
                FakeData.write(' '.join([str(item) for item in row]))
                FakeData.write('\n')


def makeFiles(amount):
    makeData(amount, 10)


makeFiles(1000000)

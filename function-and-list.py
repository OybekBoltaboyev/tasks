matnlar=['oybek ga', 'hikmat get', 'munisa yo\'qol']
# def bosh_harf(matnlar):
#     gaplar={}
#     while matnlar:
#         matn=matnlar.pop()
#         bh=matn.capitalize()
#         gaplar[matn]=bh
#     return gaplar
# matn=bosh_harf(matnlar[:])
# print(matn)
# print(matnlar)




def bahola(ismlar):
    baholar={}
    for ism in ismlar:
        baho=input(f"{ism.title()}ning bahosini kiriting: ")
        baholar[ism]=baho
    return baholar
talabalar=['ali','vali','hasan','husayin']
baholar=bahola(talabalar)
print(baholar)
print(talabalar)
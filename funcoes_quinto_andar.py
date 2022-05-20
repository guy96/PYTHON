import requests
import csv
from datetime import datetime

def abrirSite(num_banheiros, num_quartos, valor_maximo, bairro, zona_do_bairro):

    #url = 'https://glue-api.zapimoveis.com.br/v2/listings?bathrooms=' + str(num_banheiros) + '&bedrooms=' + str(num_quartos) + '&business=RENTAL&parkingSpaces=1&priceMax=' + str(valor_maximo) + '&categoryPage=RESULT&parentId=null&listingType=USED&portal=ZAP&unitSubTypes=UnitSubType_NONE,DUPLEX,TRIPLEX&unitTypes=APARTMENT&usageTypes=RESIDENTIAL&unitTypesV3=APARTMENT&text=Apartamento&addressCountry=&addressState=Rio+de+Janeiro&addressCity=Rio+de+Janeiro&addressZone=' + zona_do_bairro.replace(" ", "+") + '&addressNeighborhood=' + bairro.replace(" ", "+") + '&addressStreet=&addressAccounts=&addressType=neighborhood&addressLocationId=BR>Rio+de+Janeiro>NULL>Rio+de+Janeiro>Zona+Sul>Leme&addressPointLat=-22.969442&addressPointLon=-43.186845&addressUrl=/aluguel/apartamentos/rj+rio-de-janeiro+zona-sul+leme/&size=24&from=0&page=1&includeFields=search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,stamps,createdAt,floors,unitTypes,nonActivationReason,providerId,propertyType,unitSubTypes,unitsOnTheFloor,legacyId,id,portal,unitFloor,parkingSpaces,updatedAt,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,advertiserContact,whatsappNumber,bedrooms,acceptExchange,pricingInfos,showPrice,resale,buildings,capacityLimit,status,priceSuggestion),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,legacyZapId,minisite),medias,accountLink,link)),totalCount),expansion(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,stamps,createdAt,floors,unitTypes,nonActivationReason,providerId,propertyType,unitSubTypes,unitsOnTheFloor,legacyId,id,portal,unitFloor,parkingSpaces,updatedAt,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,advertiserContact,whatsappNumber,bedrooms,acceptExchange,pricingInfos,showPrice,resale,buildings,capacityLimit,status,priceSuggestion),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,legacyZapId,minisite),medias,accountLink,link)),totalCount)),nearby(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,stamps,createdAt,floors,unitTypes,nonActivationReason,providerId,propertyType,unitSubTypes,unitsOnTheFloor,legacyId,id,portal,unitFloor,parkingSpaces,updatedAt,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,advertiserContact,whatsappNumber,bedrooms,acceptExchange,pricingInfos,showPrice,resale,buildings,capacityLimit,status,priceSuggestion),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,legacyZapId,minisite),medias,accountLink,link)),totalCount)),page,fullUriFragments,developments(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,stamps,createdAt,floors,unitTypes,nonActivationReason,providerId,propertyType,unitSubTypes,unitsOnTheFloor,legacyId,id,portal,unitFloor,parkingSpaces,updatedAt,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,advertiserContact,whatsappNumber,bedrooms,acceptExchange,pricingInfos,showPrice,resale,buildings,capacityLimit,status,priceSuggestion),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,legacyZapId,minisite),medias,accountLink,link)),totalCount)),superPremium(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,stamps,createdAt,floors,unitTypes,nonActivationReason,providerId,propertyType,unitSubTypes,unitsOnTheFloor,legacyId,id,portal,unitFloor,parkingSpaces,updatedAt,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,advertiserContact,whatsappNumber,bedrooms,acceptExchange,pricingInfos,showPrice,resale,buildings,capacityLimit,status,priceSuggestion),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,legacyZapId,minisite),medias,accountLink,link)),totalCount)),owners(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,stamps,createdAt,floors,unitTypes,nonActivationReason,providerId,propertyType,unitSubTypes,unitsOnTheFloor,legacyId,id,portal,unitFloor,parkingSpaces,updatedAt,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,advertiserContact,whatsappNumber,bedrooms,acceptExchange,pricingInfos,showPrice,resale,buildings,capacityLimit,status,priceSuggestion),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,legacyZapId,minisite),medias,accountLink,link)),totalCount))&cityWiseStreet=1&developmentsSize=3&superPremiumSize=3&levels=NEIGHBORHOOD&ref=/aluguel/apartamentos/rj+rio-de-janeiro+zona-sul+leme/'

    url = 'https://glue-api.zapimoveis.com.br/v2/listings?bathrooms=' + str(num_banheiros) + '&bedrooms=' + str(num_quartos) + '&business=RENTAL&parkingSpaces=1&priceMax=' + str(valor_maximo) + '&categoryPage=RESULT&parentId=null&listingType=USED&portal=ZAP&unitSubTypes=UnitSubType_NONE,DUPLEX,TRIPLEX&unitTypes=APARTMENT&usageTypes=RESIDENTIAL&unitTypesV3=APARTMENT&text=Apartamento&addressCountry=&addressState=Rio+de+Janeiro&addressCity=Rio+de+Janeiro&addressZone=' + zona_do_bairro.replace(" ", "+") + '&addressNeighborhood=' + bairro.replace(" ", "+") + '&addressStreet=&addressAccounts=&addressType=neighborhood'



    headers = {
        "Accept": "application/json, text/plain, */*",
        "Referer": "https://www.zapimoveis.com.br/",
        "sec-ch-ua": '"Chromium";v="96", "Opera";v="82", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": '?0',
        "sec-ch-ua-platform": "macOS",
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 OPR/82.0.4227.43',
        "X-Domain": 'www.zapimoveis.com.br'
    }

    x = requests.get(url, headers=headers)

    
    # Retorna um json
    return x.json()



def limparRequisicao(mensagem, indice):
    # Recebe um JSON, agora vamos limpar o que a gente recebeu

    preco_total = int(mensagem["search"]["result"]["listings"][indice]["listing"]["pricingInfos"][0]["rentalInfo"]["monthlyRentalTotalPrice"])
    
    numero_de_quartos = mensagem["search"]["result"]["listings"][indice]["listing"]["bedrooms"][0]

    numero_de_banheiros = mensagem["search"]["result"]["listings"][indice]["listing"]["bathrooms"][0]

    vagas_de_garagem = mensagem["search"]["result"]["listings"][indice]["listing"]["parkingSpaces"][0]

    link = "https://www.zapimoveis.com.br" + mensagem["search"]["result"]["listings"][indice]["link"]["href"]

    """
    print("SOBRE ESSE APARTAMENTO......")
    print("Valor total: \tR$ " + str(preco_total))
    print("Num. de quartos: \t" + str(numero_de_quartos))
    print("Num. de banheiros: \t" + str(numero_de_banheiros))
    print("Num. de vagas: \t" + str(vagas_de_garagem))
    print("Link: \t" + link)
    print("\n\n")
    """

    now = datetime.now()
    data_pesquisa = now.strftime("%d/%m/%Y %H:%M:%S")

    lista = [data_pesquisa, preco_total, numero_de_quartos, numero_de_banheiros, vagas_de_garagem, link]

    print(lista)
    return lista

def verTodosApartamentos(mensagem):

    lista_final = []

    apartamentos = mensagem["search"]["result"]["listings"]

    for apartamento in range(len(apartamentos)):
        lista_final.append(limparRequisicao(mensagem, apartamento))

    fields = ['Data Pesquisa', 'Preco Total', '#Quartos', '#Banheiros', '#Vagas', 'Link']

    rows = lista_final

    with open('resultado.csv', 'a+') as f:
        # using csv.writer method from CSV package
        write = csv.writer(f)
        
        reader = csv.reader(f)
        lines = len(list(reader))
        
        print(lines)
        if lines == 0:
            write.writerow(fields)
        write.writerows(rows)






def main():
    return 0


if __name__ == "__main__":
    main()



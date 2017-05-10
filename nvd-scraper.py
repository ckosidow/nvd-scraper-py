from lxml import html
import requests
import csv

with open('dependencies.csv') as csvfile:
    dependencyReader = csv.reader(csvfile)

    for row in dependencyReader:
        query = "".join(row)

        page = requests.get(
            "https://nvd.nist.gov/vuln/search/results?adv_search=false&form_type=basic&results_type=overview&search_type=last3months&query=" + query)
        tree = html.fromstring(page.content)

        resultTable = tree.xpath('//table[@data-testid="vuln-results-table"]//tbody//tr//th//a/@href')

        for result in resultTable:
            print(query + " - https://nvd.nist.gov" + result)

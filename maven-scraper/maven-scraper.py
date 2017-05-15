from lxml import html
import requests
import csv

with open('dependencies.csv') as csvfile:
    with open('out.csv', 'w', newline='') as outFile:
        vulnWriter = csv.writer(outFile)
        dependencyReader = csv.reader(csvfile)

        for row in dependencyReader:
            dependency = "".join(row)
            mavenArtifact = "https://mvnrepository.com/artifact/" + dependency

            page = requests.get(mavenArtifact)
            tree = html.fromstring(page.content)

            resultTable = tree.xpath('//table[@class="grid versions"]/tbody/tr[td/a[@href="/repos/central"][1]]/td/a/@href')

            if resultTable:
                for result in resultTable[:1]:
                    vulnWriter.writerow([dependency, "URL: " + mavenArtifact, result])

                    print(dependency + " - " + result)
            else:
                vulnWriter.writerow([dependency, mavenArtifact])

                print(dependency + " -")
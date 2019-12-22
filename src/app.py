import sys
import time
import clearbit
import ukgov
import csvhandler

def main():
    url = "https://www.gov.uk/government/publications/tier-2-employers-in-the-health-care-sector/list-of-tier-2-employers-in-the-health-care-sector-categorised-by-region-and-the-industry-sectors" #input("gov.uk url: ")

    print("Fetching Company Names...")
    company_list = ukgov.get_company_credentials(url)

    credentials_list = []

    print("Fetching Company Email Addresses...")
    counter = 0
    length = len(company_list)
    start = time.time()

    #Debugging
    #company_credentials = clearbit.autocomplete(company_list[255][0])
    #print(company_credentials)

    #exit()

    print(f"This will take approximately {length*0.3/60} Minutes")
    print(f"(0/{length})")
    for company in company_list:
        company_name = company[0]
        company_credentials = clearbit.autocomplete(company_name)

        credentials_list.append(company_credentials)
        counter += 1
        if(counter%5 == 0):
            print(f"({counter}/{length})")
        time.sleep(.1)

    combined_list, empty_list = csvhandler.combine_lists(company_list, credentials_list)
    csvhandler.write_to_csv(combined_list, path="output.csv")
    csvhandler.write_to_csv(empty_list, path="empty.csv")
    end = time.time()

    print(f"This operation took {round((end-start)*10)/10} seconds")


if __name__ == "__main__":
    main()

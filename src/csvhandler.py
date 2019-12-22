import csv

def combine_lists(names, creds):
    combined_list = [["Search Name", "Region", "Found Name", "Website"]]
    empty_list = [["Search Name", "Region"]]

    print(names)
    print(creds)

    for i in range(len(names)):
        cred_list = creds[i]
        if len(cred_list) == 0:
            name = names[i][0]
            region = names[i][2]
            empty_list.append([name, region])
        else:
            for cred in cred_list:
                name = names[i][0]
                region = names[i][2]
                foundname = cred["name"]
                domain = cred["domain"]
                combined_list.append([name, region, foundname, domain])

    return (combined_list, empty_list)


def write_to_csv(list, path="ouput.csv"):
    with open(path, "w") as file:
        writer = csv.writer(file)
        writer.writerows(list)

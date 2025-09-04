import csv # For reading CSV files
import pandas as pd # For data manipulation and analysis


# defining class university
class University:
   
    def __init__(university, name, country, overall_score, world_rank, year):
        university.name = name
        university.country = country
        university.overall_score = float(overall_score)
        university.world_rank = int(world_rank)
        university.year = int(year)

    def display_info(university):
        print(f"  Name: {university.name} ({university.year})")
        print(f"  Country: {university.country}")
        print(f"  World Rank: {university.world_rank}")
        print(f"  Score: {university.overall_score:.2f}")
        print("-" * 30)

# function definitions
def load_university_data(filepath="cwurData.csv"):

         # LIST
         #A list is created here to store all the University objects we create.
    universities_list = []
    try:
        with open(filepath, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            # loop
            for row in reader:
                try:
                    uni_object = University(
                        name=row['institution'],
                        country=row['country'],
                        overall_score=row['score'],
                        world_rank=row['world_rank'],
                        year=row['year']
                    )

                    ## LIST
                # The .append() method adds the newly created object to our list.
                    universities_list.append(uni_object)
                except (ValueError, KeyError):
                 pass
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        print("Please make sure it is in the same directory as this Python script.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    return universities_list
def group_and_rank_by_country(universities_list):
    
    grouped_data = {}

    ##  LOOP
     # This 'for' loop iterates over the list of universities passed into the function.
    
    for uni in universities_list:
        country = uni.country

        # if statement
        # This 'if' statement checks if the country name is already a key in our dictionary.
        # This is the core logic for grouping the data.
        if country not in grouped_data:
            grouped_data[country] = []
        grouped_data[country].append(uni)
        
    for country, unis in grouped_data.items():
        unis.sort(key=lambda u: u.world_rank)
        
    return grouped_data

# main execution
if __name__ == "__main__":
    print(" World University Rankings Analysis ")
    
    # Load all university data from the CSV file.
    all_universities = load_university_data()

    if all_universities:
        print(f"\nSuccessfully loaded data for {len(all_universities)} valid university entries.")

        # Filter the master list to get only the data for the year 2015.
        universities_2015 = []
        for uni in all_universities:
            if uni.year == 2015:
                universities_2015.append(uni)
        
        print(f"Found {len(universities_2015)} entries for the year 2015.")
        
        #  Group the filtered 2015 data by country.
        ranked_by_country_2015 = group_and_rank_by_country(universities_2015)

        #  Display the top 5 universities for a selection of countries.
        countries_to_display = ["USA", "United Kingdom", "Canada", "Germany", 
                                "Japan","France","Switzerland",
                                "Australia","Italy","Netherlands"]
        
        for country in countries_to_display:
            if country in ranked_by_country_2015:
                print(f"\n--- Top 10 Universities in {country} (2015) ---")
                top_universities = ranked_by_country_2015[country]

                # LOOP 
                # This 'for' loop iterates 5 times (or fewer if a country has less than 5 universities).
                # It is used to display only the top 5 results for each country.
                
                for i in range(min(10, len(top_universities))):
                    uni = top_universities[i]
                    print(f"National Rank: {i+1}")
                    uni.display_info()
            else:
                print(f"\n--- No data found for {country} in 2015 ---")
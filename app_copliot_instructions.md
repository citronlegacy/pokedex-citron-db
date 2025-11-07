Create a Python library called pokedex_citron_db that uses a CSV file named "pokedex_db.csv" as its database. The CSV file has the following columns:
"number", "name", "primary_type", "secondary_type", "generation", "mega_evolution", "legendary", "final_stage", "regional_form".
true values are 1, false values are 0.

The library should provide the following functions:

search_by_name(name: str) -> dict

Takes a Pokémon name as input and returns a dictionary with metadata for that Pokémon. It wont return false values. For example if "legendary" is false it wont return this data. 

Returns None if the Pokémon is not found.

ispokemon(name: str) -> bool

Returns True if the input string is a valid Pokémon name in the CSV, otherwise False.

get_by_primary_type(primary_type: str) -> list

Returns a list of Pokémon names that have the specified primary type.

get_by_secondary_type(secondary_type: str) -> list

Returns a list of Pokémon names that have the specified secondary type.

get_all_megas() -> list

Returns a list of all Pokémon that have a mega evolution (i.e., the mega_evolution column is not empty or null).

get_all_regional_forms() -> list

Returns a list of all Pokémon that have a regional form (i.e., the regional_form column is not empty or null).

get_all_legendaries() -> list

Returns a list of all Pokémon where the legendary column indicates it is legendary.

The library should load the CSV once when imported and store it in memory for quick access. Use Python’s built-in csv module or pandas for handling the CSV. Make sure to include proper error handling for missing or malformed CSV files. 

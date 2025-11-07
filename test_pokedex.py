"""
Test script for the pokedex_citron_db library
"""

from pokedex_citron_db import (
    search_by_name,
    ispokemon,
    get_by_primary_type,
    get_by_secondary_type,
    get_all_megas,
    get_all_regional_forms,
    get_all_legendaries
)

def print_section(title):
    """Print a section header."""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")


def test_search_by_name():
    print_section("Testing search_by_name()")
    
    # Test regular Pokémon
    print("\nSearching for 'Pikachu':")
    print(search_by_name("Pikachu"))
    
    # Test legendary Pokémon
    print("\nSearching for 'Mewtwo':")
    print(search_by_name("Mewtwo"))
    
    # Test Pokémon with mega evolution
    print("\nSearching for 'Charizard':")
    print(search_by_name("Charizard"))
    
    # Test Pokémon with regional form
    print("\nSearching for 'Raichu':")
    print(search_by_name("Raichu"))
    
    # Test non-existent Pokémon
    print("\nSearching for 'Fakemon':")
    print(search_by_name("Fakemon"))

    # Test: Raticate should return regional_form in metadata
    print("\nSearching for 'Raticate':")
    raticate = search_by_name("Raticate")
    print(raticate)
    assert raticate is not None, "Raticate not found!"
    assert 'regional_form' in raticate and raticate['regional_form'], "Raticate should have a regional_form in metadata!"


def test_ispokemon():
    print_section("Testing ispokemon()")
    
    tests = ["Pikachu", "Charizard", "Fakemon", "mewtwo", "BULBASAUR"]
    
    for name in tests:
        result = ispokemon(name)
        print(f"Is '{name}' a Pokémon? {result}")


def test_get_by_primary_type():
    print_section("Testing get_by_primary_type()")
    
    types = ["Fire", "Water", "Psychic", "Dragon"]
    
    for ptype in types:
        pokemon = get_by_primary_type(ptype)
        print(f"\n{ptype} type Pokémon ({len(pokemon)}):")
        print(f"  {', '.join(pokemon)}")


def test_get_by_secondary_type():
    print_section("Testing get_by_secondary_type()")
    
    types = ["Flying", "Dragon", "Poison", "Steel"]
    
    for stype in types:
        pokemon = get_by_secondary_type(stype)
        print(f"\n{stype} as secondary type ({len(pokemon)}):")
        print(f"  {', '.join(pokemon)}")


def test_get_all_megas():
    print_section("Testing get_all_megas()")
    
    megas = get_all_megas()
    print(f"\nPokémon with Mega Evolutions ({len(megas)}):")
    print(f"  {', '.join(megas)}")
    # Test: Charizard should be in the list of mega Pokémon
    assert any(name.lower() == "charizard" for name in megas), "Charizard should be in the list of mega Pokémon!"
    # Test: There should be 47 mega Pokémon
    assert len(megas) == 47, f"Expected 47 mega Pokémon, found {len(megas)}"


def test_get_all_regional_forms():
    print_section("Testing get_all_regional_forms()")
    
    regional = get_all_regional_forms()
    print(f"\nPokémon with Regional Forms ({len(regional)}):")
    print(f"  {', '.join(regional)}")
    # Test: Vulpix should be in the list of Pokémon with regional variants
    assert any(name.lower() == "vulpix" for name in regional), "Vulpix should be in the list of Pokémon with regional variants!"
    # Test: There should be 52 regional form Pokémon
    assert len(regional) == 52, f"Expected 52 regional form Pokémon, found {len(regional)}"


def test_get_all_legendaries():
    print_section("Testing get_all_legendaries()")
    
    legendaries = get_all_legendaries()
    print(f"\nLegendary Pokémon ({len(legendaries)}):")
    print(f"  {', '.join(legendaries)}")
    # Test: There should be 105 legendary Pokémon (matches current CSV)
    assert len(legendaries) == 105, f"Expected 105 legendary Pokémon, found {len(legendaries)}"



if __name__ == "__main__":
    print("\n" + "="*60)
    print("  POKEDEX CITRON DB - TEST SUITE")
    print("="*60)

    test_funcs = [
        ("search_by_name", test_search_by_name),
        ("ispokemon", test_ispokemon),
        ("get_by_primary_type", test_get_by_primary_type),
        ("get_by_secondary_type", test_get_by_secondary_type),
        ("get_all_megas", test_get_all_megas),
        ("get_all_regional_forms", test_get_all_regional_forms),
        ("get_all_legendaries", test_get_all_legendaries),
    ]

    passed = 0
    failed = 0
    failed_tests = []

    for name, func in test_funcs:
        try:
            func()
            passed += 1
        except AssertionError as e:
            print(f"\n[FAILED] {name}: {e}")
            failed += 1
            failed_tests.append((name, str(e)))
        except Exception as e:
            print(f"\n[ERROR] {name}: {e}")
            failed += 1
            failed_tests.append((name, str(e)))

    print("\n" + "="*60)
    print(f"  TEST SUMMARY: {passed} passed / {passed + failed} total")
    if failed_tests:
        print("  Failed tests:")
        for name, msg in failed_tests:
            print(f"    - {name}: {msg}")
    print("="*60 + "\n")

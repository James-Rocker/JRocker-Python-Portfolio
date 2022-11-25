from types import MappingProxyType

# mapping proxy types are immutable dicts
my_first_mapping_proxy_type = MappingProxyType(
    {
        "Terry": "Pokemon",
        "Gabu": "Digimon",
    }
)

print(my_first_mapping_proxy_type)

# we can still get keys and values
print(my_first_mapping_proxy_type.keys())
print(my_first_mapping_proxy_type.values())

# However, tying to update a value results in an error
my_first_mapping_proxy_type["Terry"] = "Tamagochi"
print(my_first_mapping_proxy_type)


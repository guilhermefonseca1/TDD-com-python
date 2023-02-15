from load_json import load_json
import pytest
from unittest.mock import patch, mock_open
import json

def test_load_json_checks_filetype():
    with pytest.raises(ValueError):
        load_json('data/pokemons.csv')

def test_load_json_checks_file_exists():
    with pytest.raises(MissingFileException):
        load_json('pokemons.json')

@pytest.fixture
def fake_pokemon_data(): 
    return [
    {
      "national_number": "001",
      "evolution": null,
      "sprites": {
        "normal": "https://img.pokemondb.net/sprites/omega-ruby-alpha-sapphire/dex/normal/bulbasaur.png",
        "large": "https://img.pokemondb.net/artwork/bulbasaur.jpg",
        "animated": "https://img.pokemondb.net/sprites/black-white/anim/normal/bulbasaur.gif"
      },
      "name": "Bulbasaur",
      "type": [
        "Grass",
        "Poison"
      ],
      "total": 318,
      "hp": 45,
      "attack": 49,
      "defense": 49,
      "sp_atk": 65,
      "sp_def": 65,
      "speed": 45
    },
    {
      "national_number": "002",
      "evolution": null,
      "sprites": {
        "normal": "https://img.pokemondb.net/sprites/omega-ruby-alpha-sapphire/dex/normal/ivysaur.png",
        "large": "https://img.pokemondb.net/artwork/ivysaur.jpg",
        "animated": "https://img.pokemondb.net/sprites/black-white/anim/normal/ivysaur.gif"
      },
      "name": "Ivysaur",
      "type": [
        "Grass",
        "Poison"
      ],
      "total": 405,
      "hp": 60,
      "attack": 62,
      "defense": 63,
      "sp_atk": 80,
      "sp_def": 80,
      "speed": 60
    },
    ]

def test_load_json_checks_open_file(fake_pokemon_data):
    fake_json = json.dumps(fake_pokemon_data)
    with patch("builtins.open", mock_open(read_data=fake_json)):
        result = load_json('data/arquivoquenaoexiste.json')

        assert type(result) == list
        assert len(result) == len(fake_pokemon_data)
        assert result == fake_pokemon_data
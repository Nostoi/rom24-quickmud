from mud.world import initialize_world, create_test_character
from mud.agent.character_agent import CharacterAgentAdapter
from mud.spawning.mob_spawner import spawn_mob
from mud.registry import room_registry


def test_character_agent_actions():
    initialize_world('area/area.lst')
    char = create_test_character('Tester', 3001)
    adapter = CharacterAgentAdapter(char)
    obs = adapter.get_observation()
    assert obs['name'] == 'Tester'
    assert obs['room']['vnum'] == 3001

    say_result = adapter.perform_action('say', ['hello'])
    assert 'You say' in say_result

    move_result = adapter.perform_action('move', ['north'])
    assert 'north' in move_result
    assert char.room.vnum != 3001


def test_mob_agent_movement():
    initialize_world('area/area.lst')
    mob = spawn_mob(3000)
    room = room_registry[3001]
    room.add_mob(mob)
    adapter = CharacterAgentAdapter(mob)
    move_result = adapter.perform_action('move', ['north'])
    assert mob.room.vnum != 3001
    assert 'north' in move_result

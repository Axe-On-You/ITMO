package mypokemons;

import mymoves.slakoth.Scratch;
import mymoves.slakoth.Thunderbolt;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;

public class Slakoth extends Pokemon {

    public Slakoth (String name, int level) {
        super(name, level);

        super.setType(Type.NORMAL);

        super.setStats(60, 60, 60, 35, 35, 30);

        Scratch scratch = new Scratch(40, 100);
        Thunderbolt thunderbolt = new Thunderbolt(90, 100);

        super.setMove(scratch, thunderbolt);
    }
}

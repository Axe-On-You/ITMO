package mypokemons;

import mymoves.slakoth.FocusEnergy;
import mymoves.slakoth.Scratch;
import mymoves.slakoth.Thunderbolt;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;

public class Vigoroth extends Pokemon {

    public Vigoroth (String name, int level) {
        super(name, level);

        super.setType(Type.NORMAL);

        super.setStats(80, 80, 80, 55, 55, 90);

        Scratch scratch = new Scratch(40, 100);
        Thunderbolt thunderbolt = new Thunderbolt(90, 100);
        FocusEnergy focusEnergy = new FocusEnergy(0, 0);

        super.setMove(scratch, thunderbolt, focusEnergy);
    }
}

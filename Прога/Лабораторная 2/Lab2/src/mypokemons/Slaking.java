package mypokemons;

import mymoves.slakoth.FocusEnergy;
import mymoves.slakoth.IceBeam;
import mymoves.slakoth.Scratch;
import mymoves.slakoth.Thunderbolt;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;

public class Slaking extends Pokemon {

    public Slaking (String name, int level) {
        super(name, level);

        super.setType(Type.NORMAL);

        super.setStats(150, 160, 100, 95, 65, 100);

        Scratch scratch = new Scratch(40, 100);
        Thunderbolt thunderbolt = new Thunderbolt(90, 100);
        FocusEnergy focusEnergy = new FocusEnergy(0, 0);
        IceBeam iceBeam = new IceBeam(90, 100);

        super.setMove(scratch, thunderbolt, focusEnergy, iceBeam);
    }
}

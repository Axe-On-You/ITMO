package mymoves.spiritomb;

import lab2.Program;
import ru.ifmo.se.pokemon.Effect;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.SpecialMove;
import ru.ifmo.se.pokemon.Type;

public class DarkPulse extends SpecialMove {

    // https://pokemondb.net/move/dark-pulse

    public DarkPulse(double pow, double acc) {
        super(Type.DARK, pow, acc);
    }

    @Override
    protected void applyOppEffects(Pokemon p) {
        super.applyOppEffects(p);

        if(Program.chance(0.2)) {
            Effect.flinch(p);

            System.out.println(p + " вздрогнул");
        }
    }

    @Override
    protected String describe() {
        String[] pieces = this.getClass().toString().split("\\.");
        return "использует " + pieces[pieces.length-1];
    }

}

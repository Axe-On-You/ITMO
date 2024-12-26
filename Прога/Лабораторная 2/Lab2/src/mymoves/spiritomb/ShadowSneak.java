package mymoves.spiritomb;

import ru.ifmo.se.pokemon.PhysicalMove;
import ru.ifmo.se.pokemon.Type;

public class ShadowSneak extends PhysicalMove {

    // https://pokemondb.net/move/shadow-sneak

    public ShadowSneak(double pow, double acc, int priority, int hits) {
        super(Type.GHOST, pow, acc, priority, hits);
    }

    @Override
    protected String describe() {
        String[] pieces = this.getClass().toString().split("\\.");
        return "использует " + pieces[pieces.length-1];
    }
}

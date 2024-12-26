package mymoves.bonsly;

import ru.ifmo.se.pokemon.PhysicalMove;
import ru.ifmo.se.pokemon.Type;

public class FeintAttack extends PhysicalMove {

    // https://pokemondb.net/move/feint-attack

    public FeintAttack(double pow, double acc) {
        super(Type.DARK, pow, acc);
    }

    @Override
    protected String describe() {
        String[] pieces = this.getClass().toString().split("\\.");
        return "использует " + pieces[pieces.length-1];
    }
}

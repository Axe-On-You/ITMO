package mymoves.bonsly;

import ru.ifmo.se.pokemon.PhysicalMove;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;

public class DoubleEdge extends PhysicalMove {

    // https://pokemondb.net/move/double-edge

    public DoubleEdge(double pow, double acc) {
        super(Type.NORMAL, pow, acc);
    }

    @Override
    protected void applySelfDamage(Pokemon att, double damage) {
        double selfDamage = damage / 3;
        super.applySelfDamage(att, selfDamage);
    }

    @Override
    protected String describe() {
        String[] pieces = this.getClass().toString().split("\\.");
        return "использует " + pieces[pieces.length-1];
    }
}
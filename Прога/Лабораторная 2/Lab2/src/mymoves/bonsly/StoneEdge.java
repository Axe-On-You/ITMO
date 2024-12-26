package mymoves.bonsly;

import lab2.Program;
import ru.ifmo.se.pokemon.PhysicalMove;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Stat;
import ru.ifmo.se.pokemon.Type;

public class StoneEdge extends PhysicalMove {

    // https://pokemondb.net/move/stone-edge

    public StoneEdge(double pow, double acc) {
        super(Type.ROCK, pow, acc);
    }

    @Override
    protected double calcCriticalHit(Pokemon att, Pokemon def) {
        if (Program.chance(3 * att.getStat(Stat.SPEED) / 512.0)) {
            return 2.0;
        } else {
            return 1.0;
        }
    }

    @Override
    protected String describe() {
        String[] pieces = this.getClass().toString().split("\\.");
        return "использует " + pieces[pieces.length-1];
    }
}

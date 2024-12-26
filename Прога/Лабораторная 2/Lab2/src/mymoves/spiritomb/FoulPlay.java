package mymoves.spiritomb;

import ru.ifmo.se.pokemon.PhysicalMove;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Stat;
import ru.ifmo.se.pokemon.Type;

public class FoulPlay extends PhysicalMove {

    // https://pokemondb.net/move/foul-play

    public FoulPlay(double pow, double acc) {
        super(Type.DARK, pow, acc);
    }

    @Override
    protected double calcBaseDamage(Pokemon att, Pokemon def) {
        return def.getStat(Stat.ATTACK);
    }

    @Override
    protected void applyOppDamage(Pokemon def, double damage) {
        double calculatedDamage = calcBaseDamage(def, def);
        super.applyOppDamage(def, calculatedDamage);
    }

    @Override
    protected String describe() {
        String[] pieces = this.getClass().toString().split("\\.");
        return "использует " + pieces[pieces.length-1];
    }
}

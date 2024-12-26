package mymoves.bonsly;

import ru.ifmo.se.pokemon.*;

public class Confide extends StatusMove {

    // https://pokemondb.net/move/confide

    public Confide(double pow, double acc) {
        super(Type.NORMAL, pow, acc);
    }

    @Override
    protected void applyOppEffects(Pokemon p) {
        Effect e = new Effect().stat(Stat.SPECIAL_DEFENSE, -1);
        p.addEffect(e);

        System.out.println("У " + p + " специальная защита снижена на 1");
    }

    @Override
    protected String describe() {
        String[] pieces = this.getClass().toString().split("\\.");
        return "использует " + pieces[pieces.length-1];
    }
}

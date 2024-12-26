package mymoves.spiritomb;

import ru.ifmo.se.pokemon.*;

public class Swagger extends StatusMove {

    // https://pokemondb.net/move/swagger

    public Swagger(double pow, double acc) {
        super(Type.NORMAL, pow, acc);

    }

    @Override
    protected void applyOppEffects(Pokemon p) {
        super.applyOppEffects(p);

        Effect.confuse(p);

        System.out.println(p + " был сбит с толку");
    }

    @Override
    protected void applySelfEffects(Pokemon p) {
        super.applySelfEffects(p);

        Effect e = new Effect().stat(Stat.ATTACK, 2);

        p.addEffect(e);

        System.out.println(p + " повышает атаку на 2");
    }

    @Override
    protected String describe() {
        String[] pieces = this.getClass().toString().split("\\.");
        return "использует " + pieces[pieces.length-1];
    }

}

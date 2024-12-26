package mypokemons;

import mymoves.bonsly.*;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;

public class Bonsly extends Pokemon {

    public Bonsly(String name, int level) {
        super(name, level);

        super.setType(Type.ROCK);

        super.setStats(50, 80, 95, 10, 45, 10);

        DoubleEdge doubleEdge = new DoubleEdge(120, 100);
        FeintAttack feintAttack = new FeintAttack(60, Double.POSITIVE_INFINITY);
        Confide confide = new Confide(0, Double.POSITIVE_INFINITY);

        super.setMove(doubleEdge, feintAttack, confide);
    }
}

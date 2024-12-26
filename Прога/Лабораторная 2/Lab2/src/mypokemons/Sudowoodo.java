package mypokemons;

import mymoves.bonsly.Confide;
import mymoves.bonsly.DoubleEdge;
import mymoves.bonsly.FeintAttack;
import mymoves.bonsly.StoneEdge;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;

public class Sudowoodo extends Pokemon {

    public Sudowoodo(String name, int level) {
        super(name, level);

        super.setType(Type.ROCK);

        super.setStats(70, 100, 115, 30, 65, 30);

        DoubleEdge doubleEdge = new DoubleEdge(120, 100);
        FeintAttack feintAttack = new FeintAttack(60, Double.POSITIVE_INFINITY);
        Confide confide = new Confide(0, Double.POSITIVE_INFINITY);
        StoneEdge stoneEdge = new StoneEdge(100, 80);

        super.setMove(doubleEdge, feintAttack, confide, stoneEdge);
    }
}
